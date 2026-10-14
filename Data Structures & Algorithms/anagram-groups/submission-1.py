class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}

        for word in strs:
            signiture = "".join(sorted(word))
            if signiture not in anagram_map:
                anagram_map[signiture] = []

            anagram_map[signiture].append(str(word))
        
        return list(anagram_map.values())





