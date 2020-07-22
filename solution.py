class FileReader:
    def __init__(self, path):
        self.path = path

    def read(self):
        try:
            with open(self.path) as f:
                return f
        except IOError:
            "ERROR: FILE NOT FOUND!"


reader = FileReader("example.txt")
print(reader.read())
