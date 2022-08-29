```
print("Invertd Index")
file = open("file.txt")
read = file.read()
file.seek(0)

line = 1
for word in read:
	if word == '\n':
		line += 1
print("Number of lines in file is: ", line)
array = []
for i in range(line):
	array.append(file.readline())

punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
for ele in read:
	if ele in punc:
		read = read.replace(ele, " ")

read=read.lower()					
from nltk.tokenize import word_tokenize
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import pandas as pd
  
ps = PorterStemmer()
for i in range(1):
	text_tokens = word_tokenize(read)

tokens_without_sw = [
	ps.stem(word) for word in text_tokens if (not word in stopwords.words())]

original_data=[int(0) for i in range(line)]
for i in range(line):
    original_data[i]=[
    	ps.stem(word) for word in word_tokenize(array[i]) if not word in stopwords.words() and (not word in punc)]
#%%
print(tokens_without_sw)
dictInvIndex = {}
#%%
for i in range(line):
	check = array[i].lower()
	for item in tokens_without_sw:
		if item in check:
			if item not in dictInvIndex:
				dictInvIndex[item] = set()
			if item in dictInvIndex:
				dictInvIndex[item].add((i+1))
                
#%%
def queryProcess(words,operators):
    c=0
    ans=dictInvIndex[words[c]]
    for i in operators:
        if i == "and":
            ans=ans.intersection(dictInvIndex[words[c+1]])
        elif i == "or":
            ans=ans.union(dictInvIndex[words[c+1]])
        elif i == "not":
            ans=ans.difference(dictInvIndex[words[c+1]])
        c+=1
    return ans
#%%
print("Ans :")
print(queryProcess(["library","computer"], ["or"]))
#%%
print("Vector Space Model")
data_vector={}
tokens_set=set(tokens_without_sw)
for i in tokens_set:
    data_vector[i]=[]
    for j in range(line):
        data_vector[i].append(original_data[j].count(i))
data=pd.DataFrame(data_vector)
#%%
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.metrics.pairwise import manhattan_distances
from sklearn.metrics import pairwise_distances
#%%
q="national library"
actual_query=[
	ps.stem(word) for word in word_tokenize(q) if not word in stopwords.words() and (not word in punc)]
query_vector=[]
for i in tokens_set:
    query_vector.append(q.count(i))
#%%
query=np.array(query_vector)
query=query.reshape(1,-1)
ans=cosine_similarity(data.to_numpy(),query)
print(ans)
#%%

```
