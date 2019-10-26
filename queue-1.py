from copy import deepcopy

my_list = []
my_list.append('A')
my_list.append('B')
my_list.append('C')

my_queue = deepcopy(my_list)
my_stack = deepcopy(my_list)

print my_queue.pop(0)
print my_stack.pop()