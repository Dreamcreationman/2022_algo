def sort(data):
    if len(data) < 2 or data is None:
        return data
    j = len(data) - 1
    while j > 0:
        for i in range(j):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
        j -= 1
    return data


print(sort([5, 3,2, 3,1,3,2,3]))


"""
异或运算： 相同为0，不同为1         可以看成二进制的无进位相加
0^N=N N^N=0 

异或满足交换结合率

利用该性质，可以实现交换：
def swap(a, b):
    a = a ^ b 
    b = a ^ b 
    a = a ^ b 
    
但是a, b指向的内存区域不能相同，即如果是数组：i,j不能相等，不然会抹成0
"""