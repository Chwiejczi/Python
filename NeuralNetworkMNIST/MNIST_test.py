#from MNIST_train import activation1
from NN_class import *
import numpy as np
import json

test_data=np.loadtxt("data/mnist_test.csv",delimiter=",",skiprows=1)
X_test=test_data[:,1:]
Y_test=test_data[:,0]
Y_test=list(map(int,Y_test))
Y_test = np.array(Y_test)
X_test=X_test/255.0

with open("weights_biases.json","r") as f:
    data=json.load(f)

layer1_weights=np.array(data["layer1"]["weight"])
layer1_biases=np.array(data["layer1"]["bias"])
layer2_weights=np.array(data["layer2"]["weight"])
layer2_biases=np.array(data["layer2"]["bias"])
act1=Activation_ReLU()
act2=Activation_Softmax()

layer1=Layer_Dense(784,128)
layer2=Layer_Dense(128,10)

layer1.weights=layer1_weights
layer1.biases=layer1_biases
layer2.weights=layer2_weights
layer2.biases=layer2_biases

y_sample=Y_test[8]
x_sample=X_test[8]

layer1.forward(x_sample)
act1.forward(layer1.output)
layer2.forward(act1.output)
act2.forward(layer2.output)

print("probabilities")
print(act2.output)
print(f'\n y_sample={y_sample}')
