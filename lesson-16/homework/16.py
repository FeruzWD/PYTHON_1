1. Convert List to 1D Array
import numpy as np

lst = [12.23, 13.32, 100, 36.32]
arr = np.array(lst)

print("Original List:", lst)
print("One-dimensional NumPy array:", arr)

✅ 2. Create 3x3 Matrix (2 → 10)
arr = np.arange(2, 11).reshape(3, 3)
print(arr)


Output:

[[ 2  3  4]
 [ 5  6  7]
 [ 8  9 10]]

✅ 3. Null Vector (10) & Update Sixth Value
arr = np.zeros(10)
print("Original:", arr)

arr[5] = 11   # sixth element (index 5)
print("After update:", arr)

✅ 4. Array from 12 to 38
arr = np.arange(12, 38)
print(arr)

✅ 5. Convert Array to Float Type
arr = np.array([1, 2, 3, 4])
print("Original array:", arr)
print("Converted to float:", arr.astype(float))

✅ 6. Celsius to Fahrenheit Conversion

Formula: F = C * 9/5 + 32

celsius = np.array([0, 12, 45.21, 34, 99.91])
fahrenheit = celsius * 9/5 + 32

print("Values in Celsius:", celsius)
print("Values in Fahrenheit:", fahrenheit)

✅ 7. Append Values to Array
arr = np.array([10, 20, 30])
new_arr = np.append(arr, [40, 50, 60, 70, 80, 90])

print("Original array:", arr)
print("After append:", new_arr)

✅ 8. Array Statistical Functions
arr = np.random.randint(1, 100, 10)
print("Array:", arr)
print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard Deviation:", np.std(arr))

✅ 9. Find Min and Max
arr = np.random.rand(10, 10)  # random values between 0 and 1
print("Minimum:", arr.min())
print("Maximum:", arr.max())

✅ 10. 3x3x3 Array with Random Values
arr = np.random.rand(3, 3, 3)
print(arr)
