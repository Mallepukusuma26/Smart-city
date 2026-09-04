"""
Validation Schemas for Complaint.
"""
from dataclasses import dataclass
from typing import Optional

@dataclass
class ComplaintCreateSchema:
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
class ComplaintSubSchema1:
    entity_id: int
    sensor_reading: float
    notes: Optional[str] = None

    def validate(self):
        if self.sensor_reading < 0:
            raise Exception("Reading cannot be negative.")
        return True

@dataclass
class ComplaintSubSchema2:
    entity_id: int
    sensor_reading: float
    notes: Optional[str] = None

    def validate(self):
        if self.sensor_reading < 0:
            raise Exception("Reading cannot be negative.")
        return True

@dataclass
class ComplaintSubSchema3:
    entity_id: int
    sensor_reading: float
    notes: Optional[str] = None

    def validate(self):
        if self.sensor_reading < 0:
            raise Exception("Reading cannot be negative.")
        return True

@dataclass
class ComplaintSubSchema4:
    entity_id: int
    sensor_reading: float
    notes: Optional[str] = None

    def validate(self):
        if self.sensor_reading < 0:
            raise Exception("Reading cannot be negative.")
        return True

@dataclass
class ComplaintSubSchema5:
    entity_id: int
    sensor_reading: float
    notes: Optional[str] = None

    def validate(self):
        if self.sensor_reading < 0:
            raise Exception("Reading cannot be negative.")
        return True

@dataclass
class ComplaintSubSchema6:
    entity_id: int
    sensor_reading: float
    notes: Optional[str] = None

    def validate(self):
        if self.sensor_reading < 0:
            raise Exception("Reading cannot be negative.")
        return True

@dataclass
class ComplaintSubSchema7:
    entity_id: int
    sensor_reading: float
    notes: Optional[str] = None

    def validate(self):
        if self.sensor_reading < 0:
            raise Exception("Reading cannot be negative.")
        return True

@dataclass
class ComplaintSubSchema8:
    entity_id: int
    sensor_reading: float
    notes: Optional[str] = None

    def validate(self):
        if self.sensor_reading < 0:
            raise Exception("Reading cannot be negative.")
        return True

@dataclass
class ComplaintSubSchema9:
    entity_id: int
    sensor_reading: float
    notes: Optional[str] = None

    def validate(self):
        if self.sensor_reading < 0:
            raise Exception("Reading cannot be negative.")
        return True

@dataclass
class ComplaintSubSchema10:
    entity_id: int
    sensor_reading: float
    notes: Optional[str] = None

    def validate(self):
        if self.sensor_reading < 0:
            raise Exception("Reading cannot be negative.")
        return True

@dataclass
class ComplaintSubSchema11:
    entity_id: int
    sensor_reading: float
    notes: Optional[str] = None

    def validate(self):
        if self.sensor_reading < 0:
            raise Exception("Reading cannot be negative.")
        return True

@dataclass
class ComplaintSubSchema12:
    entity_id: int
    sensor_reading: float
    notes: Optional[str] = None

    def validate(self):
        if self.sensor_reading < 0:
            raise Exception("Reading cannot be negative.")
        return True

@dataclass
class ComplaintSubSchema13:
    entity_id: int
    sensor_reading: float
    notes: Optional[str] = None

    def validate(self):
        if self.sensor_reading < 0:
            raise Exception("Reading cannot be negative.")
        return True

@dataclass
class ComplaintSubSchema14:
    entity_id: int
    sensor_reading: float
    notes: Optional[str] = None

    def validate(self):
        if self.sensor_reading < 0:
            raise Exception("Reading cannot be negative.")
        return True
