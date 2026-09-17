---
collection: kernel
version: "6.17"
title: "GPIO_V2_LINE_SET_CONFIG_IOCTL"
source_url: https://www.kernel.org/doc/html/v6.17/userspace-api/gpio/gpio-v2-line-set-config-ioctl.html
fetched_at: 2026-09-16T16:28:46+00:00
---
# GPIO_V2_LINE_SET_CONFIG_IOCTL

## Name

GPIO_V2_LINE_SET_CONFIG_IOCTL - Update the configuration of previously requested lines.

## Synopsis

GPIO_V2_LINE_SET_CONFIG_IOCTL

`int ioctl(int req_fd, GPIO_V2_LINE_SET_CONFIG_IOCTL, struct gpio_v2_line_config *config)`

## Arguments

`req_fd`
:   The file descriptor of the GPIO character device, as returned in the
    [`request.fd`](chardev.md#c.gpio_v2_line_request "gpio_v2_line_request") by [GPIO_V2_GET_LINE_IOCTL](gpio-v2-get-line-ioctl.md).

`config`
:   The new [`configuration`](chardev.md#c.gpio_v2_line_config "gpio_v2_line_config") to apply to the
    requested lines.

## Description

Update the configuration of previously requested lines, without releasing the
line or introducing potential glitches.

The new configuration must specify a configuration for all requested lines.

The same [Configuration Rules](gpio-v2-get-line-ioctl.md#gpio-v2-get-line-config-rules) and
[Configuration Support](gpio-v2-get-line-ioctl.md#gpio-v2-get-line-config-support) that apply when requesting the lines
also apply when updating the line configuration, with the additional
restriction that a direction flag must be set to enable reconfiguration.
If no direction flag is set in the configuration for a given line then the
configuration for that line is left unchanged.

The motivating use case for this command is changing direction of
bi-directional lines between input and output, but it may also be used to
dynamically control edge detection, or more generally move lines seamlessly
from one configuration state to another.

To only change the value of output lines, use
[GPIO_V2_LINE_SET_VALUES_IOCTL](gpio-v2-line-set-values-ioctl.md).

## Return Value

On success 0.

On error -1 and the `errno` variable is set appropriately.
Common error codes are described in [GPIO Error Codes](error-codes.md).
