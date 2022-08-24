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

print(activation2.output[:5])
#Normalisation is the process of dividing each value by the total sum of values given to produce 
#the probability values associated with neural networks
#This is how we can get percentage accuracy with neural networks
