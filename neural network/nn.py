import numpy as np
import os
import pandas as pd
from concurrent.futures import ThreadPoolExecutor

class Neural_Network:
    def __init__(self,**kwargs):
        self._network = []
        self._inputs = kwargs['inputs']
        self._testing_data = None
        self._target_values = kwargs['targets']
        self._learning_rate = kwargs['learning_rate']

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
        self.structure = []
        for layer in self._network:
            self.structure.append(layer.get_neurons())
        print("The structure of this neural network is:", self.structure)

    def run(self, **kwargs):
        # Prints the structure of the network
        neural.structure()
        neural.train_test_split()

        epochs = kwargs['epochs']
        for i in range(epochs):
            for b in range(len(self.batches)):
                for i in range(len(self._network)):
                    if i != 0:
                        #Using the previous layer's outputs as the next layer's inputs
                        self._network[i].forward(self._network[i-1].outputs)
                    else:
                        #Forward pass
                        self._network[0].forward(self.batches[b].values)

                #Here, I could run the cost function to see how the program is performing
                totalCost = self.totalCost(self.batches[b].values, self.expectedBatchValues[b].values)
                accuracy = GetStuff().calculateAccuracy(self.batches[b].values, self.expectedBatchValues[b].values)
                print("Batch number {} in epoch:\n\tCost: {}\n\tAccuracy: {}%".format(b+1,totalCost,accuracy))

                self.learn(self.batches[b], self.expectedBatchValues[b])

        #//TESTING PHASE
        for i in range(len(self._network)):
            if i != 0:
                #Using the previous layer's outputs as the next layer's inputs
                self._network[i].forward(self._network[i-1].outputs)
            else:
                #Start by putting initial inputs into the input layer
                self._network[0].forward(self._testing_data)

        print("The network's testing outputs were:", self._network[-1].output)

    def train_test_split(self):
        #Split the available dataset into training data and testing data
        split = float(input("Enter a decimal between 0 and 1 to represent the fraction of data to be used for training:\n"))
        assert split >= 0 and split <=1
        data_split = round(split * len(self._inputs))
        training_data = self._inputs.iloc[0:data_split]
        testing_data = self._inputs.iloc[data_split:]
        self._inputs = training_data
        self._testing_data = testing_data

        self.batches = []
        self.expectedBatchValues = []
        batchNum = int(input("How many data points do you want to be in each mini-batch?\n"))
        assert batchNum > 1 and batchNum < len(self._inputs)
        batchSize = round(len(self._inputs) / batchNum)
        start = 0
        for i in range(len(self._inputs)):
            #Theoretically time to create another batch
            if i != 0 and i % batchSize == 0:
                self.batches.append(self._inputs.iloc[start: i])
                self.expectedBatchValues.append(self._target_values.iloc[start: i])
                start = i 
        try:
            #Collecting any leftovers and adding them to another batch
            self.batches.append(self._inputs.iloc[start:-1])
            self.expectedBatchValues.append(self._target_values.iloc[start: i])
            print("Clean-up crew all aboard")
        except:
            #Already added all of the data neatly into the batches
            print("No more batch-making for us to do, sir.")
            pass

    
    def learn(self, trainingBatch, expectedValues):
        #Backpropagation happens here
        #I could use threading to run several batches simultaneously to improve speed
        for value in range(len(trainingBatch)):
            self.updateAllGradients(trainingBatch.iloc[value,:],expectedValues.iloc[value,:])

        #Adjust all gradients
        for layer in self._network:
            layer.backward(self._learning_rate / len(trainingBatch))

        #Then reset the cost gradients - next batch can aid in guiding those for faster backpropagation
        for layer in self._network:
            layer.clearGradients()

    def updateAllGradients(self, dataPoint, expectedValues):
        #Forward pass
        self._network[0].forward(dataPoint)
        for i in range(len(self._network)-1):
            #Using the previous layer's outputs as the next layer's inputs
            outputs = self._network[i+1].forward(self._network[i].outputs)
        outputLayer = self._network[-1]

        #Updates the gradients of the output layer
        print(expectedValues)
        nodeValues = outputLayer.calcFinalNodeValues(expectedValues)
        outputLayer.updateGradients(nodeValues)

        #Updates the gradients of the hidden layer
        for i in range(len(self._network) - 2, 0, -1):
            hiddenLayer = self._network[i]
            nodeValues = hiddenLayer.calcHiddenNodeValues(self._network[i+1], nodeValues)
            hiddenLayer.updateGradients(nodeValues)

    #Basically our loss function
    def cost(self, dataPoint, expectedValues):
        #ExpectedValues should not be a one-hot encoded vector of the categories whih I am predicting for each row in the database (the dataPoint) - at least that's not how Sebastien Lague did it
        for i in range(len(self._network)):
            if i != 0:
                #Using the previous layer's outputs as the next layer's inputs
                self._network[i].forward(self._network[i-1].outputs)
            else:
                #Forward pass
                self._network[0].forward(dataPoint)

        cost = 0
        #Probably due to encapsulation but the getter refused to be got, so this is a workaround
        for i in range(len(self._network[-1].outputs)):
            #Need the compare the values at the index in the expected values which is a one
            #Basically one-hot encoding the expected categories and using those to calculate error
            #Could do automatically by storing the header names
            one_hot = expectedValues.argmax(axis=1, keepdims=True)[i]
            cost += self._network[-1].nodeCost(self._network[-1].outputs[i][one_hot], expectedValues[i][one_hot])
        return cost
    
    def totalCost(self, input_data, expectedValues):
        totalCost = 0
        #Apparently the dataPoint contains both the raw inputs meant for the first layer only combined with the softmax values?
        for dataPoint in input_data:
            totalCost += self.cost(dataPoint, expectedValues)
        return totalCost / len(input_data)

