class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = 0
        i = 0
        n = len(nums)
        while(i < n):
            if nums[i] == 0:
                c += 1
                nums.pop(i)
                n -= 1
            else:
                i += 1
        nums += [0]*c
