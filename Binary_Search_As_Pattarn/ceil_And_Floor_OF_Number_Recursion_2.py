 #
 # * This program demonstrates finding the ceiling and floor of a number in a sorted array using recursion.
 # * Ceiling: The smallest element in the array that is greater than or equal to the target.
 # * Floor: The greatest element in the array that is less than or equal to the target.
 # *
 # * The user inputs the number of test cases and the array elements for each test case.
 # * For each test case, the program finds the ceiling and floor of the given target in the array and prints the results.
 # * If the target is not found in the array, the program returns the next greater element for ceiling and the previous smaller element for floor, if available.
 # * If no greater element is found for ceiling or no smaller element is found for floor, it returns a specific value (-1 in this case) to indicate that the target is not found.
 # *
 # *
 # *
 # * @author Saifullah Mansoori

def ceiling(arr, target, left, right):
    if left > right:
        # Target not found, return the next greater element (if available)
        if left < len(arr):
            return arr[left]
        else:
            return -1  # Or some value to indicate target not found

    mid = left + (right - left) // 2  # Calculate the middle index
    if arr[mid] == target:
        return mid  # Target found, return the index
    elif arr[mid] < target:
        # Search in the right part of the array
        return ceiling(arr, target, mid + 1, right)
    else:
        # Search in the left part of the array
        return ceiling(arr, target, left, mid - 1)

def floor(arr, target, left, right):
    if left > right:
        # Target not found, return the previous smaller element (if available)
        if right >= 0:
            return arr[right]
        else:
            return -1  # Or some value to indicate target not found

    mid = left + (right - left) // 2  # Calculate the middle index
    if arr[mid] == target:
        return mid  # Target found, return the index
    elif arr[mid] < target:
        # Search in the right part of the array
        return floor(arr, target, mid + 1, right)
    else:
        # Search in the left part of the array
        return floor(arr, target, left, mid - 1)

def main():
    test_cases = int(input())  # Getting the number of test cases from the user
    for _ in range(test_cases):
        n = int(input())  # Number of elements in the array
        arr = list(map(int, input().split()))  # Input array elements
        target = int(input())  # The number to find the ceiling and floor for

        # Find the ceiling and floor using recursion and binary search
        ceil = ceiling(arr, target, 0, len(arr) - 1)
        floor_val = floor(arr, target, 0, len(arr) - 1)

        # Print the floor and ceiling values
        print(floor_val)
        print(ceil)

if __name__ == "__main__":
    main()
