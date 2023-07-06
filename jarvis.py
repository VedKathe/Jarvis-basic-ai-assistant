import json
import torch
import torch.nn as nn
import random
from Model import neuralNetwork
from NeuralNetwork import bag_of_words , tokenize 

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intent.json', 'r') as json_data:
    intents = json.load(json_data)
    
FILE = "TrainData.pth"
data = torch.load(FILE)

input_size = data["input_size"]
output_size = data["output_size"]
hidden_size = data["hidden_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = neuralNetwork(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

#-----------------------
Name = "Jarvis"
from Listen import Listen
from Speak import speak
from Task import NonInputExecution
from Task import InputExecution
def Main():
    sentance = Listen()
    if sentance == "sleep":
        exit()
    sentance = tokenize(sentance)
    x = bag_of_words(sentance, all_words)
    x = x.reshape(1, x.shape[0])
    x = torch.from_numpy(x).to(device)
    
    output = model(x)
    _ , predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]
    
    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    
    if prob.item() > 0.65:
        for intent in intents["intents"]:
            if tag == intent["tag"]:
                reply = random.choice(intent['responses'])  
                            
                if "time" in reply:
                    NonInputExecution(reply)  
                elif "date" in reply:
                    NonInputExecution(reply)
                elif "screenshot" in reply:
                    NonInputExecution(reply)
                elif "wikipedia" in reply:
                    InputExecution(reply, sentance)
                elif "google" in reply:
                    InputExecution(reply, sentance)
                elif "website" in reply:
                    InputExecution(reply, sentance)
                elif "application" in reply:
                    InputExecution(reply, sentance)
                else:
                    speak(reply)
while True:
    Main()