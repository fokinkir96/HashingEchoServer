import socket, datetime
from quests import Connected
from modules.Logging import Logging
from modules.Hash import Hash
from random import randint as ri
class Client(Connected.Connected):
    def __init__(self):
        self.conn = socket.socket()
        self.log = Logging('client')
        self.msgs = []
        self.settings = self.read_settings()


    def connect(self, host='localhost', port=9090):
        result = self.conn.connect_ex((host, port))
        if result == 0:
            self.log.add_log('Вы подключились к серверу '+str(host)+':'+str(port))
        else:
            self.log.add_log('Ошибка при подключении к серверу ' + str(host) + ':' + str(port))
            self.log.add_log('Код ошибки: ' + str(result))

        if self.settings['hash'] == 'true':
            self.change_keys()

    def save_cookie(self, data):
        with open('sessions.txt', 'w') as f:
            f.write(data['sess_id']+' '+data['expires']+'\n')

    def send_auth_cookie(self):
        with open('sessions.txt', 'r') as f:
            line = f.read()
            if len(line) == 0:
                return False
            cookie = line.split()
            dt = cookie[1]+' '+cookie[2]
            cookie = cookie[0]

            if datetime.datetime.now() < datetime.datetime.strptime(dt, '%Y-%m-%d %H:%M:%S'):
                return False

            self.send(cookie, 'auth_cookie')

    def disConnect(self):
        self.send('exit')
        self.log.add_log('Вы отключились от сервера')
