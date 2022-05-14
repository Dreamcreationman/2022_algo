def sort(data):
    if data is None or len(data) < 2:
        return data
    for i in range(len(data)):
        j = i - 1
        while j >= 0:
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
            else:
                break
            j -= 1
    return data


print(sort([5, 3,2, 3,1,3,2,3]))