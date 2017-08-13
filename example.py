import tracker

class Thing(object):
    def __init__(self):
        tracker.create(self, 'a', 34)
        tracker.create(self, 'b', dtype=float)

    def update(self):
        self.a = 200
        self.b = 3.14

t = Thing()
t.update()
print(t.a, t.b)
