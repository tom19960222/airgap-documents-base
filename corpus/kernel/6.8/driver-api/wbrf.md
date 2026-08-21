---
collection: kernel
version: "6.8"
title: "WBRF - Wifi Band RFI Mitigations"
source_url: https://www.kernel.org/doc/html/v6.8/driver-api/wbrf.html
fetched_at: 2026-08-21T03:31:28+00:00
---
# WBRF - Wifi Band RFI Mitigations

Due to electrical and mechanical constraints in certain platform designs
there may be likely interference of relatively high-powered harmonics of
the GPU memory clocks with local radio module frequency bands used by
certain Wifi bands.

To mitigate possible RFI interference producers can advertise the
frequencies in use and consumers can use this information to avoid using
these frequencies for sensitive features.

When a platform is known to have this issue with any contained devices,
the platform designer will advertise the availability of this feature via
ACPI devices with a device specific method (_DSM).
\* Producers with this _DSM will be able to advertise the frequencies in use.
\* Consumers with this _DSM will be able to register for notifications of
frequencies in use.

## Some general terms

Producer: such component who can produce high-powered radio frequency
Consumer: such component who can adjust its in-use frequency in
response to the radio frequencies of other components to mitigate the
possible RFI.

To make the mechanism function, those producers should notify active use
of their particular frequencies so that other consumers can make relative
internal adjustments as necessary to avoid this resonance.

## ACPI interface

Although initially used by for wifi + dGPU use cases, the ACPI interface
can be scaled to any type of device that a platform designer discovers
can cause interference.

The GUID used for the _DSM is 7B7656CF-DC3D-4C1C-83E9-66E721DE3070.

3 functions are available in this _DSM:

- 0: discover # of functions available
- 1: record RF bands in use
- 2: retrieve RF bands in use

## Driver programming interface

int acpi_amd_wbrf_add_remove(struct [device](infrastructure.md#c.device "device") \*dev, uint8_t action, struct wbrf_ranges_in_out \*in)
:   add or remove the frequency band the device is using

**Parameters**

`struct device *dev`
:   device pointer

`uint8_t action`
:   remove or add the frequency band into bios

`struct wbrf_ranges_in_out *in`
:   input structure containing the frequency band the device is using

**Description**

Broadcast to other consumers the frequency band the device starts
to use. Underneath the surface the information is cached into an
internal buffer first. Then a notification is sent to all those
registered consumers. So then they can retrieve that buffer to
know the latest active frequency bands. Consumers that haven't
yet been registered can retrieve the information from the cache
when they register.

**Return**

0 for success add/remove wifi frequency band.
Returns a negative error code for failure.

bool acpi_amd_wbrf_supported_producer(struct [device](infrastructure.md#c.device "device") \*dev)
:   determine if the WBRF can be enabled for the device as a producer

**Parameters**

`struct device *dev`
:   device pointer

**Description**

Check if the platform equipped with necessary implementations to
support WBRF for the device as a producer.

**Return**

true if WBRF is supported, otherwise returns false

bool acpi_amd_wbrf_supported_consumer(struct [device](infrastructure.md#c.device "device") \*dev)
:   determine if the WBRF can be enabled for the device as a consumer

**Parameters**

`struct device *dev`
:   device pointer

**Description**

Determine if the platform equipped with necessary implementations to
support WBRF for the device as a consumer.

**Return**

true if WBRF is supported, otherwise returns false.

int amd_wbrf_retrieve_freq_band(struct [device](infrastructure.md#c.device "device") \*dev, struct wbrf_ranges_in_out \*out)
:   retrieve current active frequency bands

**Parameters**

`struct device *dev`
:   device pointer

`struct wbrf_ranges_in_out *out`
:   output structure containing all the active frequency bands

**Description**

Retrieve the current active frequency bands which were broadcasted
by other producers. The consumer who calls this API should take
proper actions if any of the frequency band may cause RFI with its
own frequency band used.

**Return**

0 for getting wifi freq band successfully.
Returns a negative error code for failure.

int amd_wbrf_register_notifier(struct notifier_block \*nb)
:   register for notifications of frequency band update

**Parameters**

`struct notifier_block *nb`
:   driver notifier block

**Description**

The consumer should register itself via this API so that it can get
notified on the frequency band updates from other producers.

**Return**

0 for registering a consumer driver successfully.
Returns a negative error code for failure.

int amd_wbrf_unregister_notifier(struct notifier_block \*nb)
:   unregister for notifications of frequency band update

**Parameters**

`struct notifier_block *nb`
:   driver notifier block

**Description**

The consumer should call this API when it is longer interested with
the frequency band updates from other producers. Usually, this should
be performed during driver cleanup.

**Return**

0 for unregistering a consumer driver.
Returns a negative error code for failure.

## Sample Usage

The expected flow for the producers:
1. During probe, call acpi_amd_wbrf_supported_producer to check if WBRF
can be enabled for the device.
2. On using some frequency band, call acpi_amd_wbrf_add_remove with 'add'
param to get other consumers properly notified.
3. Or on stopping using some frequency band, call
acpi_amd_wbrf_add_remove with 'remove' param to get other consumers notified.

The expected flow for the consumers:
1. During probe, call acpi_amd_wbrf_supported_consumer to check if WBRF
can be enabled for the device.
2. Call amd_wbrf_register_notifier to register for notification
of frequency band change(add or remove) from other producers.
3. Call the amd_wbrf_retrieve_freq_band initally to retrieve
current active frequency bands considering some producers may broadcast
such information before the consumer is up.
4. On receiving a notification for frequency band change, run
amd_wbrf_retrieve_freq_band again to retrieve the latest
active frequency bands.
5. During driver cleanup, call amd_wbrf_unregister_notifier to
unregister the notifier.
