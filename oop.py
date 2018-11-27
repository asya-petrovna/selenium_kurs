class Point2D:
    def __init__(self, x, y):
        """
        Here we initialize fields of a newly created object, storing the values as properties
        :param x: horizontal coordinate
        :param y: vertical coordinate
        """
        self.x = x
        self.y = y


point_one = Point2D(3, 5)  # here new instantiate a concrete object with specific values


class Rectangle:
    number_of_angles = 4  # all rectangles share the value of this property

    def __init__(self, top_left_point, width, height):
        """
        Construct a rectangle from one point, its width and height
        """
        # and the values of properties defined below can only belong to specific instances of the class
        self.top_left = top_left_point
        # here we are free to instantiate other objects (of other classes and this class if we would like)
        # so let's create three other points, calculating their coordinates
        self.top_right = Point2D(self.top_left.x + width, self.top_left.y)
        self.bottom_left = Point2D(self.top_left.x, self.top_left.y - height)
        self.bottom_right = Point2D(self.top_right.x, self.bottom_left.y)


# since we already have a point, let's create a rectangle
rect = Rectangle(point_one, 3, 1)

# in order to print the following message we don't need to instantiate a rectangle
# since we use a static property of Rectangle class – the one that's shared across all it's instances
print(f'Rectangles always have {Rectangle.number_of_angles} angles')
# by the way, you can access static properties through a specific object reference,
# but that's usually a bad practice, as it's confusing for a reader of your code
print(f'Our new rect has {rect.number_of_angles} angles')

# the following line is incorrect, as to know a top left coordinate of a rectangle
# you need to have a specific rectangle instance
# print(f'Top left point is {Rectangle.top_left}')

# like this
print(f'Top left point is {rect.top_left}')
