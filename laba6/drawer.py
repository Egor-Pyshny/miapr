from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram

def draw_result(linkage_matrix):
    dendrogram(linkage_matrix)
    plt.show()

# draw_result([
#         [0,1,1.0,0],
#         [2,4,1.0,0],
#         [5,6,1.0,0],
#         [3,7,4.0,0],
#     ])