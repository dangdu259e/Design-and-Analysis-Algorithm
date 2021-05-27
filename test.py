from pulp import *

x1 = LpVariable("x1", 0, None, LpInteger)
x2 = LpVariable("x2", 0, None, LpInteger)
y1 = LpVariable("y1", 0, None, LpInteger)
y2 = LpVariable("y2", 0, None, LpInteger)


def ac(a=75):
    cond_1 = 25 * x1 + 46 * x2 + 16 * y1 + 34 * y2 <= 2500
    cond_2 = 50 * x1 + 30 * x2 + 28 * y1 + 12 * y2 <= 2800
    cond_3 = x1 + x2 >= 20
    cond_4 = -x1 + x2 - y1 + y2 >= 0
    for i in range(a, 101):
        temp = i/100
        # return cond_1, cond_2, cond_3, cond_4, cond_5, cond_6
        cond_5 = x1 + x2 <= temp * (x1 + x2 + y1 + y2)
        cond_6 = y1 + y2 <= temp * (x1 + x2 + y1 + y2)
        prob_1 = LpProblem("myProblem", LpMaximize)
        prob_1 += cond_1
        prob_1 += cond_2
        prob_1 += cond_3
        prob_1 += cond_4
        prob_1 += cond_5
        prob_1 += cond_6
        prob_1 += (400 * x1 + 560 * x2 + 500 * y1 + 700 * y2)
        prob_1.solve()
        print(i)
        print(prob_1.constraints)
        print("Optimal value = ", pulp.value(prob_1.objective))
ac()
