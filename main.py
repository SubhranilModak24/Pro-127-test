from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

# Website URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

# Start webdriver
browser = webdriver.Edge("msedgedriver.exe")
# browser = webdriver.Edge()
browser.get(START_URL)

time.sleep(10)
# Array to store scraped data
scraped_data = []

soup = BeautifulSoup(browser.page_source, 'html.parser')

# Defining the Scraping method
def scrape():
    # Find Table
    bstar_table = soup.find("table", attrs={"class": "wikitable"})
    
    # Find body
    bstar_body = bstar_table.find('tbody')
    
    # Find tr
    table_rows = bstar_body.find_all('tr')
    
    # Get data from td
    for row in table_rows:
        table_cols = row.find_all('td')
        print(table_cols)
        
        temp_list = []
        
        for col_data in table_cols:
            # Printing only columns textual data using .text property
            # print(col_data.text)
            
            # Removing extra white spaces using white spaces
            data = col_data.text.strip()
            print(data)
            
            temp_list.append(data)
        
        scraped_data.append(temp_list)