import numpy as np

ar = np.arange(2, 10)
print(ar)  # Output: [2 3 4 5 6 7 8 9]

# Return number of given index
print(ar[4])  # Output: 6

# Return numbers of given start to stop index
print(ar[2:5])  # Output: [4 5 6]

# Return numbers of given 0 to stop index
print(ar[:4])  # Output: [2 3 4 5]

# Return numbers of given Start to end index
print(ar[3:])  # Output: [5 6 7 8 9]

ar[3:6] = 400
print(ar)  # Output: [  2   3   4 400 400 400   8   9]

arr_2s = np.array([[23, 34, 2], [2, 3, 32], [45, 3, 45]])

print(arr_2s)
"""
Output:
        [[23 34  2]
         [ 2  3 32]
         [45  3 45]]
"""

print(arr_2s[2])  # Output: [45  3 45]

print(arr_2s[1][2])  # Output: 32
print(arr_2s[:2, 1:])

"""
Output:
        [[34  2]
         [ 3 32]]
"""

print(arr_2s[:2])

"""
Output:
        [[23 34  2]
         [ 2  3 32]]
"""

arr = np.arange(1, 10)
print(arr)  # Output: [1 2 3 4 5 6 7 8 9]

bool_arr = arr > 6
print(bool_arr)  # Output:[False False False False False False  True  True  True]
print(arr[bool_arr])  # Output: [7 8 9]

print(arr[arr < 4])  # Output: [1 2 3]
