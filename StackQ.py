# Michael Suter
# Stack method / add or remove from the end
# 3-5-20

from LinkedTail import LinkedListTail


class Stack:
    def __init__(self):
        self.the_stack = []

    def push(self, data):
        self.the_stack.append(data)

    def pop(self):
        return self.the_stack[-1]


class Queue(LinkedListTail):
    def __init__(self):
        self.myList = LinkedListTail.__init__(self)

    def pushy(self, data):
        self.myList.push_end(data)

    def popp(self):
        return self.myList.pop_head()
