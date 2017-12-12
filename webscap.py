import requests
import csv
page1= requests.get("https://www.goodreads.com/shelf/show/young-adult?page=6")
from bs4 import BeautifulSoup
soup1 = BeautifulSoup(page1.content, 'html.parser')
l=[]
r=[]
a=[]
for link in soup1.find_all('a', class_='leftAlignedImage'):
    title = [link.get('title')]
    l.append(title)
for rate in soup1.find_all( "span", {"class":"greyText smallText"} ):
     rating=(rate.get_text())
     r.append(rating)

print(r)
print (title)
for author in soup1.find_all( "span", {"itemprop":"name"} ):
     auth_name=(author.get_text())
     print(auth_name)
     a.append(auth_name)

    
csvfile="/Users/akshaykirane/Desktop/index1.csv"
with open(csvfile, "w") as csv_file:
 writer = csv.writer(csv_file)
 for val in l:
        writer.writerow([val]) 

csvfile="/Users/akshaykirane/Desktop/index2.csv"
with open(csvfile, "w") as csv_file:
    writer = csv.writer(csv_file)
    for val in r:
        writer.writerow([val]) 

csvfile="/Users/akshaykirane/Desktop/index3.csv"
with open(csvfile, "w") as csv_file:
    writer = csv.writer(csv_file)
    for val in a:
        writer.writerow([val]) 






#import pandas as pd
#df = pd.DataFrame({
 #       "title": l, 
#
 #   })
#df.to_excel('index.csv', sheet_name='sheet1', index=TRUE)
