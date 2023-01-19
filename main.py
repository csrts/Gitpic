import requests
from bs4 import BeautifulSoup
import schedule
import time
import telegram

bot = telegram.Bot(token='YOUR_TELEGRAM_BOT_TOKEN')

def job():
    # 爬取网页源码
    url = "https://tool.lu/todayonhistory/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # 取出部分内容
    text = soup.find_all("li").get_text()

    # 创建搜索 URL
    search_url = "http://www.google.com/search?q="
    query = text.split(" ")[-1]
    url = search_url + query

    # 发送消息
    bot.send_message(chat_id='YOUR_CHAT_ID', text=text + ' ' + url)

# 每天8点运行
schedule.every().day.at("8:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
