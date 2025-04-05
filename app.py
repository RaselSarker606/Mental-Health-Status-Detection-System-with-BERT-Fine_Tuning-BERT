import streamlit as st
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import pickle
import re
import nltk
from nltk.corpus import stopwords
#pip install numpy

nltk.download('stopwords')

# load save model
model = AutoModelForSequenceClassification.from_pretrained('token + model')
tokenizer = AutoTokenizer.from_pretrained('token + model')
labels = ['anxiety', 'Bipolar', 'Depression', 'Normal', 'Personality disorder', 'Stress', 'Suicidal']  # Example, you can customize this list


# Get English stopwords from NLTK
stop_words = set(stopwords.words('english'))

def clean_statement(statement):
    # Convert to lowercase
    statement = statement.lower()

    # Remove special characters (punctuation, non-alphabetic characters)
    statement = re.sub(r'[^\w\s]', '', statement)

    # Remove numbers (optional, depending on your use case)
    statement = re.sub(r'\d+', '', statement)

    # Split the statement into individual words
    words = statement.split()

    # Remove stopwords
    words = [word for word in words if word not in stop_words]

    # Rejoin words into a cleaned statement
    cleaned_statement = ' '.join(words)

    return cleaned_statement

#=========================================================================
# Function to predict mental health status
def detect_anxiety(text):
    cleaned_text = clean_statement(text)
    inputs = tokenizer(cleaned_text, return_tensors="pt", padding=True, truncation=True, max_length=200)
    outputs = model(**inputs)
    logits = outputs.logits
    predicted_class = torch.argmax(logits, dim=1).item()
    print(predicted_class)
    # Map the predicted class index to the corresponding label manually
    predicted_label = labels[predicted_class]

    return predicted_label

#==========================================================================

# UI app
st.title("Mental Health Status Detection")

input_text = st.text_input("Enter Your mental state here....")

if st.button("Predict Mental Health Status"):
    predicted_class = detect_anxiety(input_text)
    st.write("Predicted Status :", predicted_class)





