from abc import ABC
import numpy as np
import nnfs
from nnfs.datasets import spiral_data

nnfs.init()

#These will represent neurons in my input(first true) layer of neurons
#To prevent shape errors the number of inputs per batch must equal the number of neurons (1D arrays in the weights matrix

def sigmoid(x):
    return 1 / (1 * np.exp(-x))

def softmax(x):
    exp_values = np.exp(x - np.max(x,axis=1,keepdims=True))
    return exp_values / np.sum(exp_values,axis=1,keepdims=True)

''' 
#Each input have a weight. These below are the input of 3 neurons
weights = [[1,0.4,0.8,1],
           [0.7,0.6,0.3,2],
           [0.5,0.4,0.3,0.9]]
#Each neuron has its own unique bias
biases = [0.3,0.8,0.5]

#This section of code will represent the weights and biases of yet another layer of neurons
weights_2 = [[1,0.4,1],
           [0.7,0.6,2],
           [0.4,0.3,0.9]]
#Each neuron has its own unique bias
biases_2 = [-0.2,0.6,0.8]

#This example contains 3 layer neurons each receiving four inputs and outputting three outputs.
"""
output = [inputs[0]*weights[0][0] + inputs[1]*weights[0][1] + inputs[2]*weights[0][2] + inputs[3]*weights[0][3]+ bias[0],
          inputs[0]*weights[1][0] + inputs[1]*weights[1][1] + inputs[2]*weights[1][2] + inputs[3]*weights[1][3]+ bias[1],
          inputs[0]*weights[2][0] + inputs[1]*weights[2][1] + inputs[2]*weights[2][2] + inputs[3]*weights[2][3]+ bias[2]]
"""

#Quick example of how dot products work (need for vectors and matrices)
""" 
a = [1,2,3]
b = [4,5,6]
ans = 0
for i in range(3):
    #The dot product will multiply corresponding elements from each array to produce a scalar quantity
    ans += a[i] * b[i]
print(ans)
"""
#When using numpy.dot, place vectors first before scalars and place matrices before vectors
#.T stands for transpose, which 'flips' a matrix on its side so that rows become columns and vice versa. This can be used to solve shape problems brought in by using batches of inputs.

#Make sure that the rows of inputs is equal to the number of columns in the untransposed weights matrix
layer1_output = np.dot(inputs, np.array(weights).T) + biases

#Here, to connect the layers together, we pass the outputs from the previous layer as inputs in the next layer
layer2_output = np.dot(layer1_output, np.array(weights_2).T) + biases_2
print(layer2_output)
'''

class Activation_ReLU:
    def forward(self, inputs):
       self.output = np.maximum(0,inputs)

class Activation_Softmax:
    def forward(self, inputs):
        self.output = softmax(inputs)

class Loss(ABC):
    def calculate(self, output, y):
        sample_losses = self.forward(output, y)
        data_loss = np.mean(sample_losses)
        return data_loss
    
class CCrossEntropy(Loss):
    def forward(self, y_pred, y_actual):
        samples = len(y_pred)
        #Clip the values so we don't get any infinity errors if a confidence level happens to be spot on
        y_pred_clipped = np.clip(y_pred, 1e-7, 1-1e-7)

        #If one-hot encoding has not been passed in
        if len(y_actual.shape) == 1:
            correct_confidences = y_pred_clipped[range(samples),y_actual]
        elif len(y_actual.shape) == 2:
            #One-hot encoding has been used in this scenario
            correct_confidences = np.sum(y_pred_clipped*y_actual, axis=1)

        print(-np.log(y_pred[[0,1,2]]))
        #Calculate the loss and return
        loss = -np.log(correct_confidences)
        return loss

class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        #Multiplying by 0.1 ensures that all values produced are lower than 1 and greater than -1
        #There will be one array for each inputs, for each are the weights at each neuron
        #This eliminates the need for transposition when we do the forward pass
        self.weights = 0.1 * np.random.randn(n_inputs, n_neurons)
        #Biases are a 1D array, so 1 list of a length of the number of neurons
        self.biases = np.zeros((1, n_neurons))

    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases

    def backward(self, output_error, learning_rate):
        #The error of this layer's inputs is equal to its output error multipled by the 
        #transposed weights of the layer
        input_error = np.dot(output_error, self.weights.T)
        #The error of the weights in this layer is equal to the transposed matrix of inputs fed into the layer
        #multipled by the error of the output from this layer
        weights_error = np.dot(self.inputs.T, output_error)
        # dBias = output_error

        # update parameters
        self.weights -= learning_rate * weights_error
        self.biases -= learning_rate * output_error
        return input_error

    def backpropagate(self, layer_output):
        for neuron in range(len(layer_output)):
            cost_derivative = np.sum(layer_output[neuron-1])*Derivatives.get_softmax_derivative(np.sum(layer_output[neuron-1]))

X,y = spiral_data(samples=100, classes=3)

#For this, the first number is the number of values in each 1D array in the matrix of training data, so here 4
#Second number can be whatever we want
layer1 = Layer_Dense(2,6)
activation1 = Activation_ReLU()
#Here, the number of inputs must be the same as the number of neurons in the previous layer
layer2 = Layer_Dense(6,3)
activation2 = Activation_Softmax()

#Output will show the outputs from each individual neuron in arrays, and show them in batches of results shown by the 1D array count in the matrix
layer1.forward(X)
activation1.forward(layer1.output)
#print("This is the first output from Layer1,\n", layer1.output)
layer2.forward(activation1.output)
activation2.forward(layer2.output)
#print("This is the final output of this model neural network,\n", layer2.output)

print(activation2.output[0])
#Normalisation is the process of dividing each value by the total sum of values given to produce 
#the probability values associated with neural networks
#This is how we can get percentage accuracy with neural networks

#Using one-hot encoding to calculate the categorical cross-entropy of data (loss)
#In one-hot encoding, we assign the target class position we want in our array of outputs
#Then make an array of 0s of the same length as outputs but put a 1 in the target class position
#This basically simplifies to just the negative natural logarithm of the predicted target value
loss_function = CCrossEntropy()
loss = loss_function.calculate(activation2.output, y)
print("Loss:",loss)

"""
Do not ever forget this amazing website with the answers or the corresponding video:
https://towardsdatascience.com/math-neural-network-from-scratch-in-python-d6da9f29ce65
https://www.youtube.com/watch?v=pauPCy_s0Ok&t=1565s

Videos 2 & 3 from:
https://www.youtube.com/watch?v=09c7bkxpv9I
https://www.youtube.com/watch?v=znqbtL0fRA0
"""

#Calculating the partial derivative of softmax
# = delta softmax(output[j]) / delta output[i] = softmax_derivative

class Derivatives:
    def get_softmax_derivative(self,output, i,j):
        if i == j:
            softmax_derivative = softmax(output[i] * (1-softmax(output[i])))
        else:
            softmax_derivative = -softmax(output[i]) * softmax(output[j])
        return softmax_derivative
    
    def layer_cost_derivative(self, layer_output):
        pass
