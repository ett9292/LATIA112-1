from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import urllib.parse
import urllib.request as req
import time
import csv

file = open("ptt.txt", mode="a", encoding="utf-8")
articles_list = []

def getcontent(url):
    # 使用 BeautifulSoup 解析 HTML 內容
    request = req.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    })

    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")  # 中文編碼

    soup = BeautifulSoup(data, 'html.parser')

    # 在這裡加入等待元素載入完成的程式碼
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'title')))

    titles = soup.find_all("div", class_="title")

    for title in titles:
        if title.a:
            # 使用換行符號換行
            date = title.find_next("div", class_="date")
            file.write("Title: " + title.a.string + "\n")
            file.write("Date: " + date.string.strip() + "\n")

            article_info = {
                '標題': title.a.string,
                '日期': date.string.strip(),
            }
            articles_list.append(article_info)
            print(f'標題: {title.a.string}')
            print(f'日期: {date.string.strip()}')

    nextlink = soup.find("a", string="‹ 上頁")
    if nextlink:
        next_url = urllib.parse.urljoin(url, nextlink['href'])
        return next_url
    else:
        return None

url = 'https://www.ptt.cc/bbs/Education/index.html'
# 使用selenium模仿瀏覽器
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
chrome_options.add_argument('--headless')  # 在無頭模式下運行，不開啟實際的瀏覽器窗口
driver = webdriver.Chrome(options=chrome_options)

count = 0
while count < 5:
    driver.get(url)
    url = getcontent(url)
    count += 1

file.close()
driver.quit()

with open('pttEducation.csv', 'a', newline='', encoding='utf-8-sig') as csvfile:
    fieldnames = ['標題', '日期']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for article_info in articles_list:
        writer.writerow(article_info)
