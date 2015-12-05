#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket, threading

class Manager:
    def Run(self, hostname="0.0.0.0", port=8080):
        self.HttpBreak = "\r\n"

        self.Sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.Sock.bind((hostname, int(port)))
        self.Sock.listen(0)

        while True:
            client, address = self.Sock.accept()
            ClientThread = threading.Thread(target=self.Handle , args=(client, address,))
            ClientThread.start()

    def ParseHeader(self, rawHeader):
        request = {}
        request["method"] = rawHeader.split(self.HttpBreak)[0].split(" ")[0]
        request["path"] = rawHeader.split(self.HttpBreak)[0].split(" ")[1]
        request["version"] = rawHeader.split(self.HttpBreak)[0].split(" ")[2]
        for line in rawHeader.split(self.HttpBreak):
            line = line.split(": ")
            try:
                request[line[0]] = line[1]
            except:
                pass
        return request

    def ParsePath(self, path, method):
        pass

    def FormatRequest(self, request):
        pass

    def FormatResponse(self, content="None", statusCode=200, statusMessage="OK", request={}):
        rts = "HTTP/1.1 " + str(statusCode) + " " + statusMessage + self.HttpBreak
        request["Content-Type"] = "text/html"
        request["Content-Length"] = str(len(content))
        request["Connection"] = "close"
        for name in request:
            rts += str(name) + ": " + request[name] + self.HttpBreak
        rts += self.HttpBreak
        rts += content
        return rts

    def Handle(self, client, address):
        header = self.ParseHeader(client.recv(1024).decode("utf-8"))
        response = self.FormatResponse("salut")
        client.sendall(response)
        client.close()
