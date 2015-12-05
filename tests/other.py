import tornado.ioloop
import tornado.web
from Stack import *

class ManagerHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class CoreHandler(tornado.web.RequestHandler):
    def post(self):
        self.write("yo")

application = tornado.web.Application(
    [
        (r"/", ManagerHandler),
        (r"/", CoreHandler),
    ]
)
