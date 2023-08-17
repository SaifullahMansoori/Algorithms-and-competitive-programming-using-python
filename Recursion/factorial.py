# Define the recursive function to calculate factorial
def fact(n):
    # Base case: factorial of 1 is 1
    if n == 1:
        return 1
    # Recursive case: calculate factorial using recursive call
    return n * fact(n - 1)

# Read the number of test cases
num_tests = int(input())

# Process each test case
for _ in range(num_tests):
    n = int(input())  # Read the input number
    result = fact(n)  # Calculate factorial using the recursive function
    print(result)  # Print the result
