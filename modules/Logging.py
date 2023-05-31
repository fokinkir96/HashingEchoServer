import os, datetime
class Logging:

    def __init__(self, filename='server'):
        self.prefix = 'logs'
        self.ext = '.log'
        self.log_file_name = filename+self.ext
        self.log_file = self.prefix+'/'+self.log_file_name
    def create_log_file(self):
        if self.prefix not in os.listdir():
            os.mkdir('../logs')
        if self.log_file_name not in os.listdir(self.prefix):
            log = open(self.log_file, 'a', encoding='UTF-8')
            # print(log)
            log.close()

    def add_log(self, log):
        self.create_log_file()
        print(log)
        with open(self.log_file, 'a', encoding='UTF-8') as f:
            f.write(str(datetime.datetime.now())+': '+log+'\n')
