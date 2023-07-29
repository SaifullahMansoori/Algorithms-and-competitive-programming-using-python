def find_peak(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] > arr[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return arr[left]

def main():
    test_cases = int(input())  # Getting the number of test cases from the user

    # Process each test case
    for _ in range(test_cases):
        # Call the helper function for each test case
        helper()

def helper():
    n = int(input())  # Number of elements in the array
    arr = [int(x) for x in input().split()]  # Input array elements

    peak_element = find_peak(arr)  # Find the peak element using binary search
    print(peak_element)

if __name__ == "__main__":
    main()
