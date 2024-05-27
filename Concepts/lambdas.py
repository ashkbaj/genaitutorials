x = lambda x : x + 10
print(x(6))


def function(num):
    return lambda x: num * x

doubleit = function(2)
tripleit = function(3)

print(doubleit(9))

print(tripleit(11))

