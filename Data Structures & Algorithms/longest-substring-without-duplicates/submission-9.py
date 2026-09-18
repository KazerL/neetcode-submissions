class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        left = 0
        right = 0
        largest = 0

        while right < len(s):
            while s[right] in window:
                window.remove(s[left])
                left += 1
            
            window.add(s[right])
            
            largest = max(largest, right - left + 1)
            right += 1

        return largest

        