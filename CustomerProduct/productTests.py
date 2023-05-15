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
    # Since id and code are read-only properties, we don't test setters for them
    # add similar assertions for the other properties that have setters

def testProductEncapsulation():
    print('Testing Product encapsulation...')
    p = Product(101, "p101", "test description 101", 12.50, 2)
    try:
        p.id = 202
    except AttributeError:
        assert False, "Encapsulation for id failed"
    try:
        p.code = "p202"
    except AttributeError:
        assert False, "Encapsulation for code failed"
    # add similar assertions for the other properties

def run_tests():
    testProductConstructor()
    testProductPropertyGetters()
    testProductPropertySetters()
    testProductEncapsulation()
    print('All tests passed!')

if __name__ == "__main__":
    run_tests()
