import json
import functools

def to_json(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        data = json.dumps(func(*args, **kwargs))
        return data

    return wrapped


@to_json
def get_data():
    return {
        'data': 42
    }


if __name__ == '__main__':
    print(get_data())

