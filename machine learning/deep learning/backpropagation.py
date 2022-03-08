import numpy as np
import matplotlib.pyplot as plt

class NeuralNetworkDesign():
    # Constructor
    def __init__(self, inputLsize, hiddenLsize, outputLsize, learningRate):
        self.inputLsize = inputLsize
        self.hiddenLsize = hiddenLsize
        self.outputLsize = outputLsize
        self.weightIH = np.random.randn(inputLsize, hiddenLsize) # 2x8
        self.weightHO = np.random.randn(hiddenLsize, outputLsize) # 8x1
        self.learningRate = learningRate
        self.loss = 0
        self.lossArr = []
    
    # sigmoid function
    def sigmoid (self, x):
        return 1 / (1 + np.exp(-x))
    
    #sigmoid derivative function
    def sigmoid_deriv(self, x):
        return x * (1 - x)
    
    
    def train(self, x, t, epoch_num, batch_size):
        data_num = x.shape[0]

        for i in range(epoch_num):
            if i % 10 == 0 :
                print("epoch:", i)
            for j in range(data_num):
                batch = np.random.choice(data_num, replace = False, size = batch_size)
                '''forward pass'''
                # hi, output of hidden layer
                output_hi = self.sigmoid(np.dot(x[batch], self.weightIH))
                #yj, output of output layer
                output_yj = self.sigmoid(np.dot(output_hi, self.weightHO))
                
                '''backward pass'''
                #error function
                error_func = 0.5 * ((output_yj - t[batch])**2)
                # derivative of the error with regard to the net input of the output layer
                EIj = (output_yj - t[batch]) * self.sigmoid_deriv(output_yj)
            
                EIjWij = np.dot(EIj, self.weightHO.T)
                EIi = EIjWij * self.sigmoid_deriv(output_hi)
                # update weights between hidden layer and output layer
                self.weightHO = self.weightHO - (self.learningRate * np.dot(output_hi.T, EIj)) 
                # update weights between input layer and hidden layer
                self.weightIH = self.weightIH - (self.learningRate * np.dot(x[batch].T, EIi))
                
                # add loss
                self.loss += np.sum(error_func)
            
            # add loss to loss array
            self.lossArr.append(self.loss)
            # renew loss
            self.loss = 0     
            
if __name__ == "__main__":
    data = np.loadtxt("/Users/jaewanpark/Documents/jaewan/project/machine learning/deep learning/training.txt") 
    x = data[:, 0:2]
    t = data[:, 2:3]

    epoch = 30
    batch_size = 1
    
    nnd = NeuralNetworkDesign(2, 8, 1, 0.01)
    nnd.train(x, t, epoch, batch_size)
    
    plt.plot(range(epoch), nnd.lossArr)
    plt.title('Neural Network Design')
    plt.xlabel('# Epoch')
    plt.ylabel('Loss')
    plt.show()