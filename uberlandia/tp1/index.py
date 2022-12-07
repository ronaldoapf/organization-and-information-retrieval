import re
import numpy
from unidecode import unidecode
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer

def cleanAndTokenize(content):
  content = re.sub(r'[^\w\s]','', content)
  return sorted(set(word_tokenize(unidecode(content.lower()))))

def firstProblem():
  with open('entrada1.txt', 'r', encoding='utf-8') as outfile:
    contentFile = outfile.read()

  contentFile = cleanAndTokenize(contentFile)

  with open("indexTerms.txt", "w+") as outfile:
    for term in contentFile:
      outfile.writelines(term + "\n")


def secondProblem():
  with open('entrada2.txt', 'r', encoding='utf-8') as outfile:
    contentFile = outfile.read()
 
  with open('indexTerms.txt', 'r', encoding='utf-8') as outfile:
    indexTerms = outfile.read()
  
  contentFile = cleanAndTokenize(contentFile)
  indexTerms = cleanAndTokenize(indexTerms)

  bagOfWords = numpy.zeros(len(indexTerms), dtype=int)

  for termContent in contentFile:
    if termContent in indexTerms:
      termPosition = indexTerms.index(termContent)
      bagOfWords[termPosition] = 1

  print(bagOfWords)

# firstProblem()
secondProblem()