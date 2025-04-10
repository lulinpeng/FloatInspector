import random
import struct
import math

BYTE_BIT_LEN = 8
FLOAT64_MAGNITUDE_BIT_LEN = 11
FLOAT64_MANTISSA_BIT_LEN = 52

class FloatInspector:
    @staticmethod
    def random_n_bit_number(n:int):
        '''choose a random number from [0, 2^n)'''
        r = random.randint(0, 1 << n)
        return r
    
    @staticmethod
    def is_bin_str(a:str):
        '''check if the string is a binary string'''
        return set(a).issubset({'0','1'})
    
    @staticmethod
    def bin_to_bytes(bin_str:str, padding:str = '0'):
        '''
           convert a binary string into a byte array, 
           padding with zeros on the left by default 
           to ensure the length is a multiple of 8.
           e.g., '011011' -> '00011011' ->  '\\x1b' '''
        assert(FloatInspector.is_bin_str(bin_str))
        assert(padding == '0' or padding == '1')
        padded_length = math.ceil(len(bin_str)*1.0/BYTE_BIT_LEN) * BYTE_BIT_LEN
        padded_str = bin_str.rjust(padded_length, padding)
        b = []
        for i in range(padded_length // BYTE_BIT_LEN):
           b.append(int(padded_str[i*BYTE_BIT_LEN:(i+1)*BYTE_BIT_LEN], 2))
        return bytes(b)
    
    @staticmethod
    def bin_to_int(bin_str:str):
        '''convert a binary string into an integer'''
        assert(FloatInspector.is_bin_str(bin_str))
        return int(bin_str, 2)
    
    @staticmethod
    def float64_to_bin(f:float):
        ''' return the binary representation of big, IEEE 754, of a float64 number'''
        import struct
        packed = struct.pack('>d', f)  # '>d' for big-endian byte order
        unpacked = struct.unpack('>q', packed)[0]
        return f'{unpacked:064b}'

    @staticmethod
    def get_float64_magnitude_bin(f:float):
        ''' return the magnitude part of a float64 number '''
        bin_str = FloatInspector.float64_to_bin(f)
        return bin_str[1:1+FLOAT64_MAGNITUDE_BIT_LEN]
    
    @staticmethod
    def get_float64_mantissa_bin(f:float):
        ''' return the binary representation of mantissa part of a float64 number '''
        bin_str = FloatInspector.float64_to_bin(f)
        return bin_str[1+FLOAT64_MAGNITUDE_BIT_LEN:]
    
    @staticmethod
    def get_float64_sign_bin(f:float):
        ''' return the sign bit of a float64 number '''
        return '1' if f < 0 else '0'

    @staticmethod
    def get_float64_magnitude(f:float):
        ''' return the magnitude part of a float64 number '''
        magnitude_bin = FloatInspector.get_float64_magnitude_bin(f)
        magnitude = int(magnitude_bin, 2) - (1<<FLOAT64_MAGNITUDE_BIT_LEN - 1)
        return magnitude
    
    @staticmethod
    def get_float64_mantissa(f:float):
        ''' return the mantissa part of a float64 number '''
        mantissa_bin = '1' + FloatInspector.get_float64_mantissa_bin(f)
        mantissa = int(mantissa_bin, 2)
        return mantissa
    
    @staticmethod
    def get_float64_sign(f:float):
        ''' return the sign bit of a float64 number '''
        return 1 if f < 0 else 0
    
    @staticmethod
    def pretty_print(f:float):
        return f'({FloatInspector.get_float64_sign(f)}, {FloatInspector.get_float64_magnitude_bin(f)}, {FloatInspector.get_float64_mantissa_bin(f)})'

print(f'random number: {FloatInspector.random_n_bit_number(64)}')

print(f'binary representation: {FloatInspector.float64_to_bin(1.1)}')

print(f'sign bits: {FloatInspector.get_float64_sign_bin(1.1)}')

print(f'magnitude bits: {FloatInspector.get_float64_magnitude_bin(1.1)}')

print(f'mantissa bits: {FloatInspector.get_float64_mantissa_bin(1.1)}')

print(f'pretty_print: {FloatInspector.pretty_print(1.1)}')

