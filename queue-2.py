from collections import deque  # double ended queue
from copy import deepcopy

my_list = deque()
my_list.append('A')
my_list.append('B')
my_list.append('C')

my_queue = deepcopy(my_list)
my_stack = deepcopy(my_list)

print my_queue.popleft()  # 'A'
print my_stack.pop()      # 'C'
