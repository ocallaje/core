"""Sensor platform for Dummy Garage integration."""
from __future__ import annotations

import voluptuous as vol  # yes

from homeassistant.components.sensor import (
    PLATFORM_SCHEMA,
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)

# from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_MAC, CONF_NAME, UnitOfTemperature
from homeassistant.core import HomeAssistant  # yes
import homeassistant.helpers.config_validation as cv  # yes

# from homeassistant.helpers import entity_registry as er  # yes
from homeassistant.helpers.entity_platform import AddEntitiesCallback  # yes
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType  # yes

DEFAULT_NAME = "Dummy Garage - Sensor"

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_MAC): cv.string,
        vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
    }
)

'''
async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Initialize Dummy Garage config entry."""
    registry = er.async_get(hass)
    # Validate + resolve entity registry id to entity_id
    entity_id = er.async_validate_entity_id(
        registry, config_entry.options[CONF_ENTITY_ID]
    )
    #Optionally validate config entry options before creating entity
    name = config_entry.title
    unique_id = config_entry.entry_id

    async_add_entities([dummy_garageSensorEntity(unique_id, name, entity_id)])
'''


async def async_setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None,
) -> None:
    """Set up the sensor platform."""
    name = config[CONF_NAME]
    mac_addr = config[CONF_MAC]

    add_entities([DummyGarageSensor(mac_addr, name)], True)


class DummyGarageSensor(SensorEntity):
    """Representation of a Sensor."""

    def __init__(self, mac, name) -> None:
        """Docstring."""
        super().__init__()
        self._mac = mac
        self._name = name
        self._attr_name = name
        self._attr_native_unit_of_measurement = UnitOfTemperature.CELSIUS
        self._attr_device_class = SensorDeviceClass.TEMPERATURE
        self._attr_state_class = SensorStateClass.MEASUREMENT

    @property
    def name(self) -> str:
        """Return the name of the switch."""
        return self._name

    @property
    def unique_id(self) -> str:
        """Return a unique, Home Assistant friendly identifier for this entity."""
        return self._mac.replace(":", "")

    def update(self) -> None:
        """Fetch new state data for the sensor.

        This is the only method that should fetch new data for Home Assistant.
        """
        self._attr_native_value = 23
