#!/usr/bin/python3
# -*- coding: utf-8 -*-

import configparser, urllib
import tornado.ioloop
import tornado.web

class OpenXSD3:
    def __init__(self, configFile="Config.ini"):
        self.config = configparser.ConfigParser()
        self.config.read(configFile)

    class ManagerHandler(tornado.web.RequestHandler):
        def get(self):
            self.write("Hello, world")

    class CoreHandler(tornado.web.RequestHandler):
        def post(self):
            self.write("yo")

    def Run(self):
        self.application = tornado.web.Application(
            [
                (r"/", self.ManagerHandler),
                (r"/", self.CoreHandler),
            ]
        )

        self.application.listen(8080)
        tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    print("Welcome on OpenXSD3 - Copyright(C) 2015 Clint Mourlevat\r\n")
    Main = OpenXSD3()
    Main.Run()