class MyNumbers:

    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n == self.i:
            raise StopIteration

        self.i += 1
        if not self.i % 3:
            return 'HAHA'
        elif not self.i % 5:
            return 'HEHE'
        else:
            return self.i


for x in MyNumbers(20):
    print(x)
