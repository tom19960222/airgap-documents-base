---
collection: kernel
version: "6.8"
title: "ABI obsolete symbols"
source_url: https://www.kernel.org/doc/html/v6.8/admin-guide/abi-obsolete.html
fetched_at: 2026-08-21T03:54:41+00:00
---
# ABI obsolete symbols

Documents interfaces that are still remaining in the kernel, but are
marked to be removed at some later point in time.

The description of the interface will document the reason why it is
obsolete and when it can be expected to be removed.

## Symbols under /proc/i8k

|  |
| --- |
| **/proc/i8k** |

Defined on file [procfs-i8k](abi-obsolete.md#abi-file-obsolete-procfs-i8k)

Legacy interface for getting/setting sensor information like
fan speed, temperature, serial number, hotkey status etc
on Dell Laptops.
Since the driver is now using the standard hwmon sysfs interface,
the procfs interface is deprecated.

Users:
<https://github.com/vitorafsr/i8kutils>

## Symbols under /sys

|  |
| --- |
| **/sys/.../iio:deviceX/scan_elements/in_accel_type** |
| **/sys/.../iio:deviceX/scan_elements/in_anglvel_type** |
| **/sys/.../iio:deviceX/scan_elements/in_magn_type** |
| **/sys/.../iio:deviceX/scan_elements/in_incli_type** |
| **/sys/.../iio:deviceX/scan_elements/in_voltageY_type** |
| **/sys/.../iio:deviceX/scan_elements/in_voltage_type** |
| **/sys/.../iio:deviceX/scan_elements/in_voltageY_supply_type** |
| **/sys/.../iio:deviceX/scan_elements/in_voltageY_i_type** |
| **/sys/.../iio:deviceX/scan_elements/in_voltageY_q_type** |
| **/sys/.../iio:deviceX/scan_elements/in_voltage_i_type** |
| **/sys/.../iio:deviceX/scan_elements/in_voltage_q_type** |
| **/sys/.../iio:deviceX/scan_elements/in_timestamp_type** |
| **/sys/.../iio:deviceX/scan_elements/in_pressureY_type** |
| **/sys/.../iio:deviceX/scan_elements/in_pressure_type** |
| **/sys/.../iio:deviceX/scan_elements/in_rot_quaternion_type** |
| **/sys/.../iio:deviceX/scan_elements/in_proximity_type** |

Defined on file [sysfs-bus-iio](abi-obsolete.md#abi-file-obsolete-sysfs-bus-iio)

Description of the scan element data storage within the buffer
and hence the form in which it is read from user-space.
Form is [be|le]:[s|u]bits/storagebits[>>shift].
be or le specifies big or little endian. s or u specifies if
signed (2's complement) or unsigned. bits is the number of bits
of data and storagebits is the space (after padding) that it
occupies in the buffer. shift if specified, is the shift that
needs to be applied prior to masking out unused bits. Some
devices put their data in the middle of the transferred elements
with additional information on both sides. Note that some
devices will have additional information in the unused bits
so to get a clean value, the bits value must be used to mask
the buffer output value appropriately. The storagebits value
also specifies the data alignment. So s48/64>>2 will be a
signed 48 bit integer stored in a 64 bit location aligned to
a 64 bit boundary. To obtain the clean value, shift right 2
and apply a mask to zero the top 16 bits of the result.
For other storage combinations this attribute will be extended
appropriately.

Since kernel 5.11 the scan_elements attributes are merged into
the bufferY directory, to be configurable per buffer.

|  |
| --- |
| **/sys/.../iio:deviceX/scan_elements/in_accel_x_en** |
| **/sys/.../iio:deviceX/scan_elements/in_accel_y_en** |
| **/sys/.../iio:deviceX/scan_elements/in_accel_z_en** |
| **/sys/.../iio:deviceX/scan_elements/in_anglvel_x_en** |
| **/sys/.../iio:deviceX/scan_elements/in_anglvel_y_en** |
| **/sys/.../iio:deviceX/scan_elements/in_anglvel_z_en** |
| **/sys/.../iio:deviceX/scan_elements/in_magn_x_en** |
| **/sys/.../iio:deviceX/scan_elements/in_magn_y_en** |
| **/sys/.../iio:deviceX/scan_elements/in_magn_z_en** |
| **/sys/.../iio:deviceX/scan_elements/in_rot_from_north_magnetic_en** |
| **/sys/.../iio:deviceX/scan_elements/in_rot_from_north_true_en** |
| **/sys/.../iio:deviceX/scan_elements/in_rot_from_north_magnetic_tilt_comp_en** |
| **/sys/.../iio:deviceX/scan_elements/in_rot_from_north_true_tilt_comp_en** |
| **/sys/.../iio:deviceX/scan_elements/in_timestamp_en** |
| **/sys/.../iio:deviceX/scan_elements/in_voltageY_supply_en** |
| **/sys/.../iio:deviceX/scan_elements/in_voltageY_en** |
| **/sys/.../iio:deviceX/scan_elements/in_voltageY-voltageZ_en** |
| **/sys/.../iio:deviceX/scan_elements/in_voltageY_i_en** |
| **/sys/.../iio:deviceX/scan_elements/in_voltageY_q_en** |
| **/sys/.../iio:deviceX/scan_elements/in_voltage_i_en** |
| **/sys/.../iio:deviceX/scan_elements/in_voltage_q_en** |
| **/sys/.../iio:deviceX/scan_elements/in_incli_x_en** |
| **/sys/.../iio:deviceX/scan_elements/in_incli_y_en** |
| **/sys/.../iio:deviceX/scan_elements/in_pressureY_en** |
| **/sys/.../iio:deviceX/scan_elements/in_pressure_en** |
| **/sys/.../iio:deviceX/scan_elements/in_rot_quaternion_en** |
| **/sys/.../iio:deviceX/scan_elements/in_proximity_en** |

Defined on file [sysfs-bus-iio](abi-obsolete.md#abi-file-obsolete-sysfs-bus-iio)

Scan element control for triggered data capture.

Since kernel 5.11 the scan_elements attributes are merged into
the bufferY directory, to be configurable per buffer.

|  |
| --- |
| **/sys/.../iio:deviceX/scan_elements/in_voltageY_index** |
| **/sys/.../iio:deviceX/scan_elements/in_voltageY_supply_index** |
| **/sys/.../iio:deviceX/scan_elements/in_voltageY_i_index** |
| **/sys/.../iio:deviceX/scan_elements/in_voltageY_q_index** |
| **/sys/.../iio:deviceX/scan_elements/in_voltage_i_index** |
| **/sys/.../iio:deviceX/scan_elements/in_voltage_q_index** |
| **/sys/.../iio:deviceX/scan_elements/in_accel_x_index** |
| **/sys/.../iio:deviceX/scan_elements/in_accel_y_index** |
| **/sys/.../iio:deviceX/scan_elements/in_accel_z_index** |
| **/sys/.../iio:deviceX/scan_elements/in_anglvel_x_index** |
| **/sys/.../iio:deviceX/scan_elements/in_anglvel_y_index** |
| **/sys/.../iio:deviceX/scan_elements/in_anglvel_z_index** |
| **/sys/.../iio:deviceX/scan_elements/in_magn_x_index** |
| **/sys/.../iio:deviceX/scan_elements/in_magn_y_index** |
| **/sys/.../iio:deviceX/scan_elements/in_magn_z_index** |
| **/sys/.../iio:deviceX/scan_elements/in_rot_from_north_magnetic_index** |
| **/sys/.../iio:deviceX/scan_elements/in_rot_from_north_true_index** |
| **/sys/.../iio:deviceX/scan_elements/in_rot_from_north_magnetic_tilt_comp_index** |
| **/sys/.../iio:deviceX/scan_elements/in_rot_from_north_true_tilt_comp_index** |
| **/sys/.../iio:deviceX/scan_elements/in_incli_x_index** |
| **/sys/.../iio:deviceX/scan_elements/in_incli_y_index** |
| **/sys/.../iio:deviceX/scan_elements/in_timestamp_index** |
| **/sys/.../iio:deviceX/scan_elements/in_pressureY_index** |
| **/sys/.../iio:deviceX/scan_elements/in_pressure_index** |
| **/sys/.../iio:deviceX/scan_elements/in_rot_quaternion_index** |
| **/sys/.../iio:deviceX/scan_elements/in_proximity_index** |

Defined on file [sysfs-bus-iio](abi-obsolete.md#abi-file-obsolete-sysfs-bus-iio)

A single positive integer specifying the position of this
scan element in the buffer. Note these are not dependent on
what is enabled and may not be contiguous. Thus for user-space
to establish the full layout these must be used in conjunction
with all _en attributes to establish which channels are present,
and the relevant _type attributes to establish the data storage
format.

Since kernel 5.11 the scan_elements attributes are merged into
the bufferY directory, to be configurable per buffer.

## Symbols under /sys/bus

|  |
| --- |
| **/sys/bus/iio/devices/iio:deviceX/buffer/data_available** |

Defined on file [sysfs-bus-iio](abi-obsolete.md#abi-file-obsolete-sysfs-bus-iio)

A read-only value indicating the bytes of data available in the
buffer. In the case of an output buffer, this indicates the
amount of empty space available to write data to. In the case of
an input buffer, this indicates the amount of data available for
reading.

Since Kernel 5.11, multiple buffers are supported.
so, it is better to use, instead:

> /sys/bus/iio/devices/iio:deviceX/bufferY/data_available

|  |
| --- |
| **/sys/bus/iio/devices/iio:deviceX/buffer/enable** |

Defined on file [sysfs-bus-iio](abi-obsolete.md#abi-file-obsolete-sysfs-bus-iio)

Actually start the buffer capture up. Will start trigger
if first device and appropriate.

Since Kernel 5.11, multiple buffers are supported.
so, it is better to use, instead:

> /sys/bus/iio/devices/iio:deviceX/bufferY/enable

|  |
| --- |
| **/sys/bus/iio/devices/iio:deviceX/buffer/length** |

Defined on file [sysfs-bus-iio](abi-obsolete.md#abi-file-obsolete-sysfs-bus-iio)

Number of scans contained by the buffer.

Since Kernel 5.11, multiple buffers are supported.
so, it is better to use, instead:

> /sys/bus/iio/devices/iio:deviceX/bufferY/length

|  |
| --- |
| **/sys/bus/iio/devices/iio:deviceX/buffer/watermark** |

Defined on file [sysfs-bus-iio](abi-obsolete.md#abi-file-obsolete-sysfs-bus-iio)

A single positive integer specifying the maximum number of scan
elements to wait for.

Poll will block until the watermark is reached.

Blocking read will wait until the minimum between the requested
read amount or the low water mark is available.

Non-blocking read will retrieve the available samples from the
buffer even if there are less samples then watermark level. This
allows the application to block on poll with a timeout and read
the available samples after the timeout expires and thus have a
maximum delay guarantee.

Since Kernel 5.11, multiple buffers are supported.
so, it is better to use, instead:

> /sys/bus/iio/devices/iio:deviceX/bufferY/watermark

|  |
| --- |
| **/sys/bus/iio/devices/iio:deviceX/scan_elements** |

Defined on file [sysfs-bus-iio](abi-obsolete.md#abi-file-obsolete-sysfs-bus-iio)

Directory containing interfaces for elements that will be
captured for a single triggered sample set in the buffer.

Since kernel 5.11 the scan_elements attributes are merged into
the bufferY directory, to be configurable per buffer.

|  |
| --- |
| **/sys/bus/platform/devices/INT34D2:00/northpeak** |

Defined on file [sysfs-driver-intel_pmc_bxt](abi-obsolete.md#abi-file-obsolete-sysfs-driver-intel-pmc-bxt)

This interface allows userspace to enable and disable
Northpeak through the PMC/SCU.

Format: %u.

|  |
| --- |
| **/sys/bus/platform/devices/INT34D2:00/simplecmd** |

Defined on file [sysfs-driver-intel_pmc_bxt](abi-obsolete.md#abi-file-obsolete-sysfs-driver-intel-pmc-bxt)

This interface allows userspace to send an arbitrary
IPC command to the PMC/SCU.

Format: %d %d where first number is command and
second number is subcommand.

|  |
| --- |
| **/sys/bus/usb/devices/.../power/level** |

Defined on file [sysfs-bus-usb](abi-obsolete.md#abi-file-obsolete-sysfs-bus-usb)

Each USB device directory will contain a file named
power/level. This file holds a power-level setting for
the device, either "on" or "auto".

"on" means that the device is not allowed to autosuspend,
although normal suspends for system sleep will still
be honored. "auto" means the device will autosuspend
and autoresume in the usual manner, according to the
capabilities of its driver.

During normal use, devices should be left in the "auto"
level. The "on" level is meant for administrative uses.
If you want to suspend a device immediately but leave it
free to wake up in response to I/O requests, you should
write "0" to power/autosuspend.

Device not capable of proper suspend and resume should be
left in the "on" level. Although the USB spec requires
devices to support suspend/resume, many of them do not.
In fact so many don't that by default, the USB core
initializes all non-hub devices in the "on" level. Some
drivers may change this setting when they are bound.

This file is deprecated and will be removed after 2010.
Use the power/control file instead; it does exactly the
same thing.

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/arvo/roccatarvo<minor>/actual_profile** |

Defined on file [sysfs-driver-hid-roccat-arvo](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-arvo)

The integer value of this attribute ranges from 1-5.
When read, this attribute returns the number of the actual
profile which is also the profile that's active on device startup.
When written this attribute activates the selected profile
immediately.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/arvo/roccatarvo<minor>/button** |

Defined on file [sysfs-driver-hid-roccat-arvo](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-arvo)

The keyboard can store short macros with consist of 1 button with
several modifier keys internally.
When written, this file lets one set the sequence for a specific
button for a specific profile. Button and profile numbers are
included in written data. The data has to be 24 bytes long.
This file is writeonly.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/arvo/roccatarvo<minor>/info** |

Defined on file [sysfs-driver-hid-roccat-arvo](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-arvo)

When read, this file returns some info about the device like the
installed firmware version.
The size of the data is 8 bytes in size.
This file is readonly.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/arvo/roccatarvo<minor>/key_mask** |

Defined on file [sysfs-driver-hid-roccat-arvo](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-arvo)

The keyboard lets the user deactivate 5 certain keys like the
windows and application keys, to protect the user from the outcome
of accidentally pressing them.
The integer value of this attribute has bits 0-4 set depending
on the state of the corresponding key.
When read, this file returns the current state of the buttons.
When written, the given buttons are activated/deactivated
immediately.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/arvo/roccatarvo<minor>/mode_key** |

Defined on file [sysfs-driver-hid-roccat-arvo](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-arvo)

The keyboard has a condensed layout without num-lock key.
Instead it uses a mode-key which activates a gaming mode where
the assignment of the number block changes.
The integer value of this attribute ranges from 0 (OFF) to 1 (ON).
When read, this file returns the actual state of the key.
When written, the key is activated/deactivated immediately.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/isku/roccatisku<minor>/actual_profile** |

Defined on file [sysfs-driver-hid-roccat-isku](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-isku)

The integer value of this attribute ranges from 0-4.
When read, this attribute returns the number of the actual
profile. This value is persistent, so its equivalent to the
profile that's active when the device is powered on next time.
When written, this file sets the number of the startup profile
and the device activates this profile immediately.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/isku/roccatisku<minor>/control** |

Defined on file [sysfs-driver-hid-roccat-isku](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-isku)

When written, this file lets one select which data from which
profile will be read next. The data has to be 3 bytes long.
This file is writeonly.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/isku/roccatisku<minor>/info** |

Defined on file [sysfs-driver-hid-roccat-isku](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-isku)

When read, this file returns general data like firmware version.
The data is 6 bytes long.
This file is readonly.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/isku/roccatisku<minor>/key_mask** |

Defined on file [sysfs-driver-hid-roccat-isku](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-isku)

When written, this file lets one deactivate certain keys like
windows and application keys, to prevent accidental presses.
Profile number for which this settings occur is included in
written data. The data has to be 6 bytes long.
Before reading this file, control has to be written to select
which profile to read.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/isku/roccatisku<minor>/keys_capslock** |

Defined on file [sysfs-driver-hid-roccat-isku](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-isku)

When written, this file lets one set the function of the
capslock key for a specific profile. Profile number is included
in written data. The data has to be 6 bytes long.
Before reading this file, control has to be written to select
which profile to read.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/isku/roccatisku<minor>/keys_easyzone** |

Defined on file [sysfs-driver-hid-roccat-isku](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-isku)

When written, this file lets one set the function of the
easyzone keys for a specific profile. Profile number is included
in written data. The data has to be 65 bytes long.
Before reading this file, control has to be written to select
which profile to read.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/isku/roccatisku<minor>/keys_function** |

Defined on file [sysfs-driver-hid-roccat-isku](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-isku)

When written, this file lets one set the function of the
function keys for a specific profile. Profile number is included
in written data. The data has to be 41 bytes long.
Before reading this file, control has to be written to select
which profile to read.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/isku/roccatisku<minor>/keys_macro** |

Defined on file [sysfs-driver-hid-roccat-isku](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-isku)

When written, this file lets one set the function of the macro
keys for a specific profile. Profile number is included in
written data. The data has to be 35 bytes long.
Before reading this file, control has to be written to select
which profile to read.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/isku/roccatisku<minor>/keys_media** |

Defined on file [sysfs-driver-hid-roccat-isku](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-isku)

When written, this file lets one set the function of the media
keys for a specific profile. Profile number is included in
written data. The data has to be 29 bytes long.
Before reading this file, control has to be written to select
which profile to read.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/isku/roccatisku<minor>/keys_thumbster** |

Defined on file [sysfs-driver-hid-roccat-isku](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-isku)

When written, this file lets one set the function of the
thumbster keys for a specific profile. Profile number is included
in written data. The data has to be 23 bytes long.
Before reading this file, control has to be written to select
which profile to read.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/isku/roccatisku<minor>/last_set** |

Defined on file [sysfs-driver-hid-roccat-isku](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-isku)

When written, this file lets one set the time in secs since
epoch in which the last configuration took place.
The data has to be 20 bytes long.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/isku/roccatisku<minor>/light** |

Defined on file [sysfs-driver-hid-roccat-isku](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-isku)

When written, this file lets one set the backlight intensity for
a specific profile. Profile number is included in written data.
The data has to be 10 bytes long for Isku, IskuFX needs 16 bytes
of data.
Before reading this file, control has to be written to select
which profile to read.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/isku/roccatisku<minor>/macro** |

Defined on file [sysfs-driver-hid-roccat-isku](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-isku)

When written, this file lets one store macros with max 500
keystrokes for a specific button for a specific profile.
Button and profile numbers are included in written data.
The data has to be 2083 bytes long.
Before reading this file, control has to be written to select
which profile and key to read.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/isku/roccatisku<minor>/reset** |

Defined on file [sysfs-driver-hid-roccat-isku](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-isku)

When written, this file lets one reset the device.
The data has to be 3 bytes long.
This file is writeonly.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/isku/roccatisku<minor>/talk** |

Defined on file [sysfs-driver-hid-roccat-isku](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-isku)

When written, this file lets one trigger easyshift functionality
from the host.
The data has to be 16 bytes long.
This file is writeonly.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/isku/roccatisku<minor>/talkfx** |

Defined on file [sysfs-driver-hid-roccat-isku](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-isku)

When written, this file lets one trigger temporary color schemes
from the host.
The data has to be 16 bytes long.
This file is writeonly.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/koneplus/roccatkoneplus<minor>/actual_profile** |

Defined on file [sysfs-driver-hid-roccat-koneplus](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-koneplus)

The integer value of this attribute ranges from 0-4.
When read, this attribute returns the number of the actual
profile. This value is persistent, so its equivalent to the
profile that's active when the mouse is powered on next time.
When written, this file sets the number of the startup profile
and the mouse activates this profile immediately.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/koneplus/roccatkoneplus<minor>/firmware_version** |

Defined on file [sysfs-driver-hid-roccat-koneplus](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-koneplus)

When read, this file returns the raw integer version number of the
firmware reported by the mouse. Using the integer value eases
further usage in other programs. To receive the real version
number the decimal point has to be shifted 2 positions to the
left. E.g. a returned value of 121 means 1.21
This file is readonly.
Please read binary attribute info which contains firmware version.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/koneplus/roccatkoneplus<minor>/info** |

Defined on file [sysfs-driver-hid-roccat-koneplus](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-koneplus)

When read, this file returns general data like firmware version.
When written, the device can be reset.
The data is 8 bytes long.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/koneplus/roccatkoneplus<minor>/macro** |

Defined on file [sysfs-driver-hid-roccat-koneplus](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-koneplus)

The mouse can store a macro with max 500 key/button strokes
internally.
When written, this file lets one set the sequence for a specific
button for a specific profile. Button and profile numbers are
included in written data. The data has to be 2082 bytes long.
This file is writeonly.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/koneplus/roccatkoneplus<minor>/profile[1-5]_buttons** |

Defined on file [sysfs-driver-hid-roccat-koneplus](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-koneplus)

The mouse can store 5 profiles which can be switched by the
press of a button. A profile is split in settings and buttons.
profile_buttons holds information about button layout.
When read, these files return the respective profile buttons.
The returned data is 77 bytes in size.
This file is readonly.
Write control to select profile and read profile_buttons instead.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/koneplus/roccatkoneplus<minor>/profile[1-5]_settings** |

Defined on file [sysfs-driver-hid-roccat-koneplus](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-koneplus)

The mouse can store 5 profiles which can be switched by the
press of a button. A profile is split in settings and buttons.
profile_settings holds information like resolution, sensitivity
and light effects.
When read, these files return the respective profile settings.
The returned data is 43 bytes in size.
This file is readonly.
Write control to select profile and read profile_settings instead.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/koneplus/roccatkoneplus<minor>/profile_buttons** |

Defined on file [sysfs-driver-hid-roccat-koneplus](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-koneplus)

The mouse can store 5 profiles which can be switched by the
press of a button. A profile is split in settings and buttons.
profile_buttons holds information about button layout.
When written, this file lets one write the respective profile
buttons back to the mouse. The data has to be 77 bytes long.
The mouse will reject invalid data.
Which profile to write is determined by the profile number
contained in the data.
Before reading this file, control has to be written to select
which profile to read.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/koneplus/roccatkoneplus<minor>/profile_settings** |

Defined on file [sysfs-driver-hid-roccat-koneplus](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-koneplus)

The mouse can store 5 profiles which can be switched by the
press of a button. A profile is split in settings and buttons.
profile_settings holds information like resolution, sensitivity
and light effects.
When written, this file lets one write the respective profile
settings back to the mouse. The data has to be 43 bytes long.
The mouse will reject invalid data.
Which profile to write is determined by the profile number
contained in the data.
Before reading this file, control has to be written to select
which profile to read.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/koneplus/roccatkoneplus<minor>/sensor** |

Defined on file [sysfs-driver-hid-roccat-koneplus](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-koneplus)

The mouse has a tracking- and a distance-control-unit. These
can be activated/deactivated and the lift-off distance can be
set. The data has to be 6 bytes long.
This file is writeonly.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/koneplus/roccatkoneplus<minor>/startup_profile** |

Defined on file [sysfs-driver-hid-roccat-koneplus](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-koneplus)

The integer value of this attribute ranges from 0-4.
When read, this attribute returns the number of the actual
profile. This value is persistent, so its equivalent to the
profile that's active when the mouse is powered on next time.
When written, this file sets the number of the startup profile
and the mouse activates this profile immediately.
Please use actual_profile, it does the same thing.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/koneplus/roccatkoneplus<minor>/talk** |

Defined on file [sysfs-driver-hid-roccat-koneplus](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-koneplus)

Used to active some easy\* functions of the mouse from outside.
The data has to be 16 bytes long.
This file is writeonly.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/koneplus/roccatkoneplus<minor>/tcu** |

Defined on file [sysfs-driver-hid-roccat-koneplus](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-koneplus)

When written a calibration process for the tracking control unit
can be initiated/cancelled. Also lets one read/write sensor
registers.
The data has to be 4 bytes long.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/koneplus/roccatkoneplus<minor>/tcu_image** |

Defined on file [sysfs-driver-hid-roccat-koneplus](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-koneplus)

When read the mouse returns a 30x30 pixel image of the
sampled underground. This works only in the course of a
calibration process initiated with tcu.
The returned data is 1028 bytes in size.
This file is readonly.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/konepure/roccatkonepure<minor>/actual_profile** |

Defined on file [sysfs-driver-hid-roccat-konepure](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-konepure)

The mouse can store 5 profiles which can be switched by the
press of a button. actual_profile holds number of actual profile.
This value is persistent, so its value determines the profile
that's active when the mouse is powered on next time.
When written, the mouse activates the set profile immediately.
The data has to be 3 bytes long.
The mouse will reject invalid data.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/konepure/roccatkonepure<minor>/control** |

Defined on file [sysfs-driver-hid-roccat-konepure](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-konepure)

When written, this file lets one select which data from which
profile will be read next. The data has to be 3 bytes long.
This file is writeonly.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/konepure/roccatkonepure<minor>/info** |

Defined on file [sysfs-driver-hid-roccat-konepure](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-konepure)

When read, this file returns general data like firmware version.
When written, the device can be reset.
The data is 6 bytes long.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/konepure/roccatkonepure<minor>/macro** |

Defined on file [sysfs-driver-hid-roccat-konepure](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-konepure)

The mouse can store a macro with max 500 key/button strokes
internally.
When written, this file lets one set the sequence for a specific
button for a specific profile. Button and profile numbers are
included in written data. The data has to be 2082 bytes long.
This file is writeonly.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/konepure/roccatkonepure<minor>/profile_buttons** |

Defined on file [sysfs-driver-hid-roccat-konepure](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-konepure)

The mouse can store 5 profiles which can be switched by the
press of a button. A profile is split in settings and buttons.
profile_buttons holds information about button layout.
When written, this file lets one write the respective profile
buttons back to the mouse. The data has to be 59 bytes long.
The mouse will reject invalid data.
Which profile to write is determined by the profile number
contained in the data.
Before reading this file, control has to be written to select
which profile to read.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/konepure/roccatkonepure<minor>/profile_settings** |

Defined on file [sysfs-driver-hid-roccat-konepure](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-konepure)

The mouse can store 5 profiles which can be switched by the
press of a button. A profile is split in settings and buttons.
profile_settings holds information like resolution, sensitivity
and light effects.
When written, this file lets one write the respective profile
settings back to the mouse. The data has to be 31 bytes long.
The mouse will reject invalid data.
Which profile to write is determined by the profile number
contained in the data.
Before reading this file, control has to be written to select
which profile to read.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/konepure/roccatkonepure<minor>/sensor** |

Defined on file [sysfs-driver-hid-roccat-konepure](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-konepure)

The mouse has a tracking- and a distance-control-unit. These
can be activated/deactivated and the lift-off distance can be
set. The data has to be 6 bytes long.
This file is writeonly.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/konepure/roccatkonepure<minor>/talk** |

Defined on file [sysfs-driver-hid-roccat-konepure](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-konepure)

Used to active some easy\* functions of the mouse from outside.
The data has to be 16 bytes long.
This file is writeonly.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/konepure/roccatkonepure<minor>/tcu** |

Defined on file [sysfs-driver-hid-roccat-konepure](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-konepure)

When written a calibration process for the tracking control unit
can be initiated/cancelled. Also lets one read/write sensor
registers.
The data has to be 4 bytes long.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/konepure/roccatkonepure<minor>/tcu_image** |

Defined on file [sysfs-driver-hid-roccat-konepure](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-konepure)

When read the mouse returns a 30x30 pixel image of the
sampled underground. This works only in the course of a
calibration process initiated with tcu.
The returned data is 1028 bytes in size.
This file is readonly.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/kovaplus/roccatkovaplus<minor>/actual_cpi** |

Defined on file [sysfs-driver-hid-roccat-kovaplus](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-kovaplus)

The integer value of this attribute ranges from 1-4.
When read, this attribute returns the number of the active
cpi level.
This file is readonly.
Has never been used. If bookkeeping is done, it's done in userland tools.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/kovaplus/roccatkovaplus<minor>/actual_profile** |

Defined on file [sysfs-driver-hid-roccat-kovaplus](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-kovaplus)

The integer value of this attribute ranges from 0-4.
When read, this attribute returns the number of the active
profile.
When written, the mouse activates this profile immediately.
The profile that's active when powered down is the same that's
active when the mouse is powered on.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/kovaplus/roccatkovaplus<minor>/actual_sensitivity_x** |

Defined on file [sysfs-driver-hid-roccat-kovaplus](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-kovaplus)

The integer value of this attribute ranges from 1-10.
When read, this attribute returns the number of the actual
sensitivity in x direction.
This file is readonly.
Has never been used. If bookkeeping is done, it's done in userland tools.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/kovaplus/roccatkovaplus<minor>/actual_sensitivity_y** |

Defined on file [sysfs-driver-hid-roccat-kovaplus](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-kovaplus)

The integer value of this attribute ranges from 1-10.
When read, this attribute returns the number of the actual
sensitivity in y direction.
This file is readonly.
Has never been used. If bookkeeping is done, it's done in userland tools.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/kovaplus/roccatkovaplus<minor>/firmware_version** |

Defined on file [sysfs-driver-hid-roccat-kovaplus](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-kovaplus)

When read, this file returns the raw integer version number of the
firmware reported by the mouse. Using the integer value eases
further usage in other programs. To receive the real version
number the decimal point has to be shifted 2 positions to the
left. E.g. a returned value of 121 means 1.21
This file is readonly.
Obsoleted by binary sysfs attribute "info".

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/kovaplus/roccatkovaplus<minor>/info** |

Defined on file [sysfs-driver-hid-roccat-kovaplus](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-kovaplus)

When read, this file returns general data like firmware version.
When written, the device can be reset.
The data is 6 bytes long.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/kovaplus/roccatkovaplus<minor>/profile[1-5]_buttons** |

Defined on file [sysfs-driver-hid-roccat-kovaplus](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-kovaplus)

The mouse can store 5 profiles which can be switched by the
press of a button. A profile is split in settings and buttons.
profile_buttons holds information about button layout.
When read, these files return the respective profile buttons.
The returned data is 23 bytes in size.
This file is readonly.
Write control to select profile and read profile_buttons instead.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/kovaplus/roccatkovaplus<minor>/profile[1-5]_settings** |

Defined on file [sysfs-driver-hid-roccat-kovaplus](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-kovaplus)

The mouse can store 5 profiles which can be switched by the
press of a button. A profile is split in settings and buttons.
profile_settings holds information like resolution, sensitivity
and light effects.
When read, these files return the respective profile settings.
The returned data is 16 bytes in size.
This file is readonly.
Write control to select profile and read profile_settings instead.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/kovaplus/roccatkovaplus<minor>/profile_buttons** |

Defined on file [sysfs-driver-hid-roccat-kovaplus](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-kovaplus)

The mouse can store 5 profiles which can be switched by the
press of a button. A profile is split in settings and buttons.
profile_buttons holds information about button layout.
When written, this file lets one write the respective profile
buttons back to the mouse. The data has to be 23 bytes long.
The mouse will reject invalid data.
Which profile to write is determined by the profile number
contained in the data.
Before reading this file, control has to be written to select
which profile to read.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/kovaplus/roccatkovaplus<minor>/profile_settings** |

Defined on file [sysfs-driver-hid-roccat-kovaplus](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-kovaplus)

The mouse can store 5 profiles which can be switched by the
press of a button. A profile is split in settings and buttons.
profile_settings holds information like resolution, sensitivity
and light effects.
When written, this file lets one write the respective profile
settings back to the mouse. The data has to be 16 bytes long.
The mouse will reject invalid data.
Which profile to write is determined by the profile number
contained in the data.
Before reading this file, control has to be written to select
which profile to read.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/pyra/roccatpyra<minor>/actual_cpi** |

Defined on file [sysfs-driver-hid-roccat-pyra](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-pyra)

It is possible to switch the cpi setting of the mouse with the
press of a button.
When read, this file returns the raw number of the actual cpi
setting reported by the mouse. This number has to be further
processed to receive the real dpi value:

| VALUE | DPI |
| --- | --- |
| 1 | 400 |
| 2 | 800 |
| 4 | 1600 |

This file is readonly.
Has never been used. If bookkeeping is done, it's done in userland tools.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/pyra/roccatpyra<minor>/actual_profile** |

Defined on file [sysfs-driver-hid-roccat-pyra](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-pyra)

When read, this file returns the number of the actual profile in
range 0-4.
This file is readonly.
Please use binary attribute "settings" which provides this information.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/pyra/roccatpyra<minor>/firmware_version** |

Defined on file [sysfs-driver-hid-roccat-pyra](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-pyra)

When read, this file returns the raw integer version number of the
firmware reported by the mouse. Using the integer value eases
further usage in other programs. To receive the real version
number the decimal point has to be shifted 2 positions to the
left. E.g. a returned value of 138 means 1.38
This file is readonly.
Please use binary attribute "info" which provides this information.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/pyra/roccatpyra<minor>/info** |

Defined on file [sysfs-driver-hid-roccat-pyra](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-pyra)

When read, this file returns general data like firmware version.
When written, the device can be reset.
The data is 6 bytes long.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/pyra/roccatpyra<minor>/profile[1-5]_buttons** |

Defined on file [sysfs-driver-hid-roccat-pyra](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-pyra)

The mouse can store 5 profiles which can be switched by the
press of a button. A profile is split in settings and buttons.
profile_buttons holds information about button layout.
When read, these files return the respective profile buttons.
The returned data is 19 bytes in size.
This file is readonly.
Write control to select profile and read profile_buttons instead.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/pyra/roccatpyra<minor>/profile[1-5]_settings** |

Defined on file [sysfs-driver-hid-roccat-pyra](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-pyra)

The mouse can store 5 profiles which can be switched by the
press of a button. A profile is split in settings and buttons.
profile_settings holds information like resolution, sensitivity
and light effects.
When read, these files return the respective profile settings.
The returned data is 13 bytes in size.
This file is readonly.
Write control to select profile and read profile_settings instead.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/pyra/roccatpyra<minor>/profile_buttons** |

Defined on file [sysfs-driver-hid-roccat-pyra](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-pyra)

The mouse can store 5 profiles which can be switched by the
press of a button. A profile is split in settings and buttons.
profile_buttons holds information about button layout.
When written, this file lets one write the respective profile
buttons back to the mouse. The data has to be 19 bytes long.
The mouse will reject invalid data.
Which profile to write is determined by the profile number
contained in the data.
Before reading this file, control has to be written to select
which profile to read.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/pyra/roccatpyra<minor>/profile_settings** |

Defined on file [sysfs-driver-hid-roccat-pyra](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-pyra)

The mouse can store 5 profiles which can be switched by the
press of a button. A profile is split in settings and buttons.
profile_settings holds information like resolution, sensitivity
and light effects.
When written, this file lets one write the respective profile
settings back to the mouse. The data has to be 13 bytes long.
The mouse will reject invalid data.
Which profile to write is determined by the profile number
contained in the data.
Before reading this file, control has to be written to select
which profile to read.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/pyra/roccatpyra<minor>/settings** |

Defined on file [sysfs-driver-hid-roccat-pyra](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-pyra)

When read, this file returns the settings stored in the mouse.
The size of the data is 3 bytes and holds information on the
startup_profile.
When written, this file lets write settings back to the mouse.
The data has to be 3 bytes long. The mouse will reject invalid
data.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/pyra/roccatpyra<minor>/startup_profile** |

Defined on file [sysfs-driver-hid-roccat-pyra](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-pyra)

The integer value of this attribute ranges from 0-4.
When read, this attribute returns the number of the profile
that's active when the mouse is powered on.
This file is readonly.
Please use binary attribute "settings" which provides this information.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/ryos/roccatryos<minor>/control** |

Defined on file [sysfs-driver-hid-roccat-ryos](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-ryos)

When written, this file lets one select which data from which
profile will be read next. The data has to be 3 bytes long.
This file is writeonly.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/ryos/roccatryos<minor>/custom_lights** |

Defined on file [sysfs-driver-hid-roccat-ryos](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-ryos)

When written, this file lets one set the actual per-key lighting.
This attribute is only valid for the pro variant.
The data has to be 20 bytes long.
This file is writeonly.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/ryos/roccatryos<minor>/info** |

Defined on file [sysfs-driver-hid-roccat-ryos](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-ryos)

When read, this file returns general data like firmware version.
The data is 8 bytes long.
This file is readonly.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/ryos/roccatryos<minor>/key_mask** |

Defined on file [sysfs-driver-hid-roccat-ryos](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-ryos)

When written, this file lets one deactivate certain keys like
windows and application keys, to prevent accidental presses.
Profile index for which this settings occur is included in
written data. The data has to be 6 bytes long.
Before reading this file, control has to be written to select
which profile to read.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/ryos/roccatryos<minor>/keys_easyzone** |

Defined on file [sysfs-driver-hid-roccat-ryos](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-ryos)

When written, this file lets one set the function of the
easyzone keys for a specific profile. Profile index is included
in written data. The data has to be 294 bytes long.
Before reading this file, control has to be written to select
which profile to read.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/ryos/roccatryos<minor>/keys_extra** |

Defined on file [sysfs-driver-hid-roccat-ryos](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-ryos)

When written, this file lets one set the function of the
capslock and function keys for a specific profile. Profile index
is included in written data. The data has to be 8 bytes long.
Before reading this file, control has to be written to select
which profile to read.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/ryos/roccatryos<minor>/keys_function** |

Defined on file [sysfs-driver-hid-roccat-ryos](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-ryos)

When written, this file lets one set the function of the
function keys for a specific profile. Profile index is included
in written data. The data has to be 95 bytes long.
Before reading this file, control has to be written to select
which profile to read.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/ryos/roccatryos<minor>/keys_macro** |

Defined on file [sysfs-driver-hid-roccat-ryos](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-ryos)

When written, this file lets one set the function of the macro
keys for a specific profile. Profile index is included in
written data. The data has to be 35 bytes long.
Before reading this file, control has to be written to select
which profile to read.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/ryos/roccatryos<minor>/keys_primary** |

Defined on file [sysfs-driver-hid-roccat-ryos](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-ryos)

When written, this file lets one set the default of all keys for
a specific profile. Profile index is included in written data.
The data has to be 125 bytes long.
Before reading this file, control has to be written to select
which profile to read.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/ryos/roccatryos<minor>/keys_thumbster** |

Defined on file [sysfs-driver-hid-roccat-ryos](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-ryos)

When written, this file lets one set the function of the
thumbster keys for a specific profile. Profile index is included
in written data. The data has to be 23 bytes long.
Before reading this file, control has to be written to select
which profile to read.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/ryos/roccatryos<minor>/light** |

Defined on file [sysfs-driver-hid-roccat-ryos](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-ryos)

When written, this file lets one set the backlight intensity for
a specific profile. Profile index is included in written data.
This attribute is only valid for the glow and pro variant.
The data has to be 16 bytes long.
Before reading this file, control has to be written to select
which profile to read.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/ryos/roccatryos<minor>/light_control** |

Defined on file [sysfs-driver-hid-roccat-ryos](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-ryos)

When written, this file lets one switch between stored and custom
light settings.
This attribute is only valid for the pro variant.
The data has to be 8 bytes long.
This file is writeonly.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/ryos/roccatryos<minor>/light_macro** |

Defined on file [sysfs-driver-hid-roccat-ryos](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-ryos)

When written, this file lets one set a light macro that is looped
whenever the device gets in dimness mode.
This attribute is only valid for the pro variant.
The data has to be 2002 bytes long.
Before reading this file, control has to be written to select
which profile to read.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/ryos/roccatryos<minor>/macro** |

Defined on file [sysfs-driver-hid-roccat-ryos](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-ryos)

When written, this file lets one store macros with max 480
keystrokes for a specific button for a specific profile.
Button and profile indexes are included in written data.
The data has to be 2002 bytes long.
Before reading this file, control has to be written to select
which profile and key to read.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/ryos/roccatryos<minor>/profile** |

Defined on file [sysfs-driver-hid-roccat-ryos](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-ryos)

The mouse can store 5 profiles which can be switched by the
press of a button. profile holds index of actual profile.
This value is persistent, so its value determines the profile
that's active when the device is powered on next time.
When written, the device activates the set profile immediately.
The data has to be 3 bytes long.
The device will reject invalid data.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/ryos/roccatryos<minor>/reset** |

Defined on file [sysfs-driver-hid-roccat-ryos](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-ryos)

When written, this file lets one reset the device.
The data has to be 3 bytes long.
This file is writeonly.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/ryos/roccatryos<minor>/stored_lights** |

Defined on file [sysfs-driver-hid-roccat-ryos](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-ryos)

When written, this file lets one set per-key lighting for different
layers.
This attribute is only valid for the pro variant.
The data has to be 1382 bytes long.
Before reading this file, control has to be written to select
which profile to read.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/ryos/roccatryos<minor>/talk** |

Defined on file [sysfs-driver-hid-roccat-ryos](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-ryos)

When written, this file lets one trigger easyshift functionality
from the host.
The data has to be 16 bytes long.
This file is writeonly.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/savu/roccatsavu<minor>/buttons** |

Defined on file [sysfs-driver-hid-roccat-savu](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-savu)

The mouse can store 5 profiles which can be switched by the
press of a button. A profile is split into general settings and
button settings. The buttons variable holds information about
button layout. When written, this file lets one write the
respective profile buttons to the mouse. The data has to be
47 bytes long.
The mouse will reject invalid data.
Which profile to write is determined by the profile number
contained in the data.
Before reading this file, control has to be written to select
which profile to read.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/savu/roccatsavu<minor>/control** |

Defined on file [sysfs-driver-hid-roccat-savu](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-savu)

When written, this file lets one select which data from which
profile will be read next. The data has to be 3 bytes long.
This file is writeonly.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/savu/roccatsavu<minor>/general** |

Defined on file [sysfs-driver-hid-roccat-savu](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-savu)

The mouse can store 5 profiles which can be switched by the
press of a button. A profile is split into general settings and
button settings. A profile holds information like resolution,
sensitivity and light effects.
When written, this file lets one write the respective profile
settings back to the mouse. The data has to be 43 bytes long.
The mouse will reject invalid data.
Which profile to write is determined by the profile number
contained in the data.
This file is writeonly.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/savu/roccatsavu<minor>/info** |

Defined on file [sysfs-driver-hid-roccat-savu](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-savu)

When read, this file returns general data like firmware version.
When written, the device can be reset.
The data is 8 bytes long.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/savu/roccatsavu<minor>/macro** |

Defined on file [sysfs-driver-hid-roccat-savu](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-savu)

When written, this file lets one store macros with max 500
keystrokes for a specific button for a specific profile.
Button and profile numbers are included in written data.
The data has to be 2083 bytes long.
Before reading this file, control has to be written to select
which profile and key to read.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/savu/roccatsavu<minor>/profile** |

Defined on file [sysfs-driver-hid-roccat-savu](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-savu)

The mouse can store 5 profiles which can be switched by the
press of a button. profile holds number of actual profile.
This value is persistent, so its value determines the profile
that's active when the mouse is powered on next time.
When written, the mouse activates the set profile immediately.
The data has to be 3 bytes long.
The mouse will reject invalid data.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/savu/roccatsavu<minor>/sensor** |

Defined on file [sysfs-driver-hid-roccat-savu](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-savu)

The mouse has a Avago ADNS-3090 sensor.
This file allows reading and writing of the mouse sensors registers.
The data has to be 4 bytes long.

Users:
<http://roccat.sourceforge.net>

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/control** |

Defined on file [sysfs-driver-hid-roccat-lua](abi-obsolete.md#abi-file-obsolete-sysfs-driver-hid-roccat-lua)

When written, cpi, button and light settings can be configured.
When read, actual cpi setting and sensor data are returned.
The data has to be 8 bytes long.

Users:
<http://roccat.sourceforge.net>

## Symbols under /sys/class

|  |
| --- |
| **/sys/class/gpio/** |

Defined on file [sysfs-gpio](abi-obsolete.md#abi-file-obsolete-sysfs-gpio)

As a Kconfig option, individual GPIO signals may be accessed from
userspace. GPIOs are only made available to userspace by an explicit
"export" operation. If a given GPIO is not claimed for use by
kernel code, it may be exported by userspace (and unexported later).
Kernel code may export it for complete or partial access.

GPIOs are identified as they are inside the kernel, using integers in
the range 0..INT_MAX. See Documentation/admin-guide/gpio for more information.

```
/sys/class/gpio
    /export ... asks the kernel to export a GPIO to userspace
    /unexport ... to return a GPIO to the kernel
    /gpioN ... for each exported GPIO #N OR
    /<LINE-NAME> ... for a properly named GPIO line
        /value ... always readable, writes fail for input GPIOs
        /direction ... r/w as: in, out (default low); write: high, low
        /edge ... r/w as: none, falling, rising, both
    /gpiochipN ... for each gpiochip; #N is its first GPIO
        /base ... (r/o) same as N
        /label ... (r/o) descriptive, not necessarily unique
        /ngpio ... (r/o) number of GPIOs; numbered N to N + (ngpio - 1)
```

This ABI is deprecated and will be removed after 2020. It is
replaced with the GPIO character device.

|  |
| --- |
| **/sys/class/typec/<port|partner|cable>/<dev>/mode<index>/** |

Defined on file [sysfs-class-typec](abi-obsolete.md#abi-file-obsolete-sysfs-class-typec)

Every supported mode will have its own directory. The name of
a mode will be "mode<index>" (for example mode1), where <index>
is the actual index to the mode VDO returned by Discover Modes
USB power delivery command.

|  |
| --- |
| **/sys/class/typec/<port|partner|cable>/<dev>/mode<index>/active** |

Defined on file [sysfs-class-typec](abi-obsolete.md#abi-file-obsolete-sysfs-class-typec)

Shows if the mode is active or not. The attribute can be used
for entering/exiting the mode with partners and cable plugs, and
with the port alternate modes it can be used for disabling
support for specific alternate modes. Entering/exiting modes is
supported as synchronous operation so write(2) to the attribute
does not return until the enter/exit mode operation has
finished. The attribute is notified when the mode is
entered/exited so poll(2) on the attribute wakes up.
Entering/exiting a mode will also generate uevent KOBJ_CHANGE.

Valid values: yes, no

|  |
| --- |
| **/sys/class/typec/<port|partner|cable>/<dev>/mode<index>/description** |

Defined on file [sysfs-class-typec](abi-obsolete.md#abi-file-obsolete-sysfs-class-typec)

Shows description of the mode. The description is optional for
the drivers, just like with the Billboard Devices.

|  |
| --- |
| **/sys/class/typec/<port|partner|cable>/<dev>/mode<index>/vdo** |

Defined on file [sysfs-class-typec](abi-obsolete.md#abi-file-obsolete-sysfs-class-typec)

Shows the VDO in hexadecimal returned by Discover Modes command
for this mode.

|  |
| --- |
| **/sys/class/typec/<port|partner|cable>/<dev>/svid** |

Defined on file [sysfs-class-typec](abi-obsolete.md#abi-file-obsolete-sysfs-class-typec)

The SVID (Standard or Vendor ID) assigned by USB-IF for this
alternate mode.

## Symbols under /sys/devices

|  |
| --- |
| **/sys/devices/system/cpu/cpuidle/current_governor_ro** |

Defined on file [sysfs-cpuidle](abi-obsolete.md#abi-file-obsolete-sysfs-cpuidle)

current_governor_ro shows current using cpuidle governor, but read only.
with the update that cpuidle governor can be changed at runtime in default,
both current_governor and current_governor_ro co-exist under
/sys/devices/system/cpu/cpuidle/ file, it's duplicate so make
current_governor_ro obsolete.

## Symbols under /sys/firmware

|  |
| --- |
| **/sys/firmware/acpi/hotplug/force_remove** |

Defined on file [sysfs-firmware-acpi](abi-obsolete.md#abi-file-obsolete-sysfs-firmware-acpi)

Since the force_remove is inherently broken and dangerous to
use for some hotplugable resources like memory (because ignoring
the offline failure might lead to memory corruption and crashes)
enabling this knob is not safe and thus unsupported.

## Symbols under /sys/kernel

|  |
| --- |
| **/sys/kernel/fadump_enabled** |

Defined on file [sysfs-kernel-fadump_enabled](abi-obsolete.md#abi-file-obsolete-sysfs-kernel-fadump-enabled)

read only
Primarily used to identify whether the FADump is enabled in
the kernel or not.
User: Kdump service

|  |
| --- |
| **/sys/kernel/fadump_registered** |

Defined on file [sysfs-kernel-fadump_registered](abi-obsolete.md#abi-file-obsolete-sysfs-kernel-fadump-registered)

read/write
Helps to control the dump collect feature from userspace.
Setting 1 to this file enables the system to collect the
dump and 0 to disable it.
User: Kdump service

|  |
| --- |
| **/sys/kernel/fadump_release_mem** |

Defined on file [sysfs-kernel-fadump_release_mem](abi-obsolete.md#abi-file-obsolete-sysfs-kernel-fadump-release-mem)

write only
This is a special sysfs file and only available when
the system is booted to capture the vmcore using FADump.
It is used to release the memory reserved by FADump to
save the crash dump.

## Symbols under /sys/o2cb

|  |
| --- |
| **/sys/o2cb** |

Defined on file [o2cb](abi-obsolete.md#abi-file-obsolete-o2cb)

Ocfs2-tools looks at 'interface-revision' for versioning
information. Each logmask/ file controls a set of debug prints
and can be written into with the strings "allow", "deny", or
"off". Reading the file returns the current state.
Was renamed to /sys/fs/u2cb/

Users:
ocfs2-tools. It's sufficient to mail proposed changes to
[ocfs2-devel@lists.linux.dev](mailto:ocfs2-devel%40lists.linux.dev).

## File obsolete/o2cb

Has the following ABI:

- [/sys/o2cb](abi-obsolete.md#abi-sys-o2cb)

## File obsolete/procfs-i8k

Has the following ABI:

- [/proc/i8k](abi-obsolete.md#abi-proc-i8k)

## File obsolete/sysfs-bus-iio

Has the following ABI:

- [/sys/bus/iio/devices/iio:deviceX/buffer/length](abi-obsolete.md#abi-sys-bus-iio-devices-iio-devicex-buffer-length)
- [/sys/bus/iio/devices/iio:deviceX/buffer/enable](abi-obsolete.md#abi-sys-bus-iio-devices-iio-devicex-buffer-enable)
- [/sys/bus/iio/devices/iio:deviceX/scan_elements](abi-obsolete.md#abi-sys-bus-iio-devices-iio-devicex-scan-elements)
- [/sys/.../iio:deviceX/scan_elements/in_accel_x_en](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-accel-x-en)
- [/sys/.../iio:deviceX/scan_elements/in_accel_y_en](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-accel-x-en)
- [/sys/.../iio:deviceX/scan_elements/in_accel_z_en](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-accel-x-en)
- [/sys/.../iio:deviceX/scan_elements/in_anglvel_x_en](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-accel-x-en)
- [/sys/.../iio:deviceX/scan_elements/in_anglvel_y_en](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-accel-x-en)
- [/sys/.../iio:deviceX/scan_elements/in_anglvel_z_en](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-accel-x-en)
- [/sys/.../iio:deviceX/scan_elements/in_magn_x_en](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-accel-x-en)
- [/sys/.../iio:deviceX/scan_elements/in_magn_y_en](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-accel-x-en)
- [/sys/.../iio:deviceX/scan_elements/in_magn_z_en](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-accel-x-en)
- [/sys/.../iio:deviceX/scan_elements/in_rot_from_north_magnetic_en](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-accel-x-en)
- [/sys/.../iio:deviceX/scan_elements/in_rot_from_north_true_en](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-accel-x-en)
- [/sys/.../iio:deviceX/scan_elements/in_rot_from_north_magnetic_tilt_comp_en](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-accel-x-en)
- [/sys/.../iio:deviceX/scan_elements/in_rot_from_north_true_tilt_comp_en](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-accel-x-en)
- [/sys/.../iio:deviceX/scan_elements/in_timestamp_en](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-accel-x-en)
- [/sys/.../iio:deviceX/scan_elements/in_voltageY_supply_en](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-accel-x-en)
- [/sys/.../iio:deviceX/scan_elements/in_voltageY_en](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-accel-x-en)
- [/sys/.../iio:deviceX/scan_elements/in_voltageY-voltageZ_en](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-accel-x-en)
- [/sys/.../iio:deviceX/scan_elements/in_voltageY_i_en](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-accel-x-en)
- [/sys/.../iio:deviceX/scan_elements/in_voltageY_q_en](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-accel-x-en)
- [/sys/.../iio:deviceX/scan_elements/in_voltage_i_en](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-accel-x-en)
- [/sys/.../iio:deviceX/scan_elements/in_voltage_q_en](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-accel-x-en)
- [/sys/.../iio:deviceX/scan_elements/in_incli_x_en](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-accel-x-en)
- [/sys/.../iio:deviceX/scan_elements/in_incli_y_en](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-accel-x-en)
- [/sys/.../iio:deviceX/scan_elements/in_pressureY_en](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-accel-x-en)
- [/sys/.../iio:deviceX/scan_elements/in_pressure_en](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-accel-x-en)
- [/sys/.../iio:deviceX/scan_elements/in_rot_quaternion_en](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-accel-x-en)
- [/sys/.../iio:deviceX/scan_elements/in_proximity_en](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-accel-x-en)
- [/sys/.../iio:deviceX/scan_elements/in_accel_type](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-accel-type)
- [/sys/.../iio:deviceX/scan_elements/in_anglvel_type](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-accel-type)
- [/sys/.../iio:deviceX/scan_elements/in_magn_type](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-accel-type)
- [/sys/.../iio:deviceX/scan_elements/in_incli_type](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-accel-type)
- [/sys/.../iio:deviceX/scan_elements/in_voltageY_type](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-accel-type)
- [/sys/.../iio:deviceX/scan_elements/in_voltage_type](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-accel-type)
- [/sys/.../iio:deviceX/scan_elements/in_voltageY_supply_type](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-accel-type)
- [/sys/.../iio:deviceX/scan_elements/in_voltageY_i_type](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-accel-type)
- [/sys/.../iio:deviceX/scan_elements/in_voltageY_q_type](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-accel-type)
- [/sys/.../iio:deviceX/scan_elements/in_voltage_i_type](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-accel-type)
- [/sys/.../iio:deviceX/scan_elements/in_voltage_q_type](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-accel-type)
- [/sys/.../iio:deviceX/scan_elements/in_timestamp_type](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-accel-type)
- [/sys/.../iio:deviceX/scan_elements/in_pressureY_type](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-accel-type)
- [/sys/.../iio:deviceX/scan_elements/in_pressure_type](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-accel-type)
- [/sys/.../iio:deviceX/scan_elements/in_rot_quaternion_type](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-accel-type)
- [/sys/.../iio:deviceX/scan_elements/in_proximity_type](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-accel-type)
- [/sys/.../iio:deviceX/scan_elements/in_voltageY_index](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-voltagey-index)
- [/sys/.../iio:deviceX/scan_elements/in_voltageY_supply_index](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-voltagey-index)
- [/sys/.../iio:deviceX/scan_elements/in_voltageY_i_index](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-voltagey-index)
- [/sys/.../iio:deviceX/scan_elements/in_voltageY_q_index](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-voltagey-index)
- [/sys/.../iio:deviceX/scan_elements/in_voltage_i_index](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-voltagey-index)
- [/sys/.../iio:deviceX/scan_elements/in_voltage_q_index](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-voltagey-index)
- [/sys/.../iio:deviceX/scan_elements/in_accel_x_index](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-voltagey-index)
- [/sys/.../iio:deviceX/scan_elements/in_accel_y_index](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-voltagey-index)
- [/sys/.../iio:deviceX/scan_elements/in_accel_z_index](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-voltagey-index)
- [/sys/.../iio:deviceX/scan_elements/in_anglvel_x_index](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-voltagey-index)
- [/sys/.../iio:deviceX/scan_elements/in_anglvel_y_index](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-voltagey-index)
- [/sys/.../iio:deviceX/scan_elements/in_anglvel_z_index](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-voltagey-index)
- [/sys/.../iio:deviceX/scan_elements/in_magn_x_index](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-voltagey-index)
- [/sys/.../iio:deviceX/scan_elements/in_magn_y_index](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-voltagey-index)
- [/sys/.../iio:deviceX/scan_elements/in_magn_z_index](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-voltagey-index)
- [/sys/.../iio:deviceX/scan_elements/in_rot_from_north_magnetic_index](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-voltagey-index)
- [/sys/.../iio:deviceX/scan_elements/in_rot_from_north_true_index](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-voltagey-index)
- [/sys/.../iio:deviceX/scan_elements/in_rot_from_north_magnetic_tilt_comp_index](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-voltagey-index)
- [/sys/.../iio:deviceX/scan_elements/in_rot_from_north_true_tilt_comp_index](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-voltagey-index)
- [/sys/.../iio:deviceX/scan_elements/in_incli_x_index](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-voltagey-index)
- [/sys/.../iio:deviceX/scan_elements/in_incli_y_index](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-voltagey-index)
- [/sys/.../iio:deviceX/scan_elements/in_timestamp_index](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-voltagey-index)
- [/sys/.../iio:deviceX/scan_elements/in_pressureY_index](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-voltagey-index)
- [/sys/.../iio:deviceX/scan_elements/in_pressure_index](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-voltagey-index)
- [/sys/.../iio:deviceX/scan_elements/in_rot_quaternion_index](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-voltagey-index)
- [/sys/.../iio:deviceX/scan_elements/in_proximity_index](abi-obsolete.md#abi-sys-iio-devicex-scan-elements-in-voltagey-index)
- [/sys/bus/iio/devices/iio:deviceX/buffer/watermark](abi-obsolete.md#abi-sys-bus-iio-devices-iio-devicex-buffer-watermark)
- [/sys/bus/iio/devices/iio:deviceX/buffer/data_available](abi-obsolete.md#abi-sys-bus-iio-devices-iio-devicex-buffer-data-available)

## File obsolete/sysfs-bus-usb

Has the following ABI:

- [/sys/bus/usb/devices/.../power/level](abi-obsolete.md#abi-sys-bus-usb-devices-power-level)

## File obsolete/sysfs-class-typec

These files are deprecated and will be removed. The same files are available
under /sys/bus/typec (see [testing/sysfs-bus-typec](abi-testing.md#abi-file-testing-sysfs-bus-typec)).

Has the following ABI:

- [/sys/class/typec/<port|partner|cable>/<dev>/svid](abi-obsolete.md#abi-sys-class-typec-port-partner-cable-dev-svid)
- [/sys/class/typec/<port|partner|cable>/<dev>/mode<index>/](abi-obsolete.md#abi-sys-class-typec-port-partner-cable-dev-mode-index)
- [/sys/class/typec/<port|partner|cable>/<dev>/mode<index>/description](abi-obsolete.md#abi-sys-class-typec-port-partner-cable-dev-mode-index-description)
- [/sys/class/typec/<port|partner|cable>/<dev>/mode<index>/vdo](abi-obsolete.md#abi-sys-class-typec-port-partner-cable-dev-mode-index-vdo)
- [/sys/class/typec/<port|partner|cable>/<dev>/mode<index>/active](abi-obsolete.md#abi-sys-class-typec-port-partner-cable-dev-mode-index-active)

## File obsolete/sysfs-cpuidle

Has the following ABI:

- [/sys/devices/system/cpu/cpuidle/current_governor_ro](abi-obsolete.md#abi-sys-devices-system-cpu-cpuidle-current-governor-ro)

## File obsolete/sysfs-driver-hid-roccat-arvo

Has the following ABI:

- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/arvo/roccatarvo<minor>/actual_profile](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-arvo-roccatarvo-minor-actual-profile)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/arvo/roccatarvo<minor>/button](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-arvo-roccatarvo-minor-button)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/arvo/roccatarvo<minor>/info](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-arvo-roccatarvo-minor-info)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/arvo/roccatarvo<minor>/key_mask](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-arvo-roccatarvo-minor-key-mask)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/arvo/roccatarvo<minor>/mode_key](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-arvo-roccatarvo-minor-mode-key)

## File obsolete/sysfs-driver-hid-roccat-isku

Has the following ABI:

- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/isku/roccatisku<minor>/actual_profile](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-isku-roccatisku-minor-actual-profile)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/isku/roccatisku<minor>/info](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-isku-roccatisku-minor-info)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/isku/roccatisku<minor>/key_mask](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-isku-roccatisku-minor-key-mask)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/isku/roccatisku<minor>/keys_capslock](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-isku-roccatisku-minor-keys-capslock)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/isku/roccatisku<minor>/keys_easyzone](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-isku-roccatisku-minor-keys-easyzone)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/isku/roccatisku<minor>/keys_function](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-isku-roccatisku-minor-keys-function)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/isku/roccatisku<minor>/keys_macro](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-isku-roccatisku-minor-keys-macro)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/isku/roccatisku<minor>/keys_media](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-isku-roccatisku-minor-keys-media)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/isku/roccatisku<minor>/keys_thumbster](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-isku-roccatisku-minor-keys-thumbster)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/isku/roccatisku<minor>/last_set](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-isku-roccatisku-minor-last-set)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/isku/roccatisku<minor>/light](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-isku-roccatisku-minor-light)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/isku/roccatisku<minor>/macro](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-isku-roccatisku-minor-macro)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/isku/roccatisku<minor>/reset](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-isku-roccatisku-minor-reset)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/isku/roccatisku<minor>/control](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-isku-roccatisku-minor-control)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/isku/roccatisku<minor>/talk](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-isku-roccatisku-minor-talk)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/isku/roccatisku<minor>/talkfx](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-isku-roccatisku-minor-talkfx)

## File obsolete/sysfs-driver-hid-roccat-koneplus

Has the following ABI:

- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/koneplus/roccatkoneplus<minor>/actual_profile](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-koneplus-roccatkoneplus-minor-actual-profile)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/koneplus/roccatkoneplus<minor>/startup_profile](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-koneplus-roccatkoneplus-minor-startup-profile)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/koneplus/roccatkoneplus<minor>/firmware_version](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-koneplus-roccatkoneplus-minor-firmware-version)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/koneplus/roccatkoneplus<minor>/info](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-koneplus-roccatkoneplus-minor-info)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/koneplus/roccatkoneplus<minor>/macro](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-koneplus-roccatkoneplus-minor-macro)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/koneplus/roccatkoneplus<minor>/profile_buttons](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-koneplus-roccatkoneplus-minor-profile-buttons)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/koneplus/roccatkoneplus<minor>/profile[1-5]_buttons](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-koneplus-roccatkoneplus-minor-profile-1-5-buttons)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/koneplus/roccatkoneplus<minor>/profile_settings](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-koneplus-roccatkoneplus-minor-profile-settings)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/koneplus/roccatkoneplus<minor>/profile[1-5]_settings](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-koneplus-roccatkoneplus-minor-profile-1-5-settings)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/koneplus/roccatkoneplus<minor>/sensor](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-koneplus-roccatkoneplus-minor-sensor)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/koneplus/roccatkoneplus<minor>/talk](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-koneplus-roccatkoneplus-minor-talk)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/koneplus/roccatkoneplus<minor>/tcu](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-koneplus-roccatkoneplus-minor-tcu)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/koneplus/roccatkoneplus<minor>/tcu_image](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-koneplus-roccatkoneplus-minor-tcu-image)

## File obsolete/sysfs-driver-hid-roccat-konepure

Has the following ABI:

- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/konepure/roccatkonepure<minor>/actual_profile](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-konepure-roccatkonepure-minor-actual-profile)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/konepure/roccatkonepure<minor>/control](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-konepure-roccatkonepure-minor-control)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/konepure/roccatkonepure<minor>/info](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-konepure-roccatkonepure-minor-info)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/konepure/roccatkonepure<minor>/macro](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-konepure-roccatkonepure-minor-macro)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/konepure/roccatkonepure<minor>/profile_buttons](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-konepure-roccatkonepure-minor-profile-buttons)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/konepure/roccatkonepure<minor>/profile_settings](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-konepure-roccatkonepure-minor-profile-settings)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/konepure/roccatkonepure<minor>/sensor](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-konepure-roccatkonepure-minor-sensor)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/konepure/roccatkonepure<minor>/talk](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-konepure-roccatkonepure-minor-talk)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/konepure/roccatkonepure<minor>/tcu](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-konepure-roccatkonepure-minor-tcu)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/konepure/roccatkonepure<minor>/tcu_image](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-konepure-roccatkonepure-minor-tcu-image)

