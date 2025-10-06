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

while True:
    print("\nMenu:")
    print("1. View all students and courses")
    print("2. Add a course to a student")
    print("3. Exit")

    choice = input("Choose an option (1-3): ")

    if choice == "1":
        for name, courses in students_courses.items():
            print(f"{name}:")
            for course in courses:
                print(f"\t{course}")

    elif choice == "2":
        name = input("Enter the student's name: ")
        course = input("Enter the course to add: ")
        if name in students_courses:
            students_courses[name].append(course)
        else:
            students_courses[name] = [course]
        print(f"Course added for {name}.")

    elif choice == "3":
        break

    else:
        print("Invalid choice, try again.")