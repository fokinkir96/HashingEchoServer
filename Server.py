import socket
from quests import ConnectedAuthorization
from quests import Connected
from modules.Logging import Logging
class Server:

    def __init__(self, host = 'localhost', port = 9090, quantity = 5):
        self.host = host
        self.port = port
        self.quantity = quantity
        self.connected = []
        self.log = Logging()
        self.sock = self.start()

    def start(self):
        sock = socket.socket()

        try:
            sock.bind((self.host, self.port))
        except Exception:
            while True:
                try:
                    self.port += 1
                    sock.bind((self.host, self.port))
                    break
                except Exception:
                    pass

        self.log.add_log('Сервер запущен')

        sock.listen(self.quantity)
        self.log.add_log('Слушаем ' + str(self.host) + ' на ' + str(self.port) + ' порту')

        return sock

    def wait_client(self):
        c, addr = self.sock.accept()

        self.log.add_log('Клиент '+str(addr[0])+':'+str(addr[1])+' подключился')

        cl = Connected.Connected(c, addr)
        self.connected.append(cl)

        return cl
    def stop(self):
        self.log.add_log('Сервер остановлен')
        exit()
