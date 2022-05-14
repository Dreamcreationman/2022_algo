def sort(data):
    if len(data) < 2 or data is None:
        return data
    for i in range(len(data)):
        minIdx = i
        for j in range(i+1, len(data)):
            minIdx = j if data[j] < data[minIdx] else minIdx
        data[i], data[minIdx] = data[minIdx], data[i]
    return data


print(sort([5, 3,2, 3,1,3,2,3]))