class Solution(object):
    def isValid(self, s: str):
        stack = []
        mapping = {")": "(", "]": "[", "}": "{"}

        for char in s:
            if char in mapping:
                if stack and mapping[char] != stack.pop():
                    return False
                else:
                    stack.append("#")
            else:
                stack.append(char)

        return not stack
                
sol = Solution()
print(sol.isValid("]"))  # Output: False

