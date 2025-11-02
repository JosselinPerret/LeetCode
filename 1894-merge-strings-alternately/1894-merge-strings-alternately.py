class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word = ""

        l = min(len(word1), len(word2))
        longest = max([word1, word2], key=len)   

        for i in range(l):
            word += word1[i]
            word += word2[i]
            print(word)

        if len(word1) != len(word2):
            word += longest[l::]

        return word
