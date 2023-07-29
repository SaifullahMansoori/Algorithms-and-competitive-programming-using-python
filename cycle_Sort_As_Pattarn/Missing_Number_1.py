# /*
#  * Given an array nums containing n distinct numbers in the range [0, n],
#  * return the only number in the range that is missing from the array.
#
#
#  * Author: Saifullah Mansoori
#  */

def find_missing_number(nums):
    n = len(nums)
    i = 0

    # Perform the Cycle Sort algorithm to place each element at its correct position
    while i < n:
        correct = nums[i]

        # If the element is within the array bounds and not in its correct position, swap it
        if 0 <= nums[i] < n and nums[i] != nums[correct]:
            nums[i], nums[correct] = nums[correct], nums[i]
        else:
            # Otherwise, move to the next element
            i += 1

    # Check for the missing number by comparing each element with its index
    for index in range(n):
        if nums[index] != index:
            return index  # Return the missing number

    # If no missing number is found, then n is the missing number
    return n

def main():
    test = int(input("Enter the number of test cases: "))  # Get the number of test cases

    # Execute the Missing() method for each test case
    while test > 0:
        n = int(input("Enter the size of the array: "))  # Get the size of the array
        nums = list(map(int, input("Enter the elements of the array separated by space: ").split()))  # Input the elements of the array

        # Call find_missing_number() to find the missing number
        missing_number = find_missing_number(nums)

        # Print the missing number for the current test case
        print("Missing number:", missing_number)

        test -= 1

if __name__ == "__main__":
    main()
