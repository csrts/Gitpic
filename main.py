from lxml import html
import requests
import schedule
import time
from aiogram.bot import Bot
from aiogram.types import Message

bot = Bot(token='YOUR_TELEGRAM_BOT_TOKEN')

async def job():
    # 爬取网页源码
    url = "https://tool.lu/todayonhistory/"
    page = requests.get(url)
    tree = html.fromstring(page.content)

    # 取出所有<li>标签中的内容
    tohlis = tree.xpath('//li')

    # 遍历所有<li>标签
    for li in tohlis:
        text = li.text_content()

        # 创建搜索 URL
        search_url = "http://www.google.com/search?q="
        query = text.split(" ")[-1]
        url = search_url + query

        # 发送消息
        await bot.send_message(chat_id='YOUR_CHAT_ID', text=text + ' ' + url)

# 每天8点运行
schedule.every().day.at("8:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
