import os
import re
import glob
import numpy
from tqdm import tqdm
from unidecode import unidecode
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer

def cleanAndTokenize(content):
  content = re.sub(r'[^\w\s]','', content)
  return sorted(set(word_tokenize(unidecode(content.lower()))))


def main():
	documents = []
	bagOfWords = []
	vocabulary = []
	pathList = sorted(glob.glob("*.txt"))

	for files in pathList:
		with open(files, 'r') as outfile:
			content = outfile.read()
			content = cleanAndTokenize(content)
			documents.append(content)

			for word in content:
				if word not in vocabulary:
					vocabulary.append(word)
	
	vocabulary = sorted(vocabulary)

	with open("result/vocabulary.txt", "w+") as outfile:
		for term in vocabulary:
			outfile.writelines(term+"\n")

	for i in range(0, len(documents)):
		bagOfWords.append(numpy.zeros(len(vocabulary), dtype=object))

	for idxDocument, document in enumerate(documents):
		for term in document:
			if term in vocabulary:
				positionTerm = vocabulary.index(term)
				bagOfWords[idxDocument][positionTerm] = 1 			

	print(vocabulary)

	for idx, docs in enumerate(bagOfWords, start=1):
		print("Documento {}: {}".format(idx, docs))


if __name__ == "__main__":
	main()