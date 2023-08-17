# Define the recursive function to calculate the product of digits
def Product(n):
    # Base case: If n has only one digit
    if n % 10 == n:
        return n
    # Recursive case: Calculate the product of the last digit and result of recursive call
    return (n % 10) * Product(n // 10)

# Read the number of test cases
num_tests = int(input())

# Process each test case
for _ in range(num_tests):
    n = int(input())  # Read the input number
    result = Product(n)  # Calculate product of digits using the recursive function
    print(result)  # Print the result

# Note: In Python, we use '//' for integer division and '%' for the remainder operation
