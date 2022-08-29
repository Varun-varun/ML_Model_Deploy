from flask import Flask,request,jsonify,render_template
import pickle
import numpy as np
import pandas as pd
from sklearn import preprocessing

app = Flask(__name__)

model = pickle.load(open('model.pkl','rb'))

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/predict",methods = ['POST'])
def predict():
    inputQuery1 = request.form['1']
    inputQuery2 = request.form['2']
    inputQuery3 = request.form['3']
    inputQuery4 = request.form['4']
    inputQuery5 = request.form['5']
    inputQuery6 = request.form['6']
    inputQuery7 = request.form['7']
    inputQuery8 = request.form['8']
    inputQuery9 = request.form['9']
    inputQuery10 = request.form['10']
    inputQuery11 = request.form['11']
    

    data = [[inputQuery1, inputQuery2, inputQuery3, inputQuery4, inputQuery5, inputQuery6, inputQuery7, 
             inputQuery8, inputQuery9, inputQuery10, inputQuery11]]

    new_df = pd.DataFrame(data, columns = ['State','intl plan','vmail plan','Day Calls','Day Charge','Eve Charge','Night Mins','Night Calls','Intl Calls','Intl Charge','CustServ Calls'])
    prediction = model.predict(new_df)
    if format(prediction) == 1:
        return render_template('index.html',prediction_text = 'the member is NotChurned')
    else:
        return render_template('index.html',prediction_text = 'the member is Churned') 
        



if __name__ == '__main__':
    app.run(debug = True)
