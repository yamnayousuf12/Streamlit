# import the streamlit library
import streamlit as st
from PIL import Image
# give a title to our app
st.title('Welcome to BMI Calculator')

img = Image.open("bmi.png")
st.image(img) 

# Introduction

st. subheader("Introduction")
st.text("""
BMIis a person's wight in kilograms divided by the square of the square of height in meters.
A high BMI can indicate high body fatness.

If your BMI is less than 18.5, it falls within the underweight range.
If your BMI is 18.5 to <25,it falls within the healthy weight range.
If your BMIis 25.0 to <30, it falls within overweight range.
If your BMI is30.0 or higher, it falls within the obesity range.
Obesity is frequently subdivided into categories:

Class 1: BMI of 30 to < 35
Class 2: BMI of 35 to < 40
Class 3: BMI of 40 or higher.
Class 3 obesity is sometimes categorized as "severe" obesity.
        
Credits: https:// www.cdc.gov./obesity/adult/defining.html

        
""")

# TAKE WEIGHT INPUT in kgs
weight = st.number_input("Enter your weight (in kgs)")
 
# TAKE HEIGHT INPUT
# radio button to choose height format
status = st.radio('Select your height format: ',
                  ('cms', 'meters', 'feet'))
 
# compare status value
if(status == 'cms'):
    # take height input in centimeters
    height = st.number_input('Centimeters')
 
    try:
        bmi = weight / ((height/100)**2)
    except:
        st.text("Enter some value of height")
 
elif(status == 'meters'):
    # take height input in meters
    height = st.number_input('Meters')
 
    try:
        bmi = weight / (height ** 2)
    except:
        st.text("Enter some value of height")
 
else:
    # take height input in feet
    height = st.number_input('Feet')
 
    # 1 meter = 3.28
    try:
        bmi = weight / (((height/3.28))**2)
    except:
        st.text("Enter some value of height")
 
# check if the button is pressed or not
if(st.button('Calculate BMI')):
 
    # print the BMI INDEX
    st.text("Your BMI Index is {}.".format(bmi))
 
    # give the interpretation of BMI index
    if(bmi < 16):
        st.error("You are Extremely Underweight")
    elif(bmi >= 16 and bmi < 18.5):
        st.warning("You are Underweight")
    elif(bmi >= 18.5 and bmi < 25):
        st.success("Healthy")
    elif(bmi >= 25 and bmi < 30):
        st.warning("Overweight")
    elif(bmi >= 30):
        st.error("Extremely Overweight")