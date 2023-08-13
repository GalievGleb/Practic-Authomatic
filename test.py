def del_3(a):
    if a % 3 == 0:
        print("Fizz")
        return "Fizz"
    else:
        return ""


def del_5(a):
    if a % 5 == 0:
        print("Buzz")
        return "Buzz"
    else:
        return ""


a = 1
while a <= 10:
    delenie3 = del_3(a)
    delenit5 = del_5(a)
    if delenie3 != "Fizz" and delenit5 != "Buzz":
        print(a)
    a += 1
