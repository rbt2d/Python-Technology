import nltk
from nltk.corpus import wordnet as wn


synsets=wn.synsets('phone')

print[synsets]

for a in synsets:
    print (a.definition())