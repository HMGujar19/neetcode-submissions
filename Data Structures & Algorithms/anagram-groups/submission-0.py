class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_anagrams = {}
        for item in strs:
            sorted_word = ''.join(sorted(item))
            if sorted_word in grouped_anagrams:
                grouped_anagrams[sorted_word].append(item)
            else:
                grouped_anagrams[sorted_word] = [item]
        return list(grouped_anagrams.values())