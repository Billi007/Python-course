# Movie Ticket pricing
# Movie Tickets are priced based on age: $12 for adults (18 and over), $8 for children,
# Everyone gets a $2 discount on Wednesday.

age = int(input("Provide your age: "))
day = "wednesday"
price = 12 if age >= 18 else 8

if day == "tuesday":
    price = price - 2

print("Ticket price is $",price)