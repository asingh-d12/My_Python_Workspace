# So, now we are going to create an adventure game using dictionary
# PFB the locations in the game--- represented by a dictionary
locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

exits = [{"Q": 0},
         {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         {"N": 5, "Q": 0},
         {"W": 1, "Q": 0},
         {"N": 1, "W": 2, "Q": 0},
         {"W": 2, "S": 1, "Q": 0}
         ]

loc = 1
print(locations[loc])
while True:
    available_exits = ','.join(exits[loc])
    direction_to_move = input("In which direction would you like to move, you have following options({}) : "
                              .format(available_exits))
    if direction_to_move in exits[loc]:
        loc = exits[loc][direction_to_move]
        print(locations[loc])
    else:
        print("Incorrect Direction, Please try again!!")

    if loc == 0:
        break
