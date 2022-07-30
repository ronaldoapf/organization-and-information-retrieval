import os
import utils
from tqdm import tqdm

def tokenize(content):
	return content.split()

def getStopwords():
  with open('stopwords.txt', 'r', encoding="utf-8") as outfile:
    stopwords = outfile.read()
    return stopwords.split()

def getPunctuation():
  with open('punctuation.txt', 'r', encoding="utf-8") as outfile:
    punctuation = []
    splitFile = outfile.read()
    
    for punct in splitFile:
      punctuation.append(punct)
  return punctuation

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

def menu():
  print('### Trabalho ORI ###')
  print('[1] Organizar documentos a partir do corpus.txt')
  print('[2] Gerar índice invertido')
  print('[3] Realizar consulta')
  print('[4] Gerar matrix TF-IDF')


def main():
  docID = 0
  dictionary = dict()
  stopwords = getStopwords()
  punctuation = getPunctuation()

  while True:
    menu()
    option = int(input("Digite sua opção: "))

    if option == 0:
      return False

    if option == 1:
      utils.documents()

    if option == 2:
      if 'documents' not in os.listdir():
        print('É necessário organizar o documento para gerar o índice invertido')

      else:
        for filename in tqdm(sorted(os.listdir('documents'))):
          docID = docID + 1
          with open('documents/'+filename, 'r') as outfile:
            contentFile = outfile.read()

          contentFile = removePunctuation(contentFile, punctuation)
          contentFile = contentFile.lower().split()
          contentFile = removeStopwords(contentFile, stopwords)

          utils.invertedIndex(dictionary, contentFile, docID)
    
    if option == 3:
      query = str(input("Digite a consulta: "))
      if len(query.split()) > 1:
        query = removePunctuation(query, punctuation)
        query = query.lower().split()
        query = removeStopwords(query, stopwords)
      else:
        query = query.split()

      utils.booleanModel(dictionary, query)

    if option == 4:
      utils.generateTfIdf(dictionary, os.listdir('documents'))

if __name__ == "__main__":
  main()