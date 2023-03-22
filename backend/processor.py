import nltk
from nltk.stem import WordNetLemmatizer
import json
import random
import diseaseCache
import pickle
import numpy as np
from keras.models import load_model

from userService import UserService

lemmatizer = WordNetLemmatizer()
model = load_model('chatbot_model.h5')

intents = json.loads(open('job_intents.json', encoding='utf-8').read())
disease_intents = json.loads(open('disease_intents.json', encoding='utf-8').read())
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
userService = UserService()


def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words


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
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list


def getResponse(ints, msg):
    result = "Ask the right question"
    tag = ints[0]['intent']
    list_of_intents = intents['intents']
    list_of_disease_intents = disease_intents['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break

    diseaseCache.add(msg)
    matching = []

    for i in list_of_disease_intents:
        if i['tag'] == tag:
            patterns = np.array(i['patterns'])
            for m in set(diseaseCache.user_msg):
                string = list(filter(lambda r: r.lower() == m.lower(), patterns))
                if len(string) > 0:
                    matching.append(string.pop())
            if len(matching) / len(patterns) >= 0.5:
                saveUserDiseaseHistory(diseaseCache.user_msg, tag)
                return random.choice(i['responses'])
            else:
                return random.choice(list_of_disease_intents[len(list_of_disease_intents) - 1]['responses'])
    return result


def chatbot_response(msg):
    ints = predict_class(msg, model)
    res = getResponse(ints, msg)
    return res


def saveUserDiseaseHistory(userMsg: [], disease: str):
    # TODO: Pobieranie id użytkownika z tokena
    userId = 1
    return userService.saveDiseaseHistory(userId, userMsg, disease)
