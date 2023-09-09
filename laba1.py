import datetime
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt, pow

num_points = 10000
classes = 9


def distance(x1, y1, x2, y2) -> float:
    return sqrt(pow(x1-x2, 2)+pow(y1-y2, 2))


def cmp(arr1, arr2):
    delta = 0.0000
    for i in range(classes):
        temp = abs(arr1[i] - arr2[i])
        if temp > delta:
            return False
    return True


def draw(clusters, centers):
    colors = ['red', 'green', 'blue', 'orange', 'purple', 'yellow', 'cyan', 'grey', 'Indigo']
    for i, cluster in enumerate(clusters):
        cluster = np.array(cluster)
        plt.scatter(cluster[:, 0], cluster[:, 1], c=colors[i], s=20)
    plt.scatter(centers[:, 0], centers[:, 1], c='black', s=50)
    plt.show()


def make_clusters(points, centers):
    clusters = [[] for i in range(classes)]
    for point in points:
        distances = [distance(point[0], point[1], center[0], center[1]) for center in centers]
        cluster_index = np.argmin(distances)
        clusters[cluster_index].append(point)
    return clusters


def KMeans():
    points = np.random.rand(num_points, 2)
    centers = np.random.rand(classes, 2)
    clusters = make_clusters(points, centers)
    draw(clusters, centers)
    while True:
        old_center_x = [a for a in centers[:, 0]]
        old_center_y = [a for a in centers[:, 1]]
        for i in range(classes):
            sum_x = 0
            sum_y = 0
            for (x, y) in clusters[i]:
                sum_x += x
                sum_y += y
            centers[i, 0] = (sum_x / len(clusters[i]))
            centers[i, 1] = (sum_y / len(clusters[i]))
        clusters = make_clusters(points, centers)
        if cmp(old_center_x, centers[:, 0]) and cmp(old_center_y, centers[:, 1]):
            break
    draw(clusters, centers)


print(str(datetime.datetime.now()))
KMeans()
print(str(datetime.datetime.now()))
