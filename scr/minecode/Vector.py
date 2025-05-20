import math
import random

def vec_length(x, y, z):
    """Returns the magnitude of a vector."""
    return math.sqrt(x**2 + y**2 + z**2)

def addvecs(v1, v2):
    """Adds two vectors together."""
    return (v1[0] + v2[0], v1[1] + v2[1], v1[2] + v2[2])

def scalevec(vector, factor):
    """Scales the vector by a given factor."""
    return (vector[0] * factor, vector[1] * factor, vector[2] * factor)

def normalizevec(vector):
    """Returns a unit vector in the same direction."""
    length = vec_length(*vector)
    return (vector[0] / length, vector[1] / length, vector[2] / length) if length != 0 else (0, 0, 0)

def randvec(radius):
    """Generates a random vector within the given radius."""
    return (
        random.uniform(-radius, radius),
        random.uniform(-radius, radius),
        random.uniform(-radius, radius)
    )

def vec_dist(v1, v2):
    """Finds the distance between two vectors."""
    return math.sqrt((v1[0] - v2[0])**2 + (v1[1] - v2[1])**2 + (v1[2] - v2[2])**2)