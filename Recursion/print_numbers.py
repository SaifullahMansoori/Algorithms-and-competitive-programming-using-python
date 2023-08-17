# Define the recursive function to print numbers from N to 1
def print_numbers(n):
    if n == 0:
        return
    print(n)
    print_numbers(n - 1)

# Read the number of test cases
num_tests = int(input())

# Process each test case
for _ in range(num_tests):
    n = int(input())  # Read the input number
    print_numbers(n)  # Print numbers using the recursive function
