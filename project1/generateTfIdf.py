import os
import json
import math
import numpy
from tqdm import tqdm

with open('dictionary.json') as outfile:
  dictionary = json.load(outfile)

documents = os.listdir('documents')

matrix = numpy.zeros((len(dictionary), len(documents) + 1), dtype=numpy.object_)

countRows = 0
countColumns = 1

for word in dictionary:
  matrix[countRows][0] = word
  while countColumns <= len(documents):
    if str(countColumns) in dictionary[word].keys():
      tf = 1 + math.log10(dictionary[word][str(countColumns)])
      idf = math.log10(len(documents) / len(dictionary[word]))
      matrix[countRows][countColumns] = numpy.round(tf * idf, 2)
    countColumns = countColumns + 1
  countRows = countRows + 1
  countColumns = 1

with open('matrix.txt',"w") as f:
  f.write("\n".join(" ".join(map(str, x)) for x in (matrix)))
