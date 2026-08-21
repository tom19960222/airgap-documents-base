---
collection: kernel
version: "6.8"
title: "Devlink Selftests"
source_url: https://www.kernel.org/doc/html/v6.8/networking/devlink/devlink-selftests.html
fetched_at: 2026-08-21T04:00:07+00:00
---
# Devlink Selftests

The `devlink-selftests` API allows executing selftests on the device.

## Tests Mask

The `devlink-selftests` command should be run with a mask indicating
the tests to be executed.

## Tests Description

The following is a list of tests that drivers may execute.

List of tests

|  |  |
| --- | --- |
| Name | Description |
| `DEVLINK_SELFTEST_FLASH` | Devices may have the firmware on non-volatile memory on the board, e.g. flash. This particular test helps to run a flash selftest on the device. Implementation of the test is left to the driver/firmware. |

### example usage

```shell
# Query selftests supported on the devlink device
$ devlink dev selftests show DEV
# Query selftests supported on all devlink devices
$ devlink dev selftests show
# Executes selftests on the device
$ devlink dev selftests run DEV id flash
```
