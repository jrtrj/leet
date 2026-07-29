class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current = 0
        maximum = 0
        for i in nums:
            if(i == 1):
                current += 1
            elif(i == 0):
                maximum = max(current, maximum)
                current = 0
        return max(maximum, current) #since there might not be zero at the end [1,1,0,1,1,1]
            
        
