# -*- coding: utf-8 -*-
"""
penguin.components.irrigation.series
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


"""

from __future__ import annotations

from lori import Component, Configurations, Constant
from penguin.components.irrigation import SoilMoisture


# noinspection SpellCheckingInspection
class IrrigationSeries(Component):
    SECTION = "series"
    INCLUDES = [SoilMoisture.SECTION]

    STATE = Constant(bool, "watering_state", "Watering state")

    soil: SoilMoisture

    def __init__(self, context: Context, configs: Configurations, key="series", name="Series", **kwargs) -> None:  # noqa
        super().__init__(context, configs, key=key, name=name, **kwargs)
        self.soil = SoilMoisture(
            self,
            configs.get_section(
                section=SoilMoisture.SECTION,
                defaults=Component._build_defaults(configs, strict=True),
            ),
        )

    def configure(self, configs: Configurations) -> None:
        super().configure(configs)
        self.soil.configure(
            configs.get_section(
                section=SoilMoisture.SECTION,
                defaults=Component._build_defaults(configs, strict=True),
            )
        )
        self.data.add(IrrigationSeries.STATE, aggregate="max")

    # noinspection SpellCheckingInspection
    def activate(self) -> None:
        super().activate()
        self.soil.activate()

    def deactivate(self) -> None:
        super().deactivate()
        self.soil.deactivate()
