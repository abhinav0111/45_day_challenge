class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        k1 = sum(list(set(nums)))
        n = len(nums)
        n1 = len(list(set(nums)))
        return (sum(nums)-k1)//(n-n1)
