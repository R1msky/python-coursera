import tempfile
import os
import uuid
from os.path import dirname


class File:
    def __init__(self, path):
        if not os.path.exists(path):
            open(path, 'tw', encoding='utf-8').close()

        self.path = path
        self.iterator = None

    def __add__(self, other):
        new_path = os.path.join(
            tempfile.gettempdir(),
            str(uuid.uuid4().hex)
        )
        new_file = type(self)(new_path)
        new_file.write(self.read() + other.read())

        return new_file

    def __iter__(self):
        with open(self.path, 'r') as f:
            self.iterator = f.readlines()
            self.iterator.reverse()

        return self

    def __next__(self):
        if len(self.iterator) > 0:
            return self.iterator.pop()
        else:
            self.iterator = None
            raise StopIteration

    def __str__(self):
        return os.path.abspath(self.path)

    def read(self):
        with open(self.path, 'r') as f:
            data = f.read()
            print(data)
            return data
        return ''

    def write(self, data):
        with open(self.path, 'w') as f:
            f.write(data)
            print(len(data))
            return len(data)
        return 0


if __name__ == '__main__':
    path_to_file = 'some_filename'
    print(os.path.exists(path_to_file))
    file_obj = File(path_to_file)
    print(os.path.exists(path_to_file))

    file_obj.read()

    file_obj.write('some text')

    file_obj.read()

    file_obj.write('other text')

    file_obj.read()

    file_obj_1 = File(path_to_file + '_1')
    file_obj_2 = File(path_to_file + '_2')
    file_obj_1.write('line 1\n')

    file_obj_2.write('line 2\n')

    new_file_obj = file_obj_1 + file_obj_2
    print(isinstance(new_file_obj, File))

    print(new_file_obj)

    for line in new_file_obj:
        print(ascii(line))
