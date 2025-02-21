import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pickle
data=pd.read_csv(r"C:/Users/Anamika/Downloads/heart.csv")
df = pd.DataFrame(data)
X = df[['Age','Gender','Heartrate','SystolicBP','DiastolicBP','Bloodsugar','CKMB','Troponin']]
y = df['Result']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
model = LogisticRegression()
model.fit(X_train_scaled, y_train)
with open('pickle.pkl', 'wb') as file:
    pickle.dump(model, file)
