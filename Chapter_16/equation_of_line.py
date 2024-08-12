"""
The equation of a straight line is “y = ax + b”, (or perhaps “y = mx + b”). The 
coefficients a and b completely describe the line. Write a method in the Point class so 
that if a point instance is given another point, it will compute the equation of the 
straight line joining the two points. It must return the two coefficients as a tuple of
two values. For example,

>>> print(Point(4, 11).get_line_to(Point(6, 15)))
>>> (2, 3)

This tells us that the equation of the line joining the two points is “y = 2x + 3”. When 
will your method fail?
#if slope is undefined

#b = y - mx 
#Remember: y = mx + b
#Slope formula: m = (y2-y1)/(x2-x1)

#Structure of class taken from lesson
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
        return "x=" + str(self.x) + ", y=" + str(self.y)

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
    	if slope != None:
    		b = self.y - (slope*self.x)
    	else:
    		return "The slope is undefined, so x=" + str(self.x)
    	return (slope, b)
		

p = Point(3, 4)
q = Point(3, 12)
mid = p.halfway(q)
distance_test = p.distanceFromPoint(q)
p_x_reflected = q.reflect_x()
p_slope_from_origin = p.slope_from_origin()
pq_slope = p.slope_of_line(q)
pq_line_eq = p.equation_of_line(q)

print(mid)
print(mid.getX())
print(mid.getY())
print(distance_test)
print(p_x_reflected)
print(p_slope_from_origin)
print(pq_slope)
print(pq_line_eq)