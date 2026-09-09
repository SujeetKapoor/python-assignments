# python-assignments

Python lab assignments (LCA1).

**Name:** Sujeet Kapoor
**PRN:** 1272261997
**Division:** 9
**Branch:** CSE (AI-DS)
**Subject:** Python

All programs are written in plain Python with no external libraries, so they run
on any machine with Python 3 installed.

---

## How to run

```bash
python assignment1_student_data.py
```

Replace the filename to run any of the other assignments.

---

## Assignment 1 — Student Data Management Using Python Collections

Stores student information using a **dictionary, tuple and list**, then performs
add, delete and update operations on the dictionary and displays the final records.

- **Tuple** holds the attribute names, since those never change.
- **List** holds the branches offered.
- **Dictionary** holds the students, with the roll number as the key.

**Output**

```
Student attributes stored in a TUPLE:
('Roll Number', 'Name', 'Branch', 'Marks')

Branches stored in a LIST:
['CSE (AI-DS)', 'CSE', 'IT', 'ENTC', 'Mechanical']

ORIGINAL STUDENT RECORDS
-------------------------------------------------------
Roll No   Name              Branch          Marks
-------------------------------------------------------
101       Sujeet Kapoor     CSE (AI-DS)     88
102       Riya Sharma       CSE             92
103       Aman Verma        IT              76
-------------------------------------------------------

[ADD] Added student with roll number 104.
[DELETE] Removed student with roll number 102.
[UPDATE] Updated marks and branch of roll number 103.

FINAL STUDENT RECORDS
-------------------------------------------------------
Roll No   Name              Branch          Marks
-------------------------------------------------------
101       Sujeet Kapoor     CSE (AI-DS)     88
103       Aman Verma        CSE             85
104       Neha Patil        ENTC            81
-------------------------------------------------------

Total number of students: 3
```

---

## Assignment 2 — Largest of Three Numbers

Accepts three numbers and prints the largest using `if / elif / else`.

**Output**

```
Enter the first number  : 5
Enter the second number : 92
Enter the third number  : 17

The largest number is: 92.0
```

---

## Assignment 3 — Right-Angled Triangle Check

Accepts the three sides of a triangle and uses a **function** to check whether it
is right-angled, based on Pythagoras' theorem. A second function first checks
that the three sides can form a valid triangle at all.

**Output**

```
Right-Angled Triangle Checker
-----------------------------
Enter the length of side 1 : 3
Enter the length of side 2 : 4
Enter the length of side 3 : 5

Yes, this is a right-angled triangle.
```

---

## Assignment 4 — Matrix Addition

Creates two matrices as arrays (a list of lists, where each inner list is one row)
and adds them element by element using nested loops.

**Output**

```
Matrix Addition
---------------
Enter the number of rows    : 2
Enter the number of columns : 2

Enter the elements of the FIRST matrix, row by row:
Element [1][1] : 1
Element [1][2] : 2
Element [2][1] : 3
Element [2][2] : 4

Enter the elements of the SECOND matrix, row by row:
Element [1][1] : 5
Element [1][2] : 6
Element [2][1] : 7
Element [2][2] : 8

First Matrix:
    1    2
    3    4

Second Matrix:
    5    6
    7    8

Sum of the two matrices:
    6    8
   10   12
```

---

## Assignment 5 — PAN Number Validation Using Regular Expression

Validates a PAN number against the format `AAAAA9999A` using the regular
expression `^[A-Z]{5}[0-9]{4}[A-Z]{1}$`.

| Input | Result |
|---|---|
| `ABCDE1234F` | Valid PAN Number |
| `ABCD@1234F` | Invalid PAN Number |
| `ABCDE12345` | Invalid PAN Number |

**Output**

```
PAN Number Validation
---------------------
Format required : AAAAA9999A

Enter your PAN number : ABCDE1234F
Valid PAN Number
```
