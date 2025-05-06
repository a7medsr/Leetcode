class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i in {'{','[','('}:
                stack.append(i)
            else:
                if not stack:
                    return False
                if i==']':
                    if stack[-1]!='[':
                        return False
                elif i==')':
                    if stack[-1]!='(':
                        return False
                else:
                    if stack[-1]!='{':
                        return False
                stack.pop()
        if not stack:
            return True
        return False
            
