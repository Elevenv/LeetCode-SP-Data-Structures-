# https://leetcode.com/problems/pascals-triangle/?envType=study-plan&id=data-structure-i

def PascalTriangle(numRows):
    ans = [[1]]
    for i in range(numRows-1):
        temp = [0] + ans[-1] + [0]
        row = []
        for j in range(len(ans[-1])+1):
            row.append(temp[j]+temp[j+1])
        ans.append(row)
    return ans

numRows = int(input())
print(PascalTriangle(numRows))