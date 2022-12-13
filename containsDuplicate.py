# https://leetcode.com/problems/contains-duplicate-ii/
# 219. Contains Duplicates 

nums = [1,2,3,1,2,3]
# nums = [1,2,3,1]
# nums = [1,0,1,1]
k = 2
d = {}
for i in range(len(nums)):
    if nums[i] in d:
        if abs(d[nums[i]]-i)<=k:
            print(True)
            break
        else:
            d[nums[i]] = i
    else:
        d[nums[i]] = i
else:
    print(False)

# OR


# s = set(nums)
# if len(s)==len(nums):
#     print(False)
# else:
#     print(True)
