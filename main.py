# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import streamlit as st
from sklearn import metrics
from sklearn import tree
import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.model_selection import train_test_split  # training and testing split


df = pd.read_csv(
    'diabetes_data.csv', delimiter=';')
df["gender"].replace(["Male", "Female"], [0, 1], inplace=True)

train, test = train_test_split(df, test_size=0.2)

train_X = train.drop(columns=["class"])
train_Y = train["class"]

test_X = test.drop(columns=["class"])
test_Y = test["class"]

# Create a DecisionTree Classifier
model = tree.DecisionTreeClassifier()

model.fit(train_X, train_Y)
test_pred = model.predict(test_X)

print("Accuracy:", metrics.accuracy_score(test_Y, test_pred))

st.set_page_config(page_title="Too Sweet?", page_icon="🧊",
                   initial_sidebar_state="expanded")

st.image('./too.png', width=250)
header = '<p style="font-family:Monospace; color:Cyan; font-size: 45px;"><b>Diabetes Predictor</b></p>'
st.markdown(header, unsafe_allow_html=True)
st.markdown("**According to the World Health Organization (WHO), diabetes is one of the chronic, life-threatening diseases that is increasing the quickest and has already afflicted 422 million people globally. Early diabetes identification is usually preferred for a clinically significant result due to the existence of a relatively extended asymptomatic phase. Due to the protracted asymptomatic stage of the diseas, approximately 50% of all diabetics go undetected.**")

title = '<p style="font-family:Monospace; color:Cyan; font-size: 20px;">Lets see if you are at risk for getting diagnosed with Diabetes.</p>'
st.markdown(title, unsafe_allow_html=True)
st.markdown("**Please answer the following questions!**")

st.write("#")
name = st.text_input('What is Your Name?')
age = st.slider('What is your Age?', 0, 100)
gender = st.radio('Gender at birth?', ['Female', 'Male'])
polyuria = st.radio(
    'Have you been experiencing excessive urination?', ['No', 'Yes'])
polydipsia = st.radio(
    'Have you been experiencing excessive thirst/urge to drink water?', ['No', 'Yes'])
weightchange = st.radio(
    'Have you had any recent episode of sudden weight loss?', ['No', 'Yes'])
weakness = st.radio(
    'Have you had any recent episodes of feeling weak?', ['No', 'Yes'])
genitalthrush = st.radio(
    'Have you had any recent episode of yeast infection?', ['No', 'Yes'])
visualblurring = st.radio(
    'Have you had any recent episode of blurred vision?', ['No', 'Yes'])
itching = st.radio(
    'Have you had any recent episode of prolonged itching?', ['No', 'Yes'])
irritability = st.radio(
    'Have you had any recent episodes of irritation?', ['No', 'Yes'])
delayed_healing = st.radio(
    'Have you had any recent episode of delayed healing?', ['No', 'Yes'])
partial_paresis = st.radio(
    'Have you had any recent episode of weak muscles?', ['No', 'Yes'])
muscle_stiffness = st.radio(
    'Have you had any recent episode of stiff muscles?', ['No', 'Yes'])
alopecia = st.radio(
    'Have you been suffering from hairloss?', ['No', 'Yes'])
obesity = st.radio(
    'Are you suffering from Obesity?', ['No', 'Yes'])
st.markdown('#')

if gender == 'Male':
    gender = 0
else:
    gender = 1

polyuria, polydipsia, weightchange, weakness, genitalthrush, visualblurring, itching, irritability, delayed_healing, partial_paresis, muscle_stiffness, alopecia, obesity = [1 if x == 'Yes' else 0 for x in [
    polyuria, polydipsia, weightchange, weakness, genitalthrush, visualblurring, itching, irritability, delayed_healing, partial_paresis, muscle_stiffness, alopecia, obesity]]

prediction = model.predict([polyuria, polydipsia, weightchange, weakness, genitalthrush, visualblurring,
                           itching, irritability, delayed_healing, partial_paresis, muscle_stiffness, alopecia, obesity])

if st.button('Proceed with the Diabetes Predictor!'):
    st.write('Hello', name, 'The result is')
    if prediction == 1:
        st.write(
            "You are at risk of getting diagnosed with Diabetes. Please consult a doctor.")
    else:
        st.write(
            "You are NOT at risk of getting diagnosed with Diabetes. Please consult a doctor.")
    st.write(
        f"The accuracy of the model is {metrics.accuracy_score(test_Y, test_pred)*100}%")
st.markdown('#')
st.markdown('#')
st.markdown('#')
st.markdown('#')
st.markdown('#')
st.markdown('#')
st.markdown('#')
st.markdown('#')

st.markdown(
    '//datasets used: https://www.kaggle.com/datasets/andrewmvd/early-diabetes-classification')
