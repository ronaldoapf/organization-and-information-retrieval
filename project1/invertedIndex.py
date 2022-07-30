import os
import sys
import json
from tqdm import tqdm

path = 'documents'

def getPunctuation():
  with open('punctuation.txt', 'r', encoding="utf-8") as outfile:
    punctuation = []
    splitFile = outfile.read()
    
    for punct in splitFile:
      punctuation.append(punct)
  return punctuation

def tokenize(content):
	return content.split()

def getStopwords():
  with open('stopwords.txt', 'r', encoding="utf-8") as outfile:
    stopwords = outfile.read()
    return tokenize(stopwords)

def getTerms(file):
  with open(file, 'r') as outfile:
    return outfile.read()

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
  docID = 0
  dictionary = dict()
  directory = sys.argv[1]
  stopwords = getStopwords()
  punctuation = getPunctuation()
  document = os.listdir(directory)

  for filename in tqdm(sorted(document)):
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

  jsonFile = json.dumps(dictionary)
  with open("dictionary.json", "w") as outfile:
    outfile.write(jsonFile)

if __name__ == "__main__":
  main()