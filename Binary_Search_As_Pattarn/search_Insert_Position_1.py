# /**
#  * This program demonstrates finding the insert position of a target element in a sorted array using binary search.
#  * The user inputs the number of test cases and an array for each test case.
#  * For each test case, the program finds the insert position of the target element in the array using binary search.
#  * The program then prints the insert position for each test case.
#  *
#  * Author: Saifullah Mansoori
#  */

def find_insert_position(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        # If the target element is greater than the middle element, search in the right part of the array
        if arr[mid] < target:
            left = mid + 1
        # If the target element is less than or equal to the middle element, search in the left part of the array
        else:
            right = mid - 1

    # The insert position for the target element is the value of 'left'
    return left

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
