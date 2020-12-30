def xor(a, b):
    if bool(a and not b):
        return a
    elif bool(not a and b):
        return b
    return False
