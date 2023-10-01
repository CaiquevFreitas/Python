num = 0
m = 1
while True:
    num = int(input("Você quer ver a tabuada de qual número? "))
    if num < 0:
        break
    print("-"*20)
    while m <= 10:
        result = num * m
        print("{} x {} = {}".format(num, m, result))
        m += 1
    m = 1
    print("-"*20)