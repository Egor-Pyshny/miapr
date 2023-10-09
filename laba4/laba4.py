import random

attributes_amount = 3
classes_amount = 3
training_objects_amount = 1
weights = [[0 for i in range(0, attributes_amount+1)] for j in range(0, classes_amount)]
training_objects = []
c = 1


def generate_training_obj():
    training_objects.append(
        {
            "obj": [-1,-4,2],
            "class": 0,
        },
    )
    training_objects.append(
        {
            "obj": [2, -4,-5],
            "class": 1,
        },
    )
    training_objects.append(
        {
            "obj": [-5, 3, 0],
            "class": 2,
        },
    )
    for i in range(0, classes_amount):
        training_objects[i]["obj"].append(1)


def decisive_function(weight_t, temp) -> int:
    d_t = 0
    for i in range(0, attributes_amount+1):
        d_t+=(weight_t[i]*temp[i])
    return d_t


def decrease_weight(weight_ind, temp):
    for i in range(0, attributes_amount+1):
        weights[weight_ind][i] -= temp[i]


def increase_weight(weight_ind, temp):
    for i in range(0, attributes_amount+1):
        weights[weight_ind][i] += temp[i]


def reverse_any(iterable):
    for element in iterable:
        if not element:
            return False
    return True


generate_training_obj()
while True:
    correct_classification = []
    for i in range(0, len(training_objects)):
        d = []
        training_obj = training_objects[i]
        for weight in weights:
            d.append(decisive_function(weight_t=weight, temp=training_obj["obj"]))
        index = training_obj["class"]
        target_value = d[index]
        indexes_to_decrease = [i for i in range(0, classes_amount) if i != index and d[i] >= target_value]
        for ind in indexes_to_decrease:
            decrease_weight(ind, training_obj["obj"])
        if len(indexes_to_decrease) != 0:
            correct_classification.append(False)
            increase_weight(index, training_obj["obj"])
        else:
            correct_classification.append(True)
    if reverse_any(correct_classification):
        break

for j, w in enumerate(weights):
    res = f'd{j}(x) = '
    for i in range(0, attributes_amount):
        res += f'{w[i]}x{i}+'
    res += str(w[attributes_amount])
    print(res.replace('+-', '-'))
