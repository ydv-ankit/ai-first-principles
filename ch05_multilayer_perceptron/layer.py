from .neuron import Neuron

class Layer:
    def __init__(self, nin, nout):
        self.neurons = [
            Neuron(nin)
            for _ in range(nout)
        ]

    def __call__(self, x):
        outs = [neuron(x) for neuron in self.neurons]
        return outs[0] if len(outs) == 1 else outs
    
    def parameters(self):
        params = []

        for neuron in self.neurons:
            params.extend(neuron.parameters())

        return params
