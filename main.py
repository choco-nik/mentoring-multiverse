grid = input("Enter x and y value of grid size seperated by a space e.g. 4 8:  ") #

if len(grid) > 4:
    print("Error: You need to enter 2 values seperated by a space")
else:
   print(f"Thank you for entering your x={grid[0]} y={grid[2]} coordinates")

orientation = input("Enter the orientation of the robot North, East, South, West:  ")

if orientation.lower() == "north":
    orientation = "N"
elif orientation.lower() == "east":
    orientation = "E"
elif orientation.lower() == "south":
    orientation = "S"
elif orientation.lower() == "west":
    orientation = "W"
else:
    print("Please enter one of the following: North, East, South, West")

initial_state_x = input("Enter x value of the robot's position:  ")
intiial_state_y = input("Enter y value of the robot's position:  ")
movement_guide = print("Each robot can move one space (F), rotate left by 90 degrees (L) or rotate right by 90 degrees (R)")
movement = input("Please enter the robots movements using the letters e.g. LFR:  ").lower()


#Adds the moves to a list
list_of_moves = [x for x in movement]


class Robot():
    def __init__(self, start_x_cor, start_y_cor, orientation, moves):
        self.orientation = orientation
        self.x_cor = start_x_cor
        self.y_cor = start_y_cor
        self.moves = moves


    def rotate_left():
        if orientation == 'n':
            orientation = 'w'
        elif orientation == 'w':
            orientation = 's'
        elif orientation == 's':
            orientation = 'e'
        elif orientation == 'e':
            orientation = 'n'
        else:
            orientation = "Can't turn this way"


    def rotate_right():
        if orientation == 'n':
            orientation = 'e'
        elif orientation == 'e':
            orientation = 's'
        elif orientation == 's':
            orientation = 'w'
        elif orientation == 'w':
            orientation = 'n'
        else:
            orientation = "Can't turn this way"

    def move_north(self):
        self.x_cor += 1

    def move_east(self):
        self.x_cor += 1

    def move_south(self):
        self.y_cor-= 1

    def move_west(self):
        self.y_cor -= 1


    def move_forward(self):
        if self.orientation == 'n':
            self.move_north()
        elif self.orientation == 'e':
            self.move_east()
        elif self.orientation == 's':
            self.move_south()
        elif self.orientation == 'w':
            self.move_west()


user = Robot(initial_state_x, intiial_state_y, orientation, movement)
print(user.x_cor, user.y_cor)

list_of_moves = [ x for x in movement]

for i in list_of_moves:
    if i == "l":
        user.rotate_left
    if i == "f":
        user.move_forward
    if i == "r":
        user.rotate_right

