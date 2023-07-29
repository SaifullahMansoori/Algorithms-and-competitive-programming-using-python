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

def recursion_binary_search(arr, left, right, target):
    if left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Target found, return the index
        elif arr[mid] < target:
            # Search in the right part of the array
            return recursion_binary_search(arr, mid + 1, right, target)
        else:
            # Search in the left part of the array
            return recursion_binary_search(arr, left, mid - 1, target)
    return -1  # Target not found, return -1

def main():
    test_cases = int(input())  # Getting the number of test cases from the user
    for _ in range(test_cases):
        n = int(input())  # Number of elements in the array
        arr = list(map(int, input().split()))  # Input array elements
        target = int(input())  # The number to find the index for

        # Call the recursive function and save the result, then print it
        arr = merge_sort(arr)  # Sort the array using Merge Sort
        result = recursion_binary_search(arr, 0, len(arr) - 1, target)
        print(result)  # Print the index of the target

if __name__ == "__main__":
    main()
