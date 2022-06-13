# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 15:47:00 2022

@author: Ninad
"""
import numpy as np
import pickle 
import streamlit as st

model=pickle.load(open('C:/Users/Ninad/OneDrive/Desktop/Web deployment/Diab.sav','rb'))

def predict(input_data):
    input_data=np.array(input_data)
    input_data=input_data.reshape(-1,1).T
    res=model.predict(input_data)
    if res[0]==0:
        return "No diabetes detected"
    else:
        return "Diabetes Detected"

def main():
    st.title('Diabetes Test')
    
    #giving the inputs
    Pregnancy=st.text_input('Pregnancy')
    Glucose=st.text_input('Glucose level')
    BloodPressure=st.text_input('Blood Pressure')
    SkinThickness=st.text_input('SkinThickness')
    Insulin=st.text_input('Insulin')
    BMI=st.text_input('BMI')
    DiabPedFunc=st.text_input('DiabPedFunc')
    Age=st.text_input('Age')
    
    
    #deploying
    if st.button('Test for Diabetes'):
        
        diagnosis=predict([Pregnancy,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabPedFunc,Age])
        
        st.success(diagnosis)
 
if __name__=='__main__':
    main()
    
        
  

