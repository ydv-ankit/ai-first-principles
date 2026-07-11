from .layer import Layer


class MLP:
    def __init__(self, nin, nouts):
        sizes = [nin] + nouts
        layers = []
        for i in range(len(sizes) - 1):
            layers.append(Layer(sizes[i], sizes[i + 1]))
        self.layers = layers

    def __call__(self, x):
        for layer in self.layers:
            x = layer(x)
        return x

    def parameters(self):
        params = []

        for layer in self.layers:
            params.extend(layer.parameters())

        return params


if __name__ == "__main__":
    xs = [
        [2.0, 3.0, -1.0],
        [3.0, -1.0, 0.5],
        [0.5, 1.0, 1.0],
        [1.0, 1.0, -1.0],
    ]

    ys = [
        1.0,
        -1.0,
        -1.0,
        1.0,
    ]
    ypreds = []
    model = MLP(3, [4, 6, 3, 1])
    epochs = 10000
    for epoch in range(epochs):

        # forward
        ypreds = [model(x) for x in xs]

        # loss
        loss = sum((pred - target) ** 2 for pred, target in zip(ypreds, ys))

        # zero gradients
        for p in model.parameters():
            p.grad = 0

        # backward
        loss.backward()

        # update
        for p in model.parameters():
            p.value -= 0.05 * p.grad

        if epoch % 10 == 0:
            print(f"Epoch {epoch}")
            print("Loss:", loss.value)
            print([round(p.value, 3) for p in ypreds])
            print()

        print(epoch, loss.value)
