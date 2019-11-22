from random import random

def test(_value):
    return str( random() * _value )
    
if __name__ == "__main__":
    
    a = float( test(30) ) > 30
    b = float( test(30) ) <= 30
    
    print(a == False)
    print(b == True)