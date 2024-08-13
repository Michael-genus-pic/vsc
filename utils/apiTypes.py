from datetime import datetime
from pydantic import BaseModel
from enum import Enum
from typing import Dict, Optional, Literal

class RawAnimal(BaseModel):
    ident: int
    litterId: int
    birthDate: datetime
    farmId: int = None



class RawLitter(BaseModel): 
    litterId: int
    sire: int
    dam: int

class Litter(RawLitter):
    id: str    
    piglets: list[int] = []
    

class Message(BaseModel):
    msg: str

class RunQueueResult(BaseModel):
    success: int
    reQueued: int
    stopped: int

class ApiQueueData(BaseModel):
    destination: str
    function: str
    params: Optional[Dict]

class ScheduleQueueData(BaseModel):
    delay: int
    params: Optional[Dict]


class OnTest(BaseModel):
    ident: int
    testDate: datetime
    weight: float
    score: int

class Event(BaseModel):
    id: str
    eventName: str
    eventData: OnTest

class Animal(RawAnimal): 
    id: str
    events: list[Event] = []

class LitterWithLitterMates(Litter):
    litterMates: list[Animal] 
