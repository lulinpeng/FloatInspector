def is_overflow(a:int, n:int):
    '''returns True on overflow, False otherwise.'''
    assert(a > 0)
    bin_str = bin(a)[2:]
    return len(bin_str) > n

def lsb_trunc(a:int, n:int):
    '''LSB truncation'''
    assert(a > 0)
    bin_str = bin(a)[2:]
    if len(bin_str) > n:
        return int(bin_str[:n],2)
    return a

def msb_trunc(a:int, n:int):
    '''MSB truncation'''
    assert(a > 0)
    bin_str = bin(a)[2:]
    if len(bin_str) > n:
        return int(bin_str[-n:],2)
    return a

def add_with_lsb_trunc(a:int, b:int, n:int):
    return lsb_trunc(a + b, n)

def mul_with_lsb_trunc(a:int, b:int, n:int):
    return lsb_trunc(a * b, n)


def add_with_msb_trunc(a:int, b:int, n:int):
    return msb_trunc(a + b, n)

def mul_with_msb_trunc(a:int, b:int, n:int):
    return msb_trunc(a * b, n)

a = 100
b = 100
n = 10 # bit width
c = a * b
print(f'a = {a}')
print(f'b = {b}')
print(f'bit width = {n}\n')
print(f'a * b = {a * b}')
print(f'mul_with_lsb_trunc(a, b, n) = {mul_with_lsb_trunc(a, b, n)}')
print(f'mul_with_msb_trunc(a, b, n) = {mul_with_msb_trunc(a, b, n)}')
