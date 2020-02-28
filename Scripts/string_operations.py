import re
import os
import sqlite3
import pickle
import nltk
from nltk.corpus import wordnet 
from nltk.stem import WordNetLemmatizer 
import importlib
# from hash_map_operations import initial_data_dump,read_hash_map,create_hash_map,update_hash_map,access_hash_map
# from database_access import initial_data_dump_in_db,insert_to_db

def all_syno(word):
    word = '_'.join(word.split(" "))
    all_syn = []
    lemmatizer = WordNetLemmatizer()
    lemmatized_input = lemmatizer.lemmatize(word)
    syns = wordnet.synsets(lemmatized_input,)   
    for i in range(len(syns)):
        lemmas = syns[i].lemmas()
        for i in lemmas:
            if (i.name()) not in all_syn:
                all_syn.append('_'.join(i.name().lower().split('-')))
    # print(all_syn)
    return(all_syn)
def parse_string(string):
	b= []
	c= []
	a = re.findall(r"[\w']+", string)
	for i in range(len(a)-1):
		if(a[i].isdigit() and a[i+1].isdigit()):
			b.append(str(int(a[i])-2))
			b.append(str(int(a[i])-1))
			b.append(str(int(a[i])))
			b.append(str(int(a[i])+1))
			b.append(str(int(a[i])+2))
			b.append(a[i+1])
	for i in a:
		if(i not in b):
			if(i == 'cu'):
				c.append('cubic')
			elif(i == 'sq'):
				c.append('square')
			elif(i == 'ft'):
				c.append('feet')
			else:
				c.append(i)
	b = b[:-1]
	b.extend(c)
	# print(b)
	return b
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
