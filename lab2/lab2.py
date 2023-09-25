import time
import numpy as np
import matplotlib.pyplot as plt
from random import random
import math
from config import *
from algo import *
import algo_scd as algo_scd


def draw(vectors: np.ndarray, colors: np.ndarray, centers: list):
    plt.clf()
    vx = [v[0] for v in vectors]
    vy = [v[1] for v in vectors]
    plt.scatter(vx, vy, s=10, color=colors)

    cx = [c[0] for c in centers]
    cy = [c[1] for c in centers]
    plt.scatter(cx, cy, s=20, color='red')

    plt.show()
    plt.pause(0.2)

plt.ion()

vectors = np.array([ (random()*HAFL_WIDTH, random()*HAFL_WIDTH) for i in range(VECTORS_COUNT) ])
centers = [ pick_random_vector(vectors) ]
areas, colors = get_areas(vectors, centers)

draw(vectors, colors, centers)

new_center = pick_most_far_vector(vectors, centers[0])
centers.append(new_center)
areas, colors = get_areas(vectors, centers)

while True:
    draw(vectors, colors, centers)
    new_center = get_new_center(vectors, centers, areas)
    print(new_center)
    if type(new_center) == type(None):
        break

    centers.append(new_center)
    areas, colors = get_areas(vectors, centers)

centers = np.array(centers)
new_centers = centers

centers_were_changed = True
limit = 100
while centers_were_changed and limit>0:
    draw(vectors, colors, centers)
    time.sleep(1.0)
    --limit
    centers = new_centers
    areas, colors = get_areas(vectors, centers)
    new_centers = algo_scd.calculate_centers(vectors, areas, len(centers))
    centers_were_changed = not np.array_equal(centers, new_centers)

draw(vectors, colors, centers)

plt.ioff()
