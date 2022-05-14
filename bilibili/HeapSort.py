def heap_insert(arr, idx):
    while arr[idx] > arr[int((idx - 1) / 2)]:
        arr[idx], arr[int((idx - 1) / 2)] = arr[int((idx - 1) / 2)], arr[idx]
        idx = int((idx - 1) / 2)


def heapify(arr, idx, heap_size):
    left = 2 * idx + 1
    while left < heap_size:
        largest = 2 * idx + 2 if 2 * idx + 2 < heap_size and arr[2 * idx + 2] > arr[2 * idx + 1] else 2 * idx + 1
        largest = largest if arr[largest] > arr[idx] else idx
        if largest == idx:
            break
        arr[largest], arr[idx] = arr[idx], arr[largest]
        idx = largest
        left = 2 * idx + 1


def sort(data):
    if data is None or len(data) < 2: return data
    # for i in range(len(data)):
    #     heap_insert(data, i)
    i = len(data) - 1
    while i >= 0:
        heapify(data, i, len(data))
        i -= 1
    heap_size = len(data) - 1
    data[heap_size], data[0] = data[0], data[heap_size]
    while heap_size > 0:
        heapify(data, 0, heap_size)
        heap_size -= 1
        data[heap_size], data[0] = data[0], data[heap_size]


data = [5, 3,2, 3,1,3,2,3]
sort(data)
print(data)

"""
i位置左孩子 2 * i + 1，右孩子 2 * i + 2，其父节点 (i - 1) / 2
堆排序时间复杂度 O(NlogN), 空间复杂度 O(1) 在时间复杂度 O(NlogN)的排序算法中（归并，快排，堆排），堆排的空间复杂度最低
"""