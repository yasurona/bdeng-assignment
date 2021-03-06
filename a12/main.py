from setting import *
from dbscan import *
from assign_score import *


def main():
    points, epsilon, min_pts = setting()
    points, clusters = dbscan(points, epsilon, min_pts)
    assign_score(points, clusters)


if __name__ == '__main__':
    main()
