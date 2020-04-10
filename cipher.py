#! /usr/bin/python3

# make sure to edit the hashbang according to your system

import base64
import sys
import hashlib

# just the encryption key, it can be anything
key = b'AK8EwgCqe9-Y!YEhSwN9^Ftcpt_n3m0'

# characters of all 64 bit characters
bs64_char = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=']


# main conversion function that converts encodes or decodes the text
def conversion(string, type):
    hash = hashlib.sha512(key).hexdigest()
    cipher = bs64_char[:]
# iterating over the hash to convert the hexa decimal to decimal
# and substituting the values as well
    for c in hash:
        ciph_int = int(c, 16)
        pos = 65 * (ciph_int / 15)
        cipher.insert(0, cipher.pop(int(pos)-1))
        cipher = cipher[::-1]

# map of all the values
    ciph_map = {}

    for i, c in enumerate(bs64_char):
        ciph_map[c] = cipher[i]
# if we decrypt the text
    if type == 'd':
        ciph_map = dict((v, k) for k, v in ciph_map.items())

    for i, c in enumerate(string):
        string[i] = ciph_map[c]         # replacing the main text the the mapped values

    return ''.join(string)


# encryption function
def encryption(string):
    string = [c for c in base64.b64encode(string.encode()).decode()]
    return conversion(string, 'e')


# decryption function
def decryption(string):
    string = [c for c in string.strip()]
    return base64.b64decode(conversion(string, 'd')).decode()


# taking user args from the terminal
if sys.argv[1] == '-e':
    print(encryption(sys.stdin.read()))
if sys.argv[1] == '-d':
    print(decryption(sys.stdin.read()))
