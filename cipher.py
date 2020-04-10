#! /use/bin/python3
import base64
import hashlib

# just the encryption key, could be anything
key = b'AK8EwgCqe9-Y!YEhSwN9^Ft'

# list of all base64 characters
bs64_char = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz \
0123456789+/']


def convert_input(string, type):
    hash = hashlib.sha512(key).hexdigest()
    cipher = bs64_char[:]

    for c in hash:
        char_int = int(c, 16)
        position = 65 * (char_int / 15)

        cipher.insert(0, cipher.pop(int(position)-1))
        cipher = cipher[::-1]

    cipher_box = {}

    for i, c in enumerate(bs64_char):
        cipher_box[c] = cipher[i]

    if type == 'd':
        cipher_box = dict((v, k) for k, v in cipher_box.items())

    for i, c in enumerate(string):
        string[i] = string[c]
        return ''.join(string)
