# /*
#  * Given an integer array nums of length n where all the integers of nums are in the range [1, n]
#  * and each integer appears once or twice, return an array of all the integers that appear twice.
#  * You must write an algorithm that runs in O(n) time and uses only constant extra space.
#  * Author: Saifullah Mansoori
#  */



def find_duplicates(nums):
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

    duplicates = []
    # Check for the duplicate numbers by comparing each element with its index+1
    for index in range(n):
        if nums[index] != index + 1:
            duplicates.append(nums[index])  # Store the duplicate number

    return duplicates

def main():
    test = int(input())  # Get the number of test cases

    # Execute the Duplicates() method for each test case
    while test > 0:
        n = int(input())  # Get the size of the array
        nums = list(map(int, input().split()))  # Input the elements of the array

        # Call find_duplicates() to find the duplicate numbers
        duplicates = find_duplicates(nums)

        # Print the duplicate numbers for the current test case
        print(*duplicates)

        test -= 1

if __name__ == "__main__":
    main()
