---
collection: kernel
version: "6.8"
title: "2.3.5. Properties used on satellite delivery systems"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/dvb/frontend-property-satellite-systems.html
fetched_at: 2026-08-21T03:57:50+00:00
---
# 2.3.5. Properties used on satellite delivery systems

## 2.3.5.1. DVB-S delivery system

The following parameters are valid for DVB-S:

- [DTV_API_VERSION](fe_property_parameters.md#dtv-api-version)
- [DTV_DELIVERY_SYSTEM](fe_property_parameters.md#dtv-delivery-system)
- [DTV_TUNE](fe_property_parameters.md#dtv-tune)
- [DTV_CLEAR](fe_property_parameters.md#dtv-clear)
- [DTV_FREQUENCY](fe_property_parameters.md#dtv-frequency)
- [DTV_INVERSION](fe_property_parameters.md#dtv-inversion)
- [DTV_SYMBOL_RATE](fe_property_parameters.md#dtv-symbol-rate)
- [DTV_INNER_FEC](fe_property_parameters.md#dtv-inner-fec)
- [DTV_VOLTAGE](fe_property_parameters.md#dtv-voltage)
- [DTV_TONE](fe_property_parameters.md#dtv-tone)

In addition, the [DTV QoS statistics](frontend-stat-properties.md#frontend-stat-properties)
are also valid.

Future implementations might add those two missing parameters:

- [DTV_DISEQC_MASTER](fe_property_parameters.md#dtv-diseqc-master)
- [DTV_DISEQC_SLAVE_REPLY](fe_property_parameters.md#dtv-diseqc-slave-reply)

## 2.3.5.2. DVB-S2 delivery system

In addition to all parameters valid for DVB-S, DVB-S2 supports the
following parameters:

- [DTV_MODULATION](fe_property_parameters.md#dtv-modulation)
- [DTV_PILOT](fe_property_parameters.md#dtv-pilot)
- [DTV_ROLLOFF](fe_property_parameters.md#dtv-rolloff)
- [DTV_STREAM_ID](fe_property_parameters.md#dtv-stream-id)
- [DTV_SCRAMBLING_SEQUENCE_INDEX](fe_property_parameters.md#dtv-scrambling-sequence-index)

In addition, the [DTV QoS statistics](frontend-stat-properties.md#frontend-stat-properties)
are also valid.

## 2.3.5.3. Turbo code delivery system

In addition to all parameters valid for DVB-S, turbo code supports the
following parameters:

- [DTV_MODULATION](fe_property_parameters.md#dtv-modulation)

## 2.3.5.4. ISDB-S delivery system

The following parameters are valid for ISDB-S:

- [DTV_API_VERSION](fe_property_parameters.md#dtv-api-version)
- [DTV_DELIVERY_SYSTEM](fe_property_parameters.md#dtv-delivery-system)
- [DTV_TUNE](fe_property_parameters.md#dtv-tune)
- [DTV_CLEAR](fe_property_parameters.md#dtv-clear)
- [DTV_FREQUENCY](fe_property_parameters.md#dtv-frequency)
- [DTV_INVERSION](fe_property_parameters.md#dtv-inversion)
- [DTV_SYMBOL_RATE](fe_property_parameters.md#dtv-symbol-rate)
- [DTV_INNER_FEC](fe_property_parameters.md#dtv-inner-fec)
- [DTV_VOLTAGE](fe_property_parameters.md#dtv-voltage)
- [DTV_STREAM_ID](fe_property_parameters.md#dtv-stream-id)
