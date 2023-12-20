import requests
from bs4 import BeautifulSoup
import csv

# 定義 PTT baseball 版的網址
url = 'https://www.ptt.cc/bbs/Education/index.html'

# 設定爬取的頁數
pages_to_crawl = 10

# 創建一个空列表来儲存文章資料
articles_list = []

#要搜尋的關鍵字
keywords = ["獎學金", "教師", "教育"]

# 使用 requests 取得網頁內容
response = requests.get(url)

# 創建一個Session來處理Cookies
session = requests.Session()

for i in range(pages_to_crawl):
    # 使用 requests 取得網頁內容
    response = session.get(url)
    
    # 檢查是否成功取得網頁內容
    if response.status_code != 200:
        print(f'無法取得頁面 {url}')
        break

    # 使用 BeautifulSoup 解析網頁內容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 找出文章標題和連結
    articles = soup.find_all('div', class_='r-ent')
    for article in articles:
        title = article.find('div', class_='title').text.strip()
        
        # 檢查文章內容是否包含"刪除"或其他被刪除的關鍵字
        if "刪除" in title:
            continue  # 跳過已刪除的文章
         
        # 檢查文章内容是否包含關鍵字
        if any(keyword in title.lower() for keyword in keywords):
            article_link = article.find('a')['href']
            date = article.find('div', class_='date').text.strip()
            author = article.find('div', class_='author').text.strip()

            # 將文章資料存為字典
            article_info = {
                '標題': title,
                '日期': date,
                '作者': author,
            }
            articles_list.append(article_info)
            print(f'標題: {title}')
            print(f'日期: {date}')
            print(f'作者: {author}')
        
    # 找出前一頁的連結
    previous_page = soup.find('div', class_='btn-group-paging').find_all('a')[1]['href']
    url = 'https://www.ptt.cc' + previous_page

 # 將資料寫入CSV文件
with open('pttEducation_2.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
    fieldnames = ['標題', '日期', '作者']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for article_info in articles_list:
        writer.writerow(article_info)