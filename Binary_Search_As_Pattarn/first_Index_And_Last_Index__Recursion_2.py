# /**
#  * This program demonstrates finding the first and last index of a target element in a sorted array using recursion.
#  * The user inputs the number of test cases and an array for each test case.
#  * For each test case, the program finds the first and last index of the target element in the array using recursion.
#  * The program then prints the first and last index for each test case.
#  *
#  * Author: Saifullah Mansoori
#  */

def first_index(arr, key, left, right, first_index):
    if left > right or left >= len(arr) or right < 0:
        return first_index

    mid = left + (right - left) // 2
    if arr[mid] == key:
        first_index = mid
        # Continue searching in the left part of the array to find the first occurrence
        return first_index(arr, key, left, mid - 1, first_index)
    elif arr[mid] < key:
        # Search in the right part of the array
        return first_index(arr, key, mid + 1, right, first_index)
    else:
        # Search in the left part of the array
        return first_index(arr, key, left, mid - 1, first_index)

def last_index(arr, key, left, right, last_index):
    if left > right or left >= len(arr) or right < 0:
        return last_index

    mid = left + (right - left) // 2
    if arr[mid] == key:
        last_index = mid
        # Continue searching in the right part of the array to find the last occurrence
        return last_index(arr, key, mid + 1, right, last_index)
    elif arr[mid] < key:
        # Search in the right part of the array
        return last_index(arr, key, mid + 1, right, last_index)
    else:
        # Search in the left part of the array
        return last_index(arr, key, left, mid - 1, last_index)

def helper():
    n = int(input())  # Number of elements in the array
    arr = [int(x) for x in input().split()]  # Input array elements
    target = int(input())  # The number to find the first and last index of

    # Call the functions to get the first and last index and print the results
    first = first_index(arr, target, 0, len(arr) - 1, -1)
    last = last_index(arr, target, 0, len(arr) - 1, -1)
    print(first, last)

def main():
    test_cases = int(input())  # Getting the number of test cases from the user

    # Process each test case
    for _ in range(test_cases):
        # Call the helper function for each test case
        helper()

if __name__ == "__main__":
    main()
