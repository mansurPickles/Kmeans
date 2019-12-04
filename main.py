import pandas as pd
from scipy.io import loadmat
from matplotlib import pyplot as plt
import numpy as np
import math as mt

def distance(p1, p2):
    x1 = p1[0]
    x2 = p2[0]
    y1 = p1[1]
    y2 = p2[1]

    x = pow((x1-x2),2)
    y = pow((y1-y2),2)

    return mt.sqrt(x+y)

def reader():
    data = loadmat("kmeansdata.mat")
    points = data['X']
    return points

def move_centroid(points, groupings, num_centroid):
    new_centroid = [0,0]*num_centroid
    size = [0]*num_centroid
    next_centroid = [0,0]*num_centroid

    for i in range(len(points)):
        point = points[i]
        grouping = groupings[i]

        new_centroid[grouping] += point
        size[grouping] += 1
        # print(f' grouping{grouping} : {new_centroid[grouping]}')
    # return new_centroid
    # print(np.shape(new_centroid))
    # return new_centroid
    # print(new_centroid)


    # print(len(size))
    for i in range(len(size)):
        pt = new_centroid[i]
        x = pt[0]/size[i]
        y = pt[1]/size[i]

        # print(f'x:{x}  y:{y}')
        next_centroid[i] = [x,y]


    #
    # print('*'*20)
    # print(next_centroid)
    return next_centroid


def plot(points, centroid, groupings):

    x = []
    y = []
    centx = []
    centy = []

    for point in points:
        x.append(point[0])
        y.append(point[1])

    for cent in centroid:
        centx.append(cent[0])
        centy.append(cent[1])

    plt.scatter(x,y, color = 'blue')
    plt.scatter(centx,centy, color = 'red')

    plt.show()

def plot2(points, centroid, groupings):
    num_grouping = len(centroid)

    x1 = []
    y1 = []
    x2 = []
    y2 = []
    x3 = []
    y3 = []

    centx = []
    centy = []


    for i in range(len(points)):
        point = points[i]
        index = grouping[i]

        if (index == 0):
            x1.append(point[0])
            y1.append(point[1])

        if (index == 1):
            x2.append(point[0])
            y2.append(point[1])

        if (index == 2):
            x3.append(point[0])
            y3.append(point[1])

    for cent in centroid:
        centx.append(cent[0])
        centy.append(cent[1])
    plt.scatter(x1,y1, color = 'blue')
    plt.scatter(x2,y2, color = 'red')
    plt.scatter(x3,y3, color = 'green')

    plt.scatter(centx,centy, color = 'black')
    #
    plt.show()

def get_best_cand(cand):
    index = 0
    best = mt.inf
    for i in range(len(cand)):
        if (cand[i] <= best):
            index = i
            best = cand[i]
    return index


def K_means(points):
    iteration  = 10
    centroid = np.array([[3.0,3.0], [6.0,2.0], [8.0,5.0]])
    size = len(points)

    for it in range(iteration):
    #=======================
        grouping = np.array([-1]* size)
        cand = []
        index = 0

        for point in points:

            for cent in centroid:
                temp = distance(point,cent)
                cand.append(temp)

            grouping[index] = get_best_cand(cand)
            index += 1
            cand.clear()

        # print(grouping)
        temp = move_centroid(points,grouping,3)
        centroid[0] = temp[0]
        centroid[1] = temp[1]
        centroid[2] = temp[2]

        # print(temp)
        print(centroid)
        print('==='*20)

    return centroid, grouping


points = reader()
centroid,grouping = K_means(points)

plot2(points,centroid, grouping)


