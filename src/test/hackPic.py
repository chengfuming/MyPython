import urllib
import requests


WBCLIENT = 'ssologin.js(v1.4.5)'
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
    '''
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    result = opener.open(de_captcher_server, urllib.urlencode(data))'''
    # result: 0|107|44685|0|0|n7hjks
    return dict(zip(keys, result.read().split('|')))
 
 
def getCaptchaImage(url):
    """获取验证码图片
 
    Args:
        url: 字符串，图片的网址
 
    Returns:
        文件对象，图片源文件
 
        fileObj.read()
    """
url = r"http://icode.renren.com/getcode.do?t=web_login&rnd=Math.random()"
resp = session.get(url)
path = r"D:\data\workspacePython\PythonTest\src"  
data = urllib.request.urlretrieve(url,path) 
'''
browser = cPAMIE.PAMIE()
browser.navigate('http://example.com/')
captcha_image_src = browser.imageGet('image_element_ID').src

image_source = getCaptchaImage(captcha_image_src)
 
print deCaptcha(image_source)['Text']    '''
