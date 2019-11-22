def constant():
    b = 5
    return b

def test():
    c = b + 5
    print("print from test: {0}".format(c))

# start global scope
if __name__ == "__main__":
    b = constant()
    print("print from main: {0}".format(b))
    # test
    test()