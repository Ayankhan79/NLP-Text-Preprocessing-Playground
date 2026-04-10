import streamlit as st
import pandas as pd
import re
import nltk
import os

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize, sent_tokenize



# Download required NLTK data (run once)
nltk_data_path = os.path.join(os.getcwd(), "nltk_data")

if not os.path.exists(nltk_data_path):
    os.makedirs(nltk_data_path)

nltk.data.path.append(nltk_data_path)

nltk.download('punkt', download_dir=nltk_data_path)
nltk.download('punkt_tab', download_dir=nltk_data_path)  
nltk.download('stopwords', download_dir=nltk_data_path)
nltk.download('wordnet', download_dir=nltk_data_path)

# Initialize tools
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

# -------------------------------
# Preprocessing Functions
# -------------------------------

def to_lower(text):
    return text.lower()

def remove_punctuation(text):
    return re.sub(r'[^\w\s]', '', text)

def remove_stopwords(text):
    tokens = word_tokenize(text)
    return " ".join([word for word in tokens if word not in stop_words])

def apply_stemming(text):
    tokens = word_tokenize(text)
    return " ".join([stemmer.stem(word) for word in tokens])

def apply_lemmatization(text):
    tokens = word_tokenize(text)
    return " ".join([lemmatizer.lemmatize(word) for word in tokens])

def tokenize_words(text):
    return word_tokenize(text)

def tokenize_sentences(text):
    return sent_tokenize(text)

# -------------------------------
# Streamlit UI
# -------------------------------

st.title("🧠 NLP Text Preprocessing Playground")

st.write("Upload your dataset and apply preprocessing techniques interactively.")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("### Dataset Preview")
    st.dataframe(df.head(20))

    # Select text column
    text_column = st.selectbox("Select Text Column", df.columns)

    st.write("### Select Preprocessing Techniques")

    col1, col2 = st.columns(2)

    with col1:
        lowercase = st.checkbox("Lowercasing")
        punctuation = st.checkbox("Remove Punctuation")
        stopword = st.checkbox("Remove Stopwords")

    with col2:
        stemming = st.checkbox("Stemming")
        lemmatization = st.checkbox("Lemmatization")
        tokenization = st.checkbox("Tokenization (Words)")

    sentence_tokenization = st.checkbox("Sentence Tokenization")

    if st.button("🚀 Apply Preprocessing"):

        processed_df = df.copy()

        def process(text):
            if pd.isna(text):
                return ""

            text = str(text)

            if lowercase:
                text = to_lower(text)

            if punctuation:
                text = remove_punctuation(text)

            if stopword:
                text = remove_stopwords(text)

            if stemming:
                text = apply_stemming(text)

            if lemmatization:
                text = apply_lemmatization(text)

            if tokenization:
                return tokenize_words(text)

            if sentence_tokenization:
                return tokenize_sentences(text)
                

            return text

        processed_df["processed_text"] = processed_df[text_column].apply(process)

        st.write("### ✅ Processed Output")
        st.dataframe(processed_df.head(20))

 
        

        # Download option
        csv = processed_df.to_csv(index=False).encode('utf-8')

        st.download_button(
            label="📥 Download Processed Data",
            data=csv,
            file_name="processed_data.csv",
            mime="text/csv"
        )

