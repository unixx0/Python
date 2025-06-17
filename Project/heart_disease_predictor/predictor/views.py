from django.shortcuts import render
import joblib
import numpy as np


#load our trained model 
model_path = 'predictor/heart_disease.pkl'
model = joblib.load(model_path)

def home(request):
    return render(request,'predictor/home.html')

def predict(request):
    if request.method == 'POST':
        try:
            #get the data from the form
            age = float(request.POST['age'])
            sex = int(request.POST['sex'])
            cp = int(request.POST['cp'])
            trestbps = float(request.POST['trestbps']) 
            chol = float(request.POST['chol'])
            fbs = int(request.POST['fbs'])
            restecg = int(request.POST['restecg'])
            thalach = float(request.POST['thalach'])
            exang = int(request.POST['exang'])
            oldpeak = float(request.POST['oldpeak'])
            slope = int(request.POST['slope'])
            ca = int(request.POST['ca'])
            thal = int(request.POST['thal'])


            #create a numpy array
            input_data = np.array([[age,sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])  

            #make a prediction
            prediction = model.predict(input_data)

            #interpret the prediction
            
            if prediction[0] == 1:
                result = 'Type 1'
            elif prediction[0] == 2:
                result = 'Type 2'   
            elif prediction[0] == 3:
                result = 'Type 3'
            elif prediction[0] == 4: 
                result = 'Type 4'
            else:
                result = 'No Heart disease'
            return render(request, 'predictor/result.html', {'result':result})
        except:
            return render(request, 'predictor/result.html', {'result':f"Error :Error message"})
        
    return render(request,'predictor/home.html')





# Create your views here.