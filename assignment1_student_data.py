# PRN      : 1272261997
# Name     : Sujeet Kapoor
# Division : 9
# Branch   : CSE (AI-DS)
# Subject  : Python
# Assignment 1 : Student Data Management Using Python Collections
#                (Dictionary, Tuple and List)


# ---------- TUPLE ----------
# A tuple is fixed. Once made, it cannot be changed.
# The attribute names never change, so a tuple is the right choice here.
student_attributes = ("Roll Number", "Name", "Branch", "Marks")

print("Student attributes stored in a TUPLE:")
print(student_attributes)


# ---------- LIST ----------
# A list is ordered and can be changed.
# We use it to keep the branches offered by the college.
branches = ["CSE (AI-DS)", "CSE", "IT", "ENTC", "Mechanical"]

print("\nBranches stored in a LIST:")
print(branches)


# ---------- DICTIONARY ----------
# A dictionary stores data in pairs : key -> value
# Here the roll number is the key, and the student's details are the value.
students = {
    101: {"Name": "Sujeet Kapoor", "Branch": "CSE (AI-DS)", "Marks": 88},
    102: {"Name": "Riya Sharma",   "Branch": "CSE",         "Marks": 92},
    103: {"Name": "Aman Verma",    "Branch": "IT",          "Marks": 76},
}


def display_students(heading):
    """Prints every student record in a neat table."""
    print("\n" + heading)
    print("-" * 55)
    print("Roll No   Name              Branch          Marks")
    print("-" * 55)
    for roll_number in students:
        details = students[roll_number]
        print(f"{roll_number:<10}{details['Name']:<18}"
              f"{details['Branch']:<16}{details['Marks']}")
    print("-" * 55)


display_students("ORIGINAL STUDENT RECORDS")


# ---------- 1. ADD a new student record ----------
students[104] = {"Name": "Neha Patil", "Branch": "ENTC", "Marks": 81}
print("\n[ADD] Added student with roll number 104.")


# ---------- 2. DELETE an existing student record ----------
del students[102]
print("[DELETE] Removed student with roll number 102.")


# ---------- 3. UPDATE the details of a student ----------
students[103]["Marks"] = 85
students[103]["Branch"] = "CSE"
print("[UPDATE] Updated marks and branch of roll number 103.")


# ---------- 4. DISPLAY the final records ----------
display_students("FINAL STUDENT RECORDS")

print("\nTotal number of students:", len(students))
