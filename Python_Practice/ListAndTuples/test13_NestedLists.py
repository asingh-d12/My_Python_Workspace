# Let's start with 2 lists
odd = [1, 3, 5, 7, 9]
even = [2, 4, 6, 8]

# Adding/Concatenating these 2 lists
numbers = even + odd
print(numbers)

print("*" * 50)
# List of Lists
numbers = [even, odd]
# This will be a nested list - basically a list inside a list
print(numbers)

# Nested loop to print list of lists
for a_list in numbers:
    print(a_list)
    for a_num in a_list:
        print(a_num)

print("*" * 50)
# Another Nested List
menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]
# Let's go through this menu list, and print meals(items in list) which do not have spam
for a_meal in menu:
    if "spam" not in a_meal:
        print(a_meal)
    else:
        print("{} spam in meal {}".format(a_meal.count("spam"), a_meal))
