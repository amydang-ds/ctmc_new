import numpy as np
from scipy.optimize import fmin
import math

class Main(object):
    pass

def main():
    def f(x):
        exp = (math.pow(x[0], 2) + math.pow(x[1], 2)) * -1
        return math.exp(exp) * math.cos(x[0] * x[1]) * math.sin(x[0] * x[1])

    print(fmin(f, np.array([0, 1])))


if __name__ == '__main__':
    main()