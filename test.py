def calcgen():
    global A
    global B
    global C
    for i in list(range(5)):
        if i == 0:
            R1 = set()
            R1 = A - C
            yield "!C ⋂ {} ⋂ (B / C) ⋂ (!C ∪ B)".format(R1), "A / C | {}".format(R1)
        if i == 1:
            R2 = set()
            R2 = B - C
            yield "!C ⋂ {} ⋂ {} ⋂ (!C ∪ B)".format(R1, R2), "B / C | {}".format(R2)

A = {1,2,3,4}
B = {2,4,1,9, 100}
C = {8,3,9}

g = calcgen()
print(next(g))
print(next(g))
