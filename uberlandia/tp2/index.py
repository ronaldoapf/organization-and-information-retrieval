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
	vocabulary = []
	documents = sorted(glob.glob("*.txt"))

	for files in tqdm(documents):
		with open(files, 'r') as outfile:
			content = outfile.read()
			content = cleanAndTokenize(content)
			for word in content:
				if word not in vocabulary:
					vocabulary.append(word)

	with open("result/vocabulary.txt", "w+") as outfile:
		for term in vocabulary:
			outfile.writelines(term+"\n")

if __name__ == "__main__":
	main()