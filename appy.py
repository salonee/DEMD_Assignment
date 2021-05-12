#from flask import Flask, render_template, request
#import jsonify
#import requests
#import pickle
#import numpy as np

from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import flasgger
from flasgger import Swagger
import pickle
from pickle import load
import sklearn
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
Swagger(app)

loaded_model = load(open('random_forest_regression_model.pkl', 'rb'))
#classifier=pickle.load(loaded_model)



@app.route('/',methods=["Get"])
def predict():

    """Car Price Prediction
    Note: Only for houses with Latitude Ranging from: 24.93 - 24.97 , Longitude: 121.47 - 121.54
    ---
    parameters:
        - name: Year of Purchase
          in: query
          type: number
          description: "0 - 43"
          required: true
        - name: Present Price
          in: query
          type: number
          description: "24 - 4k"
          required: true
        - name: KMs Driven
          in: query
          type: number
          description: "0-10"
          required: true
        - name: Owner
          in: query
          type: string
          description: "24.93-25"
          required: true
        - name: Fuel Type
          in: query
          type: string
          description: "121.47 - 121.57"
          required: true
        - name: Seller Type
          in: query
          type: string
          description: "121.47 - 121.57"
          required: true
    responses:
          200:
              description: The output values
    """
    l=[]
    i1=request.args.get('Year of Purchase')
    l.append(i1)
    i2=request.args.get('Present Price')
    l.append(i2)
    i3=request.args.get('KMs Driven')
    l.append(i3)
    i4=request.args.get('Owner')
    l.append(i4)
    i5=request.args.get('Fuel Type')
    l.append(i5)
    i6=request.args.get('Seller Type')
    l.append(i6)
    #arr = np.array([l])
    #arr = poly.transform(arr)
    #scaled_arr = sc.transform(arr)
    #p = round(loaded_model.predict(scaled_arr)[0][0],2)
    return "Price of the car : "









if __name__=='__main__':
    app.run()