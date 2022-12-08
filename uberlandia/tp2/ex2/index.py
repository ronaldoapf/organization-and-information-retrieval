import os
import re
import sys
import glob
import numpy
from collections import Counter
from unidecode import unidecode
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer

def cleanAndTokenize(content):
  content = re.sub(r'[^\w\s]','', content)
  return word_tokenize(unidecode(content.lower()))

def main():
  # C:\Users\ronal\Desktop\organization-and-information-retrieval\uberlandia\tp2\ex1\result\vocabulary.txt
  countFiles = 0

  documents = []
  bagOfWords = []
  vocabulary = []
  
  root = sys.argv[1]
  vocabularyFile = sys.argv[2]

  # Read vocabulary according path file
  with open(vocabularyFile, 'r') as outfile:
    contentFile = outfile.read().split()
    vocabulary = contentFile

  # Read docs according path file
  for file in os.listdir(root):
    if file.endswith(".txt"):
      countFiles += 1
      with open(os.path.join(root, file), 'r') as outfile:
        content = outfile.read()
        content = cleanAndTokenize(content)
        documents.append(content)

  # Generate arrays of zeros to set what terms appears at document according with the vocabulary
  for i in range(0, len(documents)):
    bagOfWords.append(numpy.zeros(len(vocabulary), dtype=object))

  for idx, document in enumerate(documents):
    counterWords = Counter(document)
    documents[idx] = sorted(set(document))


  # Generate arrays of zeros to set what terms appears at document according with the vocabulary
  # for i in range(0, len(documents)):
  #   bagOfWords.append(numpy.zeros(len(vocabulary), dtype=object))

  # # Setting what terms appears in which document
  # for idxDocument, document in enumerate(documents):
  #   for term in document:
  #     if term in vocabulary:
  #       positionTerm = vocabulary.index(term)
  #       if bagOfWords[idxDocument][positionTerm] != 0:
  #         bagOfWords[idxDocument][positionTerm] = bagOfWords[idxDocument][positionTerm] + 1
  #       else:
  #         bagOfWords[idxDocument][positionTerm] = 1 			

  # # Printing each document
  # for idx, docs in enumerate(bagOfWords, start=1):
  #   print("Documento {}: {}".format(idx, docs))

  # print(documents)
  # for document in bagOfWords:
  #   for term in document:
  #     print(term)


if __name__ == "__main__":
	main()