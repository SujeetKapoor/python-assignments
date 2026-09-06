# PRN      : 1272261997
# Name     : Sujeet Kapoor
# Division : 9
# Branch   : CSE (AI-DS)
# Subject  : Python
# Assignment 3 : Check whether a triangle is right-angled (using function)


def is_right_angled(a, b, c):
    """Returns True if sides a, b, c form a right-angled triangle."""

    # Sort the sides so the longest one is last (that is the hypotenuse)
    sides = sorted([a, b, c])
    side1 = sides[0]
    side2 = sides[1]
    hypotenuse = sides[2]

    # Pythagoras theorem : side1^2 + side2^2 == hypotenuse^2
    if side1**2 + side2**2 == hypotenuse**2:
        return True
    else:
        return False


def is_valid_triangle(a, b, c):
    """Returns True if the three sides can actually form a triangle."""

    if a <= 0 or b <= 0 or c <= 0:
        return False

    # Sum of any two sides must be greater than the third side
    if a + b > c and b + c > a and a + c > b:
        return True
    else:
        return False


# ---------- Main program ----------

print("Right-Angled Triangle Checker")
print("-----------------------------")

a = float(input("Enter the length of side 1 : "))
b = float(input("Enter the length of side 2 : "))
c = float(input("Enter the length of side 3 : "))

if not is_valid_triangle(a, b, c):
    print("\nThese sides cannot form a triangle.")
elif is_right_angled(a, b, c):
    print("\nYes, this is a right-angled triangle.")
else:
    print("\nNo, this is not a right-angled triangle.")
