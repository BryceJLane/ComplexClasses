from domino import Domino

def testConstructor():
    print("Testing constructor...")
    domino = Domino(3, 4)
    assert domino.side1 == 3
    assert domino.side2 == 4
    print("Constructor test passed!")

def testPropertyGetters():
    print("Testing property getters...")
    domino = Domino(3, 4)
    assert domino.side1 == 3
    assert domino.side2 == 4
    print("Property getters test passed!")

def testPropertySetters():
    print("Testing property setters...")
    domino = Domino(3, 4)
    domino.side1 = 5
    domino.side2 = 6
    assert domino.side1 == 5
    assert domino.side2 == 6
    print("Property setters test passed!")

def testPropertySettersWithValidation():
    print("Testing property setters with validation...")
    domino = Domino(3, 4)
    try:
        domino.side1 = 13  # assuming 12 is max for a domino
        assert False, "Should have thrown an exception"
    except ValueError:
        pass  # exception was thrown as expected
    print("Property setters with validation test passed!")

def testEncapsulation():
    print("Testing encapsulation...")
    domino = Domino(3, 4)
    try:
        domino.__side1  # attempting to access private attribute
        assert False, "Should have thrown an exception"
    except AttributeError:
        pass  # exception was thrown as expected
    print("Encapsulation test passed!")

def testIsDouble():
    print("Testing isDouble...")
    domino = Domino(5, 5)
    assert domino.is_double() is True
    domino = Domino(5, 6)
    assert domino.is_double() is False
    print("Is double test passed!")

def testFlip():
    print("Testing flip...")
    domino = Domino(1, 2)
    domino.flip()
    assert domino.side1 == 2
    assert domino.side2 == 1
    print("Flip test passed!")

def testEquals():
    print("Testing __eq__...")
    domino1 = Domino(1, 2)
    domino2 = Domino(2, 1)
    domino3 = Domino(3, 4)
    assert (domino1 == domino2) is True
    assert (domino1 == domino3) is False
    print("__eq__ test passed!")
