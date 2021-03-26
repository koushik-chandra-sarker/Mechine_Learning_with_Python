import numpy as np
arr = np.arange(10)  # Return evenly spaced values within a given interval.
print(arr)  # Output:[0 1 2 3 4 5 6 7 8 9]

arr = np.arange(0, 10, 2)  # arange(start, stop, increment)
print(arr)  # Output:[0 2 4 6 8]

'''
    zeros(shape, dtype=float, order='C') -> by default
        Return a new array of given shape and type, filled with zeros.

        shape : int or tuple of ints
            Shape of the new array, e.g., ``(2, 3)`` or ``2``.
        dtype : data-type, optional
            The desired data-type for the array, e.g., `numpy.int8`.  Default is
            `numpy.float64`.
        order : {'C', 'F'}, optional, default: 'C'
            Whether to store multi-dimensional data in row-major
            (C-style) or column-major (Fortran-style) order in
            memory.

'''
arr = np.zeros(4)

print(arr)  # Output: [0. 0. 0. 0.]
print(arr.dtype)  # Output: float64

arr = np.zeros((5,), dtype=int)
print(arr)  # Output: [0 0 0 0 0]

arr = np.zeros((4, 3))
print(arr)
"""
Output:
        [[0. 0. 0.]
         [0. 0. 0.]
         [0. 0. 0.]
         [0. 0. 0.]]
"""

# All property like np.zeros
arr = np.ones(3)
print(arr)  # Output: [1. 1. 1.]

arr = np.ones((5,), dtype=int)
print(arr)  # Output: [1 1 1 1 1]

arr = np.ones((4, 3))
print(arr)
"""
Output:
        [[1. 1. 1.]
         [1. 1. 1.]
         [1. 1. 1.]
         [1. 1. 1.]]
"""

"""
    linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None,axis=0): -> default

    Return evenly spaced numbers over a specified interval.

    Further About: https://numpy.org/doc/stable/reference/generated/numpy.linspace.html?highlight=linspace%20start%20stop%20num%20endpoint%20true%20retstep%20false%20dtype%20none%20axis
"""
arr = np.linspace(2.0, 4.0, num=5)

print(arr)  # Output: [2.  2.5 3.  3.5 4. ]

# Identity matrix
arr = np.eye(5)  # Return a 2-D array with ones on the diagonal and zeros elsewhere.
print(arr)
"""
Output:
        [[1. 0. 0. 0. 0.]
         [0. 1. 0. 0. 0.]
         [0. 0. 1. 0. 0.]
         [0. 0. 0. 1. 0.]
         [0. 0. 0. 0. 1.]]
"""

# Further info: https://numpy.org/doc/stable/reference/random/genen rated/numpy.random.rand.html?highlight=numpy%20random%20rand#numpy.random.rand
arr = np.random.rand(4)  # Random values in a given shape.
print(arr)  # Output: [0.65553181 0.24449588 0.97759153 0.51374844]

arr = np.random.rand(4, 3)  # Random values in a given shape(4x3).
print(arr)
"""
Output:
        [[0.31751676 0.14827447 0.66337305]
         [0.50374602 0.36386274 0.61071281]
         [0.87552215 0.8624482  0.77839218]
         [0.70932579 0.89535807 0.92543718]]
"""
arr = np.random.rand(4, 3, 2)  # Random values in a given shape.4 times (3x2)
print(arr)
"""
Output:
       [[[2.98099305e-01 3.25063773e-01]
          [1.37659172e-01 2.89883115e-01]
          [3.33283039e-01 7.92146830e-01]]

         [[3.69477412e-01 2.81581774e-01]
          [6.76359623e-01 8.90729357e-01]
          [9.18319448e-02 3.98140440e-02]]

         [[1.68225359e-01 2.49589259e-01]
          [5.41252974e-01 9.76071779e-01]
          [5.88979323e-01 6.43348325e-02]]

         [[4.08771261e-01 9.42253354e-01]
          [8.98243797e-01 6.98460650e-02]
          [2.56241540e-01 7.30011130e-04]]]
"""

arr = np.random.randn(4, 3)  # Return a sample (or samples) from the "standard normal" distribution.
print(arr)
"""
Output:
       [[ 0.60191027  1.74107877 -1.75349538]
 [ 1.97112487  0.23518889  0.04567072]
 [-0.35404847 -0.32357406 -0.62053774]
 [-0.50706131  0.68610668  0.1864317 ]]
"""

"""
    randint(low, high=None, size=None, dtype=int)

            Return random integers from `low` (inclusive) to `high` (exclusive).
"""
arr = np.random.randint(50)  # Return random integers from `0` to 50
print(arr)

arr = np.random.randint(20, 100)  # Return random integers from `20` to 50
print(arr)

arr = np.random.randint(20, 100, 10)  # Return 10 random integers from `20` to 50
print(arr)

arr = np.arange(5, 20)
print(arr)  # Output: [ 5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]

print(arr.reshape(3, 5))

"""
Output: 
    [[ 5  6  7  8  9]
     [10 11 12 13 14]
     [15 16 17 18 19]]
"""

# print(arr.reshape(4, 5))  # ValueError: cannot reshape array of size 15 into shape (4,5); we need  array of size 20.

arr = np.random.randint(15, 50, 15)
print(arr)  # Output like: [33 26 47 32 15 23 49 39 43 17 49 35 39 37 22]
print(arr.min())  # Return Minimum value
print(arr.max())  # Return maximum value

# Index number of Minimum and Maximum value
print(arr.argmin())  # Return index number of Minimum value
print(arr.argmax())  # Return index number of maximum value
