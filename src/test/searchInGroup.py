# _*_ coding:utf-8 _*_
import requests
import urllib
import http.cookiejar
from bs4 import BeautifulSoup
import time
 
RESULT = []   


user_agent =  'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.95 Safari/537.36 SE 2.X MetaSr 1.0'
session = requests.session()
session.headers['User-Agent'] = user_agent
session.headers['Host'] = 'www.douban.com'
session.headers['Connection'] = 'keep-alive'
session.headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
session.headers['Accept-Language'] = 'zh-CN,zh;q=0.8'
session.headers['Accept-Encoding'] = 'gzip,deflate,sdch'
cookie = http.cookiejar.CookieJar() 
cookieProc = urllib.request.HTTPCookieProcessor(cookie) 
session.cookies = http.cookiejar.CookieJar();
 
def crawl_for_id_num(url,endpage,startpage=1):
    for i in range(startpage,endpage):
        
        print('start scanning page %d, please wait... ' % i)
        session.headers['Referer'] =  url
        lc = str((i-1)*35)
        '''
        req = urllib.request.Request(url=url + lc, headers=headers)  
        page = urllib.request.urlopen(req).read()
        contents = page.read()
        '''
        resp = session.get(url+lc)
        if (resp.status_code==403):
            print('403 bad req')
        contents =resp.content.decode( 'utf-8', 'ignore' ) 
        soup = BeautifulSoup(contents)
        j=1
        for tag in soup.find_all('a', class_='nbg'):
            href = tag['href'].replace('/group','')
            #print(href)
            #print("crawl page %d user %d" % (i,j))
            
            print('finish user %d, status: %d' % (j,getUsrLoc(href)))
            j+=1
            
           
        print('end page %d, result size: %d' % (i,len(RESULT)))
        time.sleep(5)
    print('end crawl process')
        




def getUsrLoc(url):
    time.sleep(2)
    session.headers['Referer'] =  url
    contents =session.get(url).content.decode( 'utf-8', 'ignore' ) 
    soup = BeautifulSoup(contents)  
    for tag in soup.find_all('a', {'href':'http://www.douban.com/location/nanjing/'}):
        RESULT.append(url)
        return 1
    return 0
    

def output():
    count = 0
    while count<len(RESULT):
        print(RESULT[count])
        count = count + 1
 
if __name__ == '__main__':

    #crawl('http://movie.douban.com/top250?format=text')
    url = 'http://www.douban.com/group/jiazhuangqinglv/members?start='
    endPage=10
    startPage=1
    try:
        RESULT = []
        crawl_for_id_num(url,endPage,startPage)
        output()
    except:
        print('except')
        output()
    
    
       
