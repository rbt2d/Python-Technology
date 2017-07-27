from nltk.stem import PorterStemmer
stemmer=PorterStemmer()
word="lifting"
print(stemmer.stem(word))