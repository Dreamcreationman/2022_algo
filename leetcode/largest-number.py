import functools
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp(a, b):
            if a + b == b + a:
                return 0
            elif a + b < b + a:
                return 1
            else:
                return -1

        num_str = map(str, nums)
        res = sorted(num_str, key=functools.cmp_to_key(cmp))
        if res[0] == "0": return "0"
        return "".join(res)
