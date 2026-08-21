---
collection: kernel
version: "6.8"
title: "2.3.3. Properties used on terrestrial delivery systems"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/dvb/frontend-property-terrestrial-systems.html
fetched_at: 2026-08-21T03:57:49+00:00
---
# 2.3.3. Properties used on terrestrial delivery systems

## 2.3.3.1. DVB-T delivery system

The following parameters are valid for DVB-T:

- [DTV_API_VERSION](fe_property_parameters.md#dtv-api-version)
- [DTV_DELIVERY_SYSTEM](fe_property_parameters.md#dtv-delivery-system)
- [DTV_TUNE](fe_property_parameters.md#dtv-tune)
- [DTV_CLEAR](fe_property_parameters.md#dtv-clear)
- [DTV_FREQUENCY](fe_property_parameters.md#dtv-frequency)
- [DTV_MODULATION](fe_property_parameters.md#dtv-modulation)
- [DTV_BANDWIDTH_HZ](fe_property_parameters.md#dtv-bandwidth-hz)
- [DTV_INVERSION](fe_property_parameters.md#dtv-inversion)
- [DTV_CODE_RATE_HP](fe_property_parameters.md#dtv-code-rate-hp)
- [DTV_CODE_RATE_LP](fe_property_parameters.md#dtv-code-rate-lp)
- [DTV_GUARD_INTERVAL](fe_property_parameters.md#dtv-guard-interval)
- [DTV_TRANSMISSION_MODE](fe_property_parameters.md#dtv-transmission-mode)
- [DTV_HIERARCHY](fe_property_parameters.md#dtv-hierarchy)
- [DTV_LNA](fe_property_parameters.md#dtv-lna)

In addition, the [DTV QoS statistics](frontend-stat-properties.md#frontend-stat-properties)
are also valid.

## 2.3.3.2. DVB-T2 delivery system

DVB-T2 support is currently in the early stages of development, so
expect that this section maygrow and become more detailed with time.

The following parameters are valid for DVB-T2:

- [DTV_API_VERSION](fe_property_parameters.md#dtv-api-version)
- [DTV_DELIVERY_SYSTEM](fe_property_parameters.md#dtv-delivery-system)
- [DTV_TUNE](fe_property_parameters.md#dtv-tune)
- [DTV_CLEAR](fe_property_parameters.md#dtv-clear)
- [DTV_FREQUENCY](fe_property_parameters.md#dtv-frequency)
- [DTV_MODULATION](fe_property_parameters.md#dtv-modulation)
- [DTV_BANDWIDTH_HZ](fe_property_parameters.md#dtv-bandwidth-hz)
- [DTV_INVERSION](fe_property_parameters.md#dtv-inversion)
- [DTV_CODE_RATE_HP](fe_property_parameters.md#dtv-code-rate-hp)
- [DTV_CODE_RATE_LP](fe_property_parameters.md#dtv-code-rate-lp)
- [DTV_GUARD_INTERVAL](fe_property_parameters.md#dtv-guard-interval)
- [DTV_TRANSMISSION_MODE](fe_property_parameters.md#dtv-transmission-mode)
- [DTV_HIERARCHY](fe_property_parameters.md#dtv-hierarchy)
- [DTV_STREAM_ID](fe_property_parameters.md#dtv-stream-id)
- [DTV_LNA](fe_property_parameters.md#dtv-lna)

In addition, the [DTV QoS statistics](frontend-stat-properties.md#frontend-stat-properties)
are also valid.

## 2.3.3.3. ISDB-T delivery system

This ISDB-T/ISDB-Tsb API extension should reflect all information needed
to tune any ISDB-T/ISDB-Tsb hardware. Of course it is possible that some
very sophisticated devices won't need certain parameters to tune.

The information given here should help application writers to know how
to handle ISDB-T and ISDB-Tsb hardware using the Linux Digital TV API.

The details given here about ISDB-T and ISDB-Tsb are just enough to
basically show the dependencies between the needed parameter values, but
surely some information is left out. For more detailed information see
the following documents:

ARIB STD-B31 - "Transmission System for Digital Terrestrial Television
Broadcasting" and

ARIB TR-B14 - "Operational Guidelines for Digital Terrestrial Television
Broadcasting".

In order to understand the ISDB specific parameters, one has to have
some knowledge the channel structure in ISDB-T and ISDB-Tsb. I.e. it has
to be known to the reader that an ISDB-T channel consists of 13
segments, that it can have up to 3 layer sharing those segments, and
things like that.

The following parameters are valid for ISDB-T:

- [DTV_API_VERSION](fe_property_parameters.md#dtv-api-version)
- [DTV_DELIVERY_SYSTEM](fe_property_parameters.md#dtv-delivery-system)
- [DTV_TUNE](fe_property_parameters.md#dtv-tune)
- [DTV_CLEAR](fe_property_parameters.md#dtv-clear)
- [DTV_FREQUENCY](fe_property_parameters.md#dtv-frequency)
- [DTV_BANDWIDTH_HZ](fe_property_parameters.md#dtv-bandwidth-hz)
- [DTV_INVERSION](fe_property_parameters.md#dtv-inversion)
- [DTV_GUARD_INTERVAL](fe_property_parameters.md#dtv-guard-interval)
- [DTV_TRANSMISSION_MODE](fe_property_parameters.md#dtv-transmission-mode)
- [DTV_ISDBT_LAYER_ENABLED](fe_property_parameters.md#dtv-isdbt-layer-enabled)
- [DTV_ISDBT_PARTIAL_RECEPTION](fe_property_parameters.md#dtv-isdbt-partial-reception)
- [DTV_ISDBT_SOUND_BROADCASTING](fe_property_parameters.md#dtv-isdbt-sound-broadcasting)
- [DTV_ISDBT_SB_SUBCHANNEL_ID](fe_property_parameters.md#dtv-isdbt-sb-subchannel-id)
- [DTV_ISDBT_SB_SEGMENT_IDX](fe_property_parameters.md#dtv-isdbt-sb-segment-idx)
- [DTV_ISDBT_SB_SEGMENT_COUNT](fe_property_parameters.md#dtv-isdbt-sb-segment-count)
- [DTV_ISDBT_LAYERA_FEC](fe_property_parameters.md#dtv-isdbt-layer-fec)
- [DTV_ISDBT_LAYERA_MODULATION](fe_property_parameters.md#dtv-isdbt-layer-modulation)
- [DTV_ISDBT_LAYERA_SEGMENT_COUNT](fe_property_parameters.md#dtv-isdbt-layer-segment-count)
- [DTV_ISDBT_LAYERA_TIME_INTERLEAVING](fe_property_parameters.md#dtv-isdbt-layer-time-interleaving)
- [DTV_ISDBT_LAYERB_FEC](fe_property_parameters.md#dtv-isdbt-layer-fec)
- [DTV_ISDBT_LAYERB_MODULATION](fe_property_parameters.md#dtv-isdbt-layer-modulation)
- [DTV_ISDBT_LAYERB_SEGMENT_COUNT](fe_property_parameters.md#dtv-isdbt-layer-segment-count)
- [DTV_ISDBT_LAYERB_TIME_INTERLEAVING](fe_property_parameters.md#dtv-isdbt-layer-time-interleaving)
- [DTV_ISDBT_LAYERC_FEC](fe_property_parameters.md#dtv-isdbt-layer-fec)
- [DTV_ISDBT_LAYERC_MODULATION](fe_property_parameters.md#dtv-isdbt-layer-modulation)
- [DTV_ISDBT_LAYERC_SEGMENT_COUNT](fe_property_parameters.md#dtv-isdbt-layer-segment-count)
- [DTV_ISDBT_LAYERC_TIME_INTERLEAVING](fe_property_parameters.md#dtv-isdbt-layer-time-interleaving)

In addition, the [DTV QoS statistics](frontend-stat-properties.md#frontend-stat-properties)
are also valid.

## 2.3.3.4. ATSC delivery system

The following parameters are valid for ATSC:

- [DTV_API_VERSION](fe_property_parameters.md#dtv-api-version)
- [DTV_DELIVERY_SYSTEM](fe_property_parameters.md#dtv-delivery-system)
- [DTV_TUNE](fe_property_parameters.md#dtv-tune)
- [DTV_CLEAR](fe_property_parameters.md#dtv-clear)
- [DTV_FREQUENCY](fe_property_parameters.md#dtv-frequency)
- [DTV_MODULATION](fe_property_parameters.md#dtv-modulation)
- [DTV_BANDWIDTH_HZ](fe_property_parameters.md#dtv-bandwidth-hz)

In addition, the [DTV QoS statistics](frontend-stat-properties.md#frontend-stat-properties)
are also valid.

## 2.3.3.5. ATSC-MH delivery system

The following parameters are valid for ATSC-MH:

- [DTV_API_VERSION](fe_property_parameters.md#dtv-api-version)
- [DTV_DELIVERY_SYSTEM](fe_property_parameters.md#dtv-delivery-system)
- [DTV_TUNE](fe_property_parameters.md#dtv-tune)
- [DTV_CLEAR](fe_property_parameters.md#dtv-clear)
- [DTV_FREQUENCY](fe_property_parameters.md#dtv-frequency)
- [DTV_BANDWIDTH_HZ](fe_property_parameters.md#dtv-bandwidth-hz)
- [DTV_ATSCMH_FIC_VER](fe_property_parameters.md#dtv-atscmh-fic-ver)
- [DTV_ATSCMH_PARADE_ID](fe_property_parameters.md#dtv-atscmh-parade-id)
- [DTV_ATSCMH_NOG](fe_property_parameters.md#dtv-atscmh-nog)
- [DTV_ATSCMH_TNOG](fe_property_parameters.md#dtv-atscmh-tnog)
- [DTV_ATSCMH_SGN](fe_property_parameters.md#dtv-atscmh-sgn)
- [DTV_ATSCMH_PRC](fe_property_parameters.md#dtv-atscmh-prc)
- [DTV_ATSCMH_RS_FRAME_MODE](fe_property_parameters.md#dtv-atscmh-rs-frame-mode)
- [DTV_ATSCMH_RS_FRAME_ENSEMBLE](fe_property_parameters.md#dtv-atscmh-rs-frame-ensemble)
- [DTV_ATSCMH_RS_CODE_MODE_PRI](fe_property_parameters.md#dtv-atscmh-rs-code-mode-pri)
- [DTV_ATSCMH_RS_CODE_MODE_SEC](fe_property_parameters.md#dtv-atscmh-rs-code-mode-sec)
- [DTV_ATSCMH_SCCC_BLOCK_MODE](fe_property_parameters.md#dtv-atscmh-sccc-block-mode)
- [DTV_ATSCMH_SCCC_CODE_MODE_A](fe_property_parameters.md#dtv-atscmh-sccc-code-mode-a)
- [DTV_ATSCMH_SCCC_CODE_MODE_B](fe_property_parameters.md#dtv-atscmh-sccc-code-mode-b)
- [DTV_ATSCMH_SCCC_CODE_MODE_C](fe_property_parameters.md#dtv-atscmh-sccc-code-mode-c)
- [DTV_ATSCMH_SCCC_CODE_MODE_D](fe_property_parameters.md#dtv-atscmh-sccc-code-mode-d)

In addition, the [DTV QoS statistics](frontend-stat-properties.md#frontend-stat-properties)
are also valid.

## 2.3.3.6. DTMB delivery system

The following parameters are valid for DTMB:

- [DTV_API_VERSION](fe_property_parameters.md#dtv-api-version)
- [DTV_DELIVERY_SYSTEM](fe_property_parameters.md#dtv-delivery-system)
- [DTV_TUNE](fe_property_parameters.md#dtv-tune)
- [DTV_CLEAR](fe_property_parameters.md#dtv-clear)
- [DTV_FREQUENCY](fe_property_parameters.md#dtv-frequency)
- [DTV_MODULATION](fe_property_parameters.md#dtv-modulation)
- [DTV_BANDWIDTH_HZ](fe_property_parameters.md#dtv-bandwidth-hz)
- [DTV_INVERSION](fe_property_parameters.md#dtv-inversion)
- [DTV_INNER_FEC](fe_property_parameters.md#dtv-inner-fec)
- [DTV_GUARD_INTERVAL](fe_property_parameters.md#dtv-guard-interval)
- [DTV_TRANSMISSION_MODE](fe_property_parameters.md#dtv-transmission-mode)
- [DTV_INTERLEAVING](fe_property_parameters.md#dtv-interleaving)
- [DTV_LNA](fe_property_parameters.md#dtv-lna)

In addition, the [DTV QoS statistics](frontend-stat-properties.md#frontend-stat-properties)
are also valid.
