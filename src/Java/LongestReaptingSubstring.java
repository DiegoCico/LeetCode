class Solution {
    public int longestRepeatingSubstring(String S) {
	Set<String> set = new HashSet<>();
	int max = S.length() - 1, i = 0;
	for (;i <= S.length();i++) {
		int j = i;
		if (j + max > S.length()) {
			if (--max == 0) break;
			i = -1;
			set.clear();
			continue;
		}
		String k = S.substring(j,j+max);
		if (!set.add(k)) {
			return max;
		}
	}
	return max;
}
}