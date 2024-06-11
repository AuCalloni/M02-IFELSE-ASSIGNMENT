# Austin Calloni
# M02 if..else and while.py
# Small program to accept student names and GPA, and determine if student is on Dean's list or Honor ROll


def student_status(GPA):
    if float(GPA) >= 3.5:
        return 0
    elif float(GPA) >= 3.25:
        return 1
    return 2

while True:
    last_name = input("Enter the student's last name: ")
    # Convert to upper so case sensitivity is not relevant
    if last_name.upper() == "ZZZ":
        break
    first_name = input("Enter the student's first name: ")
    GPA = float(input("Enter the student's GPA: "))
    student_string = {0: " has made the Dean's List", 1: " has made the Honor Roll", 2: " is on neither list"}
    GPA_Key = student_status(GPA)
    print(first_name + " " + last_name + student_string[GPA_Key])


