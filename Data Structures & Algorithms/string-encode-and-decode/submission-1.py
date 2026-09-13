class Solution:
    alphabet = {}
    # starts at 'a'
    charCode = 97
    

    def encode(self, strs: List[str]) -> str:
        # corresponds the word to a char
        for word in strs:
            self.alphabet[chr(self.charCode)] = word
            self.charCode += 1

        # join char array to make encoded string
        self.encoded_string = "".join(self.alphabet.keys())
        return self.encoded_string

    

    def decode(self, s: str) -> List[str]:
        decoded_string = list(s)
        decoded_strs = []

        for entry in decoded_string:
            decoded_strs.append(self.alphabet.get(entry))

        self.alphabet.clear()

        return decoded_strs




