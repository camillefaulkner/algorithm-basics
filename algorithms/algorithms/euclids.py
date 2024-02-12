# find the greatest common denominatory of two numbers
# using Euclid's algorithm

def gcd(a, b):
    while (b != 0):
        temp = a
        a = b
        b = temp % b

    return a

print(gcd(60, 96)) # should be 12 
print(gcd(20, 8)) # should be 4




