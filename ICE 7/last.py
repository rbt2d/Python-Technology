from nltk import pos_tag, ne_chunk
from nltk.tokenize import wordpunct_tokenize

s ='Jio has introduced new mobile phone'

print(ne_chunk(pos_tag(wordpunct_tokenize(s))))