import argparse
import tempfile
import json
from os import path, remove

STORAGE_PATH = path.join(tempfile.gettempdir(), 'storage.data')


def get_data():
    if not path.exists(STORAGE_PATH):
        return {}

    with open(STORAGE_PATH, 'r') as f:
        raw_data = f.read()
        if raw_data:
            return json.loads(raw_data)

    return {}


def put(key, value):
    data = get_data()

    if key in data:
        data[key].append(value)
    else:
        data[key] = [value]

    with open(STORAGE_PATH, 'w') as f:
        json.dump(data, f)


def get(key):
    data = get_data()

    return data.get(key)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', help='Key')
    parser.add_argument('--val', help='Value')
    parser.add_argument('--clear', action='store_true', help='Clear')

    args = parser.parse_args()

    if args.clear:
        remove(STORAGE_PATH)
    elif args.key and args.val:
        put(args.key, args.val)
    elif args.key:
        try:
            if len(get(args.key)) > 1:
                print(', '.join(get(args.key)))
            else:
                print(*get(args.key))
        except:
            print(None)
            
    else:
        print('Wrong command')
