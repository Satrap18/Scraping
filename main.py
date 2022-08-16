from bs4 import BeautifulSoup
import requests

# geeksforgeeks python history url
url = requests.get('https://www.geeksforgeeks.org/history-of-python/')

soup = BeautifulSoup(url.content, 'lxml')

#print(soup.title.text)

s = soup.find_all('div', class_='text')

for text in s:
    t = text.text

with open('history.html', 'w',encoding='utf-8') as file:
    file.write(str(t))