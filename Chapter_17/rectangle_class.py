"""
We can represent a rectangle by knowing three things: the location of its lower left
corner, its width, and its height. Create a class definition for a Rectangle class using
this idea. To create a Rectangle object at location (4,5) with width 6 and height 5, we
would do the following:

r = Rectangle(Point(4, 5), 6, 5)


#Structure of Point class taken from Chapter 16 of ThinkCSpy3 Interactive
"""

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
		
		"""My original code (I knew I could shorten in 1 line, but couldn't remember how.
		orig_h = self.h
		orig_w = self.w
		self.h = orig_w
		self.w = orig_h
		""" 
		
		
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
		

p = Point(3, 4)
test_rectangle = Rectangle(p, 3, 4)

print(test_rectangle.getWidth())
print(test_rectangle.getHeight())
print(test_rectangle.area())
print(test_rectangle.perimeter())
print("For test_rectangle: ", test_rectangle)

test_rectangle.transpose()

print(test_rectangle.getWidth())
print(test_rectangle.getHeight())
print(test_rectangle.area())
print(test_rectangle.perimeter())
print("For test_rectangle: ", test_rectangle)