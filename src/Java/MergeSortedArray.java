

class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        ArrayList<Integer> arrayList = new ArrayList<>();

        insert(arrayList, nums1, m);
        insert(arrayList, nums2, n);

        arrayList.sort(null);

        for (int i = 0; i < m + n; i++) {
            nums1[i] = arrayList.get(i);
        }
    }

    public void insert(ArrayList<Integer> list, int[] num, int l) {
        for (int i = 0; i < l; i++) {
            list.add(num[i]);
        }
    }
}