## File obsolete/sysfs-driver-hid-roccat-kovaplus

Has the following ABI:

- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/kovaplus/roccatkovaplus<minor>/actual_cpi](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-kovaplus-roccatkovaplus-minor-actual-cpi)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/kovaplus/roccatkovaplus<minor>/actual_profile](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-kovaplus-roccatkovaplus-minor-actual-profile)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/kovaplus/roccatkovaplus<minor>/actual_sensitivity_x](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-kovaplus-roccatkovaplus-minor-actual-sensitivity-x)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/kovaplus/roccatkovaplus<minor>/actual_sensitivity_y](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-kovaplus-roccatkovaplus-minor-actual-sensitivity-y)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/kovaplus/roccatkovaplus<minor>/firmware_version](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-kovaplus-roccatkovaplus-minor-firmware-version)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/kovaplus/roccatkovaplus<minor>/info](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-kovaplus-roccatkovaplus-minor-info)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/kovaplus/roccatkovaplus<minor>/profile_buttons](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-kovaplus-roccatkovaplus-minor-profile-buttons)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/kovaplus/roccatkovaplus<minor>/profile[1-5]_buttons](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-kovaplus-roccatkovaplus-minor-profile-1-5-buttons)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/kovaplus/roccatkovaplus<minor>/profile_settings](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-kovaplus-roccatkovaplus-minor-profile-settings)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/kovaplus/roccatkovaplus<minor>/profile[1-5]_settings](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-kovaplus-roccatkovaplus-minor-profile-1-5-settings)

