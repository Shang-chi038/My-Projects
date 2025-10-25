# 1 American mile = 1609.344 metres
# 1 American gallon = 3.785411784 litres

def litres_100km_to_miles_gallon(litres):
    miles = (1e5) * (1 / 1609.344) # how many miles does 100km make? Here, we are converting 100km to miles. (1e5 == 10^5)
    gallons = litres * (1 / 3.785411784) # how many gallons can the provided litres make?
    miles_gallon = miles / gallons
    return miles_gallon

def miles_gallon_to_litres_100km(miles):
    _100kms = 1609.344 * miles / (1e5) # how many humdred kms are in the miles provided?
    litres = 1 * 3.785411784 # because litre per 100km, which can also be read as one litre per 100km
    litres_100km = litres / _100kms
    return litres_100km

print(litres_100km_to_miles_gallon(3.9))
print(litres_100km_to_miles_gallon(7.5))
print(litres_100km_to_miles_gallon(10.))
print(miles_gallon_to_litres_100km(60.3))
print(miles_gallon_to_litres_100km(31.4))
print(miles_gallon_to_litres_100km(23.5))

