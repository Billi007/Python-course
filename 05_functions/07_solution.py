# Write a function that takes variable number of arguments and returns the sum.

def sum_args(*args):
   return sum(args)

print(sum_args(1,2,3))
print(sum_args(1,2,3,4,5,6))
print(sum_args(1,2,3,4,5,6,7,8,9,10))