from django.shortcuts import render
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Create your views here.
def home(request):
    return render(request,'index.html')




def predict(request):
    data= pd.read_csv('bidadata.csv')
    data.drop(["Loan_ID","Dependents"], axis=1, inplace=True)
    data = data.dropna()
    data.replace({'Married':{'No':0,'Yes':1},'Gender':{'Male':1,'Female':0},'Self_Employed':{'No':0,'Yes':1},
                      'Property_Area':{'Rural':0,'Semiurban':1,'Urban':2},'Education':{'Graduate':1,'Not Graduate':0}},inplace=True)
    data.replace({"Loan_Status":{'N':0,'Y':1}},inplace=True) 

    X = data.drop('Loan_Status',axis=1)
    Y = data['Loan_Status']     
    X_train, X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3,random_state=2) 
    model = LogisticRegression()
    model.fit(X_train,Y_train)          

    Gender = int(request.GET['Gender'])
    Married = int(request.GET['Married'])
    Education = int(request.GET['Education'])
    Self_Employed = int(request.GET['Self_Employed'])  
    ApplicantIncome = int(request.GET['ApplicantIncome'])  
    CoapplicantIncome = int(request.GET['CoapplicantIncome']) 
    LoanAmount = int(request.GET['LoanAmount'])   
    Loan_Amount_Term = int(request.GET['Loan_Amount_Term'])   
    Credit_History = int(request.GET['Credit_History'])   
    Property_Area = int(request.GET['Property_Area'])

    array=np.array([[Gender,Married,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area]])
    
    prediction = model.predict(array)
    
    return render(request,'predict.html',{'prediction':prediction})

def pred_for(request):
    return render(request,'App/predictor_form.html')

def about(request):
    return render(request,'App/about.html')





