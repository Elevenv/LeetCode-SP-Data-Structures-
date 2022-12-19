# https://leetcode.com/problems/first-unique-character-in-a-string/?envType=study-plan&id=data-structure-i

s = "loveleetcode"

# for i in range(len(s)):
#     if s.count(s[i])==1:
#         print(i)
#         break
# else:
#     print(-1)

hashmap = {}

for c in s:
    if c in hashmap:
        hashmap[c]+=1
    else:
        hashmap[c] = 1

for idx,item in enumerate(s):
    if item in hashmap and hashmap[item]==1:
        print(idx)
        break
else:
    print(-1)
