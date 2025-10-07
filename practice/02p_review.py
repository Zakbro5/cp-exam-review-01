from helper_functions import clear_screen
clear_screen()

# ==============
# EXAM 01 REVIEW
# ==============

'''
INTERACTING WITH DICTIONARY/LIST DURING A LOOP
----------------------------------------------

Use the provided dictionary below. Create a program that will repeatedly print
out:

Menu:
1. View all students and courses
2. Add a course to a student
3. Exit
Choose an option (1-3): 

For option 1, print out each student's name, with each of their courses indented
out on their own lines, like this:

    Bob
        Marketing
        Finance

For option 2, ask for a student name and a course to add to their course list.
If their name already exists in the dictionary, just add the course to the end
of their list. If the name isn't in the dictionary yet, add it along with the
course name in their new list.

For option 3, print a nice exit message and end the code.

For anything else, print "Invalid option"

Repeatedly ask for an option until the user enters 3 to exit.

'''

students_courses = {
    "Alice": ["Accounting", "Marketing"],
    "Ben": ["Economics"],
    "Chloe": ["Finance", "Statistics", "Marketing"]
}
option = 0
while option != "3":
    option = input("Menu:\n1. View all students and courses\n2. Add a course to a student\n3. Exit\nChoose an option (1-3): ")
    if option == "1":
        # print(students_courses)
        for key_student, value_courses_list in students_courses.items():
            print(key_student)
            for course_string in value_courses_list:
                print(f"\t{course_string}")
    elif option == "2":
        student_name = input("Enter a student's name: ")
        new_course = input("Enter a course to add to their course list: ")
        if student_name in students_courses:
            students_courses[student_name].append(new_course)
        else:
            students_courses[student_name] = new_course
    else:
        print("Invalid option")

print("Thanks for adding to the list of courses!")

