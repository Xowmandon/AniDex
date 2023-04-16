import torch
from .utils import load_model
import torchvision.transforms as transforms
from torchvision.models import resnet18
from PIL import Image
import json

def ClassifyPlant(plant_image):
    
    pil_image = Image.open(plant_image).convert('RGB')
    input_image_tensor = transform_image(pil_image)
    input_plant = input_image_tensor.unsqueeze(0)

    pil_image.close()

    model.eval()
    #disables gradient to make prediction, easier computation and memory
    with torch.no_grad():
        output = model(input_plant)

    #Gets Predicted Species
    _, predicted = torch.max(output, 1)

    # 0-1 Probabilty of all Species
    probability_plant_species = torch.nn.functional.softmax(output[0], dim=0)

    #takes top 5 Propabilties (For Human Feedback to Report which one is mostly correct, if model is incorrect)
    topk_probs, topk_indices = torch.topk(probability_plant_species , k=5)

    #takes the highest probability
    highest_species_prob = topk_probs[0].item()

    classification = (classes[predicted],str("{:.2f}".format((highest_species_prob *100))) + "%")
    return classification
    #print("Predicted: " + classes[predicted] + " Probability: " + str("{:.2f}".format((highest_species_prob *100))) + "%")
    #print()

filename = './PlantClassifier/resnet18_weights_best_acc.tar' # pre-trained model path
use_gpu = False  # load weights on the gpu
model = resnet18(num_classes=1081) # 1081 classes in Pl@ntNet-300K


#load model until selected weights
load_model(model, filename=filename, use_gpu=use_gpu)

#Associates Classes from JSON as Dict 
with open('./PlantClassifier/plantnet300K_species_id_2_name.json') as f:
    species_idx_2_name = json.load(f)



#List of Classes 
classes = list(species_idx_2_name.values())
#print(species_idx_2_name)


#image dimensions for transform
image_size = 256
crop_size = 224

#transforms input image to fit Model Expectations
transform_image = transforms.Compose([transforms.Resize(size=image_size), transforms.CenterCrop(size=crop_size),
                                             transforms.ToTensor(), transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                                                                         std=[0.229, 0.224, 0.225])])

#plant_image = "./lavender-1595581__480.jpg" # Simple Test Case
#print(ClassifyPlant(plant_image))



