class Queue:
    def __init__(self):
        self.store = []

    def enqueue(self, thing):
        self.store += [thing]

    def dequeue(self):
        item = self.store[0]
        self.store = self.store[1:]
        return item

    def is_empty(self):
        if len(self.store) == 0:
            return True
        else:
            return False


class Tree:

    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        if type(child) != Tree:
            c = Tree(child)
            self.children += [c]
        return True

    def get_val(self):
        return self.value

    def get_children(self):
        return self.children

    def is_leaf(self):
        if not self.get_children():
            return True
        else:
            return False

    def get_level_order(self):
        x = Queue()
        x.enqueue(self)
        accum = []
        while not x.is_empty():
            t = x.dequeue()
            val = t.get_val()
            accum += [val]
            for child in t.get_children():
                x.enqueue(child)
        return accum
