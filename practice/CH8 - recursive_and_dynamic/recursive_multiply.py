# Ternary operator in Java and C : c = a > b ? 1 : 0
# Ternary operator in Python c = 1 if a > b else 0 (a lot easier!)

def recursive_multiply(a, b):
    if b == 1:
        return a
    
    return a + recursive_multiply(a, b - 1)

print(recursive_multiply(6, 9))
    