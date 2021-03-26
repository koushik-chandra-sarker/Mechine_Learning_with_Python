import numpy as n

ar = n.arange(3, 12)

print(ar)  # Output: [ 3  4  5  6  7  8  9 10 11]

print(ar + ar)  # Output: [ 6  8 10 12 14 16 18 20 22]

print(ar - ar)  # Output: [0 0 0 0 0 0 0 0 0]

print(ar * ar)  # Output: [  9  16  25  36  49  64  81 100 121]

print(ar - 2)  # Output: [1 2 3 4 5 6 7 8 9]

print(ar / 2)  # Output: [1.5 2.  2.5 3.  3.5 4.  4.5 5.  5.5]

# print(ar / 0)  # RuntimeWarning: divide by zero encountered in true_divide

print(ar ** 2)  # Output: [  9  16  25  36  49  64  81 100 121]

# Squire root everything in the array
print(n.sqrt(ar))
"""
# Output: 
[1.73205081 2.         2.23606798 2.44948974 2.64575131 2.82842712
 3.         3.16227766 3.31662479]
"""

# Exponential everything in the array
print(n.exp(ar))
"""
# Output: 
[2.00855369e+01 5.45981500e+01 1.48413159e+02 4.03428793e+02
 1.09663316e+03 2.98095799e+03 8.10308393e+03 2.20264658e+04
 5.98741417e+04]
"""


# sin everything in the array
print(n.sin(ar))
"""
# Output: 
[ 0.14112001 -0.7568025  -0.95892427 -0.2794155   0.6569866   0.98935825
  0.41211849 -0.54402111 -0.99999021]
"""

# sin everything in the array
print(n.log(ar))
"""
# Output: 
[1.09861229 1.38629436 1.60943791 1.79175947 1.94591015 2.07944154
 2.19722458 2.30258509 2.39789527]
"""


# Learn For From: https://numpy.org/doc/stable/reference/ufuncs.html
