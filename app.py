from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load model and vectorizer
try:
    model = joblib.load('model.pkl')
    vectorizer = joblib.load('vectorizer.pkl')
except Exception as e:
    print(f"Error loading model files: {str(e)}")
    exit(1)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Get email text from form
            email_text = request.form['email']
            
            if not email_text.strip():
                return jsonify({
                    'status': 'error',
                    'message': 'Please enter email text'
                })
            
            # Vectorize the email
            email_vectorized = vectorizer.transform([email_text])
            
            # Make prediction
            prediction = model.predict(email_vectorized)[0]
            confidence = np.max(model.predict_proba(email_vectorized))
            
            return jsonify({
                'status': 'success',
                'prediction': 'Spam' if int(prediction) == 1 else 'Not Spam',
                'confidence': float(confidence)
            })
            
        except Exception as e:
            return jsonify({
                'status': 'error',
                'message': str(e)
            })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)