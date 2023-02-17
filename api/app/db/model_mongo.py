from typing import List, Union

from pydantic import BaseModel


class Ustavka(BaseModel):
    alarm_max: str
    alarm_min: str
    warning_max: str
    warning_min: str


class Temp(BaseModel):
    temp: str


class TempHeat(BaseModel):
    us: Ustavka
    temp: Temp


class VibrAxial(BaseModel):
    vibr_axial: str
    us: Ustavka

class VibrHori(BaseModel):
    vibr_hori: str
    us: Ustavka

class VibrVert(BaseModel):
    vibr_vert: str
    us: Ustavka


class Vibr(BaseModel):
    vibr_axial: VibrAxial
    vibr_hori: VibrHori
    vibr_vert: VibrVert


class Podsh(BaseModel):
    temp_heat: TempHeat


class PodshExtend(Podsh):
    vibration: Vibr


class Oil(BaseModel):
    temp_b: str
    temp_a: str


class Water(BaseModel):
    temp_b: str
    temp_a: str


class Coooler(BaseModel):
    oil: Oil
    water: Water


class GasCol(BaseModel):
    temp_b: str
    temp_a: str


class GasValve(BaseModel):
    closed: str
    open: str
    posit: str


class MainDrive(BaseModel):
    r_c: str
    r_v: str
    s_c: str
    s_v: str


class OilSys(BaseModel):
    l: str
    p: str


class Work(BaseModel):
    w: str


class Exgauter(BaseModel):
    bear_1: PodshExtend
    bear_2: PodshExtend
    bear_3: Podsh
    bear_4: Podsh
    bear_5: Podsh
    bear_6: Podsh
    bear_7: PodshExtend
    bear_8: PodshExtend
    bear_9: Podsh
    cooler: Coooler
    gas_valve: GasValve
    gas_col: GasCol
    gas_valve: GasValve
    main_drive: MainDrive
    oil_sys: OilSys
    work: Work


