from helper_functions import clear_screen
clear_screen()

# ==============
# EXAM 01 REVIEW
# ==============

'''
STORING LISTS INSIDE OF A DICTIONARY
'''

# 1. CREATE AN EMPTY DICTIONARY

dictionary = {}

# 2. USE LISTS AS VALUES
# Add three students (student name being the key), each with a list of courses
# they are taking as the value.

dictionary["James"] = ["math", "science", "biology"]
dictionary["Beth"] = ["basketball", "science", "biology"]
dictionary["Amy"] = ["math", "biology", "basketball"]

# 3. APPEND A COURSE TO ONE OF THE STUDENT'S LISTS
# Choose one of the students you created, and add a new course at the end of
# their list.

dictionary["Beth"].append("math")

# 4. ACCESS A LIST INSIDE A DICTIONARY
# Access the 2nd course of one of the students you entered.

second_course = dictionary["Amy"][1]
print(second_course)

print(dictionary)
