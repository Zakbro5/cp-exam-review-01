from helper_functions import clear_screen
clear_screen()

# ==============
# EXAM 01 REVIEW
# ==============

'''
INTEGRATE YOUR FUNCTION INTO LOOPING LOGIC
------------------------------------------
You are provided with code for the looping logic that you did in practice 2,
as well as a function that will count the number of courses for a student.

Add the logic for option 3:
- Ask for a student name
- Using the returned value of the count_courses function, print out a message
  saying:
    "Student <student name> is taking <number of courses> courses.

'''

# Provided funtion
def count_courses(student_name, students_courses):
    if student_name in students_courses:
        return len(students_courses[student_name])
    else:
        return 0

# provided dictionary
students_courses = {
    "Alice": ["Accounting", "Marketing"],
    "Ben": ["Economics"],
    "Chloe": ["Finance", "Statistics", "Marketing"]
}

while True:
    print("\nMenu:")
    print("1. View all students and courses")
    print("2. Add a course to a student")
    print("3. Show how many courses a student has") # new option
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        for name, courses in students_courses.items():
            print(f"{name}: {', '.join(courses)}")

    elif choice == "2":
        name = input("Enter the student's name: ")
        course = input("Enter the course to add: ")
        if name in students_courses:
            students_courses[name].append(course)
        else:
            students_courses[name] = [course]
        print(f"Course added for {name}.")

    elif choice == "3":
        name = input("Enter the student's name: ")
        total = count_courses(name, students_courses)
        print(f"{name} is enrolled in {total} course(s).")

    elif choice == "4":
        break

    else:
        print("Invalid choice, try again.")