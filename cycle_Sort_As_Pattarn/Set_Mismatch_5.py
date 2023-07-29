# /**
#  * You have a set of integers s, which originally contains all the numbers from 1 to n.
#  * Unfortunately, due to some error, one of the numbers in s got duplicated to another number in
#  * the set, which results in the repetition of one number and the loss of another number.
#  * You are given an integer array nums representing the data status of this set after the error.
#  * Find the number that occurs twice and the number that is missing and return them in the form of an array.
#  * Author: Saifullah
#  */

def find_set_mismatch(nums):
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

    # Check for the mismatched numbers by comparing each element with its index+1
    duplicated = -1
    missing = -1
    for index in range(n):
        if nums[index] != index + 1:
            duplicated = nums[index]  # Store the duplicated number
            missing = index + 1  # Store the missing number
            break

    return [duplicated, missing]

def main():
    test = int(input("Enter the number of test cases: "))  # Get the number of test cases

    # Execute the Mismatch() method for each test case
    while test > 0:
        n = int(input("Enter the size of the array: "))  # Get the size of the array
        nums = list(map(int, input("Enter the elements of the array separated by space: ").split()))  # Input the elements of the array

        # Call find_set_mismatch() to find the duplicated and missing numbers
        result = find_set_mismatch(nums)

        # Print the duplicated and missing numbers for the current test case
        print("Duplicated number:", result[0])
        print("Missing number:", result[1])

        test -= 1

if __name__ == "__main__":
    main()
