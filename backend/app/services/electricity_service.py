"""
Electricity Grid Load & Power Outage Prevention Service.
"""
from datetime import datetime
from ..models import db, Transformer, ElectricityRecord, PowerOutage

class ElectricityService:
    @staticmethod
    def calculate_transformer_thermal_stress(current_load_kw, capacity_kva, temperature_c, power_factor=0.95):
        """
        Calculates Thermal Stress Index (TSI) for high-voltage transformers.
        Triggers load shedding warning if TSI exceeds 85.0.
        """
        load_ratio = current_load_kw / max(1.0, capacity_kva * power_factor)
        
        # Temp penalty: +1 point per degree C above 50 C
        temp_penalty = max(0.0, temperature_c - 50.0) * 1.5
        
        tsi = round((load_ratio * 75.0) + temp_penalty, 1)
        tsi = min(100.0, max(0.0, tsi))

        is_critical = tsi >= 85.0
        return {
            "load_ratio_percent": round(load_ratio * 100, 1),
            "thermal_stress_index": tsi,
            "is_critical_overload": is_critical,
            "action_required": "IMMEDIATE_LOAD_SHEDDING" if is_critical else "NORMAL"
        }

    @staticmethod
    def trigger_power_outage(transformer_id, cause="Thermal Overload"):
        transformer = Transformer.query.get(transformer_id)
        if not transformer:
            return False

        transformer.status = "OUTAGE"
        outage_code = f"OUT-{datetime.utcnow().strftime('%M%S')}-{transformer_id:03d}"
        
        outage = PowerOutage(
            outage_code=outage_code,
            transformer_id=transformer_id,
            outage_cause=cause,
            affected_customers=250,
            status="ACTIVE"
        )
        db.session.add(outage)
        db.session.commit()
        return True
