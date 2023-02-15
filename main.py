import numpy
from numpy.polynomial import Polynomial as Poly


q = int(input("1) Lagrange\n2) Newton\n3) Vandernonde\n4) Hermit\nChoose a method : "))  # NOQA
n = int(input("order of the function: "))

x = []
y = []
for k in range(n + 1):
    x.append(int(input(f"Enter x[{k}] : ")))
    y.append(int(input(f"Enter y[{k}] : ")))

# floating point error
def fr(p):
    for c in range(len(p.coef)):
        p.coef[c] = numpy.round(p.coef[c], 5)
    return p


def lagrange():
    f = Poly([0])
    for i in range(n + 1):
        lp = Poly([1])
        for j in range(n + 1):
            if i != j:
                lp *= Poly([(-x[j]) / (x[i] - x[j]), 1 / (x[i] - x[j])])

        print(f"L{i} = {fr(lp)}")

        f += lp * Poly([y[i]])

    print(f"P(x) = {fr(f)}")


def newton():
    pass


def vandernonde():  # NOQA
    pass


def hermit():
    pass


if q == 1:
    lagrange()
elif q == 2:
    newton()
elif q == 3:
    vandernonde()
elif q == 4:
    hermit()
