import os
import numpy
import math
from time import time
from collections import Counter

def documents():
  startTime = time()

  if not os.path.exists('documents'):
    os.mkdir('documents')

  with open('corpus.txt', 'r', encoding='latin1') as outfile:
    file = outfile.read().splitlines()
    name = ''

    for line in file:
      if 'NOME  -' in line:
        name = line.split("NOME  - ")[1]
        if len(name) != 0:
          file = open('documents'+"/"+name+'.txt', 'w+')
          file.close()

      if 'RESU  -' in line:
        content = line.split("RESU  - ")[1]
        if len(content) != 0:
          if "(Texto informado pelo autor)" in content:
            content = content.split("(Texto informado pelo autor)")[0]

          if "(Texto gerado automaticamente pela aplicaï¿½ï¿½o CVLattes)" in content:
            content = content.split("(Texto gerado automaticamente pela aplicaï¿½ï¿½o CVLattes)")[0]
            
          file = open('documents'+"/"+name+'.txt', 'a')
          file.write(content)
          file.close()
  times = round(time() - startTime, 2)
  print("Tempo de execução:", times)

def invertedIndex(dictionary, file, docID):
  for word in file:
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

  return dictionary

def booleanModel(dictionary, query):
  i = 0
  result = []
  if len(query) == 1:
    if query not in dictionary:
      print([])
    else:
      result.append(set(dictionary[query[0]]))
  else:
    for word in query:
      print(i)
      if word == "and":
        if i == 1:
          result.append(set(dictionary[query[i-1]]) & set(dictionary[query[i+1]]))
        else:
          result.append(set(result[0]) & set(dictionary[query[i+1]]))
      i = i + 1

  print(numpy.unique(result))

def generateTfIdf(dictionary, documents):
  matrix = numpy.zeros((len(dictionary), len(documents) + 1), dtype=numpy.object_)
  print(len(documents))
  countRows = 0
  countColumns = 1

  for word in dictionary:
    matrix[countRows][0] = word
    print(countColumns)
    while countColumns <= len(documents):
      if str(countColumns) in dictionary[word].keys():
        tf = 1 + math.log10(dictionary[word][str(countColumns)])
        idf = math.log10(len(documents) / len(dictionary[word]))
        matrix[countRows][countColumns] = numpy.round(tf * idf, 2)
      countColumns = countColumns + 1
    countRows = countRows + 1
    print(countRows)
    countColumns = 1

  with open('matrix.txt',"w") as f:
    f.write("\n".join(" ".join(map(str, x)) for x in (matrix)))