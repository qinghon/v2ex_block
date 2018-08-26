#!/usr/bin/env

import requests, time
import configparser
import sys
import getopt


class Block():
    def __init__(self):
        self.S = requests.Session()
        self.lv1 = None
        self.lv2 = None
        self.lv3 = None

    def get_name_from_file(self, FILE_NAME):
        b_list = configparser.ConfigParser()
        with open(FILE_NAME, encoding="UTF-8") as cf:
            b_list.read_file(cf)
        self.lv1 = [v for k, v in b_list.items("level1")]
        self.lv2 = [v for k, v in b_list.items("level2")]
        self.lv3 = [v for k, v in b_list.items("level3")]

    def get_cookie_from_file(self,cookie_name):
        with open(cookie_name,'r',encoding='utf-8') as cf:
            c_str=cf.read()
        if c_str == '':
            return 1
        else:
            return c_str
    def block_list(self, list, tag=1):
        #list=[]
        #tag is block or unblock tag 1 or 0
        def block_post(num):
            ticks = time.time()
            data = {"t": ticks}
            self.S.get("https://www.v2ex.com/block/{0}".format(num), data=data)

        def unblock_post(num):
            ticks = time.time()
            data = {"t": ticks}
            self.S.get("https://www.v2ex.com/unblock/{0}".format(num), data=data)

        if tag == 1:
            for id in list:
                block_post(id)
        else:
            for id in list:
                unblock_post(id)

    def set_c(self, cookie_str):

        def format_cookie(cookie_str):
            cookies = {}
            def format_str(cookie_str):
                if '"' in cookie_str:
                    return cookie_str.replace('"', '')

            for line in format_str(cookie_str).split(';'):
                key, v = line.strip().split('=', 1)
                cookies[key] = v
            return cookies
        requests.utils.add_dict_to_cookiejar(self.S.cookies, format_cookie(cookie_str))


def command():
    def c_help():
        print("""
        python v2ex_block.py -c "cookie" -f "ini_filename" -l "block level" -[bu]
        [options]
        -h, --help \t\tGet option help
        -c, --cookie \t\tAdd cookie str or saved cookie file (No more than 10 characters.)
        -f, --file  \t\tAdd block list file name 
        -l, --level \t\tBlock list level ,defult 1
        -b, --block \t\tDefult block
        -u, --unblock\t\t
        """)

    shortargs = 'hc:f:l:bu'
    longargs = ["help", "cookie=", "file=","level=","block","unblock"]

    try:
        opts, args = getopt.getopt(sys.argv[1:], shortargs, longargs)

    except getopt.GetoptError:
        c_help()
        print("getoptError")
        sys.exit(1)

    cookie = None
    file_name = None
    level=1
    tag=1
    for o, a in opts:
        if o in ("-h", "--help"):
            c_help()
            sys.exit(1)
        elif o in ("-c", "--cookie"):
            cookie = a
        elif o in ("-f", "--file"):
            file_name = a
        elif o in ("-l","--level"):
            level = a
        elif o in ("b","block"):
            tag=1
        elif o in ("u","unblock"):
            tag=0
        else:
            c_help()
    if cookie is None or file_name is None:
        c_help()
        sys.exit(1)
    else:
        return cookie, file_name,level,tag


if __name__ == '__main__':
    cookie, filename ,level,tag= command()
    b = Block()
    if len(cookie)>10:

        b.set_c(cookie)
    else:
        cookie_str=b.get_cookie_from_file(cookie)
        if cookie_str!=1:
            b.set_c(cookie_str)
        else:
            print("Please put cookie in the file.")
            sys.exit(1)

    b.get_name_from_file(filename)
    if level==1:
        b.block_list(b.lv1,tag)
    elif level==2:
        b.block_list(b.lv2,tag)
    elif level==3:
        b.block_list(b.lv3,tag)
