aCoefficient = float(input("Write first coefficient: "))
bCoefficient = float(input("Write second coefficient: "))
cCoefficient = float(input("Write third coefficient: "))

discriminant = bCoefficient ** 2 - 4 * aCoefficient * cCoefficient

if discriminant > 0:
    firstX = (-bCoefficient + (discriminant ** 0.5))/2/aCoefficient
    secondX = (-bCoefficient - (discriminant ** 0.5))/2/aCoefficient
    print("First X is: ", firstX, " Second X is: ", secondX)
elif discriminant == 0:
    X = (-bCoefficient)/2/aCoefficient
    print("X is: ", X)
else:
    print("no X with these coefficients")
