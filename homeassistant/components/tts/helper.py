"""Provide helper functions for the TTS."""

from __future__ import annotations

from typing import TYPE_CHECKING

from homeassistant.core import HomeAssistant

from .const import DATA_TTS_MANAGER, DOMAIN_DATA

if TYPE_CHECKING:
    from . import TextToSpeechEntity
    from .legacy import Provider


def get_engine_instance(
    hass: HomeAssistant, engine: str
) -> TextToSpeechEntity | Provider | None:
    """Get engine instance."""
    if entity := hass.data[DOMAIN_DATA].get_entity(engine):
        return entity

    return hass.data[DATA_TTS_MANAGER].providers.get(engine)
