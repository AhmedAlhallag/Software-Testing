import os

cwd = os.path.dirname(os.path.realpath(__file__))


class Files():
    def __init__(self, filename=None):
        if filename:
            self.filename = cwd + "\\" + filename

        else:
            self.filename = None
        self.memory = None

    def set_filename(self, filename):
        self.filename = cwd + "\\" + filename

    def read_file(self):
        try:
            afile = open(self.filename, "r")
        except FileNotFoundError:
            raise FileNotFoundError(
                f"[FILE_NOT_FOUND] file {self.filename} does not exist.")
        data = afile.readlines()
        afile.close()
        return data

    def write_file(self, contents, mode):
        afile = open(self.filename, mode)
        afile.write(str(contents)+"\n")
        afile.close()
        return "[WRITING_DONE]"

    def set_memory(self):
        self.memory = self.read_file()

    def get_memory(self):
        return self.memory

    def say_hello(self, name=None):
        if name:
            print(f"Hello {name}!")
        else:
            print("Hello Stranger!")
