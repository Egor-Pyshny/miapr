import math
import random

import drawer
import matplotlib.pyplot as plt

basic_coef = [1,4,4,16]
my_coef = [0,0,0,0]
my_prev_coef = [0,0,0,0]
data = [
    {
        "obj":[-1,0],
        "class":0,
    },
    {
        "obj":[1,1],
        "class":0,
    },
    {
        "obj":[2,0],
        "class":1,
    },
    {
        "obj":[1,-2],
        "class":1,
    },
]

data_for_classification = []
for i in range(0, 250):
    temp = [random.randint(-10, 10), random.randint(-10, 10)]
    data_for_classification.append(temp)

res = False
i = 0
sign = 1
while not res:
    my_prev_coef = my_coef.copy()
    my_coef[0] = basic_coef[0]
    my_coef[1] = basic_coef[1]*data[i]["obj"][0]
    my_coef[2] = basic_coef[2]*data[i]["obj"][1]
    my_coef[3] = basic_coef[3]*data[i]["obj"][0]*data[i]["obj"][1]
    my_coef = [my_prev_coef[i]+my_coef[i]*sign for i in range(0, 4)]
    potential = my_coef[0] + \
                my_coef[1]*data[i+1]["obj"][0]+ \
                my_coef[2]*data[i+1]["obj"][1]+ \
                my_coef[3]*data[i+1]["obj"][0]*data[i+1]["obj"][1]
    if potential<=0 and not data[i+1]["class"]:
        sign=1
    else:
        sign=-1
    if not data[i+1]["class"]:
        res = potential > 0
    else:
        res = potential < 0
    i += 1
    if i == len(data)-1:
        i = 0

x_min = math.inf
x_max = -math.inf
y_min = math.inf
y_max = -math.inf

for point in data:
    x = point["obj"][0]
    y = point["obj"][1]
    if x > x_max:
        x_max = x
    if x < x_min:
        x_min = x
    if y > y_max:
        y_max = y
    if y < y_min:
        y_min = y
    if not point["class"]:
        color = "green"
    else:
        color = "red"
    plt.scatter(x, y, color=color)

for point in data_for_classification:
    x = point[0]
    y = point[1]
    if x > x_max:
        x_max = x
    if x < x_min:
        x_min = x
    if y > y_max:
        y_max = y
    if y < y_min:
        y_min = y
    p = my_coef[0] + \
        my_coef[1]*point[0] + \
        my_coef[2]*point[1] + \
        my_coef[3]*point[0]*point[1]
    if p > 0:
        color = "green"
    else:
        color = "red"
    plt.scatter(point[0],point[1],color = color)

plt.xlim(x_min-1, x_max+1)
plt.ylim(y_min-1, y_max+1)
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.grid(linewidth=0.2)
drawer.show_results(my_coef,data, plt)
plt.show()