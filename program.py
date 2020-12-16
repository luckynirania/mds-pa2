import cvxpy as cp
import numpy as np
import numpy as np

def norm0(v):
    res = 0
    for e in v:
        if e != 0:
            res+=1
    return res


def norm1(v):
    res = 0
    for e in v:
        res += abs(e)
    return res

def norm2squared(v):
    res = 0
    for e in v:
        res += e**2
    return res**2

A_inv = np.load("data/A_inv.npy")
C = np.load("data/C.npy")
y = np.load("data/y.npy")

print("A_inv.shape",A_inv.shape)
print("C.shape",C.shape)
print("y.shape",y.shape)

k,n = C.shape

print("k,n:",k,n)

# Construct the problem.
x = cp.Variable(n)
objective = cp.Minimize( cp.norm(x,1)  )
constraints = [ cp.sum_squares(y-np.dot(C,x)) ]
prob = cp.Problem(objective, constraints)

result = prob.solve()
print(x.value)

# print(constraints[0].dual_value)

# print(norm2squared([4.3212,2]))