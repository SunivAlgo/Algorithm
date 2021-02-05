from collections import deque
left = [1,2,3]
right = deque([4,5,6])
left.extend(right)
left = ''.join(list(map(str,left)))
print(left)