searchPaths = [os.environ['ONEDRIVE'], os.environ['VIRTUAL_ENV'][:-5], 'D:/']
filesToSearch = ["dataset.csv", "starting_data.csv"]        
class GetStuff():
    def __init__(cls):
        #Can be altered to suit Apple or Linux, but it's your fault if you use Apple.
        cls.searchPaths = ['C:/Users/Nana Yaw/OneDrive', 'C:/Users/Nana Yaw/Documents', 'D:/', "C:/Users/Nana Yaw/Python-Collection"]
        cls.filesToSearch = []

    def get_directory(cls, directory):
        directories = []
        for root, _, files in os.walk(directory):
            for file in files:
                if file in filesToSearch:
                    directories.append(os.path.join(root, file))
        return directories

    def get_softmax(cls,inputs):
        #Axis 1 means that we deal with each training pair array at a time
        #Keepdims makes sure that any matrix multiplcaition applies to the training pair
        exp_values = np.exp(inputs - np.max(inputs, axis=1, keepdims=True))
        probabilities = exp_values / np.sum(exp_values, axis=1, keepdims=True)
        return probabilities

    def get_softmax_derivative(cls, softmaxValues):
        #Calculating the derivative of softmax using np arrays is a pain but hopefully, this link helps:
        #https://stackoverflow.com/questions/36279904/softmax-derivative-in-numpy-approaches-0-implementation/36280783#36280783
        #This too can provide extra information: https://stats.stackexchange.com/questions/453539/softmax-derivative-implementation

        #In this answer, softmaxValues should be the activation values of the layer which I'm trying to find the softmax derivative of

        J = - softmaxValues[..., None] * softmaxValues[:, None, :] # off-diagonal Jacobian
        iy, ix = np.diag_indices_from(J[0])
        J[:, iy, ix] = softmaxValues * (1. - softmaxValues) # diagonal
        return J.sum(axis=1) # sum across-rows for each sample
    
    #Can also display percentages of how many training examples were guessed correctly
    def calculateAccuracy(self, y_pred, y_true):
        predictions = np.argmax(y_pred, axis=1)
        accuracy = np.mean(predictions == y_true) * 100
        return accuracy

