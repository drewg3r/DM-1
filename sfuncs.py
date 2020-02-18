def fintersection(A, B):
    A = list(A)
    B = list(B)
    C =[]
    for j in range(len(A)):
        for i in range(len(B)):
            if A[j] == B[i]:
                C.append(A[j])

    return set(C)

def fdifference(A,B):
    A = list(A)
    B = list(B)
    C = []
    for i in A:
        q = 0
        for j in B:
            if i == j:
                q = 1
        if q == 0:
            C.append(i)
    return set(C)

def funion(a, b):
    a = list(a)
    b = list(b)
    c = b.copy()
    for i in a:
        q=0
        for j in b:
            if i == j:
                q = 1
        if q == 0:
            c.append(i)
    return set(c)

def fadd(A, U):
    U = list(U)
    A = list(A)
    C = []
    for i in U:
        q = 0
        for j in A:
            if i == j:
                q = 1
        if q == 0:
            C.append(i)
    return set(C)
