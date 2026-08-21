---
collection: kernel
version: "6.8"
title: "2.20. V4L2 Media Bus functions and data structures"
source_url: https://www.kernel.org/doc/html/v6.8/driver-api/media/v4l2-mediabus.html
fetched_at: 2026-08-21T03:41:16+00:00
---
# 2.20. V4L2 Media Bus functions and data structures

struct v4l2_mbus_config_mipi_csi2
:   MIPI CSI-2 data bus configuration

**Definition**:

```
struct v4l2_mbus_config_mipi_csi2 {
    unsigned int flags;
    unsigned char data_lanes[V4L2_MBUS_CSI2_MAX_DATA_LANES];
    unsigned char clock_lane;
    unsigned char num_data_lanes;
    bool lane_polarities[1 + V4L2_MBUS_CSI2_MAX_DATA_LANES];
};
```

**Members**

`flags`
:   media bus (V4L2_MBUS_\*) flags

`data_lanes`
:   an array of physical data lane indexes

`clock_lane`
:   physical lane index of the clock lane

`num_data_lanes`
:   number of data lanes

`lane_polarities`
:   polarity of the lanes. The order is the same of
    the physical lanes.

struct v4l2_mbus_config_parallel
:   parallel data bus configuration

**Definition**:

```
struct v4l2_mbus_config_parallel {
    unsigned int flags;
    unsigned char bus_width;
    unsigned char data_shift;
};
```

**Members**

`flags`
:   media bus (V4L2_MBUS_\*) flags

`bus_width`
:   bus width in bits

`data_shift`
:   data shift in bits

struct v4l2_mbus_config_mipi_csi1
:   CSI-1/CCP2 data bus configuration

**Definition**:

```
struct v4l2_mbus_config_mipi_csi1 {
    unsigned char clock_inv:1;
    unsigned char strobe:1;
    bool lane_polarity[2];
    unsigned char data_lane;
    unsigned char clock_lane;
};
```

**Members**

`clock_inv`
:   polarity of clock/strobe signal
    false - not inverted, true - inverted

`strobe`
:   false - data/clock, true - data/strobe

`lane_polarity`
:   the polarities of the clock (index 0) and data lanes
    index (1)

`data_lane`
:   the number of the data lane

`clock_lane`
:   the number of the clock lane

enum v4l2_mbus_type
:   media bus type

**Constants**

`V4L2_MBUS_UNKNOWN`
:   unknown bus type, no V4L2 mediabus configuration

`V4L2_MBUS_PARALLEL`
:   parallel interface with hsync and vsync

`V4L2_MBUS_BT656`
:   parallel interface with embedded synchronisation, can
    also be used for BT.1120

`V4L2_MBUS_CSI1`
:   MIPI CSI-1 serial interface

`V4L2_MBUS_CCP2`
:   CCP2 (Compact Camera Port 2)

`V4L2_MBUS_CSI2_DPHY`
:   MIPI CSI-2 serial interface, with D-PHY

`V4L2_MBUS_CSI2_CPHY`
:   MIPI CSI-2 serial interface, with C-PHY

`V4L2_MBUS_DPI`
:   MIPI VIDEO DPI interface

`V4L2_MBUS_INVALID`
:   invalid bus type (keep as last)

struct v4l2_mbus_config
:   media bus configuration

**Definition**:

```
struct v4l2_mbus_config {
    enum v4l2_mbus_type type;
    union {
        struct v4l2_mbus_config_parallel parallel;
        struct v4l2_mbus_config_mipi_csi1 mipi_csi1;
        struct v4l2_mbus_config_mipi_csi2 mipi_csi2;
    } bus;
};
```

**Members**

`type`
:   interface type

`bus`
:   bus configuration data structure

