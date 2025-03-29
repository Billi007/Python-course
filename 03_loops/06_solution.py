# Compute the factorial of a number using while loop.

num = 5
factorial = 1

while num > 0:
    factorial *= num  #(factorial = factorial * num)
    num -= 1         #(num = num - 1)

print("Factorial of", num , "is", factorial)