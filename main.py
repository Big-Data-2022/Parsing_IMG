import requests
from bs4 import BeautifulSoup
from core.config import HEADERS, URL


#Отправили get запрос и получили html
#________________________________________________________________________________________
response = requests.get(url=URL, headers=HEADERS)
conten_html = response.content
# # print(response.status_code)

with open("core/index.html", "w", encoding="utf-8") as file:
    file.write(str(conten_html))#Страница будет сахранятся как стринг Str
#______________________________________________________________________________________



#________________________________________________________________________________________

with open("core/index.html", "r", encoding="utf-8") as file:
    content_html = file.read()


soup = BeautifulSoup(content_html, 'lxml')
teg_image = soup.find_all('img')


with open("core/index.html", "w", encoding="utf-8") as file:
    file.write(str(teg_image))

#_____________________________________________________________________________
all_image = []

for item in teg_image:
    item_img = item.get("src")
    all_image.append(item_img)
    
with open("core/image.py", "w", encoding="utf-8") as file:
    file.write(f"image = {all_image}")