class Layer_Dense:
    def __init__(self, **kwargs):
        self.inputs = []
        self.outputs = []
        self._neurons = kwargs['no_neurons']
        self._activation_function = kwargs.get('activation_function')
        #Original line which works with normal array
        self.weights = np.random.randn(kwargs['no_inputs'], self._neurons)
        #Biases are a 1D array, so 1 list of a length of the number of neurons
        self.biases = np.zeros((1, self._neurons))

        #The cost values required for each layer
        self.weightCosts = np.random.randn(kwargs['no_inputs'], self._neurons)
        self.biasCosts = np.random.randn(1, self._neurons)

    def get_neurons(self):
        return self._neurons

    def forward(self, inputs):
        self.inputs = inputs
        preActivationOutputs =  np.dot(inputs, self.weights) + self.biases
        if self._activation_function == "softmax":
            self.outputs = GetStuff().get_softmax(preActivationOutputs)
            return self.outputs
        else:
            #Can later implement other activation functions here like leaky ReLU
            pass

    def clearGradients(self):
        #Clears the cost gradients for the next batch to do their part
        self.weightCosts = np.zeros(len(self.inputs), self._neurons)
        self.biasCosts = np.zeros(1, self._neurons)

    def backward(self, learning_rate):
            #Alters the gradients of the weights and biases during learning
            for i in self.outputs:
                self.biases[i] -= self.biasCosts[i] * learning_rate
                for j in self.get_neurons():
                    self.weights[j,i] -= self.weightCosts[j,i] * learning_rate
    
    def updateGradients(self, nodeValues):
        #Index 0 is to make sure that it applies to the nodes themselves and not the batch no
        for i in range(self.outputs[0]):
            for j in range(self.get_neurons):
                #Evalutates the partial derivative (cost / weight) of current connection
                derivativeWeightCost = self.inputs[j] * nodeValues[i]
                #Derivative is being added to array here because ultimately, it will be used
                #to calculate the average gradident across all of the data in the training batch
                self.weightCosts[j,i] += derivativeWeightCost

            #Bias' derivative is just 1 - we aren't multiplying it by anything
            derivativeBiasCost = nodeValues[i]
            self.biasCosts[i] += derivativeBiasCost

    def nodeCost(self, outputActivation, expectedOutput):
        #Basically the MSE approach of calculating error - Mean Squared Error
        return (outputActivation - expectedOutput) ** 2
    
    def nodeCostDerivative(self, outputActivation, expectedOutput):
        return 2 * (outputActivation - expectedOutput)
    
    def calcFinalNodeValues(self, expectedValues):
        nodeValues = []
        for i in len(expectedValues):
            costDerivative = self.nodeCostDerivative(self.outputs[i], expectedValues[i])
            #Assuming that the user chose to use the sigmoid function - can change for other activation functions later
            #If we used the derivative as just 1 / (1 - e**weighted-Input), then the derivative would take in the weightedInputs
            activationDerivative = GetStuff().get_softmax_derivative(self.outputs)
            nodeValues[i] = costDerivative * activationDerivative
        return nodeValues
    
    def calcHiddenNodeValues(self, oldLayer, oldNodeValues):
        newnodeValues = []
        for i in len(self.outputs[0]):
            newnodeValue = 0
            for j in range(len(oldNodeValues)):
                weightedInputDerivative = oldLayer.weights[i,j]
                newnodeValue = weightedInputDerivative * oldNodeValues[j]
            newnodeValue *= GetStuff.get_softmax_derivative(self.outputs[i])
            newnodeValues[i] = newnodeValue
        return newnodeValues

#First, I'll need to fetch the inputs from a pre-processed dataset which I've created earlier
#I was sick of waiting, so i've utilising multithreading to find files much faster
result = []

with ThreadPoolExecutor() as executor:
    for rv in executor.map(GetStuff().get_directory, searchPaths):
        result.extend(rv)

input_directory = result[0]
data = pd.read_csv(input_directory, engine="python").iloc[:,1:]
network_inputs = data

#Then, fetch the data with the values that I'm meant to be predicting
target_directory = result[1]
target_values = pd.read_csv(target_directory, engine="python")

#Maybe add the below line to the target_values if things still don't work
#.drop(['political','age'],axis=1).iloc[:,0]

#One hot encoding can be used here to turn categorical variables into number patterns matching the ideal variables
one_hot_encode = pd.get_dummies(target_values, columns=['gender'], dtype=int).iloc[:,2:]

#I'm currently creating a neural network with an input layer and 3 hidden layers
neural = Neural_Network(inputs=network_inputs, learning_rate=0.15, no_layers=4, targets=one_hot_encode)
neural.run(epochs=500)