# /**
#  * This program demonstrates the Cycle Sort algorithm to sort an array.
#  * Cycle Sort is an in-place and unstable sorting algorithm known for its
#  * optimal number of writes to the array, making it useful for memory-limited scenarios.
#  * It works by arranging elements in their correct positions one at a time.
#  *
#  *
#  * Author: Saifullah Mansoori
#  */
def cycle_sort(nums):
    n = len(nums)
    i = 0

    # Perform the Cycle Sort algorithm
    while i < n:
        correct = nums[i] - 1  # The correct position of the current element

        # If the element is not in its correct position, swap it to the correct position
        if nums[i] != nums[correct]:
            nums[i], nums[correct] = nums[correct], nums[i]
        else:
            # If the element is already in its correct position, move to the next element
            i += 1

    return nums

def main():
    test = int(input())  # Get the number of test cases

    # Execute the Cycle() method for each test case
    while test > 0:
        n = int(input())  # Get the size of the array
        nums = list(map(int, input().split()))  # Input the elements of the array

        # Call cycle_sort() to sort the array
        sorted_nums = cycle_sort(nums)

        # Print the sorted array for the current test case
        print(*sorted_nums)

        test -= 1

if __name__ == "__main__":
    main()
