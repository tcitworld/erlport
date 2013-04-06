from erlport import Atom, erlang

def switch(n):
    result = 0
    for i in range(n):
        _, result = erlang.call(Atom(b"python3_tests"), Atom(b"test_callback"),
            [(result, i)])
    return n

def setup_message_handler():
    def handler(message):
        erlang.call(Atom(b"python3_tests"), Atom(b"test_callback"),
            [(Atom(b"message"), message)])
    erlang.set_message_handler(handler)

def setup_faulty_message_handler():
    def handler(message):
        raise ValueError(message)
    erlang.set_message_handler(handler)

def recurse(python, n):
    if n <= 0:
        return Atom(b"done")
    return erlang.call(Atom(b"python3_tests"), Atom(b"recurse"),
        [python, n - 1])

def identity(v):
    return v

def length(v):
    return len(v)

def print_string(s):
    print(s.to_string())

class TestClass(object):
    class TestSubClass(object):
        @staticmethod
        def test_method():
            return Atom(b"done")
