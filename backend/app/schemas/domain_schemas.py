"""
Domain Entity Payload Schemas for Traffic, Waste, Water, Electricity, Parking, Transport, Pollution, Emergency.
"""
from dataclasses import dataclass
from typing import Optional

@dataclass
class TrafficRecordSchema:
    road_id: int
    vehicle_count: int
    average_speed_kmh: float
    peak_hour: bool = False
    weather_condition: str = "Clear"

    def validate(self):
        if self.vehicle_count < 0:
            raise Exception("Vehicle count cannot be negative.")
        if self.average_speed_kmh < 0 or self.average_speed_kmh > 250:
            raise Exception("Invalid average speed.")
        return True


@dataclass
class WasteRecordSchema:
    waste_bin_id: int
    fill_level_percent: float
    waste_weight_kg: float
    temperature_celsius: float = 25.0
    methane_level_ppm: float = 5.0

    def validate(self):
        if not (0.0 <= self.fill_level_percent <= 100.0):
            raise Exception("Fill level percentage must be between 0 and 100.")
        if self.waste_weight_kg < 0:
            raise Exception("Waste weight cannot be negative.")
        return True


@dataclass
class WaterRecordSchema:
    water_tank_id: int
    flow_rate_lps: float
    consumption_liters: float
    pressure_bar: float
    ph_level: float = 7.2
    chlorine_ppm: float = 0.5

    def validate(self):
        if self.flow_rate_lps < 0:
            raise Exception("Flow rate cannot be negative.")
        if not (0.0 <= self.ph_level <= 14.0):
            raise Exception("pH level must be between 0 and 14.")
        return True


@dataclass
class ElectricityRecordSchema:
    transformer_id: int
    consumption_kwh: float
    peak_demand_kw: float
    power_factor: float = 0.95
    frequency_hz: float = 50.0
    is_peak_hour: bool = False

    def validate(self):
        if self.consumption_kwh < 0:
            raise Exception("Consumption cannot be negative.")
        if not (0.0 <= self.power_factor <= 1.0):
            raise Exception("Power factor must be between 0.0 and 1.0.")
        return True


@dataclass
class ParkingRecordSchema:
    location_id: int
    occupied_count: int
    available_count: int
    turnover_rate: float = 1.0

    def validate(self):
        if self.occupied_count < 0 or self.available_count < 0:
            raise Exception("Space counts cannot be negative.")
        return True


@dataclass
class TransportRecordSchema:
    route_id: int
    passenger_count: int
    delay_minutes: int = 0
    weather_condition: str = "Clear"
    is_peak_hour: bool = False

    def validate(self):
        if self.passenger_count < 0:
            raise Exception("Passenger count cannot be negative.")
        return True


@dataclass
class PollutionRecordSchema:
    station_id: int
    pm2_5: float
    pm10: float
    co: float
    no2: float
    so2: float
    o3: float
    temperature_c: float = 25.0
    humidity_percent: float = 50.0

    def validate(self):
        if self.pm2_5 < 0 or self.pm10 < 0:
            raise Exception("Pollutant values cannot be negative.")
        return True


@dataclass
class EmergencyIncidentSchema:
    incident_type: str
    location: str
    zone: str
    description: str
    severity: str = "CRITICAL"
    reported_by_phone: Optional[str] = None

    def validate(self):
        if not self.location or not self.description:
            raise Exception("Location and description are required for emergencies.")
        return True
