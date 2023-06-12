from decimal import Decimal

PLACEMENT_CODES = {
    "even": [
        ("PR0", 0),
        ("PR1", 0.5),
        ("PR2", 0),
        ("PR3", 0),
        ("PR4", 0.5),
        ("PR5", 0),
    ],
    "weighted": [
        ("PR0", 0),
        ("PR1", 0.25),
        ("PR2", 0),
        ("PR3", 0),
        ("PR4", 0.75),
        ("PR5", 0),
    ],
}

PLACE_CHANGE_CODES = [
    "CARPL",
    "CLOSE",
    "ALLEG",
    "STAND",
    "APPRR",
    "CREQB",
    "CREQO",
    "CHILD",
    "LAREQ",
    "PLACE",
    "CUSTOD",
    "OTHER",
]

PLACEMENT_TYPE_CODES = {
    "A3": {
        "probability": Decimal(0.01),
        "probability_age_5": Decimal(0.01),
        "provability_age_16": Decimal(0.01),
    },
    "A4": {
        "probability": Decimal(0.01),
        "probability_age_5": Decimal(0.01),
        "provability_age_16": Decimal(0.01),
    },
    "A5": {
        "probability": Decimal(0.01),
        "probability_age_5": Decimal(0.01),
        "provability_age_16": Decimal(0.01),
    },
    "A6": {
        "probability": Decimal(0.01),
        "probability_age_5": Decimal(0.01),
        "provability_age_16": Decimal(0.01),
    },
    "H5": {
        "probability": Decimal(0.35),
        "probability_age_5": Decimal(0),
        "provability_age_16": Decimal(0),
    },
    "K1": {
        "probability": Decimal(0.005),
        "probability_age_5": Decimal(0),
        "provability_age_16": Decimal(0.005),
    },
    "K2": {
        "probability": Decimal(0.005),
        "probability_age_5": Decimal(0),
        "provability_age_16": Decimal(0.125),
    },
    "P1": {
        "probability": Decimal(0.005),
        "probability_age_5": Decimal(0.01),
        "provability_age_16": Decimal(0.05),
    },
    "P2": {
        "probability": Decimal(0.35),
        "probability_age_5": Decimal(0),
        "provability_age_16": Decimal(0),
    },
    "P3": {
        "probability": Decimal(0.01),
        "probability_age_5": Decimal(0),
        "provability_age_16": Decimal(0),
    },
    "R1": {
        "probability": Decimal(0.01),
        "probability_age_5": Decimal(0),
        "provability_age_16": Decimal(0.01),
    },
    "R2": {
        "probability": Decimal(0.01),
        "probability_age_5": Decimal(0.01),
        "provability_age_16": Decimal(0.01),
    },
    "R3": {
        "probability": Decimal(0.0),
        "probability_age_5": Decimal(0.01),
        "provability_age_16": Decimal(0),
    },
    "R5": {
        "probability": Decimal(0.005),
        "probability_age_5": Decimal(0),
        "provability_age_16": Decimal(0),
    },
    "S1": {
        "probability": Decimal(0.01),
        "probability_age_5": Decimal(0),
        "provability_age_16": Decimal(0.01),
    },
    "U1": {
        "probability": Decimal(0.01),
        "probability_age_5": Decimal(0.01),
        "provability_age_16": Decimal(0.03),
    },
    "U2": {
        "probability": Decimal(0.01),
        "probability_age_5": Decimal(0.01),
        "provability_age_16": Decimal(0.03),
    },
    "U3": {
        "probability": Decimal(0.01),
        "probability_age_5": Decimal(0.01),
        "provability_age_16": Decimal(0.03),
    },
    "U4": {
        "probability": Decimal(0.08),
        "probability_age_5": Decimal(0.445),
        "provability_age_16": Decimal(0.325),
    },
    "U5": {
        "probability": Decimal(0.08),
        "probability_age_5": Decimal(0.445),
        "provability_age_16": Decimal(0.325),
    },
    "U6": {
        "probability": Decimal(0.01),
        "probability_age_5": Decimal(0.01),
        "provability_age_16": Decimal(0.01),
    },
}

"""    ("A3", 0.01),
    ("A4", 0.01),
    ("A5", 0.01),
    ("A6", 0.01),
    ("P1", 0.01),
    ("R2", 0.01),
    ("R3", 0.01),
    ("U1", 0.01),
    ("U2", 0.01),
    ("U3", 0.01),
    ("U4", 0.445),
    ("U5", 0.445),
    ("U6", 0.01),
]
"""
