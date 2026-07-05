/* 65 - 90(A-Z)
   97 - 122(a-z)
   48 - 57(0-9)
*/
class Solution {

    private boolean isAlNum(char c) {
        return Character.isLetterOrDigit(c);
    }

    public boolean isPalindrome(String s) {
        int start = 0, end = s.length() - 1;
        s = s.toLowerCase();
        if(s.length() == 1) return true;
        while(start <= end) {
            if (!isAlNum(s.charAt(start))) start++;
            else if (!isAlNum(s.charAt(end))) end--;
            else if (s.charAt(start) != s.charAt(end)) return false;
            else{
                start++;
                end--;
            }
        }
        return true;
    }
}
