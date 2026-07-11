class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: return False

        my_stack = []

        for i in range(len(s)):
            if s[i] in ('[', '{', '('):
                my_stack.append(s[i])
            else:
                if not my_stack:
                    return False
                
                current_char = my_stack.pop()

                if s[i] == ')' and current_char != '(':
                    return False

                if s[i] == ']' and current_char != '[':
                    return False

                if s[i] == '}' and current_char != '{':
                    return False

        return not my_stack