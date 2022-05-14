def merge(data, l, m, r):
    res = []
    i, j = l, m+1
    while i <= m and j <= r:
        if data[i] <= data[j]:
            res.append(data[i])
            i += 1
        else:
            res.append(data[j])
            j += 1
    if i <= m:
        res.extend(data[i:m+1])
    else:
        res.extend(data[j:r+1])
    for i in range(len(res)):
        data[l + i] = res[i]


def divide(data, l, r):
    if l == r:
        return
    m = l + ((r-l) >> 1)
    divide(data, l, m)
    divide(data, m+1, r)
    merge(data, l, m, r)


def sort(data):
    if data is None or len(data) < 2: return data
    divide(data, 0, len(data)-1)


data = [5, 3,2, 3,1,3,2,3]
sort(data)
print(data)