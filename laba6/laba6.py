import math
from drawer import draw_result

SIZE = 5
START_SIZE = 5
distances = [
    [0,13,11,10,6],
    [13,0,6,10,15],
    [11,6,0,18,6],
    [10,10,18,0,13],
    [6,15,6,13,0],
]
# distances = [
#     [0,5,0.5,2],
#     [5,0,1,0.6],
#     [0.5,1,1,2.5],
#     [2,0.6,2.5,0],
# ]

groups = []

def find_min():
    min_1 = []
    min_2 = []
    minvalue = math.inf
    for i in range(0,SIZE):
        for j in range(i+1, SIZE):
            if distances[i][j] < minvalue:
                minvalue = distances[i][j]
                min_1.append(i)
                min_2.append(j)
                return min_1, min_2, minvalue
    for i in range(0,SIZE):
        for j in range(i, SIZE):
            if distances[i][j] == minvalue:
                min_1.append(i)
                min_2.append(j)
                return min_1, min_2, minvalue
    return min_1, min_2, minvalue


def new_value(indexes, ind):
    mins = []
    for i in indexes:
        mins.append(distances[i][ind])
    return min(mins)


def is_continue():
    count = 0
    for i in range(0, SIZE):
        for j in range(0, SIZE):
            if distances[i][j] != math.inf:
                count += 1
                if count>1:
                    return True
    return False


repl = math.inf
# for l3 in distances:
#     for i in range(0,SIZE):
#         l3[i] = 1/l3[i] if l3[i]!=0 else 0

while True:
    min_i, min_j, min_v = find_min()
    temp4 = *min_i,*min_j
    temp = []
    new_grp = list(set(temp4))
    new_grp.append(float(min_v))
    groups.append(new_grp)
    t3=[]
    for l1 in range(0,SIZE):
        t1 = []
        for l2 in range(0,SIZE):
            if (l2 in min_i or l2 in min_j) or (l1 in min_i or l1 in min_j):
                t1.append(repl)
            else:
                t1.append(distances[l1][l2])
        if (l1 in min_i or l1 in min_j):
            t1.append(repl)
        else:
            t1.append(new_value([*min_i,*min_j],l1))
        t3.append(t1[-1])
        temp.append(t1)
    t3.append(0)
    temp.append(t3)
    SIZE += 1
    distances = temp
    if not is_continue():
        break
for gr in groups:
    gr.append(0)
draw_result(groups)
