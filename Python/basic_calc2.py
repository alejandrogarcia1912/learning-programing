# Algorithm description: Basic calc v1
'''
Get two numbers
Add, sub, mul, div
Print results
'''

import os
os.system('cls')  # 'clear' en Linux/Mac

# 2. Initialize vars and/or const
print("Please, enter num1: ")
num1 = float(input())

print("Please, enter num2: ")
num2 = float(input())

# 3. Processes
add = num1 + num2
subs = num1 - num2
mult = num1 * num2
div = num1 / num2

# 4. Outputs without f-strings
print("Addition:", add, type(add))
print("Subtraction:", subs, type(subs))
print("Multiplication:", mult, type(mult))
print("Division:", div, type(div))

# 5. Outputs with f-strings
print(f"Addition: {add}")
print(f"Subtraction: {subs}")
print(f"Multiplication: {mult}")
print(f"Division: {div}")