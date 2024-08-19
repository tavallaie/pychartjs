from enum import Enum


class ChartType(Enum):
    BAR = "bar"
    LINE = "line"
    PIE = "pie"
    DOUGHNUT = "doughnut"
    RADAR = "radar"
    POLAR_AREA = "polarArea"
    BUBBLE = "bubble"
    SCATTER = "scatter"


class ScaleType(Enum):
    LINEAR = "linear"
    LOGARITHMIC = "logarithmic"
    TIME = "time"
    CATEGORY = "category"


class Position(Enum):
    TOP = "top"
    LEFT = "left"
    BOTTOM = "bottom"
    RIGHT = "right"


class InteractionMode(Enum):
    POINT = "point"
    NEAREST = "nearest"
    INDEX = "index"
    DATASET = "dataset"
    X = "x"
    Y = "y"


class AnimationEasing(Enum):
    EASE_IN_QUAD = "easeInQuad"
    EASE_OUT_QUAD = "easeOutQuad"
    EASE_IN_OUT_QUAD = "easeInOutQuad"
    EASE_IN_CUBIC = "easeInCubic"
    EASE_OUT_CUBIC = "easeOutCubic"
    EASE_IN_OUT_CUBIC = "easeInOutCubic"
