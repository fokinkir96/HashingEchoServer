import os
from modules.Logging import Logging
from modules.Message import Message
from modules.Auth import Auth
from quests.Connected import Connected

class ConnectedAuthorization(Connected):

    def __init__(self, conn, addr):

        super().__init__(conn, addr)

        self.login_user()
    def greetings(self):
        self.send('Привет, ' + self.name)

    def login_user(self):
        self.name = self.auth.get_client_name(self.addr[0])

        if not self.name:
            self.send('Введите свое имя: ', 'prompt')
            self.name = self.recv()[0]
            self.auth.save_client_name(self.ip, self.name)

        if not self.check_pwd():
            # self.disConnect()
            print('wrong pass')
            pass

        self.greetings()

    def check_pwd(self):
        save = False
        wrong_pwd = True

        pwd_hash = self.auth.get_client_pwd(self.addr[0])
        if not pwd_hash:
            save = True

        for i in range(3):
            if wrong_pwd is False:
                break

            self.send('Введите пароль: ', 'prompt')
            md5_hex = self.auth.prepare_password(self.name, self.recv()[0])
            if save is True:
                self.auth.save_client_password(self.ip, md5_hex)
                wrong_pwd = False
            if md5_hex == pwd_hash:
                wrong_pwd = False
            else:
                self.send('Вы ввели неверный пароль! Попробуйте еще раз.', 'info+')

        if wrong_pwd is False:
            sess_id, expires = self.auth.create_client_session(self.ip, md5_hex)
            self.send({'sess_id': sess_id, 'expires': expires}, 'cookie')

            return True

        return False
