---
collection: kernel
version: "6.8"
title: "SCSI Interfaces Guide"
source_url: https://www.kernel.org/doc/html/v6.8/driver-api/scsi.html
fetched_at: 2026-08-21T03:30:49+00:00
---
# SCSI Interfaces Guide

Author
:   James Bottomley

Author
:   Rob Landley

## Introduction

### Protocol vs bus

Once upon a time, the Small Computer Systems Interface defined both a
parallel I/O bus and a data protocol to connect a wide variety of
peripherals (disk drives, tape drives, modems, printers, scanners,
optical drives, test equipment, and medical devices) to a host computer.

Although the old parallel (fast/wide/ultra) SCSI bus has largely fallen
out of use, the SCSI command set is more widely used than ever to
communicate with devices over a number of different busses.

The [SCSI protocol](http://www.t10.org/scsi-3.htm) is a big-endian
peer-to-peer packet based protocol. SCSI commands are 6, 10, 12, or 16
bytes long, often followed by an associated data payload.

SCSI commands can be transported over just about any kind of bus, and
are the default protocol for storage devices attached to USB, SATA, SAS,
Fibre Channel, FireWire, and ATAPI devices. SCSI packets are also
commonly exchanged over Infiniband,
[I2O](http://i2o.shadowconnect.com/faq.php), TCP/IP
([iSCSI](https://en.wikipedia.org/wiki/ISCSI)), even [Parallel
ports](http://cyberelk.net/tim/parport/parscsi.html).

### Design of the Linux SCSI subsystem

The SCSI subsystem uses a three layer design, with upper, mid, and low
layers. Every operation involving the SCSI subsystem (such as reading a
sector from a disk) uses one driver at each of the 3 levels: one upper
layer driver, one lower layer driver, and the SCSI midlayer.

The SCSI upper layer provides the interface between userspace and the
kernel, in the form of block and char device nodes for I/O and ioctl().
The SCSI lower layer contains drivers for specific hardware devices.

In between is the SCSI mid-layer, analogous to a network routing layer
such as the IPv4 stack. The SCSI mid-layer routes a packet based data
protocol between the upper layer's /dev nodes and the corresponding
devices in the lower layer. It manages command queues, provides error
handling and power management functions, and responds to ioctl()
requests.

## SCSI upper layer

The upper layer supports the user-kernel interface by providing device
nodes.

### sd (SCSI Disk)

sd (sd_mod.o)

### sr (SCSI CD-ROM)

sr (sr_mod.o)

### st (SCSI Tape)

st (st.o)

### sg (SCSI Generic)

sg (sg.o)

### ch (SCSI Media Changer)

ch (ch.c)

## SCSI mid layer

### SCSI midlayer implementation

#### include/scsi/scsi_device.h

struct scsi_vpd
:   SCSI Vital Product Data

**Definition**:

```
struct scsi_vpd {
    struct rcu_head rcu;
    int len;
    unsigned char   data[];
};
```

**Members**

`rcu`
:   For [`kfree_rcu()`](../core-api/kernel-api.md#c.kfree_rcu "kfree_rcu").

`len`
:   Length in bytes of **data**.

`data`
:   VPD data as defined in various T10 SCSI standard documents.

shost_for_each_device

`shost_for_each_device (sdev, shost)`

> iterate over all devices of a host

**Parameters**

`sdev`
:   the `struct scsi_device` to use as a cursor

`shost`
:   the `struct scsi_host` to iterate over

**Description**

Iterator that returns each device attached to **shost**. This loop
takes a reference on each device and releases it at the end. If
you break out of the loop, you must call scsi_device_put(sdev).

__shost_for_each_device

`__shost_for_each_device (sdev, shost)`

> iterate over all devices of a host (UNLOCKED)

**Parameters**

`sdev`
:   the `struct scsi_device` to use as a cursor

`shost`
:   the `struct scsi_host` to iterate over

**Description**

Iterator that returns each device attached to **shost**. It does _not_
take a reference on the scsi_device, so the whole loop must be
protected by shost->host_lock.

**Note**

The only reason to use this is because you need to access the
device list in interrupt context. Otherwise you really want to use
shost_for_each_device instead.

int scsi_device_supports_vpd(struct scsi_device \*sdev)
:   test if a device supports VPD pages

**Parameters**

`struct scsi_device *sdev`
:   the `struct scsi_device` to test

**Description**

If the 'try_vpd_pages' flag is set it takes precedence.
Otherwise we will assume VPD pages are supported if the
SCSI level is at least SPC-3 and 'skip_vpd_pages' is not set.

#### drivers/scsi/scsi.c

Main file for the SCSI midlayer.

int scsi_change_queue_depth(struct scsi_device \*sdev, int depth)
:   change a device's queue depth

**Parameters**

`struct scsi_device *sdev`
:   SCSI Device in question

`int depth`
:   number of commands allowed to be queued to the driver

**Description**

Sets the device queue depth and returns the new value.

int scsi_track_queue_full(struct scsi_device \*sdev, int depth)
:   track QUEUE_FULL events to adjust queue depth

**Parameters**

`struct scsi_device *sdev`
:   SCSI Device in question

`int depth`
:   Current number of outstanding SCSI commands on this device,
    not counting the one returned as QUEUE_FULL.

**Description**

This function will track successive QUEUE_FULL events on a
:   specific SCSI device to determine if and when there is a
    need to adjust the queue depth on the device.

Lock Status: None held on entry

**Return**

0 - No change needed, >0 - Adjust queue depth to this new depth,
:   -1 - Drop back to untagged operation using host->cmd_per_lun
    :   as the untagged command depth

**Notes**

Low level drivers may call this at any time and we will do
:   "The Right Thing." We are interrupt context safe.

int scsi_get_vpd_page(struct scsi_device \*sdev, u8 page, unsigned char \*buf, int buf_len)
:   Get Vital Product Data from a SCSI device

**Parameters**

`struct scsi_device *sdev`
:   The device to ask

`u8 page`
:   Which Vital Product Data to return

`unsigned char *buf`
:   where to store the VPD

`int buf_len`
:   number of bytes in the VPD buffer area

**Description**

SCSI devices may optionally supply Vital Product Data. Each 'page'
of VPD is defined in the appropriate SCSI document (eg SPC, SBC).
If the device supports this VPD page, this routine fills **buf**
with the data from that page and return 0. If the VPD page is not
supported or its content cannot be retrieved, -EINVAL is returned.

int scsi_report_opcode(struct scsi_device \*sdev, unsigned char \*buffer, unsigned int len, unsigned char opcode, unsigned short sa)
:   Find out if a given command is supported

**Parameters**

`struct scsi_device *sdev`
:   scsi device to query

`unsigned char *buffer`
:   scratch buffer (must be at least 20 bytes long)

`unsigned int len`
:   length of buffer

`unsigned char opcode`
:   opcode for the command to look up

`unsigned short sa`
:   service action for the command to look up

**Description**

Uses the REPORT SUPPORTED OPERATION CODES to check support for the
command identified with **opcode** and **sa**. If the command does not
have a service action, **sa** must be 0. Returns -EINVAL if RSOC fails,
0 if the command is not supported and 1 if the device claims to
support the command.

int scsi_device_get(struct scsi_device \*sdev)
:   get an additional reference to a scsi_device

**Parameters**

`struct scsi_device *sdev`
:   device to get a reference to

**Description**

Gets a reference to the scsi_device and increments the use count
of the underlying LLDD module. You must hold host_lock of the
parent Scsi_Host or already have a reference when calling this.

This will fail if a device is deleted or cancelled, or when the LLD module
is in the process of being unloaded.

void scsi_device_put(struct scsi_device \*sdev)
:   release a reference to a scsi_device

**Parameters**

`struct scsi_device *sdev`
:   device to release a reference on.

**Description**

Release a reference to the scsi_device and decrements the use
count of the underlying LLDD module. The device is freed once the last
user vanishes.

void starget_for_each_device(struct scsi_target \*starget, void \*data, void (\*fn)(struct scsi_device\*, void\*))
:   helper to walk all devices of a target

**Parameters**

`struct scsi_target *starget`
:   target whose devices we want to iterate over.

`void *data`
:   Opaque passed to each function call.

`void (*fn)(struct scsi_device *, void *)`
:   Function to call on each device

**Description**

This traverses over each device of **starget**. The devices have
a reference that must be released by scsi_host_put when breaking
out of the loop.

void __starget_for_each_device(struct scsi_target \*starget, void \*data, void (\*fn)(struct scsi_device\*, void\*))
:   helper to walk all devices of a target (UNLOCKED)

**Parameters**

`struct scsi_target *starget`
:   target whose devices we want to iterate over.

`void *data`
:   parameter for callback **fn()**

`void (*fn)(struct scsi_device *, void *)`
:   callback function that is invoked for each device

**Description**

This traverses over each device of **starget**. It does _not_
take a reference on the scsi_device, so the whole loop must be
protected by shost->host_lock.

**Note**

The only reason why drivers would want to use this is because
they need to access the device list in irq context. Otherwise you
really want to use starget_for_each_device instead.

struct scsi_device \*__scsi_device_lookup_by_target(struct scsi_target \*starget, u64 lun)
:   find a device given the target (UNLOCKED)

**Parameters**

`struct scsi_target *starget`
:   SCSI target pointer

`u64 lun`
:   SCSI Logical Unit Number

**Description**

Looks up the scsi_device with the specified **lun** for a given
**starget**. The returned scsi_device does not have an additional
reference. You must hold the host's host_lock over this call and
any access to the returned scsi_device. A scsi_device in state
SDEV_DEL is skipped.

**Note**

The only reason why drivers should use this is because
they need to access the device list in irq context. Otherwise you
really want to use scsi_device_lookup_by_target instead.

struct scsi_device \*scsi_device_lookup_by_target(struct scsi_target \*starget, u64 lun)
:   find a device given the target

**Parameters**

`struct scsi_target *starget`
:   SCSI target pointer

`u64 lun`
:   SCSI Logical Unit Number

**Description**

Looks up the scsi_device with the specified **lun** for a given
**starget**. The returned scsi_device has an additional reference that
needs to be released with scsi_device_put once you're done with it.

struct scsi_device \*__scsi_device_lookup(struct Scsi_Host \*shost, uint channel, uint id, u64 lun)
:   find a device given the host (UNLOCKED)

**Parameters**

`struct Scsi_Host *shost`
:   SCSI host pointer

`uint channel`
:   SCSI channel (zero if only one channel)

`uint id`
:   SCSI target number (physical unit number)

`u64 lun`
:   SCSI Logical Unit Number

**Description**

Looks up the scsi_device with the specified **channel**, **id**, **lun**
for a given host. The returned scsi_device does not have an additional
reference. You must hold the host's host_lock over this call and any access
to the returned scsi_device.

**Note**

The only reason why drivers would want to use this is because
they need to access the device list in irq context. Otherwise you
really want to use scsi_device_lookup instead.

struct scsi_device \*scsi_device_lookup(struct Scsi_Host \*shost, uint channel, uint id, u64 lun)
:   find a device given the host

**Parameters**

`struct Scsi_Host *shost`
:   SCSI host pointer

`uint channel`
:   SCSI channel (zero if only one channel)

`uint id`
:   SCSI target number (physical unit number)

`u64 lun`
:   SCSI Logical Unit Number

**Description**

Looks up the scsi_device with the specified **channel**, **id**, **lun**
for a given host. The returned scsi_device has an additional reference that
needs to be released with scsi_device_put once you're done with it.

#### drivers/scsi/scsicam.c

[SCSI Common Access
Method](http://www.t10.org/ftp/t10/drafts/cam/cam-r12b.pdf) support
functions, for use with HDIO_GETGEO, etc.

unsigned char \*scsi_bios_ptable(struct block_device \*dev)
:   Read PC partition table out of first sector of device.

**Parameters**

`struct block_device *dev`
:   from this device

**Description**

Reads the first sector from the device and returns `0x42` bytes
:   starting at offset `0x1be`.

**Return**

partition table in kmalloc(GFP_KERNEL) memory, or NULL on error.

bool scsi_partsize(struct block_device \*bdev, sector_t capacity, int geom[3])
:   Parse cylinders/heads/sectors from PC partition table

**Parameters**

`struct block_device *bdev`
:   block device to parse

`sector_t capacity`
:   size of the disk in sectors

`int geom[3]`
:   output in form of [hds, cylinders, sectors]

**Description**

Determine the BIOS mapping/geometry used to create the partition
table, storing the results in **geom**.

**Return**

`false` on failure, `true` on success.

int scsicam_bios_param(struct block_device \*bdev, sector_t capacity, int \*ip)
:   Determine geometry of a disk in cylinders/heads/sectors.

**Parameters**

`struct block_device *bdev`
:   which device

`sector_t capacity`
:   size of the disk in sectors

`int *ip`
:   return value: ip[0]=heads, ip[1]=sectors, ip[2]=cylinders

**Description**

determine the BIOS mapping/geometry used for a drive in a
:   SCSI-CAM system, storing the results in ip as required
    by the HDIO_GETGEO ioctl().

**Return**

-1 on failure, 0 on success.

#### drivers/scsi/scsi_error.c

Common SCSI error/timeout handling routines.

void scsi_schedule_eh(struct Scsi_Host \*shost)
:   schedule EH for SCSI host

**Parameters**

`struct Scsi_Host *shost`
:   SCSI host to invoke error handling on.

**Description**

Schedule SCSI EH without scmd.

int scsi_block_when_processing_errors(struct scsi_device \*sdev)
:   Prevent cmds from being queued.

**Parameters**

`struct scsi_device *sdev`
:   Device on which we are performing recovery.

**Description**

> We block until the host is out of error recovery, and then check to
> see whether the host or the device is offline.

Return value:
:   0 when dev was taken offline by error recovery. 1 OK to proceed.

enum scsi_disposition scsi_check_sense(struct scsi_cmnd \*scmd)
:   Examine scsi cmd sense

**Parameters**

`struct scsi_cmnd *scmd`
:   Cmd to have sense checked.

**Description**

Return value:
:   SUCCESS or FAILED or NEEDS_RETRY or ADD_TO_MLQUEUE

**Notes**

> When a deferred error is detected the current command has
> not been executed and needs retrying.

void scsi_eh_prep_cmnd(struct scsi_cmnd \*scmd, struct scsi_eh_save \*ses, unsigned char \*cmnd, int cmnd_size, unsigned sense_bytes)
:   Save a scsi command info as part of error recovery

**Parameters**

`struct scsi_cmnd *scmd`
:   SCSI command structure to hijack

`struct scsi_eh_save *ses`
:   structure to save restore information

`unsigned char *cmnd`
:   CDB to send. Can be NULL if no new cmnd is needed

`int cmnd_size`
:   size in bytes of **cmnd** (must be <= MAX_COMMAND_SIZE)

`unsigned sense_bytes`
:   size of sense data to copy. or 0 (if != 0 **cmnd** is ignored)

**Description**

This function is used to save a scsi command information before re-execution
as part of the error recovery process. If **sense_bytes** is 0 the command
sent must be one that does not transfer any data. If **sense_bytes** != 0
**cmnd** is ignored and this functions sets up a REQUEST_SENSE command
and cmnd buffers to read **sense_bytes** into **scmd->sense_buffer**.

void scsi_eh_restore_cmnd(struct scsi_cmnd \*scmd, struct scsi_eh_save \*ses)
:   Restore a scsi command info as part of error recovery

**Parameters**

`struct scsi_cmnd* scmd`
:   SCSI command structure to restore

`struct scsi_eh_save *ses`
:   saved information from a coresponding call to scsi_eh_prep_cmnd

**Description**

Undo any damage done by above [`scsi_eh_prep_cmnd()`](scsi.md#c.scsi_eh_prep_cmnd "scsi_eh_prep_cmnd").

void scsi_eh_finish_cmd(struct scsi_cmnd \*scmd, struct list_head \*done_q)
:   Handle a cmd that eh is finished with.

**Parameters**

`struct scsi_cmnd *scmd`
:   Original SCSI cmd that eh has finished.

`struct list_head *done_q`
:   Queue for processed commands.

**Notes**

> We don't want to use the normal command completion while we are are
> still handling errors - it may cause other commands to be queued,
> and that would disturb what we are doing. Thus we really want to
> keep a list of pending commands for final completion, and once we
> are ready to leave error handling we handle completion for real.

int scsi_eh_get_sense(struct list_head \*work_q, struct list_head \*done_q)
:   Get device sense data.

**Parameters**

`struct list_head *work_q`
:   Queue of commands to process.

`struct list_head *done_q`
:   Queue of processed commands.

**Description**

> See if we need to request sense information. if so, then get it
> now, so we have a better idea of what to do.

**Notes**

> This has the unfortunate side effect that if a shost adapter does
> not automatically request sense information, we end up shutting
> it down before we request it.
>
> All drivers should request sense information internally these days,
> so for now all I have to say is tough noogies if you end up in here.
>
> XXX: Long term this code should go away, but that needs an audit of
> :   all LLDDs first.

void scsi_eh_ready_devs(struct Scsi_Host \*shost, struct list_head \*work_q, struct list_head \*done_q)
:   check device ready state and recover if not.

**Parameters**

`struct Scsi_Host *shost`
:   host to be recovered.

`struct list_head *work_q`
:   `list_head` for pending commands.

`struct list_head *done_q`
:   `list_head` for processed commands.

void scsi_eh_flush_done_q(struct list_head \*done_q)
:   finish processed commands or retry them.

**Parameters**

`struct list_head *done_q`
:   list_head of processed commands.

bool scsi_get_sense_info_fld(const u8 \*sense_buffer, int sb_len, u64 \*info_out)
:   get information field from sense data (either fixed or descriptor format)

**Parameters**

`const u8 *sense_buffer`
:   byte array of sense data

`int sb_len`
:   number of valid bytes in sense_buffer

`u64 *info_out`
:   pointer to 64 integer where 8 or 4 byte information
    field will be placed if found.

**Description**

Return value:
:   true if information field found, false if not found.

#### drivers/scsi/scsi_devinfo.c

Manage scsi_dev_info_list, which tracks blacklisted and whitelisted
devices.

int scsi_dev_info_list_add(int compatible, char \*vendor, char \*model, char \*strflags, blist_flags_t flags)
:   add one dev_info list entry.

**Parameters**

`int compatible`
:   if true, null terminate short strings. Otherwise space pad.

`char *vendor`
:   vendor string

`char *model`
:   model (product) string

`char *strflags`
:   integer string

`blist_flags_t flags`
:   if strflags NULL, use this flag value

**Description**

> Create and add one dev_info entry for **vendor**, **model**, **strflags** or
> **flag**. If **compatible**, add to the tail of the list, do not space
> pad, and set devinfo->compatible. The scsi_static_device_list entries
> are added with **compatible** 1 and **clfags** NULL.

**Return**

0 OK, -error on failure.

struct scsi_dev_info_list \*scsi_dev_info_list_find(const char \*vendor, const char \*model, enum scsi_devinfo_key key)
:   find a matching dev_info list entry.

**Parameters**

`const char *vendor`
:   full vendor string

`const char *model`
:   full model (product) string

`enum scsi_devinfo_key key`
:   specify list to use

**Description**

> Finds the first dev_info entry matching **vendor**, **model**
> in list specified by **key**.

**Return**

pointer to matching entry, or ERR_PTR on failure.

int scsi_dev_info_list_add_str(char \*dev_list)
:   parse dev_list and add to the scsi_dev_info_list.

**Parameters**

`char *dev_list`
:   string of device flags to add

**Description**

> Parse dev_list, and add entries to the scsi_dev_info_list.
> dev_list is of the form "vendor:product:flag,vendor:product:flag".
> dev_list is modified via strsep. Can be called for command line
> addition, for proc or mabye a sysfs interface.

**Return**

0 if OK, -error on failure.

blist_flags_t scsi_get_device_flags(struct scsi_device \*sdev, const unsigned char \*vendor, const unsigned char \*model)
:   get device specific flags from the dynamic device list.

**Parameters**

`struct scsi_device *sdev`
:   `scsi_device` to get flags for

`const unsigned char *vendor`
:   vendor name

`const unsigned char *model`
:   model name

**Description**

> Search the global scsi_dev_info_list (specified by list zero)
> for an entry matching **vendor** and **model**, if found, return the
> matching flags value, else return the host or global default
> settings. Called during scan time.

void scsi_exit_devinfo(void)
:   remove /proc/scsi/device_info & the scsi_dev_info_list

**Parameters**

`void`
:   no arguments

int scsi_init_devinfo(void)
:   set up the dynamic device list.

**Parameters**

`void`
:   no arguments

**Description**

> Add command line entries from scsi_dev_flags, then add
> scsi_static_device_list entries to the scsi device info list.

#### drivers/scsi/scsi_ioctl.c

Handle ioctl() calls for SCSI devices.

int scsi_ioctl(struct scsi_device \*sdev, bool open_for_write, int cmd, void __user \*arg)
:   Dispatch ioctl to scsi device

**Parameters**

`struct scsi_device *sdev`
:   scsi device receiving ioctl

`bool open_for_write`
:   is the file / block device opened for writing?

`int cmd`
:   which ioctl is it

`void __user *arg`
:   data associated with ioctl

**Description**

The [`scsi_ioctl()`](scsi.md#c.scsi_ioctl "scsi_ioctl") function differs from most ioctls in that it
does not take a major/minor number as the dev field. Rather, it takes
a pointer to a `struct scsi_device`.

#### drivers/scsi/scsi_lib.c

SCSI queuing library.

int scsi_execute_cmd(struct scsi_device \*sdev, const unsigned char \*cmd, blk_opf_t opf, void \*buffer, unsigned int bufflen, int timeout, int retries, const struct scsi_exec_args \*args)
:   insert request and wait for the result

**Parameters**

`struct scsi_device *sdev`
:   scsi_device

`const unsigned char *cmd`
:   scsi command

`blk_opf_t opf`
:   block layer request cmd_flags

`void *buffer`
:   data buffer

`unsigned int bufflen`
:   len of buffer

`int timeout`
:   request timeout in HZ

`int retries`
:   number of times to retry request

`const struct scsi_exec_args *args`
:   Optional args. See struct definition for field descriptions

**Description**

Returns the scsi_cmnd result field if a command was executed, or a negative
Linux error code if we didn't get that far.

blk_status_t scsi_alloc_sgtables(struct scsi_cmnd \*cmd)
:   Allocate and initialize data and integrity scatterlists

**Parameters**

`struct scsi_cmnd *cmd`
:   SCSI command data structure to initialize.

**Description**

Initializes **cmd->sdb** and also **cmd->prot_sdb** if data integrity is enabled
for **cmd**.

**Return**

- BLK_STS_OK - on success
- BLK_STS_RESOURCE - if the failure is retryable
- BLK_STS_IOERR - if the failure is fatal

struct scsi_device \*scsi_device_from_queue(struct request_queue \*q)
:   return sdev associated with a request_queue

**Parameters**

`struct request_queue *q`
:   The request queue to return the sdev from

**Description**

Return the sdev associated with a request queue or NULL if the
request_queue does not reference a SCSI device.

void scsi_block_requests(struct Scsi_Host \*shost)
:   Utility function used by low-level drivers to prevent further commands from being queued to the device.

**Parameters**

`struct Scsi_Host *shost`
:   host in question

**Description**

There is no timer nor any other means by which the requests get unblocked
other than the low-level driver calling [`scsi_unblock_requests()`](scsi.md#c.scsi_unblock_requests "scsi_unblock_requests").

void scsi_unblock_requests(struct Scsi_Host \*shost)
:   Utility function used by low-level drivers to allow further commands to be queued to the device.

**Parameters**

`struct Scsi_Host *shost`
:   host in question

**Description**

There is no timer nor any other means by which the requests get unblocked
other than the low-level driver calling [`scsi_unblock_requests()`](scsi.md#c.scsi_unblock_requests "scsi_unblock_requests"). This is done
as an API function so that changes to the internals of the scsi mid-layer
won't require wholesale changes to drivers that use this feature.

int scsi_mode_select(struct scsi_device \*sdev, int pf, int sp, unsigned char \*buffer, int len, int timeout, int retries, struct scsi_mode_data \*data, struct scsi_sense_hdr \*sshdr)
:   issue a mode select

**Parameters**

`struct scsi_device *sdev`
:   SCSI device to be queried

`int pf`
:   Page format bit (1 == standard, 0 == vendor specific)

`int sp`
:   Save page bit (0 == don't save, 1 == save)

`unsigned char *buffer`
:   request buffer (may not be smaller than eight bytes)

`int len`
:   length of request buffer.

`int timeout`
:   command timeout

`int retries`
:   number of retries before failing

`struct scsi_mode_data *data`
:   returns a structure abstracting the mode header data

`struct scsi_sense_hdr *sshdr`
:   place to put sense data (or NULL if no sense to be collected).
    must be SCSI_SENSE_BUFFERSIZE big.

    > Returns zero if successful; negative error number or scsi
    > status on error

int scsi_mode_sense(struct scsi_device \*sdev, int dbd, int modepage, int subpage, unsigned char \*buffer, int len, int timeout, int retries, struct scsi_mode_data \*data, struct scsi_sense_hdr \*sshdr)
:   issue a mode sense, falling back from 10 to six bytes if necessary.

**Parameters**

`struct scsi_device *sdev`
:   SCSI device to be queried

`int dbd`
:   set to prevent mode sense from returning block descriptors

`int modepage`
:   mode page being requested

`int subpage`
:   sub-page of the mode page being requested

`unsigned char *buffer`
:   request buffer (may not be smaller than eight bytes)

`int len`
:   length of request buffer.

`int timeout`
:   command timeout

`int retries`
:   number of retries before failing

`struct scsi_mode_data *data`
:   returns a structure abstracting the mode header data

`struct scsi_sense_hdr *sshdr`
:   place to put sense data (or NULL if no sense to be collected).
    must be SCSI_SENSE_BUFFERSIZE big.

    > Returns zero if successful, or a negative error number on failure

int scsi_test_unit_ready(struct scsi_device \*sdev, int timeout, int retries, struct scsi_sense_hdr \*sshdr)
:   test if unit is ready

**Parameters**

`struct scsi_device *sdev`
:   scsi device to change the state of.

`int timeout`
:   command timeout

`int retries`
:   number of retries before failing

`struct scsi_sense_hdr *sshdr`
:   outpout pointer for decoded sense information.

    Returns zero if unsuccessful or an error if TUR failed. For
    removable media, UNIT_ATTENTION sets ->changed flag.

int scsi_device_set_state(struct scsi_device \*sdev, enum scsi_device_state state)
:   Take the given device through the device state model.

**Parameters**

`struct scsi_device *sdev`
:   scsi device to change the state of.

`enum scsi_device_state state`
:   state to change to.

    Returns zero if successful or an error if the requested
    transition is illegal.

void sdev_evt_send(struct scsi_device \*sdev, struct scsi_event \*evt)
:   send asserted event to uevent thread

**Parameters**

`struct scsi_device *sdev`
:   scsi_device event occurred on

`struct scsi_event *evt`
:   event to send

    Assert scsi device event asynchronously.

struct scsi_event \*sdev_evt_alloc(enum scsi_device_event evt_type, gfp_t gfpflags)
:   allocate a new scsi event

**Parameters**

`enum scsi_device_event evt_type`
:   type of event to allocate

`gfp_t gfpflags`
:   GFP flags for allocation

    Allocates and returns a new scsi_event.

void sdev_evt_send_simple(struct scsi_device \*sdev, enum scsi_device_event evt_type, gfp_t gfpflags)
:   send asserted event to uevent thread

**Parameters**

`struct scsi_device *sdev`
:   scsi_device event occurred on

`enum scsi_device_event evt_type`
:   type of event to send

`gfp_t gfpflags`
:   GFP flags for allocation

    Assert scsi device event asynchronously, given an event type.

int scsi_device_quiesce(struct scsi_device \*sdev)
:   Block all commands except power management.

**Parameters**

`struct scsi_device *sdev`
:   scsi device to quiesce.

    This works by trying to transition to the SDEV_QUIESCE state
    (which must be a legal transition). When the device is in this
    state, only power management requests will be accepted, all others will
    be deferred.

    Must be called with user context, may sleep.

    Returns zero if unsuccessful or an error if not.

void scsi_device_resume(struct scsi_device \*sdev)
:   Restart user issued commands to a quiesced device.

**Parameters**

`struct scsi_device *sdev`
:   scsi device to resume.

    Moves the device from quiesced back to running and restarts the
    queues.

    Must be called with user context, may sleep.

int scsi_internal_device_block_nowait(struct scsi_device \*sdev)
:   try to transition to the SDEV_BLOCK state

**Parameters**

`struct scsi_device *sdev`
:   device to block

**Description**

Pause SCSI command processing on the specified device. Does not sleep.

Returns zero if successful or a negative error code upon failure.

**Notes**

This routine transitions the device to the SDEV_BLOCK state (which must be
a legal transition). When the device is in this state, command processing
is paused until the device leaves the SDEV_BLOCK state. See also
[`scsi_internal_device_unblock_nowait()`](scsi.md#c.scsi_internal_device_unblock_nowait "scsi_internal_device_unblock_nowait").

int scsi_internal_device_unblock_nowait(struct scsi_device \*sdev, enum scsi_device_state new_state)
:   resume a device after a block request

**Parameters**

`struct scsi_device *sdev`
:   device to resume

`enum scsi_device_state new_state`
:   state to set the device to after unblocking

**Description**

Restart the device queue for a previously suspended SCSI device. Does not
sleep.

Returns zero if successful or a negative error code upon failure.

**Notes**

This routine transitions the device to the SDEV_RUNNING state or to one of
the offline states (which must be a legal transition) allowing the midlayer
to goose the queue for this device.

void scsi_block_targets(struct Scsi_Host \*shost, struct [device](infrastructure.md#c.device "device") \*dev)
:   transition all SCSI child devices to SDEV_BLOCK state

**Parameters**

`struct Scsi_Host *shost`
:   the Scsi_Host to which this device belongs

`struct device *dev`
:   a parent device of one or more scsi_target devices

**Description**

Iterate over all children of **dev**, which should be scsi_target devices,
and switch all subordinate scsi devices to SDEV_BLOCK state. Wait for
ongoing scsi_queue_rq() calls to finish. May sleep.

**Note**

**dev** must not itself be a scsi_target device.

int scsi_host_block(struct Scsi_Host \*shost)
:   Try to transition all logical units to the SDEV_BLOCK state

**Parameters**

`struct Scsi_Host *shost`
:   device to block

**Description**

Pause SCSI command processing for all logical units associated with the SCSI
host and wait until pending scsi_queue_rq() calls have finished.

Returns zero if successful or a negative error code upon failure.

void \*scsi_kmap_atomic_sg(struct scatterlist \*sgl, int sg_count, size_t \*offset, size_t \*len)
:   find and atomically map an sg-elemnt

**Parameters**

`struct scatterlist *sgl`
:   scatter-gather list

`int sg_count`
:   number of segments in sg

`size_t *offset`
:   offset in bytes into sg, on return offset into the mapped area

`size_t *len`
:   bytes to map, on return number of bytes mapped

**Description**

Returns virtual address of the start of the mapped page

void scsi_kunmap_atomic_sg(void \*virt)
:   atomically unmap a virtual address, previously mapped with scsi_kmap_atomic_sg

**Parameters**

`void *virt`
:   virtual address to be unmapped

int scsi_vpd_lun_id(struct scsi_device \*sdev, char \*id, size_t id_len)
:   return a unique device identification

**Parameters**

`struct scsi_device *sdev`
:   SCSI device

`char *id`
:   buffer for the identification

`size_t id_len`
:   length of the buffer

**Description**

Copies a unique device identification into **id** based
on the information in the VPD page 0x83 of the device.
The string will be formatted as a SCSI name string.

Returns the length of the identification or error on failure.
If the identifier is longer than the supplied buffer the actual
identifier length is returned and the buffer is not zero-padded.

void scsi_build_sense(struct scsi_cmnd \*scmd, int desc, u8 key, u8 asc, u8 ascq)
:   build sense data for a command

**Parameters**

`struct scsi_cmnd *scmd`
:   scsi command for which the sense should be formatted

`int desc`
:   Sense format (non-zero == descriptor format,
    0 == fixed format)

`u8 key`
:   Sense key

`u8 asc`
:   Additional sense code

`u8 ascq`
:   Additional sense code qualifier

#### drivers/scsi/scsi_lib_dma.c

SCSI library functions depending on DMA (map and unmap scatter-gather
lists).

int scsi_dma_map(struct scsi_cmnd \*cmd)
:   perform DMA mapping against command's sg lists

**Parameters**

`struct scsi_cmnd *cmd`
:   scsi command

**Description**

Returns the number of sg lists actually used, zero if the sg lists
is NULL, or -ENOMEM if the mapping failed.

void scsi_dma_unmap(struct scsi_cmnd \*cmd)
:   unmap command's sg lists mapped by scsi_dma_map

**Parameters**

`struct scsi_cmnd *cmd`
:   scsi command

#### drivers/scsi/scsi_proc.c

The functions in this file provide an interface between the PROC file
system and the SCSI device drivers It is mainly used for debugging,
statistics and to pass information directly to the lowlevel driver. I.E.
plumbing to manage /proc/scsi/\*

struct scsi_proc_entry
:   (host template, SCSI proc dir) association

**Definition**:

```
struct scsi_proc_entry {
    struct list_head        entry;
    const struct scsi_host_template *sht;
    struct proc_dir_entry   *proc_dir;
    unsigned int            present;
};
```

**Members**

`entry`
:   entry in scsi_proc_list.

`sht`
:   SCSI host template associated with the procfs directory.

`proc_dir`
:   procfs directory associated with the SCSI host template.

`present`
:   Number of SCSI hosts instantiated for **sht**.

int scsi_proc_hostdir_add(const struct scsi_host_template \*sht)
:   Create directory in /proc for a scsi host

**Parameters**

`const struct scsi_host_template *sht`
:   owner of this directory

**Description**

Sets sht->proc_dir to the new directory.

void scsi_proc_hostdir_rm(const struct scsi_host_template \*sht)
:   remove directory in /proc for a scsi host

**Parameters**

`const struct scsi_host_template *sht`
:   owner of directory

void scsi_proc_host_add(struct Scsi_Host \*shost)
:   Add entry for this host to appropriate /proc dir

**Parameters**

`struct Scsi_Host *shost`
:   host to add

void scsi_proc_host_rm(struct Scsi_Host \*shost)
:   remove this host's entry from /proc

**Parameters**

`struct Scsi_Host *shost`
:   which host

int proc_print_scsidevice(struct [device](infrastructure.md#c.device "device") \*dev, void \*data)
:   return data about this host

**Parameters**

`struct device *dev`
:   A scsi device

`void *data`
:   `struct seq_file` to output to.

**Description**

prints Host, Channel, Id, Lun, Vendor, Model, Rev, Type,
and revision.

int scsi_add_single_device(uint host, uint channel, uint id, uint lun)
:   Respond to user request to probe for/add device

**Parameters**

`uint host`
:   user-supplied decimal integer

`uint channel`
:   user-supplied decimal integer

`uint id`
:   user-supplied decimal integer

`uint lun`
:   user-supplied decimal integer

**Description**

called by writing "scsi add-single-device" to /proc/scsi/scsi.

does [`scsi_host_lookup()`](scsi.md#c.scsi_host_lookup "scsi_host_lookup") and either user_scan() if that transport
type supports it, or else scsi_scan_host_selected()

**Note**

this seems to be aimed exclusively at SCSI parallel busses.

int scsi_remove_single_device(uint host, uint channel, uint id, uint lun)
:   Respond to user request to remove a device

**Parameters**

`uint host`
:   user-supplied decimal integer

`uint channel`
:   user-supplied decimal integer

`uint id`
:   user-supplied decimal integer

`uint lun`
:   user-supplied decimal integer

**Description**

called by writing "scsi remove-single-device" to
/proc/scsi/scsi. Does a [`scsi_device_lookup()`](scsi.md#c.scsi_device_lookup "scsi_device_lookup") and [`scsi_remove_device()`](scsi.md#c.scsi_remove_device "scsi_remove_device")

ssize_t proc_scsi_write(struct [file](scsi.md#c.proc_scsi_write "file") \*file, const char __user \*buf, size_t length, loff_t \*ppos)
:   handle writes to /proc/scsi/scsi

**Parameters**

`struct file *file`
:   not used

`const char __user *buf`
:   buffer to write

`size_t length`
:   length of buf, at most PAGE_SIZE

`loff_t *ppos`
:   not used

**Description**

this provides a legacy mechanism to add or remove devices by
Host, Channel, ID, and Lun. To use,
"echo 'scsi add-single-device 0 1 2 3' > /proc/scsi/scsi" or
"echo 'scsi remove-single-device 0 1 2 3' > /proc/scsi/scsi" with
"0 1 2 3" replaced by the Host, Channel, Id, and Lun.

**Note**

this seems to be aimed at parallel SCSI. Most modern busses (USB,
SATA, Firewire, Fibre Channel, etc) dynamically assign these values to
provide a unique identifier and nothing more.

int proc_scsi_open(struct [inode](scsi.md#c.proc_scsi_open "inode") \*inode, struct [file](scsi.md#c.proc_scsi_open "file") \*file)
:   glue function

**Parameters**

`struct inode *inode`
:   not used

`struct file *file`
:   passed to single_open()

**Description**

Associates proc_scsi_show with this file

int scsi_init_procfs(void)
:   create scsi and scsi/scsi in procfs

**Parameters**

`void`
:   no arguments

void scsi_exit_procfs(void)
:   Remove scsi/scsi and scsi from procfs

**Parameters**

`void`
:   no arguments

#### drivers/scsi/scsi_netlink.c

Infrastructure to provide async events from transports to userspace via
netlink, using a single NETLINK_SCSITRANSPORT protocol for all
transports. See [the original patch
submission](http://marc.info/?l=linux-scsi&m=115507374832500&w=2) for
more details.

void scsi_nl_rcv_msg(struct [sk_buff](../networking/kapi.md#c.sk_buff "sk_buff") \*skb)
:   Receive message handler.

**Parameters**

`struct sk_buff *skb`
:   socket receive buffer

**Description**

Extracts message from a receive buffer.
:   Validates message header and calls appropriate transport message handler

void scsi_netlink_init(void)
:   Called by SCSI subsystem to initialize the SCSI transport netlink interface

**Parameters**

`void`
:   no arguments

void scsi_netlink_exit(void)
:   Called by SCSI subsystem to disable the SCSI transport netlink interface

**Parameters**

`void`
:   no arguments

#### drivers/scsi/scsi_scan.c

Scan a host to determine which (if any) devices are attached. The
general scanning/probing algorithm is as follows, exceptions are made to
it depending on device specific flags, compilation options, and global
variable (boot or module load time) settings. A specific LUN is scanned
via an INQUIRY command; if the LUN has a device attached, a scsi_device
is allocated and setup for it. For every id of every channel on the
given host, start by scanning LUN 0. Skip hosts that don't respond at
all to a scan of LUN 0. Otherwise, if LUN 0 has a device attached,
allocate and setup a scsi_device for it. If target is SCSI-3 or up,
issue a REPORT LUN, and scan all of the LUNs returned by the REPORT LUN;
else, sequentially scan LUNs up until some maximum is reached, or a LUN
is seen that cannot have a device attached to it.

int scsi_complete_async_scans(void)
:   Wait for asynchronous scans to complete

**Parameters**

`void`
:   no arguments

**Description**

When this function returns, any host which started scanning before
this function was called will have finished its scan. Hosts which
started scanning after this function was called may or may not have
finished.

void scsi_unlock_floptical(struct scsi_device \*sdev, unsigned char \*result)
:   unlock device via a special MODE SENSE command

**Parameters**

`struct scsi_device *sdev`
:   scsi device to send command to

`unsigned char *result`
:   area to store the result of the MODE SENSE

**Description**

> Send a vendor specific MODE SENSE (not a MODE SELECT) command.
> Called for BLIST_KEY devices.

struct scsi_device \*scsi_alloc_sdev(struct scsi_target \*starget, u64 lun, void \*hostdata)
:   allocate and setup a scsi_Device

**Parameters**

`struct scsi_target *starget`
:   which target to allocate a `scsi_device` for

`u64 lun`
:   which lun

`void *hostdata`
:   usually NULL and set by ->slave_alloc instead

**Description**

> Allocate, initialize for io, and return a pointer to a scsi_Device.
> Stores the **shost**, **channel**, **id**, and **lun** in the scsi_Device, and
> adds scsi_Device to the appropriate list.

Return value:
:   scsi_Device pointer, or NULL on failure.

void scsi_target_reap_ref_release(struct [kref](scsi.md#c.scsi_target_reap_ref_release "kref") \*kref)
:   remove target from visibility

**Parameters**

`struct kref *kref`
:   the reap_ref in the target being released

**Description**

Called on last put of reap_ref, which is the indication that no device
under this target is visible anymore, so render the target invisible in
sysfs. Note: we have to be in user context here because the target reaps
should be done in places where the scsi device visibility is being removed.

struct scsi_target \*scsi_alloc_target(struct [device](infrastructure.md#c.device "device") \*parent, int channel, uint id)
:   allocate a new or find an existing target

**Parameters**

`struct device *parent`
:   parent of the target (need not be a scsi host)

`int channel`
:   target channel number (zero if no channels)

`uint id`
:   target id number

**Description**

Return an existing target if one exists, provided it hasn't already
gone into STARGET_DEL state, otherwise allocate a new target.

The target is returned with an incremented reference, so the caller
is responsible for both reaping and doing a last put

void scsi_target_reap(struct scsi_target \*starget)
:   check to see if target is in use and destroy if not

**Parameters**

`struct scsi_target *starget`
:   target to be checked

**Description**

This is used after removing a LUN or doing a last put of the target
it checks atomically that nothing is using the target and removes
it if so.

int scsi_probe_lun(struct scsi_device \*sdev, unsigned char \*inq_result, int result_len, blist_flags_t \*bflags)
:   probe a single LUN using a SCSI INQUIRY

**Parameters**

`struct scsi_device *sdev`
:   scsi_device to probe

`unsigned char *inq_result`
:   area to store the INQUIRY result

`int result_len`
:   len of inq_result

`blist_flags_t *bflags`
:   store any bflags found here

**Description**

> Probe the lun associated with **req** using a standard SCSI INQUIRY;
>
> If the INQUIRY is successful, zero is returned and the
> INQUIRY data is in **inq_result**; the scsi_level and INQUIRY length
> are copied to the scsi_device any flags value is stored in **\*bflags**.

int scsi_add_lun(struct scsi_device \*sdev, unsigned char \*inq_result, blist_flags_t \*bflags, int async)
:   allocate and fully initialze a scsi_device

**Parameters**

`struct scsi_device *sdev`
:   holds information to be stored in the new scsi_device

`unsigned char *inq_result`
:   holds the result of a previous INQUIRY to the LUN

`blist_flags_t *bflags`
:   black/white list flag

`int async`
:   1 if this device is being scanned asynchronously

**Description**

> Initialize the scsi_device **sdev**. Optionally set fields based
> on values in **\*bflags**.

**Return**

> SCSI_SCAN_NO_RESPONSE: could not allocate or setup a scsi_device
> SCSI_SCAN_LUN_PRESENT: a new scsi_device was allocated and initialized

unsigned char \*scsi_inq_str(unsigned char \*buf, unsigned char \*inq, unsigned first, unsigned end)
:   print INQUIRY data from min to max index, strip trailing whitespace

**Parameters**

`unsigned char *buf`
:   Output buffer with at least end-first+1 bytes of space

`unsigned char *inq`
:   Inquiry buffer (input)

`unsigned first`
:   Offset of string into inq

`unsigned end`
:   Index after last character in inq

int scsi_probe_and_add_lun(struct scsi_target \*starget, u64 lun, blist_flags_t \*bflagsp, struct scsi_device \*\*sdevp, enum scsi_scan_mode rescan, void \*hostdata)
:   probe a LUN, if a LUN is found add it

**Parameters**

`struct scsi_target *starget`
:   pointer to target device structure

`u64 lun`
:   LUN of target device

`blist_flags_t *bflagsp`
:   store bflags here if not NULL

`struct scsi_device **sdevp`
:   probe the LUN corresponding to this scsi_device

`enum scsi_scan_mode rescan`
:   if not equal to SCSI_SCAN_INITIAL skip some code only
    needed on first scan

`void *hostdata`
:   passed to [`scsi_alloc_sdev()`](scsi.md#c.scsi_alloc_sdev "scsi_alloc_sdev")

**Description**

> Call scsi_probe_lun, if a LUN with an attached device is found,
> allocate and set it up by calling scsi_add_lun.

**Return**

> - SCSI_SCAN_NO_RESPONSE: could not allocate or setup a scsi_device
> - SCSI_SCAN_TARGET_PRESENT: target responded, but no device is
>   :   attached at the LUN
> - SCSI_SCAN_LUN_PRESENT: a new scsi_device was allocated and initialized

void scsi_sequential_lun_scan(struct scsi_target \*starget, blist_flags_t bflags, int scsi_level, enum scsi_scan_mode rescan)
:   sequentially scan a SCSI target

**Parameters**

`struct scsi_target *starget`
:   pointer to target structure to scan

`blist_flags_t bflags`
:   black/white list flag for LUN 0

`int scsi_level`
:   Which version of the standard does this device adhere to

`enum scsi_scan_mode rescan`
:   passed to scsi_probe_add_lun()

**Description**

> Generally, scan from LUN 1 (LUN 0 is assumed to already have been
> scanned) to some maximum lun until a LUN is found with no device
> attached. Use the bflags to figure out any oddities.
>
> Modifies sdevscan->lun.

int scsi_report_lun_scan(struct scsi_target \*starget, blist_flags_t bflags, enum scsi_scan_mode rescan)
:   Scan using SCSI REPORT LUN results

**Parameters**

`struct scsi_target *starget`
:   which target

`blist_flags_t bflags`
:   Zero or a mix of BLIST_NOLUN, BLIST_REPORTLUN2, or BLIST_NOREPORTLUN

`enum scsi_scan_mode rescan`
:   nonzero if we can skip code only needed on first scan

**Description**

> Fast scanning for modern (SCSI-3) devices by sending a REPORT LUN command.
> Scan the resulting list of LUNs by calling scsi_probe_and_add_lun.
>
> If BLINK_REPORTLUN2 is set, scan a target that supports more than 8
> LUNs even if it's older than SCSI-3.
> If BLIST_NOREPORTLUN is set, return 1 always.
> If BLIST_NOLUN is set, return 0 always.
> If starget->no_report_luns is set, return 1 always.

**Return**

> 0: scan completed (or no memory, so further scanning is futile)
> 1: could not scan with REPORT LUN

struct async_scan_data \*scsi_prep_async_scan(struct Scsi_Host \*shost)
:   prepare for an async scan

**Parameters**

`struct Scsi_Host *shost`
:   the host which will be scanned

**Return**

a cookie to be passed to [`scsi_finish_async_scan()`](scsi.md#c.scsi_finish_async_scan "scsi_finish_async_scan")

**Description**

Tells the midlayer this host is going to do an asynchronous scan.
It reserves the host's position in the scanning list and ensures
that other asynchronous scans started after this one won't affect the
ordering of the discovered devices.

void scsi_finish_async_scan(struct async_scan_data \*data)
:   asynchronous scan has finished

**Parameters**

`struct async_scan_data *data`
:   cookie returned from earlier call to [`scsi_prep_async_scan()`](scsi.md#c.scsi_prep_async_scan "scsi_prep_async_scan")

**Description**

All the devices currently attached to this host have been found.
This function announces all the devices it has found to the rest
of the system.

#### drivers/scsi/scsi_sysctl.c

Set up the sysctl entry: "/dev/scsi/logging_level"
(DEV_SCSI_LOGGING_LEVEL) which sets/returns scsi_logging_level.

#### drivers/scsi/scsi_sysfs.c

SCSI sysfs interface routines.

void scsi_remove_device(struct scsi_device \*sdev)
:   unregister a device from the scsi bus

**Parameters**

`struct scsi_device *sdev`
:   scsi_device to unregister

void scsi_remove_target(struct [device](infrastructure.md#c.device "device") \*dev)
:   try to remove a target and all its devices

**Parameters**

`struct device *dev`
:   generic starget or parent of generic stargets to be removed

**Note**

This is slightly racy. It is possible that if the user
requests the addition of another device then the target won't be
removed.

#### drivers/scsi/hosts.c

mid to lowlevel SCSI driver interface

void scsi_remove_host(struct Scsi_Host \*shost)
:   remove a scsi host

**Parameters**

`struct Scsi_Host *shost`
:   a pointer to a scsi host to remove

int scsi_add_host_with_dma(struct Scsi_Host \*shost, struct [device](infrastructure.md#c.device "device") \*dev, struct [device](infrastructure.md#c.device "device") \*dma_dev)
:   add a scsi host with dma device

**Parameters**

`struct Scsi_Host *shost`
:   scsi host pointer to add

`struct device *dev`
:   a [`struct device`](infrastructure.md#c.device "device") of type scsi class

`struct device *dma_dev`
:   dma device for the host

**Note**

You rarely need to worry about this unless you're in a
virtualised host environments, so use the simpler scsi_add_host()
function instead.

**Description**

Return value:
:   0 on success / != 0 for error

struct Scsi_Host \*scsi_host_alloc(const struct scsi_host_template \*sht, int privsize)
:   register a scsi host adapter instance.

**Parameters**

`const struct scsi_host_template *sht`
:   pointer to scsi host template

`int privsize`
:   extra bytes to allocate for driver

**Note**

> Allocate a new Scsi_Host and perform basic initialization.
> The host is not published to the scsi midlayer until scsi_add_host
> is called.

**Description**

Return value:
:   Pointer to a new Scsi_Host

struct Scsi_Host \*scsi_host_lookup(unsigned int hostnum)
:   get a reference to a Scsi_Host by host no

**Parameters**

`unsigned int hostnum`
:   host number to locate

**Description**

Return value:
:   A pointer to located Scsi_Host or NULL.

    The caller must do a [`scsi_host_put()`](scsi.md#c.scsi_host_put "scsi_host_put") to drop the reference
    that [`scsi_host_get()`](scsi.md#c.scsi_host_get "scsi_host_get") took. The [`put_device()`](infrastructure.md#c.put_device "put_device") below dropped
    the reference from [`class_find_device()`](infrastructure.md#c.class_find_device "class_find_device").

struct Scsi_Host \*scsi_host_get(struct Scsi_Host \*shost)
:   inc a Scsi_Host ref count

**Parameters**

`struct Scsi_Host *shost`
:   Pointer to Scsi_Host to inc.

int scsi_host_busy(struct Scsi_Host \*shost)
:   Return the host busy counter

**Parameters**

`struct Scsi_Host *shost`
:   Pointer to Scsi_Host to inc.

void scsi_host_put(struct Scsi_Host \*shost)
:   dec a Scsi_Host ref count

**Parameters**

`struct Scsi_Host *shost`
:   Pointer to Scsi_Host to dec.

int scsi_queue_work(struct Scsi_Host \*shost, struct work_struct \*work)
:   Queue work to the Scsi_Host workqueue.

**Parameters**

`struct Scsi_Host *shost`
:   Pointer to Scsi_Host.

`struct work_struct *work`
:   Work to queue for execution.

**Description**

Return value:
:   1 - work queued for execution
    0 - work is already queued
    -EINVAL - work queue doesn't exist

void scsi_flush_work(struct Scsi_Host \*shost)
:   Flush a Scsi_Host's workqueue.

**Parameters**

`struct Scsi_Host *shost`
:   Pointer to Scsi_Host.

void scsi_host_complete_all_commands(struct Scsi_Host \*shost, enum scsi_host_status status)
:   Terminate all running commands

**Parameters**

`struct Scsi_Host *shost`
:   Scsi Host on which commands should be terminated

`enum scsi_host_status status`
:   Status to be set for the terminated commands

**Description**

There is no protection against modification of the number
of outstanding commands. It is the responsibility of the
caller to ensure that concurrent I/O submission and/or
completion is stopped when calling this function.

void scsi_host_busy_iter(struct Scsi_Host \*shost, bool (\*fn)(struct scsi_cmnd\*, void\*), void \*priv)
:   Iterate over all busy commands

**Parameters**

`struct Scsi_Host *shost`
:   Pointer to Scsi_Host.

`bool (*fn)(struct scsi_cmnd *, void *)`
:   Function to call on each busy command

`void *priv`
:   Data pointer passed to **fn**

**Description**

If locking against concurrent command completions is required
ithas to be provided by the caller

#### drivers/scsi/scsi_common.c

general support functions

const char \*scsi_device_type(unsigned type)
:   Return 17-char string indicating device type.

**Parameters**

`unsigned type`
:   type number to look up

u64 scsilun_to_int(struct scsi_lun \*scsilun)
:   convert a scsi_lun to an int

**Parameters**

`struct scsi_lun *scsilun`
:   struct scsi_lun to be converted.

**Description**

> Convert **scsilun** from a struct scsi_lun to a four-byte host byte-ordered
> integer, and return the result. The caller must check for
> truncation before using this function.

**Notes**

> For a description of the LUN format, post SCSI-3 see the SCSI
> Architecture Model, for SCSI-3 see the SCSI Controller Commands.
>
> Given a struct scsi_lun of: d2 04 0b 03 00 00 00 00, this function
> returns the integer: 0x0b03d204
>
> This encoding will return a standard integer LUN for LUNs smaller
> than 256, which typically use a single level LUN structure with
> addressing method 0.

void int_to_scsilun(u64 lun, struct scsi_lun \*scsilun)
:   reverts an int into a scsi_lun

**Parameters**

`u64 lun`
:   integer to be reverted

`struct scsi_lun *scsilun`
:   struct scsi_lun to be set.

**Description**

> Reverts the functionality of the scsilun_to_int, which packed
> an 8-byte lun value into an int. This routine unpacks the int
> back into the lun value.

**Notes**

> Given an integer : 0x0b03d204, this function returns a
> struct scsi_lun of: d2 04 0b 03 00 00 00 00

bool scsi_normalize_sense(const u8 \*sense_buffer, int sb_len, struct scsi_sense_hdr \*sshdr)
:   normalize main elements from either fixed or descriptor sense data format into a common format.

**Parameters**

`const u8 *sense_buffer`
:   byte array containing sense data returned by device

`int sb_len`
:   number of valid bytes in sense_buffer

`struct scsi_sense_hdr *sshdr`
:   pointer to instance of structure that common
    elements are written to.

**Notes**

> The "main elements" from sense data are: response_code, sense_key,
> asc, ascq and additional_length (only for descriptor format).
>
> Typically this function can be called after a device has
> responded to a SCSI command with the CHECK_CONDITION status.

**Description**

Return value:
:   true if valid sense data information found, else false;

const u8 \*scsi_sense_desc_find(const u8 \*sense_buffer, int sb_len, int desc_type)
:   search for a given descriptor type in descriptor sense data format.

**Parameters**

`const u8 * sense_buffer`
:   byte array of descriptor format sense data

`int sb_len`
:   number of valid bytes in sense_buffer

`int desc_type`
:   value of descriptor type to find
    (e.g. 0 -> information)

**Notes**

> only valid when sense data is in descriptor format

**Description**

Return value:
:   pointer to start of (first) descriptor if found else NULL

void scsi_build_sense_buffer(int desc, u8 \*buf, u8 key, u8 asc, u8 ascq)
:   build sense data in a buffer

**Parameters**

`int desc`
:   Sense format (non-zero == descriptor format,
    0 == fixed format)

`u8 *buf`
:   Where to build sense data

`u8 key`
:   Sense key

`u8 asc`
:   Additional sense code

`u8 ascq`
:   Additional sense code qualifier

int scsi_set_sense_information(u8 \*buf, int buf_len, u64 info)
:   set the information field in a formatted sense data buffer

**Parameters**

`u8 *buf`
:   Where to build sense data

`int buf_len`
:   buffer length

`u64 info`
:   64-bit information value to be set

**Description**

Return value:
:   0 on success or -EINVAL for invalid sense buffer length

int scsi_set_sense_field_pointer(u8 \*buf, int buf_len, u16 fp, u8 bp, bool cd)
:   set the field pointer sense key specific information in a formatted sense data buffer

**Parameters**

`u8 *buf`
:   Where to build sense data

`int buf_len`
:   buffer length

`u16 fp`
:   field pointer to be set

`u8 bp`
:   bit pointer to be set

`bool cd`
:   command/data bit

**Description**

Return value:
:   0 on success or -EINVAL for invalid sense buffer length

### Transport classes

Transport classes are service libraries for drivers in the SCSI lower
layer, which expose transport attributes in sysfs.

#### Fibre Channel transport

The file drivers/scsi/scsi_transport_fc.c defines transport attributes
for Fibre Channel.

u32 fc_get_event_number(void)
:   Obtain the next sequential FC event number

**Parameters**

`void`
:   no arguments

**Notes**

> We could have inlined this, but it would have required fc_event_seq to
> be exposed. For now, live with the subroutine call.
> Atomic used to avoid lock/unlock...

void fc_host_post_fc_event(struct Scsi_Host \*shost, u32 event_number, enum fc_host_event_code event_code, u32 data_len, char \*data_buf, u64 vendor_id)
:   routine to do the work of posting an event on an fc_host.

**Parameters**

`struct Scsi_Host *shost`
:   host the event occurred on

`u32 event_number`
:   fc event number obtained from get_fc_event_number()

`enum fc_host_event_code event_code`
:   fc_host event being posted

`u32 data_len`
:   amount, in bytes, of event data

`char *data_buf`
:   pointer to event data

`u64 vendor_id`
:   value for Vendor id

**Notes**

> This routine assumes no locks are held on entry.

void fc_host_post_event(struct Scsi_Host \*shost, u32 event_number, enum fc_host_event_code event_code, u32 event_data)
:   called to post an even on an fc_host.

**Parameters**

`struct Scsi_Host *shost`
:   host the event occurred on

`u32 event_number`
:   fc event number obtained from get_fc_event_number()

`enum fc_host_event_code event_code`
:   fc_host event being posted

`u32 event_data`
:   32bits of data for the event being posted

**Notes**

> This routine assumes no locks are held on entry.

void fc_host_post_vendor_event(struct Scsi_Host \*shost, u32 event_number, u32 data_len, char \*data_buf, u64 vendor_id)
:   called to post a vendor unique event on an fc_host

**Parameters**

`struct Scsi_Host *shost`
:   host the event occurred on

`u32 event_number`
:   fc event number obtained from get_fc_event_number()

`u32 data_len`
:   amount, in bytes, of vendor unique data

`char * data_buf`
:   pointer to vendor unique data

`u64 vendor_id`
:   Vendor id

**Notes**

> This routine assumes no locks are held on entry.

struct fc_rport \*fc_find_rport_by_wwpn(struct Scsi_Host \*shost, u64 wwpn)
:   find the fc_rport pointer for a given wwpn

**Parameters**

`struct Scsi_Host *shost`
:   host the fc_rport is associated with

`u64 wwpn`
:   wwpn of the fc_rport device

**Notes**

> This routine assumes no locks are held on entry.

void fc_host_fpin_rcv(struct Scsi_Host \*shost, u32 fpin_len, char \*fpin_buf, u8 event_acknowledge)
:   routine to process a received FPIN.

**Parameters**

`struct Scsi_Host *shost`
:   host the FPIN was received on

`u32 fpin_len`
:   length of FPIN payload, in bytes

`char *fpin_buf`
:   pointer to FPIN payload

`u8 event_acknowledge`
:   1, if LLDD handles this event.

**Notes**

> This routine assumes no locks are held on entry.

enum scsi_timeout_action fc_eh_timed_out(struct scsi_cmnd \*scmd)
:   FC Transport I/O timeout intercept handler

**Parameters**

`struct scsi_cmnd *scmd`
:   The SCSI command which timed out

**Description**

This routine protects against error handlers getting invoked while a
rport is in a blocked state, typically due to a temporarily loss of
connectivity. If the error handlers are allowed to proceed, requests
to abort i/o, reset the target, etc will likely fail as there is no way
to communicate with the device to perform the requested function. These
failures may result in the midlayer taking the device offline, requiring
manual intervention to restore operation.

This routine, called whenever an i/o times out, validates the state of
the underlying rport. If the rport is blocked, it returns
EH_RESET_TIMER, which will continue to reschedule the timeout.
Eventually, either the device will return, or devloss_tmo will fire,
and when the timeout then fires, it will be handled normally.
If the rport is not blocked, normal error handling continues.

**Notes**

> This routine assumes no locks are held on entry.

void fc_remove_host(struct Scsi_Host \*shost)
:   called to terminate any fc_transport-related elements for a scsi host.

**Parameters**

`struct Scsi_Host *shost`
:   Which `Scsi_Host`

**Description**

This routine is expected to be called immediately preceding the
a driver's call to [`scsi_remove_host()`](scsi.md#c.scsi_remove_host "scsi_remove_host").

WARNING: A driver utilizing the fc_transport, which fails to call
:   this routine prior to [`scsi_remove_host()`](scsi.md#c.scsi_remove_host "scsi_remove_host"), will leave dangling
    objects in /sys/class/fc_remote_ports. Access to any of these
    objects can result in a system crash !!!

**Notes**

> This routine assumes no locks are held on entry.

struct fc_rport \*fc_remote_port_add(struct Scsi_Host \*shost, int channel, struct fc_rport_identifiers \*ids)
:   notify fc transport of the existence of a remote FC port.

**Parameters**

`struct Scsi_Host *shost`
:   scsi host the remote port is connected to.

`int channel`
:   Channel on shost port connected to.

`struct fc_rport_identifiers *ids`
:   The world wide names, fc address, and FC4 port
    roles for the remote port.

**Description**

The LLDD calls this routine to notify the transport of the existence
of a remote port. The LLDD provides the unique identifiers (wwpn,wwn)
of the port, it's FC address (port_id), and the FC4 roles that are
active for the port.

For ports that are FCP targets (aka scsi targets), the FC transport
maintains consistent target id bindings on behalf of the LLDD.
A consistent target id binding is an assignment of a target id to
a remote port identifier, which persists while the scsi host is
attached. The remote port can disappear, then later reappear, and
it's target id assignment remains the same. This allows for shifts
in FC addressing (if binding by wwpn or wwnn) with no apparent
changes to the scsi subsystem which is based on scsi host number and
target id values. Bindings are only valid during the attachment of
the scsi host. If the host detaches, then later re-attaches, target
id bindings may change.

This routine is responsible for returning a remote port structure.
The routine will search the list of remote ports it maintains
internally on behalf of consistent target id mappings. If found, the
remote port structure will be reused. Otherwise, a new remote port
structure will be allocated.

Whenever a remote port is allocated, a new fc_remote_port class
device is created.

Should not be called from interrupt context.

**Notes**

> This routine assumes no locks are held on entry.

void fc_remote_port_delete(struct fc_rport \*rport)
:   notifies the fc transport that a remote port is no longer in existence.

**Parameters**

`struct fc_rport *rport`
:   The remote port that no longer exists

**Description**

The LLDD calls this routine to notify the transport that a remote
port is no longer part of the topology. Note: Although a port
may no longer be part of the topology, it may persist in the remote
ports displayed by the fc_host. We do this under 2 conditions:

1. If the port was a scsi target, we delay its deletion by "blocking" it.
   This allows the port to temporarily disappear, then reappear without
   disrupting the SCSI device tree attached to it. During the "blocked"
   period the port will still exist.
2. If the port was a scsi target and disappears for longer than we
   expect, we'll delete the port and the tear down the SCSI device tree
   attached to it. However, we want to semi-persist the target id assigned
   to that port if it eventually does exist. The port structure will
   remain (although with minimal information) so that the target id
   bindings also remain.

If the remote port is not an FCP Target, it will be fully torn down
and deallocated, including the fc_remote_port class device.

If the remote port is an FCP Target, the port will be placed in a
temporary blocked state. From the LLDD's perspective, the rport no
longer exists. From the SCSI midlayer's perspective, the SCSI target
exists, but all sdevs on it are blocked from further I/O. The following
is then expected.

> If the remote port does not return (signaled by a LLDD call to
> [`fc_remote_port_add()`](scsi.md#c.fc_remote_port_add "fc_remote_port_add")) within the dev_loss_tmo timeout, then the
> scsi target is removed - killing all outstanding i/o and removing the
> scsi devices attached to it. The port structure will be marked Not
> Present and be partially cleared, leaving only enough information to
> recognize the remote port relative to the scsi target id binding if
> it later appears. The port will remain as long as there is a valid
> binding (e.g. until the user changes the binding type or unloads the
> scsi host with the binding).
>
> If the remote port returns within the dev_loss_tmo value (and matches
> according to the target id binding type), the port structure will be
> reused. If it is no longer a SCSI target, the target will be torn
> down. If it continues to be a SCSI target, then the target will be
> unblocked (allowing i/o to be resumed), and a scan will be activated
> to ensure that all luns are detected.

Called from normal process context only - cannot be called from interrupt.

**Notes**

> This routine assumes no locks are held on entry.

void fc_remote_port_rolechg(struct fc_rport \*rport, u32 roles)
:   notifies the fc transport that the roles on a remote may have changed.

**Parameters**

`struct fc_rport *rport`
:   The remote port that changed.

`u32 roles`
:   New roles for this port.

**Description**

The LLDD calls this routine to notify the transport that the
roles on a remote port may have changed. The largest effect of this is
if a port now becomes a FCP Target, it must be allocated a
scsi target id. If the port is no longer a FCP target, any
scsi target id value assigned to it will persist in case the
role changes back to include FCP Target. No changes in the scsi
midlayer will be invoked if the role changes (in the expectation
that the role will be resumed. If it doesn't normal error processing
will take place).

Should not be called from interrupt context.

**Notes**

> This routine assumes no locks are held on entry.

int fc_block_rport(struct fc_rport \*rport)
:   Block SCSI eh thread for blocked fc_rport.

**Parameters**

`struct fc_rport *rport`
:   Remote port that scsi_eh is trying to recover.

**Description**

This routine can be called from a FC LLD scsi_eh callback. It
blocks the scsi_eh thread until the fc_rport leaves the
FC_PORTSTATE_BLOCKED, or the fast_io_fail_tmo fires. This is
necessary to avoid the scsi_eh failing recovery actions for blocked
rports which would lead to offlined SCSI devices.

**Return**

0 if the fc_rport left the state FC_PORTSTATE_BLOCKED.
:   FAST_IO_FAIL if the fast_io_fail_tmo fired, this should be
    passed back to scsi_eh.

int fc_block_scsi_eh(struct scsi_cmnd \*cmnd)
:   Block SCSI eh thread for blocked fc_rport

**Parameters**

`struct scsi_cmnd *cmnd`
:   SCSI command that scsi_eh is trying to recover

**Description**

This routine can be called from a FC LLD scsi_eh callback. It
blocks the scsi_eh thread until the fc_rport leaves the
FC_PORTSTATE_BLOCKED, or the fast_io_fail_tmo fires. This is
necessary to avoid the scsi_eh failing recovery actions for blocked
rports which would lead to offlined SCSI devices.

**Return**

0 if the fc_rport left the state FC_PORTSTATE_BLOCKED.
:   FAST_IO_FAIL if the fast_io_fail_tmo fired, this should be
    passed back to scsi_eh.

struct fc_vport \*fc_vport_create(struct Scsi_Host \*shost, int channel, struct fc_vport_identifiers \*ids)
:   Admin App or LLDD requests creation of a vport

**Parameters**

`struct Scsi_Host *shost`
:   scsi host the virtual port is connected to.

`int channel`
:   channel on shost port connected to.

`struct fc_vport_identifiers *ids`
:   The world wide names, FC4 port roles, etc for
    the virtual port.

**Notes**

> This routine assumes no locks are held on entry.

int fc_vport_terminate(struct fc_vport \*vport)
:   Admin App or LLDD requests termination of a vport

**Parameters**

`struct fc_vport *vport`
:   fc_vport to be terminated

**Description**

Calls the LLDD vport_delete() function, then deallocates and removes
the vport from the shost and object tree.

**Notes**

> This routine assumes no locks are held on entry.

#### iSCSI transport class

The file drivers/scsi/scsi_transport_iscsi.c defines transport
attributes for the iSCSI class, which sends SCSI packets over TCP/IP
connections.

struct iscsi_endpoint \*iscsi_lookup_endpoint(u64 handle)
:   get ep from handle

**Parameters**

`u64 handle`
:   endpoint handle

**Description**

Caller must do a iscsi_put_endpoint.

struct iscsi_bus_flash_session \*iscsi_create_flashnode_sess(struct Scsi_Host \*shost, int index, struct iscsi_transport \*transport, int dd_size)
:   Add flashnode session entry in sysfs

**Parameters**

`struct Scsi_Host *shost`
:   pointer to host data

`int index`
:   index of flashnode to add in sysfs

`struct iscsi_transport *transport`
:   pointer to transport data

`int dd_size`
:   total size to allocate

**Description**

Adds a sysfs entry for the flashnode session attributes

**Return**

> pointer to allocated flashnode sess on success
> `NULL` on failure

struct iscsi_bus_flash_conn \*iscsi_create_flashnode_conn(struct Scsi_Host \*shost, struct iscsi_bus_flash_session \*fnode_sess, struct iscsi_transport \*transport, int dd_size)
:   Add flashnode conn entry in sysfs

**Parameters**

`struct Scsi_Host *shost`
:   pointer to host data

`struct iscsi_bus_flash_session *fnode_sess`
:   pointer to the parent flashnode session entry

`struct iscsi_transport *transport`
:   pointer to transport data

`int dd_size`
:   total size to allocate

**Description**

Adds a sysfs entry for the flashnode connection attributes

**Return**

> pointer to allocated flashnode conn on success
> `NULL` on failure

struct [device](infrastructure.md#c.device "device") \*iscsi_find_flashnode_sess(struct Scsi_Host \*shost, void \*data, int (\*fn)(struct [device](infrastructure.md#c.device "device") \*dev, void \*data))
:   finds flashnode session entry

**Parameters**

`struct Scsi_Host *shost`
:   pointer to host data

`void *data`
:   pointer to data containing value to use for comparison

`int (*fn)(struct device *dev, void *data)`
:   function pointer that does actual comparison

**Description**

Finds the flashnode session object comparing the data passed using logic
defined in passed function pointer

**Return**

> pointer to found flashnode session device object on success
> `NULL` on failure

struct [device](infrastructure.md#c.device "device") \*iscsi_find_flashnode_conn(struct iscsi_bus_flash_session \*fnode_sess)
:   finds flashnode connection entry

**Parameters**

`struct iscsi_bus_flash_session *fnode_sess`
:   pointer to parent flashnode session entry

**Description**

Finds the flashnode connection object comparing the data passed using logic
defined in passed function pointer

**Return**

> pointer to found flashnode connection device object on success
> `NULL` on failure

void iscsi_destroy_flashnode_sess(struct iscsi_bus_flash_session \*fnode_sess)
:   destroy flashnode session entry

**Parameters**

`struct iscsi_bus_flash_session *fnode_sess`
:   pointer to flashnode session entry to be destroyed

**Description**

Deletes the flashnode session entry and all children flashnode connection
entries from sysfs

void iscsi_destroy_all_flashnode(struct Scsi_Host \*shost)
:   destroy all flashnode session entries

**Parameters**

`struct Scsi_Host *shost`
:   pointer to host data

**Description**

Destroys all the flashnode session entries and all corresponding children
flashnode connection entries from sysfs

int iscsi_block_scsi_eh(struct scsi_cmnd \*cmd)
:   block scsi eh until session state has transistioned

**Parameters**

`struct scsi_cmnd *cmd`
:   scsi cmd passed to scsi eh handler

**Description**

If the session is down this function will wait for the recovery
timer to fire or for the session to be logged back in. If the
recovery timer fires then FAST_IO_FAIL is returned. The caller
should pass this error value to the scsi eh.

void iscsi_unblock_session(struct iscsi_cls_session \*session)
:   set a session as logged in and start IO.

**Parameters**

`struct iscsi_cls_session *session`
:   iscsi session

**Description**

Mark a session as ready to accept IO.

struct iscsi_cls_session \*iscsi_create_session(struct Scsi_Host \*shost, struct iscsi_transport \*transport, int dd_size, unsigned int target_id)
:   create iscsi class session

**Parameters**

`struct Scsi_Host *shost`
:   scsi host

`struct iscsi_transport *transport`
:   iscsi transport

`int dd_size`
:   private driver data size

`unsigned int target_id`
:   which target

**Description**

This can be called from a LLD or iscsi_transport.

void iscsi_force_destroy_session(struct iscsi_cls_session \*session)
:   destroy a session from the kernel

**Parameters**

`struct iscsi_cls_session *session`
:   session to destroy

**Description**

Force the destruction of a session from the kernel. This should only be
used when userspace is no longer running during system shutdown.

struct iscsi_cls_conn \*iscsi_alloc_conn(struct iscsi_cls_session \*session, int dd_size, uint32_t cid)
:   alloc iscsi class connection

**Parameters**

`struct iscsi_cls_session *session`
:   iscsi cls session

`int dd_size`
:   private driver data size

`uint32_t cid`
:   connection id

int iscsi_add_conn(struct iscsi_cls_conn \*conn)
:   add iscsi class connection

**Parameters**

`struct iscsi_cls_conn *conn`
:   iscsi cls connection

**Description**

This will expose iscsi_cls_conn to sysfs so make sure the related
resources for sysfs attributes are initialized before calling this.

void iscsi_remove_conn(struct iscsi_cls_conn \*conn)
:   remove iscsi class connection from sysfs

**Parameters**

`struct iscsi_cls_conn *conn`
:   iscsi cls connection

**Description**

Remove iscsi_cls_conn from sysfs, and wait for previous
read/write of iscsi_cls_conn's attributes in sysfs to finish.

int iscsi_session_event(struct iscsi_cls_session \*session, enum iscsi_uevent_e event)
:   send session destr. completion event

**Parameters**

`struct iscsi_cls_session *session`
:   iscsi class session

`enum iscsi_uevent_e event`
:   type of event

#### Serial Attached SCSI (SAS) transport class

The file drivers/scsi/scsi_transport_sas.c defines transport
attributes for Serial Attached SCSI, a variant of SATA aimed at large
high-end systems.

The SAS transport class contains common code to deal with SAS HBAs, an
aproximated representation of SAS topologies in the driver model, and
various sysfs attributes to expose these topologies and management
interfaces to userspace.

In addition to the basic SCSI core objects this transport class
introduces two additional intermediate objects: The SAS PHY as
represented by struct sas_phy defines an "outgoing" PHY on a SAS HBA or
Expander, and the SAS remote PHY represented by struct sas_rphy defines
an "incoming" PHY on a SAS Expander or end device. Note that this is
purely a software concept, the underlying hardware for a PHY and a
remote PHY is the exactly the same.

There is no concept of a SAS port in this code, users can see what PHYs
form a wide port based on the port_identifier attribute, which is the
same for all PHYs in a port.

void sas_remove_children(struct [device](infrastructure.md#c.device "device") \*dev)
:   tear down a devices SAS data structures

**Parameters**

`struct device *dev`
:   device belonging to the sas object

**Description**

Removes all SAS PHYs and remote PHYs for a given object

void sas_remove_host(struct Scsi_Host \*shost)
:   tear down a Scsi_Host's SAS data structures

**Parameters**

`struct Scsi_Host *shost`
:   Scsi Host that is torn down

**Description**

Removes all SAS PHYs and remote PHYs for a given Scsi_Host and remove the
Scsi_Host as well.

**Note**

Do not call [`scsi_remove_host()`](scsi.md#c.scsi_remove_host "scsi_remove_host") on the Scsi_Host any more, as it is
already removed.

u64 sas_get_address(struct scsi_device \*sdev)
:   return the SAS address of the device

**Parameters**

`struct scsi_device *sdev`
:   scsi device

**Description**

Returns the SAS address of the scsi device

unsigned int sas_tlr_supported(struct scsi_device \*sdev)
:   checking TLR bit in vpd 0x90

**Parameters**

`struct scsi_device *sdev`
:   scsi device struct

**Description**

Check Transport Layer Retries are supported or not.
If vpd page 0x90 is present, TRL is supported.

void sas_disable_tlr(struct scsi_device \*sdev)
:   setting TLR flags

**Parameters**

`struct scsi_device *sdev`
:   scsi device struct

**Description**

Seting tlr_enabled flag to 0.

void sas_enable_tlr(struct scsi_device \*sdev)
:   setting TLR flags

**Parameters**

`struct scsi_device *sdev`
:   scsi device struct

**Description**

Seting tlr_enabled flag 1.

struct sas_phy \*sas_phy_alloc(struct [device](infrastructure.md#c.device "device") \*parent, int number)
:   allocates and initialize a SAS PHY structure

**Parameters**

`struct device *parent`
:   Parent device

`int number`
:   Phy index

**Description**

Allocates an SAS PHY structure. It will be added in the device tree
below the device specified by **parent**, which has to be either a Scsi_Host
or sas_rphy.

**Return**

> SAS PHY allocated or `NULL` if the allocation failed.

int sas_phy_add(struct sas_phy \*phy)
:   add a SAS PHY to the device hierarchy

**Parameters**

`struct sas_phy *phy`
:   The PHY to be added

**Description**

Publishes a SAS PHY to the rest of the system.

void sas_phy_free(struct sas_phy \*phy)
:   free a SAS PHY

**Parameters**

`struct sas_phy *phy`
:   SAS PHY to free

**Description**

Frees the specified SAS PHY.

**Note**

> This function must only be called on a PHY that has not
> successfully been added using [`sas_phy_add()`](scsi.md#c.sas_phy_add "sas_phy_add").

void sas_phy_delete(struct sas_phy \*phy)
:   remove SAS PHY

**Parameters**

`struct sas_phy *phy`
:   SAS PHY to remove

**Description**

Removes the specified SAS PHY. If the SAS PHY has an
associated remote PHY it is removed before.

int scsi_is_sas_phy(const struct [device](infrastructure.md#c.device "device") \*dev)
:   check if a [`struct device`](infrastructure.md#c.device "device") represents a SAS PHY

**Parameters**

`const struct device *dev`
:   device to check

**Return**

> `1` if the device represents a SAS PHY, `0` else

int sas_port_add(struct sas_port \*port)
:   add a SAS port to the device hierarchy

**Parameters**

`struct sas_port *port`
:   port to be added

**Description**

publishes a port to the rest of the system

void sas_port_free(struct sas_port \*port)
:   free a SAS PORT

**Parameters**

`struct sas_port *port`
:   SAS PORT to free

**Description**

Frees the specified SAS PORT.

**Note**

> This function must only be called on a PORT that has not
> successfully been added using [`sas_port_add()`](scsi.md#c.sas_port_add "sas_port_add").

void sas_port_delete(struct sas_port \*port)
:   remove SAS PORT

**Parameters**

`struct sas_port *port`
:   SAS PORT to remove

**Description**

Removes the specified SAS PORT. If the SAS PORT has an
associated phys, unlink them from the port as well.

int scsi_is_sas_port(const struct [device](infrastructure.md#c.device "device") \*dev)
:   check if a [`struct device`](infrastructure.md#c.device "device") represents a SAS port

**Parameters**

`const struct device *dev`
:   device to check

**Return**

> `1` if the device represents a SAS Port, `0` else

struct sas_phy \*sas_port_get_phy(struct sas_port \*port)
:   try to take a reference on a port member

**Parameters**

`struct sas_port *port`
:   port to check

void sas_port_add_phy(struct sas_port \*port, struct sas_phy \*phy)
:   add another phy to a port to form a wide port

**Parameters**

`struct sas_port *port`
:   port to add the phy to

`struct sas_phy *phy`
:   phy to add

**Description**

When a port is initially created, it is empty (has no phys). All
ports must have at least one phy to operated, and all wide ports
must have at least two. The current code makes no difference
between ports and wide ports, but the only object that can be
connected to a remote device is a port, so ports must be formed on
all devices with phys if they're connected to anything.

void sas_port_delete_phy(struct sas_port \*port, struct sas_phy \*phy)
:   remove a phy from a port or wide port

**Parameters**

`struct sas_port *port`
:   port to remove the phy from

`struct sas_phy *phy`
:   phy to remove

**Description**

This operation is used for tearing down ports again. It must be
done to every port or wide port before calling sas_port_delete.

struct sas_rphy \*sas_end_device_alloc(struct sas_port \*parent)
:   allocate an rphy for an end device

**Parameters**

`struct sas_port *parent`
:   which port

**Description**

Allocates an SAS remote PHY structure, connected to **parent**.

**Return**

> SAS PHY allocated or `NULL` if the allocation failed.

struct sas_rphy \*sas_expander_alloc(struct sas_port \*parent, enum sas_device_type type)
:   allocate an rphy for an end device

**Parameters**

`struct sas_port *parent`
:   which port

`enum sas_device_type type`
:   SAS_EDGE_EXPANDER_DEVICE or SAS_FANOUT_EXPANDER_DEVICE

**Description**

Allocates an SAS remote PHY structure, connected to **parent**.

**Return**

> SAS PHY allocated or `NULL` if the allocation failed.

int sas_rphy_add(struct sas_rphy \*rphy)
:   add a SAS remote PHY to the device hierarchy

**Parameters**

`struct sas_rphy *rphy`
:   The remote PHY to be added

**Description**

Publishes a SAS remote PHY to the rest of the system.

void sas_rphy_free(struct sas_rphy \*rphy)
:   free a SAS remote PHY

**Parameters**

`struct sas_rphy *rphy`
:   SAS remote PHY to free

**Description**

Frees the specified SAS remote PHY.

**Note**

> This function must only be called on a remote
> PHY that has not successfully been added using
> [`sas_rphy_add()`](scsi.md#c.sas_rphy_add "sas_rphy_add") (or has been [`sas_rphy_remove()`](scsi.md#c.sas_rphy_remove "sas_rphy_remove")'d)

void sas_rphy_delete(struct sas_rphy \*rphy)
:   remove and free SAS remote PHY

**Parameters**

`struct sas_rphy *rphy`
:   SAS remote PHY to remove and free

**Description**

Removes the specified SAS remote PHY and frees it.

void sas_rphy_unlink(struct sas_rphy \*rphy)
:   unlink SAS remote PHY

**Parameters**

`struct sas_rphy *rphy`
:   SAS remote phy to unlink from its parent port

**Description**

Removes port reference to an rphy

void sas_rphy_remove(struct sas_rphy \*rphy)
:   remove SAS remote PHY

**Parameters**

`struct sas_rphy *rphy`
:   SAS remote phy to remove

**Description**

Removes the specified SAS remote PHY.

int scsi_is_sas_rphy(const struct [device](infrastructure.md#c.device "device") \*dev)
:   check if a [`struct device`](infrastructure.md#c.device "device") represents a SAS remote PHY

**Parameters**

`const struct device *dev`
:   device to check

**Return**

> `1` if the device represents a SAS remote PHY, `0` else

struct scsi_transport_template \*sas_attach_transport(struct sas_function_template \*ft)
:   instantiate SAS transport template

**Parameters**

`struct sas_function_template *ft`
:   SAS transport class function template

void sas_release_transport(struct scsi_transport_template \*t)
:   release SAS transport template instance

**Parameters**

`struct scsi_transport_template *t`
:   transport template instance

#### SATA transport class

The SATA transport is handled by libata, which has its own book of
documentation in this directory.

#### Parallel SCSI (SPI) transport class

The file drivers/scsi/scsi_transport_spi.c defines transport
attributes for traditional (fast/wide/ultra) SCSI busses.

void spi_schedule_dv_device(struct scsi_device \*sdev)
:   schedule domain validation to occur on the device

**Parameters**

`struct scsi_device *sdev`
:   The device to validate

    Identical to spi_dv_device() above, except that the DV will be
    scheduled to occur in a workqueue later. All memory allocations
    are atomic, so may be called from any context including those holding
    SCSI locks.

void spi_display_xfer_agreement(struct scsi_target \*starget)
:   Print the current target transfer agreement

**Parameters**

`struct scsi_target *starget`
:   The target for which to display the agreement

**Description**

Each SPI port is required to maintain a transfer agreement for each
other port on the bus. This function prints a one-line summary of
the current agreement; more detailed information is available in sysfs.

int spi_populate_tag_msg(unsigned char \*msg, struct scsi_cmnd \*cmd)
:   place a tag message in a buffer

**Parameters**

`unsigned char *msg`
:   pointer to the area to place the tag

`struct scsi_cmnd *cmd`
:   pointer to the scsi command for the tag

**Notes**

> designed to create the correct type of tag message for the
> particular request. Returns the size of the tag message.
> May return 0 if TCQ is disabled for this device.

#### SCSI RDMA (SRP) transport class

The file drivers/scsi/scsi_transport_srp.c defines transport
attributes for SCSI over Remote Direct Memory Access.

int srp_tmo_valid(int reconnect_delay, int fast_io_fail_tmo, long dev_loss_tmo)
:   check timeout combination validity

**Parameters**

`int reconnect_delay`
:   Reconnect delay in seconds.

`int fast_io_fail_tmo`
:   Fast I/O fail timeout in seconds.

`long dev_loss_tmo`
:   Device loss timeout in seconds.

**Description**

The combination of the timeout parameters must be such that SCSI commands
are finished in a reasonable time. Hence do not allow the fast I/O fail
timeout to exceed SCSI_DEVICE_BLOCK_MAX_TIMEOUT nor allow dev_loss_tmo to
exceed that limit if failing I/O fast has been disabled. Furthermore, these
parameters must be such that multipath can detect failed paths timely.
Hence do not allow all three parameters to be disabled simultaneously.

void srp_start_tl_fail_timers(struct srp_rport \*rport)
:   start the transport layer failure timers

**Parameters**

`struct srp_rport *rport`
:   SRP target port.

**Description**

Start the transport layer fast I/O failure and device loss timers. Do not
modify a timer that was already started.

int srp_reconnect_rport(struct srp_rport \*rport)
:   reconnect to an SRP target port

**Parameters**

`struct srp_rport *rport`
:   SRP target port.

**Description**

Blocks SCSI command queueing before invoking reconnect() such that
queuecommand() won't be invoked concurrently with reconnect() from outside
the SCSI EH. This is important since a reconnect() implementation may
reallocate resources needed by queuecommand().

**Notes**

- This function neither waits until outstanding requests have finished nor
  tries to abort these. It is the responsibility of the reconnect()
  function to finish outstanding commands before reconnecting to the target
  port.
- It is the responsibility of the caller to ensure that the resources
  reallocated by the reconnect() function won't be used while this function
  is in progress. One possible strategy is to invoke this function from
  the context of the SCSI EH thread only. Another possible strategy is to
  lock the rport mutex inside each SCSI LLD callback that can be invoked by
  the SCSI EH (the scsi_host_template.eh_\*() functions and also the
  scsi_host_template.queuecommand() function).

enum scsi_timeout_action srp_timed_out(struct scsi_cmnd \*scmd)
:   SRP transport intercept of the SCSI timeout EH

**Parameters**

`struct scsi_cmnd *scmd`
:   SCSI command.

**Description**

If a timeout occurs while an rport is in the blocked state, ask the SCSI
EH to continue waiting (SCSI_EH_RESET_TIMER). Otherwise let the SCSI core
handle the timeout (SCSI_EH_NOT_HANDLED).

**Note**

This function is called from soft-IRQ context and with the request
queue lock held.

void srp_rport_get(struct srp_rport \*rport)
:   increment rport reference count

**Parameters**

`struct srp_rport *rport`
:   SRP target port.

void srp_rport_put(struct srp_rport \*rport)
:   decrement rport reference count

**Parameters**

`struct srp_rport *rport`
:   SRP target port.

struct srp_rport \*srp_rport_add(struct Scsi_Host \*shost, struct srp_rport_identifiers \*ids)
:   add a SRP remote port to the device hierarchy

**Parameters**

`struct Scsi_Host *shost`
:   scsi host the remote port is connected to.

`struct srp_rport_identifiers *ids`
:   The port id for the remote port.

**Description**

Publishes a port to the rest of the system.

void srp_rport_del(struct srp_rport \*rport)
:   remove a SRP remote port

**Parameters**

`struct srp_rport *rport`
:   SRP remote port to remove

**Description**

Removes the specified SRP remote port.

void srp_remove_host(struct Scsi_Host \*shost)
:   tear down a Scsi_Host's SRP data structures

**Parameters**

`struct Scsi_Host *shost`
:   Scsi Host that is torn down

**Description**

Removes all SRP remote ports for a given Scsi_Host.
Must be called just before scsi_remove_host for SRP HBAs.

void srp_stop_rport_timers(struct srp_rport \*rport)
:   stop the transport layer recovery timers

**Parameters**

`struct srp_rport *rport`
:   SRP remote port for which to stop the timers.

**Description**

Must be called after [`srp_remove_host()`](scsi.md#c.srp_remove_host "srp_remove_host") and [`scsi_remove_host()`](scsi.md#c.scsi_remove_host "scsi_remove_host"). The caller
must hold a reference on the rport (rport->dev) and on the SCSI host
(rport->dev.parent).

struct scsi_transport_template \*srp_attach_transport(struct srp_function_template \*ft)
:   instantiate SRP transport template

**Parameters**

`struct srp_function_template *ft`
:   SRP transport class function template

void srp_release_transport(struct scsi_transport_template \*t)
:   release SRP transport template instance

**Parameters**

`struct scsi_transport_template *t`
:   transport template instance

## SCSI lower layer

### Host Bus Adapter transport types

Many modern device controllers use the SCSI command set as a protocol to
communicate with their devices through many different types of physical
connections.

In SCSI language a bus capable of carrying SCSI commands is called a
"transport", and a controller connecting to such a bus is called a "host
bus adapter" (HBA).

#### Debug transport

The file drivers/scsi/scsi_debug.c simulates a host adapter with a
variable number of disks (or disk like devices) attached, sharing a
common amount of RAM. Does a lot of checking to make sure that we are
not getting blocks mixed up, and panics the kernel if anything out of
the ordinary is seen.

To be more realistic, the simulated devices have the transport
attributes of SAS disks.

For documentation see <http://sg.danny.cz/sg/sdebug26.html>

#### todo

Parallel (fast/wide/ultra) SCSI, USB, SATA, SAS, Fibre Channel,
FireWire, ATAPI devices, Infiniband, I2O, Parallel ports,
netlink...
