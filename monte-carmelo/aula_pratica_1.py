import os
import sys

def openFile(file):
	with open(file, 'r', encoding='utf-8') as outfile:
		text = outfile.read()
		return text

def openManyFiles(directory):
	for filename in os.listdir(directory):
		return openFile(directory+'/'+filename)

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

def main():

	directory = sys.argv[1]
	query = sys.argv[2]

	contentFile = openFile(directory)
	contentFile = makeStringLower(contentFile)
	contentFile = tokenize(contentFile)
	search(query, contentFile)

if __name__ == "__main__":
	main()