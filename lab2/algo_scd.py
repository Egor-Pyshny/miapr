from config import *
from random import random
import math
import numpy as np


def get_random_centers(in_vectors: np.ndarray, clusters_count):
    centers = np.zeros((clusters_count, 2))
    for i in range(clusters_count):
        center_found = False
        while not center_found:
            new_center = in_vectors[math.floor(random()*VECTORS_COUNT)]
            if not new_center in centers:
                centers[i] = new_center
                center_found = True
    return centers

def get_area_vectors(vectors: np.ndarray, areas: np.ndarray, filter_area: np.int32):
    result_list = []
    for vi, v in enumerate(vectors):
        if areas[vi] == filter_area:
            result_list.append(v)
    return np.array(result_list)


def calculate_centers(in_vectors: np.ndarray, areas: np.ndarray, clusters_count):
    centers = np.zeros((clusters_count, 2))
    for area in range(clusters_count):
        area_vectors = get_area_vectors(in_vectors, areas, area)
        mean_vector = area_vectors.mean(0)
        centers[area] = mean_vector
    return centers


def distance(a: tuple, b: tuple):
    return np.linalg.norm(np.array(a) - np.array(b))


def get_areas(vectors: np.ndarray, centers: np.ndarray):
    areas = np.zeros(VECTORS_COUNT)
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
