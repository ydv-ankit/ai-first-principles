from random import random

def predict(x, w):
    return x * w

def loss(prediction, target):
    return (prediction - target) ** 2

def gradient(x, w, target):
    return 2 * (x * w - target) * x

def trainingLoop(x, target, epochs = 50):
    w = random()
    lr = 0.1

    for epoch in range(epochs):
        prediction = predict(x, w)

        l = loss(prediction, target)

        g = gradient(x, w, target)

        w = w - lr * g

        print("epoch=", epoch, "weight=", w, "loss=", l, "gradient=", g, "prediction", prediction)

if __name__ == "__main__":
    x = 2
    target = 30
    trainingLoop(x, target)
