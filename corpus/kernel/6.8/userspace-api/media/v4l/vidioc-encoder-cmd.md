---
collection: kernel
version: "6.8"
title: "7.10. ioctl VIDIOC_ENCODER_CMD, VIDIOC_TRY_ENCODER_CMD"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/vidioc-encoder-cmd.html
fetched_at: 2026-08-21T03:40:38+00:00
---
# 7.10. ioctl VIDIOC_ENCODER_CMD, VIDIOC_TRY_ENCODER_CMD

## 7.10.1. Name

VIDIOC_ENCODER_CMD - VIDIOC_TRY_ENCODER_CMD - Execute an encoder command

## 7.10.2. Synopsis

VIDIOC_ENCODER_CMD

`int ioctl(int fd, VIDIOC_ENCODER_CMD, struct v4l2_encoder_cmd *argp)`

VIDIOC_TRY_ENCODER_CMD

`int ioctl(int fd, VIDIOC_TRY_ENCODER_CMD, struct v4l2_encoder_cmd *argp)`

## 7.10.3. Arguments

`fd`
:   File descriptor returned by [`open()`](func-open.md#c.V4L.open "open").

`argp`
:   Pointer to struct [`v4l2_encoder_cmd`](vidioc-encoder-cmd.md#c.V4L.v4l2_encoder_cmd "v4l2_encoder_cmd").

## 7.10.4. Description

These ioctls control an audio/video (usually MPEG-) encoder.
`VIDIOC_ENCODER_CMD` sends a command to the encoder,
`VIDIOC_TRY_ENCODER_CMD` can be used to try a command without actually
executing it.

To send a command applications must initialize all fields of a struct
[`v4l2_encoder_cmd`](vidioc-encoder-cmd.md#c.V4L.v4l2_encoder_cmd "v4l2_encoder_cmd") and call
`VIDIOC_ENCODER_CMD` or `VIDIOC_TRY_ENCODER_CMD` with a pointer to
this structure.

The `cmd` field must contain the command code. Some commands use the
`flags` field for additional information.

After a STOP command, [`read()`](func-read.md#c.V4L.read "read") calls will read
the remaining data buffered by the driver. When the buffer is empty,
[`read()`](func-read.md#c.V4L.read "read") will return zero and the next [`read()`](func-read.md#c.V4L.read "read")
call will restart the encoder.

A [`read()`](func-read.md#c.V4L.read "read") or [VIDIOC_STREAMON](vidioc-streamon.md#vidioc-streamon)
call sends an implicit START command to the encoder if it has not been
started yet. Applies to both queues of mem2mem encoders.

A [`close()`](func-close.md#c.V4L.close "close") or [VIDIOC_STREAMOFF](vidioc-streamon.md#vidioc-streamon)
call of a streaming file descriptor sends an implicit immediate STOP to
the encoder, and all buffered data is discarded. Applies to both queues of
mem2mem encoders.

These ioctls are optional, not all drivers may support them. They were
introduced in Linux 2.6.21. They are, however, mandatory for stateful mem2mem
encoders (as further documented in [Memory-to-Memory Stateful Video Encoder Interface](dev-encoder.md#encoder)).

type v4l2_encoder_cmd

struct v4l2_encoder_cmd

|  |  |  |
| --- | --- | --- |
| __u32 | `cmd` | The encoder command, see [Encoder Commands](vidioc-encoder-cmd.md#encoder-cmds). |
| __u32 | `flags` | Flags to go with the command, see [Encoder Command Flags](vidioc-encoder-cmd.md#encoder-flags). If no flags are defined for this command, drivers and applications must set this field to zero. |
| __u32 | `data`[8] | Reserved for future extensions. Drivers and applications must set the array to zero. |

Encoder Commands

|  |  |  |
| --- | --- | --- |
| `V4L2_ENC_CMD_START` | 0 | Start the encoder. When the encoder is already running or paused, this command does nothing. No flags are defined for this command.  For a device implementing the [Memory-to-Memory Stateful Video Encoder Interface](dev-encoder.md#encoder), once the drain sequence is initiated with the `V4L2_ENC_CMD_STOP` command, it must be driven to completion before this command can be invoked. Any attempt to invoke the command while the drain sequence is in progress will trigger an `EBUSY` error code. See [Memory-to-Memory Stateful Video Encoder Interface](dev-encoder.md#encoder) for more details. |
| `V4L2_ENC_CMD_STOP` | 1 | Stop the encoder. When the `V4L2_ENC_CMD_STOP_AT_GOP_END` flag is set, encoding will continue until the end of the current *Group Of Pictures*, otherwise encoding will stop immediately. When the encoder is already stopped, this command does nothing.  For a device implementing the [Memory-to-Memory Stateful Video Encoder Interface](dev-encoder.md#encoder), the command will initiate the drain sequence as documented in [Memory-to-Memory Stateful Video Encoder Interface](dev-encoder.md#encoder). No flags or other arguments are accepted in this case. Any attempt to invoke the command again before the sequence completes will trigger an `EBUSY` error code. |
| `V4L2_ENC_CMD_PAUSE` | 2 | Pause the encoder. When the encoder has not been started yet, the driver will return an `EPERM` error code. When the encoder is already paused, this command does nothing. No flags are defined for this command. |
| `V4L2_ENC_CMD_RESUME` | 3 | Resume encoding after a PAUSE command. When the encoder has not been started yet, the driver will return an `EPERM` error code. When the encoder is already running, this command does nothing. No flags are defined for this command. |

Encoder Command Flags

|  |  |  |
| --- | --- | --- |
| `V4L2_ENC_CMD_STOP_AT_GOP_END` | 0x0001 | Stop encoding at the end of the current *Group Of Pictures*, rather than immediately.  Does not apply to [Memory-to-Memory Stateful Video Encoder Interface](dev-encoder.md#encoder). |

## 7.10.5. Return Value

On success 0 is returned, on error -1 and the `errno` variable is set
appropriately. The generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

EBUSY
:   A drain sequence of a device implementing the [Memory-to-Memory Stateful Video Encoder Interface](dev-encoder.md#encoder) is still in
    progress. It is not allowed to issue another encoder command until it
    completes.

EINVAL
:   The `cmd` field is invalid.

EPERM
:   The application sent a PAUSE or RESUME command when the encoder was
    not running.