`bus.parallel`
:   embedded [`struct v4l2_mbus_config_parallel`](v4l2-mediabus.md#c.v4l2_mbus_config_parallel "v4l2_mbus_config_parallel").
    Used if the bus is parallel or BT.656.

`bus.mipi_csi1`
:   embedded [`struct v4l2_mbus_config_mipi_csi1`](v4l2-mediabus.md#c.v4l2_mbus_config_mipi_csi1 "v4l2_mbus_config_mipi_csi1").
    Used if the bus is MIPI Alliance's Camera Serial
    Interface version 1 (MIPI CSI1) or Standard
    Mobile Imaging Architecture's Compact Camera Port 2
    (SMIA CCP2).

`bus.mipi_csi2`
:   embedded [`struct v4l2_mbus_config_mipi_csi2`](v4l2-mediabus.md#c.v4l2_mbus_config_mipi_csi2 "v4l2_mbus_config_mipi_csi2").
    Used if the bus is MIPI Alliance's Camera Serial
    Interface version 2 (MIPI CSI2).

void v4l2_fill_pix_format(struct [v4l2_pix_format](../../userspace-api/media/v4l/pixfmt-v4l2.md#c.v4l2_pix_format "v4l2_pix_format") \*pix_fmt, const struct [v4l2_mbus_framefmt](../../userspace-api/media/v4l/subdev-formats.md#c.v4l2_mbus_framefmt "v4l2_mbus_framefmt") \*mbus_fmt)
:   Ancillary routine that fills a [`struct v4l2_pix_format`](../../userspace-api/media/v4l/pixfmt-v4l2.md#c.v4l2_pix_format "v4l2_pix_format") fields from a [`struct v4l2_mbus_framefmt`](../../userspace-api/media/v4l/subdev-formats.md#c.v4l2_mbus_framefmt "v4l2_mbus_framefmt").

**Parameters**

`struct v4l2_pix_format *pix_fmt`
:   pointer to [`struct v4l2_pix_format`](../../userspace-api/media/v4l/pixfmt-v4l2.md#c.v4l2_pix_format "v4l2_pix_format") to be filled

`const struct v4l2_mbus_framefmt *mbus_fmt`
:   pointer to [`struct v4l2_mbus_framefmt`](../../userspace-api/media/v4l/subdev-formats.md#c.v4l2_mbus_framefmt "v4l2_mbus_framefmt") to be used as model

void v4l2_fill_mbus_format(struct [v4l2_mbus_framefmt](../../userspace-api/media/v4l/subdev-formats.md#c.v4l2_mbus_framefmt "v4l2_mbus_framefmt") \*mbus_fmt, const struct [v4l2_pix_format](../../userspace-api/media/v4l/pixfmt-v4l2.md#c.v4l2_pix_format "v4l2_pix_format") \*pix_fmt, u32 code)
:   Ancillary routine that fills a [`struct v4l2_mbus_framefmt`](../../userspace-api/media/v4l/subdev-formats.md#c.v4l2_mbus_framefmt "v4l2_mbus_framefmt") from a [`struct v4l2_pix_format`](../../userspace-api/media/v4l/pixfmt-v4l2.md#c.v4l2_pix_format "v4l2_pix_format") and a data format code.

**Parameters**

`struct v4l2_mbus_framefmt *mbus_fmt`
:   pointer to [`struct v4l2_mbus_framefmt`](../../userspace-api/media/v4l/subdev-formats.md#c.v4l2_mbus_framefmt "v4l2_mbus_framefmt") to be filled

`const struct v4l2_pix_format *pix_fmt`
:   pointer to [`struct v4l2_pix_format`](../../userspace-api/media/v4l/pixfmt-v4l2.md#c.v4l2_pix_format "v4l2_pix_format") to be used as model

`u32 code`
:   data format code (from `enum v4l2_mbus_pixelcode`)

void v4l2_fill_pix_format_mplane(struct [v4l2_pix_format_mplane](../../userspace-api/media/v4l/pixfmt-v4l2-mplane.md#c.v4l2_pix_format_mplane "v4l2_pix_format_mplane") \*pix_mp_fmt, const struct [v4l2_mbus_framefmt](../../userspace-api/media/v4l/subdev-formats.md#c.v4l2_mbus_framefmt "v4l2_mbus_framefmt") \*mbus_fmt)
:   Ancillary routine that fills a [`struct v4l2_pix_format_mplane`](../../userspace-api/media/v4l/pixfmt-v4l2-mplane.md#c.v4l2_pix_format_mplane "v4l2_pix_format_mplane") fields from a media bus structure.

**Parameters**

`struct v4l2_pix_format_mplane *pix_mp_fmt`
:   pointer to [`struct v4l2_pix_format_mplane`](../../userspace-api/media/v4l/pixfmt-v4l2-mplane.md#c.v4l2_pix_format_mplane "v4l2_pix_format_mplane") to be filled

`const struct v4l2_mbus_framefmt *mbus_fmt`
:   pointer to [`struct v4l2_mbus_framefmt`](../../userspace-api/media/v4l/subdev-formats.md#c.v4l2_mbus_framefmt "v4l2_mbus_framefmt") to be used as model

void v4l2_fill_mbus_format_mplane(struct [v4l2_mbus_framefmt](../../userspace-api/media/v4l/subdev-formats.md#c.v4l2_mbus_framefmt "v4l2_mbus_framefmt") \*mbus_fmt, const struct [v4l2_pix_format_mplane](../../userspace-api/media/v4l/pixfmt-v4l2-mplane.md#c.v4l2_pix_format_mplane "v4l2_pix_format_mplane") \*pix_mp_fmt)
:   Ancillary routine that fills a [`struct v4l2_mbus_framefmt`](../../userspace-api/media/v4l/subdev-formats.md#c.v4l2_mbus_framefmt "v4l2_mbus_framefmt") from a [`struct v4l2_pix_format_mplane`](../../userspace-api/media/v4l/pixfmt-v4l2-mplane.md#c.v4l2_pix_format_mplane "v4l2_pix_format_mplane").

**Parameters**

`struct v4l2_mbus_framefmt *mbus_fmt`
:   pointer to [`struct v4l2_mbus_framefmt`](../../userspace-api/media/v4l/subdev-formats.md#c.v4l2_mbus_framefmt "v4l2_mbus_framefmt") to be filled

`const struct v4l2_pix_format_mplane *pix_mp_fmt`
:   pointer to [`struct v4l2_pix_format_mplane`](../../userspace-api/media/v4l/pixfmt-v4l2-mplane.md#c.v4l2_pix_format_mplane "v4l2_pix_format_mplane") to be used as model
