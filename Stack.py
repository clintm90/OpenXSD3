import uuid, base64

class Stack:
    def __init__(self, filename="resources/default.db"):
        self.CurrentStack = filename
        self.fp = open(self.CurrentStack, "a")

    def ReadAll(self):
        rts = {}
        self.fp = open(self.CurrentStack, "r")
        for i in self.fp.read().split("\n"):
            try:
                rts[i.split("=")[0]] = i.split("=")[1]
            except:
                pass
        return rts

    def Push(self, value):
        uid = str(uuid.uuid1())
        self.fp.write(uid + "=" + base64.b64encode(bytes(value, "UTF-8")).decode("UTF-8 ").replace("=", "&") + "\r\n")
        self.fp.close()
        return uid

    def Get(self, uid):
        return base64.b64decode((self.ReadAll()[uid]).replace("&", "=")).decode("UTF-8")

    def Close(self):
        self.fp.close()