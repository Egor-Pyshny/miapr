import datetime
import random

import matplotlib.pyplot as plt
import numpy as np
from math import sqrt, pow

num_points = 10000
classes = 0

def distance(x1, y1, x2, y2) -> float:
    return sqrt(pow(x1-x2, 2)+pow(y1-y2, 2))


def maxind(arr):
    max = 0
    ind = 0
    for i,j in enumerate(arr):
        if i>max:
            max = i
            ind = j
    return ind


def dist_centers(centers):
    dist = 0
    i=0
    j=0
    for center1 in centers:
        j=0
        for center2 in centers:
            dist += distance(center1[0],center1[i,1],center2[j,0],center2[j,1])
            ++j
        ++i
    return dist/(2*len(centers))


def minmax():
    classes = 1
    points = np.random.rand(num_points, 2)
    centers = np.array(random.sample(list(points), classes))
    maxes = [0 for i in range(classes)]
    indexes = [0 for i in range(classes)]
    for i in range(classes):
        ind = 0
        for point in points:
            dist = distance(point[0],point[1], centers[i,0], centers[i,1])
            if dist>maxes[i]:
                maxes[i] = (dist)
                indexes[i] = ind
            ++ind
    index = indexes[maxind(maxes)]
    max_dist = maxes[maxind(maxes)]
    ++classes
    np.append(centers, points[ind])
    np.delete(points, ind)
    while dist_centers(centers)<max_dist:
        maxes = [0 for i in range(classes)]
        clusters = make_clusters(points, centers)
        indexes = [0 for i in range(classes)]
        for i in range(classes):
            ind = 0
            for point in clusters[i]:
                dist = distance(point[0], point[1], centers[i, 0], centers[i, 1])
                if dist > maxes[i]:
                    maxes[i] = (dist)
                    indexes[i] = ind
                ++ind
        index = indexes[maxind(maxes)]
        max_dist = maxes[maxind(maxes)]
        ++classes
        np.append(centers, points[ind])
        np.delete(points, ind)


# compare new centers and old centerd
def cmp(arr1, arr2) -> bool:
    delta = 0.0000
    for i in range(classes):
        temp = abs(arr1[i] - arr2[i])
        if temp > delta:
            return False
    return True


# draw points
def draw(clusters, centers) -> None:
    colors = ['red', 'green', 'blue', 'orange', 'purple', 'yellow', 'cyan', 'grey', 'Indigo', 'pink']
    for i, cluster in enumerate(clusters):
        cluster = np.array(cluster)
        plt.scatter(cluster[:, 0], cluster[:, 1], c=colors[i], s=20)
    plt.scatter(centers[:, 0], centers[:, 1], c='black', s=50)
    plt.show()


# group points into clusters
def make_clusters(points, centers) -> list:
    clusters = [[] for i in range(classes)]
    for point in points:
        distances = [distance(point[0], point[1], center[0], center[1]) for center in centers]
        cluster_index = np.argmin(distances)
        clusters[cluster_index].append(point)
    return clusters


# group points using k-Means method
def k_means() -> None:

    # generate random points & centers
    points = np.random.rand(num_points, 2)
    centers = np.random.rand(classes, 2)

    # make first clusters
    clusters = make_clusters(points, centers)

    # draw first picture
    draw(clusters, centers)
    while True:
        old_center_x = [a for a in centers[:, 0]]
        old_center_y = [a for a in centers[:, 1]]

        # computing new centers
        for i in range(classes):
            sum_x = 0
            sum_y = 0
            for (x, y) in clusters[i]:
                sum_x += x
                sum_y += y
            centers[i, 0] = (sum_x / len(clusters[i]))
            centers[i, 1] = (sum_y / len(clusters[i]))

        # remake clusters with new centers
        clusters = make_clusters(points, centers)

        # compare old and new centers
        if cmp(old_center_x, centers[:, 0]) and cmp(old_center_y, centers[:, 1]):
            break

    # draw resulting picture
    draw(clusters, centers)


minmax()
classes = 8
print(str(datetime.datetime.now()))
k_means()
print(str(datetime.datetime.now()))
