from flask import Flask,request
import pandas as pd
import numpy as np
import pickle
import flasgger
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

#load model
pickle_in = open('model_telco.pkl','rb')
model_telco = pickle.load(pickle_in)

@app.route('/')
def welcome():
    return 'Welcome to Telco Churn Prediction'

# Function for prediction
@app.route('/predict',methods=['Get'])
def predict_churn():

#Input the parameters (features) name, in(type of variable, in this case its query), type, and whether it is required

    """Telco churn prediction
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: gender
        in: query
        type: string
        required: true
      - name: SeniorCitizen
        in: query
        type: number
        required: true
      - name: Partner
        in: query
        type: string
        required: true
      - name: Dependents
        in: query
        type: string
        required: true
      - name: tenure
        in: query
        type: string
        required: true
      - name: PhoneService
        in: query
        type: string
        required: true
      - name: MultipleLines
        in: query
        type: string
        required: true
      - name: InternetService
        in: query
        type: string
        required: true
      - name: OnlineSecurity
        in: query
        type: string
        required: true
      - name: OnlineBackup
        in: query
        type: string
        required: true
      - name: DeviceProtection
        in: query
        type: string
        required: true
      - name: TechSupport
        in: query
        type: string
        required: true
      - name: StreamingTV
        in: query
        type: string
        required: true
      - name: StreamingMovies
        in: query
        type: string
        required: true
      - name: Contract
        in: query
        type: string
        required: true
      - name: PaperlessBilling
        in: query
        type: string
        required: true
      - name: PaymentMethod
        in: query
        type: string
        required: true
      - name: MonthlyCharges
        in: query
        type: string
        required: true
      - name: TotalCharge
        in: query
        type: string
        required: true
    responses:
        200:
            description: The output values
        
    """

    # Create input feature for prediction
    gender=request.args.get('gender')
    SeniorCitizen=request.args.get('SeniorCitizen')
    Partner=request.args.get('Partner')
    Dependents=request.args.get('Dependents')
    tenure=request.args.get('tenure')
    PhoneService=request.args.get('PhoneService')
    MultipleLines=request.args.get('MultipleLines')
    InternetService=request.args.get('InternetService')
    OnlineSecurity=request.args.get('OnlineSecurity')
    OnlineBackup=request.args.get('OnlineBackup')
    DeviceProtection=request.args.get('DeviceProtection')
    TechSupport=request.args.get('TechSupport')
    StreamingTV=request.args.get('StreamingTV')
    StreamingMovies=request.args.get('StreamingMovies')
    Contract=request.args.get('Contract')
    PaperlessBilling=request.args.get('PaperlessBilling')
    PaymentMethod=request.args.get('PaymentMethod')
    MonthlyCharges=request.args.get('MonthlyCharges')
    TotalCharges=request.args.get('TotalCharges')
    
    dat = [[gender, int(SeniorCitizen), Partner, Dependents, tenure,
    PhoneService, MultipleLines, InternetService, OnlineSecurity,
    OnlineBackup, DeviceProtection, TechSupport, StreamingTV,
    StreamingMovies, Contract, PaperlessBilling, PaymentMethod,
    MonthlyCharges, TotalCharges]]

    tes = pd.DataFrame(dat,columns=['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure',
       'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity',
       'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV',
       'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod',
       'MonthlyCharges', 'TotalCharges'])

    prediction = model_telco.predict(tes)

    return 'Customer churn?: '+str(prediction)

if __name__=='__main__':
    app.run()