from itertools import combinations


def pairs(iterable):
    return combinations(iterable, 2)


def get_linkage_matrix(distance_matrix):
    def distance(cluster1, cluster2):
        return min([distance_matrix[x][y] for x in cluster1 for y in cluster2])

    items_count = len(distance_matrix)
    result = []
    forest = [(i, [i]) for i in range(items_count)]
    for iteration in range(items_count - 1):
        uniting_clusters, new_distance = min((((a, b), distance(a[1], b[1])) for a, b in pairs(forest)), key=lambda x: x[1])
        new_cluster_items = uniting_clusters[0][1] + uniting_clusters[1][1]
        forest = [x for x in forest if x not in uniting_clusters]
        forest.append((items_count + iteration, new_cluster_items))
        result.append([uniting_clusters[0][0], uniting_clusters[1][0], new_distance, len(new_cluster_items)])
    return result