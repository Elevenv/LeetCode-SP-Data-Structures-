# https://leetcode.com/problems/reshape-the-matrix/?envType=study-plan&id=data-structure-i

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r*c!=(len(mat)*len(mat[0])):
            return mat

        l = [mat[i][j] for i in range(len(mat)) for j in range(len(mat[0]))]
        ans = []
        k = 0
        for i in range(r):
            sub = []
            for j in range(c):
                sub.append(l[k])
                k+=1
            ans.append(sub)
        return ans