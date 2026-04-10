

# 🧠 NLP Text Preprocessing Playground

An interactive **Streamlit web application** that allows users to upload text datasets and apply common **Natural Language Processing (NLP) preprocessing techniques** in real time.

---

## 🚀 Features

* 📂 Upload CSV datasets
* 🔍 Select any text column dynamically
* ⚙️ Apply multiple preprocessing techniques:

  * Lowercasing
  * Punctuation Removal
  * Stopword Removal
  * Stemming
  * Lemmatization
  * Word Tokenization
  * Sentence Tokenization
* 📊 Preview processed data instantly
* 📥 Download cleaned dataset

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit** (UI framework)
* **Pandas** (data handling)
* **NLTK** (NLP preprocessing)
* **Regex (re)** (text cleaning)

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Ayankhan79/NLP-Text-Preprocessing-Playground.git
cd NLP-Text-Preprocessing-Playground
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
├── app.py                # Main Streamlit application
├── nltk_data/           # Downloaded NLTK resources
├── requirements.txt     # Dependencies
└── README.md            # Project documentation
```

---

## ⚙️ How It Works

1. Upload a CSV file
2. Select the column containing text data
3. Choose preprocessing techniques
4. Click **"Apply Preprocessing"**
5. View and download the processed dataset

---

## 🧪 Preprocessing Pipeline

The app applies transformations sequentially:

```
Raw Text
   ↓
Lowercasing
   ↓
Remove Punctuation
   ↓
Remove Stopwords
   ↓
Stemming / Lemmatization
   ↓
Tokenization (Optional)
```

---

## 📊 Example Use Cases

* Text classification preprocessing
* Sentiment analysis preparation
* NLP model input cleaning
* Educational NLP demonstrations

---

## ⚠️ Notes

* NLTK resources are downloaded locally on first run
* Tokenization overrides final output (returns list instead of string)
* Large datasets may take longer to process

---


## 🤝 Contributing

Contributions are welcome!
Feel free to fork the repo and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---


