import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import numpy
import tflearn
import tensorflow
import random
import json


with open("training.json") as file:
    data = json.load(file)



words = []              #contient l'ensemble des mots qui existe dans les patterns
labels = []             # contient l'ensemble des tag
docs_x = []             # contient la liste des patterns
docs_y = []             # contient le tag de chaque pattern

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        wrds = nltk.word_tokenize(pattern)
        words.extend(wrds)
        docs_x.append(wrds)                
        docs_y.append(intent["tag"])       
    if intent["tag"] not in labels:
        labels.append(intent["tag"])


words = [stemmer.stem(w.lower()) for w in words if w != "?"]
words = sorted(list(set(words)))   # la listes des mots des patterns non repeté et ordonné



labels = sorted(labels)


training = []          # la liste d occurance des mots d'un element du patterns parmis l'ensembles des words
output = []            #(bag of words) la liste des labels de chaque pattern

out_empty = [0 for _ in range(len(labels))]     # contient

for x, doc in enumerate(docs_x):
    bag = []

    wrds = [stemmer.stem(w.lower()) for w in doc]
    for w in words:
        if w in wrds:
            bag.append(1)
        else:
            bag.append(0)

    output_row = out_empty[:]     # make a copie
    output_row[labels.index(docs_y[x])] = 1

    training.append(bag)
    output.append(output_row)

training = numpy.array(training)   # transformin into numpy arrays because that s the form we need to be taken by our model
output = numpy.array(output)


# developping the model


tensorflow.reset_default_graph()

netq = tflearn.input_data(shape=[None, len(training[0])])
netq = tflearn.fully_connected(netq, 13)
netq = tflearn.fully_connected(netq, 13)
netq = tflearn.fully_connected(netq, len(output[0]), activation="softmax")
netq = tflearn.regression(netq)

model = tflearn.DNN(netq)

try:
    model.load("model.tflearn")
except:
    model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
    model.save("model.tflearn")


def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1
            
    return numpy.array(bag)


def chat(inp):

    liste=[]
    
    results = model.predict([bag_of_words(inp, words)])
    results_index = numpy.argmax(results)
    tag = labels[results_index]
    for tg in data["intents"]:
            if tg['tag'] == tag:
                responses = tg['responses']
                liste.append(random.choice(responses))
                liste.append(tag)
    
    return(liste)
