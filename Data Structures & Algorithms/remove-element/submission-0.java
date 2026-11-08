class Solution {
    public int removeElement(int[] nums, int val) {
        int len = nums.length;
        for(int i = 0; i < len; i++){
            if(nums[i] == val){
                for(int n = i; n < len - 1; n++){
                    nums[n] = nums[n+1];
                }
                len--;
                nums[len] = -1;
                i--;
            }
        }
        return len;
    }
}