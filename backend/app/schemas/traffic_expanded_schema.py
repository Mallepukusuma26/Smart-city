"""
Validation Schemas for Traffic.
"""
from dataclasses import dataclass
from typing import Optional

@dataclass
class TrafficCreateSchema:
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
class TrafficSubSchema1:
    entity_id: int
    sensor_reading: float
    notes: Optional[str] = None

    def validate(self):
        if self.sensor_reading < 0:
            raise Exception("Reading cannot be negative.")
        return True

@dataclass
class TrafficSubSchema2:
    entity_id: int
    sensor_reading: float
    notes: Optional[str] = None

    def validate(self):
        if self.sensor_reading < 0:
            raise Exception("Reading cannot be negative.")
        return True

@dataclass
class TrafficSubSchema3:
    entity_id: int
    sensor_reading: float
    notes: Optional[str] = None

    def validate(self):
        if self.sensor_reading < 0:
            raise Exception("Reading cannot be negative.")
        return True

@dataclass
class TrafficSubSchema4:
    entity_id: int
    sensor_reading: float
    notes: Optional[str] = None

    def validate(self):
        if self.sensor_reading < 0:
            raise Exception("Reading cannot be negative.")
        return True

@dataclass
class TrafficSubSchema5:
    entity_id: int
    sensor_reading: float
    notes: Optional[str] = None

    def validate(self):
        if self.sensor_reading < 0:
            raise Exception("Reading cannot be negative.")
        return True

@dataclass
class TrafficSubSchema6:
    entity_id: int
    sensor_reading: float
    notes: Optional[str] = None

    def validate(self):
        if self.sensor_reading < 0:
            raise Exception("Reading cannot be negative.")
        return True

@dataclass
class TrafficSubSchema7:
    entity_id: int
    sensor_reading: float
    notes: Optional[str] = None

    def validate(self):
        if self.sensor_reading < 0:
            raise Exception("Reading cannot be negative.")
        return True

@dataclass
class TrafficSubSchema8:
    entity_id: int
    sensor_reading: float
    notes: Optional[str] = None

    def validate(self):
        if self.sensor_reading < 0:
            raise Exception("Reading cannot be negative.")
        return True

@dataclass
class TrafficSubSchema9:
    entity_id: int
    sensor_reading: float
    notes: Optional[str] = None

    def validate(self):
        if self.sensor_reading < 0:
            raise Exception("Reading cannot be negative.")
        return True

@dataclass
class TrafficSubSchema10:
    entity_id: int
    sensor_reading: float
    notes: Optional[str] = None

    def validate(self):
        if self.sensor_reading < 0:
            raise Exception("Reading cannot be negative.")
        return True

@dataclass
class TrafficSubSchema11:
    entity_id: int
    sensor_reading: float
    notes: Optional[str] = None

    def validate(self):
        if self.sensor_reading < 0:
            raise Exception("Reading cannot be negative.")
        return True

@dataclass
class TrafficSubSchema12:
    entity_id: int
    sensor_reading: float
    notes: Optional[str] = None

    def validate(self):
        if self.sensor_reading < 0:
            raise Exception("Reading cannot be negative.")
        return True

@dataclass
class TrafficSubSchema13:
    entity_id: int
    sensor_reading: float
    notes: Optional[str] = None

    def validate(self):
        if self.sensor_reading < 0:
            raise Exception("Reading cannot be negative.")
        return True

@dataclass
class TrafficSubSchema14:
    entity_id: int
    sensor_reading: float
    notes: Optional[str] = None

    def validate(self):
        if self.sensor_reading < 0:
            raise Exception("Reading cannot be negative.")
        return True
