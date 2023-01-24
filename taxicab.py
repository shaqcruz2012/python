# Write a class named Taxicab that has three **private** data members: one that holds the current x-coordinate, one that holds the current y-coordinate, and one that holds the current odometer reading. 
# An odometer simply measures the distance a car or bicycle has traveled by keeping track of how many times its wheels have turned. 
# So if you travel one unit left, and then one unit right, you'll be back where you started, but your odometer will tell you that you've traveled 2 units. 
# **All three** data members should be updated as needed so that they are always current. 

# The class should have an `init` method that takes two parameters and uses them to initialize the coordinates, and also initializes the odometer to zero.  

# The class should have get methods for each data member: `get_x_coord`, `get_y_coord`, and `get_odometer`. The class does not need any set methods.  

# It should have a method called `move_x` that takes a parameter that tells how far the Taxicab should shift left or right. It should have a method called `move_y` that takes a parameter that tells how far the Taxicab should shift up or down.  

# For example, the Taxicab class might be used as follows:

# cab = Taxicab(5, -8)       # creates a Taxicab object at coordinates (5, -8)
# cab.move_x(3)              # moves cab 3 units "right"
# cab.move_y(-4)             # moves cab 4 units "down"
# cab.move_x(-1)             # moves cab 1 unit "left"
# print(cab.get_odometer())  # prints the current odometer reading

# At this point the cab has traveled 3 + 4 + 1 = 8 units and is now at coordinates (7, -12)



class Taxicab:

    def get_x_coord(self):
        return self.__x_coord

    def get_y_coord(self):
        return self.__y_coord

    def get_odometer(self):
        return self.__odometer

    def __init__(self, x, y):
        self.__x_coord = x
        self.__y_coord = y
        self.__odometer = 0

    def move_x(self, distance):
        self.__x_coord += distance
        self.__odometer += abs(distance)

    def move_y(self, distance):
        self.__y_coord += distance
        self.__odometer += abs(distance)
# Here __x_coord, __y_coord, and __odometer are private data members, which are used only within the class. 
# The __init__ method takes two parameters and uses them to initialize the coordinates and also initializes the odometer to zero. 
# The move_x and move_y methods take a parameter that tells how far the Taxicab should shift left or right and updates the odometer as well. 
# The class has getter method for each data member: get_x_coord, get_y_coord, and get_odometer, which return the current value of the respective data member.