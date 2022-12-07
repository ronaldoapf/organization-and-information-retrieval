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
    for term in terms:
      if words in terms:
        terms.remove(words)

  return terms
  
def main():
  directory = sys.argv[1]
  stopwords = getStopwords()
  punctuation = getPunctuations()
  dictionary = dict()
  document = os.listdir(directory)
  docID = 0

  for filename in sorted(document):
    docID = docID + 1
    contentFile = getTerms(directory+'/'+filename)
    contentFile = removePunctuation(contentFile, punctuation)
    contentFile = tokenize(contentFile.lower())
    contentFile = removeStopwords(contentFile, stopwords)

    for word in contentFile:
      if word not in dictionary:
        dictionary[word] = [docID]
      
      if word in dictionary:
        if docID not in dictionary[word]:
          dictionary[word].append(docID)

if __name__ == "__main__":
  main()