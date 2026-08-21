---
collection: kernel
version: "6.8"
title: "Miscellaneous Devices"
source_url: https://www.kernel.org/doc/html/v6.8/driver-api/misc_devices.html
fetched_at: 2026-08-21T03:31:03+00:00
---
# Miscellaneous Devices

int misc_register(struct miscdevice \*misc)
:   register a miscellaneous device

**Parameters**

`struct miscdevice *misc`
:   device structure

    Register a miscellaneous device with the kernel. If the minor
    number is set to `MISC_DYNAMIC_MINOR` a minor number is assigned
    and placed in the minor field of the structure. For other cases
    the minor number requested is used.

    The structure passed is linked into the kernel and may not be
    destroyed until it has been unregistered. By default, an open()
    syscall to the device sets file->private_data to point to the
    structure. Drivers don't need open in fops for this.

    A zero is returned on success and a negative errno code for
    failure.

void misc_deregister(struct miscdevice \*misc)
:   unregister a miscellaneous device

**Parameters**

`struct miscdevice *misc`
:   device to unregister

    Unregister a miscellaneous device that was previously
    successfully registered with [`misc_register()`](misc_devices.md#c.misc_register "misc_register").
