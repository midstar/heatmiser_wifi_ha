# Heatmiser WiFi Home Assistant Component

## Overview
A [Heatmiser](http://www.heatmiser.com/) WiFi Thermostat Home Assistant plugin.

Supports:

* Read current air temperature
* Read/set temperature setting (i.e. wanted temperature)
* Read/set on/off of the Thermostat

Supported Heatmiser Thermostats are DT, DT-E, PRT and PRT-E.

## Installation
Copy the heatmiser_wifi_ha directory and its contents to the Home Assistant custom_components directory.

Add following configuration to Home Assistant configuration.yaml

    climate:
    - platform: heatmiser_wifi
        host:          <mandatory - hostname or ip address>
        port:          <optional  - default 8068>
        pin:           <optional  - default 0>
        friendly_name: <optional  - default 'Heatmiser MODELNO'>
  
## See also
* [Heatmiser Wifi](https://github.com/midstar/heatmiser_wifi) the library used for communication with Heatmiser Wifi
* [daveNewcastle/Heatmiser-WIFI](https://github.com/daveNewcastle/Heatmiser-WIFI) Heatmiser Wifi Home Assistant Component for older versions of Home Assistant. It has not been updated for 3 years.
 
### Author and license
This application is written by Joel Midstjärna and is licensed under the MIT License.
