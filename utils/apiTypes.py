from datetime import datetime
from pydantic import BaseModel
from enum import Enum
from typing import Dict, Optional, Literal

class RawAnimal(BaseModel):
    ident: int
    litterId: int
    birthDate: datetime
    farmId: int = None

class Animal(RawAnimal): 
    id: str


class RawLitter(BaseModel): 
    litterId: int
    sire: int
    dam: int

class Litter(RawLitter):
    id: str    
    piglets: list[int] = []
    
class LitterWithLitterMates(Litter):
    litterMates: list[Animal]

class Message(BaseModel):
    msg: str

class RunQueueResult(BaseModel):
    success: int
    reQueued: int
    stopped: int

class QueueData(BaseModel):
    destination: str
    function: str
    params: Optional[Dict]