from nltk import ngrams
sentence = 'this is a foo bar sentences and i want to ngramize it'
n = 3
sixgrams = ngrams(sentence.split(), n)

for grams in sixgrams:
  print (grams)


