import json
import os
from flask import Flask, request, make_response, jsonify
from PIL import Image
from werkzeug.utils import secure_filename
from PlantClassifier import PlantClassifier
from flask_ngrok import run_with_ngrok


#Plant Classifier Model
from PlantClassifier import PlantClassifier

app = Flask(__name__)
if __name__ == '__main__':
    app.run(port=5002)



EXTENSIONS_ALLOWED = ["png","heic","jpg","jpeg"]
def file_allowed(filename):
    return "." in filename and filename.rsplit('.', 1)[1].lower() in EXTENSIONS_ALLOWED

os.makedirs(os.path.join(app.instance_path, 'ANIMAL_UPLOADS'), exist_ok=True)
os.makedirs(os.path.join(app.instance_path, 'PLANT_UPLOADS'), exist_ok=True)
os.makedirs(os.path.join(app.instance_path, 'ANIMAL_UPLOADS_PREDICTION'), exist_ok=True)
os.makedirs(os.path.join(app.instance_path, 'PLANT_UPLOADS_PREDICTION'), exist_ok=True)



@app.route("/")
def home():
    return "Hello, Joshua!"

@app.route("/signup")
def signup():
    return "Successfully Signed up !"


@app.route("/animal", methods=["POST"])
def receive_animal_photo():
    if request.files:
        animal_photo = request.files["image"]
        if file_allowed(animal_photo):
            animal_photo.save(os.path.join(app.instance_path, "ANIMAL_UPLOADS"), secure_filename(animal_photo.filename))


    return "Animal Name"

plants_uploades_count = 0

@app.route("/plant", methods=["POST"])
def receieve_plant_photo():

    if request.files:
        plant_photo_storage = request.files["image"]
        plant_photo_prediction = request.files["image"]
        #copy of original photo, to put into predicitions with names


        #Security: Enforces Secure Filename
        #Handles proper Paths for Saving and Writing Files
        plant_uploads_dir = os.path.join(app.instance_path,"PLANT_UPLOADS")
        secure_plant_file = secure_filename(plant_photo_storage.filename)
        plant_image_path = os.path.join(plant_uploads_dir, secure_plant_file)

        #Saves Submitted Photo to br passed to classifier
        plant_photo_storage.save(plant_image_path)


        #Classifies Plant and Saves In Tuple (0 -> Species, 1 -> Probability)
        Plant_Preidiction = PlantClassifier.ClassifyPlant(plant_image_path)
        
        probability = float(Plant_Preidiction[1].rstrip("%"))
        #saves Good Predictions in Folder, with Predicted Species and Photo
        if probability >= 80:
            plant_photo_prediction_path = os.path.join(app.instance_path,"PLANT_UPLOADS_PREDICTION", 
                                            Plant_Preidiction[0].replace(" ", "-") + ".jpg")
            plant_photo_prediction.save(plant_photo_prediction_path)

        #enforces closure of submitted Image
        plant_photo_storage.close()


        #Serializes prediction into JSON
        json_plant_classification = json.dumps(Plant_Preidiction)

        #writes JSON into Predictions for future analysis
        with open("PlantClassifications.json", "w") as PC:
            PC.write(json_plant_classification)


        #return "OK!",200
        return make_response(json_plant_classification,200)
    else:
        return make_response("Bad Request or Invalid Operation",400)

def output_likely_Animal(animal_image):

    animal_species = None
    return animal_species
    

def output_likely_Plant(plant_image):



    plant_species = None
    return plant_species

