class Solution(object):
    def findPeakElement(self, nums):
        low = 1
        high = len(nums) - 2
        
        if len(nums)==1:
            return 0
        elif nums[0]>nums[1] :
            return 0
        elif nums[len(nums)-1]>nums[len(nums)-2] :
            return len(nums)-1

        while(low <= high):
            mid = (low+high)//2
            if(nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]):
                return mid
            elif(nums[mid] < nums[mid+1]): #right
                low = mid + 1
            elif(nums[mid] < nums[mid-1]): #left
                high = mid - 1
        return -1   
            
