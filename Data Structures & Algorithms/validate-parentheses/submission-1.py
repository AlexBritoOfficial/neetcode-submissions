class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False

        stack = []
        for element in s:
            if element == "(" or element == "[" or element == "{":
                stack.append(element)
            elif len(stack) > 0:
                if element == ")" and stack[-1] == "(":
                    stack.pop()
                elif element == "}" and stack[-1] == "{":
                    stack.pop()
                elif element == "]" and stack[-1] == "[":
                    stack.pop()
                else:
                    return False
            else:
                return False
        
        if len(stack) > 0:
            return False

        return True