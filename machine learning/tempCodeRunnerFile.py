recover = 9999991123000090000099900
number = recover
biggest = 0
n = 9


while True:
    digit = number % 10
    if n == digit:
        biggest = biggest * 10 + n 
        number = number // 10
    elif number == 0:
        n -= 1
        number = recover 
    elif n <= 0:
        print(biggest)
        break
    else:  
        number = number // 10