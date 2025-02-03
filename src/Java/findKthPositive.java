class Solution {
    public int findKthPositive(int[] arr, int k) {
        List<Integer> list = new ArrayList<Integer>();
        int counter = 1; 
        for (int num : arr) {
            if (num == counter) {
                counter++;
                continue;
            }

            while (counter != num) {
                list.add(counter);
                counter++;
            }

            if(list.size() > k){
                break;
            }
            counter++;
        } 

        if (list.size() < k) {
            return arr[arr.length-1] + k - list.size();
        } else {
            return list.get(k-1);
        }
    }
}