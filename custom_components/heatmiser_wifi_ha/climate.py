"""Heatmiser Wifi Platform for Home Assistant."""
import logging

from heatmiser_wifi import Heatmiser
import voluptuous as vol

import homeassistant.helpers.config_validation as cv

from homeassistant.components.climate import (
    PLATFORM_SCHEMA, ClimateEntity)

from homeassistant.components.climate.const import (
    SUPPORT_TARGET_TEMPERATURE, HVAC_MODE_OFF, HVAC_MODE_HEAT, 
    CURRENT_HVAC_OFF, CURRENT_HVAC_HEAT, CURRENT_HVAC_IDLE)

from homeassistant.const import (
    CONF_HOST, CONF_PORT, CONF_PIN, TEMP_CELSIUS, TEMP_FAHRENHEIT, 
    ATTR_FRIENDLY_NAME, ATTR_TEMPERATURE)

_LOGGER = logging.getLogger(__name__)

# Validation of the user's configuration
PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_HOST): cv.string,
    vol.Optional(CONF_PORT, default=8068): cv.port,
    vol.Optional(CONF_PIN, default=0): cv.positive_int,
    vol.Optional(ATTR_FRIENDLY_NAME, default='_not_set_'): cv.string
})


def setup_platform(hass, config, add_entities, discovery_info=None):
    # Assign configuration variables.
    # The configuration check takes care they are present.
    host = config[CONF_HOST]
    port = config[CONF_PORT]
    pin = config[CONF_PIN]
    name = config[ATTR_FRIENDLY_NAME]

    # Add devices
    add_entities([HeatmiserWifi(host, port, pin, name)], True)


class HeatmiserWifi(ClimateEntity):

    def __init__(self, host, port, pin, name):
        self._heatmiser = Heatmiser(host,port,pin)
        self._heatmiser_info = []
        self._name = name

    @property
    def name(self):
        if self._name == '_not_set_':
            self._name = 'Heatmiser ' + self._heatmiser_info['model']
        return self._name

    @property
    def supported_features(self):
        return SUPPORT_TARGET_TEMPERATURE

    @property
    def temperature_unit(self):
        if self._heatmiser_info['temperature_format'] == 'Celsius':
            return TEMP_CELSIUS
        return TEMP_FAHRENHEIT

    @property
    def current_temperature(self):
        return self._heatmiser_info['air_temp']

    @property
    def target_temperature(self):
        return self._heatmiser_info['set_room_temp']

    @property
    def target_temperature_high(self):
        return self._heatmiser_info['set_room_temp']

    @property
    def target_temperature_low(self):
        return self._heatmiser_info['set_room_temp'] - self._heatmiser_info['switch_differential']

    @property
    def max_temp(self):
        if self._heatmiser_info['temperature_format'] == 'Celsius':
            return 35 # Celsius
        return 95 # Fahrenheit

    @property
    def min_temp(self):
        if self._heatmiser_info['temperature_format'] == 'Celsius':
            return 5 # Celsius
        return 45 # Fahrenheit

    @property
    def hvac_mode(self):
        if self._heatmiser_info['on_off'] == 'Off':
            return HVAC_MODE_OFF
        return HVAC_MODE_HEAT

    @property
    def hvac_modes(self):
        return [HVAC_MODE_OFF, HVAC_MODE_HEAT]

    @property
    def hvac_action(self):
        if self._heatmiser_info['on_off'] == 'Off':
            return CURRENT_HVAC_OFF
        elif self._heatmiser_info['heating_is_currently_on']:
            return CURRENT_HVAC_HEAT
        return CURRENT_HVAC_IDLE

    @property
    def is_aux_heat(self):
        return self._heatmiser_info['heating_is_currently_on']



    def set_temperature(self, **kwargs):
        temperature = kwargs.get(ATTR_TEMPERATURE)
        if temperature == None:
            return
        self._heatmiser.connect()
        self._heatmiser.set_value('set_room_temp', temperature)
        self._heatmiser_info = self._heatmiser.get_info() # Update
        self._heatmiser.disconnect()

    def set_hvac_mode(self, hvac_mode):
        on_off = 'On'
        if hvac_mode == HVAC_MODE_OFF:
            on_off = 'Off'
        elif hvac_mode != HVAC_MODE_HEAT:
            return # Invalid mode return
        self._heatmiser.connect()
        self._heatmiser.set_value('on_off', on_off)
        self._heatmiser_info = self._heatmiser.get_info() # Update
        self._heatmiser.disconnect()
        


    def update(self):
        self._heatmiser.connect()
        self._heatmiser_info = self._heatmiser.get_info()
        self._heatmiser.disconnect()