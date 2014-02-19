import re
import json
import urllib
import base64
import binascii

import rsa
import requests
import logging
logging.basicConfig(level=logging.DEBUG)


WBCLIENT = 'ssologin.js(v1.4.5)'
user_agent = (
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.11 (KHTML, like Gecko) '
    'Chrome/20.0.1132.57 Safari/536.11'
)
session = requests.session()
session.headers['User-Agent'] = user_agent

app_key = '5786724301'
'''
Google.Nexus        1206405345 fa6095e113cd28fde6e14c7b7145c5c5 
iphone客户端                             5786724301 5Jao51NF1i5PDC91hhI3ID86ucoDtn4C 
iPad客户端                                    2849184197 7338acf99a00412983f255767c7643d0 
Weico.Android版                211160679 63b64d531b98c2dbff2443816f274dd3 
weico.iphone版                82966982 72d4545a28a46a6f329c4f2b1e949e6a 
联想乐Pad客户端                        2440435914 70dc2ae26780817793c9c533092171dd 
摩托罗拉XOOM        2190063733 9222f119671ebf566b74220768014afd 
三星GalaxyS        3442868347 07b27d2c098eda5eec681abdde832a51 
小米手机                                    xiaomi 3MqAdNoRLHomm4AECoURl7gds1sUIjun
android手机                        android 5l0WXnhiY4pJ794KIJ7Rw5F45VXg9sjo 
黑莓客户端                                blackberry ivij24vyWpP0zE0M03r56RL2u8nu0L66 
三星GalaxyTab        sxtab 6b2BhcdpiCdyZaIh4O3S1zHAUoC6Zpql 
三星Android智能手机    sxandroid App Secret：tYQO8S1RndCGgI3qNbiCEjG3cVaeOvq7 
htc                htc ybQv5D6BC2bIOqYV2wCsIs0dX9vV0xIG 
SonyXpera        x10 rPVsSGvnz8erJ7w8sIICKEE70wQMRswU 
Moto            me511 5AgbUpV7fL2APXOkI04QnRhlGUdUlwy0 
乐phone            lp 5EmMeHqPOYsLSQ2zjrdXHoUhqtD4QYGx 
魅族M9            meizu_m9 WQnVIAWDBmR9XV86YNAO97P3Xgk21az9 
S60手机                                s60 AbLmkn77N8j72iyE2Aup5RoRN8C0M3E5
weicoPro        2323547071 16ed80cc77fea11f7f7e96eca178ada3 
GIF快手                             915345515 88b51e31ddbe926089706e4500c55d2d 
美图秀秀                             4229079448 bc58f8c7179369d4bfa914656c161b15
三星GalaxyTab    3510766076 f97dfdd530d85eaaee45e63ee47445a3 
WeicoGIF        1078446352 c698c95df62b060734d3d0a9e8787a9a
webOS        1262673699 6185cf040b403dfa35de9678b5e35baf
'''

def encrypt_passwd(passwd, pubkey, servertime, nonce):
    key = rsa.PublicKey(int(pubkey, 16), int('10001', 16))
    message = str(servertime) + '\t' + str(nonce) + '\n' + str(passwd)
    passwd = rsa.encrypt(message.encode(), key)
    return binascii.b2a_hex(passwd)


def wblogin(username, password):
    resp = session.get(
        'http://login.sina.com.cn/sso/prelogin.php?'
        'entry=sso&callback=sinaSSOController.preloginCallBack&'
        'su=%s&rsakt=mod&client=%s' %
        (base64.b64encode(username.encode()), WBCLIENT)
    )
    pre_login_str = re.match(b'[^{]+({.+?})', resp.content).group(1)
    #pre_login = json.loads(pre_login_str)

    pre_login = json.loads(pre_login_str.decode())
    data = {
        'entry': 'weibo',
        'gateway': 1,
        'from': '',
        'savestate': 7,
        'userticket': 1,
        'ssosimplelogin': 1,
        'su': base64.b64encode(urllib.request.quote(username).encode()),
        'service': 'miniblog',
        'servertime': pre_login['servertime'],
        'nonce': pre_login['nonce'],
        'vsnf': 1,
        'vsnval': '',
        'pwencode': 'rsa2',
        'sp': encrypt_passwd(password, pre_login['pubkey'],
                             pre_login['servertime'], pre_login['nonce']),
        'rsakv' : pre_login['rsakv'],
        'encoding': 'UTF-8',
        'prelt': '115',
        'url': 'http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.si'
               'naSSOController.feedBackUrlCallBack',
        'returntype': 'META'
    }
    resp = session.post(
        'http://login.sina.com.cn/sso/login.php?client=%s' % WBCLIENT,
        data=data
    )

    login_url = re.search(b'replace\([\"\']([^\'\"]+)[\"\']',
                          resp.content).group(1)
    login_url = '%s' % login_url   
    login_url = login_url[2:len(login_url)-1]                 
    resp = session.get(login_url)
    login_str = re.match(b'[^{]+({.+?}})', resp.content).group(1)
    return json.loads(login_str.decode())


def wbSend(url,username,text,app_key):
    session.headers['Referer'] = 'http://weibo.com/%(username)s?wvr=5&wvr=5&lf=reg' % {'username': username}
    #session.headers['Referer'] = 'http://service.weibo.com/share/mobile.php?appkey=5786724301&amp;content=utf8'
    post_data =  {'text':text,
                'pic_id':'',
                'rank':0,
                'rankid':'',
                '_surl':'',
                'hottopicid':'',
                'location':'home',
                'module':'stissue',
                'appkey':app_key,
                '_t':0,
    }
    page = session.post(url,post_data)
    print(page)
    

if __name__ == '__main__':
    from pprint import pprint
    pprint(wblogin('lizy1630@gmail.com', 'JY900415Gu'))
    url = 'http://weibo.com/aj/mblog/add?_wv=5&__rnd='
    #url = 'http://service.weibo.com/share/mobile.php?appkey=5786724301&amp;content=utf8'
    wbSend(url,'lizy1630@gmail.com','test',app_key)