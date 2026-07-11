def perceptron(x1, x2, w1, w2, b):
    p = (x1 * w1) + (x2 * w2) + b
    if p >= 0:
        return 1
    return 0

if __name__ == "__main__":
    print(perceptron(0, 1, 0, -3.1, 3))