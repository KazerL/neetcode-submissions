class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeBracket = {")":"(", "}":"{", "]":"["}

        for char in s:
            if stack and char in closeBracket:
                if stack[-1] != closeBracket[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)

        if len(stack) == 0:
            return True
        else:
            return False





