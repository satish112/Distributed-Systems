import socket
import os, os.path

class centralized:
    def __init__(self, host, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setblocking(True)
        s.bind(('localhost', port))
        return s
