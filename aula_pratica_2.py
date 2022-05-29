import os
import sys

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
  query = 'arara'
  founds = 0

  for filename in os.listdir(directory):
    contentFile = getTerms(directory+'/'+filename)

    contentFile = removePunctuation(contentFile, punctuation)
    contentFile = tokenize(contentFile.lower())
    contentFile = removeStopwords(contentFile, stopwords)
    
    if query in contentFile:
      founds = founds + 1
      print(filename,":",founds)

    founds = 0

if __name__ == "__main__":
  main()