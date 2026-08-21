---
collection: kernel
version: "6.8"
title: "7.65. ioctl VIDIOC_SUBSCRIBE_EVENT, VIDIOC_UNSUBSCRIBE_EVENT"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/vidioc-subscribe-event.html
fetched_at: 2026-08-21T03:40:39+00:00
---
# 7.65. ioctl VIDIOC_SUBSCRIBE_EVENT, VIDIOC_UNSUBSCRIBE_EVENT

## 7.65.1. Name

VIDIOC_SUBSCRIBE_EVENT - VIDIOC_UNSUBSCRIBE_EVENT - Subscribe or unsubscribe event

## 7.65.2. Synopsis

VIDIOC_SUBSCRIBE_EVENT

`int ioctl(int fd, VIDIOC_SUBSCRIBE_EVENT, struct v4l2_event_subscription *argp)`

VIDIOC_UNSUBSCRIBE_EVENT

`int ioctl(int fd, VIDIOC_UNSUBSCRIBE_EVENT, struct v4l2_event_subscription *argp)`

## 7.65.3. Arguments

`fd`
:   File descriptor returned by [`open()`](func-open.md#c.V4L.open "open").

`argp`
:   Pointer to struct [`v4l2_event_subscription`](vidioc-subscribe-event.md#c.V4L.v4l2_event_subscription "v4l2_event_subscription").

## 7.65.4. Description

Subscribe or unsubscribe V4L2 event. Subscribed events are dequeued by
using the [ioctl VIDIOC_DQEVENT](vidioc-dqevent.md#vidioc-dqevent) ioctl.

type v4l2_event_subscription

struct v4l2_event_subscription

|  |  |  |
| --- | --- | --- |
| __u32 | `type` | Type of the event, see [Event Types](vidioc-dqevent.md#event-type).  **Note:** `V4L2_EVENT_ALL` can be used with [VIDIOC_UNSUBSCRIBE_EVENT](vidioc-subscribe-event.md#vidioc-subscribe-event) for unsubscribing all events at once. |
| __u32 | `id` | ID of the event source. If there is no ID associated with the event source, then set this to 0. Whether or not an event needs an ID depends on the event type. |
| __u32 | `flags` | Event flags, see [Event Flags](vidioc-subscribe-event.md#event-flags). |
| __u32 | `reserved`[5] | Reserved for future extensions. Drivers and applications must set the array to zero. |

Event Flags

|  |  |  |
| --- | --- | --- |
| `V4L2_EVENT_SUB_FL_SEND_INITIAL` | 0x0001 | When this event is subscribed an initial event will be sent containing the current status. This only makes sense for events that are triggered by a status change such as `V4L2_EVENT_CTRL`. Other events will ignore this flag. |
| `V4L2_EVENT_SUB_FL_ALLOW_FEEDBACK` | 0x0002 | If set, then events directly caused by an ioctl will also be sent to the filehandle that called that ioctl. For example, changing a control using [VIDIOC_S_CTRL](vidioc-g-ctrl.md#vidioc-g-ctrl) will cause a V4L2_EVENT_CTRL to be sent back to that same filehandle. Normally such events are suppressed to prevent feedback loops where an application changes a control to a one value and then another, and then receives an event telling it that that control has changed to the first value.  Since it can't tell whether that event was caused by another application or by the [VIDIOC_S_CTRL](vidioc-g-ctrl.md#vidioc-g-ctrl) call it is hard to decide whether to set the control to the value in the event, or ignore it.  Think carefully when you set this flag so you won't get into situations like that. |

## 7.65.5. Return Value

On success 0 is returned, on error -1 and the `errno` variable is set
appropriately. The generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.
