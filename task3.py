# Task 3: Find the Factorial

inputNum = int(input("Enter a number to find its factorial: "))

for i in range(1, inputNum + 1):
    if i == 1:
        factorial = 1
    else:
        factorial *= i

print(f"The factorial of {inputNum} is {factorial}")

print("\nTask Complete!")