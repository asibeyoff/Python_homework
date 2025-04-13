import math

class Vector:
    """mathematical vector in n-dimensional space."""
    
    def __init__(self, *components):
        """boshiga qaytaradi i mean initiate  a vector """
        self.components = list(components)
        if not self.components:
            raise ValueError("Error")
    
    def __str__(self):
        """Return string  of the vector."""
        return f"Vector({', '.join(str(c) for c in self.components)})"
    
    def __len__(self):
        """Return the number of dimensions."""
        return len(self.components)
    
    def _check_dimensions(self, other):
        """Check if 2 vectors have the same dimensions."""
        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimensions")
    
    def __add__(self, other):
        """Add two vectors."""
        self._check_dimensions(other)
        return Vector(*(a + b for a, b in zip(self.components, other.components)))
    
    def __sub__(self, other):
        """Subtract two vectors."""
        self._check_dimensions(other)
        return Vector(*(a - b for a, b in zip(self.components, other.components)))
    
    def __mul__(self, other):
        """Compute dot product with another vector or scalar multiplication."""
        if isinstance(other, Vector):
            self._check_dimensions(other)
            return sum(a * b for a, b in zip(self.components, other.components))
        elif isinstance(other, (int, float)):
            return Vector(*(other * c for c in self.components))
        else:
            raise TypeError("Multiplication only supported with Vector or scalar")
    
    def __rmul__(self, scalar):
        """Support scalar * vector multiplication."""
        return self.__mul__(scalar)
    
    def magnitude(self):
        """Compute the magnitude (length) of the vector."""
        return math.sqrt(sum(c ** 2 for c in self.components))
    
    def normalize(self):
        """Return the unit vector."""
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector")
        return Vector(*(c / mag for c in self.components))

#mana exampleee
if __name__ == "__main__":
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)
    
    print(v1)                    # v1
    print(v1 + v2)               # Vector(5, 7, 9)
    print(v2 - v1)               # Vector(3, 3, 3)
    print(v1 * v2)               # 32
    print(3 * v1)                # Vector(3, 6, 9)
    print(v1.magnitude())        
    print(v1.normalize())       