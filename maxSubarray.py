# https://leetcode.com/problems/maximum-subarray/?envType=study-plan&id=data-structure-i
# 53. Maximum Subarray


nums = [-2,1,-3,4,-1,2,1,-5,4]
lists = [[]]
for i in range(len(nums)+1):
    for j in range(i):
        lists.append(nums[j:i])
lists.pop(0)
large = sum(lists[0])
for k in lists:
    if sum(k)>large:
        large = sum(k)
print(large)

# OR


# maxsu=nums[0]
# su=0

# for i in nums:
#     if su<0:
#         su=0
#     su+=i
#     maxsu = max(maxsu, su)
# print(maxsu)