class Solution {
    public int minAddToMakeValid(String s) {
        int changes = 0;
        int left = 0;
        for (char c : s.toCharArray()) {
            if (c == '(') {
                changes++;
                left++;
            } else {
                if (left > 0) {
                    left--;
                    changes--;
                } else {
                changes++;
                }
            }
        }
        return changes;
    }
}