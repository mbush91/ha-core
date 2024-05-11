import asyncio
from datetime import timedelta
import logging

from homeassistant.components.bluetooth import async_get_scanner
from homeassistant.core import HomeAssistant
from homeassistant.helpers.event import async_track_time_interval

_LOGGER = logging.getLogger(__name__)

def setup(hass: HomeAssistant, config: dict):
    _LOGGER.warning("Starting Bluetooth Logger setup")  # Check if this logs
    async_track_time_interval(hass, log_bluetooth_data, timedelta(seconds=5))
    _LOGGER.warning("Bluetooth Logger setup completed")  # Check if this logs
    return True

async def log_bluetooth_data(hass):
    try:
        scanner = async_get_scanner(hass)
        devices = await scanner.discover()
        for device in devices:
            for manufacturer_id, data in device.metadata['manufacturer_data'].items():
              if manufacturer_id == 2167 :
                  _LOGGER.warning(f"Device found: {device}, Data: {data}, MID: {manufacturer_id}")
    except Exception as e:
        _LOGGER.error(f"Error during Bluetooth scan: {e!s}")  # Log any exceptions
