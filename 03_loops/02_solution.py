# Calculate the sum of even numbers up to a given number n.

n = 5
sum_even_num = 0

for i in range(1, n+1):
    if i % 2 == 0:
        sum_even_num += 1

print("Sum of even numbers of", n, "is", sum_even_num)
1
2
3
4
5
6
7
8
9
10