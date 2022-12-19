# https://leetcode.com/problems/ransom-note/?envType=study-plan&id=data-structure-i

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        rd = defaultdict(int)
        md = defaultdict(int)

        for i in ransomNote:
            rd[i]+=1

        for j in magazine:
            md[j]+=1

        for k in ransomNote:
            if rd[k]>md[k]:
                return False
        return True