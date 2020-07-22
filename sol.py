class FileReader:
    def __init__(self, path):
        self.path = path

    def read(self):
        try:
            with open(self.path) as f:
                return f.read()
        except IOError:
            return ""


file = FileReader("/Users/egorzhukov/PycharmProjects/game/sq.py")
print(file.read())