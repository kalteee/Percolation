class UnionFind: #for the size of the maximal cardinality component
    def __init__(self, n):
        self.roots = [i for i in range(n)]
        self.sizes = [1] * n
        self.maxsize = 1 if n > 0 else 0
        
    def find(self, a):
        if a != self.roots[a]:
            self.roots[a] = self.find(self.roots[a])
        return self.roots[a]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            if self.sizes[ra] < self.sizes[rb]:
                self.roots[ra] = rb
                self.sizes[rb] += self.sizes[ra]
                if self.sizes[rb] > self.maxsize:
                    self.maxsize = self.sizes[rb]
            else:
                self.roots[rb] = ra
                self.sizes[ra] += self.sizes[rb]
                if self.sizes[ra] > self.maxsize:
                    self.maxsize = self.sizes[ra]
        return self
    
    def get_maxsize(self):
        return self.maxsize
    
