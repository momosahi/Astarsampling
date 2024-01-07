""" Implementation of the paper A* Sampling """


import numpy as np


class AStarSampler:
    pass


def gumbel_sample(mu):
    """return an independant sample from Gumbel distribution."""
    return np.log(-np.log(np.random.exponential())) + mu
