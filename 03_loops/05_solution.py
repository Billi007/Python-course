# Given a string, find the first non-repeating character.

str = "teeteradscba"

for char in str:
    if str.count(char) == 1:
        print("non-repeating character:", char)
        break
        