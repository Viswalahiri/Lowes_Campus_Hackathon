#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""database_access.py: Enables dumping of product information into SQLite3 Database."""

__author__ = "Viswalahiri Swamy Hejeebu"
__credits__ = ["Viswalahiri Swamy Hejeebu"]
__license__ = "MIT"
__version__ = "0.1.0"
__maintainer__ = "Viswalahiri Swamy Hejeebu"
__email__ = 'viswalahiriswamyh@gmail.com'
__status__ = 'Dev'


import importlib
import sqlite3

from string_operations import *


def initial_data_dump_in_db():
	conn = sqlite3.connect('database/inventory.db')
	c = conn.cursor()
	c.execute(""" CREATE TABLE inventory(website_link text, product_number text, model_number text, star_rating real, recommendation_chance real, asset_link text, brand_name text, product_description text, was_price real, is_price real)""")
	#SQL Statements
	conn.commit()
	data_stream = open("scraped_data/usable_data.csv")
	data = data_stream.readlines()
	l = file_len("scraped_data/usable_data.csv")
	for i in range(0, l):
		website_link, product_number, model_number, star_rating, recommendation_chance,asset_link,brand_name, product_description, was_price, is_price = data[i].split(",")
		c.execute("INSERT INTO inventory VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (website_link, product_number, model_number, star_rating, recommendation_chance, asset_link, brand_name, product_description, was_price, is_price))
	conn.commit()
	print("Database Insertion Done")
