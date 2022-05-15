
import torch
import torch.nn as nn
from torch.optim import SGD

device = 'cuda' if torch.cuda.is_available() else 'cpu'

x = [[1, 2], [3, 4], [5, 6], [7, 8]]
y = [[3], [7], [11], [15]]

x = torch.tensor(x).float()
y = torch.tensor(y).float()

x = x.to(device)
y = y.to(device)


class MyNeuralNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.input_to_hidden_layer = nn.Linear(2,8)
        self.hidden_layer_activation = nn.ReLU()
        self.hidden_to_output_layer = nn.Linear(8,1)

    def forward(self, x):
        x = self.input_to_hidden_layer(x)
        c = self.hidden_layer_activation(x)
        x = self.hidden_to_output_layer(x)
        return x


mynet = MyNeuralNet().to(device)

loss_func = nn.MSELoss()
opt = SGD(mynet.parameters(), lr = 0.001)

loss_history = []

for _ in range(50):
    opt.zero_grad()
    loss_value = loss_func(mynet(x), y)
    loss_value.backward()
    opt.step()
    loss_history.append(loss_value)

print(loss_history)