from sieve import sieve

def func(x):
    return sieve(x)


def test_answer():
    assert func(42) == "2 3 5 7 11 13 17 19 23 29 31 37 41 "

