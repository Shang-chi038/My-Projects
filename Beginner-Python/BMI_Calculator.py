def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \ # If you use '/' in Python code and end
    # a line with it, it will tell Python to continue the line of code in the 
    # next line of code.
    weight < 20 or weight > 200:
        return None

    return weight / height ** 2


print(bmi(352.5, 1.65))
