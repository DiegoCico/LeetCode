class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        for word in strs:
            sort_word = "".join(sorted(word))
            map[sort_word].append(word)
        return list(map.values())