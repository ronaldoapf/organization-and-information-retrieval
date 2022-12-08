import os
import re
import sys
import glob
import numpy
from unidecode import unidecode
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer

def cleanAndTokenize(content):
  content = re.sub(r'[^\w\s]','', content)
  return sorted(set(word_tokenize(unidecode(content.lower()))))

def main():
	if len(sys.argv) > 1:
		print(sys.argv[1])


if __name__ == "__main__":
	main()