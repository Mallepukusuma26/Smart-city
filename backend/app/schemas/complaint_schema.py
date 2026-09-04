"""
Complaint Lifecycle Payload Schemas.
"""
from dataclasses import dataclass
from typing import Optional

@dataclass
class ComplaintCreateSchema:
    title: str
    description: str
    location: str
    zone: str = "Central Zone"
    category_id: Optional[int] = None
    priority: str = "MEDIUM"

    def validate(self):
        if not self.title or len(self.title) < 5:
            raise Exception("Title must be at least 5 characters long.")
        if not self.description or len(self.description) < 10:
            raise Exception("Description must be at least 10 characters long.")
        if not self.location:
            raise Exception("Location is required.")
        if self.priority not in ["LOW", "MEDIUM", "HIGH", "CRITICAL"]:
            raise Exception("Invalid priority level.")
        return True


@dataclass
class ComplaintUpdateSchema:
    status: str
    remarks: Optional[str] = None
    assigned_officer_id: Optional[int] = None

    def validate(self):
        valid_statuses = ["SUBMITTED", "ASSIGNED", "IN_PROGRESS", "ESCALATED", "RESOLVED", "CLOSED"]
        if self.status not in valid_statuses:
            raise Exception(f"Status must be one of {valid_statuses}")
        return True
