# Task 2: Multiplication Table with for Loops

userInput = int(input("Enter a number to generate its multiplication table: "))

for i in range(1, 11):
    print(f"{userInput} x {i} = {userInput * i}")

print("\nTask Complete!")