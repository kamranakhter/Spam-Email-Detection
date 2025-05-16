# 📧 Spam Email Detection using Machine Learning

**A simple and efficient web application to classify emails as Spam or Not Spam using traditional Machine Learning algorithms.  
Built with Python, Flask, and Scikit-learn — including both frontend and backend implementation.**

---

## 🛠️ Tech Stack

- **Language:** Python  
- **Libraries:** Scikit-learn, Pandas  
- **Model:** Multinomial Naive Bayes  
- **Text Vectorization:** CountVectorizer  
- **Frontend:** HTML, CSS  
- **Backend:** Flask  
- **Deployment:** Localhost

---

## 📂 Project Structure
```
Spam-Email-Detection/
│
├── app.py             # Flask backend application
├── templates/
│ └── index.html       # Frontend HTML UI
├── model.pkl          # Trained ML model
├── vectorizer.pkl     # CountVectorizer object
├── train_model.py     # Script to train the ML model
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation
```
---

## 🚀 How to Run

1. **Clone the Repository**
   ```bash
   git clone https://github.com/kamranakhter/Spam-Email-Detection.git
   cd Spam-Email-Detection

2. **Install Dependencies**
   ```
   pip install -r requirements.txt
   ```

4. Run the Flask App
   ```bash
   python app.py

5. Open in Browser
   ```bash
   http://localhost:5000/
   
---

## 🔍 Model Details

- Algorithm Used: Multinomial Naive Bayes
- Text Vectorization: CountVectorizer
- Accuracy: Approximately 98%
- Evaluation Metrics: Accuracy, Precision, Recall, F1-score
- Data Preprocessing: Lowercasing, removing special characters
   
---

## ✅ Sample Input and Output
Input:
> "Congratulations! You've won a $1000 gift card. Click here to claim."

Output:
> Spam
   
---

## 📌 Features

- Classifies emails as spam or not spam
- User-friendly web interface
- Lightweight and fast response
- Fully integrated ML model in backend
   
---

## 🙋‍♂️ Author

- Mohammad Kamran Akhter
- GitHub <https://github.com/kamranakhter>
- LinkedIn <https://www.linkedin.com/in/kamranakhter03/>

---

📜 License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
