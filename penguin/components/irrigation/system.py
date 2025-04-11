# -*- coding: utf-8 -*-
"""
penguin.components.irrigation.system
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


"""

from __future__ import annotations

from typing import List

import pandas as pd
from lori import ChannelState, Configurations
from lori.components import Component, register_component_type
from penguin.components.irrigation import IrrigationSeries


@register_component_type("irr", "irrigation", "watering")
class IrrigationSystem(Component):
    INCLUDES = ["storage", *IrrigationSeries.INCLUDES]

    # noinspection PyTypeChecker
    @property
    def series(self) -> List[IrrigationSeries]:
        return self.components.get_all(IrrigationSeries)

    def configure(self, configs: Configurations) -> None:
        super().configure(configs)
        self.components.load_from_type(
            IrrigationSeries,
            "series",
            key="series",
            name=f"{self.name} Series",
            includes=IrrigationSeries.INCLUDES
        )

        # As % of plant available water capacity (PAWC)
        # self.data.add("water_supply_min", name="Water supply coverage min [%]", type=float)
        # self.data.add("water_supply_max", name="Water supply coverage max [%]", type=float)
        self.data.add("water_supply_mean", name="Water supply coverage mean [%]", type=float)

        self.data.add("storage_level", name="Storage Level [%]", type=float)

    # noinspection SpellCheckingInspection
    def activate(self) -> None:
        super().activate()
        water_supplies = []
        for series in self.series:
            water_supplies.append(series.soil.data.water_supply)

        self.data.register(self._water_supply_callback, *water_supplies, how="all", unique=True)

    def _water_supply_callback(self, data: pd.DataFrame) -> None:
        water_supply = data[[c for c in data.columns if "water_supply" in c]]
        if not water_supply.empty:
            water_supply_mean = water_supply.ffill().bfill().mean(axis="columns")
            if len(water_supply_mean) == 1:
                water_supply_mean = water_supply_mean.iloc[0]
            self.data.water_supply_mean.value = water_supply_mean
        else:
            self.data.water_supply_mean.state = ChannelState.NOT_AVAILABLE
