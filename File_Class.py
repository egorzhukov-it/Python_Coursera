import os.path
import tempfile


class File:

    def __init__(self, path):
        self.path = path

    def __add__(self, other):
        new_path = os.path.join(tempfile.gettempdir(), 'sum_res.txt')

        with open(self.path, 'r') as f1:
            first_file = f1.read()
            f1.close()
        with open(other.path, 'r') as f2:
            sec_file = f2.read()
            f2.close()
        new_file = first_file + sec_file
        with open(new_path, 'w') as fn:
            fn.write(new_file)
            fn.close()
        return File(new_path)

    def write(self, line):
        with open(self.path, 'a') as f:
            f.write(line + '\n')
            f.close()

    def __str__(self):
        return self.path

    def __getitem__(self, key):
        with open(self.path, 'r') as f:
            self.data = f.read().split()
            self.index = len(self.data)
            f.close()
        return self.data[key]





