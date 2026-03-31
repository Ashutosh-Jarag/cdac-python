class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

c = Car("Toyota", 120)

# check attributes
print(hasattr(c, "brand"))   # ?
print(hasattr(c, "color"))   # ?

# get safely
print(getattr(c, "color", "No color"))  # ?

# set new attribute
setattr(c, "color", "Red")
print(c.color)   # ?