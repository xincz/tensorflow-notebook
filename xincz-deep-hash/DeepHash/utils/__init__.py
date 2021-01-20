import numpy as np


def sign(x):
    """
    :param x: an ndarray
    :return: -1 if x < 0, 1 of x > 0, random -1 or 1 if x == 0
    """
    s = np.sign(x)
    temp = s[s == 0]
    s[s == 0] = np.random.choice([-1, 1], temp.shape)
    return s


if __name__ == "__main__":
    x = np.random.choice([-1, 0, 1], [5, 5])
    print(x)
    print((sign(x)))
