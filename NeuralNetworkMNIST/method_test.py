import numpy as np

from NN_class import *


#test Layer Dense
print("test Layer Dense")
X=[[1,2,3,2.5],[2.0,5.0,-1.0,2.0],[-1.5,2.7,3.3,-0.8]]
layer1=Layer_Dense(4,5)
layer2=Layer_Dense(5,2)
layer1.forward(X)
layer2.forward(layer1.output)
print(layer2.output)

#test ReLu
print("test ReLu")
relu=Activation_ReLU()
relu.forward(X)
print(relu.output)

#test softmax

print("test softmax")
softMax=Activation_Softmax()
softMax.forward(X)
print(softMax.output)
sum_row=np.sum(softMax.output,keepdims=True,axis=1)
print("sum in rows")
print(sum_row)

#test Loss
print("test Loss")
loss=Loss_CategoricalCrossentropy()
y_pred = np.array([
    [0.7, 0.2, 0.1],
    [0.1, 0.8, 0.1]
])
#print("aaaa")
#print(len(y_pred))
y_true = np.array([0, 1])
print(loss.forward(y_pred, y_true))
print("loss")
print(loss.calculate(y_pred, y_true))



