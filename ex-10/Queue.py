from collections import deque 
queue = deque(["Ram", "Tarun", "Asif", "John"]) 
print(queue) 
queue.append("Akbar")
print(queue)
queue.popleft()                 
print(queue)
