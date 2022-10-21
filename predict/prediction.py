
import pickle
import numpy as np
import sklearn

with open('model/scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

with open('model/poly.pkl', 'rb') as file:
    poly = pickle.load(file)

with open('model/reg_model.pkl', 'rb') as file:
    model = pickle.load(file)


def predict(json_data):
    X = []

    for value in json_data.values():
        X.append(value)

    X = np.array(X).reshape(1, -1)

    X_scaled = scaler.transform(X)

    X_poly = poly.transform(X_scaled)

    y_pred = model.predict(X_poly)

    result = {'prediction': y_pred[0], 'status_code': 200}

    return result
