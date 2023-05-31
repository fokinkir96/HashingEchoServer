import datetime
import os, hashlib
from random import randint as ri

class Auth:
    def __init__(self):
        if 'serv' not in os.listdir():
            os.mkdir('serv')

        self.name = ''

    def get_login_data(self):
        name = self.get_client_name()
        self.greet_client()
        if self.pwd == False:
            self.set_password()
            # Если нет пароля, то:
            #   1. Просим пароль
            #   2. Сохраняем хеш пароля
            #   3. Отправляем токен со временем и сохраняем в файл ip:токен
            #   4. Profit
            pass
        else:
            pwd = self.get_client_password()
            # Если есть токен, то:
            #   1. чекаем валидность токена

            # Если есть пароль, то:
            #   1. Просим пароль
            #   2. Проверяем хеши
            #   3. Если ок, то profit(send token to client)
            #   4. Если не ок, то просим еще раз(3 попытки)
            #   5. Profit
            pass

    def get_client_name(self, ip):
        with open('serv/clients.txt', 'r') as f:
            for i in f.readlines():
                print(i)
                i = i.split()
                if ip == i[0]:
                    return i[1]

        return False

    def get_client_pwd(self, ip):
        with open('serv/passwords.txt', 'r') as f:
            for i in f.readlines():
                print(i)
                i = i.split()
                if ip == i[0]:
                    return i[1]

        return False

    def save_client_name(self, ip, name):
        with open('serv/clients.txt', 'a+') as f:
            f.write(str(ip)+' '+name+'\n')

    def prepare_password(self, name, pwd):
        # salt = ri(10000, 99999)
        salt = ''
        return hashlib.md5((name+pwd+str(salt)).encode('UTF-8')).hexdigest()

    def save_client_password(self, ip, hex):
        with open('serv/passwords.txt', 'a+') as f:
            f.write(str(ip)+' '+hex+'\n')

    def get_sess_id(self, ip, hex):
        salt = ri(10000, 99999)
        return hashlib.md5((ip+hex+str(salt)).encode('UTF-8')).hexdigest()
    def create_client_session(self, ip, hex):
        sess_id = self.get_sess_id(ip, hex)
        expires = str(datetime.datetime.now()+datetime.timedelta(minutes=30))[:-7]

        with open('serv/sessions.txt', 'a+') as f:
            f.write(str(ip)+' '+sess_id+' '+expires+'\n')

        return sess_id, expires
