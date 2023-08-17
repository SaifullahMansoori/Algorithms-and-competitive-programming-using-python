# Define the recursive function to calculate Fibonacci number
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

# Read the number of test cases
num_tests = int(input())

# Process each test case
for _ in range(num_tests):
    n = int(input())  # Read the input number
    ans = fib(n)  # Calculate Fibonacci number using the recursive function
    print(ans)
