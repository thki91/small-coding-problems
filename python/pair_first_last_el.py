# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns
# the first and last element of that pair. For example, car(cons(3, 4))
# returns 3, and cdr(cons(3, 4)) returns 4.


def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(pair):
    def first(a, _):
        return a
    return pair(first)


def cdr(pair):
    def last(_, b):
        return b
    return pair(last)


first_el = car(cons(3, 4))
last_el = cdr(cons(3, 4))
print(first_el)
print(last_el)
