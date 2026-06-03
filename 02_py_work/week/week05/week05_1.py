# week05_1.py

class Stack:
    def __init__(self):
        self.stack = ['두산', '로키', '부트']

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return

    def is_empty(self):
        return len(self.stack) == 0
    
    def peak(self):
        if not self.is_empty():
            return self.stack[-1]
        return
        
    def status_stack(self):
        return self.stack
    
list1 = Stack()
list1.push("캠프")
print(list1.status_stack())
print("----------------")
list1.pop()
print(list1.status_stack())