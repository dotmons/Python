
def question1(value: str) -> bool:
    stack = []
    pairs = {')': '(', 
             '}': '{', 
             ']': '['}

    for char in value:
        
        if char in pairs:
            # Check for matching opening bracket

            #print(f"Input: {char}")
            #print(f"Processing closing bracket: {pairs[char]}")
            if stack == [] or stack[-1] != pairs[char]:
                return False
            stack.pop()  # pop from stack
        else:
            stack.append(char)  # push to stack

    return len(stack) == 0
