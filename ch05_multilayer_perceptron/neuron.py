from random import uniform
from ch04_autograd_engine.autograd import Value 

class Neuron:
    def __init__(self, nin) -> None:
        self.w = [
            Value(uniform(-1, 1))
            for _ in range(nin)
        ]
        self.b = Value(uniform(-1, 1))
    
    def __call__(self, x):
        if len(x) != len(self.w):
            raise ValueError("invalid number of values")
        x = [v if isinstance(v, Value) else Value(v) for v in x]
        weighted_sum = self.b
        for wi, xi in zip(self.w, x):
            weighted_sum += (wi * xi)
        return weighted_sum.tanh()

    def parameters(self):
        return self.w + [self.b]

if __name__ == "__main__":
    n = Neuron(3)

    x = [2.0, 3.0, -1.0]

    y = n(x)

    print(y)
    y.backward()
    print("="*30)
    for i, w in enumerate(n.w):
        print(f"w{i} =", w.value, "grad =", w.grad)

    print("bias =", n.b.value, "grad =", n.b.grad)