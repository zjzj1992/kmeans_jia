import math
import random


def euler_distance(a,b):
    '''
    Calculate the distance between two points

    '''
    distance = 0.0
    for a,b in zip(a,b):
        distance += math.pow(a - b,2)
    return math.sqrt(distance)


def get_closest_dist(point,centroids):
    '''
    Returns the shortest distance
    between the sample and the centroid.

    '''
    
    min_dist = math.inf
    for i,centroid in enumerate(centroids):
        dist = euler_distance(centroid,point)
        if dist < min_dist:
            min_dist = dist
    return min_dist


def choose_center(dataSet,k):
    '''
    Select k centroid from data set

    '''
    
    cluster_centers = []
    cluster_centers.append(random.choice(dataSet))
    d = [0 for _ in range(len(dataSet))]
    for _ in range(1,k):
        total = 0.0
        for i,point in enumerate(dataSet):
            d[i] = get_closest_dist(point,cluster_centers)
            total += d[i]
        total *= random.random()
        for i,di in enumerate(d):
            total -= di
            if total > 0:
                continue
            cluster_centers.append(dataSet[i])
            break
    return cluster_centers

