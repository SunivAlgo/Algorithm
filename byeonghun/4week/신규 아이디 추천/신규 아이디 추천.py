def solution(new_id):
    stack = []
    new_id = new_id.lower()
    for v in new_id:
        if v == '-' or v == '_':
            stack.append(v)
        elif v == '.':
            if stack and stack[-1] != '.':
                stack.append(v)
        elif 97 <= ord(v) <= 122:
            stack.append(v)
        elif 48 <= ord(v) <= 57:
            stack.append(v)
    if not stack:
        stack.append("a")
    if stack[0] == '.':
        stack.pop(0)
    if stack[-1] == '.':
        stack.pop()
    if len(stack) > 15:
        del stack[15:]
        if stack[-1] == '.':
            stack.pop()
    if len(stack) <= 2:
        while len(stack) < 3:
            stack.append(stack[-1])

    return "".join(stack)


print(solution("z-+.^."))