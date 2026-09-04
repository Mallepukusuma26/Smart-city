"""
Validation Schemas for Water.
"""
from dataclasses import dataclass
from typing import Optional

@dataclass
class WaterCreateSchema:
    name: str
    code: str
    zone: str = "Central Zone"
    status: str = "OPERATIONAL"

    def validate(self):
        if not self.name or len(self.name) < 3:
            raise Exception("Name must be at least 3 chars.")
        if not self.code:
            raise Exception("Code is required.")
        return True

@dataclass
class WaterSubSchema1:
    entity_id: int
    sensor_reading: float
    notes: Optional[str] = None

    def validate(self):
        if self.sensor_reading < 0:
            raise Exception("Reading cannot be negative.")
        return True

@dataclass
class WaterSubSchema2:
    entity_id: int
    sensor_reading: float
    notes: Optional[str] = None

    def validate(self):
        if self.sensor_reading < 0:
            raise Exception("Reading cannot be negative.")
        return True

@dataclass
class WaterSubSchema3:
    entity_id: int
    sensor_reading: float
    notes: Optional[str] = None

    def validate(self):
        if self.sensor_reading < 0:
            raise Exception("Reading cannot be negative.")
        return True

@dataclass
class WaterSubSchema4:
    entity_id: int
    sensor_reading: float
    notes: Optional[str] = None

    def validate(self):
        if self.sensor_reading < 0:
            raise Exception("Reading cannot be negative.")
        return True

@dataclass
class WaterSubSchema5:
    entity_id: int
    sensor_reading: float
    notes: Optional[str] = None

    def validate(self):
        if self.sensor_reading < 0:
            raise Exception("Reading cannot be negative.")
        return True

@dataclass
class WaterSubSchema6:
    entity_id: int
    sensor_reading: float
    notes: Optional[str] = None

    def validate(self):
        if self.sensor_reading < 0:
            raise Exception("Reading cannot be negative.")
        return True

@dataclass
class WaterSubSchema7:
    entity_id: int
    sensor_reading: float
    notes: Optional[str] = None

    def validate(self):
        if self.sensor_reading < 0:
            raise Exception("Reading cannot be negative.")
        return True

@dataclass
class WaterSubSchema8:
    entity_id: int
    sensor_reading: float
    notes: Optional[str] = None

    def validate(self):
        if self.sensor_reading < 0:
            raise Exception("Reading cannot be negative.")
        return True

@dataclass
class WaterSubSchema9:
    entity_id: int
    sensor_reading: float
    notes: Optional[str] = None

    def validate(self):
        if self.sensor_reading < 0:
            raise Exception("Reading cannot be negative.")
        return True

@dataclass
class WaterSubSchema10:
    entity_id: int
    sensor_reading: float
    notes: Optional[str] = None

    def validate(self):
        if self.sensor_reading < 0:
            raise Exception("Reading cannot be negative.")
        return True

@dataclass
class WaterSubSchema11:
    entity_id: int
    sensor_reading: float
    notes: Optional[str] = None

    def validate(self):
        if self.sensor_reading < 0:
            raise Exception("Reading cannot be negative.")
        return True

@dataclass
class WaterSubSchema12:
    entity_id: int
    sensor_reading: float
    notes: Optional[str] = None

    def validate(self):
        if self.sensor_reading < 0:
            raise Exception("Reading cannot be negative.")
        return True

@dataclass
class WaterSubSchema13:
    entity_id: int
    sensor_reading: float
    notes: Optional[str] = None

    def validate(self):
        if self.sensor_reading < 0:
            raise Exception("Reading cannot be negative.")
        return True

@dataclass
class WaterSubSchema14:
    entity_id: int
    sensor_reading: float
    notes: Optional[str] = None

    def validate(self):
        if self.sensor_reading < 0:
            raise Exception("Reading cannot be negative.")
        return True
