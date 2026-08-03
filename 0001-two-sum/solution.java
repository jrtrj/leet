import java.util.HashMap;
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int n = nums.length;
        var map = new HashMap<Integer,Integer>();
        for(int i = 0; i < n; i++) {
            int complement = target - nums[i];
            if(map.containsKey(complement)) {
                return new int[]{i,map.get(complement)};
            }
            map.put(nums[i],i);
        }
        return new int[]{-1,-1};
    }
}
