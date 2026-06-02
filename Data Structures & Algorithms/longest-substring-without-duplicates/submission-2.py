class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = [-1] * 128  # ASCII
        left = 0
        ans = 0

        for right, ch in enumerate(s):
            idx = ord(ch)

            if last[idx] >= left:
                left = last[idx] + 1

            last[idx] = right
            ans = max(ans, right - left + 1)

        return ans            