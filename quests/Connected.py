import os
from modules.Logging import Logging
from modules.Message import Message
from modules.Auth import Auth
from modules.Hash import Hash
from random import randint as ri

class Connected:
    def __init__(self, conn, addr):
        self.settings = self.read_settings()

        self.conn = conn

        self.addr = addr
        if self.settings['hash'] == 'true':
            self.change_keys()
        # self.ip = self.addr[0]+':'+self.addr[1]
        self.ip = self.addr[0]
        self.name = ''

        self.log = Logging()
        self.auth = Auth()
        self.msgs = []

    def change_keys(self):
        self.hash = Hash()
        self.hash.generate_keys()
        self.conn.send(str(self.hash.public_key).encode('UTF-8'))
        cl_pbk = int(self.conn.recv(1024).decode())
        self.conn.send(str(self.hash.generate_partial_key(cl_pbk)).encode('UTF-8'))
        self.hash.generate_full_key(int(self.conn.recv(1024).decode()))

    def read_settings(self):
        with open('settings.txt', 'r') as f:
            res = {}
            for i in f.readlines():
                line = i.split('=')
                res[line[0].strip().lower()] = line[1].strip().lower()

            return res

    def recv(self, bytes = 1024):
        msg = Message(self.conn.recv(bytes), False)
        if self.settings['hash'] == 'true':
            # print(msg.body)
            msg.body = self.hash.decrypt_message(msg.body)

        self.msgs.insert(0, msg)
        self.log.add_log('Получили: '+msg.pureMsg)

        return msg.body, msg.head['Type']

    def send(self, m, type='info'):
        if self.settings['hash'] == 'true':
            m = self.hash.encrypt_message(m)

        msg = Message(m, type=type)

        self.conn.send(msg.prepare())
        self.log.add_log('Отправили: '+msg.pureMsg)

    def disConnect(self):

        # self.conn.disconnect()
        self.log.add_log('Клиент '+str(self.addr[0])+':'+str(self.addr[1])+' отключился')
