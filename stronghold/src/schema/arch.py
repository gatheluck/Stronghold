from dataclasses import dataclass

from omegaconf import MISSING


@dataclass
class ArchConfig:
    num_classes: int = MISSING


# configs for resnet architecures
@dataclass
class ResnetConfig(ArchConfig):
    pretrained: bool = MISSING


@dataclass
class Resnet50Config(ResnetConfig):
    _target_: str = "torchvision.models.resnet50"


@dataclass
class Resnet56Config(ResnetConfig):
    _target_: str = "archs.resnet56"


# configs for wide resnet architecures
@dataclass
class WideresnetConfig(ArchConfig):
    widening_factor: int = MISSING
    droprate: float = MISSING


@dataclass
class Wideresnet40Config(WideresnetConfig):
    _target_: str = "archs.wideresnet40"
