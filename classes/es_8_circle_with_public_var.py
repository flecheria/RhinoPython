######################################################################
#
# DO NOT CANCEL THIS PART
# Author: Paolo Cappelletto
# e-mail: info@flecheria.it
# skype: flecheria
# Date: 191014
# Version: 1.0
# 
# Copyright: MIT License
#
######################################################################

from math import pi, pow
from Rhino.Geometry import Point3d
import System.Guid as guid

class Circle(object):
    
    def __init__(self, _center, _radius):
        self.center = _center
        self.radius = _radius
        self.guid = guid.NewGuid()
    
    def get_circonference(self):
        return 2 * pi * self.radius
        
    def get_area(self):
        return pi * pow(self.radius, 2)
    
    def set_radius(self, value):
        self.radius = value
    
    def get_radius(self):
        return self.radius
    
    def set_center(self, center):
        self.center = center
    
    def get_center(self):
        return self.center
    
    def get_guid(self):
        return self.guid

if __name__ == "__main__":
    
    circle_1 = Circle(Point3d(5.0, 3.0, 1.0), 5.0)
    
    # print(circle_1.__radius)
    print( circle_1.get_radius() )
    print( circle_1.radius )
    
    print( circle_1.get_circonference() )
    print( circle_1.get_area() )
    print( type( circle_1.get_center() ) )
    print( circle_1.get_radius() )
    circle_1.set_radius(8.0)
    print( circle_1.get_radius() )
    print( circle_1.get_guid() )
    
    circle_1.radius = 10
    print( circle_1.get_radius() )