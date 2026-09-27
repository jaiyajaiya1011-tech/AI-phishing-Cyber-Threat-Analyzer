🛡️ AI-Based Phishing Detection & Cyber Threat Analysis System

📌 Overview

The AI-Based Phishing Detection & Cyber Threat Analysis System is a machine learning-based cybersecurity application designed to identify potentially phishing URLs and analyze suspicious web addresses.

The system extracts URL-based characteristics, applies a trained machine learning model, and provides a phishing prediction along with threat analysis.

🎯 Objectives

- Detect potentially phishing URLs using Machine Learning
- Classify URLs as legitimate or phishing
- Analyze suspicious URL characteristics
- Provide a threat/risk indication
- Help users identify potentially unsafe links without visiting them

✨ Features

- 🔗 URL-based phishing detection
- 🤖 Machine Learning classification
- ⚠️ Threat analysis
- 📊 Model performance evaluation
- 🔍 Suspicious URL indicator analysis
- 🖥️ Interactive Streamlit interface
- 📈 Accuracy, Precision, Recall and F1-score evaluation

🛠️ Technologies Used

- Python
- Pandas
- Scikit-learn
- Random Forest
- Joblib
- Streamlit
- Machine Learning

🧠 Machine Learning

The project uses a Random Forest Classifier for phishing URL classification.

The model is evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

📂 Project Structure

AI-Phishing-Cyber-Threat-Analyzer/
│
├── data/
│   └── phishing.csv
│
├── train_model.py
├── app.py
├── phishing_model.pkl
├── requirements.txt
└── README.md

⚙️ Installation

Clone the repository or download the project.

Install the required libraries:

pip install -r requirements.txt

▶️ Run the Application

First train the machine learning model:

python train_model.py

Then start the Streamlit application:

streamlit run app.py

The application will open in your browser.

🔍 How It Works

User enters URL
       ↓
URL feature extraction
       ↓
Machine Learning model
       ↓
Phishing / Legitimate prediction
       ↓
Threat analysis
       ↓
Result displayed to user

⚠️ Safety Notice

This application is intended for educational and defensive cybersecurity purposes.

The system provides a machine learning-based prediction and should not be treated as a guarantee that a URL is safe or malicious.

Users should avoid opening suspicious links directly.

🚀 Future Enhancements

- Email phishing detection using NLP
- Real-time threat intelligence integration
- Domain reputation analysis
- Detection history
- Advanced cybersecurity dashboard
- Explainable AI visualizations
- Additional machine learning models
- Database integration

👩‍💻 Author

Jaiya Dharshini RS

B.Tech Information Technology Student

📌 Project Category

Artificial Intelligence | Machine Learning | Cybersecurity
