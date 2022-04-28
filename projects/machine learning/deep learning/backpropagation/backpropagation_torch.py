import numpy as np
import matplotib as plt

class backpropagation():
    #features 
    def __init__(self, input_channel, hidden_channel, output_channel, learning_rate):
        self.input_channel = input_channel
        self.hidden_channel = hidden_channel
        self.output_channel = output_channel
        self.learning_rate = learning_rate
        #setting weight matrices for each channels
        self.weight_input_hidden = np.random.random((input_channel, hidden_channel))
        self.weight_hidden_out = np.random.random((hidden_channel, output_channel))
        #loss starts at 0
        self.loss = 0 
        #stores loss for each epoch and use it to take the average 
        self.loss_average = []
    #sigmoid activation function 
    def sigmoid(self, x, deriv):
        if deriv == True:
            return x * (1 - x)
        return 1 / (1 + np.exp(x))
    #training function 
    def train(self, data, output_labeled, epoch_number, batch_size):
        #storing data size
        data_size = data.shape[0]
        #training
            #repeated epoch number times 
            for i in range(epoch_number):
                #user report for each 10 epoches 
                if i % 10 == 0:
                    print(f'epoch: {i}')
                #number of iteration based on data size and batch size
                for j in range(data_size / batch_size):
                    #get random data from data and batch size done 
                    batch = np.random.choice(data_size, replace = False, size = batch_size)
                    #forwarding
                    #get hidden output(batch x input channel)
                    hidden_output = self.sigmoid(np.dot(data[batch], self.weight_input_hidden))
                    #get output(batch x output channel)
                    output = self.sigmoid(np.dot(hidden_output, self.weight_hidden_out))
                    #backwarding 
                    #define loss function using mean square error(batch x output)
                    loss_function = (output - output_labeled[batch]) ** 2
                    #derivation of loss regarding output(batch x output)
                    der_loss_out = 2 ** (output_label[batch] - output) * self.sigmoid(output, deriv = True)
                    #derivation of loss regarding weight from hidden to out(input channel x output channel)
                    der_loss_weight_hidden_out = np.dot(hidden_output.T, der_loss_out)
                    #derivation of loss regarding hidden output
                    der_loss_hidden = 2 ** (output_)



    