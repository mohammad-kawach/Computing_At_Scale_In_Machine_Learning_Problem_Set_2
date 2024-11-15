import multiprocessing # See https://docs.python.org/3/library/multiprocessing.html
import argparse # See https://docs.python.org/3/library/argparse.html
import random
from math import pi
from itertools import product

def sample_pi(n, seed):
    """ Perform n steps of Monte Carlo simulation for estimating Pi/4.
        Returns the number of sucesses."""
    random.seed(seed)
    print("Hello from a worker")
    s = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        if x**2 + y**2 <= 1.0:
            s += 1
    return s

### TODO: Add function below
def x():
    pass
### TODO: Add function above

def compute_pi(accuracy, workers, seed):
    ### TODO: Add/change code below
    random.seed(seed)
    n = int(steps / workers)
    seeds = [seed + i for i in range(workers)]

    for i in product([n], seeds):
        print(i)
    p = multiprocessing.Pool(workers)
    s = p.starmap(sample_pi, product([n], seeds))
    p.close()

    n_total = n*workers
    s_total = sum(s)
    pi_est = (4.0*s_total)/n_total
    print(" Steps\tSuccess\tPi est.\tError")
    print("%6d\t%7d\t%1.5f\t%1.5f" % (n_total, s_total, pi_est, pi-pi_est))
    ### TODO: Add/change code above
    return samples_per_second


if __name__ == "__main__":

    workers = 2
    seed = 0
    accuracy = 0.0001 # defined as the absolute difference between the estimated pi and pi 

    workers, samples_per_second = compute_pi(accuracy, workers, seed)
