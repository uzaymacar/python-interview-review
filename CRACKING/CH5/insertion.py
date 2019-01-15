# BIT OPERATIONS

# x << y
# Returns x with the bits shifted to the left by y places 
# (and new bits on the right-hand-side are zeros). This is the same as multiplying x by 2**y (x 2^y).

# x >> y
# Returns x with the bits shifted to the right by y places. 
# This is the same as dividing x by 2**y ( // 2^y).

# x & y
# Does a "bitwise and". Each bit of the output is 1 if the 
# corresponding bit of x AND of y is 1, otherwise it's 0.

# x | y
# Does a "bitwise or". Each bit of the output is 0 if the corresponding 
# bit of x AND of y is 0, otherwise it's 1.

# ~ x
# Returns the complement of x - the number you get by switching each 1 for a 0 and 
# each 0 for a 1. This is the same as -x - 1. Also called the NOT operator.
# ~0 is a sequence of 1's.

# x ^ y
# Does a "bitwise exclusive or". Each bit of the output is the same as the 
# corresponding bit in x if that bit in y is 0, and it's the complement of the bit in x 
# if that bit in y is 1. Also called the XOR operator. If you XOR a bit with its
# own negated value, you will always get a 1: a ^ (~a) = 111...1

# TWO'S COMPLEMENT AND NEGATIVE NUMBERS

# The binary representation of -K (negative K) as a N-bit number is the
# contanetation of [1] (sign bit to indicate -) and [2^(N-1) - K]
# -3 = 1101 => -1*2^3 + 1*2^2 + 0*2^1 + 1*2^0

# Another way to calculate: 1) Invert bits in the positive representation,
# 2) Add 1, 3) Prepend the sign bit as 1 to indicate negativeness
# +3 = 011 => 1) 100, 2) 101, 3) 1101 (DONE)


# n & (n - 1) == 0 checks if n is a power of 2 or if n is 0.
# To see this, you had to try varied test cases!

# DIFFERENCE BETWEEN ARITHMETIC (>>) AND LOGICAL SHIFT (>>>)

# In a logical right shift, we shift the bits as visually expected and put a 0
# in the most significant bit (MSB). -75 >>> 1 = +90 (notice the sign bit change)

# Whereas in an arithmetic right shift, we essentially divide the number by two by
# shifting the values to the right but filling in the new bits with the
# value of the previous sign bit. This time, -75 >> 1 = -38 (notice that sign bit didn't change)

# A sequence of all 1s in a SIGNED integer represents -1

# There is no logical shift in Python so we implement it ourselves.
def right_logical_shift(val, n):
    if val >= 0:
        return val >> n
    else:
        return (val + 0x100000000) >> n

def repeated_arithmetic_shift(x, count):
    for i in range(count):
        x >>= 1 # right arithmetic shift by 1
    return x

def repeated_logical_shift(x, count):
    for i in range(count):
        right_logical_shift(x, 1) # right logical shift by 1
    return x

# returns True if the bit at location i is 1 and False if is 0
def get_bit(num, i):
    return (num & (1 << i)) != 0

# sets the bit at location i to 1
def set_bit(num, i):
    return num | (1 << i)

# sets the bit at location i to 0
def clear_bit(num, i):
    mask = ~(1 << i)
    return num & mask

# sets the bits through locations MSB (most significant bit) to i to 0
def clear_bits_msb_through_i(num, i):
    mask = (1 << i) - 1
    return num & mask

# sets the bits through locations i to 0 to 0
def clear_bits_i_through_zero(num, i):
    mask = -1 << (i + 1)
    return num & mask

# updates the ith bit to a value v according to boolean parameter bit_is_1
def update_bit(num, i, bit_is_1):
    value = 0
    if bit_is_1:
        value = 1
    mask = ~(1 << i)
    return (num & mask) | (value << i)

# --------------------------------------------------------------------------------------- #
    
def insert(N, M, i, j):
    # don't forget to clear the bits
    add_value = 0
    for a in range(i):
        add_value += 2**a
    
    clear = (1 << j + 1) + add_value
    cleared_N = N & clear
    mask = M << i
    inserted = cleared_N | mask
    temp = N
    counter = 0
    while temp != 0:
        temp /= 2
        counter += 1
    for b in range(j + 1, counter + 1):
        if get_bit(N, b):
            inserted = set_bit(inserted, b) # set_bit returns a value!
    return inserted
    

print(insert(1024, 19, 2, 6))
# 1100