# leetcode   https://leetcode.com/problems/sort-characters-by-frequency/description/

# 451. Sort Characters By Frequency


class Solution:
    def frequencySort(self, s: str) -> str:
        char_map = {}

        for ch in s:
            char_map[ch] = char_map.get(ch, 0) + 1

        buckets = [[] for _ in range(len(s) + 1)]

        for ch, freq in char_map.items():
            buckets[freq].append(ch)

        result = []

        for freq in range(len(s), 0, -1):
            for ch in buckets[freq]:
                result.append(ch * freq)

        return "".join(result)
