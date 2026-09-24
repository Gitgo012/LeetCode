class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result=""
        smaller=min(word1,word2,key=len)
        larger=max(word1,word2,key=len)
        for i in range(len(smaller)):
            result+=(word1[i]+word2[i])
        result+=larger[len(smaller):]
        return result