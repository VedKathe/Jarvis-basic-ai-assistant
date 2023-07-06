import torch.nn as nn   

class neuralNetwork(nn.Module):
    
    def __init__(self, input_nodes, hidden_nodes, output_nodes):
        super(neuralNetwork, self).__init__()
        self.hidden = nn.Linear(input_nodes, hidden_nodes)
        self.hidden2 = nn.Linear(hidden_nodes, hidden_nodes)
        self.output = nn.Linear(hidden_nodes, output_nodes)
        self.reLU = nn.ReLU()
        
    def forward(self, x):
        output = self.hidden(x)
        output = self.reLU(output)
        output = self.hidden2(output)
        output = self.reLU(output)
        output = self.output(output)
        output = self.reLU(output)
        return output