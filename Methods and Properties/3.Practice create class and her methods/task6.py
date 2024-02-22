class Stack():
    def __init__(self):
        self.values = []
    
    def push(self, item):
        self.values.append(item)

    def pop(self):
        return self.values.pop()
    
    def peek(self):                 
        if len(self.values) != 0:
            return self.values[-1]
        else:
            return 'Empty Stack'
    
    def is_empty(self):
        if self.peek() == 'Empty Stack':      #  self.peek() - Principle 'dry'
            return True
        else: 
            return False
    
    def size(self):
        return len(self.values)
    
""" 
Example

s = Stack()
s.peek() # will print 'Empty Stack'
print(s.is_empty()) # will print True
s.push('cat') # put 'cat' element on top of the stack
s.push('dog') # put 'dog' element on top of the stack
print(s.peek()) # will print 'dog'
s.push(True) # put True element on top of the stack
print(s.size()) # will print 3
print(s.is_empty()) # will print False
s.push(777) # put 777 element on top of the stack
print(s.pop()) # remove and print the top element 777 from the stack
print(s.pop()) # remove and print the top element True from the stack
print(s.size()) # will print 2

"""
