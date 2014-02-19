# _*_ coding:utf-8 _*_
import urllib.request
import re
from bs4 import BeautifulSoup
 
def crawl(url):
    page = urllib.request.urlopen(url)
    contents = page.read()
    soup = BeautifulSoup(contents)
    print(u'豆瓣电影250: 序号 \t影片名\t 评分 \t评价人数')
    for tag in soup.find_all('tr', class_='item'):
        m_order = int(tag.find('td', class_='m_order').get_text())
        m_name = tag.a.get_text()
        m_year = tag.span.get_text()
        m_rating_score = float(tag.em.get_text())
        m_rating_num = int(tag.find(headers="m_rating_num").get_text())
        print("%s %s %s %s %s" % (m_order, m_name, m_year, m_rating_score, m_rating_num))
        
        
def crawl_for_id_num(url,endpage,startpage=0):
    for i in range(startpage,endpage):
        print('scanning page %d, please wait... ' % i)
        if i==0:
            lc=''
        else:
            lc = '?start=%d00' % i
        page = urllib.request.urlopen(url + lc )
        contents = page.read()
        soup = BeautifulSoup(contents)
        for tag in soup.find_all('p', class_=''):
            m_content = tag.get_text();
            m_re_content = tag.parent.find_all('span', class_='all')
            if m_content.find('320106') != -1:
                m_p = '%s' % (tag.find_parent().find_parent().find('div',class_='user-face').a);
                print("\n%s\n%s" % (m_content,m_p[9:53]))
                print("%s\n\n" % (url))
            if len(m_re_content) and m_re_content[0].get_text().find('320106')!=-1  :
                m_p = '%s' % (tag.find_parent().find_parent().find('div',class_='user-face').a);
                print("\nRE| %s\n\t%s\n%s" % (m_re_content[0].get_text(),m_content,m_p[9:53]))
                print("%s\n\n" % (url))
        print('end page %d' % i)
    print('end crawl process')
        
            
def crawl_for_hot(url):
    page = urllib.request.urlopen(url)
    contents = page.read()
    soup = BeautifulSoup(contents)
    print(soup)
    for tag in soup.find_all('tr', class_='pl'):
        m_content = tag.find('tr',class_='td-reply').get_text();
        m_num = m_content[:m_content.find('回应')]
        m_title = tag.find('tr',class_='td-subject').a;
        #m_p = '%s' % (tag.find_parent().find_parent().find('div',class_='user-face').a);
        if m_num>300:
            print("%s\n%s" % (m_num,m_title))
            print("%s\n\n" % (url))
  

 
if __name__ == '__main__':

    #crawl('http://movie.douban.com/top250?format=text')
    crawl_for_id_num('http://www.douban.com/group/topic/47383610/',45)
