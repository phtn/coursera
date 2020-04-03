import torch
import numpy as np
import matplotlib.pyplot as plt

torch.manual_seed(1)

X = torch.arange(-3,3,0.01).view(-1,1)
f = 1 * X - 1
Y = f + 0.1 * torch.randn(X.size()) 


plt.plot(Y)
plt.show()

