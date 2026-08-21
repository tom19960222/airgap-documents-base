---
collection: kernel
version: "6.8"
title: "Frame Buffer Library"
source_url: https://www.kernel.org/doc/html/v6.8/driver-api/frame-buffer.html
fetched_at: 2026-08-21T03:30:37+00:00
---
# Frame Buffer Library

The frame buffer drivers depend heavily on four data structures. These
structures are declared in include/linux/fb.h. They are fb_info,
fb_var_screeninfo, fb_fix_screeninfo and fb_monospecs. The last
three can be made available to and from userland.

fb_info defines the current state of a particular video card. Inside
fb_info, there exists a fb_ops structure which is a collection of
needed functions to make fbdev and fbcon work. fb_info is only visible
to the kernel.

fb_var_screeninfo is used to describe the features of a video card
that are user defined. With fb_var_screeninfo, things such as depth
and the resolution may be defined.

The next structure is fb_fix_screeninfo. This defines the properties
of a card that are created when a mode is set and can't be changed
otherwise. A good example of this is the start of the frame buffer
memory. This "locks" the address of the frame buffer memory, so that it
cannot be changed or moved.

The last structure is fb_monospecs. In the old API, there was little
importance for fb_monospecs. This allowed for forbidden things such as
setting a mode of 800x600 on a fix frequency monitor. With the new API,
fb_monospecs prevents such things, and if used correctly, can prevent a
monitor from being cooked. fb_monospecs will not be useful until
kernels 2.5.x.

## Frame Buffer Memory

