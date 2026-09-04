"""
City Infrastructure Asset Depreciation & Valuation Service.
"""
from ..models import db, CityAsset, MaintenanceRecord

class AssetService:
    @staticmethod
    def calculate_straight_line_depreciation(asset_id, current_age_years):
        asset = CityAsset.query.get(asset_id)
        if not asset:
            return None

        initial_cost = asset.valuation_usd or 5000.0
        salvage_value = initial_cost * 0.10 # 10% salvage
        lifespan = asset.estimated_lifespan_years or 10

        annual_depreciation = (initial_cost - salvage_value) / float(lifespan)
        current_valuation = max(salvage_value, initial_cost - (annual_depreciation * current_age_years))

        return {
            "asset_code": asset.asset_code,
            "initial_cost_usd": initial_cost,
            "annual_depreciation_usd": round(annual_depreciation, 2),
            "current_valuation_usd": round(current_valuation, 2),
            "remaining_lifespan_years": max(0, lifespan - current_age_years)
        }
