# 线性规划2

import pulp

profit = pulp.LpProblem("My LP Problem", pulp.LpMaximize)

x = pulp.LpVariable('x', lowBound=0, cat='Integer') #Integer---不连续的整数
y = pulp.LpVariable('y', lowBound=2, cat='Integer') #Continuous--连续的

# Objective function目标函数
profit += 72 * x + 64 * y

# Constraints约束
profit += 3 * x <= 100
profit += 12 * x + 8 * y <= 480
profit += x + y <= 50

print(profit)

profit.solve()
print(pulp.LpStatus[profit.status])

for variable in profit.variables():
    print ('{} = {}'.format(variable.name, variable.varValue))
    
print(pulp.value(profit.objective))