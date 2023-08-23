# https://www.codewars.com/kata/58635f1b2489549be50003f1


import math

def quadratic_formula(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant >= 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return [root1, root2]
    else:
        raise ValueError("Equation has complex roots")

roots = quadratic_formula(3, 20, 4) # the roots inputs
print(roots)

