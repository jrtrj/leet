class Solution {
    public void moveZeroes(int[] nums) {
       int l = 0;
       for(int r = 0; r<nums.length; r++) {
        if(nums[r] != 0 && nums.length != 1) {
            nums[l] = nums[l]+nums[r]-(nums[r]=nums[l]);
            l++;
        }
       }
    }
}
