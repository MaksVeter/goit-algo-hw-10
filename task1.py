from pulp import LpMaximize, LpProblem, LpVariable, lpSum

model = LpProblem(name="production-optimization", sense=LpMaximize)

lemonade = LpVariable(name="lemonade", lowBound=0, cat='Continuous')
fruit_juice = LpVariable(name="fruit_juice", lowBound=0, cat='Continuous')

model += lpSum([lemonade, fruit_juice]), "Total_Production"

model += (2 * lemonade + 1 * fruit_juice) <= 100, "Water_Constraint"
model += (1 * lemonade) <= 50, "Sugar_Constraint"
model += (1 * lemonade) <= 30, "Lemon_Juice_Constraint"
model += (2 * fruit_juice) <= 40, "Fruit_Puree_Constraint"

# Розв'язання моделі
model.solve()

# Виведення результатів
print(f"Status: {model.status}")
print(f"Optimal number of Lemonade units: {lemonade.value()}")
print(f"Optimal number of Fruit Juice units: {fruit_juice.value()}")
print(f"Total Production: {model.objective.value()}")
