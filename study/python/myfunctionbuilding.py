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