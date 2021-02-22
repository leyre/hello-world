from math import tan, pi
def polysum(n, s):
    """
    n: any positive int
    s: any positive int
    returns: sum of both the area and the square of the perimiter of a polygon of n sides having length s
    """
    area = 0.25*(n*(s**2))/tan(pi/n)
    perimiter_square = (n*s)**2
    return round(area + perimiter_square, 4)
