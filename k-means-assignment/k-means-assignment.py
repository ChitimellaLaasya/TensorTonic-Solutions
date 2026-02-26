import math

def k_means_assignment(points, centroids):
    """
    Assign each point to the nearest centroid.
    """
    clusters = []
    
    for p in points:
        minimum = []
        for c in centroids:
            distance = 0
            for d in range(len(p)):
                distance += (p[d] - c[d]) ** 2
            
            minimum.append([distance, c])
        
        clusters.append(min(minimum))

    c = []
    for l in clusters:
        for i in range(len(centroids)):
            if l[1] == centroids[i]:
                c.append(i)

    return c