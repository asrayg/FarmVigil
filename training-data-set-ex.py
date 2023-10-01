#Learning how to train our own data sets!!! Not gonna use it but fun to learn

import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms

# Define a simple CNN architecture
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(3, 16, kernel_size=3)
        self.fc1 = nn.Linear(16 * 30 * 30, 2)  # 2 classes (healthy and diseased)

    def forward(self, x):
        x = self.conv1(x)
        x = x.view(x.size(0), -1)
        x = self.fc1(x)
        return x

# Define data transforms and create data loaders
transform = transforms.Compose([transforms.Resize((32, 32)),
                                transforms.ToTensor()])
train_dataset = datasets.ImageFolder('train_data', transform=transform)
train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=64, shuffle=True)

# Initialize the model and optimizer
model = Net()
optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9)

# Train the model
for epoch in range(epochs):
    for batch_idx, (data, target) in enumerate(train_loader):
        optimizer.zero_grad()
        output = model(data)
        loss = nn.CrossEntropyLoss()(output, target)
        loss.backward()
        optimizer.step()
