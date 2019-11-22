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

class Utilities():
    @staticmethod
    def get_dict_from_object(obj):
        data = vars(obj)
        for key in data:
            print(key)
            a = key.split('__')
            print a[-1]

class Container(object):
    '''Immutable class structure
    '''
    def __init__(self, code, description, connection):
        self.__code = code
        self.__description = description
        self.__connection = connection
    
    @property
    def code(self):
        return self.__code
    
    @property
    def description(self):
        return self.__description
    
    @property
    def connection(self):
        return self.__connection

if __name__ == "__main__":
    item1 = Container(1234, "plate", [2, 8, 56])
    item2 = Container(4569, "support", [])
    
    print item1.code
    print item1.description
    print item1.connection

#    convert object to dict
#    print(item1.__dict__)
#    print(vars(item1))

#    Utilities.get_dict_from_object(item1)