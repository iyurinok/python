from random import randrange

__author__ = 'iyurinok'


def rand_array(n):
    array = range(n)
    for i in range(1, n):
        rand = randrange(i)
        array[rand], array[i] = array[i], array[rand]
    return array


if __name__ == "__main__":
    print rand_array(10)