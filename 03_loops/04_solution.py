# Reverse string using a loop.

str = "Hello"
reversed_str = ""

for char in str:
    reversed_str = char + reversed_str # olleH
    reversed_str = reversed_str + char # Hello

print(reversed_str)