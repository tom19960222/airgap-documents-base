---
collection: kernel
version: "6.8"
title: "Kernel driver sht4x"
source_url: https://www.kernel.org/doc/html/v6.8/hwmon/sht4x.html
fetched_at: 2026-08-21T03:53:37+00:00
---
# Kernel driver sht4x

Supported Chips:

> - Sensirion SHT4X
>
>   Prefix: 'sht4x'
>
>   Addresses scanned: None
>
>   Datasheet:
>
>   > English: <https://www.sensirion.com/fileadmin/user_upload/customers/sensirion/Dokumente/2_Humidity_Sensors/Datasheets/Sensirion_Humidity_Sensors_SHT4x_Datasheet.pdf>

Author: Navin Sankar Velliangiri <[navin@linumiz.com](mailto:navin%40linumiz.com)>

## Description

This driver implements support for the Sensirion SHT4x chip, a humidity
and temperature sensor. Temperature is measured in degree celsius, relative
humidity is expressed as a percentage. In sysfs interface, all values are
scaled by 1000, i.e. the value for 31.5 degrees celsius is 31500.

## Usage Notes

The device communicates with the I2C protocol. Sensors can have the I2C
address 0x44. See [How to instantiate I2C devices](../i2c/instantiating-devices.md) for methods
to instantiate the device.

## Sysfs entries

|  |  |
| --- | --- |
| temp1_input | Measured temperature in millidegrees Celsius |
| humidity1_input | Measured humidity in %H |
| update_interval | The minimum interval for polling the sensor, in milliseconds. Writable. Must be at least 2000. |
