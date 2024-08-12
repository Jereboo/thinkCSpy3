"""
Add a method reflect_x to Point which returns a new Point, one which is the reflection of
the point about the x-axis. For example, Point(3, 5).reflect_x() is (3, -5)

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
    	
#Add a method reflect_x to Point which returns a new Point, one which is the reflection of
#the point about the x-axis. For example, Point(3, 5).reflect_x() is (3, -5)

p = Point(3, 4)
q = Point(5, 12)
mid = p.halfway(q)
distance_test = p.distanceFromPoint(q)
p_x_reflected = q.reflect_x()

print(mid)
print(mid.getX())
print(mid.getY())
print(distance_test)
print(p_x_reflected)