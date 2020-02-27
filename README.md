[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/made-with-javascript.svg)](https://forthebadge.com)
# Lowes_Campus_Hackathon
## Solution to Problem Theme #2.
## **Build a conversational solution that enables customers to discover and order products**

This is a developmental project that acts as a solution to problem 2 of [this competition](https://www.techgig.com/hackathon/lowes-campus-hackathon).

## Tools & Services Used

The various tools and services used include 
 - AWS Elastic Beanstalk
 - Google Dialogflow
 - Kommunicate

## Steps of Development

### Step 1 : Data Scraping

Approximately 100 rows of Product Data was scraped using a python script that made use of Selenium.

**[This](https://github.com/Viswalahiri/Lowes_Campus_Hackathon/blob/master/Datasets/usable_data.csv)** is the csv file that was obtained after scraping the data.

**[This](https://github.com/Viswalahiri/Lowes_Campus_Hackathon/blob/master/Scripts/data_scraper.py)** is the python script that handled data scraping.

These lines of data concentrate on only the following goods that Lowe's Sells on its [website](https://www.lowes.com/)
- Appliances
  - Refrigerators
  - Washing Machines
  - Microwaves
  - Dishwashers
  - Oven / Ranges
  - Driers
- Home-Decor
  - Area Mats
  - Bathroom Mats
  - Rugs
  
#### **NOTE**: The values of Prices (Discounted and Current) are dummy values. This had to be done due to inconsistencies.
  
## Step 2 : Create a SQLite3 Database and Insert Scraped Data

The motivation to choose SQLite3 is due to the fact that the list of products always increases, and we needed a mechanism to enable that products get added. Along with this, we felt the need for a querying mechanism. This is help us answer more advanced questions from the user. 

Additionally, it seemed to match the requirements for an Open Source RDBMS as in the Rules, and had a vast community and good support.

**[This]()** is the python scipt that enabled creation of the SQLite3 database. 

The **initial_data_dump_in_db()** was the responsible method.

Good database practices were followed while CREATEing and INSERTing values into the database, such as making it SQL-injection proof.

## Step 3 : Perform String Parsing on Individual Product Descriptions

## Prerequisites

This package assumes you use Python 3.x. 

Expected package dependencies are listed in the "requirements.txt" file for PIP, you need to run the following command to get dependencies:
```
pip install -r requirements.txt
```


## Contributing

1. [Fork](https://github.com/Viswalahiri/Lowes_Campus_Hackathon/fork) this project.
2. Commit your changes.
3. Create a new Pull Request and link an [issue](https://github.com/Viswalahiri/Lowes_Campus_Hackathon/issues/new) with it.


## Meta [![GitHub followers](https://img.shields.io/github/followers/viswalahiri.svg?style=social&label=Follow&maxAge=2592000)](https://github.com/viswalahiri?tab=followers)


| Name | Github | LinkedIn | E-mail | Phone|
| --- | --- | --- | --- | --- |
| Viswalahiri Swamy Hejeebu | [@viswalahiri](https://github.com/viswalahiri) | [@viswalahiri](https://www.linkedin.com/in/viswalahiri/) |[E-mail](mailto:viswalahiriswamyh@gmail.com) | [(+91) 630-152-9655](tel:+916301529655)
| Kurapati Abhilash |[@abhilash](https://github.com/abhikurapati23)| [@abhilash](https://www.linkedin.com/in/kurapati-abhilash-27bbaa185/) | [E-mail](mailto:abhilash2057@gmail.com) | [(+91) 850-072-8944](tel:+918500728944)

<!--
Viswalahiri Swamy Hejeebu – [@viswalahiri](https://github.com/viswalahiri) – Message me on [LinkedIn](https://www.linkedin.com/in/viswalahiri/) or send me an [e-mail](mailto:viswalahiriswamyh@gmail.com) for any queries.

Kurapati Abhilash – Message him on [LinkedIn](https://www.linkedin.com/in/kurapati-abhilash-27bbaa185/) or send him an [e-mail](mailto:abhilash2057@gmail.com) for any queries.
-->

Distributed under the [MIT Liscence](https://opensource.org/licenses/MIT). See [`LICENSE`](https://github.com/Viswalahiri/Lowes_Campus_Hackathon/blob/master/LICENSE) for more information.
