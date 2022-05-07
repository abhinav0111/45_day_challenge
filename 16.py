class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        width = len(height)-1
        res = 0
        for i in range(len(height)-1, 0, -1):
            if height[l] < height[r]:
                res = max(res, height[l] * i)
                l = l+1
            else:
                res = max(res, height[r] * i)
                r = r-1
        return res
