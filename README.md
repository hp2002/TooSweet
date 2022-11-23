
<p align="center">
  <img src="https://user-images.githubusercontent.com/69314416/203291311-de29453f-8266-482a-8fad-73eaafc4ba35.png">
</p>
<p align="center">
   # TooSweet - *A webapp that catches early signs of diabetes*
 </p>



## Inspiration
The growing population of diabetic patients inspired the project. Many of them could have been prevented if they knew what to look out for. Today, 96 million people aged 18 years or older have prediabetes (38.0% of the adult US population) ([source]( https://www.cdc.gov/diabetes/data/statistics-report/index.html))

## What it does
The app uses an AI model to predict prediabetes and show how accurate the AI model is with the set of test samples from the dataset. It does so by asking a series of questions to the user and making predictions accordingly. For an individual, it is easy to overlook the correlation between the symptoms mentioned in the survey and diabetes, which is where the app is helpful!

## How we built it
The AI model was chosen to be a decision tree as most of the data types were categorical and binary. Due to this nature, a decision tree would give reliable results. For the user interface, a popular python library called 'streamlit' was used which helped create our super-friendly user interface. 

## Challenges we ran into
For us, the main challenge was integrating the UI with the AI model. This process would have been a lot easier if some of the python modules ran well on both of our systems. We faced issues where python in one of our systems could not import the module we used.

## Accomplishments that we're proud of
We are proud of the accuracy of the model. Usually, a model is considered to be accurate if the accuracy exceeds 85%, but our model is well beyond the baseline of > 0.85 accuracies.

## What we learned
The python library streamlit was a new endeavor for both of us. We quickly learned how to make friendly and useable UIs for web apps using this library. The AI portion of the project was hard to implement too. We knew the theory behind a good machine learning model but, it's a whole other task to be able to implement it.

## What's next for TooSweet
Next, we can collaborate with multiple hospitals across the country and use their datasets anonymously to train the AI model. This would further increase the accuracy of the model and help us find other factors that may contribute to pre-diabetes. We could use the Google Health API to upload the project and make it compute on the cloud which, would make it significantly safer to use. There are many other medical conditions that show early symptoms. With enough data, we could streamline and look out for some of the other medical conditions simultaneously, leading to early prevention of these conditions, and helping us have healthier lifestyles for all of us!

