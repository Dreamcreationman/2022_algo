import random


def partition(arr, l, r):
    less, more = l - 1, r
    while l < more:
        if arr[l] < arr[r]:
            less += 1
            arr[less], arr[l] = arr[l], arr[less]
            l += 1
        elif arr[l] == arr[r]:
            l += 1
        else:
            more -= 1
            arr[more], arr[l] = arr[l], arr[more]
    arr[more], arr[r] = arr[r], arr[more]
    return less+1, more


def quicksort(arr, l, r):
    if l < r:
        pos = l + int(random.random() * (r - l + 1))
        arr[pos], arr[r] = arr[r], arr[pos]
        left, right = partition(arr, l, r)
        quicksort(arr, l,  left - 1)
        quicksort(arr, right + 1, r)


def sort(data):
    # https://leetcode-cn.com/problems/sort-an-array/
    if data is None or len(data) < 2: return data
    quicksort(data, 0, len(data) - 1)


data = [5,1,1,2,0,0]
sort(data)
print(data)

"""
快排空间复杂度 O(logN)
"""