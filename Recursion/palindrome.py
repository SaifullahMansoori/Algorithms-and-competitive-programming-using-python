# Define the recursive function to reverse and check for palindrome
def Reverse(n):
    global sum
    if n == 0:
        return
    
    rem = n % 10
    sum = sum * 10 + rem
    Reverse(n // 10)

# Read the number of test cases
num_tests = int(input())

# Process each test case
for _ in range(num_tests):
    n = int(input())  # Read the input number
    sum = 0  # Initialize the sum for the current test case
    Reverse(n)  # Calculate reverse using the recursive function
    print(sum == n)  # Print whether the number is a palindrome or not

# Note: In Python, we use '//' for integer division
