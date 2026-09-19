class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charMap = {}
        left = 0
        right = 0
        longest = 0
        tempLongest = 0
        
        while right < len(s):
            if s[right] not in charMap:
                charMap[s[right]] = 1
            else:
                charMap[s[right]] += 1

            # valid window check
            freqChar = max(charMap, key = charMap.get) 
            currWindow = right - left + 1

            if currWindow - charMap[freqChar] <= k:
                longest = max(longest, currWindow)
                right += 1
                continue
            else:
                charMap[s[left]] -= 1
                left += 1
                right += 1
                continue

        return longest