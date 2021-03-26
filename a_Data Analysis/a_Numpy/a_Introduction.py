"""
First you need to install Numpy
There are two way to install Numpy
    1. Conda 2. pip
For conda installation you need to install anaconda
    Here the Download link of anaconda:
    https://www.anaconda.com/products/individual#Downloads

    conda installation command: > conda install numpy
    pip installation command: > pip install numpy

    Further information about Numpy Installation visit this link:
    https://numpy.org/install/


"""

"""
    NumPy is the fundamental package for scientific computing in Python.
    It is a Python library that provides a multidimensional array object,
    various derived objects (such as masked arrays and matrices), and an
    assortment of routines for fast operations on arrays, including mathematical,
    logical, shape manipulation, sorting, selecting, I/O, discrete Fourier transforms,
    basic linear algebra, basic statistical operations, random simulation and much more.

    Further information See the numpy documentation here:
    https://numpy.org/doc/stable/
"""

import numpy as np

array = [1, 4, 3, 5]
print(array)  # Output: [1, 4, 3, 5]

# Numpy show an array like  Matrix
array1 = np.array(array)
print(array1)  # Output: [1 4 3 5]

arr = [[2, 4, 1], [5, 3, 4], [3, 5, 6]]
print(arr)  # Output: [[2, 4, 1], [5, 3, 4], [3, 5, 6]]
print(type(arr))  # Output: <class 'list'>

n_arr = np.array(arr)
print(n_arr)
"""
Output:
        [[2 4 1]
         [5 3 4]
         [3 5 6]]
"""
print(n_arr.dtype)  # Output: int32
