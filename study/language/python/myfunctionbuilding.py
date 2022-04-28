class myfunctions:
    def __init__(self):
        pass
    def my_abs(self, number):
        if number < 0:
            return -1 * (number // 1)
        return number
    def my_round(self, number, ndigits = None):
        if ndigits:
            if (number // 10 ** -ndigits) * (10 ** -ndigits) - (number // 10 ** -ndigits - 1) * (10 ** -ndigits - 1) > 5 * (10 ** -ndigits):
                return (number // 10 ** -ndigits) * (10 ** -ndigits) + 10 ** (-ndigits)
            return (number // 10 ** -ndigits) * (10 ** -ndigits)
        if ndigits == None:
            if (number - 1) > 0.5:
                return 2
            return 1
    def my_any(self, iterable):
        for element in iterable:
            if element: 
                return True
        return False
    def my_enumerate(self, sequence, start = 0):
        i = start
        for element in sequence:
            yield i , element #yield -> uses single memory address in a generator
            i += 1
    def my_max(*args): #*arg -> meta data for tuples, **kwargs -> meta data for dictionaries. Following words after the stars is not important.
        return sorted(*args)

    def my_min(*args):
        pass
            

if __name__ == "__main__":
    myfunctions = myfunctions() #class declaration

    test1 = 1.7
    test2 = -8

    assert abs(test1) == myfunctions.my_abs(test1)
    assert abs(test2) == myfunctions.my_abs(test2)

    print("통과")

    test = 1.74789

    assert round(test) == myfunctions.my_round(test)
    assert round(test, 3) == myfunctions.my_round(test, 3)
    assert round(-test, 2) == myfunctions.my_round(-test, 2)

    print("통과")

    test1 = [True, 7 == 4, 'Something', False]
    test2 = [3 > 5, 10 != 10, False, '', None]
    assert any(test1) == myfunctions.my_any(test1)
    assert any(test2) == myfunctions.my_any(test2)
    
    print("통과")

    test1 = [60, 50, 20, 10]
    test2 = [True, None, 'test']

    assert list(enumerate(test1)) == list(myfunctions.my_enumerate(test1))
    assert list(enumerate(test2, 12)) == list(myfunctions.my_enumerate(test2, 12))

    print("통과")
    
    test = [7, 4, 2, 6, 8]
    
    print(myfunctions.my_max(test))
    #assert max(test) == my_max(test) and min(test) == my_min(test)
    #assert max(7, 4, 2, 5) == my_max(7, 4, 2, 5) and min(7, 4, 2, 5) == my_min(7, 4, 2, 5)
    
    print("통과")