# -*- coding: utf-8 -*-
"""
    penguin
    ~~~~~~~

    This repository provides a set of python functions and scripts to calculate the
    energy generation and provide further utility for photovoltaic systems.

"""
from . import _version
__version__ = _version.get_versions().get("version")
del _version

from .location import Location  # noqa: F401

from . import components  # noqa: F401
from .components import (  # noqa: F401
    PVSystem,
    PVArray,
    ElectricVehicle,
    ElectricalEnergyStorage,
    ThermalEnergyStorage,
    Weather,
)

from . import system  # noqa: F401
from .system import System  # noqa: F401

from . import model  # noqa: F401
from .model import Model  # noqa: F401

from loris import Application  # noqa: F401


def load(name: str = "Penguin", factory=System, **kwargs) -> Application:
    return Application.load(name, factory=factory, **kwargs)
