from SOLVER1 import bisection
f = lambda x: 2*x+ x**2+3*x**3-x**4
# The suitable interval for x=3.4567 is [3,4],
# and to reach this point we need epsilon e:1e-3
c,s = bisection(f)
print()
print(f'TotalSteps={s}\tc ={c:0.4f}\tf(c)={f(c):0.9f}')