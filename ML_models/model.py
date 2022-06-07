import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load the csv file
data = pd.read_csv('churn.csv')
data.drop(["Area Code","Day Mins","Night Charge","Intl Mins","Eve Mins","VMail Message","Eve Calls","Account Length","Phone"],inplace=True,axis=1)

# encoding categorical features
label = preprocessing.LabelEncoder()
lst = ['VMail Plan',"Int'l Plan",'Churn?','State']
for i in lst:
  data[i]=label.fit_transform(data[i])

# selecting independent and dependent features
print(data)
x = data.iloc[:,:11]
y = data['Churn?']

# splitting the dataset into train and test
train_x,test_x,train_y,test_y = train_test_split(x,y,test_size = 0.2,random_state = 3)

# Intializing the model and fitting 
model = RandomForestClassifier()
model.fit(train_x,train_y)

# Creation of pickle file of our model
pickle.dump(model,open("model.pkl","wb"))
