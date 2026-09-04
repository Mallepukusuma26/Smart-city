"""
Machine Learning Registry, Evaluation, and Prediction Logging Models.
"""
from datetime import datetime
from .user import db

class MLModelRegistry(db.Model):
    __tablename__ = "ml_model_registry"

    id = db.Column(db.Integer, primary_key=True)
    model_name = db.Column(db.String(100), unique=True, nullable=False, index=True)
    display_name = db.Column(db.String(150), nullable=False)
    target_variable = db.Column(db.String(100), nullable=False)
    algorithm_type = db.Column(db.String(100), default="RandomForest")
    version = db.Column(db.String(20), default="1.0.0")
    file_path = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(30), default="TRAINED")  # TRAINED, ACTIVE, RETRAINING, DEPRECATED
    accuracy_score = db.Column(db.Float, nullable=True)
    r2_or_f1_score = db.Column(db.Float, nullable=True)
    mae = db.Column(db.Float, nullable=True)
    rmse = db.Column(db.Float, nullable=True)
    feature_names_json = db.Column(db.Text, nullable=True)
    trained_at = db.Column(db.DateTime, default=datetime.utcnow)

    prediction_logs = db.relationship("PredictionLog", back_populates="model", cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "model_name": self.model_name,
            "display_name": self.display_name,
            "target_variable": self.target_variable,
            "algorithm_type": self.algorithm_type,
            "version": self.version,
            "file_path": self.file_path,
            "status": self.status,
            "accuracy_score": self.accuracy_score,
            "r2_or_f1_score": self.r2_or_f1_score,
            "mae": self.mae,
            "rmse": self.rmse,
            "trained_at": self.trained_at.isoformat() if self.trained_at else None,
        }


class PredictionLog(db.Model):
    __tablename__ = "prediction_logs"

    id = db.Column(db.Integer, primary_key=True)
    model_id = db.Column(db.Integer, db.ForeignKey("ml_model_registry.id", ondelete="CASCADE"), nullable=False, index=True)
    input_payload_json = db.Column(db.Text, nullable=False)
    prediction_result_json = db.Column(db.Text, nullable=False)
    confidence_score = db.Column(db.Float, nullable=True)
    execution_time_ms = db.Column(db.Float, default=1.0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)

    model = db.relationship("MLModelRegistry", back_populates="prediction_logs")

    def to_dict(self):
        return {
            "id": self.id,
            "model_id": self.model_id,
            "model_name": self.model.model_name if self.model else None,
            "input_payload": self.input_payload_json,
            "prediction_result": self.prediction_result_json,
            "confidence_score": self.confidence_score,
            "execution_time_ms": self.execution_time_ms,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }
