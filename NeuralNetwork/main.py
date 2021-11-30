import numpy as np
import matplotlib.pyplot as plt
from neuralnetwork.datasets.util import load_monk
from neuralnetwork.model.Layer import Layer
from neuralnetwork.model.NeuralNetwork import NeuralNetwork
from sklearn.metrics import confusion_matrix

from neuralnetwork.regularization import L2, L1


X_train, X_test, y_train, y_test = load_monk(3)

n_features = X_train.shape[1]

batch_size = len(X_train)
model = NeuralNetwork(epochs=300,batch_size=batch_size, lr=0.5,momentum=0.8, regularization='l2')
input_layer = Layer(n_features,3, activation_function='relu', weights_init='random_init')
hidden_layer = Layer(3,1, weights_init='xavier_uniform')
model.add_layer(input_layer)
model.add_layer(hidden_layer)
model.fit(X_train, y_train) 
model.train()

#plt.plot(model.loss)
#plt.show()

print(confusion_matrix(y_train, np.round(model.layers[-1].output)))
print(model.loss[-1])

print()

y_preds = np.round(model.predict(X_test))
error = y_test - y_preds
mse = (np.sum((error)**2))/len(y_test)
print(confusion_matrix(y_test, y_preds))
print(mse)



