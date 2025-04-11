import random
import struct
import math

BYTE_BIT_LEN = 8
FLOAT64_MAGNITUDE_BIT_LEN = 11
FLOAT64_MANTISSA_BIT_LEN = 52
FLOAT64_MAGNITUDE_OFFSET = (1 << (FLOAT64_MAGNITUDE_BIT_LEN -1)) - 1

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
        '''return the binary representation of big, IEEE 754, of a float64 number'''
        # float -> bytes
        packed_bytes = struct.pack('>d', f)  # '>' for big-endian byte order, # https://docs.python.org/3/library/struct.html
        # bytes -> integer
        a = int.from_bytes(packed_bytes, byteorder='big')
        # integer -> bit string
        return bin(a)[2:].zfill(64)

    @staticmethod
    def get_float64_magnitude_bin(f:float):
        '''return the magnitude part of a float64 number '''
        bin_str = FloatInspector.float64_to_bin(f)
        return bin_str[1:1+FLOAT64_MAGNITUDE_BIT_LEN]
    
    @staticmethod
    def get_float64_mantissa_bin(f:float):
        '''return the binary representation of mantissa part of a float64 number '''
        bin_str = FloatInspector.float64_to_bin(f)
        return bin_str[1+FLOAT64_MAGNITUDE_BIT_LEN:]
    
    @staticmethod
    def get_float64_sign_bin(f:float):
        ''' return the sign bit of a float64 number '''
        return '1' if f < 0 else '0'

    @staticmethod
    def get_float64_magnitude_int(f:float):
        '''return the magnitude part of a float64 number '''
        magnitude_bin = FloatInspector.get_float64_magnitude_bin(f)
        magnitude = int(magnitude_bin, 2)
        return magnitude
    
    @staticmethod
    def get_float64_exponent(f:float):
        '''return the binary exponent of a float64 number '''
        return int(FloatInspector.get_float64_magnitude_bin(f), 2) - FLOAT64_MAGNITUDE_OFFSET
    
    @staticmethod
    def get_float64_mantissa(f:float):
        '''return the mantissa part of a float64 number '''
        mantissa_bin = '1' + FloatInspector.get_float64_mantissa_bin(f)
        mantissa = int(mantissa_bin, 2)
        return mantissa
    
    @staticmethod
    def get_float64_sign(f:float):
        '''return the sign bit of a float64 number '''
        return 1 if f < 0 else 0
    
    @staticmethod
    def split_print(f:float):
        '''return sign/magnitude/mantissa in bit-form seperately'''
        return f'{FloatInspector.get_float64_sign(f)}, {FloatInspector.get_float64_magnitude_bin(f)}, {FloatInspector.get_float64_mantissa_bin(f)}'

    @staticmethod
    def scientific_notation_print(f:float):
        '''return the representation in scientific notation of a float64 number'''
        sign = -1 if FloatInspector.get_float64_sign(f) else 1
        mantissa = FloatInspector.get_float64_mantissa_bin(f).rstrip('0')
        exponent = FloatInspector.get_float64_exponent(f)
        return f"{sign}.{mantissa}" if exponent == 0 else f"{sign}.{mantissa} x 2^{{{exponent}}}"

print(f'random number: {FloatInspector.random_n_bit_number(64)}')

f = -0.001

print(f'binary representation: {FloatInspector.float64_to_bin(f)}')

print(f'sign bits: {FloatInspector.get_float64_sign_bin(f)}')

print(f'magnitude bits: {FloatInspector.get_float64_magnitude_bin(f)}')

print(f'mantissa bits: {FloatInspector.get_float64_mantissa_bin(f)}')

print(f'split_print: {FloatInspector.split_print(f)}')

print(f'scientific_print: {FloatInspector.scientific_notation_print(f)}')




