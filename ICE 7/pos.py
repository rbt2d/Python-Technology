from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

words = word_tokenize('hello, nagaraju and how are you ?')
print(pos_tag(words))