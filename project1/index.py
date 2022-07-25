import os
import sys
import time
import json
import math
import numpy

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

  for filename in sorted(document):
    docID = docID + 1
    print("Starting doc", docID)
    startTimeDocument = time.time()
    contentFile = getTerms(directory+'/'+filename)
    if "(Texto informado pelo autor)" in contentFile:
      contentFile = contentFile.split("(Texto informado pelo autor)")[0]

    if "(Texto gerado automaticamente pela aplicaï¿½ï¿½o CVLattes)" in contentFile:
      contentFile = contentFile.split("(Texto gerado automaticamente pela aplicaï¿½ï¿½o CVLattes)")[0]

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
      
      

    # matrix = numpy.zeros((len(dictionary) + 1, len(document) + 1), dtype=numpy.object_)

    # countRows = 1
    # countColumns = 0

    # for word in dictionary:
    #   # Cabeçalho da tabela mostrando o número dos documentos
    #   while countColumns < len(document) + 1:
    #     if countColumns == 0:
    #       matrix[0][countColumns] = "Documents"
    #       countColumns = countColumns + 1
    #     matrix[0][countColumns] = "Doc " + str(countColumns)
    #     countColumns = countColumns + 1

    #   matrix[countRows][0] = word
    #   countRows = countRows + 1

    # numberOfDocs = len(document)

    # for word in dictionary:
    #   position = numpy.where(matrix == word)
    #   if position[0][0]:
    #     keys = dictionary[word].keys()
    #     for idxDocuments in keys:
    #       tf = 1 + math.log10(dictionary[word][idxDocuments])
    #       idf = math.log10(numberOfDocs/len(dictionary[word]))
    #       matrix[position[0][0]][idxDocuments] = numpy.round(tf * idf, 2)
    print("Time to process doc", round(time.time() - startTimeDocument, 2))
  
  file = open('dictionary.txt', 'w')
  file.write(str(dictionary))
  file.close()

  jsonDump = json.dump(dictionary)
  jsonFile = open('file.json', 'w')
  jsonFile.write(jsonDump)
  jsonFile.close()
  

if __name__ == "__main__":
  startTime = time.time()
  main()
  times = round(time.time() - startTime, 2)
  print("Tempo de execução:", times)