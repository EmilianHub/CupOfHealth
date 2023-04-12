import pickle
import random
from math import ceil

import nltk
import numpy as np
from keras.models import load_model
from nltk.stem import WordNetLemmatizer
from sqlalchemy import select

import diseaseCache
from profJPA import Prof
from chorobyJPA import Diseases
from dbConnection import db_session
from responsesJPA import Responses
from tagGroup import TagGroup
from userService import UserService
from jwtService import decodeHeaderToken

lemmatizer = WordNetLemmatizer()
model = load_model('chatbot_model.h5')
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
userService = UserService()


def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return set(sentence_words)


# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence


def bow(sentence, words, show_details=True):
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
    return (np.array(bag))


def predict_class(sentence, model):
    # filter out predictions below a threshold
    p = bow(sentence, words, show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.02
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list


def getResponse(ints, msg):
    if len(ints) != 0:
        tag = ints[0]['intent']

        if isCasualResponse(tag):
            return retrieveCausalResponse(tag)
        if tag.startswith("Leczenie") :
            ss=showLeczenie(tag)
            return ss

        return retrieveDisesaseResponse(ints, msg)

    return "Na obecną chwilę nie mam na to odpowiedzi, przepraszam"


def isCasualResponse(tag):
    pFilter = filter(lambda t: t == tag, TagGroup.fetch_names())

    return len(list(pFilter)) != 0


def retrieveCausalResponse(tag):
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

    return retrieveDiseaseResponse(msg)


def retrieveDiseaseResponse(msg):
    occurrences = diseaseCache.calculateOccurrences()

    if occurrences is not None:
        confidence = calculateConfidence(occurrences)
        confidenceKey = next(iter(confidence))
        confidenceVaule = confidence.get(confidenceKey)

        response = getResponseWithConfidance(confidenceKey, confidenceVaule)
        randomResponse = random.choice(response)
        diseaseCache.assignReponseMessageId(randomResponse.id)

        return randomResponse.response.format(confidenceKey, f"{ceil(confidenceVaule*100)}%")

    return "Jeszcze nie wiem, wybacz"


def getResponseWithConfidance(confidenceKey, confidenceVaule):
    if confidenceVaule >= 0.6:
        saveUserDiseaseHistory(confidenceKey)
        return findResponseWithTagGroup(TagGroup.disease)
    elif 0.6 > confidenceVaule > 0.3:
        saveUserDiseaseHistory(confidenceKey)
        return findResponseWithTagGroup(TagGroup.question)

    return findResponseWithTagGroup(TagGroup.few_questions)


def findResponseWithTagGroup(group):
    responseQuery = select(Responses).where(Responses.response_group == group)\
        .where(Responses.id != diseaseCache.previousResponseId)
    return db_session.scalars(responseQuery).fetchall()


def calculateConfidence(occurrences):
    confidence = {}
    for k, v in occurrences.items():
        pDiseaseQuery = select(Diseases).where(Diseases.choroba.ilike(k.lower()))
        symptomsAmount = db_session.scalars(pDiseaseQuery).one_or_none()
        if symptomsAmount is None:
            confidence[k] = 0
        else:
            confidence[k] = v/len(symptomsAmount.objawy)

    return dict(sorted(confidence.items(), key=lambda item: item[1], reverse=True))



def chatbot_response(msg):
    ints = predict_class(msg, model)
    res = getResponse(ints, msg)
    return res


def saveUserDiseaseHistory(disease: str):
    token = decodeHeaderToken()
    if token:
        userMsg = diseaseCache.user_msg
        return userService.saveDiseaseHistory(userMsg, disease, token)
    return None

def showLeczenie(msg):

        hh= msg.replace("Leczenie: ","")
        ll = select(Prof.profilaktyka).join(Prof.choroba).where(Diseases.choroba.ilike(hh))

        return db_session.scalars(ll).one_or_none()

