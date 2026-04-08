from pydantic import BaseModel, ConfigDict, field_validator
from typing import Optional
from enum import Enum


class BloodType(str, Enum):
    A_POS  = "A+"
    A_NEG  = "A-"
    B_POS  = "B+"
    B_NEG  = "B-"
    AB_POS = "AB+"
    AB_NEG = "AB-"
    O_POS  = "O+"
    O_NEG  = "O-"


class ProfileUpdate(BaseModel):
    full_name: Optional[str] = None
    phone_number: Optional[str] = None
    location: Optional[str] = None
    blood_type: Optional[BloodType] = None
    blood_pressure: Optional[bool] = None
    blood_sugar: Optional[bool] = None
    weight: Optional[float] = None
    height: Optional[float] = None

    @field_validator("phone_number")
    @classmethod
    def phone_digits_only(cls, v: Optional[str]) -> Optional[str]:
        if v is not None and not v.isdigit():
            raise ValueError("phone_number must contain digits only")
        return v


class ProfileOut(BaseModel):
    id: int
    user_id: int
    full_name: Optional[str] = None
    phone_number: Optional[str] = None
    location: Optional[str] = None
    blood_type: Optional[BloodType] = None
    blood_pressure: Optional[bool] = None
    blood_sugar: Optional[bool] = None
    weight: Optional[float] = None
    height: Optional[float] = None

    model_config = ConfigDict(from_attributes=True)
