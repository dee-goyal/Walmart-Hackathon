from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load('depletion_rate_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    input_data = np.array([[
        data['stock_level'],
        data['stock_out_occurrence'],
        data['stock_out_duration'],
        data['promotion'],
        data['seasonality'],
        data['external_events'],
        data['product_price'],
        data['order_quantity']
    ]])
    
    prediction = model.predict(input_data)
    return jsonify({'Depletion Rate': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
