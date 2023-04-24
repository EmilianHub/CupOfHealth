import os
import pickle
import random
from math import ceil

import numpy as np
import openai
import spacy
from dotenv import load_dotenv
from keras.models import load_model
from sqlalchemy import select, func

import diseaseCache
import jwtService
from localizationJPA import Localization
from chorobyJPA import Diseases
from dbConnection import db_session
from profJPA import Prof
from responsesJPA import Responses
from tagGroup import TagGroup
from userService import UserService
from wikipediaService import findFunFactWithMessage

load_dotenv()
model = load_model('chatbot_model.h5')
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
userService = UserService()
nlp = spacy.load("pl_core_news_md")
openai.api_key = os.getenv("OPENAI_KEY")
stopword = nlp.Defaults.stop_words


def clean_up_sentence(sentence):
    tokenizedWord = nlp(sentence)
    sentence_words = [token.lemma_.lower() for token in tokenizedWord]
    return set(sentence_words)


# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence


def bow(sentence, show_details=True):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words - matrix of N words, vocabulary matrix
    bag = [0] * len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                # assign 1 if current word is in the vocabulary position
                bag[i] = 1
                if show_details:
                    print("found in bag: %s" % w)
    return np.array(bag)


def predict_class(sentence):
    # filter out predictions below a threshold
    p = bow(sentence, show_details=True)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.1
    results = [[i, r] for i, r in enumerate(res) if r >= ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list


def generate_chat_response(message):
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=message,
        temperature=0.8,
        max_tokens=100
    )
    return response.choices[0].text


def getOpisChoroby(msg):
    return generate_chat_response(msg)  # Generowanie odpowiedzi


def getResponse(ints, msg):
    if len(ints) == 0 and diseaseCache.suggestCure:
        return suggestCure(msg)
    elif len(ints) != 0:
        tag = ints[0]['intent']

        if tag.startswith("leczenie"):
            return showLeczenie(tag)
        if tag.startswith("opis"):
            return getOpisChoroby(msg)
        if tag.startswith("lokalizacja"):
            return getchorobaforplace(tag)
        if isCasualResponse(tag):
            return retrieveCausalResponse(tag)

        return retrieveDisesaseResponse(ints, msg)

    return findFunFactWithMessage(msg)


def isCasualResponse(tag):
    pFilter = filter(lambda t: t == tag, TagGroup.fetch_names())

    return len(list(pFilter)) != 0


def retrieveCausalResponse(tag):
    if tag == TagGroup.end_diagnosis.value:
        if len(diseaseCache.matching) != 0:
            return retrieveDiseaseResponse(None, True)
        return "Niestety nie podałeś mi żadnych objawów, na podstawie których mógłbym określić twoją przypadłość"

    response = findResponseWithTagGroup(tag)

    if response is not None:
        choice = random.choice(response)
        diseaseCache.assignReponseMessageId(choice.id)
        return choice.response

    return "Przepraszam nie mam na to odpowiedzi"


def retrieveDisesaseResponse(ints, msg):
    diseaseCache.addToMsgCache(msg)

    for i in ints:
        diseaseCache.addToMatchingCache(msg, i['intent'])

    return retrieveDiseaseResponse(ints, False)


def retrieveDiseaseResponse(ints, isForced):
    occurrences = diseaseCache.calculateOccurrences()

    if occurrences is not None:
        confidence = calculateConfidence(occurrences, ints)
        confidenceKey = next(iter(confidence))
        confidenceVaule = confidence.get(confidenceKey)[0]

        response = getResponseWithConfidance(confidenceKey, confidenceVaule, isForced)
        randomResponse = random.choice(response)
        diseaseCache.assignReponseMessageId(randomResponse.id)
        percent = calculatePercent(ceil(confidenceVaule * 100))

        return randomResponse.response.format(confidenceKey, f"{percent}%")

    return "Jeszcze nie wiem, wybacz"


