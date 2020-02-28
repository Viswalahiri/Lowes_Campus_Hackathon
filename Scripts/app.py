import json
import subprocess
import shodan
import flask
from flask import Flask, render_template, request, session, redirect, url_for, flash
import requests
import sqlite3
from hash_map_operations import *

app = app = flask.Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')


@app.route("/update_db",methods=['POST'])
def update_db():
	website_link, product_number, model_number, star_rating, recommendation_chance,asset_link,brand_name, product_description, was_price, is_price = [str(x) for x in request.form.values()]
	conn = sqlite3.connect('inventory.db')
	c = conn.cursor()
	c.execute("SELECT product_number FROM inventory WHERE product_number = ?",(product_number,))
	try:
		if(c.fetchone() == None):
			c.execute("INSERT INTO inventory VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (website_link, product_number, model_number, star_rating, recommendation_chance, asset_link, brand_name, product_description, was_price, is_price))
			conn.commit()
			dynamic_data_dump(product_number,product_description)
			return render_template('index.html', confirmation_text='Details have been uploaded.')
		else:
			return render_template('index.html', confirmation_text='Duplicate detected.')		
	except:
		return render_template('index.html', confirmation_text='Error.')				
		pass

@app.route("/general_search",methods=['POST'])
def general_search():
	#take inputs - assigned to Pranay Annaya

	# query = "smart wifi enabled black drier"
	conn = sqlite3.connect('inventory.db')
	# print(access_hash_map(query))
	c = conn.cursor()
	m = []
	for i in access_hash_map(query):
		c.execute(" SELECT website_link,asset_link,product_description,is_price,star_rating FROM inventory WHERE product_number={0}".format(i[1]))
		m.append(c.fetchall())
	main_json ={}
	count = 0
	for i in m:
		for j in i:
			my_json_string = {'website_link': j[0], 'asset_link': j[1],'product_description':j[2], 'now_price':str(int(j[3])), 'ratings':str(j[4])}
			count+=1
		main_json['Product_'+str(count)] = my_json_string
	serialized= json.dumps(main_json, sort_keys=True, indent=3)
	return serialized
	
if __name__ == "__main__":
    app.run(debug=True)
