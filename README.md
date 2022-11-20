# TooSweet - *A webapp that catches early signs of diabetes*

## Inspiration
The growing population of diabetic patients inspired the project. Many of them could have been prevented if they knew what to look out for. Today, 96 million people aged 18 years or older have prediabetes (38.0% of the adult US population) (src: https://www.cdc.gov/diabetes/data/statistics-report/index.html)

## What it does
The app consists of a set of questions. After answering the questions, the app uses an AI model to predict prediabetes and show how accurate the AI model is with the set of test samples from the dataset. For an individual, it is easy to overlook the correlation between the symptoms mentioned in the survey and diabetes, which is where the app is helpful!

## How we built it
The AI model was chosen to be a decision tree as most of the data types were categorical and binary. Due to this nature, a decision tree would give reliable results. For the user interface, a popular python library called 'streamlit' was used which helped create our super-friendly user interface. 
