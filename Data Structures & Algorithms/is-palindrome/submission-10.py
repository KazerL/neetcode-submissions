class Solution:
    def isPalindrome(self, s: str) -> bool:
        unspaced = re.sub(r'[^A-Za-z0-9]', '', s).lower()

        if len(unspaced) == 0:
            return True 
        
        char = list(unspaced)

        pointer1 = 0
        pointer2 = len(char) - 1
        arrayHalf = len(char) // 2
        
        while True:
            # even elements
            if len(char) % 2 == 0:
                if char[pointer1] == char[pointer2]:
                    pointer1 += 1
                    pointer2 -= 1
                    if pointer1 >= arrayHalf:
                        return True
                else:
                    return False

            # odd elements
            if len(char) % 2 == 1:
                while True:
                    if pointer1 == pointer2:
                        return True
                    elif char[pointer1] == char[pointer2]:
                        pointer1 += 1
                        pointer2 -= 1
                    else:
                        return False
                
        
       
        

        


