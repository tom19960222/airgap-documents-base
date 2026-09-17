---
collection: kernel
version: "6.17"
title: "drm/nouveau NVIDIA GPU Driver"
source_url: https://www.kernel.org/doc/html/v6.17/gpu/nouveau.html
fetched_at: 2026-09-16T16:39:30+00:00
---
# drm/nouveau NVIDIA GPU Driver

The drm/nouveau driver provides support for a wide range of NVIDIA GPUs,
covering GeForce, Quadro, and Tesla series, from the NV04 architecture up
to the latest Turing, Ampere, Ada families.

## NVKM: NVIDIA Kernel Manager

The NVKM component serves as the core abstraction layer within the nouveau
driver, responsible for managing NVIDIA GPU hardware at the kernel level.
NVKM provides a unified interface for handling various GPU architectures.

It enables resource management, power control, memory handling, and command
submission required for the proper functioning of NVIDIA GPUs under the
nouveau driver.

NVKM plays a critical role in abstracting hardware complexities and
providing a consistent API to upper layers of the driver stack.

### GSP Support

<https://github.com/NVIDIA/open-gpu-kernel-modules/blob/535/src/nvidia/inc/kernel/gpu/gsp/message_queue_priv.h>

The GSP command queue and status queue are message queues for the
communication between software and GSP. The software submits the GSP
RPC via the GSP command queue, GSP writes the status of the submitted
RPC in the status queue.

A GSP message queue element consists of three parts:

- message element header (`struct r535_gsp_msg`), which mostly maintains
  the metadata for queuing the element.
- RPC message header (`struct nvfw_gsp_rpc`), which maintains the info
  of the RPC. E.g., the RPC function number.
- The payload, where the RPC message stays. E.g. the params of a
  specific RPC function. Some RPC functions also have their headers
  in the payload. E.g. rm_alloc, rm_control.

The memory layout of a GSP message element can be illustrated below:

```
+------------------------+
| Message Element Header |
|    (r535_gsp_msg)      |
|                        |
| (r535_gsp_msg.data)    |
|          |             |
|----------V-------------|
|    GSP RPC Header      |
|    (nvfw_gsp_rpc)      |
|                        |
| (nvfw_gsp_rpc.data)    |
|          |             |
|----------V-------------|
|       Payload          |
|                        |
|   header(optional)     |
|        params          |
+------------------------+
```

The max size of a message queue element is 16 pages (including the
headers). When a GSP message to be sent is larger than 16 pages, the
message should be split into multiple elements and sent accordingly.

In the bunch of the split elements, the first element has the expected
function number, while the rest of the elements are sent with the
function number NV_VGPU_MSG_FUNCTION_CONTINUATION_RECORD.

GSP consumes the elements from the cmdq and always writes the result
back to the msgq. The result is also formed as split elements.

Terminology:

- gsp_msg(msg): GSP message element (element header + GSP RPC header +
  payload)
- gsp_rpc(rpc): GSP RPC (RPC header + payload)
- gsp_rpc_buf: buffer for (GSP RPC header + payload)
- gsp_rpc_len: size of (GSP RPC header + payload)
- params_size: size of params in the payload
- payload_size: size of (header if exists + params) in the payload

When sending a GSP RPC command, there can be multiple cases of handling
the GSP RPC messages, which are the reply of GSP RPC commands, according
to the requirement of the callers and the nature of the GSP RPC commands.

NVKM_GSP_RPC_REPLY_NOWAIT - If specified, immediately return to the
caller after the GSP RPC command is issued.

NVKM_GSP_RPC_REPLY_RECV - If specified, wait and receive the entire GSP
RPC message after the GSP RPC command is issued.

NVKM_GSP_RPC_REPLY_POLL - If specified, wait for the specific reply and
discard the reply before returning to the caller.
