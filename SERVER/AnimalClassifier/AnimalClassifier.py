#CNN For 90 Animal Classifications
import os
import torch
from torch.utils.data import DataLoader, random_split
from torchvision.datasets import ImageFolder
from torchvision.transforms import transforms

from Utils import show_image

#normalize Pictures Train/Test
transform = transforms.Compose([
    transforms.Resize((224, 224)),  # Resize the images to (224, 224)
    transforms.ToTensor(),  # Convert the images to tensors
    transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])  # Normalize the images
])


#dict for relating animal to subfolder
animal_types = {}

root = "./AnimalsDataSet"

#iterates over each subdir and prints and updates dict with idx
#filters files in subdirs through list comp
subdirs = [d for d in os.listdir(root) if os.path.isdir(os.path.join(root, d))]
animal_idx = 0;
for subdir in subdirs:
    animal_types[animal_idx] = subdir
    animal_idx+=1


#assigns labels
dataset = ImageFolder(root=root,transform=transform)

print("length of the dataset is:", len(dataset))

train_data_size = int(len(dataset)* 0.8)
test_data_size = len(dataset) - train_data_size
#80/20 SPlit of train/test Data
train_data, test_data = random_split(dataset,[train_data_size,test_data_size])

print("length of Train Data Set: " , len(train_data))
print("length of Test Data Set ", len(test_data))

#batch size of 32 due to low Sample Size of Animal Photos
test_load = DataLoader(test_data,batch_size=32,shuffle=False,num_workers=0)
train_load = DataLoader(train_data,batch_size=32,shuffle=True,num_workers=0)

weight_decay = 0.01

