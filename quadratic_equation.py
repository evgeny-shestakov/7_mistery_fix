from math import sqrt

def get_roots(a_coefficient, b_coefficient, c_coefficient):
    discriminant = b_coefficient ** 2 - 4 * a_coefficient * c_coefficient
    if discriminant < 0:
        return None, None
    root1 = (-b_coefficient - sqrt(discriminant)) / (2 * a_coefficient)
    root2 = (-b_coefficient + sqrt(discriminant)) / (2 * a_coefficient)
    if discriminant == 0:
        return root1, None
    else:
        return root1, root2
