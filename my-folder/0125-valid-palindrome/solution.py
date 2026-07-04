class Solution:
    def isPalindrome(self, s: str) -> bool:
        s.lower()
        start = 0
        end = len(s) - 1
    
        s = s.lower()
        if(len(s) == 1):
            return True
    
        while start <= end:
            if(not(s[end].isalnum())):
                end -= 1
            elif(not(s[start].isalnum())):
                start += 1
            elif(s[start] != s[end]):
                return False
            else:
                start += 1
                end -= 1
        return True

    
    
