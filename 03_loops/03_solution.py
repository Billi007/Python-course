# print the multiplication table for given number upto 10, but skip the 5th iteration.

num = 5

for i in range(1, 11):
  if i == 5:
    continue
  print(num, "*", i, "=", num *i) 
    