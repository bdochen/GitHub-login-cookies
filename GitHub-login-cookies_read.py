# -*- coding: UTF-8 -*-
import requests
from lxml import etree
import http.cookiejar

class Login(object):
    def __init__(self):
        self.headers = {
            'Referer': 'https://github.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
            'Host': 'github.com'
        }
        self.login_url = 'https://github.com/login'
        self.post_url = 'https://github.com/session'
        self.logined_url = 'https://github.com/settings/sessions'
        self.session = requests.Session()
        self.filename='cookies_zhihu.txt'    
        self.session.cookies = http.cookiejar.LWPCookieJar()
        self.session.cookies.load(self.filename, ignore_discard=True, ignore_expires=True) 
        #载入cookies
    def login(self, email, password):
        response = self.session.get(self.logined_url, headers=self.headers)
        self.session.cookies.save(self.filename,ignore_discard=True, ignore_expires=True)   
        #登陆成功后更新cookies，github的cookies有效期两周，每次登陆时顺便更新一下有效期
        if response.status_code == 200:
           #self.profile(response.text)
           #print((response.text).encode('utf-8'))
           #此页面能看到你所有的登陆记录
            with open('zhihu_READ.html', 'a+', encoding='utf-8') as f:
                f.write(response.text)
            print('read_over')
            
            
            

if __name__ == "__main__":
    login = Login()
    login.login(email='username', password='password')
