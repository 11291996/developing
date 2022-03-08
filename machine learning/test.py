recover = 99988000019501924806981098019860124999000012350
number = recover
biggest = 0
n = 9

while True:
    digit = number % 10
    if number == 0:
        n = n - 1
        number = recover
    elif n == digit:
        biggest = biggest * 10 + n
    elif n == -1:
        print(biggest)
        break
    number = number // 10
    