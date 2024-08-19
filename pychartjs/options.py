from dataclasses import dataclass, field
from typing import Optional, Dict
from pychartjs.enums import Position, InteractionMode, AnimationEasing


@dataclass
class Legend:
    display: Optional[bool] = True
    position: Optional[Position] = Position.TOP
    labels: Optional[Dict] = None

    def to_dict(self) -> Dict:
        return {
            "display": self.display,
            "position": self.position.value,
            "labels": self.labels,
        }


@dataclass
class Tooltip:
    enabled: Optional[bool] = True
    mode: Optional[InteractionMode] = InteractionMode.NEAREST
    intersect: Optional[bool] = True
    callbacks: Optional[Dict[str, str]] = None  # Custom callbacks for tooltip

    def to_dict(self) -> Dict:
        tooltip_dict = {
            "enabled": self.enabled,
            "mode": self.mode.value,
            "intersect": self.intersect,
        }
        if self.callbacks:
            tooltip_dict["callbacks"] = self.callbacks
        return tooltip_dict


@dataclass
class Title:
    display: Optional[bool] = False
    text: Optional[str] = None
    position: Optional[Position] = Position.TOP

    def to_dict(self) -> Dict:
        return {
            "display": self.display,
            "text": self.text,
            "position": self.position.value,
        }


@dataclass
class Animation:
    duration: Optional[int] = 1000
    easing: Optional[AnimationEasing] = AnimationEasing.EASE_IN_OUT_CUBIC
    onComplete: Optional[str] = None  # Custom callback on animation complete
    onProgress: Optional[str] = None  # Custom callback on animation progress

    def to_dict(self) -> Dict:
        animation_dict = {
            "duration": self.duration,
            "easing": self.easing.value,
        }
        if self.onComplete:
            animation_dict["onComplete"] = self.onComplete
        if self.onProgress:
            animation_dict["onProgress"] = self.onProgress
        return animation_dict


@dataclass
class Layout:
    padding: Optional[Dict[str, int]] = None

    def to_dict(self) -> Dict:
        return {
            "padding": self.padding,
        }


@dataclass
class Interaction:
    mode: Optional[InteractionMode] = InteractionMode.NEAREST
    intersect: Optional[bool] = True

    def to_dict(self) -> Dict:
        return {
            "mode": self.mode.value,
            "intersect": self.intersect,
        }


@dataclass
class ChartOptions:
    responsive: Optional[bool] = True
    maintainAspectRatio: Optional[bool] = True
    legend: Optional[Legend] = field(default_factory=Legend)
    tooltip: Optional[Tooltip] = field(default_factory=Tooltip)
    title: Optional[Title] = field(default_factory=Title)
    animation: Optional[Animation] = field(default_factory=Animation)
    layout: Optional[Layout] = field(default_factory=Layout)
    interaction: Optional[Interaction] = field(default_factory=Interaction)

    def to_dict(self) -> Dict:
        return {
            "responsive": self.responsive,
            "maintainAspectRatio": self.maintainAspectRatio,
            "legend": self.legend.to_dict(),
            "tooltip": self.tooltip.to_dict(),
            "title": self.title.to_dict(),
            "animation": self.animation.to_dict(),
            "layout": self.layout.to_dict(),
            "interaction": self.interaction.to_dict(),
        }
