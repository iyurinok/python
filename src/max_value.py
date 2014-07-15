from rand_array import rand_array

__author__ = 'iyurinok'


def max_value(arr):
    length = len(arr)
    if length == 1:
        return arr[0], []
    else:
        mid = length / 2
        l_max, l_compares = max_value(arr[:mid])
        r_max, r_compares = max_value(arr[mid:])
        return (l_max, l_compares + [r_max]) if l_max > r_max else (r_max, r_compares + [l_max])

if __name__ == "__main__":
    array = rand_array(1000)
    print array
    print max_value(array)