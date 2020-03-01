#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""app.py: Contains Flask Application for Web API."""

__author__ = "Viswalahiri Swamy Hejeebu"
__credits__ = ["Viswalahiri Swamy Hejeebu"]
__license__ = "MIT"
__version__ = "0.1.0"
__maintainer__ = "Viswalahiri Swamy Hejeebu"
__email__ = 'viswalahiriswamyh@gmail.com'
__status__ = 'Dev'


import importlib
import json
import os
from os import path
import sqlite3
import subprocess

import flask
import requests
from flask import (Flask, flash, redirect, render_template, request, session,
                   url_for)

from hash_map_operations import *

app = app = flask.Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')


@app.route("/update_db",methods = ['POST'])
def update_db():
	website_link, product_number, model_number, star_rating, recommendation_chance,asset_link,brand_name, product_description, was_price, is_price, dummy = [str(x) for x in request.form.values()]
	THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
	inventory_ = os.path.join(THIS_FOLDER, 'inventory.db')
	conn = sqlite3.connect(inventory_)
	c = conn.cursor()
	c.execute("SELECT product_number FROM inventory WHERE product_number = ?",(product_number,))
	try:
		if(c.fetchone() == None):
			c.execute("INSERT INTO inventory VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (website_link, product_number, model_number, star_rating, recommendation_chance, asset_link, brand_name, product_description, was_price, is_price))
			conn.commit()
			dynamic_data_dump(product_number,product_description)
			return render_template('index.html', confirmation_text = 'Details have been uploaded.')
		else:
			return render_template('index.html', confirmation_text = 'Duplicate detected.')
	except:
		return render_template('index.html', confirmation_text = 'Error.')
		pass


@app.route("/general_search/<string:n_query>",methods = ['GET'])
def general_search(n_query):
	query = ' '.join(n_query.split('%'))
	THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
	inventory_ = os.path.join(THIS_FOLDER, 'inventory.db')
	conn = sqlite3.connect(inventory_)
	c = conn.cursor()
	m = []
	for i in access_hash_map(query):
		c.execute(" SELECT website_link,asset_link,product_description,is_price,star_rating FROM inventory WHERE product_number = {0}".format(i[1]))
		m.append(c.fetchall())
	main_json = []
	count = 0
	for i in m:
		for j in i:
			my_json_string = {'website_link': j[0], 'asset_link': j[1],'product_description':j[2], 'now_price':str(int(j[3])), 'ratings':str(j[4])}
			count += 1
			main_json.append(my_json_string)
	serialized = json.dumps(main_json, sort_keys = True, indent = 3)
	return serialized

@app.route("/demo")
def demo():
	return render_template('trial_indian_web.html')

if __name__ == "__main__":
    app.run(debug = True)
