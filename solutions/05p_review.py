from helper_functions import clear_screen
clear_screen()

# ==============
# EXAM 01 REVIEW
# ==============

'''
INTEGRATE YOUR FUNCTION INTO LOOPING LOGIC
------------------------------------------
Given the dictionary below (salesperson name, followed by list of their sales
amounts), write a function that accepts a dictionary and name as arguments.

The function should return the total number of sales for that person if the name
exists in the dictionary. If the name doesn't exist in the dictionary, then
return None.

Afterwards, ask the user for a name, and then use that name in the function to
see how many total sales they have. Print out the returned value in a nice
message. If they don't have any sales, print out "<name> doesn't have any sales"
'''

sales = {
    "alice": [120, 135, 200, 150, 180],
    "ben": [90, 100, 95, 130, 80],
    "chloe": [200, 180, 190, 210, 250]
}

def calculate_total_sales(sales_dict, name):
    """Return the total sales for the given salesperson name."""
    if name in sales_dict:
        total = 0
        for sale in sales_dict[name]:
            total += sale
        return total
    else:
        return None

name = input("Enter a salesperson's name to see their total sales: ").lower()

total_sales = calculate_total_sales(sales, name)
if total_sales:
    print(f"{name} has total sales of ${total_sales:.2f}")
else:
    print(f"{name} doesn't have any sales.")