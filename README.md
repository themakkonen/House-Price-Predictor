# House Price Predictor

A machine learning project that predicts house prices based on historical data.  
The project includes:
- A Jupyter Notebook for data analysis, feature engineering, and model training.
- A Flask web application for serving the trained model with a simple web interface.

---

## Features
- Data preprocessing and exploratory analysis.
- Model training using regression algorithms.
- Web interface to input features and get price predictions.
- Pre-trained model included (`model.pkl`) for quick demo.

---

## Project Structure
House-price-predictor/
│
├── app/
│ ├── app.py # Flask server script
│ ├── model.pkl # Trained ML model
│ ├── train.csv # Training dataset
│ ├── test.csv # Test dataset
│ └── templates/
│ └── index.html # Web UI
│
├── House prices prediction.ipynb # Data analysis & training notebook (PDF in repo)
---

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/<your-username>/house-price-predictor.git
cd house-price-predictor/app
python app.py
