class UnionFind: 
    """
    Union-Find data structure for the update of connected components and maximal size component on the grid.
    """
    def __init__(self, n: int) -> None:
        """Initialization of the data structure with n elements (vertices)"""
        self.roots = [i for i in range(n)]
        self.sizes = [1] * n
        self.maxsize = 1 if n > 0 else 0
        
    def find(self, a: int) -> int:
        """
        Find the representative (root) of the element a with path-compression.
        
        Args: a (int): the index of the element in search
        Returns: 
            int: the root of the component of the vertex
        """
        if a != self.roots[a]:
            self.roots[a] = self.find(self.roots[a])
        return self.roots[a]

    def union(self, a: int, b: int) -> "UnionFind":

        """
        Merge the components containing 'a' and 'b' vertices. Update the size of the maximal sized component.
        
        Args:
            a (int): index of the first vertex.
            b (int): index of the second vertex.
        Returns:
            UnionFind: returns self for linking aspects.
        """
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
    
    def get_maxsize(self) -> int:
        """Returns the size of the maximal cardinality connected component"""
        return self.maxsize
    
