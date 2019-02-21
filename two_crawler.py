# -*- coding:cp949 -*-

import requests
from bs4 import BeautifulSoup

#크롤링 기능을 가진 크롤러 클래스 정의
class Crawler:

    #크롤러 객체는 저마다 url 데이터를 가진다
    def __init__(self, url):
        self.url = url

    #GET 요청 성공 시 분석가능한 BeautifulSoup 객체 반환
    def get_source(self):
        r = requests.get(self.url)
        if r.status_code == 200:
            s = BeautifulSoup(r.content, "html.parser")
            return s
        else:
            #요청 실패 시 에러 유발
            raise Exception("Invalid URL")

#보안뉴스 크롤러 클래스 정의
class Boannews(Crawler):
    def inspect(self, s, c):
        r = s.find_all(class_=c)
        return r

    def get_ten_titles(self, t):
        for idx in range(10):
            print t[idx].get_text()

#아이뉴스 크롤러 클래스 정의
class Inews(Crawler):
    def inspect(self, s, c):
        r = s.select(c)
        return r

    def get_ten_titles(self, t):
        for idx in range(10):
            print t[idx].text

if __name__ == "__main__":

    #크롤러 객체 생성
    crawler1 = Boannews("https://www.boannews.com/media/list.asp")
    crawler2 = Inews("http://www.inews24.com/list/it")

    #보안뉴스 크롤러 동작확인
    print "Boannews"
    s1 = crawler1.get_source()
    res1 = crawler1.inspect(s1, "news_txt")
    crawler1.get_ten_titles(res1)

    #아이뉴스 크롤러 동작확인
    print "Inews24"
    s2 = crawler2.get_source()
    res2 = crawler2.inspect(s2, "body > main > article > ol > li > a")
    crawler2.get_ten_titles(res2)
    
