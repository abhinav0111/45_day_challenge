class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = [0]*2
        f = 0
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    l[0] = i
                    l[1] = j
                    f = 1
                    break
            if f == 1:
                break
        return l
