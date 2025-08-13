# Gradient Descent for linear regression
# y= wx+b
#loss function: MSE 
# loss function:MSE=(y-y_pred)**2/N
import numpy as np
# initialize the parameters
x=np.random.rand(10,1)
y=2*x+np.random.rand()
#parameters
w=0.0
b=0.0
print(x)
# learning rate how fast the algo converges means learn 
learning_rate=3


# create a gradient descent function
def gradient_descent(x,y,w,b,learning_rate):
    # calculate the derivate of the loss function w.r.t w and b
    dldw=0.0
    dldb=0.0
    N =x.shape[0]
    #loss fucntion=(y-(w*x+b))**2/N
    for xi,yi in zip(x,y):
        dldw +=-2*xi*(yi-(w*xi+b))
        dldb += -2*(yi-(w*xi+b))
        # make the update for w and b 
        w=w- learning_rate*(1/N)*dldw
        b=b-learning_rate*(1/N)*dldb

        return w,b

# make update for each parameter 
for eoch in range(800):
    w,b=gradient_descent(x,y,w,b,learning_rate)
    y_pred=w*x+b
    loss=np.divide(np.sum((y-y_pred)**2,axis=0),x.shape[0])
    print(f' loss is {loss}W ={w}and B ={b}  for epoch {eoch}')


print(x)
print(y)