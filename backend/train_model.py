
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import joblib
import os

# Load Dataset
df = pd.read_csv('data/creditcard.csv')
print(df.isnull().sum())  # No missing values expected

# Features and Target
X = df.drop('Class', axis=1)
y = df['Class']

# Scale 'Time' and 'Amount'
scaler = StandardScaler()
X[['Time', 'Amount']] = scaler.fit_transform(X[['Time', 'Amount']])

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Train Isolation Forest
iso = IsolationForest(contamination=y.mean(), random_state=42)
iso.fit(X_train)

# Save model and scaler
os.makedirs('model', exist_ok=True)
joblib.dump(iso, 'model/iso_model.pkl')
joblib.dump(scaler, 'model/scaler.pkl')
print("✅ Model and scaler saved")
