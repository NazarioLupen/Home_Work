# will_you_make_it

def zero_fuel(distance, mpg, fuel_left):
    if (distance/mpg) <= fuel_left:
        return True
    return False
print(zero_fuel (50, 25, 2))
# zero_fuel (100, 50, 1)
