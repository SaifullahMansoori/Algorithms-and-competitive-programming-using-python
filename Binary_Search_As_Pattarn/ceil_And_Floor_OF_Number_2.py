 #
 # * This program demonstrates finding the ceiling and floor of a target number in a sorted array using binary search.
 # * The user inputs the number of test cases and an array for each test case.
 # * For each test case, the program finds the ceiling and floor of the target number in the array using binary search.
 # * If the target number is not present in the array, it finds the next greater (ceiling) or next smaller (floor) number.
 # * The program then prints the result for each test case.
 # *
 # * Author: Saifullah Mansoori


def ceiling(arr, target):
    left = 0
    right = len(arr) - 1
    index = -1

    while left <= right:
        mid = left + (right - left) // 2  # Calculate the middle index
        # Find the target in the array
        if arr[mid] == target:
            index = mid
            break
        elif arr[mid] < target:
            # Search in the right part of the array
            left = mid + 1
        else:
            # Search in the left part of the array
            right = mid - 1

    # Check if the target was in the array or not
    if index == -1:
        # Print the ceiling of the number (next greater number)
        print(arr[left])
    else:
        # Print the index of the target which was found in the array
        print(index)

def floor(arr, target):
    left = 0
    right = len(arr) - 1
    index = -1

    while left <= right:
        mid = left + (right - left) // 2  # Calculate the middle index
        # Find the target in the array
        if arr[mid] == target:
            index = mid
            break
        elif arr[mid] < target:
            # Search in the right part of the array
            left = mid + 1
        else:
            # Search in the left part of the array
            right = mid - 1

    # Check if the target was in the array or not
    if index == -1:
        # Print the floor of the number (next smaller number)
        print(arr[right])
    else:
        # Print the index of the target which was found in the array
        print(index)

def main():
    test_cases = int(input())  # Getting the number of test cases from the user
    for _ in range(test_cases):
        n = int(input())  # Number of elements in the array
        arr = list(map(int, input().split()))  # Input array elements
        target = int(input())  # The number to find the ceiling and floor for

        # Call the algorithm functions and print the results
        ceiling(arr, target)
        floor(arr, target)

if __name__ == "__main__":
    main()
