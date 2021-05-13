from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import flasgger
from flasgger import Swagger
import pickle
#from pickle import load
#import sklearn
#from sklearn.preprocessing import StandardScaler


#initialize flask and swagger
app = Flask(__name__)
Swagger(app)


#load pickle file
pickle_file_open = (open("random_forest_regression_model.pkl", "rb"))
rf_random=pickle.load(pickle_file_open)

# Creating the Base Route
@app.route('/', methods=['GET'])
def welcome_message() :
    try :
        return "Welcome to Praxis",200
    except Exception as e :
        return "something went wrong",400
    
    
#Creating route for prediction
@app.route('/predict', methods=['GET'])
def predict() :
    
    """Testing of prediction using test file
    -------------------
    parameters:
        - name : Present_Price
          in : query
          type : number
          description : Enter price in number
          required : true 
        - name : Kms_Driven
          in : query
          type : number
          description : Enter KMs in number
          required : true 
        - name : Owner
          in : query
          type : string
          description : Enter no. of previous owners (0, 1 or 3)
          required : true 
        - name : no_year
          in : query
          type : number
          description : Enter total no. of years car is used (current yr is 2020)
          required : true 
        - name : Fuel_Type_Diesel
          in : query
          type : number
          description : Enter 1 if diesel else enter 0
          required : true 
        - name : Fuel_Type_Petrol
          in : query
          type : number
          description : Enter 1 if petrol else enter 0
          required : true 
        - name : Seller_Type_Individual
          in : query
          type : string
          description : Enter 1 if individual else enter 0
          required : true 
        - name : Transmission_Manual
          in : query
          type : string
          description : Enter 1 if manual else enter 0 if automatic
          required : true 
          
        
    responses :
          200 :
            description : The response of file api 
    """
    
    						
    present_price = request.args.get("Present_Price")
    kms_driven = request.args.get("Kms_Driven")
    owner = request.args.get("Owner")
    no_year = request.args.get("no_year")
    fuel_type_diesel = request.args.get("Fuel_Type_Diesel")
    fuel_type_petrol = request.args.get("Fuel_Type_Petrol")
    seller_type_individual = request.args.get("Seller_Type_Individual")
    transmission_manual = request.args.get("Transmission_Manual")
    result = (rf_random.predict([[present_price,kms_driven,owner,no_year,
                                  fuel_type_diesel,fuel_type_petrol,
                                  seller_type_individual,transmission_manual]]))
    if result in [0,"0"] :  return "Invalid Car Data",200
    return "Valid Car Data",200
    
    
    #return result



@app.route('/predict_through_file',methods=['POST'])
def predict_file():
    """Testing of prediction using test file
    -------------------
    parameters :
        - name : file
          in : formData
          type : file
          required : true 
        
    responses :
          200 :
            description : The response of file is 
    """
    
    df = pd.read_csv(request.files.get("file"))
    print("-"*30+" File details "+"-"*30)
    print(df.shape)
    print(df.head())
    print("-"*70)
    result = rf_random.predict(df)
    return f"The result are as follows {result}"
    




if __name__ == "__main__":
    app.run(debug = True)