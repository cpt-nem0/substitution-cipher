#! /usr/bin/python3

import base64
import sys
import hashlib

key = b'AK8EwgCqe9-Y!YEhSwN9^Ft'
bs64_char = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=']


def conversion(string, type):
    hash = hashlib.sha512(key).hexdigest()
    cipher = bs64_char[:]

    for c in hash:
        ciph_int = int(c, 16)
        pos = 65 * (ciph_int / 15)
        cipher.insert(0, cipher.pop(int(pos)-1))
        cipher = cipher[::-1]

    ciph_map = {}

    for i, c in enumerate(bs64_char):
        ciph_map[c] = cipher[i]

    if type == 'd':
        ciph_map = dict((v, k) for k, v in ciph_map.items())

    for i, c in enumerate(string):
        string[i] = ciph_map[c]

    return ''.join(string)


def encryption(string):
    string = [c for c in base64.b64encode(string.encode()).decode()]
    return conversion(string, 'e')


def decryption(string):
    string = [c for c in string.strip()]
    return base64.b64decode(conversion(string, 'd')).decode()


if sys.argv[1] == '-e':
    print(encryption(sys.stdin.read()))
if sys.argv[1] == '-d':
    print(decryption(sys.stdin.read()))
