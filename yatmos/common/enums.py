import strawberry
from enum import Enum


@strawberry.enum
class Status(str, Enum):
    UNKNOWN = "UNKNOWN"
    PASS = "PASS"
    FAIL = "FAIL"
