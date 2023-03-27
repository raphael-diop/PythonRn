nombres = []

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        i = "FizzBuzz"
        nombres.append(i)
    elif i % 3 == 0:
        i = "Fizz"
        nombres.append(i)
    elif i % 5 == 0:
        i = "Buzz"
        nombres.append(i)
    else:
        nombres.append(i)


print(nombres)