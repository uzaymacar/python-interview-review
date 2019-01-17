def get_bit(num, i):
    return (num & (1 << i)) != 0

def binary_to_string(num):
    result = ""
    if num > 1 or num < 0:
        return "ERROR"
    if num == 0:
        return "0" * 32
    elif num == 1:
        return "0" * 31 + "1" * 1
    else:
        value = int(str(num)[2:])
        for i in range(32):
            if (value >> i) & 1 == 1: # shift right to find the bit values
                result = "1" + result
            else:
                result = "0" + result
        
        return result
        
print(binary_to_string(0.72))