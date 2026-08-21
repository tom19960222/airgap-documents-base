---
collection: kernel
version: "6.8"
title: "5.8. ioctl MEDIA_IOC_SETUP_LINK"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/mediactl/media-ioc-setup-link.html
fetched_at: 2026-08-21T03:39:58+00:00
---
# 5.8. ioctl MEDIA_IOC_SETUP_LINK

## 5.8.1. Name

MEDIA_IOC_SETUP_LINK - Modify the properties of a link

## 5.8.2. Synopsis

MEDIA_IOC_SETUP_LINK

`int ioctl(int fd, MEDIA_IOC_SETUP_LINK, struct media_link_desc *argp)`

## 5.8.3. Arguments

`fd`
:   File descriptor returned by [`open()`](media-func-open.md#c.MC.open "open").

`argp`
:   Pointer to struct [`media_link_desc`](media-ioc-enum-links.md#c.MC.media_link_desc "media_link_desc").

## 5.8.4. Description

To change link properties applications fill a struct
[`media_link_desc`](media-ioc-enum-links.md#c.MC.media_link_desc "media_link_desc") with link identification
information (source and sink pad) and the new requested link flags. They
then call the MEDIA_IOC_SETUP_LINK ioctl with a pointer to that
structure.

The only configurable property is the `ENABLED` link flag to
enable/disable a link. Links marked with the `IMMUTABLE` link flag can
not be enabled or disabled.

Link configuration has no side effect on other links. If an enabled link
at the sink pad prevents the link from being enabled, the driver returns
with an `EBUSY` error code.

Only links marked with the `DYNAMIC` link flag can be enabled/disabled
while streaming media data. Attempting to enable or disable a streaming
non-dynamic link will return an `EBUSY` error code.

If the specified link can't be found the driver returns with an `EINVAL`
error code.

## 5.8.5. Return Value

On success 0 is returned, on error -1 and the `errno` variable is set
appropriately. The generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

EINVAL
:   The struct [`media_link_desc`](media-ioc-enum-links.md#c.MC.media_link_desc "media_link_desc") references a
    non-existing link, or the link is immutable and an attempt to modify
    its configuration was made.
