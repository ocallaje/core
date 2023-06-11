"""The Dummy Garage integration."""
from __future__ import annotations

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Dummy Garage from a config entry."""
    # Optionally store an object for your platforms to access
    # hass.data[DOMAIN][entry.entry_id] = ...

    # Optionally validate config entry options before setting up platform

    await hass.config_entries.async_forward_entry_setups(entry, (Platform.SENSOR,))

    # Remove if the integration does not have an options flow
    # entry.async_on_unload(entry.add_update_listener(config_entry_update_listener))

    return True


# Remove if the integration does not have an options flow
# async def config_entry_update_listener(hass: HomeAssistant, entry: ConfigEntry) -> None:
#    """Update listener, called when the config entry options are changed."""
#    await hass.config_entries.async_reload(entry.entry_id)


# async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
#    """Unload a config entry."""
#    if unload_ok := await hass.config_entries.async_unload_platforms(
#        entry, (Platform.SENSOR,)
#    ):
#        hass.data[DOMAIN].pop(entry.entry_id)

#    return unload_ok
