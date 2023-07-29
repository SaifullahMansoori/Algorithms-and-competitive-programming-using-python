# /*
#  * Given an array nums of n integers where nums[i] is in the range [1, n],
#  * return an array of all the integers in the range [1, n] that do not appear in nums.
#
#
#  * Author: Saifullah Mansoori
#  */

def find_disappeared_numbers(nums):
    n = len(nums)
    i = 0

    # Perform the Cycle Sort algorithm to place each element at its correct position
    while i < n:
        correct = nums[i] - 1  # The correct position of the current element

        # If the element is not in its correct position, swap it to the correct position
        if nums[i] != nums[correct]:
            nums[i], nums[correct] = nums[correct], nums[i]
        else:
            # If the element is already in its correct position, move to the next element
            i += 1

    missing_numbers = []
    # Check for the missing numbers by comparing each element with its index+1
    for index in range(n):
        if nums[index] != index + 1:
            missing_numbers.append(index + 1)  # Store the missing number

    return missing_numbers

def main():
    test = int(input())  # Get the number of test cases

    # Execute the Disappeared() method for each test case
    while test > 0:
        n = int(input())  # Get the size of the array
        nums = list(map(int, input().split()))  # Input the elements of the array

        # Call find_disappeared_numbers() to find the missing numbers
        missing_numbers = find_disappeared_numbers(nums)

        # Print the missing numbers for the current test case
        print(*missing_numbers)

        test -= 1

if __name__ == "__main__":
    main()
