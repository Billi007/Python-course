# Recommand a type of pet food based on the pet's species and age.(e.g., Dog: <2 years - Puppy food, 2-5 years - Adult dog food, Cat: >5 years - Senior cat food)

pet = "Cat"
age = 1

if pet:
    if age <2:
        food = pet + " baby Food"
    elif age >= 2: 
        food = "Senior " + pet + " food"
    print("Food:",food)