def k_means_centroid_update(points, assignments, k):
    """
    Compute new centroids as the mean of assigned points.
    """
    centroid = []
    for cluster in range(k):
        sums = [points[i] for i in range(len(points)) if assignments[i] == cluster]
        n = len(sums)

        if n == 0:
            centroid.append([0] * len(points[0]))
        else:
            sums = [sum(coords)/n for coords in zip(*sums)]
            centroid.append(sums)
    return centroid