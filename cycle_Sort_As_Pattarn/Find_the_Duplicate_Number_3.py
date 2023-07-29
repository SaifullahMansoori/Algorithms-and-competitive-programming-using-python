# /*
#  * Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
#  * There is only one repeated number in nums, return this repeated number.
#  * You must solve the problem without modifying the array nums and uses only constant extra space.
#
#
#  * Author: Saifullah Mansoori
#  */

def find_duplicate(nums):
    slow = nums[0]
    fast = nums[0]

    # Phase 1: Finding the intersection point of the two pointers
    while True:
        slow = nums[slow]  # Move one step
        fast = nums[nums[fast]]  # Move two steps

        if slow == fast:
            break

    # Phase 2: Finding the start of the cycle (duplicate number)
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow

def main():
    test = int(input("Enter the number of test cases: "))  # Get the number of test cases

    # Execute the Duplicate() method for each test case
    while test > 0:
        n = int(input("Enter the size of the array: "))  # Get the size of the array
        nums = list(map(int, input("Enter the elements of the array separated by space: ").split()))  # Input the elements of the array

        # Call find_duplicate() to find the duplicate number
        duplicate = find_duplicate(nums)

        # Print the duplicate number for the current test case
        print("Duplicate number:", duplicate)

        test -= 1

if __name__ == "__main__":
    main()
