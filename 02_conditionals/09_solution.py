import math
# Determine if a year is a leap year, (Leap years are divisible by 4, but not by 100 unless they are also divisible by 400)

year = 2005

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a leap year.")
else: 
    print(f"{year} is not a leap year")