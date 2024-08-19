class Solution {
    public int lengthOfLongestSubstring(String s) {
        String lon = "";
        int longest = 0;
        
        for (char c : s.toCharArray()) {
            if (!lon.contains(Character.toString(c))) {
                lon += c; 
            } else {
                if (longest < lon.length()) {
                    longest = lon.length();
                }
                
                lon = lon.substring(lon.indexOf(c) + 1) + c;
            }
        }
        
        if (longest < lon.length()) {
            longest = lon.length();
        }

        return longest;
    }
}
