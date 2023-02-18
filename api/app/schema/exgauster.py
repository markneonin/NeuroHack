from enum import Enum
from typing import Any

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
    temperature: float
    vibration_axial: float
    vibration_vertical: float
    vibration_horizontal: float


class BearingSmall(BaseModel):
    number: int
    temperature: float


class Cooler(BaseModel):
    water_temperature_before: float
    water_temperature_after: float
    oil_temperature_before: float
    oil_temperature_after: float


class GasManifold(BaseModel):
    temperature_before: float
    underpressure_before: float


class ValvePosition(BaseModel):
    gas_valve_closed: float
    gas_valve_open: float
    gas_valve_position: float


class MainDrive(BaseModel):
    rotor_current: float
    rotor_voltage: float
    stator_current: float
    stator_voltage: float


class OilSystem(BaseModel):
    oil_level: float
    oil_pressure: float


class ExgausterWork(BaseModel):
    work: float


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


exg = {
    'number': 1,
    'name': 'У-171',
    'bearings_big': [ObjectId(), ObjectId()],
    'bearings_small': [ObjectId(), ObjectId()],
    'cooler': ObjectId(),
    'gas_manifold': ObjectId(),
    'valve_position': ObjectId(),
    'main_drive': ObjectId(),
    'oil_system': ObjectId(),
    'exgauster_work': ObjectId(),

}
