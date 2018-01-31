# -*- coding:utf-8 -*-
import requests
from pyquery import PyQuery as pq

head = {
    "Host": "weibo.cn",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate",
    "Referer": "http://weibo.cn/?sudaref=login.sina.com.cn",
    "Cookie": "SUHB=0LcSmw1b7a_ntm; SCF=At9_XRE4e4mMo6zR4OZQTzbUPgjlr6o6A8yPPkKQSqwPcDBOlbLnqZKMNMSnOMhW1JGvIK2etx2q3ru5RiGD3hk.; _T_WM=8d9a46417fd44590235eb5ba612dd56d; ALF=1495977071; SUB=_2A250B08sDeRhGeVH6FET9C7PyjSIHXVXCFFkrDV6PUJbktBeLVX4kW1kgVr0m_ijckLwuIu5Jq2P07KGiw..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5SiykF55P.JH5gBjcyOFTn5JpX5o2p5NHD95Q01Ke0eoB7e02RWs4Dqcjki--NiKnRi-zpi--fi-2fiKnNi--4iKnpiKnNeK.4S5tt",
    "Connection": "keep-alive"
}


def get_page(page_num=1):
    try:
        payload = {"page": page_num}
        url = r"http://weibo.cn/3933240318/profile"
        r = requests.get(url, headers=head, params=payload)
        print("+++++++++++++get page:%d+++++++++++++" % page_num)
        return r.content, page_num
    except Exception as e:
        print("get page error：%s" % e)
        get_page(page_num)


def get_info(r, page_num):
    if not r:
        return "get page error"
    print("loading....")
    doc = pq(r)
    d = doc("div[id^='M_']")
    # print(doc.html())
    print d.html()


if __name__ == "__main__":
    # r, page = get_page(1)
    # print(r)
    # get_info(r, page)
    url = "https://weibo.cn/3933240318/profile?page=2"
    r = requests.get(url, headers=head)
    doc = pq(r.content)
    d = doc("div[id^='M_']")
    for _d in d.items():
        print _d.text()[:10]
        print("-----")
