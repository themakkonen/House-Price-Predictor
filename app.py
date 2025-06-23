from flask import Flask, render_template, request, session, redirect, url_for
import joblib
import numpy as np

app = Flask(__name__)
app.secret_key = 'house_price_secret'
model = joblib.load('model.pkl')

def generate_suggestions(base_sqft, bedrooms, bathrooms):
    offsets = [-300, 0, 300]
    suggestions = []
    for offset in offsets:
        sqft = max(500, base_sqft + offset)
        price = model.predict(np.array([[sqft, bedrooms, bathrooms]]))[0]
        suggestions.append({
            'sqft': sqft,
            'bedrooms': bedrooms,
            'bathrooms': bathrooms,
            'price': round(price, 2)
        })

    low_offsets = [-800, -600, -400]
    low_prices = []
    for offset in low_offsets:
        sqft = max(400, base_sqft + offset)
        price = model.predict(np.array([[sqft, bedrooms, bathrooms]]))[0]
        low_prices.append({
            'sqft': sqft,
            'bedrooms': bedrooms,
            'bathrooms': bathrooms,
            'price': round(price, 2)
        })

    return suggestions, low_prices

@app.route('/')
def home():
    return render_template(
        'index.html',
        prediction=session.get('last_prediction'),
        last_input=session.get('last_input'),
        history=session.get('history', []),
        suggestions=session.get('suggestions', []),
        low_prices=session.get('low_prices', [])
    )

@app.route('/predict', methods=['POST'])
def predict():
    sqft = int(float(request.form['GrLivArea']))
    bedrooms = int(request.form['BedroomAbvGr'])
    bathrooms = int(request.form['FullBath'])

    prediction = model.predict(np.array([[sqft, bedrooms, bathrooms]]))[0]
    prediction = round(prediction, 2)

    record = {
        'sqft': sqft,
        'bedrooms': bedrooms,
        'bathrooms': bathrooms,
        'price': prediction
    }

    history = session.get('history', [])
    history.insert(0, record)
    session['history'] = history[:5]

    suggestions, low_prices = generate_suggestions(sqft, bedrooms, bathrooms)
    session['last_input'] = record
    session['last_prediction'] = prediction
    session['suggestions'] = suggestions
    session['low_prices'] = low_prices

    return redirect(url_for('home'))

@app.route('/clear')
def clear_history():
    session.clear()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
