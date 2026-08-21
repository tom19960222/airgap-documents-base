---
collection: kernel
version: "6.8"
title: "2.27. V4L2 common functions and data structures"
source_url: https://www.kernel.org/doc/html/v6.8/driver-api/media/v4l2-common.html
fetched_at: 2026-08-21T03:41:11+00:00
---
# 2.27. V4L2 common functions and data structures

int v4l2_ctrl_query_fill(struct [v4l2_queryctrl](v4l2-controls.md#c.v4l2_queryctrl "v4l2_queryctrl") \*qctrl, s32 min, s32 max, s32 step, s32 def)
:   Fill in a [`struct v4l2_queryctrl`](v4l2-controls.md#c.v4l2_queryctrl "v4l2_queryctrl")

**Parameters**

`struct v4l2_queryctrl *qctrl`
:   pointer to the [`struct v4l2_queryctrl`](v4l2-controls.md#c.v4l2_queryctrl "v4l2_queryctrl") to be filled

`s32 min`
:   minimum value for the control

`s32 max`
:   maximum value for the control

`s32 step`
:   control step

`s32 def`
:   default value for the control

**Description**

Fills the [`struct v4l2_queryctrl`](v4l2-controls.md#c.v4l2_queryctrl "v4l2_queryctrl") fields for the query control.

> **Note:**
>
> This function assumes that the **qctrl->id** field is filled.

Returns -EINVAL if the control is not known by the V4L2 core, 0 on success.

enum v4l2_i2c_tuner_type
:   specifies the range of tuner address that should be used when seeking for I2C devices.

**Constants**

`ADDRS_RADIO`
:   Radio tuner addresses.
    Represent the following I2C addresses:
    0x10 (if compiled with tea5761 support)
    and 0x60.

`ADDRS_DEMOD`
:   Demod tuner addresses.
    Represent the following I2C addresses:
    0x42, 0x43, 0x4a and 0x4b.

`ADDRS_TV`
:   TV tuner addresses.
    Represent the following I2C addresses:
    0x42, 0x43, 0x4a, 0x4b, 0x60, 0x61, 0x62,
    0x63 and 0x64.

`ADDRS_TV_WITH_DEMOD`
:   TV tuner addresses if demod is present, this
    excludes addresses used by the demodulator
    from the list of candidates.
    Represent the following I2C addresses:
    0x60, 0x61, 0x62, 0x63 and 0x64.

**NOTE**

All I2C addresses above use the 7-bit notation.

struct [v4l2_subdev](v4l2-subdev.md#c.v4l2_subdev "v4l2_subdev") \*v4l2_i2c_new_subdev(struct [v4l2_device](v4l2-device.md#c.v4l2_device "v4l2_device") \*v4l2_dev, struct i2c_adapter \*adapter, const char \*client_type, u8 addr, const unsigned short \*probe_addrs)
:   Load an i2c module and return an initialized [`struct v4l2_subdev`](v4l2-subdev.md#c.v4l2_subdev "v4l2_subdev").

**Parameters**

`struct v4l2_device *v4l2_dev`
:   pointer to [`struct v4l2_device`](v4l2-device.md#c.v4l2_device "v4l2_device")

`struct i2c_adapter *adapter`
:   pointer to struct i2c_adapter

`const char *client_type`
:   name of the chip that's on the adapter.

`u8 addr`
:   I2C address. If zero, it will use **probe_addrs**

`const unsigned short *probe_addrs`
:   array with a list of address. The last entry at such
    array should be `I2C_CLIENT_END`.

**Description**

returns a [`struct v4l2_subdev`](v4l2-subdev.md#c.v4l2_subdev "v4l2_subdev") pointer.

struct [v4l2_subdev](v4l2-subdev.md#c.v4l2_subdev "v4l2_subdev") \*v4l2_i2c_new_subdev_board(struct [v4l2_device](v4l2-device.md#c.v4l2_device "v4l2_device") \*v4l2_dev, struct i2c_adapter \*adapter, struct [i2c_board_info](../i2c.md#c.i2c_board_info "i2c_board_info") \*info, const unsigned short \*probe_addrs)
:   Load an i2c module and return an initialized [`struct v4l2_subdev`](v4l2-subdev.md#c.v4l2_subdev "v4l2_subdev").

**Parameters**

`struct v4l2_device *v4l2_dev`
:   pointer to [`struct v4l2_device`](v4l2-device.md#c.v4l2_device "v4l2_device")

`struct i2c_adapter *adapter`
:   pointer to struct i2c_adapter

`struct i2c_board_info *info`
:   pointer to [`struct i2c_board_info`](../i2c.md#c.i2c_board_info "i2c_board_info") used to replace the irq,
    platform_data and addr arguments.

`const unsigned short *probe_addrs`
:   array with a list of address. The last entry at such
    array should be `I2C_CLIENT_END`.

**Description**

returns a [`struct v4l2_subdev`](v4l2-subdev.md#c.v4l2_subdev "v4l2_subdev") pointer.

void v4l2_i2c_subdev_set_name(struct [v4l2_subdev](v4l2-subdev.md#c.v4l2_subdev "v4l2_subdev") \*sd, struct [i2c_client](../i2c.md#c.i2c_client "i2c_client") \*client, const char \*devname, const char \*postfix)
:   Set name for an I²C sub-device

**Parameters**

`struct v4l2_subdev *sd`
:   pointer to [`struct v4l2_subdev`](v4l2-subdev.md#c.v4l2_subdev "v4l2_subdev")

`struct i2c_client *client`
:   pointer to [`struct i2c_client`](../i2c.md#c.i2c_client "i2c_client")

`const char *devname`
:   the name of the device; if NULL, the I²C device drivers's name
    will be used

`const char *postfix`
:   sub-device specific string to put right after the I²C device name;
    may be NULL

void v4l2_i2c_subdev_init(struct [v4l2_subdev](v4l2-subdev.md#c.v4l2_subdev "v4l2_subdev") \*sd, struct [i2c_client](../i2c.md#c.i2c_client "i2c_client") \*client, const struct [v4l2_subdev_ops](v4l2-subdev.md#c.v4l2_subdev_ops "v4l2_subdev_ops") \*ops)
:   Initializes a [`struct v4l2_subdev`](v4l2-subdev.md#c.v4l2_subdev "v4l2_subdev") with data from an i2c_client struct.

**Parameters**

`struct v4l2_subdev *sd`
:   pointer to [`struct v4l2_subdev`](v4l2-subdev.md#c.v4l2_subdev "v4l2_subdev")

`struct i2c_client *client`
:   pointer to [`struct i2c_client`](../i2c.md#c.i2c_client "i2c_client")

`const struct v4l2_subdev_ops *ops`
:   pointer to [`struct v4l2_subdev_ops`](v4l2-subdev.md#c.v4l2_subdev_ops "v4l2_subdev_ops")

unsigned short v4l2_i2c_subdev_addr(struct [v4l2_subdev](v4l2-subdev.md#c.v4l2_subdev "v4l2_subdev") \*sd)
:   returns i2c client address of [`struct v4l2_subdev`](v4l2-subdev.md#c.v4l2_subdev "v4l2_subdev").

**Parameters**

`struct v4l2_subdev *sd`
:   pointer to [`struct v4l2_subdev`](v4l2-subdev.md#c.v4l2_subdev "v4l2_subdev")

**Description**

Returns the address of an I2C sub-device

const unsigned short \*v4l2_i2c_tuner_addrs(enum [v4l2_i2c_tuner_type](v4l2-common.md#c.v4l2_i2c_tuner_type "v4l2_i2c_tuner_type") type)
:   Return a list of I2C tuner addresses to probe.

**Parameters**

`enum v4l2_i2c_tuner_type type`
:   type of the tuner to seek, as defined by
    [`enum v4l2_i2c_tuner_type`](v4l2-common.md#c.v4l2_i2c_tuner_type "v4l2_i2c_tuner_type").

**NOTE**

Use only if the tuner addresses are unknown.

void v4l2_i2c_subdev_unregister(struct [v4l2_subdev](v4l2-subdev.md#c.v4l2_subdev "v4l2_subdev") \*sd)
:   Unregister a v4l2_subdev

**Parameters**

`struct v4l2_subdev *sd`
:   pointer to [`struct v4l2_subdev`](v4l2-subdev.md#c.v4l2_subdev "v4l2_subdev")

struct [v4l2_subdev](v4l2-subdev.md#c.v4l2_subdev "v4l2_subdev") \*v4l2_spi_new_subdev(struct [v4l2_device](v4l2-device.md#c.v4l2_device "v4l2_device") \*v4l2_dev, struct spi_master \*master, struct [spi_board_info](../spi.md#c.spi_board_info "spi_board_info") \*info)
:   Load an spi module and return an initialized [`struct v4l2_subdev`](v4l2-subdev.md#c.v4l2_subdev "v4l2_subdev").

**Parameters**

`struct v4l2_device *v4l2_dev`
:   pointer to [`struct v4l2_device`](v4l2-device.md#c.v4l2_device "v4l2_device").

`struct spi_master *master`
:   pointer to struct spi_master.

`struct spi_board_info *info`
:   pointer to [`struct spi_board_info`](../spi.md#c.spi_board_info "spi_board_info").

**Description**

returns a [`struct v4l2_subdev`](v4l2-subdev.md#c.v4l2_subdev "v4l2_subdev") pointer.

void v4l2_spi_subdev_init(struct [v4l2_subdev](v4l2-subdev.md#c.v4l2_subdev "v4l2_subdev") \*sd, struct [spi_device](../spi.md#c.spi_device "spi_device") \*spi, const struct [v4l2_subdev_ops](v4l2-subdev.md#c.v4l2_subdev_ops "v4l2_subdev_ops") \*ops)
:   Initialize a v4l2_subdev with data from an spi_device struct.

**Parameters**

`struct v4l2_subdev *sd`
:   pointer to [`struct v4l2_subdev`](v4l2-subdev.md#c.v4l2_subdev "v4l2_subdev")

`struct spi_device *spi`
:   pointer to [`struct spi_device`](../spi.md#c.spi_device "spi_device").

`const struct v4l2_subdev_ops *ops`
:   pointer to [`struct v4l2_subdev_ops`](v4l2-subdev.md#c.v4l2_subdev_ops "v4l2_subdev_ops")

void v4l2_spi_subdev_unregister(struct [v4l2_subdev](v4l2-subdev.md#c.v4l2_subdev "v4l2_subdev") \*sd)
:   Unregister a v4l2_subdev

**Parameters**

`struct v4l2_subdev *sd`
:   pointer to [`struct v4l2_subdev`](v4l2-subdev.md#c.v4l2_subdev "v4l2_subdev")

void v4l_bound_align_image(unsigned int \*width, unsigned int wmin, unsigned int wmax, unsigned int walign, unsigned int \*height, unsigned int hmin, unsigned int hmax, unsigned int halign, unsigned int salign)
:   adjust video dimensions according to a given constraints.

**Parameters**

`unsigned int *width`
:   pointer to width that will be adjusted if needed.

`unsigned int wmin`
:   minimum width.

`unsigned int wmax`
:   maximum width.

`unsigned int walign`
:   least significant bit on width.

`unsigned int *height`
:   pointer to height that will be adjusted if needed.

`unsigned int hmin`
:   minimum height.

`unsigned int hmax`
:   maximum height.

`unsigned int halign`
:   least significant bit on height.

`unsigned int salign`
:   least significant bit for the image size (e. g.
    ![width * height](../../_images/math/20d03bfef00d6b5808ba0a5d41b1dd8ce7cb9e99.png)).

**Description**

Clip an image to have **width** between **wmin** and **wmax**, and **height** between
**hmin** and **hmax**, inclusive.

Additionally, the **width** will be a multiple of ![2^{walign}](../../_images/math/67a08268328fc3a482ec0910d19f7549058c7a9c.png),
the **height** will be a multiple of ![2^{halign}](../../_images/math/004528933b2819d5b7b497a28544867b4a71a3a9.png), and the overall
size ![width * height](../../_images/math/20d03bfef00d6b5808ba0a5d41b1dd8ce7cb9e99.png) will be a multiple of ![2^{salign}](../../_images/math/a16b7e62bdc98aa49db08480890a77ee9bff9d67.png).

> **Note:**
>
> 1. The clipping rectangle may be shrunk or enlarged to fit the alignment
>    constraints.
> 2. **wmax** must not be smaller than **wmin**.
> 3. **hmax** must not be smaller than **hmin**.
> 4. The alignments must not be so high there are no possible image
>    sizes within the allowed bounds.
> 5. **wmin** and **hmin** must be at least 1 (don't use 0).
> 6. For **walign**, **halign** and **salign**, if you don't care about a certain
>    alignment, specify `0`, as ![2^0 = 1](../../_images/math/30e7079eba8ca63eee0077129966e10125c65838.png) and one byte alignment
>    is equivalent to no alignment.
> 7. If you only want to adjust downward, specify a maximum that's the
>    same as the initial value.

v4l2_find_nearest_size

`v4l2_find_nearest_size (array, array_size, width_field, height_field, width, height)`

> Find the nearest size among a discrete set of resolutions contained in an array of a driver specific struct.

**Parameters**

`array`
:   a driver specific array of image sizes

`array_size`
:   the length of the driver specific array of image sizes

`width_field`
:   the name of the width field in the driver specific struct

`height_field`
:   the name of the height field in the driver specific struct

`width`
:   desired width.

`height`
:   desired height.

**Description**

Finds the closest resolution to minimize the width and height differences
between what requested and the supported resolutions. The size of the width
and height fields in the driver specific must equal to that of u32, i.e. four
bytes.

Returns the best match or NULL if the length of the array is zero.

int v4l2_g_parm_cap(struct [video_device](v4l2-dev.md#c.video_device "video_device") \*vdev, struct [v4l2_subdev](v4l2-subdev.md#c.v4l2_subdev "v4l2_subdev") \*sd, struct v4l2_streamparm \*a)
:   helper routine for vidioc_g_parm to fill this in by calling the get_frame_interval op of the given subdev. It only works for V4L2_BUF_TYPE_VIDEO_CAPTURE(_MPLANE), hence the _cap in the function name.

**Parameters**

`struct video_device *vdev`
:   the [`struct video_device`](v4l2-dev.md#c.video_device "video_device") pointer. Used to determine the device caps.

`struct v4l2_subdev *sd`
:   the sub-device pointer.

`struct v4l2_streamparm *a`
:   the VIDIOC_G_PARM argument.

int v4l2_s_parm_cap(struct [video_device](v4l2-dev.md#c.video_device "video_device") \*vdev, struct [v4l2_subdev](v4l2-subdev.md#c.v4l2_subdev "v4l2_subdev") \*sd, struct v4l2_streamparm \*a)
:   helper routine for vidioc_s_parm to fill this in by calling the set_frame_interval op of the given subdev. It only works for V4L2_BUF_TYPE_VIDEO_CAPTURE(_MPLANE), hence the _cap in the function name.

**Parameters**

`struct video_device *vdev`
:   the [`struct video_device`](v4l2-dev.md#c.video_device "video_device") pointer. Used to determine the device caps.

`struct v4l2_subdev *sd`
:   the sub-device pointer.

`struct v4l2_streamparm *a`
:   the VIDIOC_S_PARM argument.

enum v4l2_pixel_encoding
:   specifies the pixel encoding value

**Constants**

`V4L2_PIXEL_ENC_UNKNOWN`
:   Pixel encoding is unknown/un-initialized

`V4L2_PIXEL_ENC_YUV`
:   Pixel encoding is YUV

`V4L2_PIXEL_ENC_RGB`
:   Pixel encoding is RGB

`V4L2_PIXEL_ENC_BAYER`
:   Pixel encoding is Bayer

struct v4l2_format_info
:   information about a V4L2 format

**Definition**:

```
struct v4l2_format_info {
    u32 format;
    u8 pixel_enc;
    u8 mem_planes;
    u8 comp_planes;
    u8 bpp[4];
    u8 bpp_div[4];
    u8 hdiv;
    u8 vdiv;
    u8 block_w[4];
    u8 block_h[4];
};
```

**Members**

`format`
:   4CC format identifier (V4L2_PIX_FMT_\*)

`pixel_enc`
:   Pixel encoding (see [`enum v4l2_pixel_encoding`](v4l2-common.md#c.v4l2_pixel_encoding "v4l2_pixel_encoding") above)

`mem_planes`
:   Number of memory planes, which includes the alpha plane (1 to 4).

`comp_planes`
:   Number of component planes, which includes the alpha plane (1 to 4).

`bpp`
:   Array of per-plane bytes per pixel

`bpp_div`
:   Array of per-plane bytes per pixel divisors to support fractional pixel sizes.

`hdiv`
:   Horizontal chroma subsampling factor

`vdiv`
:   Vertical chroma subsampling factor

`block_w`
:   Per-plane macroblock pixel width (optional)

`block_h`
:   Per-plane macroblock pixel height (optional)

s64 v4l2_get_link_freq(struct [v4l2_ctrl_handler](v4l2-controls.md#c.v4l2_ctrl_handler "v4l2_ctrl_handler") \*handler, unsigned int mul, unsigned int div)
:   Get link rate from transmitter

**Parameters**

`struct v4l2_ctrl_handler *handler`
:   The transmitter's control handler

`unsigned int mul`
:   The multiplier between pixel rate and link frequency. Bits per pixel on
    D-PHY, samples per clock on parallel. 0 otherwise.

`unsigned int div`
:   The divisor between pixel rate and link frequency. Number of data lanes
    times two on D-PHY, 1 on parallel. 0 otherwise.

**Description**

This function is intended for obtaining the link frequency from the
transmitter sub-devices. It returns the link rate, either from the
V4L2_CID_LINK_FREQ control implemented by the transmitter, or value
calculated based on the V4L2_CID_PIXEL_RATE implemented by the transmitter.

Returns link frequency on success, otherwise a negative error code:
:   -ENOENT: Link frequency or pixel rate control not found
    -EINVAL: Invalid link frequency value

struct v4l2_ioctl_ops
:   describe operations for each V4L2 ioctl

**Definition**:

```
struct v4l2_ioctl_ops {
    int (*vidioc_querycap)(struct file *file, void *fh, struct v4l2_capability *cap);
    int (*vidioc_enum_fmt_vid_cap)(struct file *file, void *fh, struct v4l2_fmtdesc *f);
    int (*vidioc_enum_fmt_vid_overlay)(struct file *file, void *fh, struct v4l2_fmtdesc *f);
    int (*vidioc_enum_fmt_vid_out)(struct file *file, void *fh, struct v4l2_fmtdesc *f);
    int (*vidioc_enum_fmt_sdr_cap)(struct file *file, void *fh, struct v4l2_fmtdesc *f);
    int (*vidioc_enum_fmt_sdr_out)(struct file *file, void *fh, struct v4l2_fmtdesc *f);
    int (*vidioc_enum_fmt_meta_cap)(struct file *file, void *fh, struct v4l2_fmtdesc *f);
    int (*vidioc_enum_fmt_meta_out)(struct file *file, void *fh, struct v4l2_fmtdesc *f);
    int (*vidioc_g_fmt_vid_cap)(struct file *file, void *fh, struct v4l2_format *f);
    int (*vidioc_g_fmt_vid_overlay)(struct file *file, void *fh, struct v4l2_format *f);
    int (*vidioc_g_fmt_vid_out)(struct file *file, void *fh, struct v4l2_format *f);
    int (*vidioc_g_fmt_vid_out_overlay)(struct file *file, void *fh, struct v4l2_format *f);
    int (*vidioc_g_fmt_vbi_cap)(struct file *file, void *fh, struct v4l2_format *f);
    int (*vidioc_g_fmt_vbi_out)(struct file *file, void *fh, struct v4l2_format *f);
    int (*vidioc_g_fmt_sliced_vbi_cap)(struct file *file, void *fh, struct v4l2_format *f);
    int (*vidioc_g_fmt_sliced_vbi_out)(struct file *file, void *fh, struct v4l2_format *f);
    int (*vidioc_g_fmt_vid_cap_mplane)(struct file *file, void *fh, struct v4l2_format *f);
    int (*vidioc_g_fmt_vid_out_mplane)(struct file *file, void *fh, struct v4l2_format *f);
    int (*vidioc_g_fmt_sdr_cap)(struct file *file, void *fh, struct v4l2_format *f);
    int (*vidioc_g_fmt_sdr_out)(struct file *file, void *fh, struct v4l2_format *f);
    int (*vidioc_g_fmt_meta_cap)(struct file *file, void *fh, struct v4l2_format *f);
    int (*vidioc_g_fmt_meta_out)(struct file *file, void *fh, struct v4l2_format *f);
    int (*vidioc_s_fmt_vid_cap)(struct file *file, void *fh, struct v4l2_format *f);
    int (*vidioc_s_fmt_vid_overlay)(struct file *file, void *fh, struct v4l2_format *f);
    int (*vidioc_s_fmt_vid_out)(struct file *file, void *fh, struct v4l2_format *f);
    int (*vidioc_s_fmt_vid_out_overlay)(struct file *file, void *fh, struct v4l2_format *f);
    int (*vidioc_s_fmt_vbi_cap)(struct file *file, void *fh, struct v4l2_format *f);
    int (*vidioc_s_fmt_vbi_out)(struct file *file, void *fh, struct v4l2_format *f);
    int (*vidioc_s_fmt_sliced_vbi_cap)(struct file *file, void *fh, struct v4l2_format *f);
    int (*vidioc_s_fmt_sliced_vbi_out)(struct file *file, void *fh, struct v4l2_format *f);
    int (*vidioc_s_fmt_vid_cap_mplane)(struct file *file, void *fh, struct v4l2_format *f);
    int (*vidioc_s_fmt_vid_out_mplane)(struct file *file, void *fh, struct v4l2_format *f);
    int (*vidioc_s_fmt_sdr_cap)(struct file *file, void *fh, struct v4l2_format *f);
    int (*vidioc_s_fmt_sdr_out)(struct file *file, void *fh, struct v4l2_format *f);
    int (*vidioc_s_fmt_meta_cap)(struct file *file, void *fh, struct v4l2_format *f);
    int (*vidioc_s_fmt_meta_out)(struct file *file, void *fh, struct v4l2_format *f);
    int (*vidioc_try_fmt_vid_cap)(struct file *file, void *fh, struct v4l2_format *f);
    int (*vidioc_try_fmt_vid_overlay)(struct file *file, void *fh, struct v4l2_format *f);
    int (*vidioc_try_fmt_vid_out)(struct file *file, void *fh, struct v4l2_format *f);
    int (*vidioc_try_fmt_vid_out_overlay)(struct file *file, void *fh, struct v4l2_format *f);
    int (*vidioc_try_fmt_vbi_cap)(struct file *file, void *fh, struct v4l2_format *f);
    int (*vidioc_try_fmt_vbi_out)(struct file *file, void *fh, struct v4l2_format *f);
    int (*vidioc_try_fmt_sliced_vbi_cap)(struct file *file, void *fh, struct v4l2_format *f);
    int (*vidioc_try_fmt_sliced_vbi_out)(struct file *file, void *fh, struct v4l2_format *f);
    int (*vidioc_try_fmt_vid_cap_mplane)(struct file *file, void *fh, struct v4l2_format *f);
    int (*vidioc_try_fmt_vid_out_mplane)(struct file *file, void *fh, struct v4l2_format *f);
    int (*vidioc_try_fmt_sdr_cap)(struct file *file, void *fh, struct v4l2_format *f);
    int (*vidioc_try_fmt_sdr_out)(struct file *file, void *fh, struct v4l2_format *f);
    int (*vidioc_try_fmt_meta_cap)(struct file *file, void *fh, struct v4l2_format *f);
    int (*vidioc_try_fmt_meta_out)(struct file *file, void *fh, struct v4l2_format *f);
    int (*vidioc_reqbufs)(struct file *file, void *fh, struct v4l2_requestbuffers *b);
    int (*vidioc_querybuf)(struct file *file, void *fh, struct v4l2_buffer *b);
    int (*vidioc_qbuf)(struct file *file, void *fh, struct v4l2_buffer *b);
    int (*vidioc_expbuf)(struct file *file, void *fh, struct v4l2_exportbuffer *e);
    int (*vidioc_dqbuf)(struct file *file, void *fh, struct v4l2_buffer *b);
    int (*vidioc_create_bufs)(struct file *file, void *fh, struct v4l2_create_buffers *b);
    int (*vidioc_prepare_buf)(struct file *file, void *fh, struct v4l2_buffer *b);
    int (*vidioc_overlay)(struct file *file, void *fh, unsigned int i);
    int (*vidioc_g_fbuf)(struct file *file, void *fh, struct v4l2_framebuffer *a);
    int (*vidioc_s_fbuf)(struct file *file, void *fh, const struct v4l2_framebuffer *a);
    int (*vidioc_streamon)(struct file *file, void *fh, enum v4l2_buf_type i);
    int (*vidioc_streamoff)(struct file *file, void *fh, enum v4l2_buf_type i);
    int (*vidioc_g_std)(struct file *file, void *fh, v4l2_std_id *norm);
    int (*vidioc_s_std)(struct file *file, void *fh, v4l2_std_id norm);
    int (*vidioc_querystd)(struct file *file, void *fh, v4l2_std_id *a);
    int (*vidioc_enum_input)(struct file *file, void *fh, struct v4l2_input *inp);
    int (*vidioc_g_input)(struct file *file, void *fh, unsigned int *i);
    int (*vidioc_s_input)(struct file *file, void *fh, unsigned int i);
    int (*vidioc_enum_output)(struct file *file, void *fh, struct v4l2_output *a);
    int (*vidioc_g_output)(struct file *file, void *fh, unsigned int *i);
    int (*vidioc_s_output)(struct file *file, void *fh, unsigned int i);
    int (*vidioc_queryctrl)(struct file *file, void *fh, struct v4l2_queryctrl *a);
    int (*vidioc_query_ext_ctrl)(struct file *file, void *fh, struct v4l2_query_ext_ctrl *a);
    int (*vidioc_g_ctrl)(struct file *file, void *fh, struct v4l2_control *a);
    int (*vidioc_s_ctrl)(struct file *file, void *fh, struct v4l2_control *a);
    int (*vidioc_g_ext_ctrls)(struct file *file, void *fh, struct v4l2_ext_controls *a);
    int (*vidioc_s_ext_ctrls)(struct file *file, void *fh, struct v4l2_ext_controls *a);
    int (*vidioc_try_ext_ctrls)(struct file *file, void *fh, struct v4l2_ext_controls *a);
    int (*vidioc_querymenu)(struct file *file, void *fh, struct v4l2_querymenu *a);
    int (*vidioc_enumaudio)(struct file *file, void *fh, struct v4l2_audio *a);
    int (*vidioc_g_audio)(struct file *file, void *fh, struct v4l2_audio *a);
    int (*vidioc_s_audio)(struct file *file, void *fh, const struct v4l2_audio *a);
    int (*vidioc_enumaudout)(struct file *file, void *fh, struct v4l2_audioout *a);
    int (*vidioc_g_audout)(struct file *file, void *fh, struct v4l2_audioout *a);
    int (*vidioc_s_audout)(struct file *file, void *fh, const struct v4l2_audioout *a);
    int (*vidioc_g_modulator)(struct file *file, void *fh, struct v4l2_modulator *a);
    int (*vidioc_s_modulator)(struct file *file, void *fh, const struct v4l2_modulator *a);
    int (*vidioc_g_pixelaspect)(struct file *file, void *fh, int buf_type, struct v4l2_fract *aspect);
    int (*vidioc_g_selection)(struct file *file, void *fh, struct v4l2_selection *s);
    int (*vidioc_s_selection)(struct file *file, void *fh, struct v4l2_selection *s);
    int (*vidioc_g_jpegcomp)(struct file *file, void *fh, struct v4l2_jpegcompression *a);
    int (*vidioc_s_jpegcomp)(struct file *file, void *fh, const struct v4l2_jpegcompression *a);
    int (*vidioc_g_enc_index)(struct file *file, void *fh, struct v4l2_enc_idx *a);
    int (*vidioc_encoder_cmd)(struct file *file, void *fh, struct v4l2_encoder_cmd *a);
    int (*vidioc_try_encoder_cmd)(struct file *file, void *fh, struct v4l2_encoder_cmd *a);
    int (*vidioc_decoder_cmd)(struct file *file, void *fh, struct v4l2_decoder_cmd *a);
    int (*vidioc_try_decoder_cmd)(struct file *file, void *fh, struct v4l2_decoder_cmd *a);
    int (*vidioc_g_parm)(struct file *file, void *fh, struct v4l2_streamparm *a);
    int (*vidioc_s_parm)(struct file *file, void *fh, struct v4l2_streamparm *a);
    int (*vidioc_g_tuner)(struct file *file, void *fh, struct v4l2_tuner *a);
    int (*vidioc_s_tuner)(struct file *file, void *fh, const struct v4l2_tuner *a);
    int (*vidioc_g_frequency)(struct file *file, void *fh, struct v4l2_frequency *a);
    int (*vidioc_s_frequency)(struct file *file, void *fh, const struct v4l2_frequency *a);
    int (*vidioc_enum_freq_bands)(struct file *file, void *fh, struct v4l2_frequency_band *band);
    int (*vidioc_g_sliced_vbi_cap)(struct file *file, void *fh, struct v4l2_sliced_vbi_cap *a);
    int (*vidioc_log_status)(struct file *file, void *fh);
    int (*vidioc_s_hw_freq_seek)(struct file *file, void *fh, const struct v4l2_hw_freq_seek *a);
#ifdef CONFIG_VIDEO_ADV_DEBUG;
    int (*vidioc_g_register)(struct file *file, void *fh, struct v4l2_dbg_register *reg);
    int (*vidioc_s_register)(struct file *file, void *fh, const struct v4l2_dbg_register *reg);
    int (*vidioc_g_chip_info)(struct file *file, void *fh, struct v4l2_dbg_chip_info *chip);
#endif;
    int (*vidioc_enum_framesizes)(struct file *file, void *fh, struct v4l2_frmsizeenum *fsize);
    int (*vidioc_enum_frameintervals)(struct file *file, void *fh, struct v4l2_frmivalenum *fival);
    int (*vidioc_s_dv_timings)(struct file *file, void *fh, struct v4l2_dv_timings *timings);
    int (*vidioc_g_dv_timings)(struct file *file, void *fh, struct v4l2_dv_timings *timings);
    int (*vidioc_query_dv_timings)(struct file *file, void *fh, struct v4l2_dv_timings *timings);
    int (*vidioc_enum_dv_timings)(struct file *file, void *fh, struct v4l2_enum_dv_timings *timings);
    int (*vidioc_dv_timings_cap)(struct file *file, void *fh, struct v4l2_dv_timings_cap *cap);
    int (*vidioc_g_edid)(struct file *file, void *fh, struct v4l2_edid *edid);
    int (*vidioc_s_edid)(struct file *file, void *fh, struct v4l2_edid *edid);
    int (*vidioc_subscribe_event)(struct v4l2_fh *fh, const struct v4l2_event_subscription *sub);
    int (*vidioc_unsubscribe_event)(struct v4l2_fh *fh, const struct v4l2_event_subscription *sub);
    long (*vidioc_default)(struct file *file, void *fh, bool valid_prio, unsigned int cmd, void *arg);
};
```

**Members**

`vidioc_querycap`
:   pointer to the function that implements
    [VIDIOC_QUERYCAP](../../userspace-api/media/v4l/vidioc-querycap.md#vidioc-querycap) ioctl

`vidioc_enum_fmt_vid_cap`
:   pointer to the function that implements
    [VIDIOC_ENUM_FMT](../../userspace-api/media/v4l/vidioc-enum-fmt.md#vidioc-enum-fmt) ioctl logic
    for video capture in single and multi plane mode

`vidioc_enum_fmt_vid_overlay`
:   pointer to the function that implements
    [VIDIOC_ENUM_FMT](../../userspace-api/media/v4l/vidioc-enum-fmt.md#vidioc-enum-fmt) ioctl logic
    for video overlay

`vidioc_enum_fmt_vid_out`
:   pointer to the function that implements
    [VIDIOC_ENUM_FMT](../../userspace-api/media/v4l/vidioc-enum-fmt.md#vidioc-enum-fmt) ioctl logic
    for video output in single and multi plane mode

`vidioc_enum_fmt_sdr_cap`
:   pointer to the function that implements
    [VIDIOC_ENUM_FMT](../../userspace-api/media/v4l/vidioc-enum-fmt.md#vidioc-enum-fmt) ioctl logic
    for Software Defined Radio capture

`vidioc_enum_fmt_sdr_out`
:   pointer to the function that implements
    [VIDIOC_ENUM_FMT](../../userspace-api/media/v4l/vidioc-enum-fmt.md#vidioc-enum-fmt) ioctl logic
    for Software Defined Radio output

`vidioc_enum_fmt_meta_cap`
:   pointer to the function that implements
    [VIDIOC_ENUM_FMT](../../userspace-api/media/v4l/vidioc-enum-fmt.md#vidioc-enum-fmt) ioctl logic
    for metadata capture

`vidioc_enum_fmt_meta_out`
:   pointer to the function that implements
    [VIDIOC_ENUM_FMT](../../userspace-api/media/v4l/vidioc-enum-fmt.md#vidioc-enum-fmt) ioctl logic
    for metadata output

`vidioc_g_fmt_vid_cap`
:   pointer to the function that implements
    [VIDIOC_G_FMT](../../userspace-api/media/v4l/vidioc-g-fmt.md#vidioc-g-fmt) ioctl logic for video capture
    in single plane mode

`vidioc_g_fmt_vid_overlay`
:   pointer to the function that implements
    [VIDIOC_G_FMT](../../userspace-api/media/v4l/vidioc-g-fmt.md#vidioc-g-fmt) ioctl logic for video overlay

`vidioc_g_fmt_vid_out`
:   pointer to the function that implements
    [VIDIOC_G_FMT](../../userspace-api/media/v4l/vidioc-g-fmt.md#vidioc-g-fmt) ioctl logic for video out
    in single plane mode

`vidioc_g_fmt_vid_out_overlay`
:   pointer to the function that implements
    [VIDIOC_G_FMT](../../userspace-api/media/v4l/vidioc-g-fmt.md#vidioc-g-fmt) ioctl logic for video overlay output

`vidioc_g_fmt_vbi_cap`
:   pointer to the function that implements
    [VIDIOC_G_FMT](../../userspace-api/media/v4l/vidioc-g-fmt.md#vidioc-g-fmt) ioctl logic for raw VBI capture

`vidioc_g_fmt_vbi_out`
:   pointer to the function that implements
    [VIDIOC_G_FMT](../../userspace-api/media/v4l/vidioc-g-fmt.md#vidioc-g-fmt) ioctl logic for raw VBI output

`vidioc_g_fmt_sliced_vbi_cap`
:   pointer to the function that implements
    [VIDIOC_G_FMT](../../userspace-api/media/v4l/vidioc-g-fmt.md#vidioc-g-fmt) ioctl logic for sliced VBI capture

`vidioc_g_fmt_sliced_vbi_out`
:   pointer to the function that implements
    [VIDIOC_G_FMT](../../userspace-api/media/v4l/vidioc-g-fmt.md#vidioc-g-fmt) ioctl logic for sliced VBI output

`vidioc_g_fmt_vid_cap_mplane`
:   pointer to the function that implements
    [VIDIOC_G_FMT](../../userspace-api/media/v4l/vidioc-g-fmt.md#vidioc-g-fmt) ioctl logic for video capture
    in multiple plane mode

`vidioc_g_fmt_vid_out_mplane`
:   pointer to the function that implements
    [VIDIOC_G_FMT](../../userspace-api/media/v4l/vidioc-g-fmt.md#vidioc-g-fmt) ioctl logic for video out
    in multiplane plane mode

`vidioc_g_fmt_sdr_cap`
:   pointer to the function that implements
    [VIDIOC_G_FMT](../../userspace-api/media/v4l/vidioc-g-fmt.md#vidioc-g-fmt) ioctl logic for Software Defined
    Radio capture

`vidioc_g_fmt_sdr_out`
:   pointer to the function that implements
    [VIDIOC_G_FMT](../../userspace-api/media/v4l/vidioc-g-fmt.md#vidioc-g-fmt) ioctl logic for Software Defined
    Radio output

`vidioc_g_fmt_meta_cap`
:   pointer to the function that implements
    [VIDIOC_G_FMT](../../userspace-api/media/v4l/vidioc-g-fmt.md#vidioc-g-fmt) ioctl logic for metadata capture

`vidioc_g_fmt_meta_out`
:   pointer to the function that implements
    [VIDIOC_G_FMT](../../userspace-api/media/v4l/vidioc-g-fmt.md#vidioc-g-fmt) ioctl logic for metadata output

`vidioc_s_fmt_vid_cap`
:   pointer to the function that implements
    [VIDIOC_S_FMT](../../userspace-api/media/v4l/vidioc-g-fmt.md#vidioc-g-fmt) ioctl logic for video capture
    in single plane mode

`vidioc_s_fmt_vid_overlay`
:   pointer to the function that implements
    [VIDIOC_S_FMT](../../userspace-api/media/v4l/vidioc-g-fmt.md#vidioc-g-fmt) ioctl logic for video overlay

`vidioc_s_fmt_vid_out`
:   pointer to the function that implements
    [VIDIOC_S_FMT](../../userspace-api/media/v4l/vidioc-g-fmt.md#vidioc-g-fmt) ioctl logic for video out
    in single plane mode

`vidioc_s_fmt_vid_out_overlay`
:   pointer to the function that implements
    [VIDIOC_S_FMT](../../userspace-api/media/v4l/vidioc-g-fmt.md#vidioc-g-fmt) ioctl logic for video overlay output

`vidioc_s_fmt_vbi_cap`
:   pointer to the function that implements
    [VIDIOC_S_FMT](../../userspace-api/media/v4l/vidioc-g-fmt.md#vidioc-g-fmt) ioctl logic for raw VBI capture

`vidioc_s_fmt_vbi_out`
:   pointer to the function that implements
    [VIDIOC_S_FMT](../../userspace-api/media/v4l/vidioc-g-fmt.md#vidioc-g-fmt) ioctl logic for raw VBI output

`vidioc_s_fmt_sliced_vbi_cap`
:   pointer to the function that implements
    [VIDIOC_S_FMT](../../userspace-api/media/v4l/vidioc-g-fmt.md#vidioc-g-fmt) ioctl logic for sliced VBI capture

`vidioc_s_fmt_sliced_vbi_out`
:   pointer to the function that implements
    [VIDIOC_S_FMT](../../userspace-api/media/v4l/vidioc-g-fmt.md#vidioc-g-fmt) ioctl logic for sliced VBI output

`vidioc_s_fmt_vid_cap_mplane`
:   pointer to the function that implements
    [VIDIOC_S_FMT](../../userspace-api/media/v4l/vidioc-g-fmt.md#vidioc-g-fmt) ioctl logic for video capture
    in multiple plane mode

`vidioc_s_fmt_vid_out_mplane`
:   pointer to the function that implements
    [VIDIOC_S_FMT](../../userspace-api/media/v4l/vidioc-g-fmt.md#vidioc-g-fmt) ioctl logic for video out
    in multiplane plane mode

`vidioc_s_fmt_sdr_cap`
:   pointer to the function that implements
    [VIDIOC_S_FMT](../../userspace-api/media/v4l/vidioc-g-fmt.md#vidioc-g-fmt) ioctl logic for Software Defined
    Radio capture

`vidioc_s_fmt_sdr_out`
:   pointer to the function that implements
    [VIDIOC_S_FMT](../../userspace-api/media/v4l/vidioc-g-fmt.md#vidioc-g-fmt) ioctl logic for Software Defined
    Radio output

`vidioc_s_fmt_meta_cap`
:   pointer to the function that implements
    [VIDIOC_S_FMT](../../userspace-api/media/v4l/vidioc-g-fmt.md#vidioc-g-fmt) ioctl logic for metadata capture

`vidioc_s_fmt_meta_out`
:   pointer to the function that implements
    [VIDIOC_S_FMT](../../userspace-api/media/v4l/vidioc-g-fmt.md#vidioc-g-fmt) ioctl logic for metadata output

`vidioc_try_fmt_vid_cap`
:   pointer to the function that implements
    [VIDIOC_TRY_FMT](../../userspace-api/media/v4l/vidioc-g-fmt.md#vidioc-g-fmt) ioctl logic for video capture
    in single plane mode

`vidioc_try_fmt_vid_overlay`
:   pointer to the function that implements
    [VIDIOC_TRY_FMT](../../userspace-api/media/v4l/vidioc-g-fmt.md#vidioc-g-fmt) ioctl logic for video overlay

`vidioc_try_fmt_vid_out`
:   pointer to the function that implements
    [VIDIOC_TRY_FMT](../../userspace-api/media/v4l/vidioc-g-fmt.md#vidioc-g-fmt) ioctl logic for video out
    in single plane mode

`vidioc_try_fmt_vid_out_overlay`
:   pointer to the function that implements
    [VIDIOC_TRY_FMT](../../userspace-api/media/v4l/vidioc-g-fmt.md#vidioc-g-fmt) ioctl logic for video overlay
    output

`vidioc_try_fmt_vbi_cap`
:   pointer to the function that implements
    [VIDIOC_TRY_FMT](../../userspace-api/media/v4l/vidioc-g-fmt.md#vidioc-g-fmt) ioctl logic for raw VBI capture

`vidioc_try_fmt_vbi_out`
:   pointer to the function that implements
    [VIDIOC_TRY_FMT](../../userspace-api/media/v4l/vidioc-g-fmt.md#vidioc-g-fmt) ioctl logic for raw VBI output

`vidioc_try_fmt_sliced_vbi_cap`
:   pointer to the function that implements
    [VIDIOC_TRY_FMT](../../userspace-api/media/v4l/vidioc-g-fmt.md#vidioc-g-fmt) ioctl logic for sliced VBI
    capture

`vidioc_try_fmt_sliced_vbi_out`
:   pointer to the function that implements
    [VIDIOC_TRY_FMT](../../userspace-api/media/v4l/vidioc-g-fmt.md#vidioc-g-fmt) ioctl logic for sliced VBI output

`vidioc_try_fmt_vid_cap_mplane`
:   pointer to the function that implements
    [VIDIOC_TRY_FMT](../../userspace-api/media/v4l/vidioc-g-fmt.md#vidioc-g-fmt) ioctl logic for video capture
    in multiple plane mode

`vidioc_try_fmt_vid_out_mplane`
:   pointer to the function that implements
    [VIDIOC_TRY_FMT](../../userspace-api/media/v4l/vidioc-g-fmt.md#vidioc-g-fmt) ioctl logic for video out
    in multiplane plane mode

`vidioc_try_fmt_sdr_cap`
:   pointer to the function that implements
    [VIDIOC_TRY_FMT](../../userspace-api/media/v4l/vidioc-g-fmt.md#vidioc-g-fmt) ioctl logic for Software Defined
    Radio capture

`vidioc_try_fmt_sdr_out`
:   pointer to the function that implements
    [VIDIOC_TRY_FMT](../../userspace-api/media/v4l/vidioc-g-fmt.md#vidioc-g-fmt) ioctl logic for Software Defined
    Radio output

`vidioc_try_fmt_meta_cap`
:   pointer to the function that implements
    [VIDIOC_TRY_FMT](../../userspace-api/media/v4l/vidioc-g-fmt.md#vidioc-g-fmt) ioctl logic for metadata capture

`vidioc_try_fmt_meta_out`
:   pointer to the function that implements
    [VIDIOC_TRY_FMT](../../userspace-api/media/v4l/vidioc-g-fmt.md#vidioc-g-fmt) ioctl logic for metadata output

`vidioc_reqbufs`
:   pointer to the function that implements
    [VIDIOC_REQBUFS](../../userspace-api/media/v4l/vidioc-reqbufs.md#vidioc-reqbufs) ioctl

`vidioc_querybuf`
:   pointer to the function that implements
    [VIDIOC_QUERYBUF](../../userspace-api/media/v4l/vidioc-querybuf.md#vidioc-querybuf) ioctl

`vidioc_qbuf`
:   pointer to the function that implements
    [VIDIOC_QBUF](../../userspace-api/media/v4l/vidioc-qbuf.md#vidioc-qbuf) ioctl

`vidioc_expbuf`
:   pointer to the function that implements
    [VIDIOC_EXPBUF](../../userspace-api/media/v4l/vidioc-expbuf.md#vidioc-expbuf) ioctl

`vidioc_dqbuf`
:   pointer to the function that implements
    [VIDIOC_DQBUF](../../userspace-api/media/v4l/vidioc-qbuf.md#vidioc-qbuf) ioctl

`vidioc_create_bufs`
:   pointer to the function that implements
    [VIDIOC_CREATE_BUFS](../../userspace-api/media/v4l/vidioc-create-bufs.md#vidioc-create-bufs) ioctl

`vidioc_prepare_buf`
:   pointer to the function that implements
    [VIDIOC_PREPARE_BUF](../../userspace-api/media/v4l/vidioc-prepare-buf.md#vidioc-prepare-buf) ioctl

`vidioc_overlay`
:   pointer to the function that implements
    [VIDIOC_OVERLAY](../../userspace-api/media/v4l/vidioc-overlay.md#vidioc-overlay) ioctl

`vidioc_g_fbuf`
:   pointer to the function that implements
    [VIDIOC_G_FBUF](../../userspace-api/media/v4l/vidioc-g-fbuf.md#vidioc-g-fbuf) ioctl

`vidioc_s_fbuf`
:   pointer to the function that implements
    [VIDIOC_S_FBUF](../../userspace-api/media/v4l/vidioc-g-fbuf.md#vidioc-g-fbuf) ioctl

`vidioc_streamon`
:   pointer to the function that implements
    [VIDIOC_STREAMON](../../userspace-api/media/v4l/vidioc-streamon.md#vidioc-streamon) ioctl

`vidioc_streamoff`
:   pointer to the function that implements
    [VIDIOC_STREAMOFF](../../userspace-api/media/v4l/vidioc-streamon.md#vidioc-streamon) ioctl

`vidioc_g_std`
:   pointer to the function that implements
    [VIDIOC_G_STD](../../userspace-api/media/v4l/vidioc-g-std.md#vidioc-g-std) ioctl

`vidioc_s_std`
:   pointer to the function that implements
    [VIDIOC_S_STD](../../userspace-api/media/v4l/vidioc-g-std.md#vidioc-g-std) ioctl

`vidioc_querystd`
:   pointer to the function that implements
    [VIDIOC_QUERYSTD](../../userspace-api/media/v4l/vidioc-querystd.md#vidioc-querystd) ioctl

`vidioc_enum_input`
:   pointer to the function that implements
    [VIDIOC_ENUM_INPUT](../../userspace-api/media/v4l/vidioc-g-input.md#vidioc-g-input) ioctl

`vidioc_g_input`
:   pointer to the function that implements
    [VIDIOC_G_INPUT](../../userspace-api/media/v4l/vidioc-g-input.md#vidioc-g-input) ioctl

`vidioc_s_input`
:   pointer to the function that implements
    [VIDIOC_S_INPUT](../../userspace-api/media/v4l/vidioc-g-input.md#vidioc-g-input) ioctl

`vidioc_enum_output`
:   pointer to the function that implements
    [VIDIOC_ENUM_OUTPUT](../../userspace-api/media/v4l/vidioc-g-output.md#vidioc-g-output) ioctl

`vidioc_g_output`
:   pointer to the function that implements
    [VIDIOC_G_OUTPUT](../../userspace-api/media/v4l/vidioc-g-output.md#vidioc-g-output) ioctl

`vidioc_s_output`
:   pointer to the function that implements
    [VIDIOC_S_OUTPUT](../../userspace-api/media/v4l/vidioc-g-output.md#vidioc-g-output) ioctl

`vidioc_queryctrl`
:   pointer to the function that implements
    [VIDIOC_QUERYCTRL](../../userspace-api/media/v4l/vidioc-queryctrl.md#vidioc-queryctrl) ioctl

`vidioc_query_ext_ctrl`
:   pointer to the function that implements
    [VIDIOC_QUERY_EXT_CTRL](../../userspace-api/media/v4l/vidioc-queryctrl.md#vidioc-queryctrl) ioctl

`vidioc_g_ctrl`
:   pointer to the function that implements
    [VIDIOC_G_CTRL](../../userspace-api/media/v4l/vidioc-g-ctrl.md#vidioc-g-ctrl) ioctl

`vidioc_s_ctrl`
:   pointer to the function that implements
    [VIDIOC_S_CTRL](../../userspace-api/media/v4l/vidioc-g-ctrl.md#vidioc-g-ctrl) ioctl

`vidioc_g_ext_ctrls`
:   pointer to the function that implements
    [VIDIOC_G_EXT_CTRLS](../../userspace-api/media/v4l/vidioc-g-ext-ctrls.md#vidioc-g-ext-ctrls) ioctl

`vidioc_s_ext_ctrls`
:   pointer to the function that implements
    [VIDIOC_S_EXT_CTRLS](../../userspace-api/media/v4l/vidioc-g-ext-ctrls.md#vidioc-g-ext-ctrls) ioctl

`vidioc_try_ext_ctrls`
:   pointer to the function that implements
    [VIDIOC_TRY_EXT_CTRLS](../../userspace-api/media/v4l/vidioc-g-ext-ctrls.md#vidioc-g-ext-ctrls) ioctl

`vidioc_querymenu`
:   pointer to the function that implements
    [VIDIOC_QUERYMENU](../../userspace-api/media/v4l/vidioc-queryctrl.md#vidioc-queryctrl) ioctl

`vidioc_enumaudio`
:   pointer to the function that implements
    [VIDIOC_ENUMAUDIO](../../userspace-api/media/v4l/vidioc-enumaudio.md#vidioc-enumaudio) ioctl

`vidioc_g_audio`
:   pointer to the function that implements
    [VIDIOC_G_AUDIO](../../userspace-api/media/v4l/vidioc-g-audio.md#vidioc-g-audio) ioctl

`vidioc_s_audio`
:   pointer to the function that implements
    [VIDIOC_S_AUDIO](../../userspace-api/media/v4l/vidioc-g-audio.md#vidioc-g-audio) ioctl

`vidioc_enumaudout`
:   pointer to the function that implements
    [VIDIOC_ENUMAUDOUT](../../userspace-api/media/v4l/vidioc-enumaudioout.md#vidioc-enumaudout) ioctl

`vidioc_g_audout`
:   pointer to the function that implements
    [VIDIOC_G_AUDOUT](../../userspace-api/media/v4l/vidioc-g-audioout.md#vidioc-g-audout) ioctl

`vidioc_s_audout`
:   pointer to the function that implements
    [VIDIOC_S_AUDOUT](../../userspace-api/media/v4l/vidioc-g-audioout.md#vidioc-g-audout) ioctl

`vidioc_g_modulator`
:   pointer to the function that implements
    [VIDIOC_G_MODULATOR](../../userspace-api/media/v4l/vidioc-g-modulator.md#vidioc-g-modulator) ioctl

`vidioc_s_modulator`
:   pointer to the function that implements
    [VIDIOC_S_MODULATOR](../../userspace-api/media/v4l/vidioc-g-modulator.md#vidioc-g-modulator) ioctl

`vidioc_g_pixelaspect`
:   pointer to the function that implements
    the pixelaspect part of the [VIDIOC_CROPCAP](../../userspace-api/media/v4l/vidioc-cropcap.md#vidioc-cropcap) ioctl

`vidioc_g_selection`
:   pointer to the function that implements
    [VIDIOC_G_SELECTION](../../userspace-api/media/v4l/vidioc-g-selection.md#vidioc-g-selection) ioctl

`vidioc_s_selection`
:   pointer to the function that implements
    [VIDIOC_S_SELECTION](../../userspace-api/media/v4l/vidioc-g-selection.md#vidioc-g-selection) ioctl

`vidioc_g_jpegcomp`
:   pointer to the function that implements
    [VIDIOC_G_JPEGCOMP](../../userspace-api/media/v4l/vidioc-g-jpegcomp.md#vidioc-g-jpegcomp) ioctl

`vidioc_s_jpegcomp`
:   pointer to the function that implements
    [VIDIOC_S_JPEGCOMP](../../userspace-api/media/v4l/vidioc-g-jpegcomp.md#vidioc-g-jpegcomp) ioctl

`vidioc_g_enc_index`
:   pointer to the function that implements
    [VIDIOC_G_ENC_INDEX](../../userspace-api/media/v4l/vidioc-g-enc-index.md#vidioc-g-enc-index) ioctl

`vidioc_encoder_cmd`
:   pointer to the function that implements
    [VIDIOC_ENCODER_CMD](../../userspace-api/media/v4l/vidioc-encoder-cmd.md#vidioc-encoder-cmd) ioctl

`vidioc_try_encoder_cmd`
:   pointer to the function that implements
    [VIDIOC_TRY_ENCODER_CMD](../../userspace-api/media/v4l/vidioc-encoder-cmd.md#vidioc-encoder-cmd) ioctl

`vidioc_decoder_cmd`
:   pointer to the function that implements
    [VIDIOC_DECODER_CMD](../../userspace-api/media/v4l/vidioc-decoder-cmd.md#vidioc-decoder-cmd) ioctl

`vidioc_try_decoder_cmd`
:   pointer to the function that implements
    [VIDIOC_TRY_DECODER_CMD](../../userspace-api/media/v4l/vidioc-decoder-cmd.md#vidioc-decoder-cmd) ioctl

`vidioc_g_parm`
:   pointer to the function that implements
    [VIDIOC_G_PARM](../../userspace-api/media/v4l/vidioc-g-parm.md#vidioc-g-parm) ioctl

`vidioc_s_parm`
:   pointer to the function that implements
    [VIDIOC_S_PARM](../../userspace-api/media/v4l/vidioc-g-parm.md#vidioc-g-parm) ioctl

`vidioc_g_tuner`
:   pointer to the function that implements
    [VIDIOC_G_TUNER](../../userspace-api/media/v4l/vidioc-g-tuner.md#vidioc-g-tuner) ioctl

`vidioc_s_tuner`
:   pointer to the function that implements
    [VIDIOC_S_TUNER](../../userspace-api/media/v4l/vidioc-g-tuner.md#vidioc-g-tuner) ioctl

`vidioc_g_frequency`
:   pointer to the function that implements
    [VIDIOC_G_FREQUENCY](../../userspace-api/media/v4l/vidioc-g-frequency.md#vidioc-g-frequency) ioctl

`vidioc_s_frequency`
:   pointer to the function that implements
    [VIDIOC_S_FREQUENCY](../../userspace-api/media/v4l/vidioc-g-frequency.md#vidioc-g-frequency) ioctl

`vidioc_enum_freq_bands`
:   pointer to the function that implements
    [VIDIOC_ENUM_FREQ_BANDS](../../userspace-api/media/v4l/vidioc-enum-freq-bands.md#vidioc-enum-freq-bands) ioctl

`vidioc_g_sliced_vbi_cap`
:   pointer to the function that implements
    [VIDIOC_G_SLICED_VBI_CAP](../../userspace-api/media/v4l/vidioc-g-sliced-vbi-cap.md#vidioc-g-sliced-vbi-cap) ioctl

`vidioc_log_status`
:   pointer to the function that implements
    [VIDIOC_LOG_STATUS](../../userspace-api/media/v4l/vidioc-log-status.md#vidioc-log-status) ioctl

`vidioc_s_hw_freq_seek`
:   pointer to the function that implements
    [VIDIOC_S_HW_FREQ_SEEK](../../userspace-api/media/v4l/vidioc-s-hw-freq-seek.md#vidioc-s-hw-freq-seek) ioctl

`vidioc_g_register`
:   pointer to the function that implements
    [VIDIOC_DBG_G_REGISTER](../../userspace-api/media/v4l/vidioc-dbg-g-register.md#vidioc-dbg-g-register) ioctl

`vidioc_s_register`
:   pointer to the function that implements
    [VIDIOC_DBG_S_REGISTER](../../userspace-api/media/v4l/vidioc-dbg-g-register.md#vidioc-dbg-g-register) ioctl

`vidioc_g_chip_info`
:   pointer to the function that implements
    [VIDIOC_DBG_G_CHIP_INFO](../../userspace-api/media/v4l/vidioc-dbg-g-chip-info.md#vidioc-dbg-g-chip-info) ioctl

`vidioc_enum_framesizes`
:   pointer to the function that implements
    [VIDIOC_ENUM_FRAMESIZES](../../userspace-api/media/v4l/vidioc-enum-framesizes.md#vidioc-enum-framesizes) ioctl

`vidioc_enum_frameintervals`
:   pointer to the function that implements
    [VIDIOC_ENUM_FRAMEINTERVALS](../../userspace-api/media/v4l/vidioc-enum-frameintervals.md#vidioc-enum-frameintervals) ioctl

`vidioc_s_dv_timings`
:   pointer to the function that implements
    [VIDIOC_S_DV_TIMINGS](../../userspace-api/media/v4l/vidioc-g-dv-timings.md#vidioc-g-dv-timings) ioctl

`vidioc_g_dv_timings`
:   pointer to the function that implements
    [VIDIOC_G_DV_TIMINGS](../../userspace-api/media/v4l/vidioc-g-dv-timings.md#vidioc-g-dv-timings) ioctl

`vidioc_query_dv_timings`
:   pointer to the function that implements
    [VIDIOC_QUERY_DV_TIMINGS](../../userspace-api/media/v4l/vidioc-query-dv-timings.md#vidioc-query-dv-timings) ioctl

`vidioc_enum_dv_timings`
:   pointer to the function that implements
    [VIDIOC_ENUM_DV_TIMINGS](../../userspace-api/media/v4l/vidioc-enum-dv-timings.md#vidioc-enum-dv-timings) ioctl

`vidioc_dv_timings_cap`
:   pointer to the function that implements
    [VIDIOC_DV_TIMINGS_CAP](../../userspace-api/media/v4l/vidioc-dv-timings-cap.md#vidioc-dv-timings-cap) ioctl

`vidioc_g_edid`
:   pointer to the function that implements
    [VIDIOC_G_EDID](../../userspace-api/media/v4l/vidioc-g-edid.md#vidioc-g-edid) ioctl

`vidioc_s_edid`
:   pointer to the function that implements
    [VIDIOC_S_EDID](../../userspace-api/media/v4l/vidioc-g-edid.md#vidioc-g-edid) ioctl

`vidioc_subscribe_event`
:   pointer to the function that implements
    [VIDIOC_SUBSCRIBE_EVENT](../../userspace-api/media/v4l/vidioc-subscribe-event.md#vidioc-subscribe-event) ioctl

`vidioc_unsubscribe_event`
:   pointer to the function that implements
    [VIDIOC_UNSUBSCRIBE_EVENT](../../userspace-api/media/v4l/vidioc-subscribe-event.md#vidioc-unsubscribe-event) ioctl

`vidioc_default`
:   pointed used to allow other ioctls

const char \*v4l2_norm_to_name(v4l2_std_id id)
:   Ancillary routine to analog TV standard name from its ID.

**Parameters**

`v4l2_std_id id`
:   analog TV standard ID.

**Return**

returns a string with the name of the analog TV standard.
If the standard is not found or if **id** points to multiple standard,
it returns "Unknown".

void v4l2_video_std_frame_period(int id, struct v4l2_fract \*frameperiod)
:   Ancillary routine that fills a struct `v4l2_fract` pointer with the default framerate fraction.

**Parameters**

`int id`
:   analog TV standard ID.

`struct v4l2_fract *frameperiod`
:   struct `v4l2_fract` pointer to be filled

int v4l2_video_std_construct(struct v4l2_standard \*vs, int id, const char \*name)
:   Ancillary routine that fills in the fields of a `v4l2_standard` structure according to the **id** parameter.

**Parameters**

`struct v4l2_standard *vs`
:   struct `v4l2_standard` pointer to be filled

`int id`
:   analog TV standard ID.

`const char *name`
:   name of the standard to be used

**Description**

> **Note:**
>
> This ancillary routine is obsolete. Shouldn't be used on newer drivers.

int v4l_video_std_enumstd(struct v4l2_standard \*vs, v4l2_std_id id)
:   Ancillary routine that fills in the fields of a `v4l2_standard` structure according to the **id** and **vs->index** parameters.

**Parameters**

`struct v4l2_standard *vs`
:   struct `v4l2_standard` pointer to be filled.

`v4l2_std_id id`
:   analog TV standard ID.

void v4l_printk_ioctl(const char \*prefix, unsigned int cmd)
:   Ancillary routine that prints the ioctl in a human-readable format.

**Parameters**

`const char *prefix`
:   prefix to be added at the ioctl prints.

`unsigned int cmd`
:   ioctl name

**Description**

> **Note:**
>
> If prefix != `NULL`, then it will issue a
> ``` printk(KERN_DEBUG "``s ```: ", prefix)`` first.

long int v4l2_compat_ioctl32(struct [file](v4l2-common.md#c.v4l2_compat_ioctl32 "file") \*file, unsigned int cmd, unsigned long arg)
:   32 Bits compatibility layer for 64 bits processors

**Parameters**

`struct file *file`
:   Pointer to struct `file`.

`unsigned int cmd`
:   Ioctl name.

`unsigned long arg`
:   Ioctl argument.

v4l2_kioctl
:   **Typedef**: Typedef used to pass an ioctl handler.

**Syntax**

> `long v4l2_kioctl (struct file *file, unsigned int cmd, void *arg)`

**Parameters**

`struct file *file`
:   Pointer to struct `file`.

`unsigned int cmd`
:   Ioctl name.

`void *arg`
:   Ioctl argument.

long int video_usercopy(struct [file](v4l2-common.md#c.video_usercopy "file") \*file, unsigned int cmd, unsigned long int arg, [v4l2_kioctl](v4l2-common.md#c.v4l2_kioctl "v4l2_kioctl") func)
:   copies data from/to userspace memory when an ioctl is issued.

**Parameters**

`struct file *file`
:   Pointer to struct `file`.

`unsigned int cmd`
:   Ioctl name.

`unsigned long int arg`
:   Ioctl argument.

`v4l2_kioctl func`
:   function that will handle the ioctl

**Description**

> **Note:**
>
> This routine should be used only inside the V4L2 core.

long int video_ioctl2(struct [file](v4l2-common.md#c.video_ioctl2 "file") \*file, unsigned int cmd, unsigned long int arg)
:   Handles a V4L2 ioctl.

**Parameters**

`struct file *file`
:   Pointer to struct `file`.

`unsigned int cmd`
:   Ioctl name.

`unsigned long int arg`
:   Ioctl argument.

**Description**

Method used to hancle an ioctl. Should be used to fill the
[`v4l2_ioctl_ops.unlocked_ioctl`](v4l2-common.md#c.v4l2_ioctl_ops "v4l2_ioctl_ops") on all V4L2 drivers.
