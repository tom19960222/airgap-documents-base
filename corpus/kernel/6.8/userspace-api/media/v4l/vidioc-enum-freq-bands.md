---
collection: kernel
version: "6.8"
title: "7.17. ioctl VIDIOC_ENUM_FREQ_BANDS"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/vidioc-enum-freq-bands.html
fetched_at: 2026-08-21T03:40:44+00:00
---
# 7.17. ioctl VIDIOC_ENUM_FREQ_BANDS

## 7.17.1. Name

VIDIOC_ENUM_FREQ_BANDS - Enumerate supported frequency bands

## 7.17.2. Synopsis

VIDIOC_ENUM_FREQ_BANDS

`int ioctl(int fd, VIDIOC_ENUM_FREQ_BANDS, struct v4l2_frequency_band *argp)`

## 7.17.3. Arguments

`fd`
:   File descriptor returned by [`open()`](func-open.md#c.V4L.open "open").

`argp`
:   Pointer to struct [`v4l2_frequency_band`](vidioc-enum-freq-bands.md#c.V4L.v4l2_frequency_band "v4l2_frequency_band").

## 7.17.4. Description

Enumerates the frequency bands that a tuner or modulator supports. To do
this applications initialize the `tuner`, `type` and `index`
fields, and zero out the `reserved` array of a struct
[`v4l2_frequency_band`](vidioc-enum-freq-bands.md#c.V4L.v4l2_frequency_band "v4l2_frequency_band") and call the
[ioctl VIDIOC_ENUM_FREQ_BANDS](vidioc-enum-freq-bands.md#vidioc-enum-freq-bands) ioctl with a pointer to this structure.

This ioctl is supported if the `V4L2_TUNER_CAP_FREQ_BANDS` capability
of the corresponding tuner/modulator is set.

type v4l2_frequency_band

struct v4l2_frequency_band

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| __u32 | `tuner` | The tuner or modulator index number. This is the same value as in the struct [`v4l2_input`](vidioc-enuminput.md#c.V4L.v4l2_input "v4l2_input") `tuner` field and the struct [`v4l2_tuner`](vidioc-g-tuner.md#c.V4L.v4l2_tuner "v4l2_tuner") `index` field, or the struct [`v4l2_output`](vidioc-enumoutput.md#c.V4L.v4l2_output "v4l2_output") `modulator` field and the struct [`v4l2_modulator`](vidioc-g-modulator.md#c.V4L.v4l2_modulator "v4l2_modulator") `index` field. | | |
| __u32 | `type` | The tuner type. This is the same value as in the struct [`v4l2_tuner`](vidioc-g-tuner.md#c.V4L.v4l2_tuner "v4l2_tuner") `type` field. The type must be set to `V4L2_TUNER_RADIO` for `/dev/radioX` device nodes, and to `V4L2_TUNER_ANALOG_TV` for all others. Set this field to `V4L2_TUNER_RADIO` for modulators (currently only radio modulators are supported). See [`v4l2_tuner_type`](vidioc-g-tuner.md#c.V4L.v4l2_tuner_type "v4l2_tuner_type") | | |
| __u32 | `index` | Identifies the frequency band, set by the application. | | |
| __u32 | `capability` | The tuner/modulator capability flags for this frequency band, see [Tuner and Modulator Capability Flags](vidioc-g-tuner.md#tuner-capability). The `V4L2_TUNER_CAP_LOW` or `V4L2_TUNER_CAP_1HZ` capability must be the same for all frequency bands of the selected tuner/modulator. So either all bands have that capability set, or none of them have that capability. | | |
| __u32 | `rangelow` | The lowest tunable frequency in units of 62.5 kHz, or if the `capability` flag `V4L2_TUNER_CAP_LOW` is set, in units of 62.5 Hz, for this frequency band. A 1 Hz unit is used when the `capability` flag `V4L2_TUNER_CAP_1HZ` is set. | | |
| __u32 | `rangehigh` | The highest tunable frequency in units of 62.5 kHz, or if the `capability` flag `V4L2_TUNER_CAP_LOW` is set, in units of 62.5 Hz, for this frequency band. A 1 Hz unit is used when the `capability` flag `V4L2_TUNER_CAP_1HZ` is set. | | |
| __u32 | `modulation` | The supported modulation systems of this frequency band. See [Band Modulation Systems](vidioc-enum-freq-bands.md#band-modulation).  **Note:** Currently only one modulation system per frequency band is supported. More work will need to be done if multiple modulation systems are possible. Contact the linux-media mailing list (<https://linuxtv.org/lists.php>) if you need such functionality. | | |
| __u32 | `reserved`[9] | Reserved for future extensions.  Applications and drivers must set the array to zero. | | |

Band Modulation Systems

|  |  |  |
| --- | --- | --- |
| `V4L2_BAND_MODULATION_VSB` | 0x02 | Vestigial Sideband modulation, used for analog TV. |
| `V4L2_BAND_MODULATION_FM` | 0x04 | Frequency Modulation, commonly used for analog radio. |
| `V4L2_BAND_MODULATION_AM` | 0x08 | Amplitude Modulation, commonly used for analog radio. |

## 7.17.5. Return Value

On success 0 is returned, on error -1 and the `errno` variable is set
appropriately. The generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

EINVAL
:   The `tuner` or `index` is out of bounds or the `type` field is
    wrong.
