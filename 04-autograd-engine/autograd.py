class Value:
    def __init__(self, value, children = (), op = ""):
        self.value = value
        self.grad = 0
        self.children = children
        self.op = op

    def __repr__(self):
        return f"Value(value={self.value}, grad={self.grad}, children={self.children}, op={self.op})"
    
    def __add__(self, other):
        print("adding", self.value, other.value)
        return Value(value=self.value + other.value, children=(self, other), op="+")

    def __mul__(self, other):
        print("multiplication", self.value, other.value)
        return Value(value=self.value * other.value, children=(self, other), op="*")

if __name__ == "__main__":
    a = Value(2)
    b = Value(3)

    print(a)
    print(b)

    c = a + b
    print(c)

    d = c * Value(8)
    print(d)
