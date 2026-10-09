class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        seen={}
        unique_occurences=[]
        for num in arr:
            if num in seen:
                seen[num]+=1
            seen[num]=seen.get(num,0)+1
        for key,val in seen.items():
            unique_occurences.append(val)
        return len(unique_occurences)==len(set(unique_occurences))