from helper_functions import clear_screen
clear_screen()

# ==============
# EXAM 01 REVIEW
# ==============

'''
WRITING A FUNCTION
------------------
Write a function that will accept a dictionary (with student names as keys and
lists of their courses as the values) and a student name string as arguments.

The function should return the number of courses that student is taking. If 
the student name can't be found in the dictionary, it should just return 0.

After writing your function, try calling it a couple of times using the 
provided dictionary as one of the arguments.
'''

example_data = {
    "Alice": ["Accounting", "Marketing"],
    "Ben": ["Economics"],
    "Chloe": ["Finance", "Statistics", "Marketing"]
}

