---
collection: kernel
version: "6.8"
title: "Other Firmware Interfaces"
source_url: https://www.kernel.org/doc/html/v6.8/driver-api/firmware/other_interfaces.html
fetched_at: 2026-08-21T03:32:14+00:00
---
# Other Firmware Interfaces

## DMI Interfaces

int dmi_check_system(const struct dmi_system_id \*list)
:   check system DMI data

**Parameters**

`const struct dmi_system_id *list`
:   array of dmi_system_id structures to match against
    All non-null elements of the list must match
    their slot's (field index's) data (i.e., each
    list string must be a substring of the specified
    DMI slot's string data) to be considered a
    successful match.

    > Walk the blacklist table running matching functions until someone
    > returns non zero or we hit the end. Callback function is called for
    > each successful match. Returns the number of matches.
    >
    > dmi_setup must be called before this function is called.

const struct dmi_system_id \*dmi_first_match(const struct dmi_system_id \*list)
:   find dmi_system_id structure matching system DMI data

**Parameters**

`const struct dmi_system_id *list`
:   array of dmi_system_id structures to match against
    All non-null elements of the list must match
    their slot's (field index's) data (i.e., each
    list string must be a substring of the specified
    DMI slot's string data) to be considered a
    successful match.

    > Walk the blacklist table until the first match is found. Return the
    > pointer to the matching entry or NULL if there's no match.
    >
    > dmi_setup must be called before this function is called.

const char \*dmi_get_system_info(int field)
:   return DMI data value

**Parameters**

`int field`
:   data index (see enum dmi_field)

    Returns one DMI data value, can be used to perform
    complex DMI data checks.

int dmi_name_in_vendors(const char \*str)
:   Check if string is in the DMI system or board vendor name

**Parameters**

`const char *str`
:   Case sensitive Name

const struct dmi_device \*dmi_find_device(int type, const char \*name, const struct dmi_device \*from)
:   find onboard device by type/name

**Parameters**

`int type`
:   device type or `DMI_DEV_TYPE_ANY` to match all device types

`const char *name`
:   device name string or `NULL` to match all

`const struct dmi_device *from`
:   previous device found in search, or `NULL` for new search.

    Iterates through the list of known onboard devices. If a device is
    found with a matching **type** and **name**, a pointer to its device
    structure is returned. Otherwise, `NULL` is returned.
    A new search is initiated by passing `NULL` as the **from** argument.
    If **from** is not `NULL`, searches continue from next device.

bool dmi_get_date(int field, int \*yearp, int \*monthp, int \*dayp)
:   parse a DMI date

**Parameters**

`int field`
:   data index (see enum dmi_field)

`int *yearp`
:   optional out parameter for the year

`int *monthp`
:   optional out parameter for the month

`int *dayp`
:   optional out parameter for the day

    The date field is assumed to be in the form resembling
    [mm[/dd]]/yy[yy] and the result is stored in the out
    parameters any or all of which can be omitted.

    If the field doesn't exist, all out parameters are set to zero
    and false is returned. Otherwise, true is returned with any
    invalid part of date set to zero.

    On return, year, month and day are guaranteed to be in the
    range of [0,9999], [0,12] and [0,31] respectively.

int dmi_get_bios_year(void)
:   get a year out of DMI_BIOS_DATE field

**Parameters**

`void`
:   no arguments

**Description**

> Returns year on success, -ENXIO if DMI is not selected,
> or a different negative error code if DMI field is not present
> or not parseable.

int dmi_walk(void (\*decode)(const struct dmi_header\*, void\*), void \*private_data)
:   Walk the DMI table and get called back for every record

**Parameters**

`void (*decode)(const struct dmi_header *, void *)`
:   Callback function

`void *private_data`
:   Private data to be passed to the callback function

    Returns 0 on success, -ENXIO if DMI is not selected or not present,
    or a different negative error code if DMI walking fails.

bool dmi_match(enum dmi_field f, const char \*str)
:   compare a string to the dmi field (if exists)

**Parameters**

`enum dmi_field f`
:   DMI field identifier

`const char *str`
:   string to compare the DMI field to

**Description**

Returns true if the requested field equals to the str (including NULL).

u8 dmi_memdev_type(u16 handle)
:   get the memory type

**Parameters**

`u16 handle`
:   DMI structure handle

**Description**

Return the DMI memory type of the module in the slot associated with the
given DMI handle, or 0x0 if no such DMI handle exists.

u16 dmi_memdev_handle(int slot)
:   get the DMI handle of a memory slot

**Parameters**

`int slot`
:   slot number

    Return the DMI handle associated with a given memory slot, or `0xFFFF`
    if there is no such slot.

## EDD Interfaces

ssize_t edd_show_raw_data(struct edd_device \*edev, char \*buf)
:   copies raw data to buffer for userspace to parse

**Parameters**

`struct edd_device *edev`
:   target edd_device

`char *buf`
:   output buffer

**Return**

number of bytes written, or -EINVAL on failure

void edd_release(struct kobject \*kobj)
:   free edd structure

**Parameters**

`struct kobject * kobj`
:   kobject of edd structure

    This is called when the refcount of the edd structure
    reaches 0. This should happen right after we unregister,
    but just in case, we use the release callback anyway.

int edd_dev_is_type(struct edd_device \*edev, const char \*type)
:   is this EDD device a 'type' device?

**Parameters**

`struct edd_device *edev`
:   target edd_device

`const char *type`
:   a host bus or interface identifier string per the EDD spec

**Description**

Returns 1 (TRUE) if it is a 'type' device, 0 otherwise.

struct pci_dev \*edd_get_pci_dev(struct edd_device \*edev)
:   finds pci_dev that matches edev

**Parameters**

`struct edd_device *edev`
:   edd_device

**Description**

Returns pci_dev if found, or NULL

int edd_init(void)
:   creates sysfs tree of EDD data

**Parameters**

`void`
:   no arguments

## Generic System Framebuffers Interface

void sysfb_disable(void)
:   disable the Generic System Framebuffers support

**Parameters**

`void`
:   no arguments

**Description**

This disables the registration of system framebuffer devices that match the
generic drivers that make use of the system framebuffer set up by firmware.

It also unregisters a device if this was already registered by sysfb_init().

**Context**

The function can sleep. A **disable_lock** mutex is acquired to serialize
against sysfb_init(), that registers a system framebuffer device.

## Intel Stratix10 SoC Service Layer

Some features of the Intel Stratix10 SoC require a level of privilege
higher than the kernel is granted. Such secure features include
FPGA programming. In terms of the ARMv8 architecture, the kernel runs
at Exception Level 1 (EL1), access to the features requires
Exception Level 3 (EL3).

The Intel Stratix10 SoC service layer provides an in kernel API for
drivers to request access to the secure features. The requests are queued
and processed one by one. ARM’s SMCCC is used to pass the execution
of the requests on to a secure monitor (EL3).

enum stratix10_svc_command_code
:   supported service commands

**Constants**

`COMMAND_NOOP`
:   do 'dummy' request for integration/debug/trouble-shooting

`COMMAND_RECONFIG`
:   ask for FPGA configuration preparation, return status
    is SVC_STATUS_OK

`COMMAND_RECONFIG_DATA_SUBMIT`
:   submit buffer(s) of bit-stream data for the
    FPGA configuration, return status is SVC_STATUS_SUBMITTED or SVC_STATUS_ERROR

`COMMAND_RECONFIG_DATA_CLAIM`
:   check the status of the configuration, return
    status is SVC_STATUS_COMPLETED, or SVC_STATUS_BUSY, or SVC_STATUS_ERROR

`COMMAND_RECONFIG_STATUS`
:   check the status of the configuration, return
    status is SVC_STATUS_COMPLETED, or SVC_STATUS_BUSY, or SVC_STATUS_ERROR

`COMMAND_RSU_STATUS`
:   request remote system update boot log, return status
    is log data or SVC_STATUS_RSU_ERROR

`COMMAND_RSU_UPDATE`
:   set the offset of the bitstream to boot after reboot,
    return status is SVC_STATUS_OK or SVC_STATUS_ERROR

`COMMAND_RSU_NOTIFY`
:   report the status of hard processor system
    software to firmware, return status is SVC_STATUS_OK or
    SVC_STATUS_ERROR

`COMMAND_RSU_RETRY`
:   query firmware for the current image's retry counter,
    return status is SVC_STATUS_OK or SVC_STATUS_ERROR

`COMMAND_RSU_MAX_RETRY`
:   query firmware for the max retry value,
    return status is SVC_STATUS_OK or SVC_STATUS_ERROR

`COMMAND_RSU_DCMF_VERSION`
:   query firmware for the DCMF version, return status
    is SVC_STATUS_OK or SVC_STATUS_ERROR

`COMMAND_RSU_DCMF_STATUS`
:   query firmware for the DCMF status
    return status is SVC_STATUS_OK or SVC_STATUS_ERROR

`COMMAND_FIRMWARE_VERSION`
:   query running firmware version, return status
    is SVC_STATUS_OK or SVC_STATUS_ERROR

`COMMAND_FCS_REQUEST_SERVICE`
:   request validation of image from firmware,
    return status is SVC_STATUS_OK, SVC_STATUS_INVALID_PARAM

`COMMAND_FCS_SEND_CERTIFICATE`
:   send a certificate, return status is
    SVC_STATUS_OK, SVC_STATUS_INVALID_PARAM, SVC_STATUS_ERROR

`COMMAND_FCS_GET_PROVISION_DATA`
:   read the provisioning data, return status is
    SVC_STATUS_OK, SVC_STATUS_INVALID_PARAM, SVC_STATUS_ERROR

`COMMAND_FCS_DATA_ENCRYPTION`
:   encrypt the data, return status is
    SVC_STATUS_OK, SVC_STATUS_INVALID_PARAM, SVC_STATUS_ERROR

`COMMAND_FCS_DATA_DECRYPTION`
:   decrypt the data, return status is
    SVC_STATUS_OK, SVC_STATUS_INVALID_PARAM, SVC_STATUS_ERROR

`COMMAND_FCS_RANDOM_NUMBER_GEN`
:   generate a random number, return status
    is SVC_STATUS_OK, SVC_STATUS_ERROR

`COMMAND_POLL_SERVICE_STATUS`
:   poll if the service request is complete,
    return statis is SVC_STATUS_OK, SVC_STATUS_ERROR or SVC_STATUS_BUSY

`COMMAND_MBOX_SEND_CMD`
:   send generic mailbox command, return status is
    SVC_STATUS_OK or SVC_STATUS_ERROR

`COMMAND_SMC_SVC_VERSION`
:   Non-mailbox SMC SVC API Version,
    return status is SVC_STATUS_OK

struct stratix10_svc_client_msg
:   message sent by client to service

**Definition**:

```
struct stratix10_svc_client_msg {
    void *payload;
    size_t payload_length;
    void *payload_output;
    size_t payload_length_output;
    enum stratix10_svc_command_code command;
    u64 arg[3];
};
```

**Members**

`payload`
:   starting address of data need be processed

`payload_length`
:   to be processed data size in bytes

`payload_output`
:   starting address of processed data

`payload_length_output`
:   processed data size in bytes

`command`
:   service command

`arg`
:   args to be passed via registers and not physically mapped buffers

struct stratix10_svc_command_config_type
:   config type

**Definition**:

```
struct stratix10_svc_command_config_type {
    u32 flags;
};
```

**Members**

`flags`
:   flag bit for the type of FPGA configuration

struct stratix10_svc_cb_data
:   callback data structure from service layer

**Definition**:

```
struct stratix10_svc_cb_data {
    u32 status;
    void *kaddr1;
    void *kaddr2;
    void *kaddr3;
};
```

**Members**

`status`
:   the status of sent command

`kaddr1`
:   address of 1st completed data block

`kaddr2`
:   address of 2nd completed data block

`kaddr3`
:   address of 3rd completed data block

struct stratix10_svc_client
:   service client structure

**Definition**:

```
struct stratix10_svc_client {
    struct device *dev;
    void (*receive_cb)(struct stratix10_svc_client *client, struct stratix10_svc_cb_data *cb_data);
    void *priv;
};
```

**Members**

`dev`
:   the client device

`receive_cb`
:   callback to provide service client the received data

`priv`
:   client private data

struct stratix10_svc_chan \*stratix10_svc_request_channel_byname(struct [stratix10_svc_client](other_interfaces.md#c.stratix10_svc_client "stratix10_svc_client") \*client, const char \*name)
:   request a service channel

**Parameters**

`struct stratix10_svc_client *client`
:   pointer to service client

`const char *name`
:   service client name

**Description**

This function is used by service client to request a service channel.

**Return**

a pointer to channel assigned to the client on success,
or [`ERR_PTR()`](../../core-api/kernel-api.md#c.ERR_PTR "ERR_PTR") on error.

void stratix10_svc_free_channel(struct stratix10_svc_chan \*chan)
:   free service channel

**Parameters**

`struct stratix10_svc_chan *chan`
:   service channel to be freed

**Description**

This function is used by service client to free a service channel.

int stratix10_svc_send(struct stratix10_svc_chan \*chan, void \*msg)
:   send a message data to the remote

**Parameters**

`struct stratix10_svc_chan *chan`
:   service channel assigned to the client

`void *msg`
:   message data to be sent, in the format of
    "[`struct stratix10_svc_client_msg`](other_interfaces.md#c.stratix10_svc_client_msg "stratix10_svc_client_msg")"

**Description**

This function is used by service client to add a message to the service
layer driver's queue for being sent to the secure world.

**Return**

0 for success, -ENOMEM or -ENOBUFS on error.

void stratix10_svc_done(struct stratix10_svc_chan \*chan)
:   complete service request transactions

**Parameters**

`struct stratix10_svc_chan *chan`
:   service channel assigned to the client

**Description**

This function should be called when client has finished its request
or there is an error in the request process. It allows the service layer
to stop the running thread to have maximize savings in kernel resources.

void \*stratix10_svc_allocate_memory(struct stratix10_svc_chan \*chan, size_t size)
:   allocate memory

**Parameters**

`struct stratix10_svc_chan *chan`
:   service channel assigned to the client

`size_t size`
:   memory size requested by a specific service client

**Description**

Service layer allocates the requested number of bytes buffer from the
memory pool, service client uses this function to get allocated buffers.

**Return**

address of allocated memory on success, or [`ERR_PTR()`](../../core-api/kernel-api.md#c.ERR_PTR "ERR_PTR") on error.

void stratix10_svc_free_memory(struct stratix10_svc_chan \*chan, void \*kaddr)
:   free allocated memory

**Parameters**

`struct stratix10_svc_chan *chan`
:   service channel assigned to the client

`void *kaddr`
:   memory to be freed

**Description**

This function is used by service client to free allocated buffers.
