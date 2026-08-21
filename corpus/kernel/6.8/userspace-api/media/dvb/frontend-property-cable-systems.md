---
collection: kernel
version: "6.8"
title: "2.3.4. Properties used on cable delivery systems"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/dvb/frontend-property-cable-systems.html
fetched_at: 2026-08-21T03:57:50+00:00
---
# 2.3.4. Properties used on cable delivery systems

## 2.3.4.1. DVB-C delivery system

The DVB-C Annex-A is the widely used cable standard. Transmission uses
QAM modulation.

The DVB-C Annex-C is optimized for 6MHz, and is used in Japan. It
supports a subset of the Annex A modulation types, and a roll-off of
0.13, instead of 0.15

The following parameters are valid for DVB-C Annex A/C:

- [DTV_API_VERSION](fe_property_parameters.md#dtv-api-version)
- [DTV_DELIVERY_SYSTEM](fe_property_parameters.md#dtv-delivery-system)
- [DTV_TUNE](fe_property_parameters.md#dtv-tune)
- [DTV_CLEAR](fe_property_parameters.md#dtv-clear)
- [DTV_FREQUENCY](fe_property_parameters.md#dtv-frequency)
- [DTV_MODULATION](fe_property_parameters.md#dtv-modulation)
- [DTV_INVERSION](fe_property_parameters.md#dtv-inversion)
- [DTV_SYMBOL_RATE](fe_property_parameters.md#dtv-symbol-rate)
- [DTV_INNER_FEC](fe_property_parameters.md#dtv-inner-fec)
- [DTV_LNA](fe_property_parameters.md#dtv-lna)

In addition, the [DTV QoS statistics](frontend-stat-properties.md#frontend-stat-properties)
are also valid.

## 2.3.4.2. DVB-C Annex B delivery system

The DVB-C Annex-B is only used on a few Countries like the United
States.

The following parameters are valid for DVB-C Annex B:

- [DTV_API_VERSION](fe_property_parameters.md#dtv-api-version)
- [DTV_DELIVERY_SYSTEM](fe_property_parameters.md#dtv-delivery-system)
- [DTV_TUNE](fe_property_parameters.md#dtv-tune)
- [DTV_CLEAR](fe_property_parameters.md#dtv-clear)
- [DTV_FREQUENCY](fe_property_parameters.md#dtv-frequency)
- [DTV_MODULATION](fe_property_parameters.md#dtv-modulation)
- [DTV_INVERSION](fe_property_parameters.md#dtv-inversion)
- [DTV_LNA](fe_property_parameters.md#dtv-lna)

In addition, the [DTV QoS statistics](frontend-stat-properties.md#frontend-stat-properties)
are also valid.
