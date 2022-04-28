import numpy as np

class activation:
    #features
    def __init__():
        pass
    #softmax with standardizing option
    def softmax(self, array, std):
        max = np.max(array)
        if std == True:
            return np.exp(array - max) / np.sum(np.exp(array - max))
        return np.exp(array) / np.sum(np.exp(array))
    #tangent hyperbolic 
    def tanh(self, array):
        return (np.exp(array) - np.exp(-1 * array)) / (np.exp(array) + np.exp(-1 * array))