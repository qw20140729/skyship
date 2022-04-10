# -*- encoding:utf-8 -*-
import autoit

class LoginComan(object):
    SOFT = 'SkyMngerServer.exe'
    def __init__(self, name, passwd):
        self.name = name
        self.passwd = passwd
    def login(self):
        autoit.run(self.SOFT)
        autoit.win_wait_active("[CLASS:#32770]")
        autoit.send(self.name)
        autoit.send('{Tab}')
        autoit.send(self.passwd)
        autoit.send('{Enter}')


if __name__ == '__main__':
    # 登录COMAN
    name = 'qyl'
    passwd = 'skyship'
    lc = LoginComan(name, passwd)
    lc.login()