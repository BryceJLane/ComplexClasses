from productTests import *
from productListTests import *

def main():
    # Product tests
    testProductConstructor()
    testProductPropertyGetters()
    testProductPropertySetters()
    testProductEncapsulation()

    # ProductList tests
    testConstructor()
    testAppend()
    testPop()
    testFind()
    testRemove()
    testClear()
    testGetItem()
    testSetItem()
    testIn()
    testForLoop()
    testAdd()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
