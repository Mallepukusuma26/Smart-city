"""
Local Machine Learning Prediction Pipeline Tests.
"""
from app.ml.pipelines import MLInferenceEngine

def test_traffic_ml_prediction(app):
    with app.app_context():
        res = MLInferenceEngine.predict_traffic(400, 35.0, 1)
        assert "predicted_congestion_index" in res
        assert 0.0 <= res["predicted_congestion_index"] <= 10.0

def test_waste_ml_prediction(app):
    with app.app_context():
        res = MLInferenceEngine.predict_waste_overflow(90.0, 950.0)
        assert "overflow_risk_predicted" in res
        assert res["overflow_risk_predicted"] is True

def test_pollution_aqi_ml_prediction(app):
    with app.app_context():
        res = MLInferenceEngine.predict_aqi(45.0, 85.0)
        assert "predicted_aqi" in res
        assert res["predicted_aqi"] > 0
