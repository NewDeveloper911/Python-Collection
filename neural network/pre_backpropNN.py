import numpy as np
from concurrent.futures import ThreadPoolExecutor
import os
import pandas as pd

class Neural_Network:
    def __init__(self,**kwargs):
        self._network = []
        self._inputs = kwargs['inputs']
        self._testing_data = None
        self._target_values = kwargs['targets']
        self._learning_rate = kwargs['learning_rate']
        self._output_percentages = []

        activation_function = input("Which activation function do you wish to use?\n")
        for i in range(kwargs['no_layers']):
            if i == 0:
                try:
                    #For datasets only
                    inputs=len(self._inputs.columns.values)
                except:
                    inputs = len(self._inputs)
            else:
                inputs = self._network[-1].get_neurons()
            neurons = int(input("How many neurons do you want in layer #" + str(i+1) + "?\n"))
            self._network.append(Layer_Dense(no_inputs=inputs,no_neurons=neurons,activation_function=activation_function))
        outputs = int(input("How many outputs do you wish to have in your neural network?\n"))
        output_activation = input("Which activation function do you wish to use for the output function?\n")
        inputs = self._network[-1].get_neurons()
        self._network.append(Layer_Dense(no_inputs=inputs,no_neurons=outputs,activation_function=output_activation))

    def structure(self):
        structure = []
        for layer in self._network:
            structure.append(layer.get_neurons())
        print("The structure of this neural network is:", structure)
    def run(self):
        #Training phase
        #Start by putting initial inputs into the input layer
        self._network[0].forward(self._inputs)
        for i in range(len(self._network)-1):
            #Using the previous layer's outputs as the next layer's inputs
            self._network[i+1].forward(self._network[i].output)
            
        #Normalised to represent the probablity of each category being correct
        print("The network's outputs were:", self._network[-1].output / np.sum(self._network[-1].output, axis=1, keepdims=True))

        #Evaluation needed for backpropagation

        #Testing phase
        self._network[0].forward(self._testing_data)
        for i in range(len(self._network)-1):
            #Using the previous layer's outputs as the next layer's inputs
            self._network[i+1].forward(self._network[i].output)
        print("The network's testing outputs were:", self._network[-1].output/ np.sum(self._network[-1].output, axis=1, keepdims=True))

    def train_test_split(self):
        #Split the available dataset into training data and testing data
        split = float(input("Enter a decimal between 0 and 1 to represent the fraction of data to be used for training:\n"))
        assert split >= 0 and split <=1
        data_split = round(split * len(self._inputs))
        training_data = self._inputs.iloc[0:data_split]
        testing_data = self._inputs.iloc[data_split:]
        self._inputs = training_data
        self._testing_data = testing_data

    #Can be used to evaluate the loss of the neural network
    def calculateLoss(self, y_pred, y_true):
        samples = len(y_pred)
        y_pred_clipped = np.clip(y_pred, 1e-10, 1-1e-10)
        if len(y_true.shape) == 1:
            #Only scalar class values have been passed - no one-hot encoding
            correct_confidences = y_pred_clipped[range(samples), y_true]
        elif len(y_true.shape) == 2:
            #Using one-hot encoded vectors
            correct_confidences = np.sum(y_pred_clipped*y_true, axis=1)
        sample_losses = -np.log(correct_confidences)
        data_loss = np.mean(sample_losses)
        return data_loss
    
    #Can also display percentages of how many training examples were guessed correctly
    def calculateAccuracy(self, y_pred, y_true):
        predictions = np.argmax(y_pred, axis=1)
        accuracy = np.mean(predictions == y_true) * 100
        print('Accuracy: {}%'.format(accuracy))
  
class GetStuff():
    def __init__(cls):
        pass
                
    def get_Softmax(cls, inputs):
        #Axis 1 means that we deal with each training pair array at a time
        #Keepdims makes sure that any matrix multiplcaition applies to the training pair
        exp_values = np.exp(inputs - np.max(inputs, axis=1, keepdims=True))
        probabilities = exp_values / np.sum(exp_values, axis=1, keepdims=True)
        return probabilities
    
class Layer_Dense:
    def __init__(self, **kwargs):
        self._neurons = kwargs['no_neurons']
        self._activation_function = kwargs.get('activation_function')
        #Original line which works with normal array
        self.weights = np.random.randn(kwargs['no_inputs'], self._neurons)
        #Biases are a 1D array, so 1 list of a length of the number of neurons
        self.biases = np.zeros((1, self._neurons))
    def get_neurons(self):
        return self._neurons
    def forward(self, inputs):
        #OUtput unaffected by the activation function prior to any extra bedazzle
        self._ideal_output = np.dot(inputs, self.weights) + self.biases
        #OUtput affected by the activation function
        self.output = []
        for layer_output in self._ideal_output:
            self.output.append([])
            for neuron_output in layer_output:
                #trigger the activation function
                if self._activation_function.lower() == 'relu':
                    neuron_output = np.maximum(0,neuron_output)
                elif self._activation_function.lower() == 'sigmoid':
                    neuron_output = 1 / (1 + np.exp(-neuron_output))
                #Try to figure out how to implement softmax function
                self.output[-1].append(neuron_output)

  
#First, I'll need to fetch the inputs from a pre-processed dataset which I've created earlier
#I was sick of waiting, so i've utilising multithreading to find files much faster
searchPaths = [os.environ['ONEDRIVE'], os.environ['VIRTUAL_ENV'][:-5], 'D:/']
filesToSearch = ["dataset.csv", "starting_data.csv"]  
result = []

def process_directory(directory):
    directories = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file in filesToSearch:
                directories.append(os.path.join(root, file))
    return directories

with ThreadPoolExecutor() as executor:
    for rv in executor.map(process_directory, searchPaths):
        result.extend(rv)

input_directory = result[0]
data = pd.read_csv(input_directory, engine="python").iloc[:,1:]
network_inputs = data

#Then, fetch the data with the values that I'm meant to be predicting
target_directory = result[1]
target_values = pd.read_csv(target_directory, engine="python")

#Maybe add the below line to the target_values if things still don't work
#.drop(['political','age'],axis=1).iloc[:,0]

columns = target_values.columns
print("Please enter the corresponding number to the column which you would like to predict:\n")
for i in range(len(columns)):
    print(i+1, ":", columns[i])
predictor = int(input("Please make your choice:\n"))

#One hot encoding can be used here to turn categorical variables into number patterns matching the ideal variables
one_hot_encode = pd.get_dummies(target_values, columns=[target_values.columns[predictor - 1]], dtype=int).iloc[:,2:]

#I'm currently creating a neural network with an input layer and 3 hidden layers
neural = Neural_Network(inputs=network_inputs, no_layers=4, targets=one_hot_encode, learning_rate=0.15)
#Prints the structure of the network
neural.structure()
neural.train_test_split()
neural.run()