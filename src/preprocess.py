import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib

def load_data(path):
    df = pd.read_csv(path)
    return df

def preprocess(df):
    df.drop(columns=['Serial No.'],inplace= True)
    X = df.drop("Scholarship Probability", axis=1)
    y = df["Scholarship Probability"]
    
    scaler = StandardScaler()
    joblib.dump(scaler,'models/scaler.pkl')
    X_scaled = scaler.fit_transform(X)
    
    return X_scaled, y, scaler