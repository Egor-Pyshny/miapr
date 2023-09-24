import math
import random

import numpy as np
import matplotlib.pyplot as plt

PointsCount = 1000
points1 = [0] * PointsCount
points2 = [0] * PointsCount
result1 = [0] * PointsCount
result2 = [0] * PointsCount
mx1 = 0
mx2 = 0
sigma1 = 0
sigma2 = 0
pc1 = 0.5
pc2 = 1 - pc1

for i in range(PointsCount):
    points1[i] = random.randint(100, 740)
    points2[i] = random.randint(-100, 540)
    mx1 += points1[i]
    mx2 += points2[i]

mx1 /= PointsCount
mx2 /= PointsCount

for i in range(PointsCount):
    sigma1 += (points1[i] - mx1) ** 2
    sigma2 += (points2[i] - mx2) ** 2

sigma1 = math.sqrt(sigma1 / PointsCount)
sigma2 = math.sqrt(sigma2 / PointsCount)
result1[0] = (np.exp(-0.5 * ((0 - mx1) / sigma1) ** 2) /
                 (sigma1 * np.sqrt(2 * np.pi)) * pc1)

result2[0] = (np.exp(-0.5 * ((0 - mx2) / sigma2) ** 2) /
             (sigma2 * np.sqrt(2 * np.pi)) * pc2)
d = 1000
for i in range(1, PointsCount):
    result1[i] = (np.exp(-0.5 * ((i - mx1) / sigma1) ** 2) /
                 (sigma1 * np.sqrt(2 * np.pi)) * pc1)

    result2[i] = (np.exp(-0.5 * ((i - mx2) / sigma2) ** 2) /
                 (sigma2 * np.sqrt(2 * np.pi)) * pc2)

    if np.abs(result1[i] - result2[i]) < d:
        d = np.abs(result1[i] - result2[i])
        ind = i


d = ind
error1 = np.sum(result2[:int(d)])
error2 = np.sum(result2[int(d):]) if pc1 > pc2 else np.sum(result1[int(d):])
x = [d, d]
y = [0, 0.0015]
plt.plot(x, y, color='green')
plt.plot(result1, color='blue')
plt.plot(result2, color='red')
plt.show()
print('Зона ложной тревоги = '+str(error1)+
      '\nЗона пропуска обнаружения = '+str(error2)+
      '\nСуммарная ошибка классификации = '+str(error1+error2))
