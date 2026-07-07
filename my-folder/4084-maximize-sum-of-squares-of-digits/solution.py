class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if(sum > num*9 or sum < 0):
            return ""
        res = ""
        for i in range(num):
            digit = min(9,sum)
            res = res + str(digit)
            sum -= digit
        return res
            
