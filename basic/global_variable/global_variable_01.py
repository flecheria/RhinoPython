b = 5 # this a global variable

def test():
    c = b + 5
    print("print from test: {0}".format(c))

# start global scope
if __name__ == "__main__":
    bb = 12
    print("print from main: {0}".format(bb))
    # test
    test()