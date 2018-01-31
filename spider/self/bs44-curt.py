# -*-coding:utf-8-*-
from bs4 import BeautifulSoup
import requests
import re
r = '''
<div class="c" id="M_DvDx2nD11">
111
</div>
<div class="c" id="M_DvDx2nD22">
222
</div>
<div class="c" id="M_DvDx2nD33">
333
</div>
'''
rr = '''
  <div class="c" id="M_DvDwAlO11">
   <div>
    <span class="cmt">
     转发了
     <a href="http://weibo.cn/u/2832482174">
      程序员俱乐部
     </a>
     <img alt="M" src="http://u1.sinaimg.cn/upload/h5/img/hyzs/donate_btn_s.png"/>
     的微博:
    </span>
    <span class="ctt">
     【非常上档次的HTML5/CSS3登录表单】在线演示：
     <a href="http://weibo.cn/sinaurl?f=w&amp;u=http%3A%2F%2Ft.cn%2FRz2hqX8&amp;ep=DvDwAlOh4%2C3933240318%2CDvD1WzkQl%2C2832482174">
      http://t.cn/Rz2hqX8
     </a>
     源码下载：
     <a href="http://weibo.cn/sinaurl?f=w&amp;u=http%3A%2F%2Ft.cn%2F8s0vaz6&amp;ep=DvDwAlOh4%2C3933240318%2CDvD1WzkQl%2C2832482174">
      http://t.cn/8s0vaz6
     </a>
    </span>
   </div>
   <div>
    <a href="http://weibo.cn/mblog/pic/DvD1WzkQl?rl=1">
     <img alt="图片" class="ib" src="http://ww3.sinaimg.cn/wap180/a8d43f7egw1f3varqsvoij20gc0baab8.jpg"/>
    </a>
    <a href="http://weibo.cn/mblog/oripic?id=DvD1WzkQl&amp;u=a8d43f7egw1f3varqsvoij20gc0baab8">
     原图
    </a>
    <span class="cmt">
     赞[22]
    </span>
    <span class="cmt">
     原文转发[48]
    </span>
    <a class="cc" href="http://weibo.cn/comment/DvD1WzkQl?rl=1#cmtfrm">
     原文评论[13]
    </a>    <!---->
   </div>
   <div>
    <span class="cmt">
     转发理由:
    </span>
    转发微博
    <a href="http://weibo.cn/attitude/DvDwAlOh4/add?uid=3933240318&amp;rl=1&amp;st=0b50f1">
     赞[0]
    </a>
    <a href="http://weibo.cn/repost/DvDwAlOh4?uid=3933240318&amp;rl=1">
     转发[0]
    </a>
    <a class="cc" href="http://weibo.cn/comment/DvDwAlOh4?uid=3933240318&amp;rl=1#cmtfrm">
     评论[0]
    </a>
    <a href="http://weibo.cn/fav/addFav/DvDwAlOh4?rl=1&amp;st=0b50f1">
     收藏
    </a>
    <a href="http://weibo.cn/mblog/topmblog?uid=3933240318&amp;settop=1&amp;mblogid=DvDwAlOh4&amp;toptype=&amp;st=0b50f1">
     置顶
    </a>    <!---->
    <a class="cc" href="http://weibo.cn/mblog/del?id=DvDwAlOh4&amp;rl=1&amp;st=0b50f1">
     删除
    </a>
    <span class="ct">
     今天 14:15 来自红米Note 2
    </span>
   </div>
  </div>
  
  <div class="c" id="M_DvDwAlO22">
   <div>
    <span class="cmt">
     转发了
     <a href="http://weibo.cn/u/2832482174">
      程序员俱乐部
     </a>
     <img alt="M" src="http://u1.sinaimg.cn/upload/h5/img/hyzs/donate_btn_s.png"/>
     的微博:
    </span>
    <span class="ctt">
     【非常上档次的HTML5/CSS3登录表单】在线演示：
     <a href="http://weibo.cn/sinaurl?f=w&amp;u=http%3A%2F%2Ft.cn%2FRz2hqX8&amp;ep=DvDwAlOh4%2C3933240318%2CDvD1WzkQl%2C2832482174">
      http://t.cn/Rz2hqX8
     </a>
     源码下载：
     <a href="http://weibo.cn/sinaurl?f=w&amp;u=http%3A%2F%2Ft.cn%2F8s0vaz6&amp;ep=DvDwAlOh4%2C3933240318%2CDvD1WzkQl%2C2832482174">
      http://t.cn/8s0vaz6
     </a>
    </span>
   </div>
   <div>
    <a href="http://weibo.cn/mblog/pic/DvD1WzkQl?rl=1">
     <img alt="图片" class="ib" src="http://ww3.sinaimg.cn/wap180/a8d43f7egw1f3varqsvoij20gc0baab8.jpg"/>
    </a>
    <a href="http://weibo.cn/mblog/oripic?id=DvD1WzkQl&amp;u=a8d43f7egw1f3varqsvoij20gc0baab8">
     原图
    </a>
    <span class="cmt">
     赞[22]
    </span>
    <span class="cmt">
     原文转发[48]
    </span>
    <a class="cc" href="http://weibo.cn/comment/DvD1WzkQl?rl=1#cmtfrm">
     原文评论[13]
    </a>    <!---->
   </div>
   <div>
    <span class="cmt">
     转发理由:
    </span>
    转发微博
    <a href="http://weibo.cn/attitude/DvDwAlOh4/add?uid=3933240318&amp;rl=1&amp;st=0b50f1">
     赞[0]
    </a>
    <a href="http://weibo.cn/repost/DvDwAlOh4?uid=3933240318&amp;rl=1">
     转发[0]
    </a>
    <a class="cc" href="http://weibo.cn/comment/DvDwAlOh4?uid=3933240318&amp;rl=1#cmtfrm">
     评论[0]
    </a>
    <a href="http://weibo.cn/fav/addFav/DvDwAlOh4?rl=1&amp;st=0b50f1">
     收藏
    </a>
    <a href="http://weibo.cn/mblog/topmblog?uid=3933240318&amp;settop=1&amp;mblogid=DvDwAlOh4&amp;toptype=&amp;st=0b50f1">
     置顶
    </a>    <!---->
    <a class="cc" href="http://weibo.cn/mblog/del?id=DvDwAlOh4&amp;rl=1&amp;st=0b50f1">
     删除
    </a>
    <span class="ct">
     今天 14:15 来自红米Note 2
    </span>
   </div>
  </div> 
  
'''
#def get_info(r):   
#if not r:
#    return "页面数据获取失败"

#print( r.decode('utf-8'))
rr1 = open("weiboPage1.html", encoding='utf-8')
rr = rr1.read()
rr1.close()
# print(rr)
print(type(rr))

soup = BeautifulSoup(rr, "html5lib")
#soup = BeautifulSoup(r, "html.parser")
#w eiBoAll = soup.find_all("div",class_="c",id=re.compile(r"M_.{9}"))
# weiBoAll = soup.find_all(class_="c")
#print(soup)
weiBoAll = soup.find_all(id=re.compile(r"^M_.{9}$"))
#weiBoAll = soup.find_all(class_="c")
i = 0
for weiBOList in weiBoAll:
    # print(type(weiBOList))
    i = i+1
    print("+++++++++++++正在解析本页第%d条微博+++++++++++++" % i)
    print(weiBOList)
    # print(weiBOList.get_text())
    # print(weiBOList.text)
    # print(weiBOList.find(class_="cmt"))
    print("+++++++++++++本页第%d条微博解析完成++++++++++++++" % i)
print("+++++++++++++本页解析完成+++++++++++++\n")