def calculatePercent(percent):
    if percent > 100:
        return 100
    else:
        return percent


def getResponseWithConfidance(confidenceKey, confidenceVaule, isForced):
    if confidenceVaule >= 0.6 or isForced:
        saveUserDiseaseHistory(confidenceKey, confidenceVaule)
        saveRegionDisease(confidenceKey)
        diseaseCache.setSuggestCure(True)
        diseaseCache.setSuggestDisease(confidenceKey)
        return findResponseWithTagGroup(TagGroup.disease)
    elif 0.6 > confidenceVaule > 0.3 or len(diseaseCache.user_msg) >= 3:
        saveUserDiseaseHistory(confidenceKey, confidenceVaule)
        saveRegionDisease(confidenceKey)
        return findResponseWithTagGroup(TagGroup.question)

    return findResponseWithTagGroup(TagGroup.few_questions)


def findResponseWithTagGroup(group):
    responseQuery = select(Responses).where(Responses.response_group == group) \
        .where(Responses.id != diseaseCache.previousResponseId)
    return db_session.scalars(responseQuery).fetchall()


def calculateConfidence(occurrences, ints):
    confidence = {}
    for k, v in occurrences.items():
        pDiseaseQuery = select(Diseases).where(Diseases.choroba.ilike(k.lower()))
        symptomsAmount = db_session.scalars(pDiseaseQuery).one_or_none()
        if symptomsAmount is None:
            confidence[k] = [0, 0]
        else:
            if ints is not None and ints[0]['intent'] == k:
                chatbotProbability = v / len(symptomsAmount.objawy) + float(ints[0]['probability'])
                arr = [v / len(symptomsAmount.objawy), chatbotProbability]
                confidence[k] = arr
            else:
                count = v / len(symptomsAmount.objawy)
                confidence[k] = [count, count]

    return dict(sorted(confidence.items(), key=lambda item: item[1][1], reverse=True))


def chatbot_response(msg):
    ints = predict_class(msg)
    res = getResponse(ints, msg)
    return res


def suggestCure(msg):
    res = 'Tak to tak, nie to nie :)'
    if diseaseCache.suggestForDisease:
        if "tak" in msg.lower() and diseaseCache.suggestCure:
            res = showLeczenie(diseaseCache.suggestForDisease)
        elif "nie" in msg.lower() and diseaseCache.suggestCure:
            res = "Dobrze, w takim razie sugeruję udanie się do lekarza, który dokładnie Cię zbada :)"
    diseaseCache.setSuggestCure(False)
    return res

def saveUserDiseaseHistory(disease: str, confidence: float):
    token = jwtService.decodeAuthorizationHeaderToken()
    if token:
        userMsg = diseaseCache.user_msg
        userService.saveDiseaseHistory(userMsg, disease, token, confidence)


def saveRegionDisease(disease):
    location = jwtService.decodeLocationHeader()
    if location:
        longitude = location.get("longitude")
        latitude = location.get("latitude")
        userService.saveRegionDisease(latitude, longitude, disease)


def showLeczenie(msg):
    disease = msg.replace("leczenie: ", "")
    query = select(Prof.profilaktyka).join(Prof.choroba).where(Diseases.choroba.ilike(disease))

    return db_session.scalars(query).one_or_none()

def getchorobaforplace(msg):

    qq = msg.replace("lokalizacja: ","")
    pp = select(Diseases.choroba).select_from(Localization).join(Localization.choroba).where(Localization.miasto.contains(qq)).group_by(Diseases.choroba).order_by(func.count(Localization.choroba_id).desc())
    hw = db_session.scalars(pp).first()
    if hw is None:
        dp = select(Diseases.choroba).select_from(Localization).join(Localization.choroba).where(Localization.woj.contains(qq)).group_by(Diseases.choroba).order_by(func.count(Localization.choroba_id).desc())
        return db_session.scalars(dp).first()
    return hw