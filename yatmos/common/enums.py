from enum import Enum


class Status(str, Enum):
    UNKNOWN = "UNKNOWN"
    PASS = "PASS"
    FAIL = "FAIL"
