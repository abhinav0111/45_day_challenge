class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # k1=list(set(nums))
        # n=len(k1)
        # k1=k1+[]*(len(nums)-len(k1))
        # nums=k1
        # print(nums)
        # return n
        x = 1
        for i in range(len(nums)-1):
            if(nums[i] != nums[i+1]):
                nums[x] = nums[i+1]
                x += 1
        return(x)
