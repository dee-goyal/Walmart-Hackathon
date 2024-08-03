# from flask import Flask, request, render_template
# import pandas as pd

# app = Flask(__name__)

# # Load the data
# data = pd.read_csv('stock_depletion_data.csv')

# def calculate_depletion_rate(store_id, product_id, data):
#     # Filter the data based on store ID and product ID
#     filtered_data = data[(data['Store ID'] == store_id) & (data['Product ID'] == product_id)]
    
#     # Sort the data by date
#     filtered_data = filtered_data.sort_values(by='Date')
    
#     # Calculate the depletion rate
#     depletion_rate = filtered_data['Sales Volume'].mean()
    
#     return depletion_rate

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         store_id = int(request.form['store_id'])
#         product_id = int(request.form['product_id'])
#         depletion_rate = calculate_depletion_rate(store_id, product_id, data)
#         return render_template('index.html', depletion_rate=depletion_rate)
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True)
