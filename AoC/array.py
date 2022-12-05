class Array(list):

    """
        Adds operator chaining to lists.
        Allows methods like .map, .filter, .append, e.t.c to always return the next list.
        Allows javascript style chaining.
    """

    __add__  = lambda self, n: Array(super().__add__(n))
    __iadd__ = lambda self, n: Array(super().__iadd__(n))
    __imul__ = lambda self, n: Array(super().__imul__(n))
    __mul__  = lambda self, n: Array(super().__mul__(n))
    __rmul__ = lambda self, n: Array(super().__rmul__(n))

    def append(self, n):
        c = self.copy()
        list.append(c, n)
        return c

    def clear(self):
        return Array()

    def copy(self):
        return Array(self)

    def extend(self, n):
        c = self.copy()
        list.extend(c, n)
        return c

    def insert(self, n):
        c = self.copy()
        list.insert(c, n)
        return c

    def reverse(self):
        return self.clone()[::1]

    def remove(self, n):
        c = self.copy()
        list.remove(c, n)
        return c

    def sort(self, key = None, reverse = False, ):
        c = self.copy()
        list.sort(c, key=key, reverse=reverse)
        return c

    def map(self, func):
        return Array(map(func, self))

    def filter(self, func):
        return Array(filter(func, self))

    def reduce(self, func, init = None):

        startPos = 1 if init is None else 0
        if init is None:
            init = self[0]
            
        for elem in self[startPos:]:
            init = func(init, elem)

        return init

    def forEach(self, func):

        for elem in self:
            func(elem)

        return self

