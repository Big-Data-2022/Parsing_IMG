import requests
from bs4 import BeautifulSoup
from core.config import HEADERS, URL


#Отправляем get запрос и получили html
# ----------------------------------------------------------
# response = requests.get(url=URL,headers=HEADERS)
# content_html = response.content

# with open("core/index.html", "w",encoding="utf-8") as file:
#     file.write(str(content_html)) #Страница будет сохронятся как str
# ----------------------------------------------------------

with open("core/index.html", "r", encoding="utf-8") as file:
    content_html = file.read()


soup = BeautifulSoup(content_html, 'lxml')
teg_img = soup.find_all('img')

with open("core/index.html", "w",encoding="utf-8") as file:
    file.write(str(teg_img))


# ----------------------------------------------------
all_image = []

for item in teg_img:
    item_img = item.get('src')
    all_image.append(item_img)

with open("core/image.py", "w", encoding="utf-8") as file:
    file.write(f"image = {all_image}")
# ----------------------------------------------------
