
 # * This program demonstrates finding the smallest letter greater than the target in a sorted character array using binary search.
 # * The user inputs the number of test cases and an array of characters for each test case.
 # * For each test case, the program finds the smallest letter greater than the target character in the array using binary search.
 # * The program then prints the result for each test case.
 # *
 # * Author: Saifullah Mansoori
def letter_greater_than_target(letters, target):
    left = 0
    right = len(letters) - 1
    while left <= right:
        mid = left + (right - left) // 2  # Calculate the middle index
        if letters[mid] < target:
            left = mid + 1  # Search in the right part of the array
        else:
            right = mid - 1  # Search in the left part of the array
    print(letters[left % len(letters)])  # Print the smallest letter greater than the target

def helper():
    n = int(input())  # Number of elements in the character array
    letters = [input()[0] for _ in range(n)]  # Input array elements as characters
    target = input()[0]  # The character to find the smallest letter greater than

    # Call the function to find the smallest letter greater than the target and print the result
    letter_greater_than_target(letters, target)

def main():
    test_cases = int(input())  # Getting the number of test cases from the user

    # Process each test case
    for _ in range(test_cases):
        # Call the helper function for each test case
        helper()

if __name__ == "__main__":
    main()
