# PRN      : 1272261997
# Name     : Sujeet Kapoor
# Division : 9
# Branch   : CSE (AI-DS)
# Subject  : Python
# Assignment 5 : PAN Number Validation Using Regular Expression


import re


# The pattern that a valid PAN must follow:
#   ^        -> start of the string
#   [A-Z]{5} -> exactly 5 uppercase letters
#   [0-9]{4} -> exactly 4 digits
#   [A-Z]{1} -> exactly 1 uppercase letter
#   $        -> end of the string
pan_pattern = "^[A-Z]{5}[0-9]{4}[A-Z]{1}$"


def validate_pan(pan_number):
    """Returns True if the PAN number matches the required pattern."""
    if re.fullmatch(pan_pattern, pan_number):
        return True
    else:
        return False


# ---------- Main program ----------

print("PAN Number Validation")
print("---------------------")
print("Format required : AAAAA9999A")

pan_number = input("\nEnter your PAN number : ")

if validate_pan(pan_number):
    print("Valid PAN Number")
else:
    print("Invalid PAN Number")
