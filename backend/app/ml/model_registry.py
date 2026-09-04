"""
Local Model Persistence, Versioning, and Prediction Service.
"""
import os
import joblib
import json
from datetime import datetime
from ..config.settings import Config
from ..models import db, MLModelRegistry, PredictionLog

class LocalModelRegistry:
    @staticmethod
    def save_model(model_name, display_name, target_var, algo_type, model_object, metrics, feature_names=None):
        Config.init_dirs()
        file_path = os.path.join(Config.TRAINED_MODELS_DIR, f"{model_name}.joblib")
        joblib.dump(model_object, file_path)

        reg = MLModelRegistry.query.filter_by(model_name=model_name).first()
        if not reg:
            reg = MLModelRegistry(model_name=model_name)

        reg.display_name = display_name
        reg.target_variable = target_var
        reg.algorithm_type = algo_type
        reg.file_path = file_path
        reg.status = "ACTIVE"
        reg.accuracy_score = metrics.get("accuracy") or metrics.get("r2_score")
        reg.r2_or_f1_score = metrics.get("f1_score") or metrics.get("r2_score")
        reg.mae = metrics.get("mae")
        reg.rmse = metrics.get("rmse")
        reg.feature_names_json = json.dumps(feature_names or [])
        reg.trained_at = datetime.utcnow()

        db.session.add(reg)
        db.session.commit()
        return reg

    @staticmethod
    def load_model(model_name):
        file_path = os.path.join(Config.TRAINED_MODELS_DIR, f"{model_name}.joblib")
        if not os.path.exists(file_path):
            return None
        return joblib.load(file_path)

    @staticmethod
    def log_prediction(model_name, input_payload, prediction_result, confidence=1.0, exec_time_ms=1.5):
        reg = MLModelRegistry.query.filter_by(model_name=model_name).first()
        if reg:
            log = PredictionLog(
                model_id=reg.id,
                input_payload_json=json.dumps(input_payload),
                prediction_result_json=json.dumps(prediction_result),
                confidence_score=confidence,
                execution_time_ms=exec_time_ms
            )
            db.session.add(log)
            db.session.commit()
