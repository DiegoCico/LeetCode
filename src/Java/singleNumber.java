class Solution {
    public int singleNumber(int[] nums) {
        List<Integer> list = new ArrayList<Integer>();

        for(int num : nums) {
            if (!list.contains(num)) {
                list.add(num);
            } else {
                list.remove(Integer.valueOf(num));
            }
        }

        return list.get(0);

    }
}