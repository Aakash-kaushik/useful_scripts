import torch, time, copy
import torch.nn as nn
import torch.optim as optim
import numpy as np
import torchvision  
from torchvision import datasets, models, transforms 
import os 

model_path = "<Model path here>"
val_path = "<Val dataset path>"

device = torch.device("gpu" if torch.cuda.is_available() else "cpu")

transform = transforms.Compose([transforms.Resize((224, 224)),
                                          transforms.ToTensor(),
                                          transforms.Normalize([0.485, 0.456, 0.406],[0.229, 0.224, 0.225])
                                        ])

val_datasets = datasets.ImageFolder(val_path, transform)
 
valloaders = torch.utils.data.DataLoader(val_datasets, batch_size=16, shuffle=True, num_workers=4)

nb_classes = 6
eval_model=torch.load(model_path, map_location=device)
eval_model.eval()

confusion_matrix = torch.zeros(nb_classes, nb_classes)
with torch.no_grad():
    for i, (inputs, classes) in enumerate(valloaders):
        inputs = inputs.to(device)
        classes = classes.to(device)
        outputs=eval_model(inputs)
        _, preds = torch.max(outputs, 1)
        for t, p in zip(classes.view(-1), preds.view(-1)):
                confusion_matrix[t.long(), p.long()] += 1
print(val_datasets.classes)
print("- "*15)
print(confusion_matrix)
print("- "*15)
print(confusion_matrix.diag()/confusion_matrix.sum(1))