import re
import os
import sqlite3
import pickle
import nltk
from nltk.corpus import wordnet 
from nltk.stem import WordNetLemmatizer 
import importlib
from string_operations import *
# from database_access import initial_data_dump_in_db,insert_to_db

def initial_data_dump():
	data_stream = open("initial_data.csv")
	data = data_stream.readlines()
	app_list = ['refrigerator', 'fridge', 'freezer', 'chiller', 'cooler', 'icebox','oven', 'stove', 'range', 'kiln', 'roaster','dishwasher','dish','wahing_machine', 'washer', 'washing','machine', 'dryer', 'drier', 'clothes','microwave','rug','carpet','mat']
	colors_list = ['black','white','silver','red','blue','green','yellow']
	l = file_len("initial_data.csv")
	for i in range(0,l):
		prod_id,string = data[i].split(",")
		p = parse_string(string)
		# print(p)
		p_syn = []
		for i in p:
			if( i.lower() in colors_list):
				p_syn.extend([i.lower()])
				# print(i)
			elif( i.lower() in app_list):
				# print(i.lower())
				# print(all_syno(i.lower()))
				p_syn.extend(all_syno(i.lower()))
			else:
				if(len(all_syno(i)) > 2):
					p_syn.extend(all_syno(i.lower())[0:2])
		update_hash_map(p_syn,prod_id)

def dynamic_data_dump(prod_id,string):
	app_list = ['refrigerator', 'fridge', 'freezer', 'chiller', 'cooler', 'icebox','oven', 'stove', 'range', 'kiln', 'roaster','dishwasher','dish', 'washer', 'washing','machine', 'dryer', 'drier', 'clothes','microwave','rug','carpet','mat']
	colors_list = ['black','white','silver','red','blue','green','yellow']
	p = parse_string(string)
	p_syn = []
	for i in p:
		if( i.lower() in colors_list):
			p_syn.extend([i.lower()])
			# print(i)
		elif( i.lower() in app_list):
			p_syn.extend(all_syno(i.lower()))
		else:
			if(len(all_syno(i.lower())) > 2):
				p_syn.extend(all_syno(i.lower())[0:2])
	update_hash_map(p_syn,prod_id)	

def create_hash_map():
	my_dict={'zzy':[102]}
	with open('product_synonym_hash.pkl','wb') as f:
		pickle.dump(my_dict,f)
def update_hash_map(p,prod_id):
	my_dict_1={}
	with open('product_synonym_hash.pkl','rb') as f:
		my_dict_1 = pickle.load(f)
	for i in p:
		if i in my_dict_1:
			if prod_id not in my_dict_1[i]:
				my_dict_1[i].append(prod_id)
		else:
			my_dict_1[i] = []
			my_dict_1[i].append(prod_id)
	with open('product_synonym_hash.pkl','wb') as f:
		pickle.dump(my_dict_1,f)	
def read_hash_map():
	my_dict_2={}
	with open('product_synonym_hash.pkl','rb') as f:
		my_dict_2 = pickle.load(f)
	print(my_dict_2)
def access_hash_map(query):
	p = parse_string(query)
	p_syn = []
	for i in p:
		p_syn.extend(all_syno(i))
	most_relevant = {}
	with open('product_synonym_hash.pkl','rb') as f:
		my_dict_4 = pickle.load(f)
	for i in p_syn:
		if(i in my_dict_4):
			for j in my_dict_4[i]:
				if j not in most_relevant:
					most_relevant[j] = 1
				else:
					most_relevant[j]+=1
	return(sorted((most_relevant[count], count) for count in most_relevant)[-2:])