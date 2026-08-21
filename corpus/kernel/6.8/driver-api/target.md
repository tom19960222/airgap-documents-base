---
collection: kernel
version: "6.8"
title: "target and iSCSI Interfaces Guide"
source_url: https://www.kernel.org/doc/html/v6.8/driver-api/target.html
fetched_at: 2026-08-21T03:30:50+00:00
---
# target and iSCSI Interfaces Guide

## Introduction and Overview

TBD

## Target core device interfaces

This section is blank because no kerneldoc comments have been added to
drivers/target/target_core_device.c.

## Target core transport interfaces

void transport_init_session(struct se_session \*se_sess)
:   initialize a session object

**Parameters**

`struct se_session *se_sess`
:   Session object pointer.

**Description**

The caller must have zero-initialized **se_sess** before calling this function.

struct se_session \*transport_alloc_session(enum target_prot_op sup_prot_ops)
:   allocate a session object and initialize it

**Parameters**

`enum target_prot_op sup_prot_ops`
:   bitmask that defines which T10-PI modes are supported.

int transport_alloc_session_tags(struct se_session \*se_sess, unsigned int tag_num, unsigned int tag_size)
:   allocate target driver private data

**Parameters**

`struct se_session *se_sess`
:   Session pointer.

`unsigned int tag_num`
:   Maximum number of in-flight commands between initiator and target.

`unsigned int tag_size`
:   Size in bytes of the private data a target driver associates with
    each command.

