def is_balanced(s):
    stack = []
    # Dictionary to map closing brackets to their corresponding opening brackets
    matching_parentheses = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in matching_parentheses.values():  # Opening brackets
            stack.append(char)
        elif char in matching_parentheses.keys():  # Closing brackets
            if stack and stack[-1] == matching_parentheses[char]:
                stack.pop()  # Remove the matching opening bracket
            else:
                return False  # Mismatch found
    return not stack  # True if stack is empty (all matched)

# Test cases
test_strings = [
    "()", "(())", "(()[])", "{[()]}", "({[()]})",  # Balanced examples
    "(", ")", "({[}])", "(()", "())", "(}[)",      # Unbalanced examples
]

for s in test_strings:
    print(f"{s}: {'Balanced' if is_balanced(s) else 'Not Balanced'}")
