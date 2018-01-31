from bs4 import BeautifulSoup
import requests
import re
import datetime
import ProxiesList




head = {
    "Host":" weibo.cn",
    "User-Agent":" Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate",
    "Referer":"http://weibo.cn/?sudaref=login.sina.com.cn",
    "Cookie": "SUHB=0OMkGf-wWOephU; SSOLoginState=1467294704; ALF=1469886696; SUB=_2A256cVOgDeTxGeVH6FET9C7PyjSIHXVZmn3orDV6PUJbktBeLRHhkW0efhJNESkmL_jow8b4Z8J7qJ2Tlw..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5SiykF55P.JH5gBjcyOFTn5JpX5o2p5NHD95Q01Ke0eoB7e02RWs4Dqcjki--NiKnRi-zpi--fi-2fiKnNi--4iKnpiKnNeK.4S5tt; gsid_CTandWM=4uRACpOz5XsPv9GYJ2WnNgvdm58; _T_WM=9e0da1156509158e26e56afb6bf1d353",
    "Connection": "keep-alive"
}


def get_page(page_num=1):
    try:
        payload = {"page": page_num}
        url = r"http://weibo.cn/3933240318/profile"
        r = requests.get(url, headers=head, params=payload)
        print("+++++++++++++已经获取到第%d个页面+++++++++++++" % page_num)
        return r.text
    except Exception as e:
        print("获取页面失败，因为%s" % e)
        get_page(page_num)


def get_info(r):
    if not r:
        return "页面数据获取失败"
    soup = BeautifulSoup(r, "html.parser")
    weiBoAll = soup.find_all(id=re.compile(r"^M_.{9}$"))
    i = 0
    for weiBOList in weiBoAll:
        # 微博数
        i = i+1
        # 检测微博是否有图片说明
        j = 0
        print("+++++++++++++正在解析本页第%d条微博+++++++++++++" % i)
        con = weiBOList.contents[j]
        print("来源于：%s" % con.find(class_="cmt").a.string)
        print("微博标题：%s" % con.find(class_="ctt").text)
        j += 1
        if len(weiBOList.contents) == 3:
            con = weiBOList.contents[j]
            print("演示图片：%s" % con.contents[0].img['src'])
            j += 1
        con = weiBOList.contents[j]
        weibo_time = con.find(class_="ct").string
        print("转发时间：%s" % weibo_time)
        # 下面拼凑时间
        ss = weibo_time.split(" ")[0]
        sss = ss.split()
        if len(sss) == 1:
            times = re.match(r'(\d)+', sss[0])
            minutesAgo = (datetime.datetime.now() - datetime.timedelta(minutes = int(times.group())))
            print(minutesAgo)
            #转换为其他字符串格式:
            otherStyleTime = minutesAgo.strftime("%Y-%m-%d %H:%M:%S")
            print(otherStyleTime)
        elif len(sss) == 2 and sss[0] == "今天":
            time_date = datetime.datetime.now().strftime("%Y-%m-%d")
            print("%s %s" % (time_date, sss[1]))
        elif len(sss) == 2 and "月" in sss[0]:
            time_date = datetime.datetime.now().strftime("%Y")
            time_day = sss[0].replace("月", "-").replace("日", "")
            print("%s-%s %s" % (time_date, time_day, sss[1]))
        else:
            print(ss)
        print("+++++++++++++本页第%d条微博解析完成++++++++++++++" % i)

    print("+++++++++++++本页解析完成+++++++++++++\n")
    
if __name__ == "__main__":
    r = get_page(410)
    get_info(r)