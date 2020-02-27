import re
import os
import sqlite3
import pickle
import nltk
import importlib
from nltk.corpus import wordnet 
from nltk.stem import WordNetLemmatizer
# from string_operations import all_syno,parse_string,file_len
# from hash_map_operations import initial_data_dump,read_hash_map,create_hash_map,update_hash_map,access_hash_map

def initial_data_dump_in_db():
	conn = sqlite3.connect('inventory.db')
	c = conn.cursor()
	c.execute(""" CREATE TABLE inventory(website_link text, product_number text, model_number text, star_rating real, recommendation_chance real, asset_link text, brand_name text, product_description text, was_price real, is_price real)""")
	#SQL Statements
	conn.commit()
	data_stream = open("usable_data.csv")
	data = data_stream.readlines()
	l = file_len("usable_data.csv")
	for i in range(0,l):
		website_link, product_number, model_number, star_rating, recommendation_chance,asset_link,brand_name, product_description, was_price, is_price = data[i].split(",")
		c.execute("INSERT INTO inventory VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (website_link, product_number, model_number, star_rating, recommendation_chance, asset_link, brand_name, product_description, was_price, is_price))
	conn.commit()
	print("Database Insertion Done")

def insert_to_db():
	product_1 = Product(website_link, product_number, model_number, star_rating, recommendation_chance,asset_link,brand_name, product_description, was_price, is_price)
	try:
		c.execute("INSERT INTO inventory VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",(Product.website_link, Product.product_number, Product.model_number, Product.star_rating, Product.recommendation_chance,Product.asset_link,Product.brand_name, Product.product_description, Product.was_price, Product.is_price))
		conn.commit()
		parse_string(Product.product_description)
		# conn.close()
	except:
		pass

