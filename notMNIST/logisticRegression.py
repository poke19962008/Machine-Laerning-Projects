import numpy as np
from sklearn.linear_model import LogisticRegression
import os, pickle


with open("bin/notMNIST.pkl", 'r') as f:
    alphabTest = pickle.load(f)

    X = alphabTest["trainingSet"]
    X = X[:len(X)].reshape(len(X), 784)
    Y = alphabTest["trainingLabel"]
    del alphabTest

    logreg = LogisticRegression(C=1e5)
    logreg.fit(X, Y)
