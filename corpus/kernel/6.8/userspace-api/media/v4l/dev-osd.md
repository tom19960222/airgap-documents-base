---
collection: kernel
version: "6.8"
title: "4.4. Video Output Overlay Interface"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/dev-osd.html
fetched_at: 2026-08-21T03:57:30+00:00
---
# 4.4. Video Output Overlay Interface

**Also known as On-Screen Display (OSD)**

Some video output devices can overlay a framebuffer image onto the
outgoing video signal. Applications can set up such an overlay using
this interface, which borrows structures and ioctls of the
[Video Overlay](dev-overlay.md#overlay) interface.

The OSD function is accessible through the same character special file
as the [Video Output](dev-capture.md#capture) function.

> **Note:**
>
> The default function of such a `/dev/video` device is video
> capturing or output. The OSD function is only available after calling
> the [VIDIOC_S_FMT](vidioc-g-fmt.md#vidioc-g-fmt) ioctl.

## 4.4.1. Querying Capabilities

Devices supporting the *Video Output Overlay* interface set the
`V4L2_CAP_VIDEO_OUTPUT_OVERLAY` flag in the `capabilities` field of
struct `v4l2_capability` returned by the
[ioctl VIDIOC_QUERYCAP](vidioc-querycap.md#vidioc-querycap) ioctl.

## 4.4.2. Framebuffer

Contrary to the *Video Overlay* interface the framebuffer is normally
implemented on the TV card and not the graphics card. On Linux it is
accessible as a framebuffer device (`/dev/fbN`). Given a V4L2 device,
applications can find the corresponding framebuffer device by calling
the [VIDIOC_G_FBUF](vidioc-g-fbuf.md#vidioc-g-fbuf) ioctl. It returns, amongst
other information, the physical address of the framebuffer in the
`base` field of struct `v4l2_framebuffer`.
The framebuffer device ioctl `FBIOGET_FSCREENINFO` returns the same
address in the `smem_start` field of struct
`fb_fix_screeninfo`. The `FBIOGET_FSCREENINFO`
ioctl and struct `fb_fix_screeninfo` are defined in
the `linux/fb.h` header file.

The width and height of the framebuffer depends on the current video
standard. A V4L2 driver may reject attempts to change the video standard
(or any other ioctl which would imply a framebuffer size change) with an
`EBUSY` error code until all applications closed the framebuffer device.

### 4.4.2.1. Example: Finding a framebuffer device for OSD

```c
#include <linux/fb.h>

struct v4l2_framebuffer fbuf;
unsigned int i;
int fb_fd;

if (-1 == ioctl(fd, VIDIOC_G_FBUF, &fbuf)) {
    perror("VIDIOC_G_FBUF");
    exit(EXIT_FAILURE);
}

for (i = 0; i < 30; i++) {
    char dev_name[16];
    struct fb_fix_screeninfo si;

    snprintf(dev_name, sizeof(dev_name), "/dev/fb%u", i);

    fb_fd = open(dev_name, O_RDWR);
    if (-1 == fb_fd) {
        switch (errno) {
        case ENOENT: /* no such file */
        case ENXIO:  /* no driver */
            continue;

        default:
            perror("open");
            exit(EXIT_FAILURE);
        }
    }

    if (0 == ioctl(fb_fd, FBIOGET_FSCREENINFO, &si)) {
        if (si.smem_start == (unsigned long)fbuf.base)
            break;
    } else {
        /* Apparently not a framebuffer device. */
    }

    close(fb_fd);
    fb_fd = -1;
}

/* fb_fd is the file descriptor of the framebuffer device
   for the video output overlay, or -1 if no device was found. */
```

## 4.4.3. Overlay Window and Scaling

The overlay is controlled by source and target rectangles. The source
rectangle selects a subsection of the framebuffer image to be overlaid,
the target rectangle an area in the outgoing video signal where the
image will appear. Drivers may or may not support scaling, and arbitrary
sizes and positions of these rectangles. Further drivers may support any
(or none) of the clipping/blending methods defined for the
[Video Overlay](dev-overlay.md#overlay) interface.

A struct [`v4l2_window`](dev-overlay.md#c.v4l2_window "v4l2_window") defines the size of the
source rectangle, its position in the framebuffer and the
clipping/blending method to be used for the overlay. To get the current
parameters applications set the `type` field of a struct
`v4l2_format` to
`V4L2_BUF_TYPE_VIDEO_OUTPUT_OVERLAY` and call the
[VIDIOC_G_FMT](vidioc-g-fmt.md#vidioc-g-fmt) ioctl. The driver fills the
struct [`v4l2_window`](dev-overlay.md#c.v4l2_window "v4l2_window") substructure named `win`. It is not
possible to retrieve a previously programmed clipping list or bitmap.

To program the source rectangle applications set the `type` field of a
struct `v4l2_format` to
`V4L2_BUF_TYPE_VIDEO_OUTPUT_OVERLAY`, initialize the `win`
substructure and call the [VIDIOC_S_FMT](vidioc-g-fmt.md#vidioc-g-fmt) ioctl.
The driver adjusts the parameters against hardware limits and returns
the actual parameters as [VIDIOC_G_FMT](vidioc-g-fmt.md#vidioc-g-fmt) does. Like [VIDIOC_S_FMT](vidioc-g-fmt.md#vidioc-g-fmt),
the [VIDIOC_TRY_FMT](vidioc-g-fmt.md#vidioc-g-fmt) ioctl can be used to learn
about driver capabilities without actually changing driver state. Unlike
[VIDIOC_S_FMT](vidioc-g-fmt.md#vidioc-g-fmt) this also works after the overlay has been enabled.

A struct `v4l2_crop` defines the size and position
of the target rectangle. The scaling factor of the overlay is implied by
the width and height given in struct [`v4l2_window`](dev-overlay.md#c.v4l2_window "v4l2_window")
and struct `v4l2_crop`. The cropping API applies to
*Video Output* and *Video Output Overlay* devices in the same way as to
*Video Capture* and *Video Overlay* devices, merely reversing the
direction of the data flow. For more information see [Image Cropping, Insertion and Scaling -- the CROP API](crop.md#crop).

## 4.4.4. Enabling Overlay

There is no V4L2 ioctl to enable or disable the overlay, however the
framebuffer interface of the driver may support the `FBIOBLANK` ioctl.
