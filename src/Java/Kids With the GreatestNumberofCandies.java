class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        List<Boolean> list = new ArrayList<>(); 
        int small = Arrays.stream(candies).max().getAsInt();

        for (int candy : candies) {
            int c = candy + extraCandies;
            if (c >= small)
                list.add(true);
            else
                list.add(false);
        }

        return list;
    }
}