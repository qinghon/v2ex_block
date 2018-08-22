import requests,time
import configparser
import sys
import getopt


class block():
    def __init__(self):
        self.S=requests.Session()

    def get_name_from_file(self,FILE_NAME):
        b_list=configparser.ConfigParser()
        with open(FILE_NAME,encoding="UTF-8") as cf:

            b_list.read_file(cf)
        lv1=b_list.items("level1")
        lv2=b_list.items("level2")
        lv3=b_list.items("level3")
        return {"lv1":lv1,"lv2":lv2,"lv3":lv3}
        

    def block_post(self,NAME,num):
        ticks=time.time()
        data={"t":ticks}
        self.S.get("https://www.v2ex.com/block/{0}".format(num),data=data)

    def unblock_post(self,NAME,num):
        ticks=time.time()
        data={"t":ticks}
        self.S.get("https://www.v2ex.com/unblock/{0}".format(num),data=data)

    def login(self,cookies_str):
        cookies={}
        for line in cookies_str.split(';'):
            key,v=line.strip().split('=')
            cookies[key]=v
        self.S.cookies.set_cookie(cookies)

def test():
    v2er=block()
    print(v2er.get_name_from_file("list.ini"))


if __name__ == '__main__':
    test()
    pass
