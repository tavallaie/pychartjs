from dataclasses import dataclass, field
from typing import Optional, Dict
from pychartjs.enums import ScaleType, Position


@dataclass
class GridLines:
    color: Optional[str] = None
    lineWidth: Optional[int] = None
    drawBorder: Optional[bool] = None
    drawOnChartArea: Optional[bool] = None
    drawTicks: Optional[bool] = None

    def to_dict(self) -> Dict:
        return {
            "color": self.color,
            "lineWidth": self.lineWidth,
            "drawBorder": self.drawBorder,
            "drawOnChartArea": self.drawOnChartArea,
            "drawTicks": self.drawTicks,
        }


@dataclass
class Scale:
    scale_type: ScaleType
    display: Optional[bool] = True
    position: Optional[Position] = Position.LEFT
    gridLines: Optional[GridLines] = field(default_factory=GridLines)

    def to_dict(self) -> Dict:
        """Convert the scale into a dictionary for Chart.js."""
        return {
            "type": self.scale_type.value,
            "display": self.display,
            "position": self.position.value,
            "gridLines": self.gridLines.to_dict(),
        }


@dataclass
class LinearScale(Scale):
    beginAtZero: Optional[bool] = False
    min: Optional[int] = None
    max: Optional[int] = None
    stepSize: Optional[int] = None

    def to_dict(self) -> Dict:
        data = super().to_dict()
        data.update(
            {
                "beginAtZero": self.beginAtZero,
                "min": self.min,
                "max": self.max,
                "stepSize": self.stepSize,
            }
        )
        return data


@dataclass
class LogarithmicScale(Scale):
    min: Optional[int] = None
    max: Optional[int] = None

    def to_dict(self) -> Dict:
        data = super().to_dict()
        data.update(
            {
                "min": self.min,
                "max": self.max,
            }
        )
        return data


@dataclass
class TimeScale(Scale):
    time_format: Optional[str] = None
    tooltipFormat: Optional[str] = None
    unit: Optional[str] = None
    stepSize: Optional[int] = None
    displayFormats: Optional[Dict] = None

    def to_dict(self) -> Dict:
        data = super().to_dict()
        data.update(
            {
                "time": {
                    "parser": self.time_format,
                    "tooltipFormat": self.tooltipFormat,
                    "unit": self.unit,
                    "stepSize": self.stepSize,
                    "displayFormats": self.displayFormats,
                },
            }
        )
        return data
