from dataclasses import dataclass
from typing import List, Union, Optional, Dict


@dataclass
class Dataset:
    label: str
    data: List[Union[int, float, Dict[str, Union[int, float]]]]
    backgroundColor: Optional[Union[str, List[str]]] = None
    borderColor: Optional[Union[str, List[str]]] = None
    borderWidth: Optional[int] = None
    fill: Optional[Union[bool, str]] = None  # Filler Plugin support
    order: Optional[int] = 0  # Support for drawing order
    tension: Optional[float] = None
    pointStyle: Optional[str] = None
    hoverBackgroundColor: Optional[str] = None
    steppedLine: Optional[bool] = None
    pointRadius: Optional[int] = None
    pointHoverRadius: Optional[int] = None
    pointHoverBackgroundColor: Optional[str] = None

    def to_dict(self) -> Dict:
        """Convert the dataset into a dictionary for Chart.js."""
        return {
            "label": self.label,
            "data": self.data,
            "backgroundColor": self.backgroundColor,
            "borderColor": self.borderColor,
            "borderWidth": self.borderWidth,
            "fill": self.fill,
            "order": self.order,
            "tension": self.tension,
            "pointStyle": self.pointStyle,
            "hoverBackgroundColor": self.hoverBackgroundColor,
            "steppedLine": self.steppedLine,
            "pointRadius": self.pointRadius,
            "pointHoverRadius": self.pointHoverRadius,
            "pointHoverBackgroundColor": self.pointHoverBackgroundColor,
        }
