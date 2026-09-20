class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # pointers
        left = 0
        right = 0
        minLeft = 0
        minRight = 0

        # var
        shortWindow = len(s) + 1

        # break conditon
        if len(s) < len(t):
            return ""

        # hashmaps
        tMap = {}
        sMap = {}

        # comparison nums
        have = 0
        need = 0

        for char in t:
            tMap[char] = tMap.get(char, 0) + 1
            need += 1
    
        while right <= len(s):
            if have == need:
                currWindow = right - left
                
                if currWindow < shortWindow:
                    shortWindow = currWindow
                    minLeft = left
                    minRight = right 

                if s[left] in tMap:
                    sMap[s[left]] -= 1
                    if sMap[s[left]] < tMap[s[left]]:
                        have -= 1
                
                left += 1
                continue
            
            if right == len(s):
                break

            if s[right] in tMap:
                sMap[s[right]] = sMap.get(s[right], 0) + 1

                if sMap[s[right]] <= tMap[s[right]]:
                    have += 1

            right += 1

        if shortWindow == len(s) + 1:
            return ""
        else:
            return s[minLeft:minRight]


            
           

                    
                    

                    


            
