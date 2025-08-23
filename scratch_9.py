student={'Vedant':80,'Alice':70,'Shauraya':82}

a=str(input("Enter the student's name : ")).capitalize()
if a not in student:
    print("Student not found")
else:
    print(f"{a}'s marks: {student.get(a)}")