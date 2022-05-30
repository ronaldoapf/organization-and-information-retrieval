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
    for term in terms:
      if words in terms:
        terms.remove(words)

  return terms

def inverseDocumentFrequency():
  print("inverseDocumentFrequency")

def termFrequency(element):
  print("termFrequency")

def main():
  docID = 0
  dictionary = dict()
  directory = sys.argv[1]
  stopwords = getStopwords()
  punctuation = getPunctuations()
  document = os.listdir(directory)

  for filename in sorted(document):
    docID = docID + 1
    contentFile = getTerms(directory+'/'+filename)
    contentFile = removePunctuation(contentFile, punctuation)
    contentFile = tokenize(contentFile.lower())
    contentFile = removeStopwords(contentFile, stopwords)

    for word in contentFile:
      if word not in dictionary:
        dictChild = dict()
        dictChild[docID] = 1
        dictionary[word] = dictChild

      elif word in dictionary:
        if docID in dictionary[word]:
          dictionary[word][docID] = dictionary[word][docID] + 1
        
        if docID not in dictionary[word]:
          newChildDict = dict()
          newChildDict[docID] = 1 
          dictionary[word].update(newChildDict)
  
  lines = []
  columns = []

  for word in dictionary:
    lines.append(word)

  for index, docs in enumerate(sorted(document), start=1):
    print(docs) 
    columns.append(index)

  print(lines)
  print(columns)

if __name__ == "__main__":
  main()