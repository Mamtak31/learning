import math
x = float(input("Enter a number x: "))
y = float(input("Enter a number y: "))
result_power = x ** y
result_add = x + y
result_sub = x - y
result_mul = x * y
result_div = x / y
result_mod = x % y
print(f"x + y = {result_add}")
print(f"x - y = {result_sub}")
print(f"x * y = {result_mul}")
print(f"x / y = {result_div}")      
print(f"x % y = {result_mod}")
print(f"{x} raised to the power {y} is: {result_power}")
result_log = math.log2(x)
print(f"The log base 2 of {x} is: {result_log}")