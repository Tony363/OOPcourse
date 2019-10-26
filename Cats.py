class Cats:
    class _cat_iter:
        def __init__(self, cats):
            self.cats = cats
            self.cur = 0

        def next(self):
            i = self.cur
            if i >= len(self.cats):
                raise StopIteration
            self.cur += 1
            return self.cats[i]

    def __init__(self):
        self.cats = []

    def add(self, name):
        self.cats.append(name)
        return self

    def __iter__(self):
        return Cats._cat_iter(self.cats)

a = Cats()
a.add("joe").add("jack").add('fink').add('dink')
for c in a:
    print(c)                            