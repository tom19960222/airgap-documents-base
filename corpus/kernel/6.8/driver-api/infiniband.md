---
collection: kernel
version: "6.8"
title: "InfiniBand and Remote DMA (RDMA) Interfaces"
source_url: https://www.kernel.org/doc/html/v6.8/driver-api/infiniband.html
fetched_at: 2026-08-21T03:30:35+00:00
---
# InfiniBand and Remote DMA (RDMA) Interfaces

## Introduction and Overview

TBD

## InfiniBand core interfaces

struct iwpm_nlmsg_request \*iwpm_get_nlmsg_request(__u32 nlmsg_seq, u8 nl_client, gfp_t gfp)
:   Allocate and initialize netlink message request

**Parameters**

`__u32 nlmsg_seq`
:   Sequence number of the netlink message

`u8 nl_client`
:   The index of the netlink client

`gfp_t gfp`
:   Indicates how the memory for the request should be allocated

**Description**

Returns the newly allocated netlink request object if successful,
otherwise returns NULL

void iwpm_free_nlmsg_request(struct [kref](infiniband.md#c.iwpm_free_nlmsg_request "kref") \*kref)
:   Deallocate netlink message request

**Parameters**

`struct kref *kref`
:   Holds reference of netlink message request

struct iwpm_nlmsg_request \*iwpm_find_nlmsg_request(__u32 echo_seq)
:   Find netlink message request in the request list

**Parameters**

`__u32 echo_seq`
:   Sequence number of the netlink request to find

**Description**

Returns the found netlink message request,
if not found, returns NULL

int iwpm_wait_complete_req(struct iwpm_nlmsg_request \*nlmsg_request)
:   Block while servicing the netlink request

**Parameters**

`struct iwpm_nlmsg_request *nlmsg_request`
:   Netlink message request to service

**Description**

Wakes up, after the request is completed or expired
Returns 0 if the request is complete without error

int iwpm_get_nlmsg_seq(void)
:   Get the sequence number for a netlink message to send to the port mapper

**Parameters**

`void`
:   no arguments

**Description**

Returns the sequence number for the netlink message.

void iwpm_add_remote_info(struct iwpm_remote_info \*reminfo)
:   Add remote address info of the connecting peer to the remote info hash table

**Parameters**

`struct iwpm_remote_info *reminfo`
:   The remote info to be added

u32 iwpm_check_registration(u8 nl_client, u32 reg)
:   Check if the client registration matches the given one

**Parameters**

`u8 nl_client`
:   The index of the netlink client

`u32 reg`
:   The given registration type to compare with

**Description**

Call iwpm_register_pid() to register a client
Returns true if the client registration matches reg,
otherwise returns false

void iwpm_set_registration(u8 nl_client, u32 reg)
:   Set the client registration

**Parameters**

`u8 nl_client`
:   The index of the netlink client

`u32 reg`
:   Registration type to set

u32 iwpm_get_registration(u8 nl_client)
:   Get the client registration

**Parameters**

`u8 nl_client`
:   The index of the netlink client

**Description**

Returns the client registration type

int iwpm_send_mapinfo(u8 nl_client, int iwpm_pid)
:   Send local and mapped IPv4/IPv6 address info of a client to the user space port mapper

**Parameters**

`u8 nl_client`
:   The index of the netlink client

`int iwpm_pid`
:   The pid of the user space port mapper

**Description**

If successful, returns the number of sent mapping info records

int iwpm_mapinfo_available(void)
:   Check if any mapping info records is available in the hash table

**Parameters**

`void`
:   no arguments

**Description**

Returns 1 if mapping information is available, otherwise returns 0

int iwpm_compare_sockaddr(struct sockaddr_storage \*a_sockaddr, struct sockaddr_storage \*b_sockaddr)
:   Compare two sockaddr storage structs

**Parameters**

`struct sockaddr_storage *a_sockaddr`
:   first sockaddr to compare

`struct sockaddr_storage *b_sockaddr`
:   second sockaddr to compare

**Return**

0 if they are holding the same ip/tcp address info,
otherwise returns 1

int iwpm_validate_nlmsg_attr(struct nlattr \*nltb[], int nla_count)
:   Check for NULL netlink attributes

**Parameters**

`struct nlattr *nltb[]`
:   Holds address of each netlink message attributes

`int nla_count`
:   Number of netlink message attributes

**Description**

Returns error if any of the nla_count attributes is NULL

struct [sk_buff](../networking/kapi.md#c.sk_buff "sk_buff") \*iwpm_create_nlmsg(u32 nl_op, struct [nlmsghdr](../userspace-api/netlink/intro.md#c.nlmsghdr "nlmsghdr") \*\*nlh, int nl_client)
:   Allocate skb and form a netlink message

**Parameters**

`u32 nl_op`
:   Netlink message opcode

`struct nlmsghdr **nlh`
:   Holds address of the netlink message header in skb

`int nl_client`
:   The index of the netlink client

**Description**

Returns the newly allcated skb, or NULL if the tailroom of the skb
is insufficient to store the message header and payload

int iwpm_parse_nlmsg(struct netlink_callback \*cb, int policy_max, const struct nla_policy \*nlmsg_policy, struct nlattr \*nltb[], const char \*msg_type)
:   Validate and parse the received netlink message

**Parameters**

`struct netlink_callback *cb`
:   Netlink callback structure

`int policy_max`
:   Maximum attribute type to be expected

`const struct nla_policy *nlmsg_policy`
:   Validation policy

`struct nlattr *nltb[]`
:   Array to store policy_max parsed elements

`const char *msg_type`
:   Type of netlink message

**Description**

Returns 0 on success or a negative error code

void iwpm_print_sockaddr(struct sockaddr_storage \*sockaddr, char \*msg)
:   Print IPv4/IPv6 address and TCP port

**Parameters**

`struct sockaddr_storage *sockaddr`
:   Socket address to print

`char *msg`
:   Message to print

int iwpm_send_hello(u8 nl_client, int iwpm_pid, u16 abi_version)
:   Send hello response to iwpmd

**Parameters**

`u8 nl_client`
:   The index of the netlink client

`int iwpm_pid`
:   The pid of the user space port mapper

`u16 abi_version`
:   The kernel's abi_version

**Description**

Returns 0 on success or a negative error code

int ib_process_cq_direct(struct ib_cq \*cq, int budget)
:   process a CQ in caller context

**Parameters**

`struct ib_cq *cq`
:   CQ to process

`int budget`
:   number of CQEs to poll for

**Description**

This function is used to process all outstanding CQ entries.
It does not offload CQ processing to a different context and does
not ask for completion interrupts from the HCA.
Using direct processing on CQ with non IB_POLL_DIRECT type may trigger
concurrent processing.

**Note**

do not pass -1 as `budget` unless it is guaranteed that the number
of completions that will be processed is small.

struct ib_cq \*__ib_alloc_cq(struct ib_device \*dev, void \*private, int nr_cqe, int comp_vector, enum ib_poll_context poll_ctx, const char \*caller)
:   allocate a completion queue

**Parameters**

`struct ib_device *dev`
:   device to allocate the CQ for

`void *private`
:   driver private data, accessible from cq->cq_context

`int nr_cqe`
:   number of CQEs to allocate

`int comp_vector`
:   HCA completion vectors for this CQ

`enum ib_poll_context poll_ctx`
:   context to poll the CQ from.

`const char *caller`
:   module owner name.

**Description**

This is the proper interface to allocate a CQ for in-kernel users. A
CQ allocated with this interface will automatically be polled from the
specified context. The ULP must use wr->wr_cqe instead of wr->wr_id
to use this CQ abstraction.

struct ib_cq \*__ib_alloc_cq_any(struct ib_device \*dev, void \*private, int nr_cqe, enum ib_poll_context poll_ctx, const char \*caller)
:   allocate a completion queue

**Parameters**

`struct ib_device *dev`
:   device to allocate the CQ for

`void *private`
:   driver private data, accessible from cq->cq_context

`int nr_cqe`
:   number of CQEs to allocate

`enum ib_poll_context poll_ctx`
:   context to poll the CQ from

`const char *caller`
:   module owner name

**Description**

Attempt to spread ULP Completion Queues over each device's interrupt
vectors. A simple best-effort mechanism is used.

void ib_free_cq(struct ib_cq \*cq)
:   free a completion queue

**Parameters**

`struct ib_cq *cq`
:   completion queue to free.

struct ib_cq \*ib_cq_pool_get(struct ib_device \*dev, unsigned int nr_cqe, int comp_vector_hint, enum ib_poll_context poll_ctx)
:   Find the least used completion queue that matches a given cpu hint (or least used for wild card affinity) and fits nr_cqe.

**Parameters**

`struct ib_device *dev`
:   rdma device

`unsigned int nr_cqe`
:   number of needed cqe entries

`int comp_vector_hint`
:   completion vector hint (-1) for the driver to assign
    a comp vector based on internal counter

`enum ib_poll_context poll_ctx`
:   cq polling context

**Description**

Finds a cq that satisfies **comp_vector_hint** and **nr_cqe** requirements and
claim entries in it for us. In case there is no available cq, allocate
a new cq with the requirements and add it to the device pool.
IB_POLL_DIRECT cannot be used for shared cqs so it is not a valid value
for **poll_ctx**.

void ib_cq_pool_put(struct ib_cq \*cq, unsigned int nr_cqe)
:   Return a CQ taken from a shared pool.

**Parameters**

`struct ib_cq *cq`
:   The CQ to return.

`unsigned int nr_cqe`
:   The max number of cqes that the user had requested.

int ib_cm_listen(struct ib_cm_id \*cm_id, __be64 service_id)
:   Initiates listening on the specified service ID for connection and service ID resolution requests.

**Parameters**

`struct ib_cm_id *cm_id`
:   Connection identifier associated with the listen request.

`__be64 service_id`
:   Service identifier matched against incoming connection
    and service ID resolution requests. The service ID should be specified
    network-byte order. If set to IB_CM_ASSIGN_SERVICE_ID, the CM will
    assign a service ID to the caller.

struct ib_cm_id \*ib_cm_insert_listen(struct ib_device \*device, ib_cm_handler cm_handler, __be64 service_id)
:   Create a new listening ib_cm_id and listen on the given service ID.

**Parameters**

`struct ib_device *device`
:   Device associated with the cm_id. All related communication will
    be associated with the specified device.

`ib_cm_handler cm_handler`
:   Callback invoked to notify the user of CM events.

`__be64 service_id`
:   Service identifier matched against incoming connection
    and service ID resolution requests. The service ID should be specified
    network-byte order. If set to IB_CM_ASSIGN_SERVICE_ID, the CM will
    assign a service ID to the caller.

**Description**

If there's an existing ID listening on that same device and service ID,
return it.

Callers should call ib_destroy_cm_id when done with the listener ID.

int rdma_rw_ctx_init(struct rdma_rw_ctx \*ctx, struct ib_qp \*qp, u32 port_num, struct scatterlist \*sg, u32 sg_cnt, u32 sg_offset, u64 remote_addr, u32 rkey, enum dma_data_direction dir)
:   initialize a RDMA READ/WRITE context

**Parameters**

`struct rdma_rw_ctx *ctx`
:   context to initialize

`struct ib_qp *qp`
:   queue pair to operate on

`u32 port_num`
:   port num to which the connection is bound

`struct scatterlist *sg`
:   scatterlist to READ/WRITE from/to

`u32 sg_cnt`
:   number of entries in **sg**

`u32 sg_offset`
:   current byte offset into **sg**

`u64 remote_addr`
:   remote address to read/write (relative to **rkey**)

`u32 rkey`
:   remote key to operate on

`enum dma_data_direction dir`
:   `DMA_TO_DEVICE` for RDMA WRITE, `DMA_FROM_DEVICE` for RDMA READ

**Description**

Returns the number of WQEs that will be needed on the workqueue if
successful, or a negative error code.

int rdma_rw_ctx_signature_init(struct rdma_rw_ctx \*ctx, struct ib_qp \*qp, u32 port_num, struct scatterlist \*sg, u32 sg_cnt, struct scatterlist \*prot_sg, u32 prot_sg_cnt, struct ib_sig_attrs \*sig_attrs, u64 remote_addr, u32 rkey, enum dma_data_direction dir)
:   initialize a RW context with signature offload

**Parameters**

`struct rdma_rw_ctx *ctx`
:   context to initialize

`struct ib_qp *qp`
:   queue pair to operate on

`u32 port_num`
:   port num to which the connection is bound

`struct scatterlist *sg`
:   scatterlist to READ/WRITE from/to

`u32 sg_cnt`
:   number of entries in **sg**

`struct scatterlist *prot_sg`
:   scatterlist to READ/WRITE protection information from/to

`u32 prot_sg_cnt`
:   number of entries in **prot_sg**

`struct ib_sig_attrs *sig_attrs`
:   signature offloading algorithms

`u64 remote_addr`
:   remote address to read/write (relative to **rkey**)

`u32 rkey`
:   remote key to operate on

`enum dma_data_direction dir`
:   `DMA_TO_DEVICE` for RDMA WRITE, `DMA_FROM_DEVICE` for RDMA READ

**Description**

Returns the number of WQEs that will be needed on the workqueue if
successful, or a negative error code.

struct ib_send_wr \*rdma_rw_ctx_wrs(struct rdma_rw_ctx \*ctx, struct ib_qp \*qp, u32 port_num, struct ib_cqe \*cqe, struct ib_send_wr \*chain_wr)
:   return chain of WRs for a RDMA READ or WRITE operation

**Parameters**

`struct rdma_rw_ctx *ctx`
:   context to operate on

`struct ib_qp *qp`
:   queue pair to operate on

`u32 port_num`
:   port num to which the connection is bound

`struct ib_cqe *cqe`
:   completion queue entry for the last WR

`struct ib_send_wr *chain_wr`
:   WR to append to the posted chain

**Description**

Return the WR chain for the set of RDMA READ/WRITE operations described by
**ctx**, as well as any memory registration operations needed. If **chain_wr**
is non-NULL the WR it points to will be appended to the chain of WRs posted.
If **chain_wr** is not set **cqe** must be set so that the caller gets a
completion notification.

int rdma_rw_ctx_post(struct rdma_rw_ctx \*ctx, struct ib_qp \*qp, u32 port_num, struct ib_cqe \*cqe, struct ib_send_wr \*chain_wr)
:   post a RDMA READ or RDMA WRITE operation

**Parameters**

`struct rdma_rw_ctx *ctx`
:   context to operate on

`struct ib_qp *qp`
:   queue pair to operate on

`u32 port_num`
:   port num to which the connection is bound

`struct ib_cqe *cqe`
:   completion queue entry for the last WR

`struct ib_send_wr *chain_wr`
:   WR to append to the posted chain

**Description**

Post the set of RDMA READ/WRITE operations described by **ctx**, as well as
any memory registration operations needed. If **chain_wr** is non-NULL the
WR it points to will be appended to the chain of WRs posted. If **chain_wr**
is not set **cqe** must be set so that the caller gets a completion
notification.

void rdma_rw_ctx_destroy(struct rdma_rw_ctx \*ctx, struct ib_qp \*qp, u32 port_num, struct scatterlist \*sg, u32 sg_cnt, enum dma_data_direction dir)
:   release all resources allocated by rdma_rw_ctx_init

**Parameters**

`struct rdma_rw_ctx *ctx`
:   context to release

`struct ib_qp *qp`
:   queue pair to operate on

`u32 port_num`
:   port num to which the connection is bound

`struct scatterlist *sg`
:   scatterlist that was used for the READ/WRITE

`u32 sg_cnt`
:   number of entries in **sg**

`enum dma_data_direction dir`
:   `DMA_TO_DEVICE` for RDMA WRITE, `DMA_FROM_DEVICE` for RDMA READ

void rdma_rw_ctx_destroy_signature(struct rdma_rw_ctx \*ctx, struct ib_qp \*qp, u32 port_num, struct scatterlist \*sg, u32 sg_cnt, struct scatterlist \*prot_sg, u32 prot_sg_cnt, enum dma_data_direction dir)
:   release all resources allocated by rdma_rw_ctx_signature_init

**Parameters**

`struct rdma_rw_ctx *ctx`
:   context to release

`struct ib_qp *qp`
:   queue pair to operate on

`u32 port_num`
:   port num to which the connection is bound

`struct scatterlist *sg`
:   scatterlist that was used for the READ/WRITE

`u32 sg_cnt`
:   number of entries in **sg**

`struct scatterlist *prot_sg`
:   scatterlist that was used for the READ/WRITE of the PI

`u32 prot_sg_cnt`
:   number of entries in **prot_sg**

`enum dma_data_direction dir`
:   `DMA_TO_DEVICE` for RDMA WRITE, `DMA_FROM_DEVICE` for RDMA READ

unsigned int rdma_rw_mr_factor(struct ib_device \*device, u32 port_num, unsigned int maxpages)
:   return number of MRs required for a payload

**Parameters**

`struct ib_device *device`
:   device handling the connection

`u32 port_num`
:   port num to which the connection is bound

`unsigned int maxpages`
:   maximum payload pages per rdma_rw_ctx

**Description**

Returns the number of MRs the device requires to move **maxpayload**
bytes. The returned value is used during transport creation to
compute max_rdma_ctxts and the size of the transport's Send and
Send Completion Queues.

bool rdma_dev_access_netns(const struct ib_device \*dev, const struct [net](infiniband.md#c.rdma_dev_access_netns "net") \*net)
:   Return whether an rdma device can be accessed from a specified net namespace or not.

**Parameters**

`const struct ib_device *dev`
:   Pointer to rdma device which needs to be checked

`const struct net *net`
:   Pointer to net namesapce for which access to be checked

**Description**

When the rdma device is in shared mode, it ignores the net namespace.
When the rdma device is exclusive to a net namespace, rdma device net
namespace is checked against the specified one.

void ib_device_put(struct ib_device \*device)
:   Release IB device reference

**Parameters**

`struct ib_device *device`
:   device whose reference to be released

**Description**

[`ib_device_put()`](infiniband.md#c.ib_device_put "ib_device_put") releases reference to the IB device to allow it to be
unregistered and eventually free.

struct ib_device \*ib_device_get_by_name(const char \*name, enum rdma_driver_id driver_id)
:   Find an IB device by name

**Parameters**

`const char *name`
:   The name to look for

`enum rdma_driver_id driver_id`
:   The driver ID that must match (RDMA_DRIVER_UNKNOWN matches all)

**Description**

Find and hold an ib_device by its name. The caller must call
[`ib_device_put()`](infiniband.md#c.ib_device_put "ib_device_put") on the returned pointer.

struct ib_device \*_ib_alloc_device(size_t size)
:   allocate an IB device struct

**Parameters**

`size_t size`
:   size of structure to allocate

**Description**

Low-level drivers should use ib_alloc_device() to allocate `struct
ib_device`. **size** is the size of the structure to be allocated,
including any private data used by the low-level driver.
[`ib_dealloc_device()`](infiniband.md#c.ib_dealloc_device "ib_dealloc_device") must be used to free structures allocated with
ib_alloc_device().

void ib_dealloc_device(struct ib_device \*device)
:   free an IB device struct

**Parameters**

`struct ib_device *device`
:   structure to free

**Description**

Free a structure allocated with ib_alloc_device().

const struct ib_port_immutable \*ib_port_immutable_read(struct ib_device \*dev, unsigned int port)
:   Read rdma port's immutable data

**Parameters**

`struct ib_device *dev`
:   IB device

`unsigned int port`
:   port number whose immutable data to read. It starts with index 1 and
    valid upto including rdma_end_port().

int ib_register_device(struct ib_device \*device, const char \*name, struct [device](infiniband.md#c.ib_register_device "device") \*dma_device)
:   Register an IB device with IB core

**Parameters**

`struct ib_device *device`
:   Device to register

`const char *name`
:   unique string device name. This may include a '%' which will
    cause a unique index to be added to the passed device name.

`struct device *dma_device`
:   pointer to a DMA-capable device. If `NULL`, then the IB
    device will be used. In this case the caller should fully
    setup the ibdev for DMA. This usually means using dma_virt_ops.

**Description**

Low-level drivers use [`ib_register_device()`](infiniband.md#c.ib_register_device "ib_register_device") to register their
devices with the IB core. All registered clients will receive a
callback for each device that is added. **device** must be allocated
with ib_alloc_device().

If the driver uses ops.dealloc_driver and calls any [`ib_unregister_device()`](infiniband.md#c.ib_unregister_device "ib_unregister_device")
asynchronously then the device pointer may become freed as soon as this
function returns.

void ib_unregister_device(struct ib_device \*ib_dev)
:   Unregister an IB device

**Parameters**

`struct ib_device *ib_dev`
:   The device to unregister

**Description**

Unregister an IB device. All clients will receive a remove callback.

Callers should call this routine only once, and protect against races with
registration. Typically it should only be called as part of a remove
callback in an implementation of driver core's [`struct device_driver`](infrastructure.md#c.device_driver "device_driver") and
related.

If ops.dealloc_driver is used then ib_dev will be freed upon return from
this function.

void ib_unregister_device_and_put(struct ib_device \*ib_dev)
:   Unregister a device while holding a 'get'

**Parameters**

`struct ib_device *ib_dev`
:   The device to unregister

**Description**

This is the same as [`ib_unregister_device()`](infiniband.md#c.ib_unregister_device "ib_unregister_device"), except it includes an internal
[`ib_device_put()`](infiniband.md#c.ib_device_put "ib_device_put") that should match a 'get' obtained by the caller.

It is safe to call this routine concurrently from multiple threads while
holding the 'get'. When the function returns the device is fully
unregistered.

Drivers using this flow MUST use the driver_unregister callback to clean up
their resources associated with the device and dealloc it.

void ib_unregister_driver(enum rdma_driver_id driver_id)
:   Unregister all IB devices for a driver

**Parameters**

`enum rdma_driver_id driver_id`
:   The driver to unregister

**Description**

This implements a fence for device unregistration. It only returns once all
devices associated with the driver_id have fully completed their
unregistration and returned from ib_unregister_device\*().

If device's are not yet unregistered it goes ahead and starts unregistering
them.

This does not block creation of new devices with the given driver_id, that
is the responsibility of the caller.

void ib_unregister_device_queued(struct ib_device \*ib_dev)
:   Unregister a device using a work queue

**Parameters**

`struct ib_device *ib_dev`
:   The device to unregister

**Description**

This schedules an asynchronous unregistration using a WQ for the device. A
driver should use this to avoid holding locks while doing unregistration,
such as holding the RTNL lock.

Drivers using this API must use ib_unregister_driver before module unload
to ensure that all scheduled unregistrations have completed.

int ib_register_client(struct ib_client \*client)
:   Register an IB client

**Parameters**

`struct ib_client *client`
:   Client to register

**Description**

Upper level users of the IB drivers can use [`ib_register_client()`](infiniband.md#c.ib_register_client "ib_register_client") to
register callbacks for IB device addition and removal. When an IB
device is added, each registered client's add method will be called
(in the order the clients were registered), and when a device is
removed, each client's remove method will be called (in the reverse
order that clients were registered). In addition, when
[`ib_register_client()`](infiniband.md#c.ib_register_client "ib_register_client") is called, the client will receive an add
callback for all devices already registered.

void ib_unregister_client(struct ib_client \*client)
:   Unregister an IB client

**Parameters**

`struct ib_client *client`
:   Client to unregister

**Description**

Upper level users use [`ib_unregister_client()`](infiniband.md#c.ib_unregister_client "ib_unregister_client") to remove their client
registration. When [`ib_unregister_client()`](infiniband.md#c.ib_unregister_client "ib_unregister_client") is called, the client
will receive a remove callback for each IB device still registered.

This is a full fence, once it returns no client callbacks will be called,
or are running in another thread.

void ib_set_client_data(struct ib_device \*device, struct ib_client \*client, void \*data)
:   Set IB client context

**Parameters**

`struct ib_device *device`
:   Device to set context for

`struct ib_client *client`
:   Client to set context for

`void *data`
:   Context to set

**Description**

[`ib_set_client_data()`](infiniband.md#c.ib_set_client_data "ib_set_client_data") sets client context data that can be retrieved with
ib_get_client_data(). This can only be called while the client is
registered to the device, once the ib_client remove() callback returns this
cannot be called.

void ib_register_event_handler(struct ib_event_handler \*event_handler)
:   Register an IB event handler

**Parameters**

`struct ib_event_handler *event_handler`
:   Handler to register

**Description**

[`ib_register_event_handler()`](infiniband.md#c.ib_register_event_handler "ib_register_event_handler") registers an event handler that will be
called back when asynchronous IB events occur (as defined in
chapter 11 of the InfiniBand Architecture Specification). This
callback occurs in workqueue context.

void ib_unregister_event_handler(struct ib_event_handler \*event_handler)
:   Unregister an event handler

**Parameters**

`struct ib_event_handler *event_handler`
:   Handler to unregister

**Description**

Unregister an event handler registered with
[`ib_register_event_handler()`](infiniband.md#c.ib_register_event_handler "ib_register_event_handler").

int ib_query_port(struct ib_device \*device, u32 port_num, struct ib_port_attr \*port_attr)
:   Query IB port attributes

**Parameters**

`struct ib_device *device`
:   Device to query

`u32 port_num`
:   Port number to query

`struct ib_port_attr *port_attr`
:   Port attributes

**Description**

[`ib_query_port()`](infiniband.md#c.ib_query_port "ib_query_port") returns the attributes of a port through the
**port_attr** pointer.

int ib_device_set_netdev(struct ib_device \*ib_dev, struct [net_device](../networking/kapi.md#c.net_device "net_device") \*ndev, u32 port)
:   Associate the ib_dev with an underlying net_device

**Parameters**

`struct ib_device *ib_dev`
:   Device to modify

`struct net_device *ndev`
:   net_device to affiliate, may be NULL

`u32 port`
:   IB port the net_device is connected to

**Description**

Drivers should use this to link the ib_device to a netdev so the netdev
shows up in interfaces like ib_enum_roce_netdev. Only one netdev may be
affiliated with any port.

The caller must ensure that the given ndev is not unregistered or
unregistering, and that either the ib_device is unregistered or
[`ib_device_set_netdev()`](infiniband.md#c.ib_device_set_netdev "ib_device_set_netdev") is called with NULL when the ndev sends a
NETDEV_UNREGISTER event.

struct ib_device \*ib_device_get_by_netdev(struct [net_device](../networking/kapi.md#c.net_device "net_device") \*ndev, enum rdma_driver_id driver_id)
:   Find an IB device associated with a netdev

**Parameters**

`struct net_device *ndev`
:   netdev to locate

`enum rdma_driver_id driver_id`
:   The driver ID that must match (RDMA_DRIVER_UNKNOWN matches all)

**Description**

Find and hold an ib_device that is associated with a netdev via
[`ib_device_set_netdev()`](infiniband.md#c.ib_device_set_netdev "ib_device_set_netdev"). The caller must call [`ib_device_put()`](infiniband.md#c.ib_device_put "ib_device_put") on the
returned pointer.

int ib_query_pkey(struct ib_device \*device, u32 port_num, u16 index, u16 \*pkey)
:   Get P_Key table entry

**Parameters**

`struct ib_device *device`
:   Device to query

`u32 port_num`
:   Port number to query

`u16 index`
:   P_Key table index to query

`u16 *pkey`
:   Returned P_Key

**Description**

[`ib_query_pkey()`](infiniband.md#c.ib_query_pkey "ib_query_pkey") fetches the specified P_Key table entry.

int ib_modify_device(struct ib_device \*device, int device_modify_mask, struct ib_device_modify \*device_modify)
:   Change IB device attributes

**Parameters**

`struct ib_device *device`
:   Device to modify

`int device_modify_mask`
:   Mask of attributes to change

`struct ib_device_modify *device_modify`
:   New attribute values

**Description**

[`ib_modify_device()`](infiniband.md#c.ib_modify_device "ib_modify_device") changes a device's attributes as specified by
the **device_modify_mask** and **device_modify** structure.

int ib_modify_port(struct ib_device \*device, u32 port_num, int port_modify_mask, struct ib_port_modify \*port_modify)
:   Modifies the attributes for the specified port.

**Parameters**

`struct ib_device *device`
:   The device to modify.

`u32 port_num`
:   The number of the port to modify.

`int port_modify_mask`
:   Mask used to specify which attributes of the port
    to change.

`struct ib_port_modify *port_modify`
:   New attribute values for the port.

**Description**

[`ib_modify_port()`](infiniband.md#c.ib_modify_port "ib_modify_port") changes a port's attributes as specified by the
**port_modify_mask** and **port_modify** structure.

int ib_find_gid(struct ib_device \*device, union ib_gid \*gid, u32 \*port_num, u16 \*index)
:   Returns the port number and GID table index where a specified GID value occurs. Its searches only for IB link layer.

**Parameters**

`struct ib_device *device`
:   The device to query.

`union ib_gid *gid`
:   The GID value to search for.

`u32 *port_num`
:   The port number of the device where the GID value was found.

`u16 *index`
:   The index into the GID table where the GID was found. This
    parameter may be NULL.

int ib_find_pkey(struct ib_device \*device, u32 port_num, u16 pkey, u16 \*index)
:   Returns the PKey table index where a specified PKey value occurs.

**Parameters**

`struct ib_device *device`
:   The device to query.

`u32 port_num`
:   The port number of the device to search for the PKey.

`u16 pkey`
:   The PKey value to search for.

`u16 *index`
:   The index into the PKey table where the PKey was found.

struct [net_device](../networking/kapi.md#c.net_device "net_device") \*ib_get_net_dev_by_params(struct ib_device \*dev, u32 port, u16 pkey, const union ib_gid \*gid, const struct sockaddr \*addr)
:   Return the appropriate net_dev for a received CM request

**Parameters**

`struct ib_device *dev`
:   An RDMA device on which the request has been received.

`u32 port`
:   Port number on the RDMA device.

`u16 pkey`
:   The Pkey the request came on.

`const union ib_gid *gid`
:   A GID that the net_dev uses to communicate.

`const struct sockaddr *addr`
:   Contains the IP address that the request specified as its
    destination.

struct ib_pd \*__ib_alloc_pd(struct ib_device \*device, unsigned int flags, const char \*caller)
:   Allocates an unused protection domain.

**Parameters**

`struct ib_device *device`
:   The device on which to allocate the protection domain.

`unsigned int flags`
:   protection domain flags

`const char *caller`
:   caller's build-time module name

**Description**

A protection domain object provides an association between QPs, shared
receive queues, address handles, memory regions, and memory windows.

Every PD has a local_dma_lkey which can be used as the lkey value for local
memory operations.

int ib_dealloc_pd_user(struct ib_pd \*pd, struct ib_udata \*udata)
:   Deallocates a protection domain.

**Parameters**

`struct ib_pd *pd`
:   The protection domain to deallocate.

`struct ib_udata *udata`
:   Valid user data or NULL for kernel object

**Description**

It is an error to call this function while any resources in the pd still
exist. The caller is responsible to synchronously destroy them and
guarantee no new allocations will happen.

void rdma_copy_ah_attr(struct rdma_ah_attr \*dest, const struct rdma_ah_attr \*src)
:   Copy rdma ah attribute from source to destination.

**Parameters**

`struct rdma_ah_attr *dest`
:   Pointer to destination ah_attr. Contents of the destination
    pointer is assumed to be invalid and attribute are overwritten.

`const struct rdma_ah_attr *src`
:   Pointer to source ah_attr.

void rdma_replace_ah_attr(struct rdma_ah_attr \*old, const struct rdma_ah_attr \*new)
:   Replace valid ah_attr with new one.

**Parameters**

`struct rdma_ah_attr *old`
:   Pointer to existing ah_attr which needs to be replaced.
    old is assumed to be valid or zero'd

`const struct rdma_ah_attr *new`
:   Pointer to the new ah_attr.

**Description**

[`rdma_replace_ah_attr()`](infiniband.md#c.rdma_replace_ah_attr "rdma_replace_ah_attr") first releases any reference in the old ah_attr if
old the ah_attr is valid; after that it copies the new attribute and holds
the reference to the replaced ah_attr.

void rdma_move_ah_attr(struct rdma_ah_attr \*dest, struct rdma_ah_attr \*src)
:   Move ah_attr pointed by source to destination.

**Parameters**

`struct rdma_ah_attr *dest`
:   Pointer to destination ah_attr to copy to.
    dest is assumed to be valid or zero'd

`struct rdma_ah_attr *src`
:   Pointer to the new ah_attr.

**Description**

[`rdma_move_ah_attr()`](infiniband.md#c.rdma_move_ah_attr "rdma_move_ah_attr") first releases any reference in the destination ah_attr
if it is valid. This also transfers ownership of internal references from
src to dest, making src invalid in the process. No new reference of the src
ah_attr is taken.

struct ib_ah \*rdma_create_ah(struct ib_pd \*pd, struct rdma_ah_attr \*ah_attr, u32 flags)
:   Creates an address handle for the given address vector.

**Parameters**

`struct ib_pd *pd`
:   The protection domain associated with the address handle.

`struct rdma_ah_attr *ah_attr`
:   The attributes of the address vector.

`u32 flags`
:   Create address handle flags (see enum rdma_create_ah_flags).

**Description**

It returns 0 on success and returns appropriate error code on error.
The address handle is used to reference a local or global destination
in all UD QP post sends.

struct ib_ah \*rdma_create_user_ah(struct ib_pd \*pd, struct rdma_ah_attr \*ah_attr, struct ib_udata \*udata)
:   Creates an address handle for the given address vector. It resolves destination mac address for ah attribute of RoCE type.

**Parameters**

`struct ib_pd *pd`
:   The protection domain associated with the address handle.

`struct rdma_ah_attr *ah_attr`
:   The attributes of the address vector.

`struct ib_udata *udata`
:   pointer to user's input output buffer information need by
    provider driver.

**Description**

It returns 0 on success and returns appropriate error code on error.
The address handle is used to reference a local or global destination
in all UD QP post sends.

void rdma_move_grh_sgid_attr(struct rdma_ah_attr \*attr, union ib_gid \*dgid, u32 flow_label, u8 hop_limit, u8 traffic_class, const struct ib_gid_attr \*sgid_attr)
:   Sets the sgid attribute of GRH, taking ownership of the reference

**Parameters**

`struct rdma_ah_attr *attr`
:   Pointer to AH attribute structure

`union ib_gid *dgid`
:   Destination GID

`u32 flow_label`
:   Flow label

`u8 hop_limit`
:   Hop limit

`u8 traffic_class`
:   traffic class

`const struct ib_gid_attr *sgid_attr`
:   Pointer to SGID attribute

**Description**

This takes ownership of the sgid_attr reference. The caller must ensure
[`rdma_destroy_ah_attr()`](infiniband.md#c.rdma_destroy_ah_attr "rdma_destroy_ah_attr") is called before destroying the rdma_ah_attr after
calling this function.

void rdma_destroy_ah_attr(struct rdma_ah_attr \*ah_attr)
:   Release reference to SGID attribute of ah attribute.

**Parameters**

`struct rdma_ah_attr *ah_attr`
:   Pointer to ah attribute

**Description**

Release reference to the SGID attribute of the ah attribute if it is
non NULL. It is safe to call this multiple times, and safe to call it on
a zero initialized ah_attr.

struct ib_srq \*ib_create_srq_user(struct ib_pd \*pd, struct ib_srq_init_attr \*srq_init_attr, struct ib_usrq_object \*uobject, struct ib_udata \*udata)
:   Creates a SRQ associated with the specified protection domain.

**Parameters**

`struct ib_pd *pd`
:   The protection domain associated with the SRQ.

`struct ib_srq_init_attr *srq_init_attr`
:   A list of initial attributes required to create the
    SRQ. If SRQ creation succeeds, then the attributes are updated to
    the actual capabilities of the created SRQ.

`struct ib_usrq_object *uobject`
:   uobject pointer if this is not a kernel SRQ

`struct ib_udata *udata`
:   udata pointer if this is not a kernel SRQ

**Description**

srq_attr->max_wr and srq_attr->max_sge are read the determine the
requested size of the SRQ, and set to the actual values allocated
on return. If ib_create_srq() succeeds, then max_wr and max_sge
will always be at least as large as the requested values.

struct ib_qp \*ib_create_qp_user(struct ib_device \*dev, struct ib_pd \*pd, struct ib_qp_init_attr \*attr, struct ib_udata \*udata, struct ib_uqp_object \*uobj, const char \*caller)
:   Creates a QP associated with the specified protection domain.

**Parameters**

`struct ib_device *dev`
:   IB device

`struct ib_pd *pd`
:   The protection domain associated with the QP.

`struct ib_qp_init_attr *attr`
:   A list of initial attributes required to create the
    QP. If QP creation succeeds, then the attributes are updated to
    the actual capabilities of the created QP.

`struct ib_udata *udata`
:   User data

`struct ib_uqp_object *uobj`
:   uverbs obect

`const char *caller`
:   caller's build-time module name

int ib_modify_qp_with_udata(struct [ib_qp](infiniband.md#c.ib_modify_qp_with_udata "ib_qp") \*ib_qp, struct ib_qp_attr \*attr, int attr_mask, struct ib_udata \*udata)
:   Modifies the attributes for the specified QP.

**Parameters**

`struct ib_qp *ib_qp`
:   The QP to modify.

`struct ib_qp_attr *attr`
:   On input, specifies the QP attributes to modify. On output,
    the current values of selected QP attributes are returned.

`int attr_mask`
:   A bit-mask used to specify which attributes of the QP
    are being modified.

`struct ib_udata *udata`
:   pointer to user's input output buffer information
    are being modified.
    It returns 0 on success and returns appropriate error code on error.

struct ib_mr \*ib_alloc_mr(struct ib_pd \*pd, enum ib_mr_type mr_type, u32 max_num_sg)
:   Allocates a memory region

**Parameters**

`struct ib_pd *pd`
:   protection domain associated with the region

`enum ib_mr_type mr_type`
:   memory region type

`u32 max_num_sg`
:   maximum sg entries available for registration.

**Notes**

Memory registeration page/sg lists must not exceed max_num_sg.
For mr_type IB_MR_TYPE_MEM_REG, the total length cannot exceed
max_num_sg \* used_page_size.

struct ib_mr \*ib_alloc_mr_integrity(struct ib_pd \*pd, u32 max_num_data_sg, u32 max_num_meta_sg)
:   Allocates an integrity memory region

**Parameters**

`struct ib_pd *pd`
:   protection domain associated with the region

`u32 max_num_data_sg`
:   maximum data sg entries available for registration

`u32 max_num_meta_sg`
:   maximum metadata sg entries available for
    registration

**Notes**

Memory registration page/sg lists must not exceed max_num_sg,
also the integrity page/sg lists must not exceed max_num_meta_sg.

struct ib_xrcd \*ib_alloc_xrcd_user(struct ib_device \*device, struct [inode](infiniband.md#c.ib_alloc_xrcd_user "inode") \*inode, struct ib_udata \*udata)
:   Allocates an XRC domain.

**Parameters**

`struct ib_device *device`
:   The device on which to allocate the XRC domain.

`struct inode *inode`
:   inode to connect XRCD

`struct ib_udata *udata`
:   Valid user data or NULL for kernel object

int ib_dealloc_xrcd_user(struct ib_xrcd \*xrcd, struct ib_udata \*udata)
:   Deallocates an XRC domain.

**Parameters**

`struct ib_xrcd *xrcd`
:   The XRC domain to deallocate.

`struct ib_udata *udata`
:   Valid user data or NULL for kernel object

struct ib_wq \*ib_create_wq(struct ib_pd \*pd, struct ib_wq_init_attr \*wq_attr)
:   Creates a WQ associated with the specified protection domain.

**Parameters**

`struct ib_pd *pd`
:   The protection domain associated with the WQ.

`struct ib_wq_init_attr *wq_attr`
:   A list of initial attributes required to create the
    WQ. If WQ creation succeeds, then the attributes are updated to
    the actual capabilities of the created WQ.

**Description**

wq_attr->max_wr and wq_attr->max_sge determine
the requested size of the WQ, and set to the actual values allocated
on return.
If [`ib_create_wq()`](infiniband.md#c.ib_create_wq "ib_create_wq") succeeds, then max_wr and max_sge will always be
at least as large as the requested values.

int ib_destroy_wq_user(struct ib_wq \*wq, struct ib_udata \*udata)
:   Destroys the specified user WQ.

**Parameters**

`struct ib_wq *wq`
:   The WQ to destroy.

`struct ib_udata *udata`
:   Valid user data

int ib_map_mr_sg_pi(struct ib_mr \*mr, struct scatterlist \*data_sg, int data_sg_nents, unsigned int \*data_sg_offset, struct scatterlist \*meta_sg, int meta_sg_nents, unsigned int \*meta_sg_offset, unsigned int page_size)
:   Map the dma mapped SG lists for PI (protection information) and set an appropriate memory region for registration.

**Parameters**

`struct ib_mr *mr`
:   memory region

`struct scatterlist *data_sg`
:   dma mapped scatterlist for data

`int data_sg_nents`
:   number of entries in data_sg

`unsigned int *data_sg_offset`
:   offset in bytes into data_sg

`struct scatterlist *meta_sg`
:   dma mapped scatterlist for metadata

`int meta_sg_nents`
:   number of entries in meta_sg

`unsigned int *meta_sg_offset`
:   offset in bytes into meta_sg

`unsigned int page_size`
:   page vector desired page size

**Description**

Constraints:
- The MR must be allocated with type IB_MR_TYPE_INTEGRITY.

After this completes successfully, the memory region
is ready for registration.

**Return**

0 on success.

int ib_map_mr_sg(struct ib_mr \*mr, struct scatterlist \*sg, int sg_nents, unsigned int \*sg_offset, unsigned int page_size)
:   Map the largest prefix of a dma mapped SG list and set it the memory region.

**Parameters**

`struct ib_mr *mr`
:   memory region

`struct scatterlist *sg`
:   dma mapped scatterlist

`int sg_nents`
:   number of entries in sg

`unsigned int *sg_offset`
:   offset in bytes into sg

`unsigned int page_size`
:   page vector desired page size

**Description**

Constraints:

- The first sg element is allowed to have an offset.
- Each sg element must either be aligned to page_size or virtually
  contiguous to the previous element. In case an sg element has a
  non-contiguous offset, the mapping prefix will not include it.
- The last sg element is allowed to have length less than page_size.
- If sg_nents total byte length exceeds the mr max_num_sge \* page_size
  then only max_num_sg entries will be mapped.
- If the MR was allocated with type IB_MR_TYPE_SG_GAPS, none of these
  constraints holds and the page_size argument is ignored.

Returns the number of sg elements that were mapped to the memory region.

After this completes successfully, the memory region
is ready for registration.

int ib_sg_to_pages(struct ib_mr \*mr, struct scatterlist \*sgl, int sg_nents, unsigned int \*sg_offset_p, int (\*set_page)(struct ib_mr\*, u64))
:   Convert the largest prefix of a sg list to a page vector

**Parameters**

`struct ib_mr *mr`
:   memory region

`struct scatterlist *sgl`
:   dma mapped scatterlist

`int sg_nents`
:   number of entries in sg

`unsigned int *sg_offset_p`
:   |  |  |
    | --- | --- |
    | IN | start offset in bytes into sg |
    | OUT | offset in bytes for element n of the sg of the first byte that has not been processed where n is the return value of this function. |

`int (*set_page)(struct ib_mr *, u64)`
:   driver page assignment function pointer

**Description**

Core service helper for drivers to convert the largest
prefix of given sg list to a page vector. The sg list
prefix converted is the prefix that meet the requirements
of ib_map_mr_sg.

Returns the number of sg elements that were assigned to
a page vector.

void ib_drain_sq(struct ib_qp \*qp)
:   Block until all SQ CQEs have been consumed by the application.

**Parameters**

`struct ib_qp *qp`
:   queue pair to drain

**Description**

If the device has a provider-specific drain function, then
call that. Otherwise call the generic drain function
__ib_drain_sq().

The caller must:

ensure there is room in the CQ and SQ for the drain work request and
completion.

allocate the CQ using ib_alloc_cq().

ensure that there are no other contexts that are posting WRs concurrently.
Otherwise the drain is not guaranteed.

void ib_drain_rq(struct ib_qp \*qp)
:   Block until all RQ CQEs have been consumed by the application.

**Parameters**

`struct ib_qp *qp`
:   queue pair to drain

**Description**

If the device has a provider-specific drain function, then
call that. Otherwise call the generic drain function
__ib_drain_rq().

The caller must:

ensure there is room in the CQ and RQ for the drain work request and
completion.

allocate the CQ using ib_alloc_cq().

ensure that there are no other contexts that are posting WRs concurrently.
Otherwise the drain is not guaranteed.

void ib_drain_qp(struct ib_qp \*qp)
:   Block until all CQEs have been consumed by the application on both the RQ and SQ.

**Parameters**

`struct ib_qp *qp`
:   queue pair to drain

**Description**

The caller must:

ensure there is room in the CQ(s), SQ, and RQ for drain work requests
and completions.

allocate the CQs using ib_alloc_cq().

ensure that there are no other contexts that are posting WRs concurrently.
Otherwise the drain is not guaranteed.

struct rdma_hw_stats \*rdma_alloc_hw_stats_struct(const struct rdma_stat_desc \*descs, int num_counters, unsigned long lifespan)
:   Helper function to allocate dynamic struct for the drivers.

**Parameters**

`const struct rdma_stat_desc *descs`
:   array of static descriptors

`int num_counters`
:   number of elements in array

`unsigned long lifespan`
:   milliseconds between updates

void rdma_free_hw_stats_struct(struct rdma_hw_stats \*stats)
:   Helper function to release rdma_hw_stats

**Parameters**

`struct rdma_hw_stats *stats`
:   statistics to release

void ib_pack(const struct ib_field \*desc, int desc_len, void \*structure, void \*buf)
:   Pack a structure into a buffer

**Parameters**

`const struct ib_field *desc`
:   Array of structure field descriptions

`int desc_len`
:   Number of entries in **desc**

`void *structure`
:   Structure to pack from

`void *buf`
:   Buffer to pack into

**Description**

[`ib_pack()`](infiniband.md#c.ib_pack "ib_pack") packs a list of structure fields into a buffer,
controlled by the array of fields in **desc**.

void ib_unpack(const struct ib_field \*desc, int desc_len, void \*buf, void \*structure)
:   Unpack a buffer into a structure

**Parameters**

`const struct ib_field *desc`
:   Array of structure field descriptions

`int desc_len`
:   Number of entries in **desc**

`void *buf`
:   Buffer to unpack from

`void *structure`
:   Structure to unpack into

**Description**

[`ib_pack()`](infiniband.md#c.ib_pack "ib_pack") unpacks a list of structure fields from a buffer,
controlled by the array of fields in **desc**.

void ib_sa_cancel_query(int id, struct ib_sa_query \*query)
:   try to cancel an SA query

**Parameters**

`int id`
:   ID of query to cancel

`struct ib_sa_query *query`
:   query pointer to cancel

**Description**

Try to cancel an SA query. If the id and query don't match up or
the query has already completed, nothing is done. Otherwise the
query is canceled and will complete with a status of -EINTR.

int ib_init_ah_attr_from_path(struct ib_device \*device, u32 port_num, struct sa_path_rec \*rec, struct rdma_ah_attr \*ah_attr, const struct ib_gid_attr \*gid_attr)
:   Initialize address handle attributes based on an SA path record.

**Parameters**

`struct ib_device *device`
:   Device associated ah attributes initialization.

`u32 port_num`
:   Port on the specified device.

`struct sa_path_rec *rec`
:   path record entry to use for ah attributes initialization.

`struct rdma_ah_attr *ah_attr`
:   address handle attributes to initialization from path record.

`const struct ib_gid_attr *gid_attr`
:   SGID attribute to consider during initialization.

**Description**

When [`ib_init_ah_attr_from_path()`](infiniband.md#c.ib_init_ah_attr_from_path "ib_init_ah_attr_from_path") returns success,
(a) for IB link layer it optionally contains a reference to SGID attribute
when GRH is present for IB link layer.
(b) for RoCE link layer it contains a reference to SGID attribute.
User must invoke [`rdma_destroy_ah_attr()`](infiniband.md#c.rdma_destroy_ah_attr "rdma_destroy_ah_attr") to release reference to SGID
attributes which are initialized using [`ib_init_ah_attr_from_path()`](infiniband.md#c.ib_init_ah_attr_from_path "ib_init_ah_attr_from_path").

int ib_sa_path_rec_get(struct ib_sa_client \*client, struct ib_device \*device, u32 port_num, struct sa_path_rec \*rec, ib_sa_comp_mask comp_mask, unsigned long timeout_ms, gfp_t gfp_mask, void (\*callback)(int status, struct sa_path_rec \*resp, unsigned int num_paths, void \*context), void \*context, struct ib_sa_query \*\*sa_query)
:   Start a Path get query

**Parameters**

`struct ib_sa_client *client`
:   SA client

`struct ib_device *device`
:   device to send query on

`u32 port_num`
:   port number to send query on

`struct sa_path_rec *rec`
:   Path Record to send in query

`ib_sa_comp_mask comp_mask`
:   component mask to send in query

`unsigned long timeout_ms`
:   time to wait for response

`gfp_t gfp_mask`
:   GFP mask to use for internal allocations

`void (*callback)(int status, struct sa_path_rec *resp, unsigned int num_paths, void *context)`
:   function called when query completes, times out or is
    canceled

`void *context`
:   opaque user context passed to callback

`struct ib_sa_query **sa_query`
:   query context, used to cancel query

**Description**

Send a Path Record Get query to the SA to look up a path. The
callback function will be called when the query completes (or
fails); status is 0 for a successful response, -EINTR if the query
is canceled, -ETIMEDOUT is the query timed out, or -EIO if an error
occurred sending the query. The resp parameter of the callback is
only valid if status is 0.

If the return value of [`ib_sa_path_rec_get()`](infiniband.md#c.ib_sa_path_rec_get "ib_sa_path_rec_get") is negative, it is an
error code. Otherwise it is a query ID that can be used to cancel
the query.

int ib_ud_header_init(int payload_bytes, int lrh_present, int eth_present, int vlan_present, int grh_present, int ip_version, int udp_present, int immediate_present, struct ib_ud_header \*header)
:   Initialize UD header structure

**Parameters**

`int payload_bytes`
:   Length of packet payload

`int lrh_present`
:   specify if LRH is present

`int eth_present`
:   specify if Eth header is present

`int vlan_present`
:   packet is tagged vlan

`int grh_present`
:   GRH flag (if non-zero, GRH will be included)

`int ip_version`
:   if non-zero, IP header, V4 or V6, will be included

`int udp_present`
:   if non-zero, UDP header will be included

`int immediate_present`
:   specify if immediate data is present

`struct ib_ud_header *header`
:   Structure to initialize

int ib_ud_header_pack(struct ib_ud_header \*header, void \*buf)
:   Pack UD header struct into wire format

**Parameters**

`struct ib_ud_header *header`
:   UD header struct

`void *buf`
:   Buffer to pack into

**Description**

[`ib_ud_header_pack()`](infiniband.md#c.ib_ud_header_pack "ib_ud_header_pack") packs the UD header structure **header** into wire
format in the buffer **buf**.

int ib_ud_header_unpack(void \*buf, struct ib_ud_header \*header)
:   Unpack UD header struct from wire format

**Parameters**

`void *buf`
:   Buffer to pack into

`struct ib_ud_header *header`
:   UD header struct

**Description**

[`ib_ud_header_pack()`](infiniband.md#c.ib_ud_header_pack "ib_ud_header_pack") unpacks the UD header structure **header** from wire
format in the buffer **buf**.

unsigned long ib_umem_find_best_pgsz(struct ib_umem \*umem, unsigned long pgsz_bitmap, unsigned long virt)
:   Find best HW page size to use for this MR

**Parameters**

`struct ib_umem *umem`
:   umem struct

`unsigned long pgsz_bitmap`
:   bitmap of HW supported page sizes

`unsigned long virt`
:   IOVA

**Description**

This helper is intended for HW that support multiple page
sizes but can do only a single page size in an MR.

Returns 0 if the umem requires page sizes not supported by
the driver to be mapped. Drivers always supporting PAGE_SIZE
or smaller will never see a 0 result.

struct ib_umem \*ib_umem_get(struct ib_device \*device, unsigned long addr, size_t size, int access)
:   Pin and DMA map userspace memory.

**Parameters**

`struct ib_device *device`
:   IB device to connect UMEM

`unsigned long addr`
:   userspace virtual address to start at

`size_t size`
:   length of region to pin

`int access`
:   IB_ACCESS_xxx flags for memory being pinned

void ib_umem_release(struct ib_umem \*umem)
:   release memory pinned with ib_umem_get

**Parameters**

`struct ib_umem *umem`
:   umem struct to release

struct ib_umem_odp \*ib_umem_odp_alloc_implicit(struct ib_device \*device, int access)
:   Allocate a parent implicit ODP umem

**Parameters**

`struct ib_device *device`
:   IB device to create UMEM

`int access`
:   ib_reg_mr access flags

**Description**

Implicit ODP umems do not have a VA range and do not have any page lists.
They exist only to hold the per_mm reference to help the driver create
children umems.

struct ib_umem_odp \*ib_umem_odp_alloc_child(struct ib_umem_odp \*root, unsigned long addr, size_t size, const struct mmu_interval_notifier_ops \*ops)
:   Allocate a child ODP umem under an implicit parent ODP umem

**Parameters**

`struct ib_umem_odp *root`
:   The parent umem enclosing the child. This must be allocated using
    ib_alloc_implicit_odp_umem()

`unsigned long addr`
:   The starting userspace VA

`size_t size`
:   The length of the userspace VA

`const struct mmu_interval_notifier_ops *ops`
:   MMU interval ops, currently only **invalidate**

struct ib_umem_odp \*ib_umem_odp_get(struct ib_device \*device, unsigned long addr, size_t size, int access, const struct mmu_interval_notifier_ops \*ops)
:   Create a umem_odp for a userspace va

**Parameters**

`struct ib_device *device`
:   IB device struct to get UMEM

`unsigned long addr`
:   userspace virtual address to start at

`size_t size`
:   length of region to pin

`int access`
:   IB_ACCESS_xxx flags for memory being pinned

`const struct mmu_interval_notifier_ops *ops`
:   MMU interval ops, currently only **invalidate**

**Description**

The driver should use when the access flags indicate ODP memory. It avoids
pinning, instead, stores the mm for future page fault handling in
conjunction with MMU notifiers.

int ib_umem_odp_map_dma_and_lock(struct ib_umem_odp \*umem_odp, u64 user_virt, u64 bcnt, u64 access_mask, bool fault)
:   DMA map userspace memory in an ODP MR and lock it.

**Parameters**

`struct ib_umem_odp *umem_odp`
:   the umem to map and pin

`u64 user_virt`
:   the address from which we need to map.

`u64 bcnt`
:   the minimal number of bytes to pin and map. The mapping might be
    bigger due to alignment, and may also be smaller in case of an error
    pinning or mapping a page. The actual pages mapped is returned in
    the return value.

`u64 access_mask`
:   bit mask of the requested access permissions for the given
    range.

`bool fault`
:   is faulting required for the given range

**Description**

Maps the range passed in the argument to DMA addresses.
The DMA addresses of the mapped pages is updated in umem_odp->dma_list.
Upon success the ODP MR will be locked to let caller complete its device
page table update.

Returns the number of pages mapped in success, negative error code
for failure.

## RDMA Verbs transport library

int rvt_fast_reg_mr(struct rvt_qp \*qp, struct ib_mr \*ibmr, u32 key, int access)
:   fast register physical MR

**Parameters**

`struct rvt_qp *qp`
:   the queue pair where the work request comes from

`struct ib_mr *ibmr`
:   the memory region to be registered

`u32 key`
:   updated key for this memory region

`int access`
:   access flags for this memory region

**Description**

Returns 0 on success.

int rvt_invalidate_rkey(struct rvt_qp \*qp, u32 rkey)
:   invalidate an MR rkey

**Parameters**

`struct rvt_qp *qp`
:   queue pair associated with the invalidate op

`u32 rkey`
:   rkey to invalidate

**Description**

Returns 0 on success.

int rvt_lkey_ok(struct rvt_lkey_table \*rkt, struct rvt_pd \*pd, struct rvt_sge \*isge, struct rvt_sge \*last_sge, struct ib_sge \*sge, int acc)
:   check IB SGE for validity and initialize

**Parameters**

`struct rvt_lkey_table *rkt`
:   table containing lkey to check SGE against

`struct rvt_pd *pd`
:   protection domain

`struct rvt_sge *isge`
:   outgoing internal SGE

`struct rvt_sge *last_sge`
:   last outgoing SGE written

`struct ib_sge *sge`
:   SGE to check

`int acc`
:   access flags

**Description**

Check the IB SGE for validity and initialize our internal version
of it.

Increments the reference count when a new sge is stored.

**Return**

0 if compressed, 1 if added , otherwise returns -errno.

int rvt_rkey_ok(struct rvt_qp \*qp, struct rvt_sge \*sge, u32 len, u64 vaddr, u32 rkey, int acc)
:   check the IB virtual address, length, and RKEY

**Parameters**

`struct rvt_qp *qp`
:   qp for validation

`struct rvt_sge *sge`
:   SGE state

`u32 len`
:   length of data

`u64 vaddr`
:   virtual address to place data

`u32 rkey`
:   rkey to check

`int acc`
:   access flags

**Return**

1 if successful, otherwise 0.

**Description**

increments the reference count upon success

__be32 rvt_compute_aeth(struct rvt_qp \*qp)
:   compute the AETH (syndrome + MSN)

**Parameters**

`struct rvt_qp *qp`
:   the queue pair to compute the AETH for

**Description**

Returns the AETH.

void rvt_get_credit(struct rvt_qp \*qp, u32 aeth)
:   flush the send work queue of a QP

**Parameters**

`struct rvt_qp *qp`
:   the qp who's send work queue to flush

`u32 aeth`
:   the Acknowledge Extended Transport Header

**Description**

The QP s_lock should be held.

u32 rvt_restart_sge(struct rvt_sge_state \*ss, struct rvt_swqe \*wqe, u32 len)
:   rewind the sge state for a wqe

**Parameters**

`struct rvt_sge_state *ss`
:   the sge state pointer

`struct rvt_swqe *wqe`
:   the wqe to rewind

`u32 len`
:   the data length from the start of the wqe in bytes

**Description**

Returns the remaining data length.

int rvt_check_ah(struct ib_device \*ibdev, struct rdma_ah_attr \*ah_attr)
:   validate the attributes of AH

**Parameters**

`struct ib_device *ibdev`
:   the ib device

`struct rdma_ah_attr *ah_attr`
:   the attributes of the AH

**Description**

If driver supports a more detailed check_ah function call back to it
otherwise just check the basics.

**Return**

0 on success

struct rvt_dev_info \*rvt_alloc_device(size_t size, int nports)
:   allocate rdi

**Parameters**

`size_t size`
:   how big of a structure to allocate

`int nports`
:   number of ports to allocate array slots for

**Description**

Use IB core device alloc to allocate space for the rdi which is assumed to be
inside of the ib_device. Any extra space that drivers require should be
included in size.

We also allocate a port array based on the number of ports.

**Return**

pointer to allocated rdi

void rvt_dealloc_device(struct rvt_dev_info \*rdi)
:   deallocate rdi

**Parameters**

`struct rvt_dev_info *rdi`
:   structure to free

**Description**

Free a structure allocated with [`rvt_alloc_device()`](infiniband.md#c.rvt_alloc_device "rvt_alloc_device")

int rvt_register_device(struct rvt_dev_info \*rdi)
:   register a driver

**Parameters**

`struct rvt_dev_info *rdi`
:   main dev structure for all of rdmavt operations

**Description**

It is up to drivers to allocate the rdi and fill in the appropriate
information.

**Return**

0 on success otherwise an errno.

void rvt_unregister_device(struct rvt_dev_info \*rdi)
:   remove a driver

**Parameters**

`struct rvt_dev_info *rdi`
:   rvt dev struct

int rvt_init_port(struct rvt_dev_info \*rdi, struct rvt_ibport \*port, int port_index, u16 \*pkey_table)
:   init internal data for driver port

**Parameters**

`struct rvt_dev_info *rdi`
:   rvt_dev_info struct

`struct rvt_ibport *port`
:   rvt port

`int port_index`
:   0 based index of ports, different from IB core port num

`u16 *pkey_table`
:   pkey_table for **port**

**Description**

Keep track of a list of ports. No need to have a detach port.
They persist until the driver goes away.

**Return**

always 0

bool rvt_cq_enter(struct rvt_cq \*cq, struct ib_wc \*entry, bool solicited)
:   add a new entry to the completion queue

**Parameters**

`struct rvt_cq *cq`
:   completion queue

`struct ib_wc *entry`
:   work completion entry to add

`bool solicited`
:   true if **entry** is solicited

**Description**

This may be called with qp->s_lock held.

**Return**

return true on success, else return
false if cq is full.

int rvt_error_qp(struct rvt_qp \*qp, enum ib_wc_status err)
:   put a QP into the error state

**Parameters**

`struct rvt_qp *qp`
:   the QP to put into the error state

`enum ib_wc_status err`
:   the receive completion error to signal if a RWQE is active

**Description**

Flushes both send and receive work queues.

**Return**

true if last WQE event should be generated.
The QP r_lock and s_lock should be held and interrupts disabled.
If we are already in error state, just return.

int rvt_get_rwqe(struct rvt_qp \*qp, bool wr_id_only)
:   copy the next RWQE into the QP's RWQE

**Parameters**

`struct rvt_qp *qp`
:   the QP

`bool wr_id_only`
:   update qp->r_wr_id only, not qp->r_sge

**Description**

Return -1 if there is a local error, 0 if no RWQE is available,
otherwise return 1.

Can be called from interrupt level.

void rvt_comm_est(struct rvt_qp \*qp)
:   handle trap with QP established

**Parameters**

`struct rvt_qp *qp`
:   the QP

void rvt_add_rnr_timer(struct rvt_qp \*qp, u32 aeth)
:   add/start an rnr timer on the QP

**Parameters**

`struct rvt_qp *qp`
:   the QP

`u32 aeth`
:   aeth of RNR timeout, simulated aeth for loopback

void rvt_stop_rc_timers(struct rvt_qp \*qp)
:   stop all timers

**Parameters**

`struct rvt_qp *qp`
:   the QP
    stop any pending timers

void rvt_del_timers_sync(struct rvt_qp \*qp)
:   wait for any timeout routines to exit

**Parameters**

`struct rvt_qp *qp`
:   the QP

struct [rvt_qp_iter](infiniband.md#c.rvt_qp_iter "rvt_qp_iter") \*rvt_qp_iter_init(struct rvt_dev_info \*rdi, u64 v, void (\*cb)(struct rvt_qp \*qp, u64 v))
:   initial for QP iteration

**Parameters**

`struct rvt_dev_info *rdi`
:   rvt devinfo

`u64 v`
:   u64 value

`void (*cb)(struct rvt_qp *qp, u64 v)`
:   user-defined callback

**Description**

This returns an iterator suitable for iterating QPs
in the system.

The **cb** is a user-defined callback and **v** is a 64-bit
value passed to and relevant for processing in the
**cb**. An example use case would be to alter QP processing
based on criteria not part of the rvt_qp.

Use cases that require memory allocation to succeed
must preallocate appropriately.

**Return**

a pointer to an rvt_qp_iter or NULL

int rvt_qp_iter_next(struct [rvt_qp_iter](infiniband.md#c.rvt_qp_iter "rvt_qp_iter") \*iter)
:   return the next QP in iter

**Parameters**

`struct rvt_qp_iter *iter`
:   the iterator

**Description**

Fine grained QP iterator suitable for use
with debugfs seq_file mechanisms.

Updates iter->qp with the current QP when the return
value is 0.

**Return**

0 - iter->qp is valid 1 - no more QPs

void rvt_qp_iter(struct rvt_dev_info \*rdi, u64 v, void (\*cb)(struct rvt_qp \*qp, u64 v))
:   iterate all QPs

**Parameters**

`struct rvt_dev_info *rdi`
:   rvt devinfo

`u64 v`
:   a 64-bit value

`void (*cb)(struct rvt_qp *qp, u64 v)`
:   a callback

**Description**

This provides a way for iterating all QPs.

The **cb** is a user-defined callback and **v** is a 64-bit
value passed to and relevant for processing in the
cb. An example use case would be to alter QP processing
based on criteria not part of the rvt_qp.

The code has an internal iterator to simplify
non seq_file use cases.

void rvt_copy_sge(struct rvt_qp \*qp, struct rvt_sge_state \*ss, void \*data, u32 length, bool release, bool copy_last)
:   copy data to SGE memory

**Parameters**

`struct rvt_qp *qp`
:   associated QP

`struct rvt_sge_state *ss`
:   the SGE state

`void *data`
:   the data to copy

`u32 length`
:   the length of the data

`bool release`
:   boolean to release MR

`bool copy_last`
:   do a separate copy of the last 8 bytes

void rvt_ruc_loopback(struct rvt_qp \*sqp)
:   handle UC and RC loopback requests

**Parameters**

`struct rvt_qp *sqp`
:   the sending QP

**Description**

This is called from rvt_do_send() to forward a WQE addressed to the same HFI
Note that although we are single threaded due to the send engine, we still
have to protect against post_send(). We don't have to worry about
receive interrupts since this is a connected protocol and all packets
will pass through here.

struct rvt_mcast \*rvt_mcast_find(struct rvt_ibport \*ibp, union ib_gid \*mgid, u16 lid)
:   search the global table for the given multicast GID/LID

**Parameters**

`struct rvt_ibport *ibp`
:   the IB port structure

`union ib_gid *mgid`
:   the multicast GID to search for

`u16 lid`
:   the multicast LID portion of the multicast address (host order)

**NOTE**

It is valid to have 1 MLID with multiple MGIDs. It is not valid
to have 1 MGID with multiple MLIDs.

**Description**

The caller is responsible for decrementing the reference count if found.

**Return**

NULL if not found.

## Upper Layer Protocols

### iSCSI Extensions for RDMA (iSER)

struct iser_data_buf
:   iSER data buffer

**Definition**:

```
struct iser_data_buf {
    struct scatterlist *sg;
    int size;
    unsigned long      data_len;
    int dma_nents;
};
```

**Members**

`sg`
:   pointer to the sg list

`size`
:   num entries of this sg

`data_len`
:   total buffer byte len

`dma_nents`
:   returned by dma_map_sg

struct iser_mem_reg
:   iSER memory registration info

**Definition**:

```
struct iser_mem_reg {
    struct ib_sge sge;
    u32 rkey;
    struct iser_fr_desc *desc;
};
```

**Members**

`sge`
:   memory region sg element

`rkey`
:   memory region remote key

`desc`
:   pointer to fast registration context

struct iser_tx_desc
:   iSER TX descriptor

**Definition**:

```
struct iser_tx_desc {
    struct iser_ctrl             iser_header;
    struct iscsi_hdr             iscsi_header;
    enum iser_desc_type        type;
    u64 dma_addr;
    struct ib_sge                tx_sg[2];
    int num_sge;
    struct ib_cqe                cqe;
    bool mapped;
    struct ib_reg_wr             reg_wr;
    struct ib_send_wr            send_wr;
    struct ib_send_wr            inv_wr;
};
```

**Members**

`iser_header`
:   iser header

`iscsi_header`
:   iscsi header

`type`
:   command/control/dataout

`dma_addr`
:   header buffer dma_address

`tx_sg`
:   sg[0] points to iser/iscsi headers
    sg[1] optionally points to either of immediate data
    unsolicited data-out or control

`num_sge`
:   number sges used on this TX task

`cqe`
:   completion handler

`mapped`
:   Is the task header mapped

`reg_wr`
:   registration WR

`send_wr`
:   send WR

`inv_wr`
:   invalidate WR

struct iser_rx_desc
:   iSER RX descriptor

**Definition**:

```
struct iser_rx_desc {
    struct iser_ctrl             iser_header;
    struct iscsi_hdr             iscsi_header;
    char data[ISER_RECV_DATA_SEG_LEN];
    u64 dma_addr;
    struct ib_sge                rx_sg;
    struct ib_cqe                cqe;
    char pad[ISER_RX_PAD_SIZE];
};
```

**Members**

`iser_header`
:   iser header

`iscsi_header`
:   iscsi header

`data`
:   received data segment

`dma_addr`
:   receive buffer dma address

`rx_sg`
:   ib_sge of receive buffer

`cqe`
:   completion handler

`pad`
:   for sense data TODO: Modify to maximum sense length supported

struct iser_login_desc
:   iSER login descriptor

**Definition**:

```
struct iser_login_desc {
    void *req;
    void *rsp;
    u64 req_dma;
    u64 rsp_dma;
    struct ib_sge                sge;
    struct ib_cqe                cqe;
};
```

**Members**

`req`
:   pointer to login request buffer

`rsp`
:   pointer to login response buffer

`req_dma`
:   DMA address of login request buffer

`rsp_dma`
:   DMA address of login response buffer

`sge`
:   IB sge for login post recv

`cqe`
:   completion handler

struct iser_device
:   iSER device handle

**Definition**:

```
struct iser_device {
    struct ib_device             *ib_device;
    struct ib_pd                 *pd;
    struct ib_event_handler      event_handler;
    struct list_head             ig_list;
    int refcount;
};
```

**Members**

`ib_device`
:   RDMA device

`pd`
:   Protection Domain for this device

`event_handler`
:   IB events handle routine

`ig_list`
:   entry in devices list

`refcount`
:   Reference counter, dominated by open iser connections

struct iser_reg_resources
:   Fast registration resources

**Definition**:

```
struct iser_reg_resources {
    struct ib_mr                     *mr;
    struct ib_mr                     *sig_mr;
};
```

**Members**

`mr`
:   memory region

`sig_mr`
:   signature memory region

struct iser_fr_desc
:   Fast registration descriptor

**Definition**:

```
struct iser_fr_desc {
    struct list_head                  list;
    struct iser_reg_resources         rsc;
    bool sig_protected;
    struct list_head                  all_list;
};
```

**Members**

`list`
:   entry in connection fastreg pool

`rsc`
:   data buffer registration resources

`sig_protected`
:   is region protected indicator

`all_list`
:   first and last list members

struct iser_fr_pool
:   connection fast registration pool

**Definition**:

```
struct iser_fr_pool {
    struct list_head        list;
    spinlock_t lock;
    int size;
    struct list_head        all_list;
};
```

**Members**

`list`
:   list of fastreg descriptors

`lock`
:   protects fastreg pool

`size`
:   size of the pool

`all_list`
:   first and last list members

struct ib_conn
:   Infiniband related objects

**Definition**:

```
struct ib_conn {
    struct rdma_cm_id           *cma_id;
    struct ib_qp                *qp;
    struct ib_cq                *cq;
    u32 cq_size;
    struct iser_device          *device;
    struct iser_fr_pool          fr_pool;
    bool pi_support;
    struct ib_cqe                reg_cqe;
};
```

**Members**

`cma_id`
:   rdma_cm connection maneger handle

`qp`
:   Connection Queue-pair

`cq`
:   Connection completion queue

`cq_size`
:   The number of max outstanding completions

`device`
:   reference to iser device

`fr_pool`
:   connection fast registration pool

`pi_support`
:   Indicate device T10-PI support

`reg_cqe`
:   completion handler

struct iser_conn
:   iSER connection context

**Definition**:

```
struct iser_conn {
    struct ib_conn               ib_conn;
    struct iscsi_conn            *iscsi_conn;
    struct iscsi_endpoint        *ep;
    enum iser_conn_state         state;
    unsigned qp_max_recv_dtos;
    u16 max_cmds;
    char name[ISER_OBJECT_NAME_SIZE];
    struct work_struct           release_work;
    struct mutex                 state_mutex;
    struct completion            stop_completion;
    struct completion            ib_completion;
    struct completion            up_completion;
    struct list_head             conn_list;
    struct iser_login_desc       login_desc;
    struct iser_rx_desc          *rx_descs;
    u32 num_rx_descs;
    unsigned short               scsi_sg_tablesize;
    unsigned short               pages_per_mr;
    bool snd_w_inv;
};
```

**Members**

`ib_conn`
:   connection RDMA resources

`iscsi_conn`
:   link to matching iscsi connection

`ep`
:   transport handle

`state`
:   connection logical state

`qp_max_recv_dtos`
:   maximum number of data outs, corresponds
    to max number of post recvs

`max_cmds`
:   maximum cmds allowed for this connection

`name`
:   connection peer portal

`release_work`
:   deferred work for release job

`state_mutex`
:   protects iser onnection state

`stop_completion`
:   conn_stop completion

`ib_completion`
:   RDMA cleanup completion

`up_completion`
:   connection establishment completed
    (state is ISER_CONN_UP)

`conn_list`
:   entry in ig conn list

`login_desc`
:   login descriptor

`rx_descs`
:   rx buffers array (cyclic buffer)

`num_rx_descs`
:   number of rx descriptors

`scsi_sg_tablesize`
:   scsi host sg_tablesize

`pages_per_mr`
:   maximum pages available for registration

`snd_w_inv`
:   connection uses remote invalidation

struct iscsi_iser_task
:   iser task context

**Definition**:

```
struct iscsi_iser_task {
    struct iser_tx_desc          desc;
    struct iser_conn             *iser_conn;
    enum iser_task_status        status;
    struct scsi_cmnd             *sc;
    int command_sent;
    int dir[ISER_DIRS_NUM];
    struct iser_mem_reg          rdma_reg[ISER_DIRS_NUM];
    struct iser_data_buf         data[ISER_DIRS_NUM];
    struct iser_data_buf         prot[ISER_DIRS_NUM];
};
```

**Members**

`desc`
:   TX descriptor

`iser_conn`
:   link to iser connection

`status`
:   current task status

`sc`
:   link to scsi command

`command_sent`
:   indicate if command was sent

`dir`
:   iser data direction

`rdma_reg`
:   task rdma registration desc

`data`
:   iser data buffer desc

`prot`
:   iser protection buffer desc

struct iser_global
:   iSER global context

**Definition**:

```
struct iser_global {
    struct mutex      device_list_mutex;
    struct list_head  device_list;
    struct mutex      connlist_mutex;
    struct list_head  connlist;
    struct kmem_cache *desc_cache;
};
```

**Members**

`device_list_mutex`
:   protects device_list

`device_list`
:   iser devices global list

`connlist_mutex`
:   protects connlist

`connlist`
:   iser connections global list

`desc_cache`
:   kmem cache for tx dataout

int iscsi_iser_pdu_alloc(struct iscsi_task \*task, uint8_t opcode)
:   allocate an iscsi-iser PDU

**Parameters**

`struct iscsi_task *task`
:   iscsi task

`uint8_t opcode`
:   iscsi command opcode

**Description**

Netes: This routine can't fail, just assign iscsi task
:   hdr and max hdr size.

int iser_initialize_task_headers(struct iscsi_task \*task, struct [iser_tx_desc](infiniband.md#c.iser_tx_desc "iser_tx_desc") \*tx_desc)
:   Initialize task headers

**Parameters**

`struct iscsi_task *task`
:   iscsi task

`struct iser_tx_desc *tx_desc`
:   iser tx descriptor

**Notes**

This routine may race with iser teardown flow for scsi
error handling TMFs. So for TMF we should acquire the
state mutex to avoid dereferencing the IB device which
may have already been terminated.

int iscsi_iser_task_init(struct iscsi_task \*task)
:   Initialize iscsi-iser task

**Parameters**

`struct iscsi_task *task`
:   iscsi task

**Description**

Initialize the task for the scsi command or mgmt command.

**Return**

Returns zero on success or -ENOMEM when failing
:   to init task headers (dma mapping error).

int iscsi_iser_mtask_xmit(struct iscsi_conn \*conn, struct iscsi_task \*task)
:   xmit management (immediate) task

**Parameters**

`struct iscsi_conn *conn`
:   iscsi connection

`struct iscsi_task *task`
:   task management task

**Notes**

> The function can return -EAGAIN in which case caller must
> call it again later, or recover. '0' return code means successful
> xmit.

int iscsi_iser_task_xmit(struct iscsi_task \*task)
:   xmit iscsi-iser task

**Parameters**

`struct iscsi_task *task`
:   iscsi task

**Return**

zero on success or escalates $error on failure.

void iscsi_iser_cleanup_task(struct iscsi_task \*task)
:   cleanup an iscsi-iser task

**Parameters**

`struct iscsi_task *task`
:   iscsi task

**Notes**

In case the RDMA device is already NULL (might have
:   been removed in DEVICE_REMOVAL CM event it will bail-out
    without doing dma unmapping.

u8 iscsi_iser_check_protection(struct iscsi_task \*task, sector_t \*sector)
:   check protection information status of task.

**Parameters**

`struct iscsi_task *task`
:   iscsi task

`sector_t *sector`
:   error sector if exsists (output)

**Return**

zero if no data-integrity errors have occured
:   0x1: data-integrity error occured in the guard-block
    0x2: data-integrity error occured in the reference tag
    0x3: data-integrity error occured in the application tag

    In addition the error sector is marked.

struct iscsi_cls_conn \*iscsi_iser_conn_create(struct iscsi_cls_session \*cls_session, uint32_t conn_idx)
:   create a new iscsi-iser connection

**Parameters**

`struct iscsi_cls_session *cls_session`
:   iscsi class connection

`uint32_t conn_idx`
:   connection index within the session (for MCS)

**Return**

iscsi_cls_conn when iscsi_conn_setup succeeds or NULL
:   otherwise.

int iscsi_iser_conn_bind(struct iscsi_cls_session \*cls_session, struct iscsi_cls_conn \*cls_conn, uint64_t transport_eph, int is_leading)
:   bind iscsi and iser connection structures

**Parameters**

`struct iscsi_cls_session *cls_session`
:   iscsi class session

`struct iscsi_cls_conn *cls_conn`
:   iscsi class connection

`uint64_t transport_eph`
:   transport end-point handle

`int is_leading`
:   indicate if this is the session leading connection (MCS)

**Return**

zero on success, $error if iscsi_conn_bind fails and
:   -EINVAL in case end-point doesn't exists anymore or iser connection
    state is not UP (teardown already started).

int iscsi_iser_conn_start(struct iscsi_cls_conn \*cls_conn)
:   start iscsi-iser connection

**Parameters**

`struct iscsi_cls_conn *cls_conn`
:   iscsi class connection

**Notes**

Here iser intialize (or re-initialize) stop_completion as
:   from this point iscsi must call conn_stop in session/connection
    teardown so iser transport must wait for it.

void iscsi_iser_conn_stop(struct iscsi_cls_conn \*cls_conn, int flag)
:   stop iscsi-iser connection

**Parameters**

`struct iscsi_cls_conn *cls_conn`
:   iscsi class connection

`int flag`
:   indicate if recover or terminate (passed as is)

**Notes**

Calling iscsi_conn_stop might theoretically race with
:   DEVICE_REMOVAL event and dereference a previously freed RDMA device
    handle, so we call it under iser the state lock to protect against
    this kind of race.

void iscsi_iser_session_destroy(struct iscsi_cls_session \*cls_session)
:   destroy iscsi-iser session

**Parameters**

`struct iscsi_cls_session *cls_session`
:   iscsi class session

**Description**

Removes and free iscsi host.

struct iscsi_cls_session \*iscsi_iser_session_create(struct iscsi_endpoint \*ep, uint16_t cmds_max, uint16_t qdepth, uint32_t initial_cmdsn)
:   create an iscsi-iser session

**Parameters**

`struct iscsi_endpoint *ep`
:   iscsi end-point handle

`uint16_t cmds_max`
:   maximum commands in this session

`uint16_t qdepth`
:   session command queue depth

`uint32_t initial_cmdsn`
:   initiator command sequnce number

**Description**

Allocates and adds a scsi host, expose DIF supprot if
exists, and sets up an iscsi session.

struct iscsi_endpoint \*iscsi_iser_ep_connect(struct Scsi_Host \*shost, struct sockaddr \*dst_addr, int non_blocking)
:   Initiate iSER connection establishment

**Parameters**

`struct Scsi_Host *shost`
:   scsi_host

`struct sockaddr *dst_addr`
:   destination address

`int non_blocking`
:   indicate if routine can block

**Description**

Allocate an iscsi endpoint, an iser_conn structure and bind them.
After that start RDMA connection establishment via rdma_cm. We
don't allocate iser_conn embedded in iscsi_endpoint since in teardown
the endpoint will be destroyed at ep_disconnect while iser_conn will
cleanup its resources asynchronuously.

**Return**

iscsi_endpoint created by iscsi layer or ERR_PTR(error)
:   if fails.

int iscsi_iser_ep_poll(struct iscsi_endpoint \*ep, int timeout_ms)
:   poll for iser connection establishment to complete

**Parameters**

`struct iscsi_endpoint *ep`
:   iscsi endpoint (created at ep_connect)

`int timeout_ms`
:   polling timeout allowed in ms.

**Description**

This routine boils down to waiting for up_completion signaling
that cma_id got CONNECTED event.

**Return**

1 if succeeded in connection establishment, 0 if timeout expired
:   (libiscsi will retry will kick in) or -1 if interrupted by signal
    or more likely iser connection state transitioned to TEMINATING or
    DOWN during the wait period.

void iscsi_iser_ep_disconnect(struct iscsi_endpoint \*ep)
:   Initiate connection teardown process

**Parameters**

`struct iscsi_endpoint *ep`
:   iscsi endpoint handle

**Description**

This routine is not blocked by iser and RDMA termination process
completion as we queue a deffered work for iser/RDMA destruction
and cleanup or actually call it immediately in case we didn't pass
iscsi conn bind/start stage, thus it is safe.

int iser_send_command(struct iscsi_conn \*conn, struct iscsi_task \*task)
:   send command PDU

**Parameters**

`struct iscsi_conn *conn`
:   link to matching iscsi connection

`struct iscsi_task *task`
:   SCSI command task

int iser_send_data_out(struct iscsi_conn \*conn, struct iscsi_task \*task, struct iscsi_data \*hdr)
:   send data out PDU

**Parameters**

`struct iscsi_conn *conn`
:   link to matching iscsi connection

`struct iscsi_task *task`
:   SCSI command task

`struct iscsi_data *hdr`
:   pointer to the LLD's iSCSI message header

int iser_alloc_fastreg_pool(struct [ib_conn](infiniband.md#c.iser_alloc_fastreg_pool "ib_conn") \*ib_conn, unsigned cmds_max, unsigned int size)
:   Creates pool of fast_reg descriptors for fast registration work requests.

**Parameters**

`struct ib_conn *ib_conn`
:   connection RDMA resources

`unsigned cmds_max`
:   max number of SCSI commands for this connection

`unsigned int size`
:   max number of pages per map request

**Return**

0 on success, or errno code on failure

void iser_free_fastreg_pool(struct [ib_conn](infiniband.md#c.iser_free_fastreg_pool "ib_conn") \*ib_conn)
:   releases the pool of fast_reg descriptors

**Parameters**

`struct ib_conn *ib_conn`
:   connection RDMA resources

void iser_free_ib_conn_res(struct [iser_conn](infiniband.md#c.iser_free_ib_conn_res "iser_conn") \*iser_conn, bool destroy)
:   release IB related resources

**Parameters**

`struct iser_conn *iser_conn`
:   iser connection struct

`bool destroy`
:   indicator if we need to try to release the
    iser device and memory regoins pool (only iscsi
    shutdown and DEVICE_REMOVAL will use this).

**Description**

This routine is called with the iser state mutex held
so the cm_id removal is out of here. It is Safe to
be invoked multiple times.

void iser_conn_release(struct [iser_conn](infiniband.md#c.iser_conn_release "iser_conn") \*iser_conn)
:   Frees all conn objects and deallocs conn descriptor

**Parameters**

`struct iser_conn *iser_conn`
:   iSER connection context

int iser_conn_terminate(struct [iser_conn](infiniband.md#c.iser_conn_terminate "iser_conn") \*iser_conn)
:   triggers start of the disconnect procedures and waits for them to be done

**Parameters**

`struct iser_conn *iser_conn`
:   iSER connection context

**Description**

Called with state mutex held

int iser_post_send(struct [ib_conn](infiniband.md#c.iser_post_send "ib_conn") \*ib_conn, struct [iser_tx_desc](infiniband.md#c.iser_tx_desc "iser_tx_desc") \*tx_desc)
:   Initiate a Send DTO operation

**Parameters**

`struct ib_conn *ib_conn`
:   connection RDMA resources

`struct iser_tx_desc *tx_desc`
:   iSER TX descriptor

**Return**

0 on success, -1 on failure

### Omni-Path (OPA) Virtual NIC support

struct opa_vnic_ctrl_port
:   OPA virtual NIC control port

**Definition**:

```
struct opa_vnic_ctrl_port {
    struct ib_device           *ibdev;
    struct opa_vnic_ctrl_ops   *ops;
    u8 num_ports;
};
```

**Members**

`ibdev`
:   pointer to ib device

`ops`
:   opa vnic control operations

`num_ports`
:   number of opa ports

struct opa_vnic_adapter
:   OPA VNIC netdev private data structure

**Definition**:

```
struct opa_vnic_adapter {
    struct net_device             *netdev;
    struct ib_device              *ibdev;
    struct opa_vnic_ctrl_port     *cport;
    const struct net_device_ops   *rn_ops;
    u8 port_num;
    u8 vport_num;
    struct mutex lock;
    struct __opa_veswport_info  info;
    u8 vema_mac_addr[ETH_ALEN];
    u32 umac_hash;
    u32 mmac_hash;
    struct hlist_head  __rcu   *mactbl;
    struct mutex mactbl_lock;
    spinlock_t stats_lock;
    u8 flow_tbl[OPA_VNIC_FLOW_TBL_SIZE];
    unsigned long trap_timeout;
    u8 trap_count;
};
```

**Members**

`netdev`
:   pointer to associated netdev

`ibdev`
:   ib device

`cport`
:   pointer to opa vnic control port

`rn_ops`
:   rdma netdev's net_device_ops

`port_num`
:   OPA port number

`vport_num`
:   vesw port number

`lock`
:   adapter lock

`info`
:   virtual ethernet switch port information

`vema_mac_addr`
:   mac address configured by vema

`umac_hash`
:   unicast maclist hash

`mmac_hash`
:   multicast maclist hash

`mactbl`
:   hash table of MAC entries

`mactbl_lock`
:   mac table lock

`stats_lock`
:   statistics lock

`flow_tbl`
:   flow to default port redirection table

`trap_timeout`
:   trap timeout

`trap_count`
:   no. of traps allowed within timeout period

struct opa_vnic_mac_tbl_node
:   OPA VNIC mac table node

**Definition**:

```
struct opa_vnic_mac_tbl_node {
    struct hlist_node                    hlist;
    u16 index;
    struct __opa_vnic_mactable_entry     entry;
};
```

**Members**

`hlist`
:   hash list handle

`index`
:   index of entry in the mac table

`entry`
:   entry in the table

struct opa_vesw_info
:   OPA vnic switch information

**Definition**:

```
struct opa_vesw_info {
    __be16 fabric_id;
    __be16 vesw_id;
    u8 rsvd0[6];
    __be16 def_port_mask;
    u8 rsvd1[2];
    __be16 pkey;
    u8 rsvd2[4];
    __be32 u_mcast_dlid;
    __be32 u_ucast_dlid[OPA_VESW_MAX_NUM_DEF_PORT];
    __be32 rc;
    u8 rsvd3[56];
    __be16 eth_mtu;
    u8 rsvd4[2];
};
```

**Members**

`fabric_id`
:   10-bit fabric id

`vesw_id`
:   12-bit virtual ethernet switch id

`rsvd0`
:   reserved bytes

`def_port_mask`
:   bitmask of default ports

`rsvd1`
:   reserved bytes

`pkey`
:   partition key

`rsvd2`
:   reserved bytes

`u_mcast_dlid`
:   unknown multicast dlid

`u_ucast_dlid`
:   array of unknown unicast dlids

`rc`
:   routing control

`rsvd3`
:   reserved bytes

`eth_mtu`
:   Ethernet MTU

`rsvd4`
:   reserved bytes

struct opa_per_veswport_info
:   OPA vnic per port information

**Definition**:

```
struct opa_per_veswport_info {
    __be32 port_num;
    u8 eth_link_status;
    u8 rsvd0[3];
    u8 base_mac_addr[ETH_ALEN];
    u8 config_state;
    u8 oper_state;
    __be16 max_mac_tbl_ent;
    __be16 max_smac_ent;
    __be32 mac_tbl_digest;
    u8 rsvd1[4];
    __be32 encap_slid;
    u8 pcp_to_sc_uc[OPA_VNIC_MAX_NUM_PCP];
    u8 pcp_to_vl_uc[OPA_VNIC_MAX_NUM_PCP];
    u8 pcp_to_sc_mc[OPA_VNIC_MAX_NUM_PCP];
    u8 pcp_to_vl_mc[OPA_VNIC_MAX_NUM_PCP];
    u8 non_vlan_sc_uc;
    u8 non_vlan_vl_uc;
    u8 non_vlan_sc_mc;
    u8 non_vlan_vl_mc;
    u8 rsvd2[48];
    __be16 uc_macs_gen_count;
    __be16 mc_macs_gen_count;
    u8 rsvd3[8];
};
```

**Members**

`port_num`
:   port number

`eth_link_status`
:   current ethernet link state

`rsvd0`
:   reserved bytes

`base_mac_addr`
:   base mac address

`config_state`
:   configured port state

`oper_state`
:   operational port state

`max_mac_tbl_ent`
:   max number of mac table entries

`max_smac_ent`
:   max smac entries in mac table

`mac_tbl_digest`
:   mac table digest

`rsvd1`
:   reserved bytes

`encap_slid`
:   base slid for the port

`pcp_to_sc_uc`
:   sc by pcp index for unicast ethernet packets

`pcp_to_vl_uc`
:   vl by pcp index for unicast ethernet packets

`pcp_to_sc_mc`
:   sc by pcp index for multicast ethernet packets

`pcp_to_vl_mc`
:   vl by pcp index for multicast ethernet packets

`non_vlan_sc_uc`
:   sc for non-vlan unicast ethernet packets

`non_vlan_vl_uc`
:   vl for non-vlan unicast ethernet packets

`non_vlan_sc_mc`
:   sc for non-vlan multicast ethernet packets

`non_vlan_vl_mc`
:   vl for non-vlan multicast ethernet packets

`rsvd2`
:   reserved bytes

`uc_macs_gen_count`
:   generation count for unicast macs list

`mc_macs_gen_count`
:   generation count for multicast macs list

`rsvd3`
:   reserved bytes

struct opa_veswport_info
:   OPA vnic port information

**Definition**:

```
struct opa_veswport_info {
    struct opa_vesw_info          vesw;
    struct opa_per_veswport_info  vport;
};
```

**Members**

`vesw`
:   OPA vnic switch information

`vport`
:   OPA vnic per port information

**Description**

On host, each of the virtual ethernet ports belongs
to a different virtual ethernet switches.

struct opa_veswport_mactable_entry
:   single entry in the forwarding table

**Definition**:

```
struct opa_veswport_mactable_entry {
    u8 mac_addr[ETH_ALEN];
    u8 mac_addr_mask[ETH_ALEN];
    __be32 dlid_sd;
};
```

**Members**

`mac_addr`
:   MAC address

`mac_addr_mask`
:   MAC address bit mask

`dlid_sd`
:   Matching DLID and side data

**Description**

On the host each virtual ethernet port will have
a forwarding table. These tables are used to
map a MAC to a LID and other data. For more
details see struct opa_veswport_mactable_entries.
This is the structure of a single mactable entry

struct opa_veswport_mactable
:   Forwarding table array

**Definition**:

```
struct opa_veswport_mactable {
    __be16 offset;
    __be16 num_entries;
    __be32 mac_tbl_digest;
    struct opa_veswport_mactable_entry  tbl_entries[];
};
```

**Members**

`offset`
:   mac table starting offset

`num_entries`
:   Number of entries to get or set

`mac_tbl_digest`
:   mac table digest

`tbl_entries`
:   Array of table entries

**Description**

The EM sends down this structure in a MAD indicating
the starting offset in the forwarding table that this
entry is to be loaded into and the number of entries
that that this MAD instance contains
The mac_tbl_digest has been added to this MAD structure. It will be set by
the EM and it will be used by the EM to check if there are any
discrepancies with this value and the value
maintained by the EM in the case of VNIC port being deleted or unloaded
A new instantiation of a VNIC will always have a value of zero.
This value is stored as part of the vnic adapter structure and will be
accessed by the GET and SET routines for both the mactable entries and the
veswport info.

struct opa_veswport_summary_counters
:   summary counters

**Definition**:

```
struct opa_veswport_summary_counters {
    __be16 vp_instance;
    __be16 vesw_id;
    __be32 veswport_num;
    __be64 tx_errors;
    __be64 rx_errors;
    __be64 tx_packets;
    __be64 rx_packets;
    __be64 tx_bytes;
    __be64 rx_bytes;
    __be64 tx_unicast;
    __be64 tx_mcastbcast;
    __be64 tx_untagged;
    __be64 tx_vlan;
    __be64 tx_64_size;
    __be64 tx_65_127;
    __be64 tx_128_255;
    __be64 tx_256_511;
    __be64 tx_512_1023;
    __be64 tx_1024_1518;
    __be64 tx_1519_max;
    __be64 rx_unicast;
    __be64 rx_mcastbcast;
    __be64 rx_untagged;
    __be64 rx_vlan;
    __be64 rx_64_size;
    __be64 rx_65_127;
    __be64 rx_128_255;
    __be64 rx_256_511;
    __be64 rx_512_1023;
    __be64 rx_1024_1518;
    __be64 rx_1519_max;
    __be64 reserved[16];
};
```

**Members**

`vp_instance`
:   vport instance on the OPA port

`vesw_id`
:   virtual ethernet switch id

`veswport_num`
:   virtual ethernet switch port number

`tx_errors`
:   transmit errors

`rx_errors`
:   receive errors

`tx_packets`
:   transmit packets

`rx_packets`
:   receive packets

`tx_bytes`
:   transmit bytes

`rx_bytes`
:   receive bytes

`tx_unicast`
:   unicast packets transmitted

`tx_mcastbcast`
:   multicast/broadcast packets transmitted

`tx_untagged`
:   non-vlan packets transmitted

`tx_vlan`
:   vlan packets transmitted

`tx_64_size`
:   transmit packet length is 64 bytes

`tx_65_127`
:   transmit packet length is >=65 and < 127 bytes

`tx_128_255`
:   transmit packet length is >=128 and < 255 bytes

`tx_256_511`
:   transmit packet length is >=256 and < 511 bytes

`tx_512_1023`
:   transmit packet length is >=512 and < 1023 bytes

`tx_1024_1518`
:   transmit packet length is >=1024 and < 1518 bytes

`tx_1519_max`
:   transmit packet length >= 1519 bytes

`rx_unicast`
:   unicast packets received

`rx_mcastbcast`
:   multicast/broadcast packets received

`rx_untagged`
:   non-vlan packets received

`rx_vlan`
:   vlan packets received

`rx_64_size`
:   received packet length is 64 bytes

`rx_65_127`
:   received packet length is >=65 and < 127 bytes

`rx_128_255`
:   received packet length is >=128 and < 255 bytes

`rx_256_511`
:   received packet length is >=256 and < 511 bytes

`rx_512_1023`
:   received packet length is >=512 and < 1023 bytes

`rx_1024_1518`
:   received packet length is >=1024 and < 1518 bytes

`rx_1519_max`
:   received packet length >= 1519 bytes

`reserved`
:   reserved bytes

**Description**

All the above are counters of corresponding conditions.

struct opa_veswport_error_counters
:   error counters

**Definition**:

```
struct opa_veswport_error_counters {
    __be16 vp_instance;
    __be16 vesw_id;
    __be32 veswport_num;
    __be64 tx_errors;
    __be64 rx_errors;
    __be64 rsvd0;
    __be64 tx_smac_filt;
    __be64 rsvd1;
    __be64 rsvd2;
    __be64 rsvd3;
    __be64 tx_dlid_zero;
    __be64 rsvd4;
    __be64 tx_logic;
    __be64 rsvd5;
    __be64 tx_drop_state;
    __be64 rx_bad_veswid;
    __be64 rsvd6;
    __be64 rx_runt;
    __be64 rx_oversize;
    __be64 rsvd7;
    __be64 rx_eth_down;
    __be64 rx_drop_state;
    __be64 rx_logic;
    __be64 rsvd8;
    __be64 rsvd9[16];
};
```

**Members**

`vp_instance`
:   vport instance on the OPA port

`vesw_id`
:   virtual ethernet switch id

`veswport_num`
:   virtual ethernet switch port number

`tx_errors`
:   transmit errors

`rx_errors`
:   receive errors

`rsvd0`
:   reserved bytes

`tx_smac_filt`
:   smac filter errors

`rsvd1`
:   reserved bytes

`rsvd2`
:   reserved bytes

`rsvd3`
:   reserved bytes

`tx_dlid_zero`
:   transmit packets with invalid dlid

`rsvd4`
:   reserved bytes

`tx_logic`
:   other transmit errors

`rsvd5`
:   reserved bytes

`tx_drop_state`
:   packet tansmission in non-forward port state

`rx_bad_veswid`
:   received packet with invalid vesw id

`rsvd6`
:   reserved bytes

`rx_runt`
:   received ethernet packet with length < 64 bytes

`rx_oversize`
:   received ethernet packet with length > MTU size

`rsvd7`
:   reserved bytes

`rx_eth_down`
:   received packets when interface is down

`rx_drop_state`
:   received packets in non-forwarding port state

`rx_logic`
:   other receive errors

`rsvd8`
:   reserved bytes

`rsvd9`
:   reserved bytes

**Description**

All the above are counters of corresponding error conditions.

struct opa_veswport_trap
:   Trap message sent to EM by VNIC

**Definition**:

```
struct opa_veswport_trap {
    __be16 fabric_id;
    __be16 veswid;
    __be32 veswportnum;
    __be16 opaportnum;
    u8 veswportindex;
    u8 opcode;
    __be32 reserved;
};
```

**Members**

`fabric_id`
:   10 bit fabric id

`veswid`
:   12 bit virtual ethernet switch id

`veswportnum`
:   logical port number on the Virtual switch

`opaportnum`
:   physical port num (redundant on host)

`veswportindex`
:   switch port index on opa port 0 based

`opcode`
:   operation

`reserved`
:   32 bit for alignment

**Description**

The VNIC will send trap messages to the Ethernet manager to
inform it about changes to the VNIC config, behaviour etc.
This is the format of the trap payload.

struct opa_vnic_iface_mac_entry
:   single entry in the mac list

**Definition**:

```
struct opa_vnic_iface_mac_entry {
    u8 mac_addr[ETH_ALEN];
};
```

**Members**

`mac_addr`
:   MAC address

struct opa_veswport_iface_macs
:   Msg to set globally administered MAC

**Definition**:

```
struct opa_veswport_iface_macs {
    __be16 start_idx;
    __be16 num_macs_in_msg;
    __be16 tot_macs_in_lst;
    __be16 gen_count;
    struct opa_vnic_iface_mac_entry entry[];
};
```

**Members**

`start_idx`
:   position of first entry (0 based)

`num_macs_in_msg`
:   number of MACs in this message

`tot_macs_in_lst`
:   The total number of MACs the agent has

`gen_count`
:   gen_count to indicate change

`entry`
:   The mac list entry

**Description**

Same attribute IDS and attribute modifiers as in locally administered
addresses used to set globally administered addresses

struct opa_vnic_vema_mad
:   Generic VEMA MAD

**Definition**:

```
struct opa_vnic_vema_mad {
    struct ib_mad_hdr  mad_hdr;
    struct ib_rmpp_hdr rmpp_hdr;
    u8 reserved;
    u8 oui[3];
    u8 data[OPA_VNIC_EMA_DATA];
};
```

**Members**

`mad_hdr`
:   Generic MAD header

`rmpp_hdr`
:   RMPP header for vendor specific MADs

`reserved`
:   reserved bytes

`oui`
:   Unique org identifier

`data`
:   MAD data

struct opa_vnic_notice_attr
:   Generic Notice MAD

**Definition**:

```
struct opa_vnic_notice_attr {
    u8 gen_type;
    u8 oui_1;
    u8 oui_2;
    u8 oui_3;
    __be16 trap_num;
    __be16 toggle_count;
    __be32 issuer_lid;
    __be32 reserved;
    u8 issuer_gid[16];
    u8 raw_data[64];
};
```

**Members**

`gen_type`
:   Generic/Specific bit and type of notice

`oui_1`
:   Vendor ID byte 1

`oui_2`
:   Vendor ID byte 2

`oui_3`
:   Vendor ID byte 3

`trap_num`
:   Trap number

`toggle_count`
:   Notice toggle bit and count value

`issuer_lid`
:   Trap issuer's lid

`reserved`
:   reserved bytes

`issuer_gid`
:   Issuer GID (only if Report method)

`raw_data`
:   Trap message body

struct opa_vnic_vema_mad_trap
:   Generic VEMA MAD Trap

**Definition**:

```
struct opa_vnic_vema_mad_trap {
    struct ib_mad_hdr            mad_hdr;
    struct ib_rmpp_hdr           rmpp_hdr;
    u8 reserved;
    u8 oui[3];
    struct opa_vnic_notice_attr  notice;
};
```

**Members**

`mad_hdr`
:   Generic MAD header

`rmpp_hdr`
:   RMPP header for vendor specific MADs

`reserved`
:   reserved bytes

`oui`
:   Unique org identifier

`notice`
:   Notice structure

void opa_vnic_vema_report_event(struct [opa_vnic_adapter](infiniband.md#c.opa_vnic_adapter "opa_vnic_adapter") \*adapter, u8 event)
:   sent trap to report the specified event

**Parameters**

`struct opa_vnic_adapter *adapter`
:   vnic port adapter

`u8 event`
:   event to be reported

**Description**

This function calls vema api to sent a trap for the given event.

void opa_vnic_get_summary_counters(struct [opa_vnic_adapter](infiniband.md#c.opa_vnic_adapter "opa_vnic_adapter") \*adapter, struct [opa_veswport_summary_counters](infiniband.md#c.opa_veswport_summary_counters "opa_veswport_summary_counters") \*cntrs)
:   get summary counters

**Parameters**

`struct opa_vnic_adapter *adapter`
:   vnic port adapter

`struct opa_veswport_summary_counters *cntrs`
:   pointer to destination summary counters structure

**Description**

This function populates the summary counters that is maintained by the
given adapter to destination address provided.

void opa_vnic_get_error_counters(struct [opa_vnic_adapter](infiniband.md#c.opa_vnic_adapter "opa_vnic_adapter") \*adapter, struct [opa_veswport_error_counters](infiniband.md#c.opa_veswport_error_counters "opa_veswport_error_counters") \*cntrs)
:   get error counters

**Parameters**

`struct opa_vnic_adapter *adapter`
:   vnic port adapter

`struct opa_veswport_error_counters *cntrs`
:   pointer to destination error counters structure

**Description**

This function populates the error counters that is maintained by the
given adapter to destination address provided.

void opa_vnic_get_vesw_info(struct [opa_vnic_adapter](infiniband.md#c.opa_vnic_adapter "opa_vnic_adapter") \*adapter, struct [opa_vesw_info](infiniband.md#c.opa_vesw_info "opa_vesw_info") \*info)
:   - Get the vesw information

**Parameters**

`struct opa_vnic_adapter *adapter`
:   vnic port adapter

`struct opa_vesw_info *info`
:   pointer to destination vesw info structure

**Description**

This function copies the vesw info that is maintained by the
given adapter to destination address provided.

void opa_vnic_set_vesw_info(struct [opa_vnic_adapter](infiniband.md#c.opa_vnic_adapter "opa_vnic_adapter") \*adapter, struct [opa_vesw_info](infiniband.md#c.opa_vesw_info "opa_vesw_info") \*info)
:   - Set the vesw information

**Parameters**

`struct opa_vnic_adapter *adapter`
:   vnic port adapter

`struct opa_vesw_info *info`
:   pointer to vesw info structure

**Description**

This function updates the vesw info that is maintained by the
given adapter with vesw info provided. Reserved fields are stored
and returned back to EM as is.

void opa_vnic_get_per_veswport_info(struct [opa_vnic_adapter](infiniband.md#c.opa_vnic_adapter "opa_vnic_adapter") \*adapter, struct [opa_per_veswport_info](infiniband.md#c.opa_per_veswport_info "opa_per_veswport_info") \*info)
:   - Get the vesw per port information

**Parameters**

`struct opa_vnic_adapter *adapter`
:   vnic port adapter

`struct opa_per_veswport_info *info`
:   pointer to destination vport info structure

**Description**

This function copies the vesw per port info that is maintained by the
given adapter to destination address provided.
Note that the read only fields are not copied.

void opa_vnic_set_per_veswport_info(struct [opa_vnic_adapter](infiniband.md#c.opa_vnic_adapter "opa_vnic_adapter") \*adapter, struct [opa_per_veswport_info](infiniband.md#c.opa_per_veswport_info "opa_per_veswport_info") \*info)
:   - Set vesw per port information

**Parameters**

`struct opa_vnic_adapter *adapter`
:   vnic port adapter

`struct opa_per_veswport_info *info`
:   pointer to vport info structure

**Description**

This function updates the vesw per port info that is maintained by the
given adapter with vesw per port info provided. Reserved fields are
stored and returned back to EM as is.

void opa_vnic_query_mcast_macs(struct [opa_vnic_adapter](infiniband.md#c.opa_vnic_adapter "opa_vnic_adapter") \*adapter, struct [opa_veswport_iface_macs](infiniband.md#c.opa_veswport_iface_macs "opa_veswport_iface_macs") \*macs)
:   query multicast mac list

**Parameters**

`struct opa_vnic_adapter *adapter`
:   vnic port adapter

`struct opa_veswport_iface_macs *macs`
:   pointer mac list

**Description**

This function populates the provided mac list with the configured
multicast addresses in the adapter.

void opa_vnic_query_ucast_macs(struct [opa_vnic_adapter](infiniband.md#c.opa_vnic_adapter "opa_vnic_adapter") \*adapter, struct [opa_veswport_iface_macs](infiniband.md#c.opa_veswport_iface_macs "opa_veswport_iface_macs") \*macs)
:   query unicast mac list

**Parameters**

`struct opa_vnic_adapter *adapter`
:   vnic port adapter

`struct opa_veswport_iface_macs *macs`
:   pointer mac list

**Description**

This function populates the provided mac list with the configured
unicast addresses in the adapter.

struct opa_vnic_vema_port
:   - VNIC VEMA port details

**Definition**:

```
struct opa_vnic_vema_port {
    struct opa_vnic_ctrl_port      *cport;
    struct ib_mad_agent            *mad_agent;
    struct opa_class_port_info      class_port_info;
    u64 tid;
    u8 port_num;
    struct xarray                   vports;
    struct ib_event_handler         event_handler;
    struct mutex                    lock;
};
```

**Members**

`cport`
:   pointer to port

`mad_agent`
:   pointer to mad agent for port

`class_port_info`
:   Class port info information.

`tid`
:   Transaction id

`port_num`
:   OPA port number

`vports`
:   vnic ports

`event_handler`
:   ib event handler

`lock`
:   adapter interface lock

u8 vema_get_vport_num(struct [opa_vnic_vema_mad](infiniband.md#c.opa_vnic_vema_mad "opa_vnic_vema_mad") \*recvd_mad)
:   - Get the vnic from the mad

**Parameters**

`struct opa_vnic_vema_mad *recvd_mad`
:   Received mad

**Return**

returns value of the vnic port number

struct [opa_vnic_adapter](infiniband.md#c.opa_vnic_adapter "opa_vnic_adapter") \*vema_get_vport_adapter(struct [opa_vnic_vema_mad](infiniband.md#c.opa_vnic_vema_mad "opa_vnic_vema_mad") \*recvd_mad, struct [opa_vnic_vema_port](infiniband.md#c.opa_vnic_vema_port "opa_vnic_vema_port") \*port)
:   - Get vnic port adapter from recvd mad

**Parameters**

`struct opa_vnic_vema_mad *recvd_mad`
:   received mad

`struct opa_vnic_vema_port *port`
:   ptr to port struct on which MAD was recvd

**Return**

vnic adapter

bool vema_mac_tbl_req_ok(struct [opa_veswport_mactable](infiniband.md#c.opa_veswport_mactable "opa_veswport_mactable") \*mac_tbl)
:   - Check if mac request has correct values

**Parameters**

`struct opa_veswport_mactable *mac_tbl`
:   mac table

**Description**

This function checks for the validity of the offset and number of
entries required.

**Return**

true if offset and num_entries are valid

struct [opa_vnic_adapter](infiniband.md#c.opa_vnic_adapter "opa_vnic_adapter") \*vema_add_vport(struct [opa_vnic_vema_port](infiniband.md#c.opa_vnic_vema_port "opa_vnic_vema_port") \*port, u8 vport_num)
:   - Add a new vnic port

**Parameters**

`struct opa_vnic_vema_port *port`
:   ptr to opa_vnic_vema_port struct

`u8 vport_num`
:   vnic port number (to be added)

**Description**

Return a pointer to the vnic adapter structure

void vema_get_class_port_info(struct [opa_vnic_vema_port](infiniband.md#c.opa_vnic_vema_port "opa_vnic_vema_port") \*port, struct [opa_vnic_vema_mad](infiniband.md#c.opa_vnic_vema_mad "opa_vnic_vema_mad") \*recvd_mad, struct [opa_vnic_vema_mad](infiniband.md#c.opa_vnic_vema_mad "opa_vnic_vema_mad") \*rsp_mad)
:   - Get class info for port

**Parameters**

`struct opa_vnic_vema_port *port`
:   Port on whic MAD was received

`struct opa_vnic_vema_mad *recvd_mad`
:   pointer to the received mad

`struct opa_vnic_vema_mad *rsp_mad`
:   pointer to respose mad

**Description**

This function copies the latest class port info value set for the
port and stores it for generating traps

void vema_set_class_port_info(struct [opa_vnic_vema_port](infiniband.md#c.opa_vnic_vema_port "opa_vnic_vema_port") \*port, struct [opa_vnic_vema_mad](infiniband.md#c.opa_vnic_vema_mad "opa_vnic_vema_mad") \*recvd_mad, struct [opa_vnic_vema_mad](infiniband.md#c.opa_vnic_vema_mad "opa_vnic_vema_mad") \*rsp_mad)
:   - Get class info for port

**Parameters**

`struct opa_vnic_vema_port *port`
:   Port on whic MAD was received

`struct opa_vnic_vema_mad *recvd_mad`
:   pointer to the received mad

`struct opa_vnic_vema_mad *rsp_mad`
:   pointer to respose mad

**Description**

This function updates the port class info for the specific vnic
and sets up the response mad data

void vema_get_veswport_info(struct [opa_vnic_vema_port](infiniband.md#c.opa_vnic_vema_port "opa_vnic_vema_port") \*port, struct [opa_vnic_vema_mad](infiniband.md#c.opa_vnic_vema_mad "opa_vnic_vema_mad") \*recvd_mad, struct [opa_vnic_vema_mad](infiniband.md#c.opa_vnic_vema_mad "opa_vnic_vema_mad") \*rsp_mad)
:   - Get veswport info

**Parameters**

`struct opa_vnic_vema_port *port`
:   source port on which MAD was received

`struct opa_vnic_vema_mad *recvd_mad`
:   pointer to the received mad

`struct opa_vnic_vema_mad *rsp_mad`
:   pointer to respose mad

void vema_set_veswport_info(struct [opa_vnic_vema_port](infiniband.md#c.opa_vnic_vema_port "opa_vnic_vema_port") \*port, struct [opa_vnic_vema_mad](infiniband.md#c.opa_vnic_vema_mad "opa_vnic_vema_mad") \*recvd_mad, struct [opa_vnic_vema_mad](infiniband.md#c.opa_vnic_vema_mad "opa_vnic_vema_mad") \*rsp_mad)
:   - Set veswport info

**Parameters**

`struct opa_vnic_vema_port *port`
:   source port on which MAD was received

`struct opa_vnic_vema_mad *recvd_mad`
:   pointer to the received mad

`struct opa_vnic_vema_mad *rsp_mad`
:   pointer to respose mad

**Description**

This function gets the port class infor for vnic

void vema_get_mac_entries(struct [opa_vnic_vema_port](infiniband.md#c.opa_vnic_vema_port "opa_vnic_vema_port") \*port, struct [opa_vnic_vema_mad](infiniband.md#c.opa_vnic_vema_mad "opa_vnic_vema_mad") \*recvd_mad, struct [opa_vnic_vema_mad](infiniband.md#c.opa_vnic_vema_mad "opa_vnic_vema_mad") \*rsp_mad)
:   - Get MAC entries in VNIC MAC table

**Parameters**

`struct opa_vnic_vema_port *port`
:   source port on which MAD was received

`struct opa_vnic_vema_mad *recvd_mad`
:   pointer to the received mad

`struct opa_vnic_vema_mad *rsp_mad`
:   pointer to respose mad

**Description**

This function gets the MAC entries that are programmed into
the VNIC MAC forwarding table. It checks for the validity of
the index into the MAC table and the number of entries that
are to be retrieved.

void vema_set_mac_entries(struct [opa_vnic_vema_port](infiniband.md#c.opa_vnic_vema_port "opa_vnic_vema_port") \*port, struct [opa_vnic_vema_mad](infiniband.md#c.opa_vnic_vema_mad "opa_vnic_vema_mad") \*recvd_mad, struct [opa_vnic_vema_mad](infiniband.md#c.opa_vnic_vema_mad "opa_vnic_vema_mad") \*rsp_mad)
:   - Set MAC entries in VNIC MAC table

**Parameters**

`struct opa_vnic_vema_port *port`
:   source port on which MAD was received

`struct opa_vnic_vema_mad *recvd_mad`
:   pointer to the received mad

`struct opa_vnic_vema_mad *rsp_mad`
:   pointer to respose mad

**Description**

This function sets the MAC entries in the VNIC forwarding table
It checks for the validity of the index and the number of forwarding
table entries to be programmed.

void vema_set_delete_vesw(struct [opa_vnic_vema_port](infiniband.md#c.opa_vnic_vema_port "opa_vnic_vema_port") \*port, struct [opa_vnic_vema_mad](infiniband.md#c.opa_vnic_vema_mad "opa_vnic_vema_mad") \*recvd_mad, struct [opa_vnic_vema_mad](infiniband.md#c.opa_vnic_vema_mad "opa_vnic_vema_mad") \*rsp_mad)
:   - Reset VESW info to POD values

**Parameters**

`struct opa_vnic_vema_port *port`
:   source port on which MAD was received

`struct opa_vnic_vema_mad *recvd_mad`
:   pointer to the received mad

`struct opa_vnic_vema_mad *rsp_mad`
:   pointer to respose mad

**Description**

This function clears all the fields of veswport info for the requested vesw
and sets them back to the power-on default values. It does not delete the
vesw.

void vema_get_mac_list(struct [opa_vnic_vema_port](infiniband.md#c.opa_vnic_vema_port "opa_vnic_vema_port") \*port, struct [opa_vnic_vema_mad](infiniband.md#c.opa_vnic_vema_mad "opa_vnic_vema_mad") \*recvd_mad, struct [opa_vnic_vema_mad](infiniband.md#c.opa_vnic_vema_mad "opa_vnic_vema_mad") \*rsp_mad, u16 attr_id)
:   - Get the unicast/multicast macs.

**Parameters**

`struct opa_vnic_vema_port *port`
:   source port on which MAD was received

`struct opa_vnic_vema_mad *recvd_mad`
:   Received mad contains fields to set vnic parameters

`struct opa_vnic_vema_mad *rsp_mad`
:   Response mad to be built

`u16 attr_id`
:   Attribute ID indicating multicast or unicast mac list

void vema_get_summary_counters(struct [opa_vnic_vema_port](infiniband.md#c.opa_vnic_vema_port "opa_vnic_vema_port") \*port, struct [opa_vnic_vema_mad](infiniband.md#c.opa_vnic_vema_mad "opa_vnic_vema_mad") \*recvd_mad, struct [opa_vnic_vema_mad](infiniband.md#c.opa_vnic_vema_mad "opa_vnic_vema_mad") \*rsp_mad)
:   - Gets summary counters.

**Parameters**

`struct opa_vnic_vema_port *port`
:   source port on which MAD was received

`struct opa_vnic_vema_mad *recvd_mad`
:   Received mad contains fields to set vnic parameters

`struct opa_vnic_vema_mad *rsp_mad`
:   Response mad to be built

void vema_get_error_counters(struct [opa_vnic_vema_port](infiniband.md#c.opa_vnic_vema_port "opa_vnic_vema_port") \*port, struct [opa_vnic_vema_mad](infiniband.md#c.opa_vnic_vema_mad "opa_vnic_vema_mad") \*recvd_mad, struct [opa_vnic_vema_mad](infiniband.md#c.opa_vnic_vema_mad "opa_vnic_vema_mad") \*rsp_mad)
:   - Gets summary counters.

**Parameters**

`struct opa_vnic_vema_port *port`
:   source port on which MAD was received

`struct opa_vnic_vema_mad *recvd_mad`
:   Received mad contains fields to set vnic parameters

`struct opa_vnic_vema_mad *rsp_mad`
:   Response mad to be built

void vema_get(struct [opa_vnic_vema_port](infiniband.md#c.opa_vnic_vema_port "opa_vnic_vema_port") \*port, struct [opa_vnic_vema_mad](infiniband.md#c.opa_vnic_vema_mad "opa_vnic_vema_mad") \*recvd_mad, struct [opa_vnic_vema_mad](infiniband.md#c.opa_vnic_vema_mad "opa_vnic_vema_mad") \*rsp_mad)
:   - Process received get MAD

**Parameters**

`struct opa_vnic_vema_port *port`
:   source port on which MAD was received

`struct opa_vnic_vema_mad *recvd_mad`
:   Received mad

`struct opa_vnic_vema_mad *rsp_mad`
:   Response mad to be built

void vema_set(struct [opa_vnic_vema_port](infiniband.md#c.opa_vnic_vema_port "opa_vnic_vema_port") \*port, struct [opa_vnic_vema_mad](infiniband.md#c.opa_vnic_vema_mad "opa_vnic_vema_mad") \*recvd_mad, struct [opa_vnic_vema_mad](infiniband.md#c.opa_vnic_vema_mad "opa_vnic_vema_mad") \*rsp_mad)
:   - Process received set MAD

**Parameters**

`struct opa_vnic_vema_port *port`
:   source port on which MAD was received

`struct opa_vnic_vema_mad *recvd_mad`
:   Received mad contains fields to set vnic parameters

`struct opa_vnic_vema_mad *rsp_mad`
:   Response mad to be built

void vema_send(struct ib_mad_agent \*mad_agent, struct ib_mad_send_wc \*mad_wc)
:   - Send handler for VEMA MAD agent

**Parameters**

`struct ib_mad_agent *mad_agent`
:   pointer to the mad agent

`struct ib_mad_send_wc *mad_wc`
:   pointer to mad send work completion information

**Description**

Free all the data structures associated with the sent MAD

void vema_recv(struct ib_mad_agent \*mad_agent, struct ib_mad_send_buf \*send_buf, struct ib_mad_recv_wc \*mad_wc)
:   - Recv handler for VEMA MAD agent

**Parameters**

`struct ib_mad_agent *mad_agent`
:   pointer to the mad agent

`struct ib_mad_send_buf *send_buf`
:   Send buffer if found, else NULL

`struct ib_mad_recv_wc *mad_wc`
:   pointer to mad send work completion information

**Description**

Handle only set and get methods and respond to other methods
as unsupported. Allocate response buffer and address handle
for the response MAD.

struct [opa_vnic_vema_port](infiniband.md#c.opa_vnic_vema_port "opa_vnic_vema_port") \*vema_get_port(struct [opa_vnic_ctrl_port](infiniband.md#c.opa_vnic_ctrl_port "opa_vnic_ctrl_port") \*cport, u8 port_num)
:   - Gets the opa_vnic_vema_port

**Parameters**

`struct opa_vnic_ctrl_port *cport`
:   pointer to control dev

`u8 port_num`
:   Port number

**Description**

This function loops through the ports and returns
the opa_vnic_vema port structure that is associated
with the OPA port number

**Return**

ptr to requested opa_vnic_vema_port strucure
:   if success, NULL if not

void opa_vnic_vema_send_trap(struct [opa_vnic_adapter](infiniband.md#c.opa_vnic_adapter "opa_vnic_adapter") \*adapter, struct __opa_veswport_trap \*data, u32 lid)
:   - This function sends a trap to the EM

**Parameters**

`struct opa_vnic_adapter *adapter`
:   pointer to vnic adapter

`struct __opa_veswport_trap *data`
:   pointer to trap data filled by calling function

`u32 lid`
:   issuers lid (encap_slid from vesw_port_info)

**Description**

This function is called from the VNIC driver to send a trap if there
is somethng the EM should be notified about. These events currently
are
1) UNICAST INTERFACE MACADDRESS changes
2) MULTICAST INTERFACE MACADDRESS changes
3) ETHERNET LINK STATUS changes
While allocating the send mad the remote site qpn used is 1
as this is the well known QP.

void vema_unregister(struct [opa_vnic_ctrl_port](infiniband.md#c.opa_vnic_ctrl_port "opa_vnic_ctrl_port") \*cport)
:   - Unregisters agent

**Parameters**

`struct opa_vnic_ctrl_port *cport`
:   pointer to control port

**Description**

This deletes the registration by VEMA for MADs

int vema_register(struct [opa_vnic_ctrl_port](infiniband.md#c.opa_vnic_ctrl_port "opa_vnic_ctrl_port") \*cport)
:   - Registers agent

**Parameters**

`struct opa_vnic_ctrl_port *cport`
:   pointer to control port

**Description**

This function registers the handlers for the VEMA MADs

**Return**

returns 0 on success. non zero otherwise

void opa_vnic_ctrl_config_dev(struct [opa_vnic_ctrl_port](infiniband.md#c.opa_vnic_ctrl_port "opa_vnic_ctrl_port") \*cport, bool en)
:   - This function sends a trap to the EM by way of ib_modify_port to indicate support for ethernet on the fabric.

**Parameters**

`struct opa_vnic_ctrl_port *cport`
:   pointer to control port

`bool en`
:   enable or disable ethernet on fabric support

int opa_vnic_vema_add_one(struct ib_device \*device)
:   - Handle new ib device

**Parameters**

`struct ib_device *device`
:   ib device pointer

**Description**

Allocate the vnic control port and initialize it.

void opa_vnic_vema_rem_one(struct ib_device \*device, void \*client_data)
:   - Handle ib device removal

**Parameters**

`struct ib_device *device`
:   ib device pointer

`void *client_data`
:   ib client data

**Description**

Uninitialize and free the vnic control port.

### InfiniBand SCSI RDMA protocol target support

enum srpt_command_state
:   SCSI command state managed by SRPT

**Constants**

`SRPT_STATE_NEW`
:   New command arrived and is being processed.

`SRPT_STATE_NEED_DATA`
:   Processing a write or bidir command and waiting
    for data arrival.

`SRPT_STATE_DATA_IN`
:   Data for the write or bidir command arrived and is
    being processed.

`SRPT_STATE_CMD_RSP_SENT`
:   SRP_RSP for SRP_CMD has been sent.

`SRPT_STATE_MGMT`
:   Processing a SCSI task management command.

`SRPT_STATE_MGMT_RSP_SENT`
:   SRP_RSP for SRP_TSK_MGMT has been sent.

`SRPT_STATE_DONE`
:   Command processing finished successfully, command
    processing has been aborted or command processing
    failed.

struct srpt_ioctx
:   shared SRPT I/O context information

**Definition**:

```
struct srpt_ioctx {
    struct ib_cqe           cqe;
    void *buf;
    dma_addr_t dma;
    uint32_t offset;
    uint32_t index;
};
```

**Members**

`cqe`
:   Completion queue element.

`buf`
:   Pointer to the buffer.

`dma`
:   DMA address of the buffer.

`offset`
:   Offset of the first byte in **buf** and **dma** that is actually used.

`index`
:   Index of the I/O context in its ioctx_ring array.

struct srpt_recv_ioctx
:   SRPT receive I/O context

**Definition**:

```
struct srpt_recv_ioctx {
    struct srpt_ioctx       ioctx;
    struct list_head        wait_list;
    int byte_len;
};
```

**Members**

`ioctx`
:   See above.

`wait_list`
:   Node for insertion in srpt_rdma_ch.cmd_wait_list.

`byte_len`
:   Number of bytes in **ioctx.buf**.

struct srpt_send_ioctx
:   SRPT send I/O context

**Definition**:

```
struct srpt_send_ioctx {
    struct srpt_ioctx       ioctx;
    struct srpt_rdma_ch     *ch;
    struct srpt_recv_ioctx  *recv_ioctx;
    struct srpt_rw_ctx      s_rw_ctx;
    struct srpt_rw_ctx      *rw_ctxs;
    struct scatterlist      imm_sg;
    struct ib_cqe           rdma_cqe;
    enum srpt_command_state state;
    struct se_cmd           cmd;
    u8 n_rdma;
    u8 n_rw_ctx;
    bool queue_status_only;
    u8 sense_data[TRANSPORT_SENSE_BUFFER];
};
```

**Members**

`ioctx`
:   See above.

`ch`
:   Channel pointer.

`recv_ioctx`
:   Receive I/O context associated with this send I/O context.
    Only used for processing immediate data.

`s_rw_ctx`
:   **rw_ctxs** points here if only a single rw_ctx is needed.

`rw_ctxs`
:   RDMA read/write contexts.

`imm_sg`
:   Scatterlist for immediate data.

`rdma_cqe`
:   RDMA completion queue element.

`state`
:   I/O context state.

`cmd`
:   Target core command data structure.

`n_rdma`
:   Number of work requests needed to transfer this ioctx.

`n_rw_ctx`
:   Size of rw_ctxs array.

`queue_status_only`
:   Send a SCSI status back to the initiator but no data.

`sense_data`
:   Sense data to be sent to the initiator.

enum rdma_ch_state
:   SRP channel state

**Constants**

`CH_CONNECTING`
:   QP is in RTR state; waiting for RTU.

`CH_LIVE`
:   QP is in RTS state.

`CH_DISCONNECTING`
:   DREQ has been sent and waiting for DREP or DREQ has
    been received.

`CH_DRAINING`
:   DREP has been received or waiting for DREP timed out
    and last work request has been queued.

`CH_DISCONNECTED`
:   Last completion has been received.

struct srpt_rdma_ch
:   RDMA channel

**Definition**:

```
struct srpt_rdma_ch {
    struct srpt_nexus       *nexus;
    struct ib_qp            *qp;
    union {
        struct {
            struct ib_cm_id         *cm_id;
        } ib_cm;
        struct {
            struct rdma_cm_id       *cm_id;
        } rdma_cm;
    };
    struct ib_cq            *cq;
    u32 cq_size;
    struct ib_cqe           zw_cqe;
    struct rcu_head         rcu;
    struct kref             kref;
    struct completion       *closed;
    int rq_size;
    u32 max_rsp_size;
    atomic_t sq_wr_avail;
    struct srpt_port        *sport;
    int max_ti_iu_len;
    atomic_t req_lim;
    atomic_t req_lim_delta;
    u16 imm_data_offset;
    spinlock_t spinlock;
    enum rdma_ch_state      state;
    struct kmem_cache       *rsp_buf_cache;
    struct srpt_send_ioctx  **ioctx_ring;
    struct kmem_cache       *req_buf_cache;
    struct srpt_recv_ioctx  **ioctx_recv_ring;
    struct list_head        list;
    struct list_head        cmd_wait_list;
    uint16_t pkey;
    bool using_rdma_cm;
    bool processing_wait_list;
    struct se_session       *sess;
    u8 sess_name[40];
    struct work_struct      release_work;
};
```

**Members**

`nexus`
:   I_T nexus this channel is associated with.

`qp`
:   IB queue pair used for communicating over this channel.

`{unnamed_union}`
:   anonymous

`ib_cm`
:   See below.

`ib_cm.cm_id`
:   IB CM ID associated with the channel.

`rdma_cm`
:   See below.

`rdma_cm.cm_id`
:   RDMA CM ID associated with the channel.

`cq`
:   IB completion queue for this channel.

`cq_size`
:   Number of CQEs in **cq**.

`zw_cqe`
:   Zero-length write CQE.

`rcu`
:   RCU head.

`kref`
:   kref for this channel.

`closed`
:   Completion object that will be signaled as soon as a new
    channel object with the same identity can be created.

`rq_size`
:   IB receive queue size.

`max_rsp_size`
:   Maximum size of an RSP response message in bytes.

`sq_wr_avail`
:   number of work requests available in the send queue.

`sport`
:   pointer to the information of the HCA port used by this
    channel.

`max_ti_iu_len`
:   maximum target-to-initiator information unit length.

`req_lim`
:   request limit: maximum number of requests that may be sent
    by the initiator without having received a response.

`req_lim_delta`
:   Number of credits not yet sent back to the initiator.

`imm_data_offset`
:   Offset from start of SRP_CMD for immediate data.

`spinlock`
:   Protects free_list and state.

`state`
:   channel state. See also [`enum rdma_ch_state`](infiniband.md#c.rdma_ch_state "rdma_ch_state").

`rsp_buf_cache`
:   kmem_cache for **ioctx_ring**.

`ioctx_ring`
:   Send ring.

`req_buf_cache`
:   kmem_cache for **ioctx_recv_ring**.

`ioctx_recv_ring`
:   Receive I/O context ring.

`list`
:   Node in srpt_nexus.ch_list.

`cmd_wait_list`
:   List of SCSI commands that arrived before the RTU event. This
    list contains [`struct srpt_ioctx`](infiniband.md#c.srpt_ioctx "srpt_ioctx") elements and is protected
    against concurrent modification by the cm_id spinlock.

`pkey`
:   P_Key of the IB partition for this SRP channel.

`using_rdma_cm`
:   Whether the RDMA/CM or IB/CM is used for this channel.

`processing_wait_list`
:   Whether or not cmd_wait_list is being processed.

`sess`
:   Session information associated with this SRP channel.

`sess_name`
:   Session name.

`release_work`
:   Allows scheduling of srpt_release_channel().

struct srpt_nexus
:   I_T nexus

**Definition**:

```
struct srpt_nexus {
    struct rcu_head         rcu;
    struct list_head        entry;
    struct list_head        ch_list;
    u8 i_port_id[16];
    u8 t_port_id[16];
};
```

**Members**

`rcu`
:   RCU head for this data structure.

`entry`
:   srpt_port.nexus_list list node.

`ch_list`
:   [`struct srpt_rdma_ch`](infiniband.md#c.srpt_rdma_ch "srpt_rdma_ch") list. Protected by srpt_port.mutex.

`i_port_id`
:   128-bit initiator port identifier copied from SRP_LOGIN_REQ.

`t_port_id`
:   128-bit target port identifier copied from SRP_LOGIN_REQ.

struct srpt_port_attrib
:   attributes for SRPT port

**Definition**:

```
struct srpt_port_attrib {
    u32 srp_max_rdma_size;
    u32 srp_max_rsp_size;
    u32 srp_sq_size;
    bool use_srq;
};
```

**Members**

`srp_max_rdma_size`
:   Maximum size of SRP RDMA transfers for new connections.

`srp_max_rsp_size`
:   Maximum size of SRP response messages in bytes.

`srp_sq_size`
:   Shared receive queue (SRQ) size.

`use_srq`
:   Whether or not to use SRQ.

struct srpt_tpg
:   information about a single "target portal group"

**Definition**:

```
struct srpt_tpg {
    struct list_head        entry;
    struct srpt_port_id     *sport_id;
    struct se_portal_group  tpg;
};
```

**Members**

`entry`
:   Entry in **sport_id->tpg_list**.

`sport_id`
:   Port name this TPG is associated with.

`tpg`
:   LIO TPG data structure.

**Description**

Zero or more target portal groups are associated with each port name
(srpt_port_id). With each TPG an ACL list is associated.

struct srpt_port_id
:   LIO RDMA port information

**Definition**:

```
struct srpt_port_id {
    struct mutex            mutex;
    struct list_head        tpg_list;
    struct se_wwn           wwn;
    char name[64];
};
```

**Members**

`mutex`
:   Protects **tpg_list** changes.

`tpg_list`
:   TPGs associated with the RDMA port name.

`wwn`
:   WWN associated with the RDMA port name.

`name`
:   ASCII representation of the port name.

**Description**

Multiple sysfs directories can be associated with a single RDMA port. This
data structure represents a single (port, name) pair.

struct srpt_port
:   SRPT RDMA port information

**Definition**:

```
struct srpt_port {
    struct srpt_device      *sdev;
    struct ib_mad_agent     *mad_agent;
    bool enabled;
    u8 port;
    u32 sm_lid;
    u32 lid;
    union ib_gid            gid;
    struct work_struct      work;
    char guid_name[64];
    struct srpt_port_id     *guid_id;
    char gid_name[64];
    struct srpt_port_id     *gid_id;
    struct srpt_port_attrib port_attrib;
    atomic_t refcount;
    struct completion       *freed_channels;
    struct mutex            mutex;
    struct list_head        nexus_list;
};
```

**Members**

`sdev`
:   backpointer to the HCA information.

`mad_agent`
:   per-port management datagram processing information.

`enabled`
:   Whether or not this target port is enabled.

`port`
:   one-based port number.

`sm_lid`
:   cached value of the port's sm_lid.

`lid`
:   cached value of the port's lid.

`gid`
:   cached value of the port's gid.

`work`
:   work structure for refreshing the aforementioned cached values.

`guid_name`
:   port name in GUID format.

`guid_id`
:   LIO target port information for the port name in GUID format.

`gid_name`
:   port name in GID format.

`gid_id`
:   LIO target port information for the port name in GID format.

`port_attrib`
:   Port attributes that can be accessed through configfs.

`refcount`
:   Number of objects associated with this port.

`freed_channels`
:   Completion that will be signaled once **refcount** becomes 0.

`mutex`
:   Protects nexus_list.

`nexus_list`
:   Nexus list. See also srpt_nexus.entry.

struct srpt_device
:   information associated by SRPT with a single HCA

**Definition**:

```
struct srpt_device {
    struct kref             refcnt;
    struct ib_device        *device;
    struct ib_pd            *pd;
    u32 lkey;
    struct ib_srq           *srq;
    struct ib_cm_id         *cm_id;
    int srq_size;
    struct mutex            sdev_mutex;
    bool use_srq;
    struct kmem_cache       *req_buf_cache;
    struct srpt_recv_ioctx  **ioctx_ring;
    struct ib_event_handler event_handler;
    struct list_head        list;
    struct srpt_port        port[];
};
```

**Members**

`refcnt`
:   Reference count for this device.

`device`
:   Backpointer to the struct ib_device managed by the IB core.

`pd`
:   IB protection domain.

`lkey`
:   L_Key (local key) with write access to all local memory.

`srq`
:   Per-HCA SRQ (shared receive queue).

`cm_id`
:   Connection identifier.

`srq_size`
:   SRQ size.

`sdev_mutex`
:   Serializes use_srq changes.

`use_srq`
:   Whether or not to use SRQ.

`req_buf_cache`
:   kmem_cache for **ioctx_ring** buffers.

`ioctx_ring`
:   Per-HCA SRQ.

`event_handler`
:   Per-HCA asynchronous IB event handler.

`list`
:   Node in srpt_dev_list.

`port`
:   Information about the ports owned by this HCA.

void srpt_event_handler(struct ib_event_handler \*handler, struct ib_event \*event)
:   asynchronous IB event callback function

**Parameters**

`struct ib_event_handler *handler`
:   IB event handler registered by [`ib_register_event_handler()`](infiniband.md#c.ib_register_event_handler "ib_register_event_handler").

`struct ib_event *event`
:   Description of the event that occurred.

**Description**

Callback function called by the InfiniBand core when an asynchronous IB
event occurs. This callback may occur in interrupt context. See also
section 11.5.2, Set Asynchronous Event Handler in the InfiniBand
Architecture Specification.

void srpt_srq_event(struct ib_event \*event, void \*ctx)
:   SRQ event callback function

**Parameters**

`struct ib_event *event`
:   Description of the event that occurred.

`void *ctx`
:   Context pointer specified at SRQ creation time.

void srpt_qp_event(struct ib_event \*event, void \*ptr)
:   QP event callback function

**Parameters**

`struct ib_event *event`
:   Description of the event that occurred.

`void *ptr`
:   SRPT RDMA channel.

void srpt_set_ioc(u8 \*c_list, u32 slot, u8 value)
:   initialize a IOUnitInfo structure

**Parameters**

`u8 *c_list`
:   controller list.

`u32 slot`
:   one-based slot number.

`u8 value`
:   four-bit value.

**Description**

Copies the lowest four bits of value in element slot of the array of four
bit elements called c_list (controller list). The index slot is one-based.

void srpt_get_class_port_info(struct ib_dm_mad \*mad)
:   copy ClassPortInfo to a management datagram

**Parameters**

`struct ib_dm_mad *mad`
:   Datagram that will be sent as response to DM_ATTR_CLASS_PORT_INFO.

**Description**

See also section 16.3.3.1 ClassPortInfo in the InfiniBand Architecture
Specification.

void srpt_get_iou(struct ib_dm_mad \*mad)
:   write IOUnitInfo to a management datagram

**Parameters**

`struct ib_dm_mad *mad`
:   Datagram that will be sent as response to DM_ATTR_IOU_INFO.

**Description**

See also section 16.3.3.3 IOUnitInfo in the InfiniBand Architecture
Specification. See also section B.7, table B.6 in the SRP r16a document.

void srpt_get_ioc(struct [srpt_port](infiniband.md#c.srpt_port "srpt_port") \*sport, u32 slot, struct ib_dm_mad \*mad)
:   write IOControllerprofile to a management datagram

**Parameters**

`struct srpt_port *sport`
:   HCA port through which the MAD has been received.

`u32 slot`
:   Slot number specified in DM_ATTR_IOC_PROFILE query.

`struct ib_dm_mad *mad`
:   Datagram that will be sent as response to DM_ATTR_IOC_PROFILE.

**Description**

See also section 16.3.3.4 IOControllerProfile in the InfiniBand
Architecture Specification. See also section B.7, table B.7 in the SRP
r16a document.

void srpt_get_svc_entries(u64 ioc_guid, u16 slot, u8 hi, u8 lo, struct ib_dm_mad \*mad)
:   write ServiceEntries to a management datagram

**Parameters**

`u64 ioc_guid`
:   I/O controller GUID to use in reply.

`u16 slot`
:   I/O controller number.

`u8 hi`
:   End of the range of service entries to be specified in the reply.

`u8 lo`
:   Start of the range of service entries to be specified in the reply..

`struct ib_dm_mad *mad`
:   Datagram that will be sent as response to DM_ATTR_SVC_ENTRIES.

**Description**

See also section 16.3.3.5 ServiceEntries in the InfiniBand Architecture
Specification. See also section B.7, table B.8 in the SRP r16a document.

void srpt_mgmt_method_get(struct [srpt_port](infiniband.md#c.srpt_port "srpt_port") \*sp, struct ib_mad \*rq_mad, struct ib_dm_mad \*rsp_mad)
:   process a received management datagram

**Parameters**

`struct srpt_port *sp`
:   HCA port through which the MAD has been received.

`struct ib_mad *rq_mad`
:   received MAD.

`struct ib_dm_mad *rsp_mad`
:   response MAD.

void srpt_mad_send_handler(struct ib_mad_agent \*mad_agent, struct ib_mad_send_wc \*mad_wc)
:   MAD send completion callback

**Parameters**

`struct ib_mad_agent *mad_agent`
:   Return value of ib_register_mad_agent().

`struct ib_mad_send_wc *mad_wc`
:   Work completion reporting that the MAD has been sent.

void srpt_mad_recv_handler(struct ib_mad_agent \*mad_agent, struct ib_mad_send_buf \*send_buf, struct ib_mad_recv_wc \*mad_wc)
:   MAD reception callback function

**Parameters**

`struct ib_mad_agent *mad_agent`
:   Return value of ib_register_mad_agent().

`struct ib_mad_send_buf *send_buf`
:   Not used.

`struct ib_mad_recv_wc *mad_wc`
:   Work completion reporting that a MAD has been received.

int srpt_refresh_port(struct [srpt_port](infiniband.md#c.srpt_port "srpt_port") \*sport)
:   configure a HCA port

**Parameters**

`struct srpt_port *sport`
:   SRPT HCA port.

**Description**

Enable InfiniBand management datagram processing, update the cached sm_lid,
lid and gid values, and register a callback function for processing MADs
on the specified port.

**Note**

It is safe to call this function more than once for the same port.

void srpt_unregister_mad_agent(struct [srpt_device](infiniband.md#c.srpt_device "srpt_device") \*sdev, int port_cnt)
:   unregister MAD callback functions

**Parameters**

`struct srpt_device *sdev`
:   SRPT HCA pointer.

`int port_cnt`
:   number of ports with registered MAD

**Note**

It is safe to call this function more than once for the same device.

struct [srpt_ioctx](infiniband.md#c.srpt_ioctx "srpt_ioctx") \*srpt_alloc_ioctx(struct [srpt_device](infiniband.md#c.srpt_device "srpt_device") \*sdev, int ioctx_size, struct kmem_cache \*buf_cache, enum dma_data_direction dir)
:   allocate a SRPT I/O context structure

**Parameters**

`struct srpt_device *sdev`
:   SRPT HCA pointer.

`int ioctx_size`
:   I/O context size.

`struct kmem_cache *buf_cache`
:   I/O buffer cache.

`enum dma_data_direction dir`
:   DMA data direction.

void srpt_free_ioctx(struct [srpt_device](infiniband.md#c.srpt_device "srpt_device") \*sdev, struct [srpt_ioctx](infiniband.md#c.srpt_ioctx "srpt_ioctx") \*ioctx, struct kmem_cache \*buf_cache, enum dma_data_direction dir)
:   free a SRPT I/O context structure

**Parameters**

`struct srpt_device *sdev`
:   SRPT HCA pointer.

`struct srpt_ioctx *ioctx`
:   I/O context pointer.

`struct kmem_cache *buf_cache`
:   I/O buffer cache.

`enum dma_data_direction dir`
:   DMA data direction.

struct [srpt_ioctx](infiniband.md#c.srpt_ioctx "srpt_ioctx") \*\*srpt_alloc_ioctx_ring(struct [srpt_device](infiniband.md#c.srpt_device "srpt_device") \*sdev, int ring_size, int ioctx_size, struct kmem_cache \*buf_cache, int alignment_offset, enum dma_data_direction dir)
:   allocate a ring of SRPT I/O context structures

**Parameters**

`struct srpt_device *sdev`
:   Device to allocate the I/O context ring for.

`int ring_size`
:   Number of elements in the I/O context ring.

`int ioctx_size`
:   I/O context size.

`struct kmem_cache *buf_cache`
:   I/O buffer cache.

`int alignment_offset`
:   Offset in each ring buffer at which the SRP information
    unit starts.

`enum dma_data_direction dir`
:   DMA data direction.

void srpt_free_ioctx_ring(struct [srpt_ioctx](infiniband.md#c.srpt_ioctx "srpt_ioctx") \*\*ioctx_ring, struct [srpt_device](infiniband.md#c.srpt_device "srpt_device") \*sdev, int ring_size, struct kmem_cache \*buf_cache, enum dma_data_direction dir)
:   free the ring of SRPT I/O context structures

**Parameters**

`struct srpt_ioctx **ioctx_ring`
:   I/O context ring to be freed.

`struct srpt_device *sdev`
:   SRPT HCA pointer.

`int ring_size`
:   Number of ring elements.

`struct kmem_cache *buf_cache`
:   I/O buffer cache.

`enum dma_data_direction dir`
:   DMA data direction.

enum [srpt_command_state](infiniband.md#c.srpt_command_state "srpt_command_state") srpt_set_cmd_state(struct [srpt_send_ioctx](infiniband.md#c.srpt_send_ioctx "srpt_send_ioctx") \*ioctx, enum [srpt_command_state](infiniband.md#c.srpt_command_state "srpt_command_state") new)
:   set the state of a SCSI command

**Parameters**

`struct srpt_send_ioctx *ioctx`
:   Send I/O context.

`enum srpt_command_state new`
:   New I/O context state.

**Description**

Does not modify the state of aborted commands. Returns the previous command
state.

bool srpt_test_and_set_cmd_state(struct [srpt_send_ioctx](infiniband.md#c.srpt_send_ioctx "srpt_send_ioctx") \*ioctx, enum [srpt_command_state](infiniband.md#c.srpt_command_state "srpt_command_state") old, enum [srpt_command_state](infiniband.md#c.srpt_command_state "srpt_command_state") new)
:   test and set the state of a command

**Parameters**

`struct srpt_send_ioctx *ioctx`
:   Send I/O context.

`enum srpt_command_state old`
:   Current I/O context state.

`enum srpt_command_state new`
:   New I/O context state.

**Description**

Returns true if and only if the previous command state was equal to 'old'.

int srpt_post_recv(struct [srpt_device](infiniband.md#c.srpt_device "srpt_device") \*sdev, struct [srpt_rdma_ch](infiniband.md#c.srpt_rdma_ch "srpt_rdma_ch") \*ch, struct [srpt_recv_ioctx](infiniband.md#c.srpt_recv_ioctx "srpt_recv_ioctx") \*ioctx)
:   post an IB receive request

**Parameters**

`struct srpt_device *sdev`
:   SRPT HCA pointer.

`struct srpt_rdma_ch *ch`
:   SRPT RDMA channel.

`struct srpt_recv_ioctx *ioctx`
:   Receive I/O context pointer.

int srpt_zerolength_write(struct [srpt_rdma_ch](infiniband.md#c.srpt_rdma_ch "srpt_rdma_ch") \*ch)
:   perform a zero-length RDMA write

**Parameters**

`struct srpt_rdma_ch *ch`
:   SRPT RDMA channel.

**Description**

A quote from the InfiniBand specification: C9-88: For an HCA responder
using Reliable Connection service, for each zero-length RDMA READ or WRITE
request, the R_Key shall not be validated, even if the request includes
Immediate data.

int srpt_get_desc_tbl(struct [srpt_recv_ioctx](infiniband.md#c.srpt_recv_ioctx "srpt_recv_ioctx") \*recv_ioctx, struct [srpt_send_ioctx](infiniband.md#c.srpt_send_ioctx "srpt_send_ioctx") \*ioctx, struct [srp_cmd](infiniband.md#c.srpt_get_desc_tbl "srp_cmd") \*srp_cmd, enum dma_data_direction \*dir, struct scatterlist \*\*sg, unsigned int \*sg_cnt, u64 \*data_len, u16 imm_data_offset)
:   parse the data descriptors of a SRP_CMD request

**Parameters**

`struct srpt_recv_ioctx *recv_ioctx`
:   I/O context associated with the received command **srp_cmd**.

`struct srpt_send_ioctx *ioctx`
:   I/O context that will be used for responding to the initiator.

`struct srp_cmd *srp_cmd`
:   Pointer to the SRP_CMD request data.

`enum dma_data_direction *dir`
:   Pointer to the variable to which the transfer direction will be
    written.

`struct scatterlist **sg`
:   [out] scatterlist for the parsed SRP_CMD.

`unsigned int *sg_cnt`
:   [out] length of **sg**.

`u64 *data_len`
:   Pointer to the variable to which the total data length of all
    descriptors in the SRP_CMD request will be written.

`u16 imm_data_offset`
:   [in] Offset in SRP_CMD requests at which immediate data
    starts.

**Description**

This function initializes ioctx->nrbuf and ioctx->r_bufs.

Returns -EINVAL when the SRP_CMD request contains inconsistent descriptors;
-ENOMEM when memory allocation fails and zero upon success.

int srpt_init_ch_qp(struct [srpt_rdma_ch](infiniband.md#c.srpt_rdma_ch "srpt_rdma_ch") \*ch, struct ib_qp \*qp)
:   initialize queue pair attributes

**Parameters**

`struct srpt_rdma_ch *ch`
:   SRPT RDMA channel.

`struct ib_qp *qp`
:   Queue pair pointer.

**Description**

Initialized the attributes of queue pair 'qp' by allowing local write,
remote read and remote write. Also transitions 'qp' to state IB_QPS_INIT.

int srpt_ch_qp_rtr(struct [srpt_rdma_ch](infiniband.md#c.srpt_rdma_ch "srpt_rdma_ch") \*ch, struct ib_qp \*qp)
:   change the state of a channel to 'ready to receive' (RTR)

**Parameters**

`struct srpt_rdma_ch *ch`
:   channel of the queue pair.

`struct ib_qp *qp`
:   queue pair to change the state of.

**Description**

Returns zero upon success and a negative value upon failure.

**Note**

currently a struct ib_qp_attr takes 136 bytes on a 64-bit system.
If this structure ever becomes larger, it might be necessary to allocate
it dynamically instead of on the stack.

int srpt_ch_qp_rts(struct [srpt_rdma_ch](infiniband.md#c.srpt_rdma_ch "srpt_rdma_ch") \*ch, struct ib_qp \*qp)
:   change the state of a channel to 'ready to send' (RTS)

**Parameters**

`struct srpt_rdma_ch *ch`
:   channel of the queue pair.

`struct ib_qp *qp`
:   queue pair to change the state of.

**Description**

Returns zero upon success and a negative value upon failure.

**Note**

currently a struct ib_qp_attr takes 136 bytes on a 64-bit system.
If this structure ever becomes larger, it might be necessary to allocate
it dynamically instead of on the stack.

int srpt_ch_qp_err(struct [srpt_rdma_ch](infiniband.md#c.srpt_rdma_ch "srpt_rdma_ch") \*ch)
:   set the channel queue pair state to 'error'

**Parameters**

`struct srpt_rdma_ch *ch`
:   SRPT RDMA channel.

struct [srpt_send_ioctx](infiniband.md#c.srpt_send_ioctx "srpt_send_ioctx") \*srpt_get_send_ioctx(struct [srpt_rdma_ch](infiniband.md#c.srpt_rdma_ch "srpt_rdma_ch") \*ch)
:   obtain an I/O context for sending to the initiator

**Parameters**

`struct srpt_rdma_ch *ch`
:   SRPT RDMA channel.

int srpt_abort_cmd(struct [srpt_send_ioctx](infiniband.md#c.srpt_send_ioctx "srpt_send_ioctx") \*ioctx)
:   abort a SCSI command

**Parameters**

`struct srpt_send_ioctx *ioctx`
:   I/O context associated with the SCSI command.

void srpt_rdma_read_done(struct ib_cq \*cq, struct ib_wc \*wc)
:   RDMA read completion callback

**Parameters**

`struct ib_cq *cq`
:   Completion queue.

`struct ib_wc *wc`
:   Work completion.

**Description**

XXX: what is now target_execute_cmd used to be asynchronous, and unmapping
the data that has been transferred via IB RDMA had to be postponed until the
check_stop_free() callback. None of this is necessary anymore and needs to
be cleaned up.

int srpt_build_cmd_rsp(struct [srpt_rdma_ch](infiniband.md#c.srpt_rdma_ch "srpt_rdma_ch") \*ch, struct [srpt_send_ioctx](infiniband.md#c.srpt_send_ioctx "srpt_send_ioctx") \*ioctx, u64 tag, int status)
:   build a SRP_RSP response

**Parameters**

`struct srpt_rdma_ch *ch`
:   RDMA channel through which the request has been received.

`struct srpt_send_ioctx *ioctx`
:   I/O context associated with the SRP_CMD request. The response will
    be built in the buffer ioctx->buf points at and hence this function will
    overwrite the request data.

`u64 tag`
:   tag of the request for which this response is being generated.

`int status`
:   value for the STATUS field of the SRP_RSP information unit.

**Description**

Returns the size in bytes of the SRP_RSP response.

An SRP_RSP response contains a SCSI status or service response. See also
section 6.9 in the SRP r16a document for the format of an SRP_RSP
response. See also SPC-2 for more information about sense data.

int srpt_build_tskmgmt_rsp(struct [srpt_rdma_ch](infiniband.md#c.srpt_rdma_ch "srpt_rdma_ch") \*ch, struct [srpt_send_ioctx](infiniband.md#c.srpt_send_ioctx "srpt_send_ioctx") \*ioctx, u8 rsp_code, u64 tag)
:   build a task management response

**Parameters**

`struct srpt_rdma_ch *ch`
:   RDMA channel through which the request has been received.

`struct srpt_send_ioctx *ioctx`
:   I/O context in which the SRP_RSP response will be built.

`u8 rsp_code`
:   RSP_CODE that will be stored in the response.

`u64 tag`
:   Tag of the request for which this response is being generated.

**Description**

Returns the size in bytes of the SRP_RSP response.

An SRP_RSP response contains a SCSI status or service response. See also
section 6.9 in the SRP r16a document for the format of an SRP_RSP
response.

void srpt_handle_cmd(struct [srpt_rdma_ch](infiniband.md#c.srpt_rdma_ch "srpt_rdma_ch") \*ch, struct [srpt_recv_ioctx](infiniband.md#c.srpt_recv_ioctx "srpt_recv_ioctx") \*recv_ioctx, struct [srpt_send_ioctx](infiniband.md#c.srpt_send_ioctx "srpt_send_ioctx") \*send_ioctx)
:   process a SRP_CMD information unit

**Parameters**

`struct srpt_rdma_ch *ch`
:   SRPT RDMA channel.

`struct srpt_recv_ioctx *recv_ioctx`
:   Receive I/O context.

`struct srpt_send_ioctx *send_ioctx`
:   Send I/O context.

void srpt_handle_tsk_mgmt(struct [srpt_rdma_ch](infiniband.md#c.srpt_rdma_ch "srpt_rdma_ch") \*ch, struct [srpt_recv_ioctx](infiniband.md#c.srpt_recv_ioctx "srpt_recv_ioctx") \*recv_ioctx, struct [srpt_send_ioctx](infiniband.md#c.srpt_send_ioctx "srpt_send_ioctx") \*send_ioctx)
:   process a SRP_TSK_MGMT information unit

**Parameters**

`struct srpt_rdma_ch *ch`
:   SRPT RDMA channel.

`struct srpt_recv_ioctx *recv_ioctx`
:   Receive I/O context.

`struct srpt_send_ioctx *send_ioctx`
:   Send I/O context.

**Description**

Returns 0 if and only if the request will be processed by the target core.

For more information about SRP_TSK_MGMT information units, see also section
6.7 in the SRP r16a document.

bool srpt_handle_new_iu(struct [srpt_rdma_ch](infiniband.md#c.srpt_rdma_ch "srpt_rdma_ch") \*ch, struct [srpt_recv_ioctx](infiniband.md#c.srpt_recv_ioctx "srpt_recv_ioctx") \*recv_ioctx)
:   process a newly received information unit

**Parameters**

`struct srpt_rdma_ch *ch`
:   RDMA channel through which the information unit has been received.

`struct srpt_recv_ioctx *recv_ioctx`
:   Receive I/O context associated with the information unit.

void srpt_send_done(struct ib_cq \*cq, struct ib_wc \*wc)
:   send completion callback

**Parameters**

`struct ib_cq *cq`
:   Completion queue.

`struct ib_wc *wc`
:   Work completion.

**Note**

Although this has not yet been observed during tests, at least in
theory it is possible that the [`srpt_get_send_ioctx()`](infiniband.md#c.srpt_get_send_ioctx "srpt_get_send_ioctx") call invoked by
[`srpt_handle_new_iu()`](infiniband.md#c.srpt_handle_new_iu "srpt_handle_new_iu") fails. This is possible because the req_lim_delta
value in each response is set to one, and it is possible that this response
makes the initiator send a new request before the send completion for that
response has been processed. This could e.g. happen if the call to
srpt_put_send_iotcx() is delayed because of a higher priority interrupt or
if IB retransmission causes generation of the send completion to be
delayed. Incoming information units for which [`srpt_get_send_ioctx()`](infiniband.md#c.srpt_get_send_ioctx "srpt_get_send_ioctx") fails
are queued on cmd_wait_list. The code below processes these delayed
requests one at a time.

int srpt_create_ch_ib(struct [srpt_rdma_ch](infiniband.md#c.srpt_rdma_ch "srpt_rdma_ch") \*ch)
:   create receive and send completion queues

**Parameters**

`struct srpt_rdma_ch *ch`
:   SRPT RDMA channel.

bool srpt_close_ch(struct [srpt_rdma_ch](infiniband.md#c.srpt_rdma_ch "srpt_rdma_ch") \*ch)
:   close a RDMA channel

**Parameters**

`struct srpt_rdma_ch *ch`
:   SRPT RDMA channel.

**Description**

Make sure all resources associated with the channel will be deallocated at
an appropriate time.

Returns true if and only if the channel state has been modified into
CH_DRAINING.

int srpt_cm_req_recv(struct [srpt_device](infiniband.md#c.srpt_device "srpt_device") \*const sdev, struct [ib_cm_id](infiniband.md#c.srpt_cm_req_recv "ib_cm_id") \*ib_cm_id, struct [rdma_cm_id](infiniband.md#c.srpt_cm_req_recv "rdma_cm_id") \*rdma_cm_id, u8 port_num, __be16 pkey, const struct srp_login_req \*req, const char \*src_addr)
:   process the event IB_CM_REQ_RECEIVED

**Parameters**

`struct srpt_device *const sdev`
:   HCA through which the login request was received.

`struct ib_cm_id *ib_cm_id`
:   IB/CM connection identifier in case of IB/CM.

`struct rdma_cm_id *rdma_cm_id`
:   RDMA/CM connection identifier in case of RDMA/CM.

`u8 port_num`
:   Port through which the REQ message was received.

`__be16 pkey`
:   P_Key of the incoming connection.

`const struct srp_login_req *req`
:   SRP login request.

`const char *src_addr`
:   GID (IB/CM) or IP address (RDMA/CM) of the port that submitted
    the login request.

**Description**

Ownership of the cm_id is transferred to the target session if this
function returns zero. Otherwise the caller remains the owner of cm_id.

void srpt_cm_rtu_recv(struct [srpt_rdma_ch](infiniband.md#c.srpt_rdma_ch "srpt_rdma_ch") \*ch)
:   process an IB_CM_RTU_RECEIVED or USER_ESTABLISHED event

**Parameters**

`struct srpt_rdma_ch *ch`
:   SRPT RDMA channel.

**Description**

An RTU (ready to use) message indicates that the connection has been
established and that the recipient may begin transmitting.

int srpt_cm_handler(struct ib_cm_id \*cm_id, const struct ib_cm_event \*event)
:   IB connection manager callback function

**Parameters**

`struct ib_cm_id *cm_id`
:   IB/CM connection identifier.

`const struct ib_cm_event *event`
:   IB/CM event.

**Description**

A non-zero return value will cause the caller destroy the CM ID.

**Note**

[`srpt_cm_handler()`](infiniband.md#c.srpt_cm_handler "srpt_cm_handler") must only return a non-zero value when transferring
ownership of the cm_id to a channel by [`srpt_cm_req_recv()`](infiniband.md#c.srpt_cm_req_recv "srpt_cm_req_recv") failed. Returning
a non-zero value in any other case will trigger a race with the
ib_destroy_cm_id() call in srpt_release_channel().

void srpt_queue_response(struct se_cmd \*cmd)
:   transmit the response to a SCSI command

**Parameters**

`struct se_cmd *cmd`
:   SCSI target command.

**Description**

Callback function called by the TCM core. Must not block since it can be
invoked on the context of the IB completion handler.

int srpt_release_sport(struct [srpt_port](infiniband.md#c.srpt_port "srpt_port") \*sport)
:   disable login and wait for associated channels

**Parameters**

`struct srpt_port *sport`
:   SRPT HCA port.

struct port_and_port_id srpt_lookup_port(const char \*name)
:   Look up an RDMA port by name

**Parameters**

`const char *name`
:   ASCII port name

**Description**

Increments the RDMA port reference count if an RDMA port pointer is returned.
The caller must drop that reference count by calling srpt_port_put_ref().

int srpt_add_one(struct ib_device \*device)
:   InfiniBand device addition callback function

**Parameters**

`struct ib_device *device`
:   Describes a HCA.

void srpt_remove_one(struct ib_device \*device, void \*client_data)
:   InfiniBand device removal callback function

**Parameters**

`struct ib_device *device`
:   Describes a HCA.

`void *client_data`
:   The value passed as the third argument to [`ib_set_client_data()`](infiniband.md#c.ib_set_client_data "ib_set_client_data").

void srpt_close_session(struct se_session \*se_sess)
:   forcibly close a session

**Parameters**

`struct se_session *se_sess`
:   SCSI target session.

**Description**

Callback function invoked by the TCM core to clean up sessions associated
with a node ACL when the user invokes
rmdir /sys/kernel/config/target/$driver/$port/$tpg/acls/$i_port_id

int srpt_parse_i_port_id(u8 i_port_id[16], const char \*name)
:   parse an initiator port ID

**Parameters**

`u8 i_port_id[16]`
:   Binary 128-bit port ID.

`const char *name`
:   ASCII representation of a 128-bit initiator port ID.

struct se_portal_group \*srpt_make_tpg(struct se_wwn \*wwn, const char \*name)
:   configfs callback invoked for mkdir /sys/kernel/config/target/$driver/$port/$tpg

**Parameters**

`struct se_wwn *wwn`
:   Corresponds to $driver/$port.

`const char *name`
:   $tpg.

void srpt_drop_tpg(struct se_portal_group \*tpg)
:   configfs callback invoked for rmdir /sys/kernel/config/target/$driver/$port/$tpg

**Parameters**

`struct se_portal_group *tpg`
:   Target portal group to deregister.

struct se_wwn \*srpt_make_tport(struct target_fabric_configfs \*tf, struct config_group \*group, const char \*name)
:   configfs callback invoked for mkdir /sys/kernel/config/target/$driver/$port

**Parameters**

`struct target_fabric_configfs *tf`
:   Not used.

`struct config_group *group`
:   Not used.

`const char *name`
:   $port.

void srpt_drop_tport(struct se_wwn \*wwn)
:   configfs callback invoked for rmdir /sys/kernel/config/target/$driver/$port

**Parameters**

`struct se_wwn *wwn`
:   $port.

int srpt_init_module(void)
:   kernel module initialization

**Parameters**

`void`
:   no arguments

**Note**

Since [`ib_register_client()`](infiniband.md#c.ib_register_client "ib_register_client") registers callback functions, and since at
least one of these callback functions ([`srpt_add_one()`](infiniband.md#c.srpt_add_one "srpt_add_one")) calls target core
functions, this driver must be registered with the target core before
[`ib_register_client()`](infiniband.md#c.ib_register_client "ib_register_client") is called.

### iSCSI Extensions for RDMA (iSER) target support

void isert_conn_terminate(struct [isert_conn](infiniband.md#c.isert_conn_terminate "isert_conn") \*isert_conn)
:   Initiate connection termination

**Parameters**

`struct isert_conn *isert_conn`
:   isert connection struct

**Notes**

In case the connection state is BOUND, move state
to TEMINATING and start teardown sequence (rdma_disconnect).
In case the connection state is UP, complete flush as well.

**Description**

This routine must be called with mutex held. Thus it is
safe to call multiple times.

void isert_put_unsol_pending_cmds(struct iscsit_conn \*conn)
:   Drop commands waiting for unsolicitate dataout

**Parameters**

`struct iscsit_conn *conn`
:   iscsi connection

**Description**

We might still have commands that are waiting for unsolicited
dataouts messages. We must put the extra reference on those
before blocking on the target_wait_for_session_cmds
