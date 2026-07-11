import math
from random import random

hours = [1, 2, 3, 4, 5]
scores = [5, 20, 24, 37, 51]

def totalError(weight):
    error = 0
    for hour, score in zip(hours, scores):
        error += abs((hour * weight) - score)
    return error

def predict(weight):
    errorThreshold = 0.01
    lr = 0.01
    oldError = totalError(weight)
    while True:
        oldError = totalError(weight)
        newWeight = weight + lr
        newError = totalError(newWeight)
        print("old error", oldError)
        print("new error", newError)
        if newError < oldError:
            weight = newWeight
        else:
            lr = -lr
        if newError < errorThreshold:
            break
    print("weight", weight)

if __name__ == "__main__":
    weight = random()
    print("weight", weight)
    predict(weight)