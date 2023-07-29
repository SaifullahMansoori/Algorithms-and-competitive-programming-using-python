# /**
#  * This program demonstrates finding the first index and last index of a target element in a sorted array using binary search.
#  * The user inputs the number of test cases and an array for each test case.
#  * For each test case, the program finds the first index and last index of the target element in the array using binary search.
#  * The program then prints the first index and last index for each test case.
#  *
#  * Author: Saifullah Mansoori
#  */

def first_index(arr, target):
    first_index = -1
    left = 0
    right = len(arr) - 1
    # Finding the first Index
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            first_index = mid
            # Search again to find the first occurrence
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    print(first_index, end=' ')

def last_index(arr, target):
    left = 0
    right = len(arr) - 1
    last_index = -1
    # Finding the last Index
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            last_index = mid
            # Search again to find the last occurrence
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    print(last_index)

def helper():
    n = int(input())  # Number of elements in the array
    arr = [int(x) for x in input().split()]  # Input array elements
    target = int(input())  # The number to find the first index and last index of

    # Call the functions to get the first and last index and print the results
    first_index(arr, target)
    last_index(arr, target)

def main():
    test_cases = int(input())  # Getting the number of test cases from the user

    # Process each test case
    for _ in range(test_cases):
        # Call the helper function for each test case
        helper()

if __name__ == "__main__":
    main()
