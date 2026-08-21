---
collection: kernel
version: "6.8"
title: "7.53. ioctl VIDIOC_S_HW_FREQ_SEEK"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/vidioc-s-hw-freq-seek.html
fetched_at: 2026-08-21T03:40:46+00:00
---
# 7.53. ioctl VIDIOC_S_HW_FREQ_SEEK

## 7.53.1. Name

VIDIOC_S_HW_FREQ_SEEK - Perform a hardware frequency seek

## 7.53.2. Synopsis

VIDIOC_S_HW_FREQ_SEEK

`int ioctl(int fd, VIDIOC_S_HW_FREQ_SEEK, struct v4l2_hw_freq_seek *argp)`

## 7.53.3. Arguments

`fd`
:   File descriptor returned by [`open()`](func-open.md#c.V4L.open "open").

`argp`
:   Pointer to struct [`v4l2_hw_freq_seek`](vidioc-s-hw-freq-seek.md#c.V4L.v4l2_hw_freq_seek "v4l2_hw_freq_seek").

## 7.53.4. Description

Start a hardware frequency seek from the current frequency. To do this
applications initialize the `tuner`, `type`, `seek_upward`,
`wrap_around`, `spacing`, `rangelow` and `rangehigh` fields, and
zero out the `reserved` array of a struct
[`v4l2_hw_freq_seek`](vidioc-s-hw-freq-seek.md#c.V4L.v4l2_hw_freq_seek "v4l2_hw_freq_seek") and call the
`VIDIOC_S_HW_FREQ_SEEK` ioctl with a pointer to this structure.

The `rangelow` and `rangehigh` fields can be set to a non-zero value
to tell the driver to search a specific band. If the struct
[`v4l2_tuner`](vidioc-g-tuner.md#c.V4L.v4l2_tuner "v4l2_tuner") `capability` field has the
`V4L2_TUNER_CAP_HWSEEK_PROG_LIM` flag set, these values must fall
within one of the bands returned by
[ioctl VIDIOC_ENUM_FREQ_BANDS](vidioc-enum-freq-bands.md#vidioc-enum-freq-bands). If the
`V4L2_TUNER_CAP_HWSEEK_PROG_LIM` flag is not set, then these values
must exactly match those of one of the bands returned by
[ioctl VIDIOC_ENUM_FREQ_BANDS](vidioc-enum-freq-bands.md#vidioc-enum-freq-bands). If the
current frequency of the tuner does not fall within the selected band it
will be clamped to fit in the band before the seek is started.

If an error is returned, then the original frequency will be restored.

This ioctl is supported if the `V4L2_CAP_HW_FREQ_SEEK` capability is
set.

If this ioctl is called from a non-blocking filehandle, then `EAGAIN`
error code is returned and no seek takes place.

type v4l2_hw_freq_seek

struct v4l2_hw_freq_seek

|  |  |  |
| --- | --- | --- |
| __u32 | `tuner` | The tuner index number. This is the same value as in the struct [`v4l2_input`](vidioc-enuminput.md#c.V4L.v4l2_input "v4l2_input") `tuner` field and the struct [`v4l2_tuner`](vidioc-g-tuner.md#c.V4L.v4l2_tuner "v4l2_tuner") `index` field. |
| __u32 | `type` | The tuner type. This is the same value as in the struct [`v4l2_tuner`](vidioc-g-tuner.md#c.V4L.v4l2_tuner "v4l2_tuner") `type` field. See [`v4l2_tuner_type`](vidioc-g-tuner.md#c.V4L.v4l2_tuner_type "v4l2_tuner_type") |
| __u32 | `seek_upward` | If non-zero, seek upward from the current frequency, else seek downward. |
| __u32 | `wrap_around` | If non-zero, wrap around when at the end of the frequency range, else stop seeking. The struct [`v4l2_tuner`](vidioc-g-tuner.md#c.V4L.v4l2_tuner "v4l2_tuner") `capability` field will tell you what the hardware supports. |
| __u32 | `spacing` | If non-zero, defines the hardware seek resolution in Hz. The driver selects the nearest value that is supported by the device. If spacing is zero a reasonable default value is used. |
| __u32 | `rangelow` | If non-zero, the lowest tunable frequency of the band to search in units of 62.5 kHz, or if the struct [`v4l2_tuner`](vidioc-g-tuner.md#c.V4L.v4l2_tuner "v4l2_tuner") `capability` field has the `V4L2_TUNER_CAP_LOW` flag set, in units of 62.5 Hz or if the struct [`v4l2_tuner`](vidioc-g-tuner.md#c.V4L.v4l2_tuner "v4l2_tuner") `capability` field has the `V4L2_TUNER_CAP_1HZ` flag set, in units of 1 Hz. If `rangelow` is zero a reasonable default value is used. |
| __u32 | `rangehigh` | If non-zero, the highest tunable frequency of the band to search in units of 62.5 kHz, or if the struct [`v4l2_tuner`](vidioc-g-tuner.md#c.V4L.v4l2_tuner "v4l2_tuner") `capability` field has the `V4L2_TUNER_CAP_LOW` flag set, in units of 62.5 Hz or if the struct [`v4l2_tuner`](vidioc-g-tuner.md#c.V4L.v4l2_tuner "v4l2_tuner") `capability` field has the `V4L2_TUNER_CAP_1HZ` flag set, in units of 1 Hz. If `rangehigh` is zero a reasonable default value is used. |
| __u32 | `reserved`[5] | Reserved for future extensions. Applications must set the array to zero. |

## 7.53.5. Return Value

On success 0 is returned, on error -1 and the `errno` variable is set
appropriately. The generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

EINVAL
:   The `tuner` index is out of bounds, the `wrap_around` value is
    not supported or one of the values in the `type`, `rangelow` or
    `rangehigh` fields is wrong.

EAGAIN
:   Attempted to call `VIDIOC_S_HW_FREQ_SEEK` with the filehandle in
    non-blocking mode.

ENODATA
:   The hardware seek found no channels.

EBUSY
:   Another hardware seek is already in progress.