int register_framebuffer(struct [fb_info](frame-buffer.md#c.register_framebuffer "fb_info") \*fb_info)
:   registers a frame buffer device

**Parameters**

`struct fb_info *fb_info`
:   frame buffer info structure

    Registers a frame buffer device **fb_info**.

    Returns negative errno on error, or zero for success.

void unregister_framebuffer(struct [fb_info](frame-buffer.md#c.unregister_framebuffer "fb_info") \*fb_info)
:   releases a frame buffer device

**Parameters**

`struct fb_info *fb_info`
:   frame buffer info structure

    Unregisters a frame buffer device **fb_info**.

    Returns negative errno on error, or zero for success.

    This function will also notify the framebuffer console
    to release the driver.

    This is meant to be called within a driver's [`module_exit()`](basics.md#c.module_exit "module_exit")
    function. If this is called outside [`module_exit()`](basics.md#c.module_exit "module_exit"), ensure
    that the driver implements fb_open() and fb_release() to
    check that no processes are using the device.

void fb_set_suspend(struct fb_info \*info, int state)
:   low level driver signals suspend

**Parameters**

`struct fb_info *info`
:   framebuffer affected

`int state`
:   0 = resuming, !=0 = suspending

    This is meant to be used by low level drivers to
    signal suspend/resume to the core & clients.
    It must be called with the console semaphore held

## Frame Buffer Colormap

void fb_dealloc_cmap(struct fb_cmap \*cmap)
:   deallocate a colormap

**Parameters**

`struct fb_cmap *cmap`
:   frame buffer colormap structure

    Deallocates a colormap that was previously allocated with
    fb_alloc_cmap().

int fb_copy_cmap(const struct fb_cmap \*from, struct fb_cmap \*to)
:   copy a colormap

**Parameters**

`const struct fb_cmap *from`
:   frame buffer colormap structure

`struct fb_cmap *to`
:   frame buffer colormap structure

    Copy contents of colormap from **from** to **to**.

int fb_set_cmap(struct fb_cmap \*cmap, struct fb_info \*info)
:   set the colormap

**Parameters**

`struct fb_cmap *cmap`
:   frame buffer colormap structure

`struct fb_info *info`
:   frame buffer info structure

    Sets the colormap **cmap** for a screen of device **info**.

    Returns negative errno on error, or zero on success.

const struct fb_cmap \*fb_default_cmap(int len)
:   get default colormap

**Parameters**

`int len`
:   size of palette for a depth

    Gets the default colormap for a specific screen depth. **len**
    is the size of the palette for a particular screen depth.

    Returns pointer to a frame buffer colormap structure.

void fb_invert_cmaps(void)
:   invert all defaults colormaps

**Parameters**

`void`
:   no arguments

**Description**

> Invert all default colormaps.

## Frame Buffer Video Mode Database

int fb_try_mode(struct fb_var_screeninfo \*var, struct fb_info \*info, const struct fb_videomode \*mode, unsigned int bpp)
:   test a video mode

**Parameters**

`struct fb_var_screeninfo *var`
:   frame buffer user defined part of display

`struct fb_info *info`
:   frame buffer info structure

`const struct fb_videomode *mode`
:   frame buffer video mode structure

`unsigned int bpp`
:   color depth in bits per pixel

    Tries a video mode to test it's validity for device **info**.

    Returns 1 on success.

void fb_delete_videomode(const struct fb_videomode \*mode, struct list_head \*head)
:   removed videomode entry from modelist

**Parameters**

`const struct fb_videomode *mode`
:   videomode to remove

`struct list_head *head`
:   struct list_head of modelist

**NOTES**

Will remove all matching mode entries

int fb_find_mode(struct fb_var_screeninfo \*var, struct fb_info \*info, const char \*mode_option, const struct fb_videomode \*db, unsigned int dbsize, const struct fb_videomode \*default_mode, unsigned int default_bpp)
:   finds a valid video mode

**Parameters**

`struct fb_var_screeninfo *var`
:   frame buffer user defined part of display

`struct fb_info *info`
:   frame buffer info structure

`const char *mode_option`
:   string video mode to find

`const struct fb_videomode *db`
:   video mode database

`unsigned int dbsize`
:   size of **db**

`const struct fb_videomode *default_mode`
:   default video mode to fall back to

`unsigned int default_bpp`
:   default color depth in bits per pixel

**Description**

Finds a suitable video mode, starting with the specified mode
in **mode_option** with fallback to **default_mode**. If
**default_mode** fails, all modes in the video mode database will
be tried.

Valid mode specifiers for **mode_option**:

```
<xres>x<yres>[M][R][-<bpp>][@<refresh>][i][p][m]
```

or

```
<name>[-<bpp>][@<refresh>]
```

with <xres>, <yres>, <bpp> and <refresh> decimal numbers and
<name> a string.

If 'M' is present after yres (and before refresh/bpp if present),
the function will compute the timings using VESA(tm) Coordinated
Video Timings (CVT). If 'R' is present after 'M', will compute with
reduced blanking (for flatpanels). If 'i' or 'p' are present, compute
interlaced or progressive mode. If 'm' is present, add margins equal
to 1.8% of xres rounded down to 8 pixels, and 1.8% of yres. The char
'i', 'p' and 'm' must be after 'M' and 'R'. Example:

```
1024x768MR-8@60m - Reduced blank with margins at 60Hz.
```

Returns zero for failure, 1 if using specified **mode_option**,
2 if using specified **mode_option** with an ignored refresh rate,
3 if default mode is used, 4 if fall back to any valid mode.

**NOTE**

The passed struct **var** is _not_ cleared! This allows you
to supply values for e.g. the grayscale and accel_flags fields.

void fb_var_to_videomode(struct fb_videomode \*mode, const struct fb_var_screeninfo \*var)
:   convert fb_var_screeninfo to fb_videomode

**Parameters**

`struct fb_videomode *mode`
:   pointer to struct fb_videomode

`const struct fb_var_screeninfo *var`
:   pointer to struct fb_var_screeninfo

void fb_videomode_to_var(struct fb_var_screeninfo \*var, const struct fb_videomode \*mode)
:   convert fb_videomode to fb_var_screeninfo

**Parameters**

`struct fb_var_screeninfo *var`
:   pointer to struct fb_var_screeninfo

`const struct fb_videomode *mode`
:   pointer to struct fb_videomode

int fb_mode_is_equal(const struct fb_videomode \*mode1, const struct fb_videomode \*mode2)
:   compare 2 videomodes

**Parameters**

`const struct fb_videomode *mode1`
:   first videomode

`const struct fb_videomode *mode2`
:   second videomode

**Return**

1 if equal, 0 if not

const struct fb_videomode \*fb_find_best_mode(const struct fb_var_screeninfo \*var, struct list_head \*head)
:   find best matching videomode

**Parameters**

`const struct fb_var_screeninfo *var`
:   pointer to struct fb_var_screeninfo

`struct list_head *head`
:   pointer to struct list_head of modelist

**Return**

struct fb_videomode, NULL if none found

**Description**

IMPORTANT:
This function assumes that all modelist entries in
info->modelist are valid.

**NOTES**

Finds best matching videomode which has an equal or greater dimension than
var->xres and var->yres. If more than 1 videomode is found, will return
the videomode with the highest refresh rate

const struct fb_videomode \*fb_find_nearest_mode(const struct fb_videomode \*mode, struct list_head \*head)
:   find closest videomode

**Parameters**

`const struct fb_videomode *mode`
:   pointer to struct fb_videomode

`struct list_head *head`
:   pointer to modelist

**Description**

Finds best matching videomode, smaller or greater in dimension.
If more than 1 videomode is found, will return the videomode with
the closest refresh rate.

const struct fb_videomode \*fb_match_mode(const struct fb_var_screeninfo \*var, struct list_head \*head)
:   find a videomode which exactly matches the timings in var

**Parameters**

`const struct fb_var_screeninfo *var`
:   pointer to struct fb_var_screeninfo

`struct list_head *head`
:   pointer to struct list_head of modelist

**Return**

struct fb_videomode, NULL if none found

int fb_add_videomode(const struct fb_videomode \*mode, struct list_head \*head)
:   adds videomode entry to modelist

**Parameters**

`const struct fb_videomode *mode`
:   videomode to add

`struct list_head *head`
:   struct list_head of modelist

**NOTES**

Will only add unmatched mode entries

void fb_destroy_modelist(struct list_head \*head)
:   destroy modelist

**Parameters**

`struct list_head *head`
:   struct list_head of modelist

void fb_videomode_to_modelist(const struct fb_videomode \*modedb, int num, struct list_head \*head)
:   convert mode array to mode list

**Parameters**

`const struct fb_videomode *modedb`
:   array of struct fb_videomode

`int num`
:   number of entries in array

`struct list_head *head`
:   struct list_head of modelist

## Frame Buffer Macintosh Video Mode Database

int mac_vmode_to_var(int vmode, int cmode, struct fb_var_screeninfo \*var)
:   converts vmode/cmode pair to var structure

**Parameters**

`int vmode`
:   MacOS video mode

`int cmode`
:   MacOS color mode

`struct fb_var_screeninfo *var`
:   frame buffer video mode structure

    Converts a MacOS vmode/cmode pair to a frame buffer video
    mode structure.

    Returns negative errno on error, or zero for success.

int mac_map_monitor_sense(int sense)
:   Convert monitor sense to vmode

**Parameters**

`int sense`
:   Macintosh monitor sense number

    Converts a Macintosh monitor sense number to a MacOS
    vmode number.

    Returns MacOS vmode video mode number.

int mac_find_mode(struct fb_var_screeninfo \*var, struct fb_info \*info, const char \*mode_option, unsigned int default_bpp)
:   find a video mode

**Parameters**

`struct fb_var_screeninfo *var`
:   frame buffer user defined part of display

`struct fb_info *info`
:   frame buffer info structure

`const char *mode_option`
:   video mode name (see mac_modedb[])

`unsigned int default_bpp`
:   default color depth in bits per pixel

    Finds a suitable video mode. Tries to set mode specified
    by **mode_option**. If the name of the wanted mode begins with
    'mac', the Mac video mode database will be used, otherwise it
    will fall back to the standard video mode database.

**Note**

Function marked as __init and can only be used during
:   system boot.

    Returns error code from fb_find_mode (see fb_find_mode
    function).

## Frame Buffer Fonts

Refer to the file lib/fonts/fonts.c for more information.
