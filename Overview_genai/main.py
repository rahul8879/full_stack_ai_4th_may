import pickle
import pandas as pd
with open('knn_model.pkl', 'rb') as f:
    model = pickle.load(f)
    
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

input_v= pd.DataFrame(scaler.transform([[5000, 30]]), columns=['CIBIL Score', 'Monthly Income (₹)'])
y_pred = model.predict(input_v)

    