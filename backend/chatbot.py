import nltk
import json
import pickle
from nltk.stem import WordNetLemmatizer
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD
import random
from sqlalchemy import select
from patternsJPA import Patterns
from responsesJPA import Responses
from chorobyJPA import Diseases
from dbConnection import db_session
from collections import defaultdict
import pdb

nltk.download('punkt')
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()

words = []
classes = []
documents = []
ignore_words = ['?', '!']

casualPatterns = db_session.scalars(select(Patterns)).fetchall()
casualDiseases = db_session.scalars(select(Diseases)).fetchall()
groupedCasualPatterns = defaultdict(list)

for i in casualPatterns:
    groupedCasualPatterns[i.pattern_group].append(i.pattern)

for k, v in groupedCasualPatterns.items():
    for pattern in v:

        w = nltk.word_tokenize(pattern)
        words.extend(w)

        documents.append((w, k))

        if k not in classes:
            classes.append(k)

#TODO: Wyciaganie z jpa db_session.scalars(select(Diseases)).fetchall() bez grupowania, budujesz tylko worldneta
for i in casualDiseases:
    w = nltk.word_tokenize(pattern)
    words.extend(w)

    documents.append((w, i.objawy))

    if i not in classes:
        classes.append(i)

#    i.choroba
#       i.objawyy

# for dIntents in disease_intents['intents']:
#     for pattern in dIntents['patterns']:
#
#         w = nltk.word_tokenize(pattern)
#         words.extend(w)
#
#         documents.append((w, dIntents['tag']))
#
#         if dIntents['tag'] not in classes:
#             classes.append(dIntents['tag'])
#
# words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
# words = sorted(list(set(words)))
#
# classes = sorted(list(set(classes)))
#
# print(len(documents), "documents")
#
# print(len(classes), "classes", classes)
#
# print(len(words), "unique lemmatized words", words)
#
# pickle.dump(words, open('words.pkl', 'wb'))
# pickle.dump(classes, open('classes.pkl', 'wb'))
#
# # initializing training data
# training = []
# output_empty = [0] * len(classes)
# for doc in documents:
#
#     bag = []
#
#     pattern_words = doc[0]
#     pattern_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_words]
#
#     for w in words:
#         bag.append(1) if w in pattern_words else bag.append(0)
#
#     output_row = list(output_empty)
#     output_row[classes.index(doc[1])] = 1
#
#     training.append([bag, output_row])
#
# random.shuffle(training)
# training = np.array(training)
# # create train and test lists. X - patterns, Y - intents
# train_x = list(training[:, 0])
# train_y = list(training[:, 1])
# print("Training data created")
#
# # Create model - 3 layers. First layer 128 neurons, second layer 64 neurons and 3rd output layer contains number of neurons
# # equal to number of intents to predict output intent with softmax
# model = Sequential()
# model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
# model.add(Dropout(0.5))
# model.add(Dense(64, activation='relu'))
# model.add(Dropout(0.5))
# model.add(Dense(len(train_y[0]), activation='softmax'))
#
# # Compile model. Stochastic gradient descent with Nesterov accelerated gradient gives good results for this model
# sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
# model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])
#
# # fitting and saving the model
# hist = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)
# model.save('chatbot_model.h5', hist)
#
# print("model created")