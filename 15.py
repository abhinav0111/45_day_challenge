from collections import Counter


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        zd = dict(Counter(nums))
        z = list(zd.values())
        k = list(zd.keys())
        al = []
        for i in range(0, len(z)):
            if z[i] > 1:
                al.append(k[i])
        return al
