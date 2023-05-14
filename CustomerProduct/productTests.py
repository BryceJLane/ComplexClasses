from productList import ProductList, Product

def testProductConstructor():
    print('Testing Product constructor...')
    p = Product(101, "p101", "test description 101", 12.50, 2)
    assert isinstance(p, Product), 'Product constructor test failed'

def testProductPropertyGetters():
    print('Testing Product property getters...')
    p = Product(101, "p101", "test description 101", 12.50, 2)
    assert p.id == 101, 'Product id getter test failed'
    assert p.code == "p101", 'Product code getter test failed'
    # add similar assertions for the other properties

def testProductPropertySetters():
    print('Testing Product property setters...')
    p = Product(101, "p101", "test description 101", 12.50, 2)
    p.id = 102
    p.code = "p102"
    assert p.id == 102, 'Product id setter test failed'
    assert p.code == "p102", 'Product code setter test failed'
    # add similar assertions for the other properties

def testProductEncapsulation():
    print('Testing Product encapsulation...')
    p = Product(101, "p101", "test description 101", 12.50, 2)
    try:
        p.__id = 202
        assert False, "Encapsulation for id failed"
    except AttributeError:
        pass
    try:
        p.__code = "p202"
        assert False, "Encapsulation for code failed"
    except AttributeError:
        pass
    # add similar assertions for the other properties

def run_tests():
    testProductConstructor()
    testProductPropertyGetters()
    testProductPropertySetters()
    testProductEncapsulation()
    print('All tests passed!')

if __name__ == "__main__":
    run_tests()
