class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start = 0
        peak = 0
        end = len(nums) - 1
        if len(nums) == 1:
            return 0
        while(start <= end):
            if(nums[start] > nums[peak]):
                peak = start
            if(nums[end] > nums[peak]):
                peak = end
            start+=1
            end-=1
        return peak
