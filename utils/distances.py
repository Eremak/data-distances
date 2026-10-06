def manhattan(a, b):
    d_x = b[0] - a[0]
    d_y = b[1] - a[1]

    distance = abs(d_x) + abs(d_y)
    return distance


manhattan((1, 1), (4, 5))

def euclidean(a, b):
    d_x = (b[0]**2 - a[0]**2)
    d_y = (b[1]**2 - a[1]**2)

    distance = (d_x + d_y)**0.5
    return distance
