---
collection: kernel
version: "6.8"
title: "7.40. ioctl VIDIOC_G_SLICED_VBI_CAP"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/vidioc-g-sliced-vbi-cap.html
fetched_at: 2026-08-21T03:40:52+00:00
---
# 7.40. ioctl VIDIOC_G_SLICED_VBI_CAP

## 7.40.1. Name

VIDIOC_G_SLICED_VBI_CAP - Query sliced VBI capabilities

## 7.40.2. Synopsis

VIDIOC_G_SLICED_VBI_CAP

`int ioctl(int fd, VIDIOC_G_SLICED_VBI_CAP, struct v4l2_sliced_vbi_cap *argp)`

## 7.40.3. Arguments

`fd`
:   File descriptor returned by [`open()`](func-open.md#c.V4L.open "open").

`argp`
:   Pointer to struct [`v4l2_sliced_vbi_cap`](vidioc-g-sliced-vbi-cap.md#c.V4L.v4l2_sliced_vbi_cap "v4l2_sliced_vbi_cap").

## 7.40.4. Description

To find out which data services are supported by a sliced VBI capture or
output device, applications initialize the `type` field of a struct
[`v4l2_sliced_vbi_cap`](vidioc-g-sliced-vbi-cap.md#c.V4L.v4l2_sliced_vbi_cap "v4l2_sliced_vbi_cap"), clear the
`reserved` array and call the [VIDIOC_G_SLICED_VBI_CAP](vidioc-g-sliced-vbi-cap.md#vidioc-g-sliced-vbi-cap) ioctl. The
driver fills in the remaining fields or returns an `EINVAL` error code if
the sliced VBI API is unsupported or `type` is invalid.

> **Note:**
>
> The `type` field was added, and the ioctl changed from read-only
> to write-read, in Linux 2.6.19.

type v4l2_sliced_vbi_cap

struct v4l2_sliced_vbi_cap

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __u16 | `service_set` | A set of all data services supported by the driver.  Equal to the union of all elements of the `service_lines` array. | | |
| __u16 | `service_lines`[2][24] | Each element of this array contains a set of data services the hardware can look for or insert into a particular scan line. Data services are defined in [Sliced VBI services](vidioc-g-sliced-vbi-cap.md#vbi-services). Array indices map to ITU-R line numbers[1](vidioc-g-sliced-vbi-cap.md#f1) as follows: | | |
|  |  | Element | 525 line systems | 625 line systems |
|  |  | `service_lines`[0][1] | 1 | 1 |
|  |  | `service_lines`[0][23] | 23 | 23 |
|  |  | `service_lines`[1][1] | 264 | 314 |
|  |  | `service_lines`[1][23] | 286 | 336 |
|  | | | | |
|  |  | The number of VBI lines the hardware can capture or output per frame, or the number of services it can identify on a given line may be limited. For example on PAL line 16 the hardware may be able to look for a VPS or Teletext signal, but not both at the same time. Applications can learn about these limits using the [VIDIOC_S_FMT](vidioc-g-fmt.md#vidioc-g-fmt) ioctl as described in [Sliced VBI Data Interface](dev-sliced-vbi.md#sliced). | | |
|  | | | | |
|  |  | Drivers must set `service_lines` [0][0] and `service_lines`[1][0] to zero. | | |
| __u32 | `type` | Type of the data stream, see [`v4l2_buf_type`](buffer.md#c.V4L.v4l2_buf_type "v4l2_buf_type"). Should be `V4L2_BUF_TYPE_SLICED_VBI_CAPTURE` or `V4L2_BUF_TYPE_SLICED_VBI_OUTPUT`. | | |
| __u32 | `reserved`[3] | This array is reserved for future extensions.  Applications and drivers must set it to zero. | | |

[1](vidioc-g-sliced-vbi-cap.md#id1)
:   See also [Figure 4.2. ITU-R 525 line numbering (M/NTSC and M/PAL)](dev-raw-vbi.md#vbi-525) and [Figure 4.3. ITU-R 625 line numbering](dev-raw-vbi.md#vbi-625).

Sliced VBI services

| Symbol | Value | Reference | Lines, usually | Payload |
| --- | --- | --- | --- | --- |
| `V4L2_SLICED_TELETEXT_B` (Teletext System B) | 0x0001 | [ETS 300 706](biblio.md#ets300706),  [ITU BT.653](biblio.md#itu653) | PAL/SECAM line 7-22, 320-335 (second field 7-22) | Last 42 of the 45 byte Teletext packet, that is without clock run-in and framing code, lsb first transmitted. |
| `V4L2_SLICED_VPS` | 0x0400 | [ETS 300 231](biblio.md#ets300231) | PAL line 16 | Byte number 3 to 15 according to Figure 9 of ETS 300 231, lsb first transmitted. |
| `V4L2_SLICED_CAPTION_525` | 0x1000 | [CEA 608-E](biblio.md#cea608) | NTSC line 21, 284 (second field 21) | Two bytes in transmission order, including parity bit, lsb first transmitted. |
| `V4L2_SLICED_WSS_625` | 0x4000 | [EN 300 294](biblio.md#en300294),  [ITU BT.1119](biblio.md#itu1119) | PAL/SECAM line 23 | See [V4L2_SLICED_VBI_CAP WSS_625 payload](vidioc-g-sliced-vbi-cap.md#v4l2-sliced-vbi-cap-wss-625-payload) below. |
| `V4L2_SLICED_VBI_525` | 0x1000 | Set of services applicable to 525 line systems. | | |
| `V4L2_SLICED_VBI_625` | 0x4401 | Set of services applicable to 625 line systems. | | |

### 7.40.4.1. V4L2_SLICED_VBI_CAP WSS_625 payload

The payload for `V4L2_SLICED_WSS_625` is:

> |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
> | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
> | Byte | 0 | | | | | | | | 1 | | | | | | | |
> | Bit | msb | | | | lsb | | | | msb | | | | lsb | | | |
> | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 | x | x | 13 | 12 | 11 | 10 | 9 | 8 |

## 7.40.5. Return Value

On success 0 is returned, on error -1 and the `errno` variable is set
appropriately. The generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

EINVAL
:   The value in the `type` field is wrong.
