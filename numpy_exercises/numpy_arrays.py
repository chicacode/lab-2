import numpy as np

# Task 1
# Crate array 1d
array_1d = np.arange(1, 31)

print("Array:", array_1d)

print("Shape of the array: ", array_1d.shape)

print("Element at index 10: ", array_1d[10])

# Task 2
array_2d = array_1d.reshape(6,5)

print("2d Arrays: ", array_2d)

print("Element at row 3, column 4: ", array_2d[2,3])

# Task 3 - Subsetting Array

third_row = array_2d[2, :]
print(" Third Row: ", third_row)

subset_arr = array_2d[:2, -3]
print(" First two rows and last three columns: ", subset_arr)

# Task 4 Random

random_int = np.random.randint(10, 100, size=15)

print("Random int: ", random_int)

max_val = random_int.max()
min_val = random_int.min()

print("Max value: ", max_val)
print("Min val: ", min_val)

# Task 5 2d Random Array
random_2d_array = np.random.randint(0, 51, size=(4,4))
print("2d Random int: ", random_2d_array)

sum_items = random_2d_array.sum()
print("Sum result od all items: ", sum_items)

# Task 6 Manipulating Arrays

random_array_5 = np.random.randint(1,21, size=(5,5))
print("Random 5x5 array: ", random_array_5)

random_array_5[1, :] = 0
print("Values second row 0: ", random_array_5)

# replace values
random_array_5[random_array_5 > 10] = 99
print("Values after replacing", random_array_5)

# Task 7 Arithmetic Operations Array

arr_1 = np.random.randint(1,11, size=5 )
arr_2 = np.random.randint(1,11, size=5 )
print("Arr 1: ", arr_1)
print("Arr 2: ", arr_2)

addition = arr_1 + arr_2
substraction = arr_1 - arr_2
multiplication = arr_1 * arr_2

print("Result addition: ", addition)
print("Result substraction: ", substraction)
print("Result multiplication: ", multiplication)

# Task 8 Broadcasting in Numpy

arr_1_broadcasting = np.array([2,4,6,8])
arr_2_broadcasting = np.random.randint(1,6,size=(3,4))
print("2nd Array: ", arr_2_broadcasting)
result_broadcasting = arr_2_broadcasting + arr_1_broadcasting
print("Result broadcasting: ", result_broadcasting)
# Task 9 Filtering an Array


# Task 10 Reshaping Array

