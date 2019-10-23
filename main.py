print("trial:1")

for i in range(1, 100+1):

    if i % 15 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)

print("trial2")
def fizbuz(i):

    if i % 15 == 0:
        return("fizzbuzz")
    elif i % 3 == 0:
        return("fizz")
    elif i % 5 == 0:
        return("buzz")
    else:
        return(i)

for i in range(1,101):
    fizbuz(i)
