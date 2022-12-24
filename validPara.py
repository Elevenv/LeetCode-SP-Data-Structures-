# https://leetcode.com/problems/valid-parentheses/?envType=study-plan&id=data-structure-i
# 20.Valid Paranthesis

# def paraCheck(s):  
#    while True:  
#        if '()' in s :  
#            s = s.replace ( '()' , '' )  
#        elif '{}' in s :  
#            s = s.replace ( '{}' , '' )  
#        elif '[]' in s :  
#            s = s.replace ( '[]' , '' )  
#        else :  
#            return not s
#         #    return False

# s = "(){}[]"
# print(paraCheck(s))

# OR

class Solution:
    def isValid(self,s):
        stack = []
        closeToOpen = {")":"(","]":"[","}":"{"}
            
        for x in s:
            if x in closeToOpen:
                if stack and stack[-1] == closeToOpen[x]:
                    stack.pop()
                else:
                    return '1False'
            else:
                stack.append(x)
        if not stack:
            return True
        else:
            return False

obj = Solution()
s = "(){}[]"
print(obj.isValid(s))

