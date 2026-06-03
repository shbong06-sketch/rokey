# queue_list.py

# 빈 큐 구현
queue = []

# Enqueue
queue.append(1)
print(f"queue: {queue}")
queue.append(2)
print(f"queue: {queue}")
queue.append(3)
print(f"queue: {queue}")
queue.append(4)
print(f"queue: {queue}")

# Dequeue
queue.pop(0)
print(f"queue: {queue}")
queue.pop(0)
print(f"queue: {queue}")
queue.pop(0)
print(f"queue: {queue}")
queue.pop(0)
print(f"queue: {queue}")
# queue.pop(0)        # IndexError
# print(f"queue: {queue}")

# 큐가 비어있는 경우
if queue == []:
    print("is_empty!")
else:
    queue.pop(0)        # IndexError
    print(f"queue: {queue}")

