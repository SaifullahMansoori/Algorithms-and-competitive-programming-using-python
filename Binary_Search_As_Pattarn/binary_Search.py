
#  * This program demonstrates binary search on a sorted array.
#  * The user inputs the number of test cases and an array for each test case.
#  * For each test case, the program sorts the array using an optimized sorting algorithm,
#  * and then performs binary search to find the index of the target element in the array.
#  * If the target element is found, it prints its index; otherwise, it prints -1.
#  *
#  * The binary search algorithm assumes that the input array is sorted in ascending order.
#  * If the array is not sorted, the binary search will not work correctly.
#  *
#  * The optimized sorting algorithm used here is the "Merge Sort" algorithm.
#  * Merge Sort is a divide-and-conquer algorithm with a time complexity of O(n log n).
#  * It is more efficient than the previous sorting algorithm (bubble sort) used in the original code.
#  *
#  * Author: Saifullah Mansoori


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])

    return merge(left_arr, right_arr)

def merge(left_arr, right_arr):
    merged_arr = []
    left_index, right_index = 0, 0

    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] <= right_arr[right_index]:
            merged_arr.append(left_arr[left_index])
            left_index += 1
        else:
            merged_arr.append(right_arr[right_index])
            right_index += 1

    # Append the remaining elements, if any
    merged_arr.extend(left_arr[left_index:])
    merged_arr.extend(right_arr[right_index:])
    return merged_arr

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Target found, return the index
        elif arr[mid] < target:
            left = mid + 1  # Search in the right part of the array
        else:
            right = mid - 1  # Search in the left part of the array

    return -1  # Target not found, return -1

def main():
    test_cases = int(input())  # Getting the number of test cases from the user
    for _ in range(test_cases):
        n = int(input())  # Number of elements in the array
        arr = list(map(int, input().split()))  # Input array elements
        target = int(input())  # The number to find the index for

        # Sort the array using Merge Sort
        arr = merge_sort(arr)

        # Find the index of the target using binary search
        index = binary_search(arr, target)

        # Print the index of the target
        print(index)

if __name__ == "__main__":
    main()
