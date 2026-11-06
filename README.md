# Spam Email Classification

A Machine Learning project that classifies email messages as **Spam** or **Ham (Not Spam)** using Python and Scikit-learn.

## Project Overview

This project uses text processing and Machine Learning to identify whether an email message is spam or legitimate.

A Streamlit web application allows users to enter an email message and get a prediction.

## Dataset

- Total messages: 5,572
- Ham messages: 4,825
- Spam messages: 747

## Technologies & Libraries

- Python
- Pandas
- Scikit-learn
- CountVectorizer
- StandardScaler
- Logistic Regression
- K-Nearest Neighbors (KNN)
- Streamlit
- Joblib

## Machine Learning Workflow

1. Data loading and exploration
2. Data preprocessing
3. Feature extraction using CountVectorizer
4. Message length scaling using StandardScaler
5. Train-test splitting with stratification
6. Model training and evaluation
7. Saving the trained model and preprocessor

## Model Evaluation

Two models were evaluated:

| Metric | Logistic Regression | KNN |
|---|---:|---:|
| Accuracy | 98.74% | 93.81% |
| Spam Precision | 0.97 | 1.00 |
| Spam Recall | 0.94 | 0.54 |
| Spam F1-score | 0.95 | 0.70 |

Logistic Regression achieved better overall performance, especially in detecting spam messages.

## Project Structure

```text
Spam_Email_Classification/
├── app/
│   └── app.py
├── data/
├── models/
│   ├── spam_classifier.pkl
│   └── preprocessor.pkl
├── notebooks/
├── requirements.txt
├── .gitignore
└── README.md
```

## Run the Application

1. Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
```

2. Navigate to the project folder:

```bash
cd Spam_Email_Classification
```

3. Install the required libraries:

```bash
pip install -r requirements.txt
```

4. Run the Streamlit application:

```bash
python -m streamlit run app/app.py
```

## Author

**Kenzy Ahmed**