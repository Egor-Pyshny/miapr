import drawer

basic_coef = [1,4,4,16]
my_coef = [0,0,0,0]
my_prev_coef = [0,0,0,0]
data = [
    {
        "obj":[-1,1],
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
res = False
i = 0
sign=1
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
    i+=1
    if i==3:
        i=0
drawer.show_results(my_coef,data)