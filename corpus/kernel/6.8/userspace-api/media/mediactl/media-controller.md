---
collection: kernel
version: "6.8"
title: "Part IV - Media Controller API"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/mediactl/media-controller.html
fetched_at: 2026-08-21T03:35:38+00:00
---
# Part IV - Media Controller API

Table of Contents

- [1. Introduction](media-controller-intro.md)
- [2. Media device model](media-controller-model.md)
- [3. Types and flags used to represent the media graph elements](media-types.md)
- [4. Request API](request-api.md)
  - [4.1. General Usage](request-api.md#general-usage)
  - [4.2. Request Allocation](request-api.md#request-allocation)
  - [4.3. Request Preparation](request-api.md#request-preparation)
  - [4.4. Request Submission](request-api.md#request-submission)
  - [4.5. Recycling and Destruction](request-api.md#recycling-and-destruction)
  - [4.6. Example for a Codec Device](request-api.md#example-for-a-codec-device)
  - [4.7. Example for a Simple Capture Device](request-api.md#example-for-a-simple-capture-device)
- [5. Function Reference](media-funcs.md)
  - [5.1. media open()](media-func-open.md)
    - [5.1.1. Name](media-func-open.md#name)
    - [5.1.2. Synopsis](media-func-open.md#synopsis)
    - [5.1.3. Arguments](media-func-open.md#arguments)
    - [5.1.4. Description](media-func-open.md#description)
    - [5.1.5. Return Value](media-func-open.md#return-value)
  - [5.2. media close()](media-func-close.md)
    - [5.2.1. Name](media-func-close.md#name)
    - [5.2.2. Synopsis](media-func-close.md#synopsis)
    - [5.2.3. Arguments](media-func-close.md#arguments)
    - [5.2.4. Description](media-func-close.md#description)
    - [5.2.5. Return Value](media-func-close.md#return-value)
  - [5.3. media ioctl()](media-func-ioctl.md)
    - [5.3.1. Name](media-func-ioctl.md#name)
    - [5.3.2. Synopsis](media-func-ioctl.md#synopsis)
    - [5.3.3. Arguments](media-func-ioctl.md#arguments)
    - [5.3.4. Description](media-func-ioctl.md#description)
    - [5.3.5. Return Value](media-func-ioctl.md#return-value)
  - [5.4. ioctl MEDIA_IOC_DEVICE_INFO](media-ioc-device-info.md)
    - [5.4.1. Name](media-ioc-device-info.md#name)
    - [5.4.2. Synopsis](media-ioc-device-info.md#synopsis)
    - [5.4.3. Arguments](media-ioc-device-info.md#arguments)
    - [5.4.4. Description](media-ioc-device-info.md#description)
    - [5.4.5. Return Value](media-ioc-device-info.md#return-value)
  - [5.5. ioctl MEDIA_IOC_G_TOPOLOGY](media-ioc-g-topology.md)
    - [5.5.1. Name](media-ioc-g-topology.md#name)
    - [5.5.2. Synopsis](media-ioc-g-topology.md#synopsis)
    - [5.5.3. Arguments](media-ioc-g-topology.md#arguments)
    - [5.5.4. Description](media-ioc-g-topology.md#description)
    - [5.5.5. Return Value](media-ioc-g-topology.md#return-value)
  - [5.6. ioctl MEDIA_IOC_ENUM_ENTITIES](media-ioc-enum-entities.md)
    - [5.6.1. Name](media-ioc-enum-entities.md#name)
    - [5.6.2. Synopsis](media-ioc-enum-entities.md#synopsis)
    - [5.6.3. Arguments](media-ioc-enum-entities.md#arguments)
    - [5.6.4. Description](media-ioc-enum-entities.md#description)
    - [5.6.5. Return Value](media-ioc-enum-entities.md#return-value)
  - [5.7. ioctl MEDIA_IOC_ENUM_LINKS](media-ioc-enum-links.md)
    - [5.7.1. Name](media-ioc-enum-links.md#name)
    - [5.7.2. Synopsis](media-ioc-enum-links.md#synopsis)
    - [5.7.3. Arguments](media-ioc-enum-links.md#arguments)
    - [5.7.4. Description](media-ioc-enum-links.md#description)
    - [5.7.5. Return Value](media-ioc-enum-links.md#return-value)
  - [5.8. ioctl MEDIA_IOC_SETUP_LINK](media-ioc-setup-link.md)
    - [5.8.1. Name](media-ioc-setup-link.md#name)
    - [5.8.2. Synopsis](media-ioc-setup-link.md#synopsis)
    - [5.8.3. Arguments](media-ioc-setup-link.md#arguments)
    - [5.8.4. Description](media-ioc-setup-link.md#description)
    - [5.8.5. Return Value](media-ioc-setup-link.md#return-value)
  - [5.9. ioctl MEDIA_IOC_REQUEST_ALLOC](media-ioc-request-alloc.md)
    - [5.9.1. Name](media-ioc-request-alloc.md#name)
    - [5.9.2. Synopsis](media-ioc-request-alloc.md#synopsis)
    - [5.9.3. Arguments](media-ioc-request-alloc.md#arguments)
    - [5.9.4. Description](media-ioc-request-alloc.md#description)
    - [5.9.5. Return Value](media-ioc-request-alloc.md#return-value)
  - [5.10. request close()](request-func-close.md)
    - [5.10.1. Name](request-func-close.md#name)
    - [5.10.2. Synopsis](request-func-close.md#synopsis)
    - [5.10.3. Arguments](request-func-close.md#arguments)
    - [5.10.4. Description](request-func-close.md#description)
    - [5.10.5. Return Value](request-func-close.md#return-value)
  - [5.11. request ioctl()](request-func-ioctl.md)
    - [5.11.1. Name](request-func-ioctl.md#name)
    - [5.11.2. Synopsis](request-func-ioctl.md#synopsis)
    - [5.11.3. Arguments](request-func-ioctl.md#arguments)
    - [5.11.4. Description](request-func-ioctl.md#description)
    - [5.11.5. Return Value](request-func-ioctl.md#return-value)
  - [5.12. request poll()](request-func-poll.md)
    - [5.12.1. Name](request-func-poll.md#name)
    - [5.12.2. Synopsis](request-func-poll.md#synopsis)
    - [5.12.3. Arguments](request-func-poll.md#arguments)
    - [5.12.4. Description](request-func-poll.md#description)
    - [5.12.5. Return Value](request-func-poll.md#return-value)
  - [5.13. ioctl MEDIA_REQUEST_IOC_QUEUE](media-request-ioc-queue.md)
    - [5.13.1. Name](media-request-ioc-queue.md#name)
    - [5.13.2. Synopsis](media-request-ioc-queue.md#synopsis)
    - [5.13.3. Arguments](media-request-ioc-queue.md#arguments)
    - [5.13.4. Description](media-request-ioc-queue.md#description)
    - [5.13.5. Return Value](media-request-ioc-queue.md#return-value)
  - [5.14. ioctl MEDIA_REQUEST_IOC_REINIT](media-request-ioc-reinit.md)
    - [5.14.1. Name](media-request-ioc-reinit.md#name)
    - [5.14.2. Synopsis](media-request-ioc-reinit.md#synopsis)
    - [5.14.3. Arguments](media-request-ioc-reinit.md#arguments)
    - [5.14.4. Description](media-request-ioc-reinit.md#description)
    - [5.14.5. Return Value](media-request-ioc-reinit.md#return-value)
- [6. Media Controller Header File](media-header.md)
  - [6.1. media.h](media-header.md#media-h)

## Revision and Copyright

Authors:

- Pinchart, Laurent <[laurent.pinchart@ideasonboard.com](mailto:laurent.pinchart%40ideasonboard.com)>

> - Initial version.

- Carvalho Chehab, Mauro <[mchehab@kernel.org](mailto:mchehab%40kernel.org)>

> - MEDIA_IOC_G_TOPOLOGY documentation and documentation improvements.

**Copyright** © 2010 : Laurent Pinchart

**Copyright** © 2015-2016 : Mauro Carvalho Chehab

## Revision History

revision
:   1.1.0 / 2015-12-12 (*mcc*)

revision
:   1.0.0 / 2010-11-10 (*lp*)

Initial revision
