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

from Rhino.Geometry import Point3d

if __name__ == "__main__":
    # everything in Python is an object
    name = "Pippo"
    print( dir(name) ) # this call all the method available for the name object

    test_list = [4, 'a', 8.96]
    print( dir(test_list) )

    test_point = Point3d(0., 0., 0.)
    print( dir(test_point) )    # same things for the test_point object

    # some method are similar between the tow object
    # These are the default method that every Python object has
