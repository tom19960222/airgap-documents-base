---
collection: kernel
version: "6.17"
title: "2.13.3. V4L2_META_FMT_GENERIC_8 (‘MET8’), V4L2_META_FMT_GENERIC_CSI2_10 (‘MC1A’), V4L2_META_FMT_GENERIC_CSI2_12 (‘MC1C’), V4L2_META_FMT_GENERIC_CSI2_14 (‘MC1E’), V4L2_META_FMT_GENERIC_CSI2_16 (‘MC1G’), V4L2_META_FMT_GENERIC_CSI2_20 (‘MC1K’), V4L2_META_FMT_GENERIC_CSI2_24 (‘MC1O’)"
source_url: https://www.kernel.org/doc/html/v6.17/userspace-api/media/v4l/metafmt-generic.html
fetched_at: 2026-09-16T16:55:43+00:00
---
# 2.13.3. V4L2_META_FMT_GENERIC_8 (‘MET8’), V4L2_META_FMT_GENERIC_CSI2_10 (‘MC1A’), V4L2_META_FMT_GENERIC_CSI2_12 (‘MC1C’), V4L2_META_FMT_GENERIC_CSI2_14 (‘MC1E’), V4L2_META_FMT_GENERIC_CSI2_16 (‘MC1G’), V4L2_META_FMT_GENERIC_CSI2_20 (‘MC1K’), V4L2_META_FMT_GENERIC_CSI2_24 (‘MC1O’)

Generic line-based metadata formats

## 2.13.3.1. Description

These generic line-based metadata formats define the memory layout of the data
without defining the format or meaning of the metadata itself.

### 2.13.3.1.1. V4L2_META_FMT_GENERIC_8

