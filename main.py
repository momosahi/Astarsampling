""" Implementation of the paper A* Sampling """


import numpy as np


class AStarSampler:
    pass


def gumbel_sample(x):
    """return an independant sample from Gumbel distribution with location 0 and scale 1"""
    return np.random.gumbel(loc=0, scale=1, size=x.shape)
