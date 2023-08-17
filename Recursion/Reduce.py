# Define the recursive function to count steps to reduce a number to zero
def Reduce(number, step):
    if number == 0:
        return step
    
    if number % 2 == 0:
        return Reduce(number // 2, step + 1)
    else:
        return Reduce(number - 1, step + 1)

# Read the number of test cases
num_tests = int(input())

# Process each test case
for _ in range(num_tests):
    n = int(input())  # Read the input number
    count = Reduce(n, 0)  # Calculate steps using the recursive function
    print(count)
