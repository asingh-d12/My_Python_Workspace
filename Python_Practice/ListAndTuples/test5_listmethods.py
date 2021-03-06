current_choice = "-"
computer_choice = []
computer_parts = ["computer",
                  "mouse",
                  "keyboard",
                  "Monitor",
                  "mouse mat",
                  "HDMI Cable"
                  ]


# I am creating a separate function, that will remove an item from the list
def remove_the_item(an_item):
    if an_item in computer_choice:
        computer_choice.remove(an_item)


def print_list():
    print("*" * 50)
    print("Your List now contains = {}".format(computer_choice))
    print("*" * 50)


while current_choice != 0:
    if current_choice in list(range(1, len(computer_parts) + 1)):
        print("Adding {}".format(computer_parts[current_choice - 1]))
        # Checking if chosen part is already in the list
        if computer_parts[current_choice - 1] in computer_choice:
            ch = input("Computer part is already in the list, Do you want to add again (y/n) : ")
            if (not ch) or (ch.lower() not in 'yn'):
                print("Incorrect choice, Discarding the duplicate part!!")
                current_choice = '-'
                print_list()
                continue
            elif ch.lower() == 'n':
                print("Discarding the duplicate part {}".format(computer_parts[current_choice - 1]))
                current_choice = '-'
                print_list()
                continue
        # APPENDING DATA IN A LIST WHICH STARTED EMPTY
        computer_choice.append(computer_parts[current_choice - 1])
        print_list()
    else:
        print("Add options from the list below : ")
        for x in range(len(computer_parts)):
            print("{} -> {}".format(x + 1, computer_parts[x]))
        print("0 -> Exit/Finish!!")
    current_choice = int(input("Enter your choice : "))


print("Final Computer Choice = {}".format(computer_choice))

print("*" * 100)
# REMOVING ITEM FROM THE LIST
print("Removing Item from the list")
remove_the_item("computer")
print_list()
remove_the_item("mouse")
print_list()

