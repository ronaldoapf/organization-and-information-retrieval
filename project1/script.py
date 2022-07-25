import os
import time

startTime = time.time()

if not os.path.exists('documents'):
  os.mkdir('documents')

with open('corpus.txt', 'r', encoding='latin1') as outfile:
  file = outfile.read().splitlines()
  name = ''

  for line in file:
    if 'NOME  -' in line:
      name = line.split("NOME  - ")[1]
      if len(name) != 0:
        file = open('documents/'+name+'.txt', 'w+')
        file.close()

    if 'RESU  -' in line:
      content = line.split("RESU  - ")[1]
      if len(content) != 0:
        file = open('documents/'+name+'.txt', 'a')
        file.write(content)
        file.close()

times = round(time.time() - startTime, 2)
print("Tempo de execução:", times)