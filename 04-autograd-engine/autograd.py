class Value:
    def __init__(self, value, _prev = (), op = ""):
        self.value = value
        self.grad = 0
        self._prev = _prev
        self.op = op
        self._backward = lambda: None

    def __repr__(self):
        return f"Value(value={self.value}, grad={self.grad}, _prev={self._prev}, op={self.op})"
    
    def __add__(self, other):
        out = Value(value=self.value + other.value, _prev=(self, other), op="+")
        def _backward():
            self.grad += out.grad
            other.grad += out.grad
        out._backward = _backward
        return out

    def __mul__(self, other):
        out = Value(value=self.value * other.value, _prev=(self, other), op="*")
        def _backward():
            self.grad += out.grad * other.value
            other.grad += out.grad * self.value
        out._backward = _backward
        return out

    def build(self):
        visited: set[Value] = set()
        topo: list[Value] = list()
        def buildGraph(self: Value):
            if self in visited:
                return
            visited.add(self)
            if self._prev:
                for ch in self._prev:
                    buildGraph(ch)
            topo.append(self)
        buildGraph(self)
        return topo

    def backward(self):
        topo = self.build()
        self.grad = 1
        for node in reversed(topo):
            node._backward()

if __name__ == "__main__":
    a = Value(2)
    b = Value(3)

    print(a)
    print(b)

    c = a + b
    print(c)

    d = c * Value(8)
    print(d)
    print("="*100)
    d.backward()
    print("a.grad=", a.grad)
    print("b.grad=", b.grad)
    print("c.grad=", c.grad)
    print("d.grad=", d.grad)
