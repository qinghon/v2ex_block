import requests,time
import configparser

class block():
    def __init__(self):
        self.S=requests.Session()
        
    def get_name_from_file(self,FILE_NAME):
        pass

    def block_post_name(self,NAME,num):
        ticks=time.time()
        data={"t":ticks}
        self.S.get("https://www.v2ex.com/block/{0}".format(num),params=data)

    def login(self):
        pass