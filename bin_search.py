"""This project illustrates that binary search is more efficient than linear search"""

import random
import time


def linear_search(lst, key):
    n = len(lst)
    for i in range(n):
        if lst[i] == key:
            return i
    return -1


def bin_search(lt, key):
    low = 0
    high = len(lt) - 1
    while low <= high:
        mid = (low + high)//2
        if lt[mid] == key:
            return mid
        elif key < lt[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


if __name__ == '__main__':
    length = 10000
    lst = set()
    while len(lst) < length:
        lst.add(random.randint(-3*length, 3*length))
    lst = sorted(list(lst))

    start = time.time()
    for key in lst:
        linear_search(lst, key)
    end = time.time()
    print("Linear search time", (end - start), "seconds")

    start = time.time()
    for key in lst:
        bin_search(lst, key)
    end = time.time()
    print("Binary search time", (end - start), "seconds")

