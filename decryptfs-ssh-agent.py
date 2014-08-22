#!/usr/bin/env python
#
# Original author: kasperd at kasperd.net
# Code found at http://serverfault.com/questions/622344
#

from sys import argv
from os import environ
import socket

s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
s.connect(environ['SSH_AUTH_SOCK'])

def encode_int(v):
    return ('%08x' % v).decode('hex')

def encode_string(s):
    return encode_int(len(s)) + s

def encode_mpint(v):
    h = '%x' % v
    if len(h) & 1: h = '0' + h
    return ('%04x%s' % (len(h) * 4, h)).decode('hex')

key_blob = argv[1].decode('base64')
msg = 'ecryptfs-decrypt ' + argv[2]

s.send(encode_string(chr(13) +
                     encode_string(key_blob) +
                     encode_string(msg) +
                     encode_int(0)))

response = s.recv(1024)

assert response == encode_string(chr(14) + response[5:]), argv[1]

passphrase = response[-48:].encode('base64').replace('\n', '')

print passphrase