## File obsolete/sysfs-driver-hid-roccat-lua

Has the following ABI:

- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/control](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-control)

## File obsolete/sysfs-driver-hid-roccat-pyra

Has the following ABI:

- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/pyra/roccatpyra<minor>/actual_cpi](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-pyra-roccatpyra-minor-actual-cpi)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/pyra/roccatpyra<minor>/actual_profile](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-pyra-roccatpyra-minor-actual-profile)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/pyra/roccatpyra<minor>/firmware_version](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-pyra-roccatpyra-minor-firmware-version)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/pyra/roccatpyra<minor>/info](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-pyra-roccatpyra-minor-info)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/pyra/roccatpyra<minor>/profile_buttons](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-pyra-roccatpyra-minor-profile-buttons)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/pyra/roccatpyra<minor>/profile[1-5]_buttons](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-pyra-roccatpyra-minor-profile-1-5-buttons)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/pyra/roccatpyra<minor>/profile_settings](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-pyra-roccatpyra-minor-profile-settings)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/pyra/roccatpyra<minor>/profile[1-5]_settings](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-pyra-roccatpyra-minor-profile-1-5-settings)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/pyra/roccatpyra<minor>/settings](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-pyra-roccatpyra-minor-settings)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/pyra/roccatpyra<minor>/startup_profile](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-pyra-roccatpyra-minor-startup-profile)

