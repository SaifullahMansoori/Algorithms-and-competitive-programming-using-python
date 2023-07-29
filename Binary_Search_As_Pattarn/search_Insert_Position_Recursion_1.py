# /**
#  * This program demonstrates finding the insert position of a target element in a sorted array using binary search and recursion.
#  * The user inputs the number of test cases and an array for each test case.
#  * For each test case, the program finds the insert position of the target element in the array using binary search and recursion.
#  * The program then prints the insert position for each test case.
#  *
#  * Author: Saifullah Mansoori
#  */

def find_insert_position(arr, target):
    return insert_position_recursion(arr, 0, len(arr) - 1, target)

def insert_position_recursion(arr, left, right, key):
    # Base case: If left is greater than right or if left is out of array bounds, return the current left index as the insert position
    if left > right or left >= len(arr) or right < 0:
        return left

    mid = left + (right - left) // 2  # Calculate the middle index

    if arr[mid] < key:
        # If the target element is greater than the middle element, search in the right part of the array
        return insert_position_recursion(arr, mid + 1, right, key)
    else:
        # If the target element is less than or equal to the middle element, search in the left part of the array
        return insert_position_recursion(arr, left, mid - 1, key)

def main():
    test_cases = int(input())  # Getting the number of test cases from the user

    # Process each test case
    for _ in range(test_cases):
        # Call the helper function for each test case
        helper()

def helper():
    n = int(input())  # Number of elements in the array
    arr = list(map(int, input().split()))  # Input array elements as integers
    target = int(input())  # The number to find the insert position of

    # Call the algorithm function to find the insert position and print the result
    insert_position = find_insert_position(arr, target)
    print(insert_position)

if __name__ == "__main__":
    main()
