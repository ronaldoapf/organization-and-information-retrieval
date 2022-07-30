import os
import time

startTime = time.time()

path = 'documents'

if not os.path.exists(path):
  os.mkdir(path)

with open('corpusReduced.txt', 'r', encoding='latin1') as outfile:
  file = outfile.read().splitlines()
  name = ''

  for line in file:
    if 'NOME  -' in line:
      name = line.split("NOME  - ")[1]
      if len(name) != 0:
        file = open(path+"/"+name+'.txt', 'w+')
        file.close()

    if 'RESU  -' in line:
      content = line.split("RESU  - ")[1]
      if len(content) != 0:
        if "(Texto informado pelo autor)" in content:
          content = content.split("(Texto informado pelo autor)")[0]

        if "(Texto gerado automaticamente pela aplicaï¿½ï¿½o CVLattes)" in content:
          content = content.split("(Texto gerado automaticamente pela aplicaï¿½ï¿½o CVLattes)")[0]
          
        file = open(path+"/"+name+'.txt', 'a')
        file.write(content)
        file.close()

times = round(time.time() - startTime, 2)
print("Tempo de execução:", times)