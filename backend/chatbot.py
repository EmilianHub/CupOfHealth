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

words = []
classes = []
documents = []
ignore_words = ['?', '!', ",", ">", "<", "``", "''", "z", "i", "w", "się", "mam", "dla", "w", "o", "z", "pod", "nad"]

casualPatterns = db_session.scalars(select(Patterns)).fetchall()
casualDiseases = db_session.scalars(select(Diseases)).fetchall()
groupedCasualPatterns = defaultdict(list)



for i in casualPatterns:
    groupedCasualPatterns[i.pattern_group.value].append(i.pattern)

for k, v in groupedCasualPatterns.items():
    for pattern in v:

        w = nltk.word_tokenize(str(pattern))
        words.extend(w)

        documents.append((w, str(k)))

        if k not in classes:
            classes.append(str(k))

#TODO: Wyciaganie z jpa db_session.scalars(select(Diseases)).fetchall() bez grupowania, budujesz tylko worldneta
for i in casualDiseases:
    for j in i.objawy:
        w = nltk.word_tokenize(str(j.objawy))
        words.extend(w)

        documents.append((w, str(i.choroba)))

        if i not in classes:
            classes.append(str(i.choroba))

words = [lemmatizer.lemmatize(w.lower(), wn.ADJ) for w in words if w not in ignore_words]
words += [lemmatizer.lemmatize(w.lower(), wn.ADV) for w in words if w not in ignore_words]
words += [lemmatizer.lemmatize(w.lower(), wn.ADJ_SAT) for w in words if w not in ignore_words]


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
nlp = spacy.load("pl_core_news_sm")
doc = nlp(sentences[0])

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
