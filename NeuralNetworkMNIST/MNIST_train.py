from torch.ao.nn.quantized.modules import activation

from NN_class import *
import numpy as np
import json
train_data=np.loadtxt("data/mnist_train.csv",delimiter=",",skiprows=1)
test_data=np.loadtxt("data/mnist_test.csv",delimiter=",",skiprows=1)

X_train=train_data[:,1:]
Y_train=train_data[:,0]  #labels
Y_train=list(map(int,Y_train))
Y_train = np.array(Y_train)

X_test=test_data[:,1:]
Y_test=test_data[:,0]
Y_test=list(map(int,Y_test))
Y_test = np.array(Y_test)

#normalization
X_train=X_train/255.0
X_test=X_test/255.0


#test
'''
layer1=Layer_Dense(784,128)
activation1=Activation_ReLU()
layer2=Layer_Dense(128,10)
activation2=Activation_Softmax()

X_sample=X_train[:1]

layer1.forward(X_sample)
activation1.forward(layer1.output)
layer2.forward(activation1.output)
activation2.forward(layer2.output)

print("test 1")
print(activation2.output)
print("sum")
print(np.sum(activation2.output,axis=1))

'''
epoch=2000
layer1=Layer_Dense(784,128)
layer2=Layer_Dense(128,10)
activation1=Activation_ReLU()
activation2=Activation_Softmax()
loss_func=Loss_CategoricalCrossentropy()
opt=Optimizer()

X_samples=X_train[:100]
y_samples=Y_train[:100]


#layer1.forward(X_samples)
#activation1.forward(layer1.output)
#layer2.forward(activation1.output)
#activation2.forward(layer2.output)
#print(activation2.output)



for i in range(epoch):

    #tutaj robimy forward, wrzucamy wszytsko do sieci
    layer1.forward(X_samples)
    activation1.forward(layer1.output)
    layer2.forward(activation1.output)
    activation2.forward(layer2.output)


    loss=loss_func.calculate(activation2.output,y_samples)

    print(loss)

    dvalues=loss_func.backward(activation2.output,y_samples)
    layer2.backward(dvalues)
    activation1.backward(layer2.dinputs)
    layer1.backward(activation1.dinputs)
    opt.update_params(layer1)
    opt.update_params(layer2)


weights_biases={}
weights_biases["layer1"]={"weight":layer1.weights.tolist(),"bias":layer1.biases.tolist()}
weights_biases["layer2"]={"weight":layer2.weights.tolist(),"bias":layer2.biases.tolist()}

with open("weights_biases.json","w") as f:
    json.dump(weights_biases,f)
















