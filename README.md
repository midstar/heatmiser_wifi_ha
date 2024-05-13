# DEPRECATED - Heatmiser WiFi Home Assistant Component

[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/custom-components/hacs)
[![No Maintenance Intended](http://unmaintained.tech/badge.svg)](http://unmaintained.tech/)

This repository is no longer maintained. 

Please use clone at [iainbullock/heatmiser_wifi_ha](https://github.com/iainbullock/heatmiser_wifi_ha) instead.



## Overview
A [Heatmiser](http://www.heatmiser.com/) WiFi Thermostat Home Assistant plugin.

Supports:

* Read current air temperature
* Read/set temperature setting (i.e. wanted temperature)
* Read/set on/off of the Thermostat

Supported Heatmiser Thermostats are WiFi versions of DT, DT-E, PRT and PRT-E.

Note that non-WiFi thermostat versions (i.e. using RS-485 serial bus) 
connected through an Heatmiser Ethernet HUB are supported by the
[Home Assistant Heatmiser Core component](https://www.home-assistant.io/integrations/heatmiser/)

## Installation
Install through [HACS](https://hacs.xyz/).

Alternatively copy the heatmiser_wifi directory and its contents to the 
Home Assistant custom_components directory.

## Configuration
Add following configuration to Home Assistant configuration.yaml

    climate:
    - platform: heatmiser_wifi
        host:          <mandatory - hostname or ip address>
        port:          <optional  - default 8068>
        pin:           <optional  - default 0>
        friendly_name: <optional  - default 'Heatmiser MODELNO'>
  
## See also
* [Heatmiser Wifi](https://github.com/midstar/heatmiser_wifi) the library used for communication with Heatmiser WiFi
* [daveNewcastle/Heatmiser-WIFI](https://github.com/daveNewcastle/Heatmiser-WIFI) Heatmiser Wifi Home Assistant Component for older versions of Home Assistant. It has not been updated for many years.
* [Home Assistant Heatmiser Core component](https://www.home-assistant.io/integrations/heatmiser/) for non WiFi versions of Heatmister Thermostats.
 
### Author and license
This component is written by Joel Midstjärna and is licensed under the MIT License.
