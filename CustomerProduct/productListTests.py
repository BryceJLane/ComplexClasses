from productList import *


def testConstructor():
    pList = ProductList()
    print(f"Testing constructor.  Expect empty list. {pList}")
    print(f"Expect count property to be 0. {pList.count}")
    print(f"Expect len function to be 0. {len(pList)}")


def testAppend():
    pList = ProductList()
    p1 = Product(101, "p101", "test description 101", 12.50, 2)
    p2 = Product(102, "p102", "test description 102", 20, 4)
    pList.append(p1)
    pList.append(p2)
    print(f"Testing append.  Expect list with 2 products. {pList}")
    print(f"Expect count property to be 2. {pList.count}")
    print(f"Expect len function to be 2. {len(pList)}")


def createList():
    pList = ProductList()
    p1 = Product(101, "p101", "test description 101", 12.50, 2)
    p2 = Product(102, "p102", "test description 102", 20, 4)
    p3 = Product(103, "p103", "test description 103", 30, 1)
    pList.append(p1)
    pList.append(p2)
    pList.append(p3)
    return pList


def testPop():
    pList = createList()
    print(f"Testing pop.  Before pop expect list with 3 products. {pList}")
    print(f"Expect count property to be 3. {pList.count}")
    print(f"Expect len function to be 3. {len(pList)}")
    p3 = pList.pop()
    print(f"After pop with no parameter.  Expect first 2 products. {pList}")
    print(f"Expect popped product to be p103. {p3}")
    print(f"Expect count property to be 2. {pList.count}")
    print(f"Expect len function to be 2. {len(pList)}")
    p1 = pList.pop(0)
    print(f"After pop with 0 parameter.  Expect just p102. {pList}")
    print(f"Expect popped product to be p101. {p1}")
    print(f"Expect count property to be 1. {pList.count}")
    print(f"Expect len function to be 1. {len(pList)}")


def testFind():
    pList = createList()
    print(f"Testing find.  Current list with 3 products. {pList}")
    index = pList.find("p102")
    print(f"Called find with p102 as parameter.  Expect index to be 1. {index}")
    p2 = Product(102, "p102", "test description 102", 20, 4)
    # this will return -1 if __eq__ is not defined on the product class
    index = pList.find(p2)
    print(f"Called find with Product object p102 as parameter.  Expect index to be 1. {index}")
    index = pList.find("p104")
    print(f"Called find with p104 as parameter.  Expect index to be -1. {index}")
    p4 = Product(104, "p104", "test description 104", 20, 4)
    index = pList.find(p4)
    print(f"Called find with Product object p104 as parameter.  Expect index to be -1. {index}")


def testRemove():
    pList = createList()
    p2 = Product(102, "p102", "test description 102", 20, 4)
    print(f"Testing find.  Current list with 3 products. {pList}")
    pList.remove(p2)
    print(f"Called remove with Product object p102 as parameter.  Expect list to now have 2 products. {pList}")
    p4 = Product(104, "p104", "test description 104", 20, 4)
    try:
        pList.remove(p4)
        print(f"Called remove with Product object p104 as parameter.  An exception should have been thrown but was not.")
    except ValueError:
        print(f"Called remove with Product object p104 as parameter.  An exception was expected and was thrown")
        print(f"Expect list to still have 2 products. {pList}")


def testClear():
    pList = createList()
    print(f"Testing clear.  Current list with 3 products. {pList}")
    pList.clear()
    print(f"After the call to clear.  Expect list to be empty. {pList}")


def testGetItem():
    pList = createList()
    print(f"Testing list access by index.  Current list with 3 products. {pList}")
    p = pList[1]
    print(f"Element at index 1.  Expect p102. {p}")
    p = pList["p103"]
    print(f"Element with key of p103.  Expect p103. {p}")
    try:
        p = pList[2.5]
    except TypeError:
        print(f"Used [] with float as index.  An exception was expected and was thrown")


def testSetItem():
    pList = createList()
    print(f"Testing changing a list element by index.  Current list with 3 products. {pList}")
    p4 = Product(104, "p104", "test description 104", 20, 4)
    pList[2] = p4
    print(f"Set element at index 2 to p104.  p104 should be at the end of the list. {pList}")
    try:
        pList["p104"] = p4
    except TypeError:
        print(f"Used [] with string as index.  An exception was expected and was thrown")
    try:
        pList[1] = "cat"
    except TypeError:
        print(f"Used [] with string element rather than a product.  An exception was expected and was thrown")


def testIn():
    pList = createList()
    print(f"Testing in.  Current list with 3 products. {pList}")
    p2 = Product(102, "p102", "test description 102", 20, 4)
    p4 = Product(104, "p104", "test description 104", 20, 4)
    print(f"Is p102 in the list?  Expect true  {p2 in pList}")
    print(f"Is p104 in the list?  Expect false  {p4 in pList}")


def testForLoop():
    pList = createList()
    print(f"Testing for loop.  Current list with 3 products. {pList}")
    print(f"Iterating through the list with for in.  Expect 3 individual products")
    for p in pList:
        print(p)


def testAdd():
    pList = createList()
    pList2 = createList()
    pListCombined = pList + pList2
    print(f"Testing adding 2 product lists.  Expect list with 6 products. {pListCombined}")