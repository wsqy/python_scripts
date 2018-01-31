import os
import requests
from bs4 import BeautifulSoup 
import sqlite3

#创建数据库，如已存在先删除
def create_db():
    if os.path.exists('ip.db'):
        os.remove('ip.db')
    conn = sqlite3.connect('ip.db')
    cursor = conn.cursor()
    cursor.execute('create table ip(ip varchar(20), port int)')
    #cursor.execute(r"insert into ip values ('192.168.1.1',95)")
    cursor.close()
    conn.commit()
    conn.close()

"""
通过西刺代理获取代理ip,启动前先检查可以的代理ip个数，如果少于5个，就再次获取，
正常状态为{ip,类型，端口，验证次数(正常为3，连接失败减一次，
连接成功设为3，当次数为0的时候删除此条代理)}
"""

Headers ={
    "Host" : "www.xicidaili.com",
    "Cookie" : "CNZZDATA1256960793=1662416928-1459134890-%7C1461144106; _free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJTUzYzVkYmViZWYzNDY5YjFlNWVhNjFkZDhlYWZkYTE2BjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMUI1aTgrenAzTXBiUVpqQ21CZjh4MlFQRE1RWjZJMzl3ZnNweEs2azhTc3c9BjsARg%3D%3D--2c0a55d5198a778ed50af34e2b356ab878c17d72",
    "User-Agent" : r"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0",
    "Accept" : r"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept_Language" : "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept_Encoding" : r"gzip, deflate",
    "Connection" : r"keep-alive",
    "Cache-Control": r"max-age=0",
}
 
#获取代理ip
def getIPList():
    r = requests.get(r"http://www.xicidaili.com/nn/",headers=Headers)
    soup = BeautifulSoup(r.text,"html5lib")
    ListProxy = soup.find_all("tr")
    create_db()
    conn = sqlite3.connect('ip.db')
    cursor = conn.cursor()
    for i in ListProxy:
        info = i.find_all("td",limit = 3)
        i = 0
        a=[]
        for j in info:
            if i:
                a.append(j.string)
            i =i+1
        if len(a):
            cursor.execute(r"insert into ip values ('%s',%s)" % (a[0],a[1]))
    cursor.close()
    conn.commit()
    conn.close()
    print("---------完成---------------")

if __name__ == "__main__":
    getIPList()
    
