"""
Write a new method called diagonal that will return the length of the diagonal that runs
from the lower left corner to the opposite corner. 

Solution based on pythagorean theorem
a**2 + b**2 = c**2
(H**2 + W**2) ** .5 = diagonal

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
	
	def __str__(self):
		return "Corner=" + str(self.corner) + ", Width=" + str(self.w) + ", Height=" + str(self.h)

	def getWidth(self):
		return self.w
	
	def getHeight(self):
		return self.h
	
	def area(self):
		return self.w * self.h

	def perimeter(self):
		return self.w * 2 + self.h * 2
	
	def transpose(self):
		orig_h = self.h
		self.h = self.w
		self.w = orig_h
	
	def contains(self, test_point):
		if self.corner.x <= test_point.x < (self.corner.x + self.w) and self.corner.y <= test_point.y < (self.corner.y + self.h):
			return True
		else:
			return False
	
	def diagonal(self):
		return (self.h**2 + self.w**2) ** .5
		
		
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
		

p = Point(0, 0)
test_point_1 = Point(4,2)
test_point_2 = Point(-2,2)
test_rectangle = Rectangle(p, 10, 5)

print(test_rectangle.getWidth())
print(test_rectangle.getHeight())
print(test_rectangle.area())
print(test_rectangle.perimeter())
print(test_rectangle.contains(test_point_1)) #should print True
print(test_rectangle.contains(test_point_2)) #should print False
print("For test_rectangle: ", test_rectangle)
print(test_rectangle.diagonal())

test(test_rectangle.contains(Point(0, 0)), True)
test(test_rectangle.contains(Point(3, 3)), True)
test(test_rectangle.contains(Point(3, 7)), False)
test(test_rectangle.contains(Point(3, 5)), False)
test(test_rectangle.contains(Point(3, 4.99999)), True)
test(test_rectangle.contains(Point(-3, -3)), False)
