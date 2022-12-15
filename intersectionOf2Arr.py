# https://leetcode.com/problems/intersection-of-two-arrays-ii/description/?envType=study-plan&id=data-structure-i

# nums1 = [1,2,2,1]
# nums2 = [2,2]

nums1 = [3,1,2]
nums2 = [1,1]
nums3 = []
if len(nums1)<=len(nums2):
    for i in nums1:
        if i in nums2:
            nums3.append(i)
            nums2.remove(i)
else:
    for i in nums2:
        if i in nums1:
            nums3.append(i)
            nums1.remove(i)

print(nums3)

# OR


# temp = []
# d1 = Counter(nums1)
# for i in nums2:
#     if i in d1 and d1[i] > 0 :
#         temp.append(i)
#         d1[i] -= 1 
# print(temp)


# OR

# nums1.sort()
# nums2.sort()
# pointer1, pointer2, out = 0, 0, list()
# while pointer1 < len(nums1) and pointer2 < len(nums2):
#     if nums1[pointer1] == nums2[pointer2]:
#         out.append(nums1[pointer1])
#         pointer1 += 1
#         pointer2 += 1
#     elif nums1[pointer1] > nums2[pointer2]:
#         pointer2 += 1
#     else:
#         pointer1 += 1

# print(out)