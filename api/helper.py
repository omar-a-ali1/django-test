import os
import joblib

_base = os.path.dirname(os.path.abspath(__file__))

scaler = joblib.load(os.path.join(_base, 'output', 'scaler_ecg_.pkl'))
knn_model = joblib.load(os.path.join(_base, 'output', 'knn_model.pkl'))
dt_model = joblib.load(os.path.join(_base, 'output', 'model_dt_model.pkl'))
rf_model = joblib.load(os.path.join(_base, 'output', 'model_rf_validator.pkl'))
svm_model = joblib.load(os.path.join(_base, 'output', 'model_svm_triage.pkl'))
xgboost_model = joblib.load(os.path.join(_base, 'output', 'model_xg_boost.pkl'))
