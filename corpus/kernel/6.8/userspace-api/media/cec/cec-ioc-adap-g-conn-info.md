---
collection: kernel
version: "6.8"
title: "2.8. ioctl CEC_ADAP_G_CONNECTOR_INFO"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/cec/cec-ioc-adap-g-conn-info.html
fetched_at: 2026-08-21T03:38:47+00:00
---
# 2.8. ioctl CEC_ADAP_G_CONNECTOR_INFO

## 2.8.1. Name

CEC_ADAP_G_CONNECTOR_INFO - Query HDMI connector information

## 2.8.2. Synopsis

CEC_ADAP_G_CONNECTOR_INFO

`int ioctl(int fd, CEC_ADAP_G_CONNECTOR_INFO, struct cec_connector_info *argp)`

## 2.8.3. Arguments

`fd`
:   File descriptor returned by [`open()`](cec-func-open.md#c.CEC.open "open").

`argp`

## 2.8.4. Description

Using this ioctl an application can learn which HDMI connector this CEC
device corresponds to. While calling this ioctl the application should
provide a pointer to a cec_connector_info struct which will be populated
by the kernel with the info provided by the adapter's driver. This ioctl
is only available if the `CEC_CAP_CONNECTOR_INFO` capability is set.

type cec_connector_info

struct cec_connector_info

|  |  |  |
| --- | --- | --- |
| __u32 | `type` | The type of connector this adapter is associated with. |
| union { | `(anonymous)` | |
| `struct cec_drm_connector_info` | drm | [struct cec_drm_connector_info](cec-ioc-adap-g-conn-info.md#cec-drm-connector-info) |
| } |  | |

Connector types

|  |  |  |
| --- | --- | --- |
| `CEC_CONNECTOR_TYPE_NO_CONNECTOR` | 0 | No connector is associated with the adapter/the information is not provided by the driver. |
| `CEC_CONNECTOR_TYPE_DRM` | 1 | Indicates that a DRM connector is associated with this adapter. Information about the connector can be found in [struct cec_drm_connector_info](cec-ioc-adap-g-conn-info.md#cec-drm-connector-info). |

type cec_drm_connector_info

struct cec_drm_connector_info

|  |  |  |
| --- | --- | --- |
| __u32 | `card_no` | DRM card number: the number from a card's path, e.g. 0 in case of /dev/card0. |
| __u32 | `connector_id` | DRM connector ID. |
