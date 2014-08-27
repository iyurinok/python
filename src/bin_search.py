__author__ = 'e21349'


def inc_dec_search(arr, k):
    pass


def rotated_search(arr, k):
    def search_util(lo, hi):
        if lo >= hi:
            return hi if arr[hi] == k else -1
        mid = (hi + lo) / 2
        if arr[mid] == k:
            return mid
        # elif
        return -1

    print list(enumerate(arr))
    return search_util(0, len(arr) - 1)


def bin_search(arr, k):
    def search_util(lo, hi):
        if lo >= hi:
            return hi if arr[hi] == k else -1
        mid = (hi + lo) / 2
        if arr[mid] == k:
            return mid
        elif arr[mid] > k:
            return search_util(lo, mid - 1)
        else:
            return search_util(mid + 1, hi)

    print arr
    return search_util(0, len(arr) - 1)


test_array = range(10)
#print bin_search(test_array, 11)

offset = 3
print rotated_search(test_array[offset:] + test_array[:offset], 8)
