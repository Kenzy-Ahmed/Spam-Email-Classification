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

### Model Evaluation

#### 1. Initial Model Evaluation

The initial evaluation compared two machine learning models: Logistic Regression and K-Nearest Neighbors (KNN).

| Metric | Logistic Regression | KNN |
|:---|:---:|:---:|
| Accuracy | 98.74% | 93.81% |
| Spam Precision | 0.97 | 1.00 |
| Spam Recall | 0.94 | 0.54 |
| Spam F1-score | 0.95 | 0.70 |

Logistic Regression achieved better overall performance, especially in detecting spam messages, and was initially selected as the best-performing model.

#### 2. Further Model Experiments

To explore better performance, four additional configurations were evaluated using two text vectorization techniques (CountVectorizer and TF-IDF) with two classification algorithms (Logistic Regression and Multinomial Naive Bayes).

| Metric | LR + Count | LR + TF-IDF | NB + Count | NB + TF-IDF |
|:---|:---:|:---:|:---:|:---:|
| Accuracy | 98.65% | 97.67% | **99.19%** | 96.32% |
| Spam Precision | 1.00 | 1.00 | **1.00** | 1.00 |
| Spam Recall | 0.90 | 0.83 | **0.94** | 0.72 |
| Spam F1-score | 0.95 | 0.90 | **0.97** | 0.84 |

#### 3. Final Model Selection

Among the four additional configurations, **Multinomial Naive Bayes with CountVectorizer** achieved the best overall performance:

- **Accuracy:** 99.19%
- **Spam Precision:** 100%
- **Spam Recall:** 93.96%
- **Spam F1-score:** 96.89%

Therefore, Multinomial Naive Bayes with CountVectorizer was selected as the final model and integrated into the Streamlit application.

## Application Screenshots

### HAM Prediction
![HAM Prediction](Images/Ham%20prediction.png)

### SPAM Prediction
![SPAM Prediction](Images/Spam%20prediction.png)

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
git clone https://github.com/Kenzy-Ahmed/Spam-Email-Classification
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
