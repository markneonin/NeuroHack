from enum import Enum
from typing import Any, Optional

from bson import ObjectId
from pydantic import BaseModel


class Status(str, Enum):
    NORMAL = 'normal'
    WARNING = 'warning'
    ALARM = 'alarm'


class Value(BaseModel):
    value: Any
    status: Status


class BearingBig(BaseModel):
    number: int
    temperature: Optional[float]
    vibration_axial: Optional[float]
    vibration_vertical: Optional[float]
    vibration_horizontal: Optional[float]


class BearingSmall(BaseModel):
    number: int
    temperature: Optional[float]


class Cooler(BaseModel):
    water_temperature_before: Optional[float]
    water_temperature_after: Optional[float]
    oil_temperature_before: Optional[float]
    oil_temperature_after: Optional[float]


class GasManifold(BaseModel):
    temperature_before: Optional[float]
    underpressure_before: Optional[float]


class ValvePosition(BaseModel):
    gas_valve_closed: Optional[float]
    gas_valve_open: Optional[float]
    gas_valve_position: Optional[float]


class MainDrive(BaseModel):
    rotor_current: Optional[float]
    rotor_voltage: Optional[float]
    stator_current: Optional[float]
    stator_voltage: Optional[float]


class OilSystem(BaseModel):
    oil_level: Optional[float]
    oil_pressure: Optional[float]


class ExgausterWork(BaseModel):
    work: Optional[float]


class Exgauster(BaseModel):
    number: int
    name: str
    bearings_big: list[BearingBig]
    bearings_small: list[BearingSmall]
    cooler: Cooler
    gas_manifold: GasManifold
    valve_position: ValvePosition
    main_drive: MainDrive
    oil_system: OilSystem
    exgauster_work: ExgausterWork

