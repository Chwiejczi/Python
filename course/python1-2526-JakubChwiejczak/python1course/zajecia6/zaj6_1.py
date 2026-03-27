class FibonacciIterator:
    i = 1

    def __init__(self, max_elements):
        self.max_elements = max_elements

    def __iter__(self):
        self.a = 0
        self.b = 1
        print(f"{self.a}")
        print(f"{self.b}")
        return self

    def __next__(self):
        self.i = self.i + 1
        if self.i < self.max_elements:
            res = self.a + self.b
            self.a = self.b
            self.b = res
            return res


fib = FibonacciIterator(7)
it = iter(fib)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
