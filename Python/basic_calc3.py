# Algorithm description: Basic calc v1
'''
Get two numbers
Add, sub, mul, div
Print results
'''
import time
import os
os.system('cls')  # 'clear' en Linux/Mac

# 2. Initialize vars and/or const
print("Hello")
def showGreeting(userName):
    print("Hello " + userName + ", welcome")

# Main
print("Enter your name: ")
userName = input()
showGreeting(userName)

print("Please, enter num1: ")
num1 = float(input())

print("Please, enter num2: ")
num2 = float(input())

# 3. Processes
add = num1 + num2
subs = num1 - num2
mult = num1 * num2
div = num1 / num2

print()

# 4. Outputs without f-strings
start = time.perf_counter()
print("Addition:", add, type(add))
end = time.perf_counter()
start = time.perf_counter()
print("Subtraction:", subs, type(subs))
end = time.perf_counter()
start = time.perf_counter()
print("Multiplication:", mult, type(mult))
end = time.perf_counter()
start = time.perf_counter()
print("Division:", div, type(div))

print()

# 5. Outputs with f-strings
start = time.perf_counter()
print(f"Addition: {add}")
end = time.perf_counter()
start = time.perf_counter()
print(f"Subtraction: {subs}")
end = time.perf_counter()
start = time.perf_counter()
print(f"Multiplication: {mult}")
end = time.perf_counter()
start = time.perf_counter()
print(f"Division: {div}")
end = time.perf_counter()
print()
print(f"Total time: {end - start}")
print()
print("¡have a great day! " + userName)