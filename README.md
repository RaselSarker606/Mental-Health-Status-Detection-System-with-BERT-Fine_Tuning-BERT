# 🧠 Mental Health Status Detection Web App

A mental health classification app built with Streamlit and transformers. This interactive tool predicts the user's mental health condition using a fine-tuned transformer model and a simple, user-friendly web interface.

---

## 📖 Overview

This project allows users to input a text description of their mental state. The system:

- Cleans and processes the text  
- Predicts the mental health category using a transformer-based model  
- Displays the result in a clear and accessible interface  

It’s ideal for showcasing the practical use of NLP models in healthcare-related applications.

---

## 📂 Features

- 🧹 **Text Cleaning**: Removes stopwords, numbers, and punctuation  
- 🤗 **Transformers Integration**: Uses HuggingFace’s AutoModelForSequenceClassification  
- 📊 **Multi-Class Prediction**: Classifies into seven mental health categories  
- 🌐 **Streamlit UI**: Real-time interactive web interface  
- 💬 **Simple Input Field**: Type a message and get the result instantly  

---

## 🛠️ Methodology

### 🧼 Text Preprocessing
- Lowercases all characters  
- Removes punctuation, numbers, and stopwords using NLTK  
- Tokenizes and formats input for the transformer model  

### 🧠 Prediction Logic
- Loads a saved fine-tuned transformer model  
- Applies tokenization and feeds data into the model  
- Uses argmax to determine the predicted label  

### 💻 Web App
- Developed with Streamlit for easy deployment and interaction  
- Displays prediction after the user submits their input  

---

## 📊 Example Output

**Title:** Mental Health Status Detection  
**User Input:** "I feel very down and hopeless lately."  
**Predicted Status:** Depression

---

## 🚀 Installation & Usage

### 📦 Requirements
- Python 3.x  
- Streamlit  
- Transformers  
- PyTorch  
- NLTK  

### 🔧 Setup

```bash
pip install streamlit transformers torch nltk
```

### ▶️ Running the App

1. Place your trained model in the specified directory (update "token + model" path)  
2. Save the Python script as `app.py`  
3. Run the app:

```bash
streamlit run app.py
```

4. Interact with the UI in your browser

---

## 🧠 Mental Health Labels Used

- Anxiety  
- Bipolar  
- Depression  
- Normal  
- Personality Disorder  
- Stress  
- Suicidal  

---

## 📌 Future Improvements

- 🧠 Train with a larger dataset for improved accuracy  
- 🏥 Add severity-level predictions  
- 🌍 Multi-language support (e.g., Bengali, Hindi)  
- 📱 Deploy to cloud or mobile  
- 🔒 Add privacy & data protection disclaimers  

---
