class Blob:
    def Write(self, string, path="blob://"):
        pass

    def Read(self, path):
        obj = self.Object()
        obj.set("salut")
        print(obj.get())

    def WriteBinary(self, value, path="blob://"):
        pass

    class Object:
        def __init__(self):
            self.content = None
            self.object = {}

        def get(self):
            self.object["content"] = self.content
            return self.object

        def set(self, value):
            self.content = value

    class Properties:
        def fuck(self):
            pass