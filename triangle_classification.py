"""
Created on Tuesday, Jan 28 2020
Author: Ejona Kocibelli
Project Description: Triangle Classification Implementation
"""


def triangle_classification(side_a, side_b, side_c):
    """Function triangle_classification has three sides of a triangle
     as parameters and classifies the triangle if it is equilateral,
     scalene or isosceles and whether it is right triangle as well"""
    try:
        side_a = float(side_a)
        side_b = float(side_b)
        side_c = float(side_c)
    except ValueError:
        raise ValueError("Each side of triangle has to be a number!")
    else:
        [side_a, side_b, side_c] = sorted([side_a, side_b, side_c])
        if side_a > 0 and side_b > 0 and side_c > 0:
            if (side_a + side_b > side_c) and \
                    (side_b + side_c > side_a) and \
                    (side_a + side_c > side_b):
                if round(((side_a ** 2) + (side_b ** 2)), 2) == round((side_c ** 2), 2):
                    if side_a == side_b or side_b == side_c or side_c == side_a:
                        return 'Right and Isosceles Triangle'
                    else:
                        return 'Right and Scalene Triangle'
                elif side_a == side_b == side_c:
                    return "Equilateral Triangle"
                elif side_a == side_b or side_b == side_c or side_c == side_a:
                    return "Isosceles Triangle"
                else:
                    return "Scalene Triangle"
            else:
                return "This is not a triangle"
        else:
            return 'A triangle cannot have any negative or 0 side'
