from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict = {key : 0 for key in arr}

        for i in arr:
            if i in dict:
                dict[i] += 1
        
        return len(set(dict.values())) == len(dict.values())


arr = [1,2,2,1,1,3]
sol = Solution()
print(sol.uniqueOccurrences(arr))



