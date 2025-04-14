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

# FYI
| Type Name | Sign Bits | Magnitude Bits |	Mantissa Bits | Total Bits | Alias | Supported Hardware |
|:--------:| :---------: | :---------:|:--------:| :--------: |  :--------: |  :--------: |
|FP64 | 1 | 11 | 52 | 64| double-precision | CPUs, High-end GPUs | 
|FP32 | 1 | 8 | 23 | 32| single-precision | All CPUs/GPUs |
|FP16 | 1 | 5 | 10 | 16| half-precision | NVIDIA/AMD GPUs, AI accelerators | 
|FP8 (E4M3) | 1 | 4 | 3 | 8| - | NVIDIA H100, AMD CDNA3 |
|FP8 (E5M3) | 1 | 5 | 2 | 8| - | NVIDIA H100, AMD CDNA3 | 
|FP4 (E2M1) | 1 | 2 | 1 | 4| - | Experimental hardware (some AI accelerators/FPGAs) ｜
|FP4 (E3M0) | 1 | 3 | 0 | 4| - | Research prototypes (e.g., custom chips) ｜
|TF32 | 1 | 8 | 10 | 19| TensorFloat-32 (occupy 32 bits, but only 19 bits in computation)| NVIDIA A100, H100 GPUs | 
|BF16 | 1 | 8 | 7 | 16| brain floating point | Google TPU, NVIDIA Ampere/Ada GPUs | 

Note that *TF32 uses 32-bit storage but only 19 bits (1 sign + 8 exponent + 10 mantissa) in computation.*

