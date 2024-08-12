"""
In games, we often put a rectangular “bounding box” around our sprites in the game. We can
then do collision detection between, say, bombs and spaceships, by comparing whether their
rectangles overlap anywhere.

Write a function to determine whether two rectangles collide. Hint: this might be quite a
tough exercise! Think carefully about all the cases before you code.

#It works! Not efficient, but it works. And without looking up a solution... Hmm!
#Didn't have a very satisfying moment of triumph as it took me forever to verify I got it right...


#Structure of Point class taken from Chapter 16 of ThinkCSpy3 Interactive
"""

#I discovered test() is not a fx that is a out of the box with Python3. I need to figure 
#out how to write this into something I can import into future code
#^^^L/U import stuff soon.

def test(actual, expected):
    """ Compare the actual to the expected value,
        and print a suitable message.
        Source: https://stackoverflow.com/questions/6913023/test-function-in-python-book-how-to-think-like-a-computer-scientist
    """
    import sys
    linenum = sys._getframe(1).f_lineno   # get the caller's line number.
    if (expected == actual):
        msg = "Test on line {0} passed.".format(linenum)
    else:
        msg = ("Test on line {0} failed. Expected '{1}', but got '{2}'."
                                     . format(linenum, expected, actual))
    print(msg)


class Rectangle:
	
	def __init__(self, corner_point, width, height):
		self.corner = corner_point
		self.w = width
		self.h = height
		self.corner.top_left = Point(self.corner.x, (self.corner.y + self.h))
		self.corner.top_right = Point((self.corner.x + self.w), (self.corner.y + self.h))
		self.corner.bottom_right = Point((self.corner.x + self.w), self.corner.y)
	
	def __str__(self):
		return "Corner=" + str(self.corner) + ", Width=" + str(self.w) + ", Height=" + str(self.h)

	def getWidth(self):
		return self.w
	
	def getHeight(self):
		return self.h
	
	def getCorner(self):
		return self.corner
	
	def area(self):
		return self.w * self.h

	def perimeter(self):
		return self.w * 2 + self.h * 2
	
	def transpose(self):
		orig_h = self.h
		self.h = self.w
		self.w = orig_h
	
	def contains(self, test_point):
		if self.corner.x <= test_point.x <= (self.corner.x + self.w) and self.corner.y <= test_point.y <= (self.corner.y + self.h):
			return True
		else:
			return False
	
	def diagonal(self):
		return (self.h**2 + self.w**2) ** .5
	
	def bounding_box(self, other_rectangle):
		main_rectangle_points = [self.corner, self.corner.top_left, self.corner.top_right, self.corner.bottom_right]
		other_rectangle_points = [other_rectangle.corner, other_rectangle.corner.top_left, other_rectangle.corner.top_right, other_rectangle.corner.bottom_right]
		for point in other_rectangle_points:
			if self.contains(point) == True:
				collision_statement = "Point " + str(point) + " of the second rectangle is within or touching the first."
				return collision_statement
		#Is the next if statement necessary?
		for point in main_rectangle_points:
			if other_rectangle.contains(point) == True:
				collision_statement = "Point" + str(point) + " of the first rectangle is within or touching the second."
				return collision_statement
			else:
				non_collision_statment = "Neither of the rectangles touch."
				return non_collision_statment
		
		
class Point:

    def __init__(self, initX, initY):
        """ Create a new point at the given coordinates. """
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"
        #return "x=" + str(self.x) + ", y=" + str(self.y) #<-- Their __str__ method

    def halfway(self, target):
         mx = (self.x + target.x) / 2
         my = (self.y + target.y) / 2
         return Point(mx, my)
    
    def distanceFromPoint(self, point):
    	#based on distance formula: distance = (((x2-x1)**2) + ((y2-y1)**2)) ** 0.5
    	x_dif = point.x - self.x
    	y_dif = point.y - self.y
    	return ((x_dif**2) + (y_dif**2)) ** 0.5
    	
    def reflect_x(self):
    	reflected_y = self.y * -1
    	return Point(self.x, reflected_y)
    
    def slope_from_origin(self):
    	#based on slope formula: m = (y2-y1)/(x2-x1)
    	if self.x == 0:
    		return None
    	else:
    		return self.y/self.x
    
    def slope_of_line(self, point):
    	#based on slope formula: m = (y2-y1)/(x2-x1)
    	x_dif = point.x - self.x
    	y_dif = point.y - self.y
    	if x_dif == 0:
    		slope = None
    	else:
    		slope = y_dif/x_dif    	
    	return slope
    	
    def equation_of_line(self, point):
    	#based on: y = mx + b
    	#b = y - mx
    	slope = self.slope_of_line(point)
    	b = self.y - (slope*self.x)
    	return (slope, b)
    
    def move_point(self, dx, dy):
    	self.x = self.x + dx
    	self.y = self.y + dy
		

#p = Point(0, 0)
#test_point_1 = Point(4,2)
#test_point_2 = Point(-2,2)
test_rectangle = Rectangle(Point(-1,-1), 3, 3)
test_rectangle_2 = Rectangle(Point(1,1), 3, 4)
test_rectangle_3 = Rectangle(Point(2,2), 2, 2)
test_rectangle_4 = Rectangle(Point(3,2), 2, 2)


#print(test_rectangle.getWidth())
#print(test_rectangle.getHeight())
print("For test_rectangle: ", test_rectangle)
print(test_rectangle.getCorner())
print(test_rectangle.corner.top_left)
print(test_rectangle.corner.top_right)
print(test_rectangle.corner.bottom_right)
print()
print("For test_rectangle_2: ", test_rectangle_2)
print(test_rectangle_2.getCorner())
print(test_rectangle_2.corner.top_left)
print(test_rectangle_2.corner.top_right)
print(test_rectangle_2.corner.bottom_right)
print()
print(test_rectangle.bounding_box(test_rectangle_2))
print()
print("For test_rectangle_3: ", test_rectangle_3)
print(test_rectangle_3.getCorner())
print(test_rectangle_3.corner.top_left)
print(test_rectangle_3.corner.top_right)
print(test_rectangle_3.corner.bottom_right)
print()
print(test_rectangle.bounding_box(test_rectangle_3))
print()
print("For test_rectangle_4: ", test_rectangle_4)
print(test_rectangle_4.getCorner())
print(test_rectangle_4.corner.top_left)
print(test_rectangle_4.corner.top_right)
print(test_rectangle_4.corner.bottom_right)
print()
print(test_rectangle.bounding_box(test_rectangle_4))