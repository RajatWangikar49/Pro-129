import pandas as pd
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

start_url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
browser = webdriver.Chrome("C:/Users/DELL/Desktop/Pro 127/chromedriver.exe")
browser.get(start_url)
time.sleep(10)

page = requests.get(start_url)
soup = BeautifulSoup(page.text, "html.parser")

table = soup.find_all("table", attrs = {"class" ,"wikitable sortable"})
total_table = len(table)
dwarf_data = []

tr_tags = table[2].find_all("tr")

for tr in tr_tags :
    td_tags = tr.find_all("td")
    row = [i.text.strip() for i in td_tags]
    dwarf_data.append(row)

brown_dwarf_data = []

for i in range (2, len(dwarf_data)) :
    Stars_name = dwarf_data[i][0]
    Radius = dwarf_data[i][8]
    Mass = dwarf_data[i][7]
    Distance = dwarf_data[i][5]

    required_data = [Stars_name, Radius, Mass, Distance]
    brown_dwarf_data.append(required_data)

header = ["Star_name", "Radius", "Mass", "Distance"]
dwarf_df = pd.DataFrame(brown_dwarf_data, columns = header)
dwarf_df.to_csv("brown_dwarf_data.csv", index = True, index_label = "id")

