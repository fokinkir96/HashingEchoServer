import json, datetime
from modules.Hash import Hash

class Message:

    def __init__(self, msg, parsed=True, type='info'):
        self.head = {}
        self.pureMsg = ''

        if parsed:
            self.head['Type'] = type
            self.head['Content-length'] = len(msg)
            self.body = msg
        else:
            self.parse(msg)

    def parse(self, msg):
        self.pureMsg = msg.decode()
        data = json.loads(self.pureMsg)

        self.head = data['Header']
        self.body = data['Body']

    def prepare(self):
        self.head['DateTime'] = str(datetime.datetime.now())
        message = {
            'Header': self.head,
            'Body': self.body,
        }
        self.pureMsg = json.dumps(message)

        return self.pureMsg.encode('UTF-8')
