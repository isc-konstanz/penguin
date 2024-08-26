# -*- coding: utf-8 -*-
"""
    penguin.components
    ~~~~~~~~~~~~~~~~~~


"""

from . import weather  # noqa: F401
from .weather import Weather

from .current import (  # noqa: F401
    DirectCurrent,
    AlternatingCurrent,
)
from .storage import (  # noqa: F401
    ElectricalEnergyStorage,
    ThermalEnergyStorage,
)
from .vehicle import ElectricVehicle  # noqa: F401

from . import solar  # noqa: F401
from .solar import (  # noqa: F401
    SolarArray,
    SolarSystem,
)

from . import irrigation  # noqa: F401
from .irrigation import (  # noqa: F401
    IrrigationArray,
    IrrigationSystem,
)
