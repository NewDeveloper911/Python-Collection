import numpy as np
import os
import pandas as pd
import csv
class Neural_Network:
    def __init__(self,**kwargs):
        self._network = []
        self._inputs = kwargs['inputs']
        self._testing_data = None
        self._target_values = kwargs['targets']

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
        inputs = self._network[-1].get_neurons()
        self._network.append(Layer_Dense(no_inputs=inputs,no_neurons=outputs,activation_function=activation_function))

    def structure(self):
        structure = []
        for layer in self._network:
            structure.append(layer.get_neurons())
        print("The structure of this neural network is:", structure)
    def run(self):
        #Start by putting initial inputs into the input layer
        self._network[0].forward(self._inputs)
        for i in range(len(self._network)-1):
            #Using the previous layer's outputs as the next layer's inputs
            self._network[i+1].forward(self._network[i].output)
        print("The network's outputs were:", self._network[-1].output)

    def train_test_split(self):
        #Split the available dataset into training data and testing data
        split = float(input("Enter a decimal between 0 and 1 to represent the fraction of data to be used for testing:\n"))
        assert split >= 0 and split <=1
        data_split = round(split * len(self._inputs.columns.values))
        training_data = self._inputs.iloc[:data_split]
        testing_data = self._inputs.iloc[data_split:]
        self._inputs = training_data
        self._testing_data = testing_data

    def evaluate(self):
        final_outputs = self._network[-1].output
        total_age_error = 0.0
        total_gender_error = 0.0
        total_politic_error = 0.0
        for i in len(final_outputs):
            #Figure out a way to get the final outputs  unaffected by the activation function or I affect the 
            #target values with the same activation function
            gender = final_outputs[i][0]
            political_affiliations = final_outputs[i][1]
            age = final_outputs[i][2]

            target_gender = self._target_values.iloc[i][0]
            target_political_affiliations = self._target_values.iloc[i][1]
            target_age = float(self._target_values.iloc[i][2])

            age_error = abs(target_age - age)
            politic_error = abs(target_political_affiliations-political_affiliations)
            gender_error = abs(target_gender-gender)
  
class GetStuff():
    def __init__(cls):
        pass
    def get_directory(cls,file_name):
        for root, dirs, files in os.walk(r'/'):
            for name in files:
                if name == file_name:
                    return os.path.abspath(os.path.join(root, name))
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
                self.output[-1].append(neuron_output)

  
#First, I'll need to fetch the inputs from a pre-processed dataset which I've created earlier
input_directory = GetStuff().get_directory("dataset.csv")
data = pd.read_csv(input_directory, engine="python")
network_inputs = data
#Then, fetch the data with the values that I'm meant to be predicting
target_directory = GetStuff().get_directory("starting_data.csv")
target_values = pd.read_csv(target_directory, engine="python")
#I'm currently creating a neural network with an input layer and 3 hidden layers
neural = Neural_Network(inputs=network_inputs, no_layers=4, targets=target_values)
#Prints the structure of the network
neural.structure()
neural.train_test_split()
neural.run()