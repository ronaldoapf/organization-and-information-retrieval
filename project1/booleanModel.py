query = input("Digite a consulta a ser realizada: ")

query = query.lower()

i = 0
result = []

if len(query) == 1:
  result.append(set(Dict[query[0]]))
else:
  for word in query:
    if word == "and":
      result.append(set(Dict[word[i-1]]) & set(Dict[word[i+1]]))
      
print(np.unique(result))