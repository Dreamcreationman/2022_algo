def max_recur(data, l, r):
    if l == r:
        return data[l]
    m = l + ((r - l) >> 1)
    l_max = max_recur(data, l, m)
    r_max = max_recur(data, m + 1, r)
    return l_max if l_max > r_max else r_max


print(max_recur([5, 3,2, 3,1,3,2,3], 0, 4)) # 时间复杂度 O(N)

"""
求递归时间复杂度的Master公式：
T(N) = a T(N/b) + O(N^d)

如果 log_b^a < d -----> 时间复杂度为 O(N^d)
如果 log_b^a > d -----> 时间复杂度为 O(N^(log_b^a))
如果 log_b^a = d -----> 时间复杂度为 O(Nlog N)
"""