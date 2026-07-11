import math

class Value:
    def __init__(self, value, _prev = (), op = ""):
        self.value = value
        self.grad = 0
        self._prev = _prev
        self.op = op
        self._backward = lambda: None

    def __repr__(self):
        return f"Value(value={self.value}, grad={self.grad}, _prev={self._prev}, op={self.op})"

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

    def __add__(self, other):
        if not isinstance(other, Value):
            other = Value(other)

        out = Value(self.value + other.value, (self, other), "+")

        def _backward():
            self.grad += out.grad
            other.grad += out.grad

        out._backward = _backward
        return out
    
    def __mul__(self, other):
        if not isinstance(other, Value):
            other = Value(other)

        out = Value(self.value * other.value, (self, other), "+")

        def _backward():
            self.grad += out.grad * other.value
            other.grad += out.grad * self.value

        out._backward = _backward
        return out
    
    def __radd__(self, other):
        return self + other
    
    def __rmul__(self, other):
        return self * other

    def __neg__(self):
        return self * -1
    
    def __sub__(self, other):
        return self + (-other)

    def __pow__(self, other):
        assert isinstance(other, (int, float))

        out = Value(self.value ** other, (self,), f"**{other}")

        def _backward():
            self.grad += out.grad * other * (self.value ** (other - 1))

        out._backward = _backward

        return out
    
    def __truediv__(self, other):
        if not isinstance(other, Value):
            other = Value(other)

        return self * (other ** -1)

    def __rtruediv__(self, other):
        return other * (self ** -1)

    def tanh(self):
        t = math.tanh(self.value)
        out = Value(
            t,
            (self,),
            "tanh"
        )
        def _backward():
            self.grad += out.grad * (1 - out.value ** 2)

        out._backward = _backward
        return out

if __name__ == "__main__":
    a = Value(2)
    b = Value(3)

    print(a)
    print(b)

    c = a + b
    print(c)

    d = c * a
    print(d)
    print("="*100)
    d.backward()
    print("a.grad=", a.grad)
    print("b.grad=", b.grad)
    print("c.grad=", c.grad)
    print("d.grad=", d.grad)
