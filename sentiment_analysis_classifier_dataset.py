# -*- coding: utf-8 -*-
"""Sentiment_Analysis_Classifier_Dataset.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WDJFJla3Uf45Vl75PUeRZILba-p3hkBl
"""

!pip install spacy--upgrade
#pip install spacy==version
!python -m spacy download pt
!python install nltk --upgrade
!python3 -m spacy download pt

import spacy
from nltk.stem import PorterStemmer
from spacy import displacy
from spacy.lang.pt.examples import sentences
from spacy.lang.en.stop_words import STOP_WORDS
from spacy.lang.pt.stop_words import STOP_WORDSPT
import panda as pd
import string
import random
import seaborn as sns
import numpy as np
spacy.__version__, nltk.__version__

dataset = pd.read_csv('dataset_train', encodig = 'utf-8')
dataset.shape
dataset.head()

dataset.tail()

sns.countplot(dataset['emotion'], label = 'Count');

pont = string.punctuation
pont

stop_words = STOP_WORDS
stop_words

print(Len(stop_words))

nlp_pt = spacy.load('pt')
nlp_en = spacy.load('en')

def preprocessing(text):
  text = text.lower()
  doc = nlp_en(text)
  list_ = []
  for token in doc:
    #list_.append(token.text)
    list_.append(token.lemma_)
  list_ = [word for word in list_ if word not in stop_words and word not in pont]
  list_ = ''.join([str(element) for element in list_ not element.isdigit()])
  return list

test = preprocessing("I'm learning Natural 10 50 100 Language Processing")

dataset.head(10)

dataset['text'] = dataset['text'].apply(preprocessing)

dataset.head(10)

dataset_final = []
i = 0
for text, emotion in zip(dataset['text'], dataset['emotion']):
  #print(text, emotion)
  if emotion == 'happy':
    dic = ({'HAPPY': True, 'Fear': False})
  elif emotion == 'FEAR':
    dic = ({'HAPPY': False, 'Fear': True})

  dataset_final.append([text, dic.copy()])

len(dataset_final)

dataset_final[0]
dataset_final[0][0]
dataset_final[0][1]
type(dataset_final[0][1])
dataset_final

model = spacy.blank('en')
cat = model.create_pipe('textcat')
cat.add_label('HAPPY')
cat.add_label('FEAR')
model.add_pipe(cat)
historical = []