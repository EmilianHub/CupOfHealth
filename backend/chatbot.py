import pdb
import pickle
import random
from collections import defaultdict
import spacy
from spacy.lang.pl.examples import sentences
import nltk
import numpy as np
from keras.layers import Dense, Dropout
from keras.models import Sequential
from keras.optimizers import SGD
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sqlalchemy import select

from chorobyJPA import Diseases
from dbConnection import db_session
from patternsJPA import Patterns
from stempel import StempelStemmer


nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('pl196x')
nltk.download('cess_esp')
lemmatizer = WordNetLemmatizer()
stemmer = StempelStemmer.polimorf()
nlp = spacy.load("pl_core_news_sm")
words = []
classes = []
documents = []
ignore_words = ['?', '!', ",", ">", "<", "``", "''", "z", "i", "w", "się", "mam", "dla", "w", "o", "z", "pod", "nad"]

casualPatterns = db_session.scalars(select(Patterns)).fetchall()
casualDiseases = db_session.scalars(select(Diseases)).fetchall()
groupedCasualPatterns = defaultdict(list)



for pattern in casualPatterns:
    pattern_words = [token.lemma_ for token in nlp(pattern.pattern)]
    words.extend(pattern_words)
    documents.append((pattern_words, str(pattern.pattern_group.value)))
    if str(pattern.pattern_group.value) not in classes:
        classes.append(str(pattern.pattern_group.value))

for disease in casualDiseases:
    for symptom in disease.objawy:
        symptom_words = [token.lemma_ for token in nlp(symptom.objawy)]
        words.extend(symptom_words)
        documents.append((symptom_words, str(disease.choroba)))
        if str(disease.choroba) not in classes:
            classes.append(str(disease.choroba))

words = [lemmatizer.lemmatize(w.lower(), wn.ADJ) for w in words if w not in ignore_words]
words += [lemmatizer.lemmatize(w.lower(), wn.ADV) for w in words if w not in ignore_words]
words += [lemmatizer.lemmatize(w.lower(), wn.ADJ_SAT) for w in words if w not in ignore_words]


for sentence in sentences:
    doc = nlp(sentence)
    for token in doc:
        if token.lemma_.lower() not in words:
            words.append(token.lemma_.lower())

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
    pattern_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_words]

    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)


    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1

    training.append([bag, output_row])

random.shuffle(training)
training = np.array(training)
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