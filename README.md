# FloatInspector
The fundamental **difference between floating-point and integer arithmetic** lies in their overflow handling: **floating-point operations truncate lower-order bits**, whereas **integer operations truncate higher-order bits when overflow occurs**.

# RUN
```shell
python floatinspector.py
input: 4.2 <class 'float'>
# 0100000000010000110011001100110011001100110011001100110011001101
# sign, magnitude, mantissa = 0, 10000000001, 0000110011001100110011001100110011001100110011001101
# 1.0000110011001100110011001100110011001100110011001101 x 2^{2}

python floatinspector.py --value 3.14
# input: 3.14 <class 'float'>
# 0100000000001001000111101011100001010001111010111000010100011111
# sign, magnitude, mantissa = 0, 10000000000, 1001000111101011100001010001111010111000010100011111
# 1.1001000111101011100001010001111010111000010100011111 x 2^{1}
```

# Float64
![image](https://github.com/lulinpeng/FloatInspector/blob/main/resources/float64.png)

# Truncation
![image](https://github.com/lulinpeng/FloatInspector/blob/main/resources/truncation.png)
