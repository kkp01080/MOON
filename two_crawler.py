# -*- coding:cp949 -*-

import requests
from bs4 import BeautifulSoup

#ũ�Ѹ� ����� ���� ũ�ѷ� Ŭ���� ����
class Crawler:

    #ũ�ѷ� ��ü�� ������ url �����͸� ������
    def __init__(self, url):
        self.url = url

    #GET ��û ���� �� �м������� BeautifulSoup ��ü ��ȯ
    def get_source(self):
        r = requests.get(self.url)
        if r.status_code == 200:
            s = BeautifulSoup(r.content, "html.parser")
            return s
        else:
            #��û ���� �� ���� ����
            raise Exception("Invalid URL")

#���ȴ��� ũ�ѷ� Ŭ���� ����
class Boannews(Crawler):
    def inspect(self, s, c):
        r = s.find_all(class_=c)
        return r

    def get_ten_titles(self, t):
        for idx in range(10):
            print t[idx].get_text()

#���̴��� ũ�ѷ� Ŭ���� ����
class Inews(Crawler):
    def inspect(self, s, c):
        r = s.select(c)
        return r

    def get_ten_titles(self, t):
        for idx in range(10):
            print t[idx].text

if __name__ == "__main__":

    #ũ�ѷ� ��ü ����
    crawler1 = Boannews("https://www.boannews.com/media/list.asp")
    crawler2 = Inews("http://www.inews24.com/list/it")

    #���ȴ��� ũ�ѷ� ����Ȯ��
    print "Boannews"
    s1 = crawler1.get_source()
    res1 = crawler1.inspect(s1, "news_txt")
    crawler1.get_ten_titles(res1)

    #���̴��� ũ�ѷ� ����Ȯ��
    print "Inews24"
    s2 = crawler2.get_source()
    res2 = crawler2.inspect(s2, "body > main > article > ol > li > a")
    crawler2.get_ten_titles(res2)
    
