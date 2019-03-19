


def finn(a):
    b=set(a)
    if len(a) == len(b):
        return False
    else:
        return True

assert finn([1,2,3]) is False , True
assert finn([1,2,1]) is True , False





