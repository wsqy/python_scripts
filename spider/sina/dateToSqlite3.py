# -*- coding:utf-8 -*-
from __future__ import print_function
from gevent import monkey
monkey.patch_all()
from bs4 import BeautifulSoup
import requests
import re
import datetime
import time
import gevent
import RedisObj
from sqlalchemy import *
import sys
reload(sys)
sys.setdefaultencoding('utf8')
head = {
    "Host": "weibo.cn",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate",
    "Referer": "http://weibo.cn/?sudaref=login.sina.com.cn",
    "Cookie": "SUHB=0OMkGf-wWOephU; SSOLoginState=1467294704; ALF=1469886696; SUB=_2A256cVOgDeTxGeVH6FET9C7PyjSIHXVZmn3orDV6PUJbktBeLRHhkW0efhJNESkmL_jow8b4Z8J7qJ2Tlw..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5SiykF55P.JH5gBjcyOFTn5JpX5o2p5NHD95Q01Ke0eoB7e02RWs4Dqcjki--NiKnRi-zpi--fi-2fiKnNi--4iKnpiKnNeK.4S5tt; gsid_CTandWM=4uRACpOz5XsPv9GYJ2WnNgvdm58; _T_WM=9e0da1156509158e26e56afb6bf1d353",
    "Connection": "keep-alive"
}


def get_weibo_count(r):
    if not r:
        return "页面数据获取失败"
    soup = BeautifulSoup(r, "html.parser")
    weiBoAll = soup.select("span[class='tc']")
    reMatch = re.search(r'\d+', weiBoAll[0].string)
    # print(reMatch.group())
    return reMatch.group()


def get_page(page_list):
    while len(page_list) != 0:
        page_num = page_list.pop(0)
        try:
            payload = {"page": page_num}
            url = r"http://weibo.cn/3933240318/profile"
            r = requests.get(url, headers=head, params=payload)
            print("+++++++++++++已经获取到第%d个页面+++++++++++++" % page_num)
            # print(r.text)
            # RedisObj.RedisObj().set_string(page_num, r.text)
        except Exception as e:
            print("获取页面失败：%s" % e)


def get_info(page_list, data_con):
    while len(page_list) != 0:
        page_num = page_list.pop()
        r = RedisObj.RedisObj(3).get_string(page_num)
        if not r:
            print("页面数据获取失败")
            continue
        soup = BeautifulSoup(r, "html.parser")
        weiBoAll = soup.find_all(id=re.compile(r"^M_.{9}$"))
        i = 0
        for weiBOList in weiBoAll:
            try:
                # 微博数
                i = i + 1
                # 检测微博是否有图片说明
                j = 0
                print("+++++++++++++正在解析%d页第%d条微博+++++++++++++" % (page_num, i))
                con = weiBOList.contents[j]
                try:
                    print("来源于：%s" % con.find(class_="cmt").a.string)
                    laiyuan = con.find(class_="cmt").a.string
                except AttributeError as e:
                    print("原创")
                    laiyuan = "原创"
                print("微博标题：%s" % con.find(class_="ctt").text)
                title = con.find(class_="ctt").text
                j += 1
                if len(weiBOList.contents) == 3:
                    con = weiBOList.contents[j]
                    print("演示图片：%s" % con.contents[0].img['src'])
                    picture = con.contents[0].img['src']
                    j += 1
                con = weiBOList.contents[j]
                weibo_time = con.find(class_="ct").string
                print("转发时间：%s" % weibo_time)
                # 下面拼凑时间
                ss = weibo_time.split(" ")[0]
                sss = ss.split()
                if len(sss) == 1:
                    times = re.match(r'(\d)+', sss[0])
                    minutesAgo = (datetime.datetime.now() - datetime.timedelta(minutes=int(times.group())))
                    # 转换为其他字符串格式:
                    otherStyleTime = minutesAgo.strftime("%Y-%m-%d %H:%M:%S")
                    print(otherStyleTime)
                    weibo_update = otherStyleTime
                elif len(sss) == 2 and sss[0] == "今天":
                    time_date = datetime.datetime.now().strftime("%Y-%m-%d")
                    print("%s %s" % (time_date, sss[1]))
                    weibo_update = "%s %s" % (time_date, sss[1])
                elif len(sss) == 2 and "月" in sss[0]:
                    time_date = datetime.datetime.now().strftime("%Y")
                    time_day = sss[0].replace("月", "-").replace("日", "")
                    print("%s-%s %s" % (time_date, time_day, sss[1]))
                    weibo_update = "%s-%s %s" % (time_date, time_day, sss[1])
                else:
                    print(ss)
                    weibo_update = ss
                i = data_con.insert()
                i.execute({
                    "source": laiyuan,
                    "title": title,
                    "preview_picture": picture,
                    "weibo_update": weibo_update
                })
                print("+++++++++++++%d页第%d条微博解析完成++++++++++++++" % (page_num, i))
            except:
                print("出错啦。。。")
            print("+++++++++++++%d页解析完成+++++++++++++\n" % page_num)


def gevent_join(page_list, data_con):
    gevent_task = []
    for each in range(40):
        gevent_task.append(gevent.spawn(get_info, page_list, data_con))
    gevent.joinall(gevent_task)


def op_sqlite():
    db = create_engine('sqlite:///weibo.db')
    db.echo = False
    metadata = MetaData(db)

    data = Table('data', metadata,
        Column('source', String),
        Column('title', String),
        Column('preview_picture', String),
        Column('weibo_update', String),
    )
    data.create()
    return data

if __name__ == "__main__":
    data_con = op_sqlite()
    page_list = range(1, 496)
    startTime = time.time()
    gevent_join(page_list, data_con)
    endTime = time.time()
    print("获取496个页面完成,耗时:%f" % (endTime - startTime))
