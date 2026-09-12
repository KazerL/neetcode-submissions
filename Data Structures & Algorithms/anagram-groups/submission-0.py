from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupMap = defaultdict(list)
        outputList = []

        index = 0

        for word in strs:
            # break the word down
            broken = list(word)
            broken.sort()
            fix = "".join(broken)
            
            # adds grouped anagrams with 
            groupMap[fix].append(word)
            
            index += 1

        # stores all the grouped words in an output list    
        for entry in groupMap:
            outputList.append(groupMap[entry])

        return outputList










            