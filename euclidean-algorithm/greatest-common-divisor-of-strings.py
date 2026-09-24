class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        smaller=min(str1,str2,key=len)
        for i in range(len(smaller),0,-1):
            prefix=smaller[:i]
            if (prefix*(len(str1)//len(prefix))==str1 and prefix*(len(str2)//len(prefix))==str2):
                return prefix
        return ""