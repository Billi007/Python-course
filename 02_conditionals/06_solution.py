# Choose a mode of transporting based on the distance (e.g., <3 Km: Walk, 3-15 Km: Bike, >15 Km: Car)

distance = 5
if distance < 3:
    print("Walk")
elif distance <= 15:
    print("Bike")
elif distance > 15:
    print("Car")
else: 
    print("jaise man hai waise jao...")