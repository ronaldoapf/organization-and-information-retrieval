import os
import sys

def openFile(file):
	with open(file, 'r') as outfile:
		return outfile.read()

def tokenize(content):
	return content.split()

def makeStringLower(content):
	return content.lower()

def search(query, content):
	if query in content:
		if content.count(query) > 1:
			print(query, 'aparece', content.count(query), 'vezes no documento')
			return
		
		print(query, 'aparece', content.count(query), 'vez no documento')

def createDictionary(dictionary, document, content):
	for word in content:
		if len(dictionary) == 0:
			newDictionary = dict()
			newDictionary[document] = 1
			dictionary[word] = newDictionary

		else:
			for teste in dictionary:
				if word in dictionary:
					print(dictionary[teste])	

def main():

	dictionary = dict()
	document = 1
	directory = sys.argv[1]
	# query = sys.argv[2]
	for filename in os.listdir(directory):
		contentFile = openFile(directory+'/'+filename)
		contentFile = makeStringLower(contentFile)
		contentFile = tokenize(contentFile)
		createDictionary(dictionary, document, contentFile)

	# contentFile = tokenize(contentFile)
	# search(query, contentFile)

if __name__ == "__main__":
	main()