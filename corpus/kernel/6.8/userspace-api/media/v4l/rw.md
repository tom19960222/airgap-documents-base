---
collection: kernel
version: "6.8"
title: "3.1. Read/Write"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/rw.html
fetched_at: 2026-08-21T03:57:27+00:00
---
# 3.1. Read/Write

Input and output devices support the [`read()`](func-read.md#c.V4L.read "read") and
[`write()`](func-write.md#c.V4L.write "write") function, respectively, when the
`V4L2_CAP_READWRITE` flag in the `capabilities` field of struct
[`v4l2_capability`](vidioc-querycap.md#c.V4L.v4l2_capability "v4l2_capability") returned by the
[ioctl VIDIOC_QUERYCAP](vidioc-querycap.md#vidioc-querycap) ioctl is set.

Drivers may need the CPU to copy the data, but they may also support DMA
to or from user memory, so this I/O method is not necessarily less
efficient than other methods merely exchanging buffer pointers. It is
considered inferior though because no meta-information like frame
counters or timestamps are passed. This information is necessary to
recognize frame dropping and to synchronize with other data streams.
However this is also the simplest I/O method, requiring little or no
setup to exchange data. It permits command line stunts like this (the
vidctrl tool is fictitious):

```
$ vidctrl /dev/video --input=0 --format=YUYV --size=352x288
$ dd if=/dev/video of=myimage.422 bs=202752 count=1
```

To read from the device applications use the [`read()`](func-read.md#c.V4L.read "read")
function, to write the [`write()`](func-write.md#c.V4L.write "write") function. Drivers
must implement one I/O method if they exchange data with applications,
but it need not be this. [1](rw.md#f1) When reading or writing is supported, the
driver must also support the [`select()`](func-select.md#c.V4L.select "select") and
[`poll()`](func-poll.md#c.V4L.poll "poll") function. [2](rw.md#f2)

[1](rw.md#id1)
:   It would be desirable if applications could depend on drivers
    supporting all I/O interfaces, but as much as the complex memory
    mapping I/O can be inadequate for some devices we have no reason to
    require this interface, which is most useful for simple applications
    capturing still images.

[2](rw.md#id2)
:   At the driver level [`select()`](func-select.md#c.V4L.select "select") and [`poll()`](func-poll.md#c.V4L.poll "poll") are
    the same, and [`select()`](func-select.md#c.V4L.select "select") is too important to be optional.
