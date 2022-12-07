import os
import sys
import numpy 

def getPunctuations():
  punctuation = list()
  with open('punctuation.txt', 'r') as outfile:
    splitFile =  outfile.read()
    
    for punct in splitFile:
      punctuation.append(punct)
  
  return punctuation

def getStopwords():
  with open('stopwords.txt', 'r') as outfile:
    stopwords = outfile.read()
    return tokenize(stopwords)

def getTerms(file):
  with open(file, 'r') as outfile:
    return outfile.read()

def tokenize(content):
	return content.split()

def removePunctuation(terms, punctuation):
  for punct in punctuation:
    if punct in terms:
      terms = terms.replace(punct, "")
    
  return terms

def removeStopwords(terms, stopwords):
  for words in stopwords:
    if words in terms:
      terms.remove(words)

  return terms
  
def main():
  directory = sys.argv[1]
  stopwords = getStopwords()
  punctuation = getPunctuations()
  listTerms = list()
  lengthTerms = 0
  document = os.listdir(directory)

  for filename in document:
    contentFile = getTerms(directory+'/'+filename)
    contentFile = removePunctuation(contentFile, punctuation)
    contentFile = tokenize(contentFile.lower())
    contentFile = removeStopwords(contentFile, stopwords)
    for word in contentFile:
      if not word in listTerms:
        listTerms.append(word)

  matrix = numpy.zeros((len(listTerms), len(document)))

  for terms in listTerms:
    if not terms in matrix:
      matrix[0][0].astype =  = terms    

  print(matrix)
if __name__ == "__main__":
  main()