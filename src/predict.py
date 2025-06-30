import joblib
# Functions for making predictions
def load_model(model_path = "models/best_model.pkl",scaler_path ="models/scaler.pkl"):
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    return model , scaler
def predict_singer(model , scaler , input_data):
    X_scaled = scaler.tranform(input_data)
    pred = model.predict(X_scaled)
    return pred[0]