---
collection: kernel
version: "6.8"
title: "6.1.1.1. Frontend type"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/dvb/fe-type-t.html
fetched_at: 2026-08-21T03:39:42+00:00
---
# 6.1.1.1. Frontend type

For historical reasons, frontend types are named by the type of
modulation used in transmission. The fontend types are given by
fe_type_t type, defined as:

type fe_type

Frontend types

| fe_type | Description | [DTV_DELIVERY_SYSTEM](fe_property_parameters.md#dtv-delivery-system) equivalent type |
| --- | --- | --- |
| `FE_QPSK` | For DVB-S standard | `SYS_DVBS` |
| `FE_QAM` | For DVB-C annex A standard | `SYS_DVBC_ANNEX_A` |
| `FE_OFDM` | For DVB-T standard | `SYS_DVBT` |
| `FE_ATSC` | For ATSC standard (terrestrial) or for DVB-C Annex B (cable) used in US. | `SYS_ATSC` (terrestrial) or `SYS_DVBC_ANNEX_B` (cable) |

Newer formats like DVB-S2, ISDB-T, ISDB-S and DVB-T2 are not described
at the above, as they're supported via the new
[FE_GET_PROPERTY/FE_GET_SET_PROPERTY](fe-get-property.md#fe-get-property)
ioctl's, using the [DTV_DELIVERY_SYSTEM](fe_property_parameters.md#dtv-delivery-system)
parameter.

In the old days, struct [`dvb_frontend_info`](frontend-header.md#c.dvb_frontend_info "dvb_frontend_info")
used to contain `fe_type_t` field to indicate the delivery systems,
filled with either `FE_QPSK, FE_QAM, FE_OFDM` or `FE_ATSC`. While this
is still filled to keep backward compatibility, the usage of this field
is deprecated, as it can report just one delivery system, but some
devices support multiple delivery systems. Please use
[DTV_ENUM_DELSYS](fe_property_parameters.md#dtv-enum-delsys) instead.

On devices that support multiple delivery systems, struct
[`dvb_frontend_info`](frontend-header.md#c.dvb_frontend_info "dvb_frontend_info")::`fe_type_t` is
filled with the currently standard, as selected by the last call to
[FE_SET_PROPERTY](fe-get-property.md#fe-get-property) using the
[DTV_DELIVERY_SYSTEM](fe_property_parameters.md#dtv-delivery-system) property.
