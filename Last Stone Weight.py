stones = [1, 3]
stack = sorted(stones)
while len(stack) != 1:
    x = stack.pop()
    y = stack.pop()
    if x != y:
        stack.append(x - y)
    else:
        stack.append(0)
    stack = sorted(stack)
print(stack[0])
