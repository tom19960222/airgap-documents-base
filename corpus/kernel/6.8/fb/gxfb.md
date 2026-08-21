---
collection: kernel
version: "6.8"
title: "What is gxfb?"
source_url: https://www.kernel.org/doc/html/v6.8/fb/gxfb.html
fetched_at: 2026-08-21T03:48:23+00:00
---
# What is gxfb?

This is a graphics framebuffer driver for AMD Geode GX2 based processors.

Advantages:

> - No need to use AMD's VSA code (or other VESA emulation layer) in the
>   BIOS.
> - It provides a nice large console (128 cols + 48 lines with 1024x768)
>   without using tiny, unreadable fonts.
> - You can run XF68_FBDev on top of /dev/fb0
> - Most important: boot logo :-)

Disadvantages:

> - graphic mode is slower than text mode...

## How to use it?

Switching modes is done using gxfb.mode_option=<resolution>... boot
parameter or using fbset program.

See [modedb default video mode support](modedb.md) for more information on modedb
resolutions.

## X11

XF68_FBDev should generally work fine, but it is non-accelerated.

## Configuration

You can pass kernel command line options to gxfb with gxfb.<option>.
For example, [gxfb.mode_option=800x600@75](mailto:gxfb.mode_option=800x600%4075).
Accepted options:

|  |  |
| --- | --- |
| mode_option | specify the video mode. Of the form <x>x<y>[-<bpp>][@<refresh>] |
| vram | size of video ram (normally auto-detected) |
| vt_switch | enable vt switching during suspend/resume. The vt switch is slow, but harmless. |

Andres Salomon <[dilinger@debian.org](mailto:dilinger%40debian.org)>
