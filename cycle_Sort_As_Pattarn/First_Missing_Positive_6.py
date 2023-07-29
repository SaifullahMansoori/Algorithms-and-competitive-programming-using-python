# /**
#  * Given an unsorted integer array nums, return the smallest missing positive integer.
#  * You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.
#  * Author: Saifullah Mansoori
#  */



def first_missing_positive(nums):
    n = len(nums)
    i = 0

    # Perform the Cycle Sort algorithm to place each element at its correct position
    while i < n:
        correct = nums[i] - 1  # The correct position of the current element

        # If the element is not in its correct position, swap it to the correct position
        if 0 < nums[i] <= n and nums[i] != nums[correct]:
            nums[i], nums[correct] = nums[correct], nums[i]
        else:
            # If the element is already in its correct position or out of range, move to the next element
            i += 1

    # Check for the smallest missing positive integer by comparing each element with its index+1
    for index in range(n):
        if nums[index] != index + 1:
            return index + 1  # Return the smallest missing positive integer

    # If all positive integers from 1 to n are present, the smallest missing positive integer is n+1
    return n + 1

def main():
    test = int(input("Enter the number of test cases: "))  # Get the number of test cases

    # Execute the Missing_Positive() method for each test case
    while test > 0:
        n = int(input("Enter the size of the array: "))  # Get the size of the array
        nums = list(map(int, input("Enter the elements of the array separated by space: ").split()))  # Input the elements of the array

        # Call first_missing_positive() to find the smallest missing positive integer
        missing_positive = first_missing_positive(nums)

        # Print the smallest missing positive integer for the current test case
        print("Smallest missing positive integer:", missing_positive)

        test -= 1

if __name__ == "__main__":
    main()
