def change():
    b = 100

def test():
    c = b + 5
    print("print from test: {0}".format(c))

# start global scope
if __name__ == "__main__":
    b = 12
    print("print from main: {0}".format(b))
    # test
    test()
    # change the value of the
    change()
    # test another time
    test()
    # as before we print the local variable
    print("print from main: {0}".format(b))