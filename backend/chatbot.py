import pickle
import random

import numpy as np
import spacy
from keras.layers import Dense, Dropout
from keras.models import Sequential
from keras.optimizers import SGD
from sqlalchemy import select

from chorobyJPA import Diseases
from dbConnection import db_session
from patternsJPA import Patterns
from tagGroup import TagGroup

nlp = spacy.load("pl_core_news_md")
words = []
classes = []
documents = []

ignore_words = nlp.Defaults.stop_words
ignore_words.update({'?', '!', ",", ">", "<", "``", "''", ".", "-", '\n'})

casualPatterns = db_session.scalars(select(Patterns).where(Patterns.pattern_group != TagGroup.leczenie).where(Patterns.pattern_group != TagGroup.opis)).fetchall()
casualDiseases = db_session.scalars(select(Diseases)).fetchall()
leczeniePatterns = db_session.scalars(select(Patterns).where(Patterns.pattern_group == TagGroup.leczenie)).fetchall()
opisPatterns = db_session.scalars(select(Patterns).where(Patterns.pattern_group == TagGroup.opis)).fetchall()


for pattern in casualPatterns:
    tokenizedWord = nlp(pattern.pattern)
    pattern_words = [token.lemma_.lower() for token in tokenizedWord]
    pattern_words += [token.text.lower() for token in tokenizedWord]

    words.extend(pattern_words)
    documents.append((pattern_words, str(pattern.pattern_group.value)))

    if str(pattern.pattern_group.value) not in classes:
        classes.append(str(pattern.pattern_group.value))


for disease in casualDiseases:
    for symptom in disease.objawy:
        tokenizedWord = nlp(symptom.objawy)
        symptom_words = [token.text.lower() for token in tokenizedWord if token.lemma_ not in ignore_words]
        symptom_words += [token.lemma_.lower() for token in tokenizedWord if token.lemma_ not in ignore_words]

        words.extend(symptom_words)
        documents.append((symptom_words, str(disease.choroba)))

        if str(disease.choroba) not in classes:
            classes.append(str(disease.choroba))


for disease in casualDiseases:
    for q in opisPatterns:
        tokenizedWord = nlp(f"{q.pattern} {disease.choroba}")
        l = [token.text.lower() for token in tokenizedWord]
        l += [token.lemma_.lower() for token in tokenizedWord]
        words.extend(l)

        documents.append((l, str(f"opis: {disease.choroba}")))

        if f"opis: {disease.choroba}" not in classes:
            classes.append(str(f"opis: {disease.choroba}"))


for p in casualDiseases:
    for pattern in leczeniePatterns:
        tokenizedWord = nlp(f"{pattern.pattern} {p.choroba}")
        l = [token.text.lower() for token in tokenizedWord if token.lemma_ not in ignore_words]
        l += [token.lemma_.lower() for token in tokenizedWord if token.lemma_ not in ignore_words]
        words.extend(l)

        documents.append((l, str(f"leczenie: {p.choroba}")))

        if f"leczenie: {p.choroba}" not in classes:
            classes.append(str(f"leczenie: {p.choroba}"))


words = sorted(list(set(words)))
classes = sorted(list(set(classes)))

print(len(documents), "documents")

print(len(classes), "classes", classes)

print(len(words), "unique lemmatized words", words)

pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))

# initializing training data
training = []
output_empty = [0] * len(classes)
for doc in documents:
    bag = []
    pattern_words = doc[0]
    temp = []
    for word in pattern_words:
        tokenizedWord = nlp(word)
        temp.extend([token.lemma_.lower() for token in tokenizedWord])
        temp.extend([token.text.lower() for token in tokenizedWord])

    for w in words:
        bag.append(1) if w in temp else bag.append(0)

    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1

    training.append([bag, output_row])

random.shuffle(training)
training = np.array(training, dtype=object)
# create train and test lists. X - patterns, Y - intents
train_x = list(training[:, 0])
train_y = list(training[:, 1])
print("Training data created")

# Create model - 3 layers. First layer 128 neurons, second layer 64 neurons and 3rd output layer contains number of neurons
# equal to number of intents to predict output intent with softmax
model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

# Compile model. Stochastic gradient descent with Nesterov accelerated gradient gives good results for this model
sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

# fitting and saving the model
hist = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)
model.save('chatbot_model.h5', hist)
print("model created")