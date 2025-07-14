def is_balanced(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    return len(stack) == 0

test_strings = ["()", "(())", "(()[])", "{[()]}", "({[()]})", "(", ")", "({[}])", "(()", "())", "(}[)"]

for s in test_strings:
    print(f"{s}: {'Balanced' if is_balanced(s) else 'Not Balanced'}")