## File obsolete/sysfs-driver-hid-roccat-ryos

Has the following ABI:

- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/ryos/roccatryos<minor>/control](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-ryos-roccatryos-minor-control)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/ryos/roccatryos<minor>/profile](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-ryos-roccatryos-minor-profile)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/ryos/roccatryos<minor>/keys_primary](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-ryos-roccatryos-minor-keys-primary)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/ryos/roccatryos<minor>/keys_function](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-ryos-roccatryos-minor-keys-function)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/ryos/roccatryos<minor>/keys_macro](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-ryos-roccatryos-minor-keys-macro)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/ryos/roccatryos<minor>/keys_thumbster](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-ryos-roccatryos-minor-keys-thumbster)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/ryos/roccatryos<minor>/keys_extra](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-ryos-roccatryos-minor-keys-extra)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/ryos/roccatryos<minor>/keys_easyzone](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-ryos-roccatryos-minor-keys-easyzone)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/ryos/roccatryos<minor>/key_mask](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-ryos-roccatryos-minor-key-mask)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/ryos/roccatryos<minor>/light](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-ryos-roccatryos-minor-light)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/ryos/roccatryos<minor>/macro](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-ryos-roccatryos-minor-macro)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/ryos/roccatryos<minor>/info](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-ryos-roccatryos-minor-info)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/ryos/roccatryos<minor>/reset](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-ryos-roccatryos-minor-reset)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/ryos/roccatryos<minor>/talk](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-ryos-roccatryos-minor-talk)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/ryos/roccatryos<minor>/light_control](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-ryos-roccatryos-minor-light-control)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/ryos/roccatryos<minor>/stored_lights](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-ryos-roccatryos-minor-stored-lights)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/ryos/roccatryos<minor>/custom_lights](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-ryos-roccatryos-minor-custom-lights)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/ryos/roccatryos<minor>/light_macro](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-ryos-roccatryos-minor-light-macro)

