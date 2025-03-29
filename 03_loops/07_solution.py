# Keep asking the user for input until they enter a number bewtween 1 and 10.

while True:
   input_value = int(input("Please enter a number b/w 1 and 10: "))
   if 1 <= input_value <= 10:
      print("Thank you!")
      break
   else: 
      print("Invalid input, Try again!")