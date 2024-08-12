"""
Add a method slope_from_origin which returns the slope of the line joining the origin to
the point. For example:

>>> Point(4, 10).slope_from_origin()
2.5

What cases will cause your method to fail? Return None when it happens.
-Error: if you have to divide by 0 (so if x2 = x1) as slope will be undefined (i.e. x = ...)
-Slope can = 0 (just means y = b)

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

p = Point(3, 4)
q = Point(5, 12)
mid = p.halfway(q)
distance_test = p.distanceFromPoint(q)
p_x_reflected = q.reflect_x()
p_slope_from_origin = p.slope_from_origin()
pq_slope = p.slope_of_line(q)

print(mid)
print(mid.getX())
print(mid.getY())
print(distance_test)
print(p_x_reflected)
print(p_slope_from_origin)
print(pq_slope)