The V4L2_META_FMT_GENERIC_8 format is a plain 8-bit metadata format. This format
is used on CSI-2 for 8 bits per [Data Unit](../glossary.md#term-Data-Unit).

Additionally it is used for 16 bits per Data Unit when two bytes of metadata are
packed into one 16-bit Data Unit. Otherwise the 16 bits per pixel dataformat is
[V4L2_META_FMT_GENERIC_CSI2_16](metafmt-generic.md#v4l2-meta-fmt-generic-csi2-16).

**Byte Order Of V4L2_META_FMT_GENERIC_8.**
Each cell is one byte. “M” denotes a byte of metadata.

Sample 4x2 Metadata Frame

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| start + 0: | M00 | M10 | M20 | M30 |
| start + 4: | M01 | M11 | M21 | M31 |

### 2.13.3.1.2. V4L2_META_FMT_GENERIC_CSI2_10

V4L2_META_FMT_GENERIC_CSI2_10 contains 8-bit generic metadata packed in 10-bit
Data Units, with one padding byte after every four bytes of metadata. This
format is typically used by CSI-2 receivers with a source that transmits
MEDIA_BUS_FMT_META_10 and the CSI-2 receiver writes the received data to memory
as-is.

The packing of the data follows the MIPI CSI-2 specification and the padding of
the data is defined in the MIPI CCS specification.

This format is also used in conjunction with 20 bits per [Data Unit](../glossary.md#term-Data-Unit)
formats that pack two bytes of metadata into one Data Unit. Otherwise the
20 bits per pixel dataformat is [V4L2_META_FMT_GENERIC_CSI2_20](metafmt-generic.md#v4l2-meta-fmt-generic-csi2-20).

This format is little endian.

**Byte Order Of V4L2_META_FMT_GENERIC_CSI2_10.**
Each cell is one byte. “M” denotes a byte of metadata and “x” a byte of padding.

Sample 4x2 Metadata Frame

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| start + 0: | M00 | M10 | M20 | M30 | x |
| start + 5: | M01 | M11 | M21 | M31 | x |

### 2.13.3.1.3. V4L2_META_FMT_GENERIC_CSI2_12

V4L2_META_FMT_GENERIC_CSI2_12 contains 8-bit generic metadata packed in 12-bit
Data Units, with one padding byte after every two bytes of metadata. This format
is typically used by CSI-2 receivers with a source that transmits
MEDIA_BUS_FMT_META_12 and the CSI-2 receiver writes the received data to memory
as-is.

The packing of the data follows the MIPI CSI-2 specification and the padding of
the data is defined in the MIPI CCS specification.

This format is also used in conjunction with 24 bits per [Data Unit](../glossary.md#term-Data-Unit)
formats that pack two bytes of metadata into one Data Unit. Otherwise the
24 bits per pixel dataformat is [V4L2_META_FMT_GENERIC_CSI2_24](metafmt-generic.md#v4l2-meta-fmt-generic-csi2-24).

This format is little endian.

**Byte Order Of V4L2_META_FMT_GENERIC_CSI2_12.**
Each cell is one byte. “M” denotes a byte of metadata and “x” a byte of padding.

Sample 4x2 Metadata Frame

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| start + 0: | M00 | M10 | x | M20 | M30 | x |
| start + 6: | M01 | M11 | x | M21 | M31 | x |

### 2.13.3.1.4. V4L2_META_FMT_GENERIC_CSI2_14

V4L2_META_FMT_GENERIC_CSI2_14 contains 8-bit generic metadata packed in 14-bit
Data Units, with three padding bytes after every four bytes of metadata. This
format is typically used by CSI-2 receivers with a source that transmits
MEDIA_BUS_FMT_META_14 and the CSI-2 receiver writes the received data to memory
as-is.

The packing of the data follows the MIPI CSI-2 specification and the padding of
the data is defined in the MIPI CCS specification.

This format is little endian.

**Byte Order Of V4L2_META_FMT_GENERIC_CSI2_14.**
Each cell is one byte. “M” denotes a byte of metadata and “x” a byte of padding.

Sample 4x2 Metadata Frame

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| start + 0: | M00 | M10 | M20 | M30 | x | x | x |
| start + 7: | M01 | M11 | M21 | M31 | x | x | x |

### 2.13.3.1.5. V4L2_META_FMT_GENERIC_CSI2_16

V4L2_META_FMT_GENERIC_CSI2_16 contains 8-bit generic metadata packed in 16-bit
Data Units, with one padding byte after every byte of metadata. This format is
typically used by CSI-2 receivers with a source that transmits
MEDIA_BUS_FMT_META_16 and the CSI-2 receiver writes the received data to memory
as-is.

The packing of the data follows the MIPI CSI-2 specification and the padding of
the data is defined in the MIPI CCS specification.

Some devices support more efficient packing of metadata in conjunction with
16-bit image data. In that case the dataformat is
[V4L2_META_FMT_GENERIC_8](metafmt-generic.md#v4l2-meta-fmt-generic-8).

This format is little endian.

**Byte Order Of V4L2_META_FMT_GENERIC_CSI2_16.**
Each cell is one byte. “M” denotes a byte of metadata and “x” a byte of padding.

Sample 4x2 Metadata Frame

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| start + 0: | M00 | x | M10 | x | M20 | x | M30 | x |
| start + 8: | M01 | x | M11 | x | M21 | x | M31 | x |

### 2.13.3.1.6. V4L2_META_FMT_GENERIC_CSI2_20

V4L2_META_FMT_GENERIC_CSI2_20 contains 8-bit generic metadata packed in 20-bit
Data Units, with alternating one or two padding bytes after every byte of
metadata. This format is typically used by CSI-2 receivers with a source that
transmits MEDIA_BUS_FMT_META_20 and the CSI-2 receiver writes the received data
to memory as-is.

The packing of the data follows the MIPI CSI-2 specification and the padding of
the data is defined in the MIPI CCS specification.

Some devices support more efficient packing of metadata in conjunction with
16-bit image data. In that case the dataformat is
[V4L2_META_FMT_GENERIC_CSI2_10](metafmt-generic.md#v4l2-meta-fmt-generic-csi2-10).

This format is little endian.

**Byte Order Of V4L2_META_FMT_GENERIC_CSI2_20.**
Each cell is one byte. “M” denotes a byte of metadata and “x” a byte of padding.

Sample 4x2 Metadata Frame

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| start + 0: | M00 | x | M10 | x | x | M20 | x | M30 | x | x |
| start + 10: | M01 | x | M11 | x | x | M21 | x | M31 | x | x |

### 2.13.3.1.7. V4L2_META_FMT_GENERIC_CSI2_24

V4L2_META_FMT_GENERIC_CSI2_24 contains 8-bit generic metadata packed in 24-bit
Data Units, with two padding bytes after every byte of metadata. This format is
typically used by CSI-2 receivers with a source that transmits
MEDIA_BUS_FMT_META_24 and the CSI-2 receiver writes the received data to memory
as-is.

The packing of the data follows the MIPI CSI-2 specification and the padding of
the data is defined in the MIPI CCS specification.

Some devices support more efficient packing of metadata in conjunction with
16-bit image data. In that case the dataformat is
[V4L2_META_FMT_GENERIC_CSI2_12](metafmt-generic.md#v4l2-meta-fmt-generic-csi2-12).

This format is little endian.

**Byte Order Of V4L2_META_FMT_GENERIC_CSI2_24.**
Each cell is one byte. “M” denotes a byte of metadata and “x” a byte of padding.

Sample 4x2 Metadata Frame

|  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| start + 0: | M00 | x | x | M10 | x | x | M20 | x | x | M30 | x | x |
| start + 12: | M01 | x | x | M11 | x | x | M21 | x | x | M31 | x | x |
