class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        map = {}
        count = 0
        finalOutput = []

        # iterate and add values to hash
        for entry in nums:
            # frequency logger
            if entry in map:
                map[entry] += 1
            else:
                map[entry] = 1

        # finds the k most frequent elements
        for count in range(k):
            freqKey = max(map, key=map.get)
            map.pop(freqKey)
            finalOutput.append(freqKey)
        
        return finalOutput



