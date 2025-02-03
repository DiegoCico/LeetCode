class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> list = new HashMap<>();
        for (int num : nums) {
            if (list.containsKey(num)) {
                list.put(num, list.get(num) + 1);
            } else {
                list.put(num, 1);
            }
        }

        List<Integer> keys = new ArrayList<>(list.keySet());
        int[] result = new int[k];
        
        for (int i = 0; i < k; i++) {
            int maxKey = keys.get(0);

            for (int j = 1; j < keys.size(); j++) {
                int candidateKey = keys.get(j);
                if (list.get(candidateKey) > list.get(maxKey)) {
                    maxKey = candidateKey;
                }
            }

            result[i] = maxKey;

            keys.remove(Integer.valueOf(maxKey));
        }

        return result;
    }
}