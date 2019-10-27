from collections import deque  # double ended queue

warteschlange = deque()
warteschlange.append('A')
warteschlange.append('B')
warteschlange.append('C')

print warteschlange.popleft()  # 'A'
print warteschlange.pop()      # 'C'
