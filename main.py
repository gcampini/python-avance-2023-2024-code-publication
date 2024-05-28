import pandas as pd
from data_processing.processing import load_data, clean_data, extract_features
from data_analysis.analysis import compute_statistics, visualize_data
from sales_prediction.prediction import train_model, predict_sales

# Charger et nettoyer les données
data = load_data("sales_data.csv")
cleaned_data = clean_data(data)
features = extract_features(cleaned_data)
print(features)

# Analyser les données
stats = compute_statistics(features)
visualize_data(features)

# Entraîner le modèle et prédire les ventes
model = train_model(features)
new_data = pd.DataFrame({"date": pd.to_datetime(["2023-02-01", "2023-02-02"])})
predictions = predict_sales(model, new_data)
print(predictions)
