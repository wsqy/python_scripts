from bs4 import BeautifulSoup 
import re  
 
def get_info():  
    print("+++++++++++++解析器准备+++++++++++++")
    soup = BeautifulSoup(open("weiboPage2.html").decode('utf-8'), "html5lib")
    #print(soup.prettify())
    print("+++++++++++++解析器就绪+++++++++++++")
    # "div",class_="c",id=re.compile(r"M_.{9}")
    # weiBoAll = soup.find_all("div",class_="c",id=re.compile(r"^M_.{9}$"))
    weiBoAll = soup.find_all(class_="c")
    i = 0
    for weiBOList in weiBoAll:
        i = i+1
        print("+++++++++++++正在解析本页第%d条微博+++++++++++++" % i)
        print(weiBOList)
        print("+++++++++++++本页第%d条微博解析完成+++++++++++++" % i)
    print("+++++++++++++本页解析完成+++++++++++++")
    
if __name__ == "__main__":
    get_info() 

    