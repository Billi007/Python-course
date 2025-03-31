# Write a function that greets a user. If no name is provided, the function should greet with a default name.

user_input = str(input("Enter your name: "))
def greet(name = "Tanishka"):
   return "Hello " + name + "!"

print(greet(user_input))