lass Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = [""]
        s = s.replace("()", "")
        for i in s:
            if i == "(":
                stack.append("")
            elif i == ")":
                last = stack.pop()[::-1]
                stack[-1] += last
            else:
                stack[-1] += i

        return stack.pop()
