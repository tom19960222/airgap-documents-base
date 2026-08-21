---
collection: kernel
version: "6.8"
title: "Firmware lookup order"
source_url: https://www.kernel.org/doc/html/v6.8/driver-api/firmware/lookup-order.html
fetched_at: 2026-08-21T03:46:22+00:00
---
# Firmware lookup order

Different functionality is available to enable firmware to be found.
Below is chronological order of how firmware will be looked for once
a driver issues a firmware API call.

- The ''Built-in firmware'' is checked first, if the firmware is present we
  return it immediately
- The ''Firmware cache'' is looked at next. If the firmware is found we
  return it immediately
- The ''Direct filesystem lookup'' is performed next, if found we
  return it immediately
- The ''Platform firmware fallback'' is performed next, but only when
  [`firmware_request_platform()`](request_firmware.md#c.firmware_request_platform "firmware_request_platform") is used, if found we return it immediately
- If no firmware has been found and the fallback mechanism was enabled
  the sysfs interface is created. After this either a kobject uevent
  is issued or the custom firmware loading is relied upon for firmware
  loading up to the timeout value.
