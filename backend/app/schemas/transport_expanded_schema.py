"""
Validation Schemas for Transport.
"""
from dataclasses import dataclass
from typing import Optional

@dataclass
class TransportCreateSchema:
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
class TransportSubSchema1:
    entity_id: int
    sensor_reading: float
    notes: Optional[str] = None

    def validate(self):
        if self.sensor_reading < 0:
            raise Exception("Reading cannot be negative.")
        return True

@dataclass
class TransportSubSchema2:
    entity_id: int
    sensor_reading: float
    notes: Optional[str] = None

    def validate(self):
        if self.sensor_reading < 0:
            raise Exception("Reading cannot be negative.")
        return True

@dataclass
class TransportSubSchema3:
    entity_id: int
    sensor_reading: float
    notes: Optional[str] = None

    def validate(self):
        if self.sensor_reading < 0:
            raise Exception("Reading cannot be negative.")
        return True

@dataclass
class TransportSubSchema4:
    entity_id: int
    sensor_reading: float
    notes: Optional[str] = None

    def validate(self):
        if self.sensor_reading < 0:
            raise Exception("Reading cannot be negative.")
        return True

@dataclass
class TransportSubSchema5:
    entity_id: int
    sensor_reading: float
    notes: Optional[str] = None

    def validate(self):
        if self.sensor_reading < 0:
            raise Exception("Reading cannot be negative.")
        return True

@dataclass
class TransportSubSchema6:
    entity_id: int
    sensor_reading: float
    notes: Optional[str] = None

    def validate(self):
        if self.sensor_reading < 0:
            raise Exception("Reading cannot be negative.")
        return True

@dataclass
class TransportSubSchema7:
    entity_id: int
    sensor_reading: float
    notes: Optional[str] = None

    def validate(self):
        if self.sensor_reading < 0:
            raise Exception("Reading cannot be negative.")
        return True

@dataclass
class TransportSubSchema8:
    entity_id: int
    sensor_reading: float
    notes: Optional[str] = None

    def validate(self):
        if self.sensor_reading < 0:
            raise Exception("Reading cannot be negative.")
        return True

@dataclass
class TransportSubSchema9:
    entity_id: int
    sensor_reading: float
    notes: Optional[str] = None

    def validate(self):
        if self.sensor_reading < 0:
            raise Exception("Reading cannot be negative.")
        return True

@dataclass
class TransportSubSchema10:
    entity_id: int
    sensor_reading: float
    notes: Optional[str] = None

    def validate(self):
        if self.sensor_reading < 0:
            raise Exception("Reading cannot be negative.")
        return True

@dataclass
class TransportSubSchema11:
    entity_id: int
    sensor_reading: float
    notes: Optional[str] = None

    def validate(self):
        if self.sensor_reading < 0:
            raise Exception("Reading cannot be negative.")
        return True

@dataclass
class TransportSubSchema12:
    entity_id: int
    sensor_reading: float
    notes: Optional[str] = None

    def validate(self):
        if self.sensor_reading < 0:
            raise Exception("Reading cannot be negative.")
        return True

@dataclass
class TransportSubSchema13:
    entity_id: int
    sensor_reading: float
    notes: Optional[str] = None

    def validate(self):
        if self.sensor_reading < 0:
            raise Exception("Reading cannot be negative.")
        return True

@dataclass
class TransportSubSchema14:
    entity_id: int
    sensor_reading: float
    notes: Optional[str] = None

    def validate(self):
        if self.sensor_reading < 0:
            raise Exception("Reading cannot be negative.")
        return True
