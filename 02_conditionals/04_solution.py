# Determine if a fruit is ripe, overripe, or unripe based on its color (e.g: Green - unripe, Yellow - ripe, brown - Overripe)

fruit = "apple"
fruit_color = "brown"

if fruit == "apple":
  if fruit_color == "green":
    print("Unripe")

  elif fruit_color == "brown":
    print("Overripe")

  elif fruit_color == "yellow":
    print("Ripe")
  else:
    print("No fruit provided")