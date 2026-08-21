---
collection: kernel
version: "6.8"
title: "HID-BPF"
source_url: https://www.kernel.org/doc/html/v6.8/hid/hid-bpf.html
fetched_at: 2026-08-21T03:39:47+00:00
---
# HID-BPF

HID is a standard protocol for input devices but some devices may require
custom tweaks, traditionally done with a kernel driver fix. Using the eBPF
capabilities instead speeds up development and adds new capabilities to the
existing HID interfaces.

- [When (and why) to use HID-BPF](hid-bpf.md#when-and-why-to-use-hid-bpf)

  - [Dead zone of a joystick](hid-bpf.md#dead-zone-of-a-joystick)
  - [Simple fixup of report descriptor](hid-bpf.md#simple-fixup-of-report-descriptor)
  - [Add a new feature that requires a new kernel API](hid-bpf.md#add-a-new-feature-that-requires-a-new-kernel-api)
  - [Morph a device into something else and control that from userspace](hid-bpf.md#morph-a-device-into-something-else-and-control-that-from-userspace)
  - [Firewall](hid-bpf.md#firewall)
  - [Tracing](hid-bpf.md#tracing)
- [High-level view of HID-BPF](hid-bpf.md#high-level-view-of-hid-bpf)
- [Available types of programs](hid-bpf.md#available-types-of-programs)
- [Developer API:](hid-bpf.md#developer-api)

  - [User API data structures available in programs:](hid-bpf.md#user-api-data-structures-available-in-programs)
  - [Available tracing functions to attach a HID-BPF program:](hid-bpf.md#available-tracing-functions-to-attach-a-hid-bpf-program)
  - [Available API that can be used in all HID-BPF programs:](hid-bpf.md#available-api-that-can-be-used-in-all-hid-bpf-programs)
  - [Available API that can be used in syscall HID-BPF programs:](hid-bpf.md#available-api-that-can-be-used-in-syscall-hid-bpf-programs)
- [General overview of a HID-BPF program](hid-bpf.md#general-overview-of-a-hid-bpf-program)

  - [Accessing the data attached to the context](hid-bpf.md#accessing-the-data-attached-to-the-context)
  - [Effect of a HID-BPF program](hid-bpf.md#effect-of-a-hid-bpf-program)
- [Attaching a bpf program to a device](hid-bpf.md#attaching-a-bpf-program-to-a-device)
- [An (almost) complete example of a BPF enhanced HID device](hid-bpf.md#an-almost-complete-example-of-a-bpf-enhanced-hid-device)

  - [Filtering events](hid-bpf.md#filtering-events)
  - [Controlling the device](hid-bpf.md#controlling-the-device)

## [When (and why) to use HID-BPF](hid-bpf.md#id1)

There are several use cases when using HID-BPF is better
than standard kernel driver fix:

### [Dead zone of a joystick](hid-bpf.md#id2)

Assuming you have a joystick that is getting older, it is common to see it
wobbling around its neutral point. This is usually filtered at the application
level by adding a *dead zone* for this specific axis.

With HID-BPF, we can apply this filtering in the kernel directly so userspace
does not get woken up when nothing else is happening on the input controller.

Of course, given that this dead zone is specific to an individual device, we
can not create a generic fix for all of the same joysticks. Adding a custom
kernel API for this (e.g. by adding a sysfs entry) does not guarantee this new
kernel API will be broadly adopted and maintained.

HID-BPF allows the userspace program to load the program itself, ensuring we
only load the custom API when we have a user.

### [Simple fixup of report descriptor](hid-bpf.md#id3)

In the HID tree, half of the drivers only fix one key or one byte
in the report descriptor. These fixes all require a kernel patch and the
subsequent shepherding into a release, a long and painful process for users.

We can reduce this burden by providing an eBPF program instead. Once such a
program has been verified by the user, we can embed the source code into the
kernel tree and ship the eBPF program and load it directly instead of loading
a specific kernel module for it.

Note: distribution of eBPF programs and their inclusion in the kernel is not
yet fully implemented

### [Add a new feature that requires a new kernel API](hid-bpf.md#id4)

An example for such a feature are the Universal Stylus Interface (USI) pens.
Basically, USI pens require a new kernel API because there are new
channels of communication that our HID and input stack do not support.
Instead of using hidraw or creating new sysfs entries or ioctls, we can rely
on eBPF to have the kernel API controlled by the consumer and to not
impact the performances by waking up userspace every time there is an
event.

### [Morph a device into something else and control that from userspace](hid-bpf.md#id5)

The kernel has a relatively static mapping of HID items to evdev bits.
It cannot decide to dynamically transform a given device into something else
as it does not have the required context and any such transformation cannot be
undone (or even discovered) by userspace.

However, some devices are useless with that static way of defining devices. For
example, the Microsoft Surface Dial is a pushbutton with haptic feedback that
is barely usable as of today.

With eBPF, userspace can morph that device into a mouse, and convert the dial
events into wheel events. Also, the userspace program can set/unset the haptic
feedback depending on the context. For example, if a menu is visible on the
screen we likely need to have a haptic click every 15 degrees. But when
scrolling in a web page the user experience is better when the device emits
events at the highest resolution.

### [Firewall](hid-bpf.md#id6)

What if we want to prevent other users to access a specific feature of a
device? (think a possibly broken firmware update entry point)

With eBPF, we can intercept any HID command emitted to the device and
validate it or not.

This also allows to sync the state between the userspace and the
kernel/bpf program because we can intercept any incoming command.

### [Tracing](hid-bpf.md#id7)

The last usage is tracing events and all the fun we can do we BPF to summarize
and analyze events.

Right now, tracing relies on hidraw. It works well except for a couple
of issues:

1. if the driver doesn't export a hidraw node, we can't trace anything
   (eBPF will be a "god-mode" there, so this may raise some eyebrows)
2. hidraw doesn't catch other processes' requests to the device, which
   means that we have cases where we need to add printks to the kernel
   to understand what is happening.

## [High-level view of HID-BPF](hid-bpf.md#id8)

The main idea behind HID-BPF is that it works at an array of bytes level.
Thus, all of the parsing of the HID report and the HID report descriptor
must be implemented in the userspace component that loads the eBPF
program.

For example, in the dead zone joystick from above, knowing which fields
in the data stream needs to be set to `0` needs to be computed by userspace.

A corollary of this is that HID-BPF doesn't know about the other subsystems
available in the kernel. *You can not directly emit input event through the
input API from eBPF*.

When a BPF program needs to emit input events, it needs to talk with the HID
protocol, and rely on the HID kernel processing to translate the HID data into
input events.

## [Available types of programs](hid-bpf.md#id9)

HID-BPF is built "on top" of BPF, meaning that we use tracing method to
declare our programs.

HID-BPF has the following attachment types available:

1. event processing/filtering with `SEC("fmod_ret/hid_bpf_device_event")` in libbpf
2. actions coming from userspace with `SEC("syscall")` in libbpf
3. change of the report descriptor with `SEC("fmod_ret/hid_bpf_rdesc_fixup")` in libbpf

A `hid_bpf_device_event` is calling a BPF program when an event is received from
the device. Thus we are in IRQ context and can act on the data or notify userspace.
And given that we are in IRQ context, we can not talk back to the device.

A `syscall` means that userspace called the syscall `BPF_PROG_RUN` facility.
This time, we can do any operations allowed by HID-BPF, and talking to the device is
allowed.

Last, `hid_bpf_rdesc_fixup` is different from the others as there can be only one
BPF program of this type. This is called on `probe` from the driver and allows to
change the report descriptor from the BPF program. Once a `hid_bpf_rdesc_fixup`
program has been loaded, it is not possible to overwrite it unless the program which
inserted it allows us by pinning the program and closing all of its fds pointing to it.

## [Developer API:](hid-bpf.md#id10)

### [User API data structures available in programs:](hid-bpf.md#id11)

struct hid_bpf_ctx
:   User accessible data for all HID programs

**Definition**:

```
struct hid_bpf_ctx {
    __u32 index;
    const struct hid_device *hid;
    __u32 allocated_size;
    enum hid_report_type report_type;
    union {
        __s32 retval;
        __s32 size;
    };
};
```

**Members**

`index`
:   program index in the jump table. No special meaning (a smaller index
    doesn't mean the program will be executed before another program with
    a bigger index).

`hid`
:   the `struct hid_device` representing the device itself

`allocated_size`
:   Allocated size of data.

    This is how much memory is available and can be requested
    by the HID program.
    Note that for `HID_BPF_RDESC_FIXUP`, that memory is set to
    `4096` (4 KB)

`report_type`
:   used for `hid_bpf_device_event()`

`{unnamed_union}`
:   anonymous

`retval`
:   Return value of the previous program.

`size`
:   Valid data in the data field.

    Programs can get the available valid size in data by fetching this field.
    Programs can also change this value by returning a positive number in the
    program.
    To discard the event, return a negative error code.

    `size` must always be less or equal than `allocated_size` (it is enforced
    once all BPF programs have been run).

**Description**

`data` is not directly accessible from the context. We need to issue
a call to `hid_bpf_get_data()` in order to get a pointer to that field.

All of these fields are currently read-only.

enum hid_bpf_attach_flags
:   flags used when attaching a HIF-BPF program

**Constants**

`HID_BPF_FLAG_NONE`
:   no specific flag is used, the kernel choses where to
    insert the program

`HID_BPF_FLAG_INSERT_HEAD`
:   insert the given program before any other program
    currently attached to the device. This doesn't
    guarantee that this program will always be first

`HID_BPF_FLAG_MAX`
:   sentinel value, not to be used by the callers

### [Available tracing functions to attach a HID-BPF program:](hid-bpf.md#id12)

noinline int hid_bpf_device_event(struct [hid_bpf_ctx](hid-bpf.md#c.hid_bpf_ctx "hid_bpf_ctx") \*ctx)
:   Called whenever an event is coming in from the device

**Parameters**

`struct hid_bpf_ctx *ctx`
:   The HID-BPF context

**Description**

**return** `0` on success and keep processing; a positive value to change the
incoming size buffer; a negative error code to interrupt the processing
of this event

Declare an `fmod_ret` tracing bpf program to this function and attach this
program through [`hid_bpf_attach_prog()`](hid-bpf.md#c.hid_bpf_attach_prog "hid_bpf_attach_prog") to have this helper called for
any incoming event from the device itself.

The function is called while on IRQ context, so we can not sleep.

noinline int hid_bpf_rdesc_fixup(struct [hid_bpf_ctx](hid-bpf.md#c.hid_bpf_ctx "hid_bpf_ctx") \*ctx)
:   Called when the probe function parses the report descriptor of the HID device

**Parameters**

`struct hid_bpf_ctx *ctx`
:   The HID-BPF context

**Description**

**return** 0 on success and keep processing; a positive value to change the
incoming size buffer; a negative error code to interrupt the processing
of this event

Declare an `fmod_ret` tracing bpf program to this function and attach this
program through [`hid_bpf_attach_prog()`](hid-bpf.md#c.hid_bpf_attach_prog "hid_bpf_attach_prog") to have this helper called before any
parsing of the report descriptor by HID.

### [Available API that can be used in all HID-BPF programs:](hid-bpf.md#id13)

__bpf_kfunc __u8 \*hid_bpf_get_data(struct [hid_bpf_ctx](hid-bpf.md#c.hid_bpf_ctx "hid_bpf_ctx") \*ctx, unsigned int offset, const size_t rdwr_buf_size)
:   Get the kernel memory pointer associated with the context **ctx**

**Parameters**

`struct hid_bpf_ctx *ctx`
:   The HID-BPF context

`unsigned int offset`
:   The offset within the memory

`const size_t rdwr_buf_size`
:   the const size of the buffer

**Description**

**returns** `NULL` on error, an `__u8` memory pointer on success

### [Available API that can be used in syscall HID-BPF programs:](hid-bpf.md#id14)

__bpf_kfunc int hid_bpf_attach_prog(unsigned int hid_id, int prog_fd, __u32 flags)
:   Attach the given **prog_fd** to the given HID device

**Parameters**

`unsigned int hid_id`
:   the system unique identifier of the HID device

`int prog_fd`
:   an fd in the user process representing the program to attach

`__u32 flags`
:   any logical OR combination of [`enum hid_bpf_attach_flags`](hid-bpf.md#c.hid_bpf_attach_flags "hid_bpf_attach_flags")

**Description**

**returns** an fd of a bpf_link object on success (> `0`), an error code otherwise.
Closing this fd will detach the program from the HID device (unless the bpf_link
is pinned to the BPF file system).

__bpf_kfunc struct [hid_bpf_ctx](hid-bpf.md#c.hid_bpf_ctx "hid_bpf_ctx") \*hid_bpf_allocate_context(unsigned int hid_id)
:   Allocate a context to the given HID device

**Parameters**

`unsigned int hid_id`
:   the system unique identifier of the HID device

**Description**

**returns** A pointer to [`struct hid_bpf_ctx`](hid-bpf.md#c.hid_bpf_ctx "hid_bpf_ctx") on success, `NULL` on error.

__bpf_kfunc void hid_bpf_release_context(struct [hid_bpf_ctx](hid-bpf.md#c.hid_bpf_ctx "hid_bpf_ctx") \*ctx)
:   Release the previously allocated context **ctx**

**Parameters**

`struct hid_bpf_ctx *ctx`
:   the HID-BPF context to release

__bpf_kfunc int hid_bpf_hw_request(struct [hid_bpf_ctx](hid-bpf.md#c.hid_bpf_ctx "hid_bpf_ctx") \*ctx, __u8 \*buf, size_t buf__sz, enum hid_report_type rtype, enum hid_class_request reqtype)
:   Communicate with a HID device

**Parameters**

`struct hid_bpf_ctx *ctx`
:   the HID-BPF context previously allocated in [`hid_bpf_allocate_context()`](hid-bpf.md#c.hid_bpf_allocate_context "hid_bpf_allocate_context")

`__u8 *buf`
:   a `PTR_TO_MEM` buffer

`size_t buf__sz`
:   the size of the data to transfer

`enum hid_report_type rtype`
:   the type of the report (`HID_INPUT_REPORT`, `HID_FEATURE_REPORT`, `HID_OUTPUT_REPORT`)

`enum hid_class_request reqtype`
:   the type of the request (`HID_REQ_GET_REPORT`, `HID_REQ_SET_REPORT`, ...)

**Description**

**returns** `0` on success, a negative error code otherwise.

## [General overview of a HID-BPF program](hid-bpf.md#id15)

### [Accessing the data attached to the context](hid-bpf.md#id16)

The `struct hid_bpf_ctx` doesn't export the `data` fields directly and to access
it, a bpf program needs to first call [`hid_bpf_get_data()`](hid-bpf.md#c.hid_bpf_get_data "hid_bpf_get_data").

`offset` can be any integer, but `size` needs to be constant, known at compile
time.

This allows the following:

1. for a given device, if we know that the report length will always be of a certain value,
   we can request the `data` pointer to point at the full report length.

   The kernel will ensure we are using a correct size and offset and eBPF will ensure
   the code will not attempt to read or write outside of the boundaries:

   ```
   __u8 *data = hid_bpf_get_data(ctx, 0 /* offset */, 256 /* size */);

   if (!data)
       return 0; /* ensure data is correct, now the verifier knows we
                  * have 256 bytes available */

   bpf_printk("hello world: %02x %02x %02x", data[0], data[128], data[255]);
   ```
2. if the report length is variable, but we know the value of `X` is always a 16-bit
   integer, we can then have a pointer to that value only:

   ```
   __u16 *x = hid_bpf_get_data(ctx, offset, sizeof(*x));

   if (!x)
       return 0; /* something went wrong */

   *x += 1; /* increment X by one */
   ```

### [Effect of a HID-BPF program](hid-bpf.md#id17)

For all HID-BPF attachment types except for [`hid_bpf_rdesc_fixup()`](hid-bpf.md#c.hid_bpf_rdesc_fixup "hid_bpf_rdesc_fixup"), several eBPF
programs can be attached to the same device.

Unless `HID_BPF_FLAG_INSERT_HEAD` is added to the flags while attaching the
program, the new program is appended at the end of the list.
`HID_BPF_FLAG_INSERT_HEAD` will insert the new program at the beginning of the
list which is useful for e.g. tracing where we need to get the unprocessed events
from the device.

Note that if there are multiple programs using the `HID_BPF_FLAG_INSERT_HEAD` flag,
only the most recently loaded one is actually the first in the list.

#### `SEC("fmod_ret/hid_bpf_device_event")`

Whenever a matching event is raised, the eBPF programs are called one after the other
and are working on the same data buffer.

If a program changes the data associated with the context, the next one will see
the modified data but it will have *no* idea of what the original data was.

Once all the programs are run and return `0` or a positive value, the rest of the
HID stack will work on the modified data, with the `size` field of the last hid_bpf_ctx
being the new size of the input stream of data.

A BPF program returning a negative error discards the event, i.e. this event will not be
processed by the HID stack. Clients (hidraw, input, LEDs) will **not** see this event.

#### `SEC("syscall")`

`syscall` are not attached to a given device. To tell which device we are working
with, userspace needs to refer to the device by its unique system id (the last 4 numbers
in the sysfs path: `/sys/bus/hid/devices/xxxx:yyyy:zzzz:0000`).

To retrieve a context associated with the device, the program must call
[`hid_bpf_allocate_context()`](hid-bpf.md#c.hid_bpf_allocate_context "hid_bpf_allocate_context") and must release it with [`hid_bpf_release_context()`](hid-bpf.md#c.hid_bpf_release_context "hid_bpf_release_context")
before returning.
Once the context is retrieved, one can also request a pointer to kernel memory with
[`hid_bpf_get_data()`](hid-bpf.md#c.hid_bpf_get_data "hid_bpf_get_data"). This memory is big enough to support all input/output/feature
reports of the given device.

#### `SEC("fmod_ret/hid_bpf_rdesc_fixup")`

The `hid_bpf_rdesc_fixup` program works in a similar manner to
`.report_fixup` of `struct hid_driver`.

When the device is probed, the kernel sets the data buffer of the context with the
content of the report descriptor. The memory associated with that buffer is
`HID_MAX_DESCRIPTOR_SIZE` (currently 4kB).

The eBPF program can modify the data buffer at-will and the kernel uses the
modified content and size as the report descriptor.

Whenever a `SEC("fmod_ret/hid_bpf_rdesc_fixup")` program is attached (if no
program was attached before), the kernel immediately disconnects the HID device
and does a reprobe.

In the same way, when the `SEC("fmod_ret/hid_bpf_rdesc_fixup")` program is
detached, the kernel issues a disconnect on the device.

There is no `detach` facility in HID-BPF. Detaching a program happens when
all the user space file descriptors pointing at a program are closed.
Thus, if we need to replace a report descriptor fixup, some cooperation is
required from the owner of the original report descriptor fixup.
The previous owner will likely pin the program in the bpffs, and we can then
replace it through normal bpf operations.

## [Attaching a bpf program to a device](hid-bpf.md#id18)

`libbpf` does not export any helper to attach a HID-BPF program.
Users need to use a dedicated `syscall` program which will call
`hid_bpf_attach_prog(hid_id, program_fd, flags)`.

`hid_id` is the unique system ID of the HID device (the last 4 numbers in the
sysfs path: `/sys/bus/hid/devices/xxxx:yyyy:zzzz:0000`)

`progam_fd` is the opened file descriptor of the program to attach.

`flags` is of type `enum hid_bpf_attach_flags`.

We can not rely on hidraw to bind a BPF program to a HID device. hidraw is an
artefact of the processing of the HID device, and is not stable. Some drivers
even disable it, so that removes the tracing capabilities on those devices
(where it is interesting to get the non-hidraw traces).

On the other hand, the `hid_id` is stable for the entire life of the HID device,
even if we change its report descriptor.

Given that hidraw is not stable when the device disconnects/reconnects, we recommend
accessing the current report descriptor of the device through the sysfs.
This is available at `/sys/bus/hid/devices/BUS:VID:PID.000N/report_descriptor` as a
binary stream.

Parsing the report descriptor is the responsibility of the BPF programmer or the userspace
component that loads the eBPF program.

## [An (almost) complete example of a BPF enhanced HID device](hid-bpf.md#id19)

*Foreword: for most parts, this could be implemented as a kernel driver*

Let's imagine we have a new tablet device that has some haptic capabilities
to simulate the surface the user is scratching on. This device would also have
a specific 3 positions switch to toggle between *pencil on paper*, *cray on a wall*
and *brush on a painting canvas*. To make things even better, we can control the
physical position of the switch through a feature report.

And of course, the switch is relying on some userspace component to control the
haptic feature of the device itself.

### [Filtering events](hid-bpf.md#id20)

The first step consists in filtering events from the device. Given that the switch
position is actually reported in the flow of the pen events, using hidraw to implement
that filtering would mean that we wake up userspace for every single event.

This is OK for libinput, but having an external library that is just interested in
one byte in the report is less than ideal.

For that, we can create a basic skeleton for our BPF program:

```
#include "vmlinux.h"
#include <bpf/bpf_helpers.h>
#include <bpf/bpf_tracing.h>

/* HID programs need to be GPL */
char _license[] SEC("license") = "GPL";

/* HID-BPF kfunc API definitions */
extern __u8 *hid_bpf_get_data(struct hid_bpf_ctx *ctx,
                            unsigned int offset,
                            const size_t __sz) __ksym;
extern int hid_bpf_attach_prog(unsigned int hid_id, int prog_fd, u32 flags) __ksym;

struct {
      __uint(type, BPF_MAP_TYPE_RINGBUF);
      __uint(max_entries, 4096 * 64);
} ringbuf SEC(".maps");

struct attach_prog_args {
      int prog_fd;
      unsigned int hid;
      unsigned int flags;
      int retval;
};

SEC("syscall")
int attach_prog(struct attach_prog_args *ctx)
{
      ctx->retval = hid_bpf_attach_prog(ctx->hid,
                                        ctx->prog_fd,
                                        ctx->flags);
      return 0;
}

__u8 current_value = 0;

SEC("?fmod_ret/hid_bpf_device_event")
int BPF_PROG(filter_switch, struct hid_bpf_ctx *hid_ctx)
{
      __u8 *data = hid_bpf_get_data(hid_ctx, 0 /* offset */, 192 /* size */);
      __u8 *buf;

      if (!data)
              return 0; /* EPERM check */

      if (current_value != data[152]) {
              buf = bpf_ringbuf_reserve(&ringbuf, 1, 0);
              if (!buf)
                      return 0;

              *buf = data[152];

              bpf_ringbuf_commit(buf, 0);

              current_value = data[152];
      }

      return 0;
}
```

To attach `filter_switch`, userspace needs to call the `attach_prog` syscall
program first:

```
static int attach_filter(struct hid *hid_skel, int hid_id)
{
      int err, prog_fd;
      int ret = -1;
      struct attach_prog_args args = {
              .hid = hid_id,
      };
      DECLARE_LIBBPF_OPTS(bpf_test_run_opts, tattrs,
              .ctx_in = &args,
              .ctx_size_in = sizeof(args),
      );

      args.prog_fd = bpf_program__fd(hid_skel->progs.filter_switch);

      prog_fd = bpf_program__fd(hid_skel->progs.attach_prog);

      err = bpf_prog_test_run_opts(prog_fd, &tattrs);
      if (err)
              return err;

      return args.retval; /* the fd of the created bpf_link */
}
```

Our userspace program can now listen to notifications on the ring buffer, and
is awaken only when the value changes.

When the userspace program doesn't need to listen to events anymore, it can just
close the returned fd from `attach_filter()`, which will tell the kernel to
detach the program from the HID device.

Of course, in other use cases, the userspace program can also pin the fd to the
BPF filesystem through a call to `bpf_obj_pin()`, as with any bpf_link.

### [Controlling the device](hid-bpf.md#id21)

To be able to change the haptic feedback from the tablet, the userspace program
needs to emit a feature report on the device itself.

Instead of using hidraw for that, we can create a `SEC("syscall")` program
that talks to the device:

```
/* some more HID-BPF kfunc API definitions */
extern struct hid_bpf_ctx *hid_bpf_allocate_context(unsigned int hid_id) __ksym;
extern void hid_bpf_release_context(struct hid_bpf_ctx *ctx) __ksym;
extern int hid_bpf_hw_request(struct hid_bpf_ctx *ctx,
                            __u8* data,
                            size_t len,
                            enum hid_report_type type,
                            enum hid_class_request reqtype) __ksym;

struct hid_send_haptics_args {
      /* data needs to come at offset 0 so we can do a memcpy into it */
      __u8 data[10];
      unsigned int hid;
};

SEC("syscall")
int send_haptic(struct hid_send_haptics_args *args)
{
      struct hid_bpf_ctx *ctx;
      int ret = 0;

      ctx = hid_bpf_allocate_context(args->hid);
      if (!ctx)
              return 0; /* EPERM check */

      ret = hid_bpf_hw_request(ctx,
                               args->data,
                               10,
                               HID_FEATURE_REPORT,
                               HID_REQ_SET_REPORT);

      hid_bpf_release_context(ctx);

      return ret;
}
```

And then userspace needs to call that program directly:

```
static int set_haptic(struct hid *hid_skel, int hid_id, __u8 haptic_value)
{
      int err, prog_fd;
      int ret = -1;
      struct hid_send_haptics_args args = {
              .hid = hid_id,
      };
      DECLARE_LIBBPF_OPTS(bpf_test_run_opts, tattrs,
              .ctx_in = &args,
              .ctx_size_in = sizeof(args),
      );

      args.data[0] = 0x02; /* report ID of the feature on our device */
      args.data[1] = haptic_value;

      prog_fd = bpf_program__fd(hid_skel->progs.set_haptic);

      err = bpf_prog_test_run_opts(prog_fd, &tattrs);
      return err;
}
```

Now our userspace program is aware of the haptic state and can control it. The
program could make this state further available to other userspace programs
(e.g. via a DBus API).

The interesting bit here is that we did not created a new kernel API for this.
Which means that if there is a bug in our implementation, we can change the
interface with the kernel at-will, because the userspace application is
responsible for its own usage.
