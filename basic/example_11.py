######################################################################
#
# Write something here to recognize your own file
# 
# Copyright: MIT License
#
######################################################################

if __name__ == "__main__":
    # LOGICAL OPERATOR
    # and Logical AND	
    # If both the operands are true then condition becomes true.	
    print(True and True)
    
    # or Logical OR
    # If any of the two operands are non-zero then condition becomes true.	
    print(True or False)
    
    # not Logical NOT
    # Used to reverse the logical state of its operand.	
    print(not True)
    
    #COMPARISON OPERATOR
    # >	Greater that - True if left operand is greater than the right	x > y
    # <	Less that - True if left operand is less than the right	x < y
    # ==	Equal to - True if both operands are equal	x == y
    # !=	Not equal to - True if operands are not equal	x != y
    # >=	Greater than or equal to - True if left operand is greater than or equal to the right	x >= y
    # <=	Less than or equal to - True if left operand is less than or equal to the right
    
    x = 10
    y = 12
    # Output: x > y is False
    print('x > y  is', x > y)
    # Output: x < y is True
    print('x < y  is', x < y)
    # Output: x == y is False
    print('x == y is', x == y)
    # Output: x != y is True
    print('x != y is', x != y)
    # Output: x >= y is False
    print('x >= y is', x >= y)
    # Output: x <= y is True
    print('x <= y is', x <= y)
    
    # BRANCH FLOW
    var = 100
    if var == 200:
       print "1 - Got a true expression value"
       print var
    elif var == 150:
       print "2 - Got a true expression value"
       print var
    elif var == 100:
       print "3 - Got a true expression value"
       print var
    else:
       print "4 - Got a false expression value"
       print var
    
    print "Good bye!"