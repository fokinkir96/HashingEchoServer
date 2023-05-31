import os
from random import randint as ri
class Hash:

    def __init__(self):
        self.public_key = 0
        self.private_key = 0
        self.public_key2 = 0
        self.partial_key = 0
        self.full_key = None

    def generate_keys(self):
        if 'public.key' in os.listdir() or 'private.key' in os.listdir():
            with open('public.key', 'r') as f:
                self.public_key = f.read()

            with open('private.key', 'r') as f:
                self.private_key = f.read()
        else:
            self.public_key = ri(1000, 10000)
            self.private_key = ri(1000, 10000)

            self.save_keys()

        self.public_key = int(self.public_key)
        self.private_key = int(self.private_key)

        return self.public_key

    def save_keys(self):
        with open('public.key', 'w+') as f:
            f.write(str(self.public_key))
        with open('private.key', 'w+') as f:
            f.write(str(self.private_key))


    def generate_partial_key(self, public_key2):
        self.public_key2 = public_key2
        partial_key = self.public_key ** self.private_key
        partial_key = partial_key % self.public_key2
        self.partial_key = partial_key
        return partial_key

    def generate_full_key(self, partial_key_r):
        full_key = partial_key_r ** self.private_key
        full_key = full_key % self.public_key2
        self.full_key = full_key
        return full_key

    def encrypt_message(self, message):
        encrypted_message = ""
        key = self.full_key
        for c in message:
            encrypted_message += chr(ord(c) + key)
        return encrypted_message

    def decrypt_message(self, encrypted_message):
        decrypted_message = ""
        key = self.full_key
        for c in encrypted_message:
            decrypted_message += chr(ord(c) - key)
        return decrypted_message


