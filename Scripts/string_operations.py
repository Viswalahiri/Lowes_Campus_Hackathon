#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""string_operations.py: Contains core NLP Operations of API service."""

__author__ = "Viswalahiri Swamy Hejeebu"
__credits__ = ["Viswalahiri Swamy Hejeebu"]
__license__ = "MIT"
__version__ = "0.1.0"
__maintainer__ = "Viswalahiri Swamy Hejeebu"
__email__ = 'viswalahiriswamyh@gmail.com'
__status__ = 'Dev'


import importlib
import re

import nltk
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer


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
	return(all_syn)

def parse_string(string):
	b = []
	c = []
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
	return b

def file_len(fname):
	with open(fname) as f:
		for i, l in enumerate(f):
			pass
	return i + 1
