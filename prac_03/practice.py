# Random Things
import random

# 1
random_boolean = random.choice([True, False])
print(random_boolean)

# 2
result = random.random()
if result < 0.5:
    random_boolean = False
else:
    random_boolean = True
print(random_boolean)

# 3
random_boolean = bool(random.randint(0, 1))
print(random_boolean)



