# -*- coding:utf-8 -*-
from __future__ import print_function

from bs4 import BeautifulSoup
import requests
import re
import datetime
import time
import random
import sqlite3
# import gevent
import sys
# from gevent import monkey
# monkey.patch_all()
reload(sys)
sys.setdefaultencoding('utf8')
# Turn off bytecode generation
sys.dont_write_bytecode = True

# # Django specific settings
# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
# import django
# django.setup()
#
# # Import your models for use in your script
# from db.models import *

head = {
    "Host": "weibo.cn",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate",
    "Referer": "http://weibo.cn/3933240318/profile",
    "Cookie": "SCF=Agu1hzaS8OpPBpU6BJqs0xHJKp4AYVNO-yXBBIcFCCnnANA2vK2nUbIsPuqG97uOYnfU9TA98Mj-nGwxyn7DNYw.; SUHB=0rr7hZ8lZb8DLE; ALF=1482040717; _T_WM=53acb94c0941f1ef89cd4c628957e18f; SUB=_2A251KujJDeTxGeVH6FET9C7PyjSIHXVW1IiBrDV6PUJbktBeLVjXkW2R7Cb0IFhChu0oUdMWbfBUEJQhkA..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5SiykF55P.JH5gBjcyOFTn5JpX5o2p5NHD95Q01Ke0eoB7e02RWs4Dqcjki--NiKnRi-zpi--fi-2fiKnNi--4iKnpiKnNeK.4S5tt",
    "Connection": "keep-alive"
}


# URL数字改成自己的
def get_page(page_num=1):
    try:
        payload = {"page": page_num}
        url = r"http://weibo.cn/3933240318/profile"
        r = requests.get(url, headers=head, params=payload)
        print("+++++++++++++已经获取到第%d个页面+++++++++++++" % page_num)
        return r.text
    except Exception as e:
        print("获取页面失败：%s" % e)
        return


def formatDateTime(time):
    if len(time) == 1:
        times = re.match(r'(\d)+', time[0])
        minutesAgo = (datetime.datetime.now() - datetime.timedelta(minutes=int(times.group())))
        return minutesAgo.strftime("%Y-%m-%d %H:%M:%S")
    elif len(time) == 2 and time[0] == "今天":
        time_date = datetime.datetime.now().strftime("%Y-%m-%d")
        return "%s %s:%s" % (time_date, time[1], random.randint(10, 55))
    elif len(time) == 2 and "月" in time[0]:
        time_date = datetime.datetime.now().strftime("%Y")
        time_day = time[0].replace("月", "-").replace("日", "")
        return "%s-%s %s:%s" % (time_date, time_day, time[1], random.randint(10, 55))
    else:
        return "%s %s" % (time[0], time[1])


def weibo_author(con):
    try:
        laiyuan = con.find(class_="cmt").a.string
    except AttributeError as e:
        # 代表自己发布的
        laiyuan = 0
    # print(laiyuan)
    # 『超级有用的9个PHP代码片段 – 码农网』http://t.cn/RfKkt9V
    title_old = con.find(class_="ctt").text
    # print(title_old)
    index = title_old.find("http")
    # print(index)
    if index != -1:
        title = title_old[:index]
        # print(title)
        # print("-------")
        # print(title_old[index:])
        r = requests.get(title_old[index:])
        url = r.url
        # print(url)
    else:
        title = title_old
        try:
            url = con.find(class_="ctt").a["href"]
            # url = requests.get(url).url
        except TypeError as e:
            # 代表无来源信息
            url = 0
        else:
            if not url.startswith("http"):
                url = 0
    return laiyuan, title, url


def get_info(r):
    if not r:
        return "页面数据获取失败"
    soup = BeautifulSoup(r, "html.parser")
    weiBoAll = soup.find_all(id=re.compile(r"^M_.{9}$"))
    for weibo_num, weiBOList in enumerate(weiBoAll, 1):
        print("+++++++++++++正在解析本页第%d条微博+++++++++++++" % weibo_num)
        # 解析发布人信息
        laiyuan, title, url = weibo_author(weiBOList.contents[0])
        print(laiyuan, "\t", title, "\t", url)
        # 解析发布时间
        ss = weiBOList.contents[-1].find(class_="ct").string

        time = formatDateTime(ss.split(" ")[0].split())
        print(time)
        website = re.search(r"(?i)https?://(\w+\.){1,4}[a-z0-9]+", url).group() if url else url
        print("website:%s" % website)
        print("+++++++++++++本页第%d条微博解析完成++++++++++++++" % weibo_num)
        info = {
            "laiyuan": laiyuan,
            "title": title,
            "url": url,
            "time": time,
            "website": website,
        }
        sql_demo(info)
    print("+++++++++++++本页解析完成+++++++++++++\n")


# def sql_demo(info):
#     Weibo.objects.create(**info)
#     print("11111111111111111111")


if __name__ == '__main__':
    # con = get_page(4)
    # get_info(con)
    get_info(get_page(page_num=1))
    # sql_demo()
