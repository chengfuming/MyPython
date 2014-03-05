# _*_ coding:utf-8 _*_
import urllib
import requests
import time

user_agent = (
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.11 (KHTML, like Gecko) '
    'Chrome/20.0.1132.57 Safari/536.11'
)
session = requests.session()
session.headers['User-Agent'] = user_agent

def deCaptcha(image_source):
    """
    imageSource: image file
    return dict
    """
    data = {
        'username': 'username',
        'password': 'password',
        'function': 'picture2',
        'pict_to': '0',
        'pict_type': '0',
        'pict': image_source
    }
    keys = [
        'ResultCode',
        'MajorID',
        'MinorID',
        'Type',
        'Timeout',
        'Text'
    ]
    de_captcher_server = "http://poster.de-captcher.com/"
    result = session.post(de_captcher_server,data)
   
    '''opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor())
    result = opener.open(de_captcher_server, urllib.parse.urlencode(data).encode())'''
    # result: 0|107|44685|0|0|n7hjks
    print(result.content)
    return dict(zip(keys, result.content.decode().split('|')))
 
 
def getCaptchaImage(url,rtimes=1):
    i=1
    try:
        for i in range(1,rtimes+1):
            print("start getting pic %d" % i)
            path = r"D:/data/workspacePython/PythonTest/src/"+r"%d.jpg" % i
            data = urllib.request.urlretrieve(url,path)
            print(data)
            print("end getting pic %d" % i)
            time.sleep(1)
    except:
        print("fail to aquire pic %d" % i)
        return
    print("end getting pics")
    return

if __name__ == '__main__':
    '''url = r"http://icode.renren.com/getcode.do?t=web_login&rnd=Math.random()"i
    getCaptchaImage(url,10)
    resp = session.get(url)'''
    '''
    browser = cPAMIE.PAMIE()
    browser.navigate('http://example.com/')
    captcha_image_src = browser.imageGet('image_element_ID').src
    
    image_source = getCaptchaImage(captcha_image_src) '''
     
    print(deCaptcha(r"D:/data/workspacePython/PythonTest/src/4.jpg")['Text'])
