"""
Municipal Water Supply, Purity & Leakage Triangulation Service.
"""
from datetime import datetime
from ..models import db, WaterTank, WaterPipeline, WaterRecord, WaterLeakage

class WaterService:
    @staticmethod
    def calculate_water_purity_index(ph_level, turbidity_ntu, chlorine_ppm):
        """
        Calculates Water Quality Index (WQI) based on pH, turbidity, and chlorine.
        Standard pH range: 6.5 - 8.5
        Ideal Turbidity: < 1.0 NTU
        Standard Chlorine: 0.2 - 1.0 PPM
        """
        ph_score = 100 - abs(7.2 - ph_level) * 30
        turbidity_score = max(0, 100 - (turbidity_ntu * 20))
        chlorine_score = 100 if (0.2 <= chlorine_ppm <= 1.0) else 50

        wqi = round((ph_score * 0.4) + (turbidity_score * 0.4) + (chlorine_score * 0.2), 1)
        wqi = min(100.0, max(0.0, wqi))

        if wqi >= 90.0:
            status = "EXCELLENT"
        elif wqi >= 75.0:
            status = "GOOD"
        elif wqi >= 60.0:
            status = "FAIR"
        else:
            status = "POOR"

        return {"wqi_score": wqi, "quality_rating": status}

    @staticmethod
    def detect_pipeline_leakage(pipeline_id, actual_pressure_bar, flow_rate_lps):
        pipeline = WaterPipeline.query.get(pipeline_id)
        if not pipeline:
            return None

        expected_pressure = pipeline.normal_pressure_bar or 4.5
        pressure_drop_pct = ((expected_pressure - actual_pressure_bar) / expected_pressure) * 100.0

        is_leak = pressure_drop_pct >= 20.0
        if is_leak:
            pipeline.status = "LEAKAGE_DETECTED"
            leak_code = f"LEAK-{pipeline.zone[:3].upper()}-{datetime.utcnow().strftime('%M%S')}"
            
            leakage = WaterLeakage(
                leakage_code=leak_code,
                pipeline_id=pipeline.id,
                severity="HIGH" if pressure_drop_pct >= 40.0 else "MEDIUM",
                estimated_loss_lps=round(flow_rate_lps * 0.25, 1),
                status="REPORTED"
            )
            db.session.add(leakage)
            db.session.commit()

        return {
            "pipeline_code": pipeline.pipeline_code,
            "pressure_drop_percentage": round(pressure_drop_pct, 1),
            "leakage_detected": is_leak
        }
