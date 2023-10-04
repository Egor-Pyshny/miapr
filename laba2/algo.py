from config import *
from random import random
import math
import numpy as np


def pick_random_vector(vectors: np.ndarray):
    return vectors[math.floor(random()*VECTORS_COUNT)]

def pick_most_far_vector(vectors: np.ndarray, center: np.ndarray):
    distances = distance_array(vectors, np.full((VECTORS_COUNT, 2), center))
    index = np.argmax(distances)
    return vectors[index]

def get_area_vectors(vectors: np.ndarray, areas: np.ndarray, filter_area: np.int32):
    result_list = []
    for vi, v in enumerate(vectors):
        if areas[vi] == filter_area:
            result_list.append(v)
    return np.array(result_list)


def distance(a: np.ndarray, b: np.ndarray):
    return np.linalg.norm(np.array(a) - np.array(b))

def distance_array(a: np.ndarray, b: np.ndarray):
    distances = []
    len_a = len(a)
    for i in range(len_a):
        distances.append(distance(a[i], b[i]))
    return np.array(distances)



def get_areas(vectors: np.ndarray, centers: np.ndarray):
    areas = np.zeros(VECTORS_COUNT, dtype=np.int32)
    colors = np.zeros(VECTORS_COUNT, dtype=object)
    for vi, v in enumerate(vectors):
        type = 0
        min_distance = math.inf
        for ci, c in enumerate(centers):
            calc_distance = distance(v, c)
            if calc_distance < min_distance:
                min_distance = calc_distance
                type = ci
        areas[vi] = type
        colors[vi] = COLORS[type]
    return areas, colors

def avg_distance_between_all_centers(centers: np.ndarray):
    centers_len = len(centers)
    count = centers_len * (centers_len-1) / 2
    sum = np.float64(0.0)
    for i in range(centers_len):
        for j in range(i+1, centers_len):
            sum += distance(centers[i], centers[j])
    return sum / count

def get_new_center(vectors: np.ndarray, centers: np.ndarray, areas: np.ndarray):
    # get distances
    distances = np.zeros(VECTORS_COUNT)
    for vi, v in enumerate(vectors):
        c = centers[areas[vi]]
        distances[vi] = distance(v, c)
    
    # get max distances
    max_distances = np.zeros(len(centers))
    max_vector_ids = np.zeros(len(centers))
    for vi, v in enumerate(vectors):
        area = areas[vi]
        if max_distances[area] < distances[vi]:
            max_distances[area] = distances[vi]
            max_vector_ids[area] = vi
    
    pretendent_vector_distance = np.max(max_distances)
    pretendent_vector_id = np.int32(max_vector_ids[np.argmax(max_distances)])

    # get avg distance
    avg_distance = avg_distance_between_all_centers(centers)
    if pretendent_vector_distance > avg_distance / 2:
        return vectors[pretendent_vector_id]
    else:
        return None


    


