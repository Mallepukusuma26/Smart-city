"""
Air Quality Index (AQI) Calculation & EPA Health Advisory Service.
"""
from ..models import PollutionRecord, PollutionStation
from ..config.constants import AQIRatings

class PollutionService:
    @staticmethod
    def calculate_epa_aqi(pm2_5, pm10):
        """
        US EPA Standard AQI Sub-index Interpolation Algorithm.
        """
        # PM2.5 Breakpoints: (C_low, C_high, I_low, I_high)
        breakpoints = [
            (0.0, 12.0, 0, 50),
            (12.1, 35.4, 51, 100),
            (35.5, 55.4, 101, 150),
            (55.5, 150.4, 151, 200),
            (150.5, 250.4, 201, 300),
            (250.5, 500.4, 301, 500),
        ]
        
        aqi_val = 50.0
        for c_low, c_high, i_low, i_high in breakpoints:
            if c_low <= pm2_5 <= c_high:
                aqi_val = ((i_high - i_low) / (c_high - c_low)) * (pm2_5 - c_low) + i_low
                break
        
        aqi_val = round(aqi_val, 1)
        min_v, max_v, category, color = AQIRatings.get_rating(aqi_val)

        return {
            "calculated_aqi": aqi_val,
            "category": category,
            "color_hex": color,
            "health_advisory": "Air quality is satisfactory." if aqi_val <= 50 else ("Sensitive groups should reduce outdoor exercise." if aqi_val <= 100 else "Wear N95 masks outdoors.")
        }
