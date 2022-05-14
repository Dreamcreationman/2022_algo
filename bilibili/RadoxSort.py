def getDigit(num, d, radix=10):
    while True:
        if d== 0:
            return num % radix
        num = num // radix
        d -= 1


def sort(data, l, r, digit=9):
    """
    :param data:
    :param l:
    :param r:
    :param digit: 最大值有多少个十进制为
    :return:
    """
    radix = 10 # 基底
    bucket = [0] * (r - l + 1) # 辅助数组
    for d in range(digit): # 最大值有多少个位就有多少次出入桶
        count = [0] * radix # 桶
        for i in range(l, r+1):
            j = getDigit(data[i], d, radix)
            count[j] += 1
        for i in range(1, len(count)): # 将计数变成累加和数组
            count[i] += count[i-1]
        i = r
        while i >= l:
            j = getDigit(data[i], d, radix)
            bucket[count[j] - 1] = data[i]
            count[j] -= 1
            i -= 1
        data[l:r+1] = bucket[0:]


data = [5,2,3,1]
sort(data, 0, len(data)-1)
print(data)