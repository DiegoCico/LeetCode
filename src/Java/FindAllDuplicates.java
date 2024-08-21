class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        if (nums.length <= 1)
            return List.of();
        List<Integer> duplicates = new ArrayList<>();
        for(int i = 0; i < nums.length-1; i++){
            for(int j = i +1; j<nums.length; j++){
                if (nums[i] == nums[j]){
                    duplicates.add(nums[i]);
                    break;
                }
            }
        }
        return duplicates;
    }
}