# Define the recursive function to count occurrences of a target digit
def numberCount(n, target, c):
    if n == 0:
        return c
    
    rem = n % 10
    if rem == target:
        return numberCount(n // 10, target, c + 1)
    return numberCount(n // 10, target, c)

# Read the number of test cases
num_tests = int(input())

# Process each test case
for _ in range(num_tests):
    n, target = map(int, input().split())  # Read the input number and target digit
    result = numberCount(n, target, 0)  # Calculate occurrences using the recursive function
    print("result", result)
