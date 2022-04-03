class qickFind():
    def __init__(self, size):
        self.size = size
        self.root = [i for i in range(size)]

    def find(self, x):
        return self.root[x]

    def connected(self, x, y):
        return self.find(x) == self.find(y)

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootY != rootX:
            for i in range(self.size):
                if self.root[i] == rootY:
                    self.root[i] = rootX
        return self.root


# Test Case
uf = qickFind(10)
# 1-2-5-6-7 3-8-9 4

uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
uf.union(3, 8)
uf.union(8, 9)

print(uf.connected(1, 4))
print(uf.connected(1, 7))


