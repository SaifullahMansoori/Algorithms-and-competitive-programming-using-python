# Define the recursive function to calculate the sum of N natural numbers
def sum_natural_numbers(n):
    if n < 1:
        return 0
    return n + sum_natural_numbers(n - 1)

# Read the number of test cases
num_tests = int(input())

# Process each test case
for _ in range(num_tests):
    n = int(input())  # Read the input number
    result = sum_natural_numbers(n)  # Calculate sum using the recursive function
    print(result)  # Print the sum
