import numpy as np
from MLlib.activations import Sigmoid, Relu


def test_Sigmoid():
    X = np.random.random((3, 2))
    assert np.array_equal(
        (1 / (1 + np.exp(-X))),
        Sigmoid.activation(X)
        ) is True
    assert np.array_equal(
        (1 / (1 + np.exp(-X)))*(1-(1 / (1 + np.exp(-X)))),
        Sigmoid.derivative(X)) is True


def test_Relu():
    X = np.array([[1, -2, 3], [-1, 2, 1]])
    assert np.array_equal(
        np.maximum(0, X),
        Relu.activation(X)
        ) is True
    assert np.array_equal(
        np.greater(X, 0).astype(int),
        Relu.derivative(X)) is True