int target_init_cmd(struct [se_cmd](target.md#c.target_init_cmd "se_cmd") \*se_cmd, struct se_session \*se_sess, unsigned char \*sense, u64 unpacked_lun, u32 data_length, int task_attr, int data_dir, int flags)
:   initialize se_cmd

**Parameters**

`struct se_cmd *se_cmd`
:   command descriptor to init

`struct se_session *se_sess`
:   associated se_sess for endpoint

`unsigned char *sense`
:   pointer to SCSI sense buffer

`u64 unpacked_lun`
:   unpacked LUN to reference for struct se_lun

`u32 data_length`
:   fabric expected data transfer length

`int task_attr`
:   SAM task attribute

`int data_dir`
:   DMA data direction

`int flags`
:   flags for command submission from target_sc_flags_tables

**Description**

Task tags are supported if the caller has set **se_cmd->tag**.

If the fabric driver calls target_stop_session, then it must check the
return code and handle failures. This will never fail for other drivers,
and the return code can be ignored.

**Return**

> - less than zero to signal active I/O shutdown failure.
> - zero on success.

int target_submit_prep(struct [se_cmd](target.md#c.target_submit_prep "se_cmd") \*se_cmd, unsigned char \*cdb, struct scatterlist \*sgl, u32 sgl_count, struct scatterlist \*sgl_bidi, u32 sgl_bidi_count, struct scatterlist \*sgl_prot, u32 sgl_prot_count, gfp_t gfp)
:   prepare cmd for submission

**Parameters**

`struct se_cmd *se_cmd`
:   command descriptor to prep

`unsigned char *cdb`
:   pointer to SCSI CDB

`struct scatterlist *sgl`
:   struct scatterlist memory for unidirectional mapping

`u32 sgl_count`
:   scatterlist count for unidirectional mapping

`struct scatterlist *sgl_bidi`
:   struct scatterlist memory for bidirectional READ mapping

`u32 sgl_bidi_count`
:   scatterlist count for bidirectional READ mapping

`struct scatterlist *sgl_prot`
:   struct scatterlist memory protection information

`u32 sgl_prot_count`
:   scatterlist count for protection information

`gfp_t gfp`
:   gfp allocation type

**Return**

> - less than zero to signal failure.
> - zero on success.

**Description**

If failure is returned, lio will the callers queue_status to complete
the cmd.

void target_submit_cmd(struct [se_cmd](target.md#c.target_submit_cmd "se_cmd") \*se_cmd, struct se_session \*se_sess, unsigned char \*cdb, unsigned char \*sense, u64 unpacked_lun, u32 data_length, int task_attr, int data_dir, int flags)
:   lookup unpacked lun and submit uninitialized se_cmd

**Parameters**

`struct se_cmd *se_cmd`
:   command descriptor to submit

`struct se_session *se_sess`
:   associated se_sess for endpoint

`unsigned char *cdb`
:   pointer to SCSI CDB

`unsigned char *sense`
:   pointer to SCSI sense buffer

`u64 unpacked_lun`
:   unpacked LUN to reference for struct se_lun

`u32 data_length`
:   fabric expected data transfer length

`int task_attr`
:   SAM task attribute

`int data_dir`
:   DMA data direction

`int flags`
:   flags for command submission from target_sc_flags_tables

**Description**

Task tags are supported if the caller has set **se_cmd->tag**.

This may only be called from process context, and also currently
assumes internal allocation of fabric payload buffer by target-core.

It also assumes interal target core SGL memory allocation.

This function must only be used by drivers that do their own
sync during shutdown and does not use target_stop_session. If there
is a failure this function will call into the fabric driver's
queue_status with a CHECK_CONDITION.

int target_submit(struct [se_cmd](target.md#c.target_submit "se_cmd") \*se_cmd)
:   perform final initialization and submit cmd to LIO core

**Parameters**

`struct se_cmd *se_cmd`
:   command descriptor to submit

**Description**

target_submit_prep or something similar must have been called on the cmd,
and this must be called from process context.

int target_submit_tmr(struct [se_cmd](target.md#c.target_submit_tmr "se_cmd") \*se_cmd, struct se_session \*se_sess, unsigned char \*sense, u64 unpacked_lun, void \*fabric_tmr_ptr, unsigned char tm_type, gfp_t gfp, u64 tag, int flags)
:   lookup unpacked lun and submit uninitialized se_cmd for TMR CDBs

**Parameters**

`struct se_cmd *se_cmd`
:   command descriptor to submit

`struct se_session *se_sess`
:   associated se_sess for endpoint

`unsigned char *sense`
:   pointer to SCSI sense buffer

`u64 unpacked_lun`
:   unpacked LUN to reference for struct se_lun

`void *fabric_tmr_ptr`
:   fabric context for TMR req

`unsigned char tm_type`
:   Type of TM request

`gfp_t gfp`
:   gfp type for caller

`u64 tag`
:   referenced task tag for TMR_ABORT_TASK

`int flags`
:   submit cmd flags

**Description**

Callable from all contexts.

int target_get_sess_cmd(struct [se_cmd](target.md#c.target_get_sess_cmd "se_cmd") \*se_cmd, bool ack_kref)
:   Verify the session is accepting cmds and take ref

**Parameters**

`struct se_cmd *se_cmd`
:   command descriptor to add

`bool ack_kref`
:   Signal that fabric will perform an ack [`target_put_sess_cmd()`](target.md#c.target_put_sess_cmd "target_put_sess_cmd")

int target_put_sess_cmd(struct [se_cmd](target.md#c.target_put_sess_cmd "se_cmd") \*se_cmd)
:   decrease the command reference count

**Parameters**

`struct se_cmd *se_cmd`
:   command to drop a reference from

**Description**

Returns 1 if and only if this [`target_put_sess_cmd()`](target.md#c.target_put_sess_cmd "target_put_sess_cmd") call caused the
refcount to drop to zero. Returns zero otherwise.

void target_stop_cmd_counter(struct target_cmd_counter \*cmd_cnt)
:   Stop new IO from being added to the counter.

**Parameters**

`struct target_cmd_counter *cmd_cnt`
:   counter to stop

void target_stop_session(struct se_session \*se_sess)
:   Stop new IO from being queued on the session.

**Parameters**

`struct se_session *se_sess`
:   session to stop

void target_wait_for_cmds(struct target_cmd_counter \*cmd_cnt)
:   Wait for outstanding cmds.

**Parameters**

`struct target_cmd_counter *cmd_cnt`
:   counter to wait for active I/O for.

void target_wait_for_sess_cmds(struct se_session \*se_sess)
:   Wait for outstanding commands

**Parameters**

`struct se_session *se_sess`
:   session to wait for active I/O

bool transport_wait_for_tasks(struct se_cmd \*cmd)
:   set CMD_T_STOP and wait for t_transport_stop_comp

**Parameters**

`struct se_cmd *cmd`
:   command to wait on

int target_send_busy(struct se_cmd \*cmd)
:   Send SCSI BUSY status back to the initiator

**Parameters**

`struct se_cmd *cmd`
:   SCSI command for which to send a BUSY reply.

**Note**

Only call this function if target_submit_cmd\*() failed.

## Target-supported userspace I/O

### Userspace I/O

Define a shared-memory interface for LIO to pass SCSI commands and
data to userspace for processing. This is to allow backends that
are too complex for in-kernel support to be possible.

It uses the UIO framework to do a lot of the device-creation and
introspection work for us.

See the .h file for how the ring is laid out. Note that while the
command ring is defined, the particulars of the data area are
not. Offset values in the command entry point to other locations
internal to the mmap-ed area. There is separate space outside the
command ring for data buffers. This leaves maximum flexibility for
moving buffer allocations, or even page flipping or other
allocation techniques, without altering the command ring layout.

SECURITY:
The user process must be assumed to be malicious. There's no way to
prevent it breaking the command ring protocol if it wants, but in
order to prevent other issues we must only ever read *data* from
the shared memory area, not offsets or sizes. This applies to
command ring entries as well as the mailbox. Extra code needed for
this may have a 'UAM' comment.

### Ring Design

The mmaped area is divided into three parts:
1) The mailbox (struct tcmu_mailbox, below);
2) The command ring;
3) Everything beyond the command ring (data).

The mailbox tells userspace the offset of the command ring from the
start of the shared memory region, and how big the command ring is.

The kernel passes SCSI commands to userspace by putting a struct
tcmu_cmd_entry in the ring, updating mailbox->cmd_head, and poking
userspace via UIO's interrupt mechanism.

tcmu_cmd_entry contains a header. If the header type is PAD,
userspace should skip hdr->length bytes (mod cmdr_size) to find the
next cmd_entry.

Otherwise, the entry will contain offsets into the mmaped area that
contain the cdb and data buffers -- the latter accessible via the
iov array. iov addresses are also offsets into the shared area.

When userspace is completed handling the command, set
entry->rsp.scsi_status, fill in rsp.sense_buffer if appropriate,
and also set mailbox->cmd_tail equal to the old cmd_tail plus
hdr->length, mod cmdr_size. If cmd_tail doesn't equal cmd_head, it
should process the next packet the same way, and so on.

## iSCSI helper functions

void iscsi_prep_data_out_pdu(struct iscsi_task \*task, struct iscsi_r2t_info \*r2t, struct iscsi_data \*hdr)
:   initialize Data-Out

**Parameters**

`struct iscsi_task *task`
:   scsi command task

`struct iscsi_r2t_info *r2t`
:   R2T info

`struct iscsi_data *hdr`
:   iscsi data in pdu

**Notes**

> Initialize Data-Out within this R2T sequence and finds
> proper data_offset within this SCSI command.
>
> This function is called with connection lock taken.

void __iscsi_put_task(struct iscsi_task \*task)
:   drop the refcount on a task

**Parameters**

`struct iscsi_task *task`
:   iscsi_task to drop the refcount on

**Description**

The back_lock must be held when calling in case it frees the task.

void iscsi_complete_scsi_task(struct iscsi_task \*task, uint32_t exp_cmdsn, uint32_t max_cmdsn)
:   finish scsi task normally

**Parameters**

`struct iscsi_task *task`
:   iscsi task for scsi cmd

`uint32_t exp_cmdsn`
:   expected cmd sn in cpu format

`uint32_t max_cmdsn`
:   max cmd sn in cpu format

**Description**

This is used when drivers do not need or cannot perform
lower level pdu processing.

Called with session back_lock

struct iscsi_task \*iscsi_itt_to_task(struct iscsi_conn \*conn, itt_t itt)
:   look up task by itt

**Parameters**

`struct iscsi_conn *conn`
:   iscsi connection

`itt_t itt`
:   itt

**Description**

This should be used for mgmt tasks like login and nops, or if
the LDD's itt space does not include the session age.

The session back_lock must be held.

int __iscsi_complete_pdu(struct iscsi_conn \*conn, struct iscsi_hdr \*hdr, char \*data, int datalen)
:   complete pdu

**Parameters**

`struct iscsi_conn *conn`
:   iscsi conn

`struct iscsi_hdr *hdr`
:   iscsi header

`char *data`
:   data buffer

`int datalen`
:   len of data buffer

**Description**

Completes pdu processing by freeing any resources allocated at
queuecommand or send generic. session back_lock must be held and verify
itt must have been called.

struct iscsi_task \*iscsi_itt_to_ctask(struct iscsi_conn \*conn, itt_t itt)
:   look up ctask by itt

**Parameters**

`struct iscsi_conn *conn`
:   iscsi connection

`itt_t itt`
:   itt

**Description**

This should be used for cmd tasks.

The session back_lock must be held.

void iscsi_requeue_task(struct iscsi_task \*task)
:   requeue task to run from session workqueue

**Parameters**

`struct iscsi_task *task`
:   task to requeue

**Description**

Callers must have taken a ref to the task that is going to be requeued.

void iscsi_suspend_queue(struct iscsi_conn \*conn)
:   suspend iscsi_queuecommand

**Parameters**

`struct iscsi_conn *conn`
:   iscsi conn to stop queueing IO on

**Description**

This grabs the session frwd_lock to make sure no one is in
xmit_task/queuecommand, and then sets suspend to prevent
new commands from being queued. This only needs to be called
by offload drivers that need to sync a path like ep disconnect
with the iscsi_queuecommand/xmit_task. To start IO again libiscsi
will call iscsi_start_tx and iscsi_unblock_session when in FFP.

void iscsi_suspend_tx(struct iscsi_conn \*conn)
:   suspend iscsi_data_xmit

**Parameters**

`struct iscsi_conn *conn`
:   iscsi conn to stop processing IO on.

**Description**

This function sets the suspend bit to prevent iscsi_data_xmit
from sending new IO, and if work is queued on the xmit thread
it will wait for it to be completed.

void iscsi_suspend_rx(struct iscsi_conn \*conn)
:   Prevent recvwork from running again.

**Parameters**

`struct iscsi_conn *conn`
:   iscsi conn to stop.

void iscsi_conn_unbind(struct iscsi_cls_conn \*cls_conn, bool is_active)
:   prevent queueing to conn.

**Parameters**

`struct iscsi_cls_conn *cls_conn`
:   iscsi conn ep is bound to.

`bool is_active`
:   is the conn in use for boot or is this for EH/termination

**Description**

This must be called by drivers implementing the ep_disconnect callout.
It disables queueing to the connection from libiscsi in preparation for
an ep_disconnect call.

int iscsi_eh_session_reset(struct scsi_cmnd \*sc)
:   drop session and attempt relogin

**Parameters**

`struct scsi_cmnd *sc`
:   scsi command

**Description**

This function will wait for a relogin, session termination from
userspace, or a recovery/replacement timeout.

int iscsi_eh_recover_target(struct scsi_cmnd \*sc)
:   reset target and possibly the session

**Parameters**

`struct scsi_cmnd *sc`
:   scsi command

**Description**

This will attempt to send a warm target reset. If that fails,
we will escalate to ERL0 session recovery.

int iscsi_host_add(struct Scsi_Host \*shost, struct [device](infrastructure.md#c.device "device") \*pdev)
:   add host to system

**Parameters**

`struct Scsi_Host *shost`
:   scsi host

`struct device *pdev`
:   parent device

**Description**

This should be called by partial offload and software iscsi drivers
to add a host to the system.

struct Scsi_Host \*iscsi_host_alloc(const struct scsi_host_template \*sht, int dd_data_size, bool xmit_can_sleep)
:   allocate a host and driver data

**Parameters**

`const struct scsi_host_template *sht`
:   scsi host template

`int dd_data_size`
:   driver host data size

`bool xmit_can_sleep`
:   bool indicating if LLD will queue IO from a work queue

**Description**

This should be called by partial offload and software iscsi drivers.
To access the driver specific memory use the iscsi_host_priv() macro.

void iscsi_host_remove(struct Scsi_Host \*shost, bool is_shutdown)
:   remove host and sessions

**Parameters**

`struct Scsi_Host *shost`
:   scsi host

`bool is_shutdown`
:   true if called from a driver shutdown callout

**Description**

If there are any sessions left, this will initiate the removal and wait
for the completion.

struct iscsi_cls_session \*iscsi_session_setup(struct iscsi_transport \*iscsit, struct Scsi_Host \*shost, uint16_t cmds_max, int dd_size, int cmd_task_size, uint32_t initial_cmdsn, unsigned int id)
:   create iscsi cls session and host and session

**Parameters**

`struct iscsi_transport *iscsit`
:   iscsi transport template

`struct Scsi_Host *shost`
:   scsi host

`uint16_t cmds_max`
:   session can queue

`int dd_size`
:   private driver data size, added to session allocation size

`int cmd_task_size`
:   LLD task private data size

`uint32_t initial_cmdsn`
:   initial CmdSN

`unsigned int id`
:   target ID to add to this session

**Description**

This can be used by software iscsi_transports that allocate
a session per scsi host.

Callers should set cmds_max to the largest total numer (mgmt + scsi) of
tasks they support. The iscsi layer reserves ISCSI_MGMT_CMDS_MAX tasks
for nop handling and login/logout requests.

void iscsi_session_free(struct iscsi_cls_session \*cls_session)
:   Free iscsi session and it's resources

**Parameters**

`struct iscsi_cls_session *cls_session`
:   iscsi session

void iscsi_session_teardown(struct iscsi_cls_session \*cls_session)
:   destroy session and cls_session

**Parameters**

`struct iscsi_cls_session *cls_session`
:   iscsi session

struct iscsi_cls_conn \*iscsi_conn_setup(struct iscsi_cls_session \*cls_session, int dd_size, uint32_t conn_idx)
:   create iscsi_cls_conn and iscsi_conn

**Parameters**

`struct iscsi_cls_session *cls_session`
:   iscsi_cls_session

`int dd_size`
:   private driver data size

`uint32_t conn_idx`
:   cid

void iscsi_conn_teardown(struct iscsi_cls_conn \*cls_conn)
:   teardown iscsi connection

**Parameters**

`struct iscsi_cls_conn *cls_conn`
:   iscsi class connection

**Description**

TODO: we may need to make this into a two step process
like scsi-mls remove + put host

## iSCSI boot information

struct iscsi_boot_kobj \*iscsi_boot_create_target(struct iscsi_boot_kset \*boot_kset, int index, void \*data, ssize_t (\*show)(void \*data, int type, char \*buf), umode_t (\*is_visible)(void \*data, int type), void (\*release)(void \*data))
:   create boot target sysfs dir

**Parameters**

`struct iscsi_boot_kset *boot_kset`
:   boot kset

`int index`
:   the target id

`void *data`
:   driver specific data for target

`ssize_t (*show) (void *data, int type, char *buf)`
:   attr show function

`umode_t (*is_visible) (void *data, int type)`
:   attr visibility function

`void (*release) (void *data)`
:   release function

**Note**

The boot sysfs lib will free the data passed in for the caller
when all refs to the target kobject have been released.

struct iscsi_boot_kobj \*iscsi_boot_create_initiator(struct iscsi_boot_kset \*boot_kset, int index, void \*data, ssize_t (\*show)(void \*data, int type, char \*buf), umode_t (\*is_visible)(void \*data, int type), void (\*release)(void \*data))
:   create boot initiator sysfs dir

**Parameters**

`struct iscsi_boot_kset *boot_kset`
:   boot kset

`int index`
:   the initiator id

`void *data`
:   driver specific data

`ssize_t (*show) (void *data, int type, char *buf)`
:   attr show function

`umode_t (*is_visible) (void *data, int type)`
:   attr visibility function

`void (*release) (void *data)`
:   release function

**Note**

The boot sysfs lib will free the data passed in for the caller
when all refs to the initiator kobject have been released.

struct iscsi_boot_kobj \*iscsi_boot_create_ethernet(struct iscsi_boot_kset \*boot_kset, int index, void \*data, ssize_t (\*show)(void \*data, int type, char \*buf), umode_t (\*is_visible)(void \*data, int type), void (\*release)(void \*data))
:   create boot ethernet sysfs dir

**Parameters**

`struct iscsi_boot_kset *boot_kset`
:   boot kset

`int index`
:   the ethernet device id

`void *data`
:   driver specific data

`ssize_t (*show) (void *data, int type, char *buf)`
:   attr show function

`umode_t (*is_visible) (void *data, int type)`
:   attr visibility function

`void (*release) (void *data)`
:   release function

**Note**

The boot sysfs lib will free the data passed in for the caller
when all refs to the ethernet kobject have been released.

struct iscsi_boot_kobj \*iscsi_boot_create_acpitbl(struct iscsi_boot_kset \*boot_kset, int index, void \*data, ssize_t (\*show)(void \*data, int type, char \*buf), umode_t (\*is_visible)(void \*data, int type), void (\*release)(void \*data))
:   create boot acpi table sysfs dir

**Parameters**

`struct iscsi_boot_kset *boot_kset`
:   boot kset

`int index`
:   not used

`void *data`
:   driver specific data

`ssize_t (*show)(void *data, int type, char *buf)`
:   attr show function

`umode_t (*is_visible)(void *data, int type)`
:   attr visibility function

`void (*release)(void *data)`
:   release function

**Note**

The boot sysfs lib will free the data passed in for the caller
when all refs to the acpitbl kobject have been released.

struct iscsi_boot_kset \*iscsi_boot_create_kset(const char \*set_name)
:   creates root sysfs tree

**Parameters**

`const char *set_name`
:   name of root dir

struct iscsi_boot_kset \*iscsi_boot_create_host_kset(unsigned int hostno)
:   creates root sysfs tree for a scsi host

**Parameters**

`unsigned int hostno`
:   host number of scsi host

void iscsi_boot_destroy_kset(struct iscsi_boot_kset \*boot_kset)
:   destroy kset and kobjects under it

**Parameters**

`struct iscsi_boot_kset *boot_kset`
:   boot kset

**Description**

This will remove the kset and kobjects and attrs under it.

## iSCSI TCP interfaces

int iscsi_sw_tcp_recv(read_descriptor_t \*rd_desc, struct [sk_buff](../networking/kapi.md#c.sk_buff "sk_buff") \*skb, unsigned int offset, size_t len)
:   TCP receive in sendfile fashion

**Parameters**

`read_descriptor_t *rd_desc`
:   read descriptor

`struct sk_buff *skb`
:   socket buffer

`unsigned int offset`
:   offset in skb

`size_t len`
:   skb->len - offset

int iscsi_sw_sk_state_check(struct [sock](../networking/kapi.md#c.sock "sock") \*sk)
:   check socket state

**Parameters**

`struct sock *sk`
:   socket

**Description**

If the socket is in CLOSE or CLOSE_WAIT we should
not close the connection if there is still some
data pending.

Must be called with sk_callback_lock.

void iscsi_sw_tcp_write_space(struct [sock](../networking/kapi.md#c.sock "sock") \*sk)
:   Called when more output buffer space is available

**Parameters**

`struct sock *sk`
:   socket space is available for

int iscsi_sw_tcp_xmit_segment(struct iscsi_tcp_conn \*tcp_conn, struct iscsi_segment \*segment)
:   transmit segment

**Parameters**

`struct iscsi_tcp_conn *tcp_conn`
:   the iSCSI TCP connection

`struct iscsi_segment *segment`
:   the buffer to transmnit

**Description**

This function transmits as much of the buffer as
the network layer will accept, and returns the number of
bytes transmitted.

If CRC hashing is enabled, the function will compute the
hash as it goes. When the entire segment has been transmitted,
it will retrieve the hash value and send it as well.

int iscsi_sw_tcp_xmit(struct iscsi_conn \*conn)
:   TCP transmit

**Parameters**

`struct iscsi_conn *conn`
:   iscsi connection

int iscsi_sw_tcp_xmit_qlen(struct iscsi_conn \*conn)
:   return the number of bytes queued for xmit

**Parameters**

`struct iscsi_conn *conn`
:   iscsi connection

int iscsi_tcp_segment_done(struct iscsi_tcp_conn \*tcp_conn, struct iscsi_segment \*segment, int recv, unsigned copied)
:   check whether the segment is complete

**Parameters**

`struct iscsi_tcp_conn *tcp_conn`
:   iscsi tcp connection

`struct iscsi_segment *segment`
:   iscsi segment to check

`int recv`
:   set to one of this is called from the recv path

`unsigned copied`
:   number of bytes copied

**Description**

Check if we're done receiving this segment. If the receive
buffer is full but we expect more data, move on to the
next entry in the scatterlist.

If the amount of data we received isn't a multiple of 4,
we will transparently receive the pad bytes, too.

This function must be re-entrant.

void iscsi_tcp_hdr_recv_prep(struct iscsi_tcp_conn \*tcp_conn)
:   prep segment for hdr reception

**Parameters**

`struct iscsi_tcp_conn *tcp_conn`
:   iscsi connection to prep for

**Description**

This function always passes NULL for the hash argument, because when this
function is called we do not yet know the final size of the header and want
to delay the digest processing until we know that.

void iscsi_tcp_cleanup_task(struct iscsi_task \*task)
:   free tcp_task resources

**Parameters**

`struct iscsi_task *task`
:   iscsi task

**Description**

must be called with session back_lock

int iscsi_tcp_recv_segment_is_hdr(struct iscsi_tcp_conn \*tcp_conn)
:   tests if we are reading in a header

**Parameters**

`struct iscsi_tcp_conn *tcp_conn`
:   iscsi tcp conn

**Description**

returns non zero if we are currently processing or setup to process
a header.

int iscsi_tcp_recv_skb(struct iscsi_conn \*conn, struct [sk_buff](../networking/kapi.md#c.sk_buff "sk_buff") \*skb, unsigned int offset, bool offloaded, int \*status)
:   Process skb

**Parameters**

`struct iscsi_conn *conn`
:   iscsi connection

`struct sk_buff *skb`
:   network buffer with header and/or data segment

`unsigned int offset`
:   offset in skb

`bool offloaded`
:   bool indicating if transfer was offloaded

`int *status`
:   iscsi TCP status result

**Description**

Will return status of transfer in **status**. And will return
number of bytes copied.

int iscsi_tcp_task_init(struct iscsi_task \*task)
:   Initialize iSCSI SCSI_READ or SCSI_WRITE commands

**Parameters**

`struct iscsi_task *task`
:   scsi command task

int iscsi_tcp_task_xmit(struct iscsi_task \*task)
:   xmit normal PDU task

**Parameters**

`struct iscsi_task *task`
:   iscsi command task

**Description**

We're expected to return 0 when everything was transmitted successfully,
-EAGAIN if there's still data in the queue, or != 0 for any other kind
of error.
