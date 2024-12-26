def is_balanced(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in "({[":  # If it's an opening bracket
            stack.append(char)
        elif char in ")}]":  # If it's a closing bracket
            if not stack or stack[-1] != pairs[char]:  # Check for match
                return False
            stack.pop()  # Remove the last opening bracket
    return len(stack) == 0  # True if no unmatched brackets

# Test cases
test_strings = ["()", "(())", "(()[])", "{[()]}", "({[()]})", "(", ")", "({[}])", "(()", "())", "(}[)"]

for s in test_strings:
    print(f"{s}: {'Balanced' if is_balanced(s) else 'Not Balanced'}")
