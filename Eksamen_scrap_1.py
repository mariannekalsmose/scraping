#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 19:22:16 2026

@author: mariannemollerkalsmose
"""


import requests
from bs4 import BeautifulSoup
import os
import time
import pandas as pd

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,"
        " like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )
}

# Create a local directory to store downloaded HTML files
output_dir = "laureates"
if not os.path.exists(output_dir):
  os.makedirs(output_dir)

url = "https://en.wikipedia.org/wiki/List_of_Nobel_laureates"
try:
    print("Fetching:",url)

    # HTTP GET request
    response = requests.get(url, headers=headers, timeout=10)

    # if the request succeeded
    if response.status_code == 200:
      filename = "laureates.html"
      file_path = output_dir + "/" + filename

      # Save HTML text to pages directory
      with open(file_path, "w", encoding="utf-8") as f:
        f.write(response.text)
    
      print(url,"saved successfully to",file_path)

    else:
      print("Failed to download",url,"Status code:",response.status_code)

except requests.exceptions.RequestException as e:
   print("A network error occurred:",e)




laureates = []
# reading from downloaded file
page = open(output_dir + "/" + 'laureates.html','r',encoding='utf-8').read()
soup = BeautifulSoup(page,features="lxml")

# finding the table that holds all the links
table = soup.find('table',attrs={'id':'mwmg'})

# finding all links in the DOM element
links = table.findAll('a',attrs={'rel':'mw:WikiLink'})



# for link in links:    
#     try:
#         t = link["title"]
#     except Exception:
#         print(link)


#scrape each page
for link in links:
    
    name = link['title']
    
    try:
        print("Getting laureates: ",name)
        url = link['href']
           
        response = requests.get(url, headers = headers, timeout=10)
                
        if response.status_code == 200:
                    
            with open(output_dir + "/" + name + ".html", 'w') as f:
                        f.write(response.text)
        else:
            print("Failed to download",url,"Status code:",response.status_code)
        #time.sleep(5)
    except requests.exeption.RequestExeption as e:
        print("A network error occurred:",e)

#    time.sleep(5)









# full_name = ""
# gender = ""
# birth_date = ""
# death_date = "" 
# birth_city = ""
# birth_country = ""
# place_of_education = ""
# award_year = ""
# award_category = ""
# motivation_statement = ""



# laureates.append([full_name, gender, birth_date,
# death_date, birth_city, birth_country, place_of_education, award_year, award_category,motivation_statement])

# df = pd.DataFrame(laureates,columns = ['full_name', 'gender', 'birth_date',
# 'death_date', 'birth_city', 'birth_country', 'place_of_education', 'award_year', 'award_category','motivation_statement'])
# df.to_csv('laureates.csv', index=False, encoding='utf-8')






        