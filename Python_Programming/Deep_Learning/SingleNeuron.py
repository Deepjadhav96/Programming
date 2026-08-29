import numpy as np

#Step1: Define input features i.e X
                #[x1 , x2 , x3]
input = np.array([2.0,3.0,4.0])
print("X: ",input)

#Step2: Define weight i.e w
               #   [w1, w2, w3]
weights = np.array([0.5,0.3,0.2])
print("Weights: ",weights)

#Step3: Define bias i.e b
#      b
bias = 1.0
print("bias :",bias)

#Step4: Calculate weighted sum
#z = x1w1 + x2w2 + x3w3 + b
#z = (2.0*0.5) + (3.0*0.3)+ (4.0*0.2) + 1.o

z = np.dot(input,weights)  + bias
print("Z :",z)

#Step5: Activation function (ReLU)

def ReLU(x):
    return max(0,x)

#Step6: Final output i.e y

Y = ReLU(z)
print("Y :",Y)


