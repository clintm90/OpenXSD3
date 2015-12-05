#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket, threading

class Core:
    def Run(self, hostname="0.0.0.0", port=89):
        self.Sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.Sock.bind((hostname, int(port)))
        self.Sock.listen(0)

        while True:
            client, address = self.Sock.accept()
            ClientThread = threading.Thread(target=self.Handle, args=(client, address,))
            ClientThread.start()

    def Handle(self, client, address):
        while True:
            data = client.recv(1024)
            print(str(data))
            data.sendall("fuck")