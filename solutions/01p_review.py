from helper_functions import clear_screen
clear_screen()

# ==============
# EXAM 01 REVIEW
# ==============

'''
STORING LISTS INSIDE OF A DICTIONARY
'''

# 1. CREATE AN EMPTY DICTIONARY
students_courses = {}

# 2. USE LISTS AS VALUES
# Add three students (student name being the key), each with a list of courses
# they are taking as the value.
students_courses["Alice"] = ["Accounting", "Marketing"]
students_courses["Ben"] = ["Economics"]
students_courses["Chloe"] = ["Finance", "Statistics", "Marketing"]

# 3. APPEND A COURSE TO ONE OF THE STUDENT'S LISTS
# Choose one of the students you created, and add a new course at the end of
# their list.
students_courses["Ben"].append("Biology")

# 4. ACCESS A LIST INSIDE A DICTIONARY
# Access the 2nd course of one of the students you entered.
print(students_courses["Chloe"][1])