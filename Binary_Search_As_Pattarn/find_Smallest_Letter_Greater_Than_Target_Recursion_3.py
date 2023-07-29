 #
 # * This program demonstrates finding the smallest letter greater than the target in a sorted character array using binary search.
 # * The user inputs the number of test cases and an array of characters for each test case.
 # * For each test case, the program finds the smallest letter greater than the target character in the array using binary search.
 # * The program then prints the result for each test case.
 # *
 # * Author: Saifullah Mansoori


def letter_greater_than_target_recursion(letters, target, left, right):
    # Base case: If the left index becomes greater than the right index,
    # we have searched the entire array without finding the desired letter.
    # In this case, we need to handle the wraparound behavior and return the first letter.
    if left > right:
        return letters[left % len(letters)]  # Handle wraparound

    # Calculate the middle index of the current search range
    mid = left + (right - left) // 2

    # If the middle letter is less than or equal to the target,
    # it means the desired letter lies in the right half of the array.
    # So, we recursively search the right half of the array.
    if letters[mid] <= target:
        return letter_greater_than_target_recursion(letters, target, mid + 1, right)
    else:
        # If the middle letter is greater than the target,
        # it means the desired letter lies in the left half of the array.
        # So, we recursively search the left half of the array.
        return letter_greater_than_target_recursion(letters, target, left, mid - 1)

def helper():
    # Read the number of elements in the array from the user
    n = int(input())

    # Create an array to store the letters
    letters = []

    # Read the letters from the user and store them in the array
    for _ in range(n):
        letters.append(input()[0])

    # Read the target letter from the user
    target = input()[0]

    # Call the recursive function to find the smallest letter greater than the target
    result = letter_greater_than_target_recursion(letters, target, 0, len(letters) - 1)

    # Print the result - the smallest letter greater than the target
    print(result)

def main():
    test_cases = int(input())  # Read the number of test cases from the user

    # Process each test case
    for _ in range(test_cases):
        # Call the helper method for each test case
        helper()

if __name__ == "__main__":
    main()
