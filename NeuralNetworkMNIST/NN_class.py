import numpy as np
np.random.seed(0)
class Layer_Dense:
    def __init__(self,n_inputs,n_neurons):
        self.weights = 0.10*np.random.randn(n_inputs,n_neurons)
        self.biases=np.zeros((1,n_neurons))
    def forward(self,inputs):
        self.inputs=inputs
        self.output=np.dot(inputs,self.weights)+self.biases

    def backward(self,dvalues):
        self.dweights=np.dot(self.inputs.T,dvalues)
        self.dbiases=np.sum(dvalues,axis=0,keepdims=True)
        self.dinputs=np.dot(dvalues,self.weights.T)



class Activation_ReLU:
    def forward(self,inputs):
        self.output=np.maximum(0,inputs)
        self.inputs=inputs
    def backward(self,dvalues):
        self.dinputs=dvalues.copy()
        self.dinputs[self.inputs<=0]=0   #mowi nam gdzie będzimy mogli operowac na wagach, tam gdzie zadzialala funkcja aktywacji

class Activation_Softmax:
    def forward(self,inputs):
        exp_values=np.exp(inputs-np.max(inputs,axis=1,keepdims=True))
        probabilities=exp_values/np.sum(exp_values,axis=1,keepdims=True)
        self.output=probabilities
class Loss:
    def calculate(self,output,y):
        sample_losses=self.forward(output,y)
        data_loss=np.mean(sample_losses)
        return data_loss
class Loss_CategoricalCrossentropy(Loss):
    def forward(self,y_pred,y_true):
        samples=len(y_pred)
        y_pred_clipped=np.clip(y_pred,1e-7,1-1e-7)  
        if len(y_true.shape)==1:
            correct_confidences=y_pred_clipped[range(samples),y_true]
        else :
            correct_confidences=np.sum(y_pred_clipped*y_true,axis=1)

        negative_log_likelihood=-np.log(correct_confidences)
        return negative_log_likelihood
    def backward(self,y_pred,y_true):
        n=y_pred.shape[0]
        size_of_pred=y_pred.shape[1]

        if len(y_true.shape)==1:
            y_true_changed=np.zeros((n,size_of_pred))
            for i in range(n):
                y_true_changed[i,y_true[i]]=1
            grad=(y_pred-y_true_changed)/n
            return grad
        else:
            grad=(y_pred-y_true)/n
            return grad




class Optimizer:
    def __init__(self,learning_rate=0.001):
        self.learning_rate=learning_rate
    def update_params(self,layer):
        layer.weights -=self.learning_rate*layer.dweights
        layer.biases -=self.learning_rate*layer.dbiases

