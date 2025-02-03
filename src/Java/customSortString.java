import java.util.HashMap;
import java.util.Map;

class Solution {
    public String customSortString(String order, String s) {
        Map<Character, Integer> freqMap = new HashMap<>();
        for (char c : s.toCharArray()) {
            freqMap.put(c, freqMap.getOrDefault(c, 0) + 1);
        }

        StringBuilder result = new StringBuilder();
        for (char c : order.toCharArray()) {
            if (freqMap.containsKey(c)) {
                int count = freqMap.get(c);
                for (int i = 0; i < count; i++) {
                    result.append(c);
                }
                freqMap.remove(c);
            }
        }

        for (Map.Entry<Character, Integer> entry : freqMap.entrySet()) {
            char leftoverChar = entry.getKey();
            int count = entry.getValue();
            for (int i = 0; i < count; i++) {
                result.append(leftoverChar);
            }
        }
        return result.toString();
    }
}
