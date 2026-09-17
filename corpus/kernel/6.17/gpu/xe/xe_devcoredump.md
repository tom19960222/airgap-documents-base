---
collection: kernel
version: "6.17"
title: "Xe Device Coredump"
source_url: https://www.kernel.org/doc/html/v6.17/gpu/xe/xe_devcoredump.html
fetched_at: 2026-09-16T16:30:48+00:00
---
# Xe Device Coredump

Xe uses dev_coredump infrastructure for exposing the crash errors in a
standardized way. Once a crash occurs, devcoredump exposes a temporary
node under `/sys/class/devcoredump/devcd<m>/`. The same node is also
accessible in `/sys/class/drm/card<n>/device/devcoredump/`. The
`failing_device` symlink points to the device that crashed and created the
coredump.

The following characteristics are observed by xe when creating a device
coredump:

**Snapshot at hang**:
:   The ‘data’ file contains a snapshot of the HW and driver states at the time
    the hang happened. Due to the driver recovering from resets/crashes, it may
    not correspond to the state of the system when the file is read by
    userspace.

**Coredump release**:
:   After a coredump is generated, it stays in kernel memory until released by
    userspace by writing anything to it, or after an internal timer expires. The
    exact timeout may vary and should not be relied upon. Example to release
    a coredump:

    ```shell
    $ > /sys/class/drm/card0/device/devcoredump/data
    ```

**First failure only**:
:   In general, the first hang is the most critical one since the following
    hangs can be a consequence of the initial hang. For this reason a snapshot
    is taken only for the first failure. Until the devcoredump is released by
    userspace or kernel, all subsequent hangs do not override the snapshot nor
    create new ones. Devcoredump has a delayed work queue that will eventually
    delete the file node and free all the dump information.

## Internal API

ssize_t xe_devcoredump_read(char \*buffer, loff_t offset, size_t count, void \*data, size_t datalen)
:   Read data from the Xe device coredump snapshot

**Parameters**

`char *buffer`
:   Destination buffer to copy the coredump data into

`loff_t offset`
:   Offset in the coredump data to start reading from

`size_t count`
:   Number of bytes to read

`void *data`
:   Pointer to the xe_devcoredump structure

`size_t datalen`
:   Length of the data (unused)

**Description**

Reads a chunk of the coredump snapshot data into the provided buffer.
If the devcoredump is smaller than 1.5 GB (XE_DEVCOREDUMP_CHUNK_MAX),
it is read directly from a pre-written buffer. For larger devcoredumps,
the pre-written buffer must be periodically repopulated from the snapshot
state due to kmalloc size limitations.

**Return**

Number of bytes copied on success, or a negative error code on failure.

void xe_devcoredump(struct xe_exec_queue \*q, struct xe_sched_job \*job, const char \*fmt, ...)
:   Take the required snapshots and initialize coredump device.

**Parameters**

`struct xe_exec_queue *q`
:   The faulty xe_exec_queue, where the issue was detected.

`struct xe_sched_job *job`
:   The faulty xe_sched_job, where the issue was detected.

`const char *fmt`
:   Printf format + args to describe the reason for the core dump

`...`
:   variable arguments

**Description**

This function should be called at the crash time within the serialized
gt_reset. It is skipped if we still have the core dump device available
with the information of the ‘first’ snapshot.

void xe_print_blob_ascii85(struct [drm_printer](../drm-internals.md#c.drm_printer "drm_printer") \*p, const char \*prefix, char suffix, const void \*blob, size_t offset, size_t size)
:   print a BLOB to some useful location in ASCII85

**Parameters**

`struct drm_printer *p`
:   the printer object to output to

`const char *prefix`
:   optional prefix to add to output string

`char suffix`
:   optional suffix to add at the end. 0 disables it and is
    not added to the output, which is useful when using multiple calls
    to dump data to **p**

`const void *blob`
:   the Binary Large OBject to dump out

`size_t offset`
:   offset in bytes to skip from the front of the BLOB, must be a multiple of sizeof(u32)

`size_t size`
:   the size in bytes of the BLOB, must be a multiple of sizeof(u32)

**Description**

The output is split into multiple calls to [`drm_puts()`](../drm-internals.md#c.drm_puts "drm_puts") because some print
targets, e.g. dmesg, cannot handle arbitrarily long lines. These targets may
add newlines, as is the case with dmesg: each [`drm_puts()`](../drm-internals.md#c.drm_puts "drm_puts") call creates a
separate line.

There is also a scheduler yield call to prevent the ‘task has been stuck for
120s’ kernel hang check feature from firing when printing to a slow target
such as dmesg over a serial port.
