class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '(' + str(self.getX()) + ',' + str(self.getY()) + ')'
    def __eq__(self, coor):
        if self.getX() == coor.getX() and self.getY() == coor.getY():
           return True
        else:
           return False
    def __repr__(self):
        #return "Coordinate(" + str(self.getX()) + "," + str(self.getY()) + ")"
		return "Coordinate" + self.__str__() #str(self)
coor1 = Coordinate(1,1) # __init__(1,1)
coor1.__init__(2,2)
coor2 = Coordinate(1,1)
#print coor1.__eq__(coor2)
#print coor1 == coor2
print repr(coor1) # coor1.__repr__()
print eval(repr(coor1))
print coor1 == eval(repr(coor1))
print coor2 == eval(repr(coor1))
