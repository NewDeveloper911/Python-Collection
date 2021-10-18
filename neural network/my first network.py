import numpy as np
#These will represent neurons in my input(first true) layer of neurons
inputs = [[1.2, 5.2, 2.9,0.7],
          [0.6,0.23,0.2,0.4],
          [1.5,0,9,2,0.5],
          [1.4, 0.5, 0.2,0.3]]
#Each input have a weight. These below are the input of 3 output layer neurons
weights = [[1,0.4,0.8,1],[0.7,0.6,0.3,2],[0.5,0.4,0.3,0.9]]
#Each neuron has its own unique bias
biases = [0.3,0.8,0.5]

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
output = np.dot(weights, inputs) + biases
print(output)