## File obsolete/sysfs-driver-hid-roccat-savu

Has the following ABI:

- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/savu/roccatsavu<minor>/buttons](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-savu-roccatsavu-minor-buttons)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/savu/roccatsavu<minor>/control](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-savu-roccatsavu-minor-control)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/savu/roccatsavu<minor>/general](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-savu-roccatsavu-minor-general)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/savu/roccatsavu<minor>/info](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-savu-roccatsavu-minor-info)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/savu/roccatsavu<minor>/macro](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-savu-roccatsavu-minor-macro)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/savu/roccatsavu<minor>/profile](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-savu-roccatsavu-minor-profile)
- [/sys/bus/usb/devices/<busnum>-<devnum>:<config num>.<interface num>/<hid-bus>:<vendor-id>:<product-id>.<num>/savu/roccatsavu<minor>/sensor](abi-obsolete.md#abi-sys-bus-usb-devices-busnum-devnum-config-num-interface-num-hid-bus-vendor-id-product-id-num-savu-roccatsavu-minor-sensor)

## File obsolete/sysfs-driver-intel_pmc_bxt

These files allow sending arbitrary IPC commands to the PMC/SCU which
may be dangerous. These will be removed eventually and should not be
used in any new applications.

Has the following ABI:

- [/sys/bus/platform/devices/INT34D2:00/simplecmd](abi-obsolete.md#abi-sys-bus-platform-devices-int34d2-00-simplecmd)
- [/sys/bus/platform/devices/INT34D2:00/northpeak](abi-obsolete.md#abi-sys-bus-platform-devices-int34d2-00-northpeak)

## File obsolete/sysfs-firmware-acpi

Has the following ABI:

- [/sys/firmware/acpi/hotplug/force_remove](abi-obsolete.md#abi-sys-firmware-acpi-hotplug-force-remove)

## File obsolete/sysfs-gpio

Has the following ABI:

- [/sys/class/gpio/](abi-obsolete.md#abi-sys-class-gpio)

## File obsolete/sysfs-kernel-fadump_enabled

This ABI is renamed and moved to a new location /sys/kernel/fadump/enabled.

Has the following ABI:

- [/sys/kernel/fadump_enabled](abi-testing.md#abi-sys-kernel-fadump-enabled)

## File obsolete/sysfs-kernel-fadump_registered

This ABI is renamed and moved to a new location /sys/kernel/fadump/registered.

Has the following ABI:

- [/sys/kernel/fadump_registered](abi-testing.md#abi-sys-kernel-fadump-registered)

## File obsolete/sysfs-kernel-fadump_release_mem

This ABI is renamed and moved to a new location /sys/kernel/fadump/release_mem.

Has the following ABI:

- [/sys/kernel/fadump_release_mem](abi-testing.md#abi-sys-kernel-fadump-release-mem)
