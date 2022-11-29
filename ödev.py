from pulp import*

TYPES = ["warehouse","factory"] #i
CITIES = ["bolu","sivas"] #j

p = {"warehouse":{"bolu":1,"sivas":2},"factory":{"bolu":3,"sivas":2}}
c = {"warehouse":{"bolu":5,"sivas":2},"factory":{"bolu":6,"sivas":3}}

model = LpProblem("Profit_Maximization",LpMaximize)

X = LpVariable.dicts("",[(i,j) for i in TYPES for j in CITIES],0, 1, cat = "Binary")

model += lpSum(lpSum([[X[(i,j)]*p[i][j] for j in CITIES] for i in TYPES]))

model += lpSum([X[("warehouse",j)] for j in CITIES])<=1

model += lpSum(lpSum([[c[i][j]*X[(i,j)] for j in CITIES] for i in TYPES])) <= 10
               
for j in CITIES:

    model += X[("factory",j)] >= X[("warehouse",j)]

print(model)
status = model.solve()
status = LpStatus[status]

print("Values for opening a wirehouse in bolu,sivas and opening a factory in bolu,sivas given below respectively.")
print([X[(i,j)]for i in TYPES for j in CITIES], [X[(i,j)].varValue for i in TYPES for j in CITIES])
print("PROFIT: ", value(model.objective),"Million")
print(status)
