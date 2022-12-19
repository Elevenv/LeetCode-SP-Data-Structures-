# https://leetcode.com/problems/valid-anagram/?envType=study-plan&id=data-structure-i

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # ss = sorted(s)
        # tt = sorted(t)
        # return ss==tt
        
        # OR
        
        # if len(s)!=len(t):
        #     return False
        
        # for i in s:
        #     if i not in t:
        #         return False
        # else:
        #     d = {}
        #     d1 = {}
        #     for j in s:
        #         if j in d:
        #             d[j]+=1
        #         else:
        #             d[j] = 1

        #     for k in t:
        #         if k in d1:
        #             d1[k]+=1
        #         else:
        #             d1[k] = 1
        #     for l in d:
        #         if d[l]!=d1[l]:
        #             return False
        #     return True

# OR

#         l = []

#         for i in t:
#             l.append(i)

#         for j in s:
#             if j not in l:
#                 return False
#             l.remove(j)
            
#         if l:
#             return False
#         else:
#             return True

# OR


        if len(s)!=len(t):
            return False
        sd ,td = defaultdict(int),defaultdict(int)

        for i in s:
            sd[i]+=1

        for j in t:
            td[j]+=1

        for k in s:
            if sd[k]!=td[k]:
                return False
        else:
            return True

# OR
        # if len(s)!=len(t): return False
        # s = sorted(s)
        # t = sorted(t)
        # for i in range(len(s)):
        #     if s[i]!=t[i]:
        #         return False
        # return True