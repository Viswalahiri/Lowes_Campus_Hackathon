#data scraping from Lowe's Website
import csv
import os
import selenium
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

# core logic and statements to print out various elements on the lowes site
# web is list of website links
def show_me_the_money(web):
	# If you are running this, you must first install the geckodriver. Please look at another repository of mine called Results_Fetcher where I provide instructions on how to do so.
    # Change directory to web driver
    os.chdir('C://Drivers//Web_Drivers')
    driver = webdriver.Firefox(executable_path=r'C://Drivers//Web_Drivers//geckodriver.exe')
    for website_link in web:
        try:
            driver.get(website_link)
            #item number
            print(driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/section[1]/div[2]/div[1]/p/span[1]').text,end=",")
            #model number
            print(driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/section[1]/div[2]/div[1]/p/span[2]').text,end=",")
            #star rating
            print(driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/section[1]/div[2]/div[3]/div[1]/div/span[1]').text,end=",")
            #percentage rating
            print(driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/section[1]/div[2]/div[3]/div[2]/span[1]').text,end=",")
            #image link in anchor tag
            print(driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/section[1]/div[2]/div[4]/div[3]/a/img').get_attribute("src"),end=",")
            #brand
            print(driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/section[1]/div[2]/div[2]/h1").text.split(' ')[0],end=",")
            #description
            print(' '.join(driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/section[1]/div[2]/div[2]/h1").text.split(' ')[1:]))
            print(driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/section[1]/div[3]/div[2]/div[1]/div[1]/span[1]').text,end=",")
                #then price
            print(driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/section[1]/div[3]/div[2]/div[1]/div[1]/span[3]').text)
            driver.close()
    except :
        print("Error")
        pass
# returns length of file (number of lines)
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

if __name__ == "__main__":
	# All files in directory appliances each have individual links in them.
	#change directory if you'd like to run this
	directory = 'C://Users//Viswa//Documents//Programming//Projects//Lowes//Data_Scraping//Data//appliances'
	for filename in os.listdir(directory):
	    os.chdir(directory)
	    if filename.endswith(".txt"): 
	        b_in = open(filename)
	        size = file_len(filename)
	        data = b_in.readlines()
	        links = []
	        i = 0
	        while(i!=size):
	            link = data[i]
	            links.append(link)
	            i+=1
	        show_me_the_money(links)
	        continue
	    else:
	        continue