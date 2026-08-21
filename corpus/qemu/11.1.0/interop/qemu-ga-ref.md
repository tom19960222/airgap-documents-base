---
collection: qemu
version: "11.1.0"
title: "QEMU Guest Agent Protocol Reference"
source_url: https://www.qemu.org/docs/master/interop/qemu-ga-ref.html
fetched_at: 2026-08-21T03:22:18+00:00
---
# QEMU Guest Agent Protocol Reference

This manual describes the commands supported by the QEMU Guest Agent
Protocol.

For locating a particular item, please see the [QGA Index](../qapi-qga-index.md).

The following notation is used in examples:

> **Example::**
>
> ```QMP
> -> ... text sent by client (commands) ...
> <- ... text sent by server (command responses and events) ...
> ```

Example text is formatted for readability. However, in real
protocol usage, its commonly emitted as a single line.

Please refer to the
[QEMU Machine Protocol Specification](qmp-spec.md)
for the general format of commands, responses, and events.

*Command* guest-sync-delimited (Since: 1.1)
:   Echo back a unique integer value, and prepend to response a leading
    sentinel byte (0xFF) the client can check scan for.

    This is used by clients talking to the guest agent over the wire to
    ensure the stream is in sync and doesn’t contain stale data from
    previous client. It must be issued upon initial connection, and
    after any client-side timeouts (including timeouts on receiving a
    response to this command).

    After issuing this request, all guest agent responses should be
    ignored until the response containing the unique integer value the
    client passed in is returned. Receival of the 0xFF sentinel byte
    must be handled as an indication that the client’s
    lexer/tokenizer/parser state should be flushed/reset in preparation
    for reliably receiving the subsequent response. As an optimization,
    clients may opt to ignore all data until a sentinel value is
    receiving to avoid unnecessary processing of stale data.

    Similarly, clients should also precede this *request* with a 0xFF
    byte to make sure the guest agent flushes any partially read JSON
    data from a previous client connection.

    Arguments:
    :   - **id** (`int`) – randomly generated 64-bit integer

    Return:
    :   `int` – The unique integer id passed in by the client

*Command* guest-sync (Since: 0.15.0)
:   Echo back a unique integer value

    This is used by clients talking to the guest agent over the wire to
    ensure the stream is in sync and doesn’t contain stale data from
    previous client. All guest agent responses should be ignored until
    the provided unique integer value is returned, and it is up to the
    client to handle stale whole or partially-delivered JSON text in
    such a way that this response can be obtained.

    In cases where a partial stale response was previously received by
    the client, this cannot always be done reliably. One particular
    scenario being if qemu-ga responses are fed character-by-character
    into a JSON parser. In these situations, using
    [`guest-sync-delimited`](qemu-ga-ref.md#command-QGA-qapi-schema.guest-sync-delimited "QGA:qapi-schema.guest-sync-delimited") may be optimal.

    For clients that fetch responses line by line and convert them to
    JSON objects, [`guest-sync`](qemu-ga-ref.md#command-QGA-qapi-schema.guest-sync "QGA:qapi-schema.guest-sync") should be sufficient, but note that in
    cases where the channel is dirty some attempts at parsing the
    response may result in a parser error.

    Such clients should also precede this command with a 0xFF byte to
    make sure the guest agent flushes any partially read JSON data from
    a previous session.

    Arguments:
    :   - **id** (`int`) – randomly generated 64-bit integer

    Return:
    :   `int` – The unique integer id passed in by the client

*Command* guest-ping (Since: 0.15.0)
:   Ping the guest agent, a non-error return implies success

*Command* guest-get-time (Since: 1.5)
:   Get the information about guest’s System Time relative to the Epoch
    of 1970-01-01 in UTC.

    Return:
    :   `int` – Time in nanoseconds.

*Command* guest-set-time (Since: 1.5)
:   Set guest time.

    When a guest is paused or migrated to a file then loaded from that
    file, the guest OS has no idea that there was a big gap in the time.
    Depending on how long the gap was, NTP might not be able to
    resynchronize the guest.

    This command tries to set guest’s System Time to the given value,
    then sets the Hardware Clock (RTC) to the current System Time. This
    will make it easier for a guest to resynchronize without waiting for
    NTP. If no `time` is specified, then the time to set is read from
    RTC. However, this may not be supported on all platforms (i.e.
    Windows). If that’s the case users are advised to always pass a
    value.

    Arguments:
    :   - **time** (`int`, *optional*) – time of nanoseconds, relative to the Epoch of 1970-01-01 in
          UTC.

*Object* GuestAgentCommandInfo (Since: 1.1.0)
:   Information about guest agent commands.

    Members:
    :   - **name** (`string`) – name of the command
        - **enabled** (`boolean`) – whether command is currently enabled by guest admin
        - **success-response** (`boolean`) – whether command returns a response on success
          (since 1.7)

*Object* GuestAgentInfo (Since: 0.15.0)
:   Information about guest agent.

    Members:
    :   - **version** (`string`) – guest agent version
        - **supported_commands** (`[`[`GuestAgentCommandInfo`](qemu-ga-ref.md#object-QGA-qapi-schema.GuestAgentCommandInfo "QGA:qapi-schema.GuestAgentCommandInfo")`]`) – Information about guest agent commands

*Command* guest-info (Since: 0.15.0)
:   Get some information about the guest agent.

    Return:
    :   [`GuestAgentInfo`](qemu-ga-ref.md#object-QGA-qapi-schema.GuestAgentInfo "QGA:qapi-schema.GuestAgentInfo")

*Command* guest-shutdown (Since: 0.15.0)
:   Initiate guest-activated shutdown. Note: this is an asynchronous
    shutdown request, with no guarantee of successful shutdown.

    Arguments:
    :   - **mode** (`string`, *optional*) – “halt”, “powerdown” (default), or “reboot”

    This command does NOT return a response on success. Success
    condition is indicated by the VM exiting with a zero exit status or,
    when running with –no-shutdown, by issuing the [`query-status`](qemu-qmp-ref.md#command-QMP-run-state.query-status "QMP:run-state.query-status") QMP
    command to confirm the VM status is “shutdown”.

*Command* guest-file-open (Since: 0.15.0)
:   Open a file in the guest and retrieve a file handle for it

    Arguments:
    :   - **path** (`string`) – Full path to the file in the guest to open.
        - **mode** (`string`, *optional*) – open mode, as per fopen(), “r” is the default.

    Return:
    :   `int` – Guest file handle

*Command* guest-file-close (Since: 0.15.0)
:   Close an open file in the guest

    Arguments:
    :   - **handle** (`int`) – filehandle returned by [`guest-file-open`](qemu-ga-ref.md#command-QGA-qapi-schema.guest-file-open "QGA:qapi-schema.guest-file-open")

*Object* GuestFileRead (Since: 0.15.0)
:   Result of guest agent file-read operation

    Members:
    :   - **count** (`int`) – number of bytes read (note: count is *before*
          base64-encoding is applied)
        - **buf-b64** (`string`) – base64-encoded bytes read
        - **eof** (`boolean`) – whether EOF was encountered during read operation.

*Command* guest-file-read (Since: 0.15.0)
:   Read from an open file in the guest. Data will be base64-encoded.
    As this command is just for limited, ad-hoc debugging, such as log
    file access, the number of bytes to read is limited to 48 MB.

    Arguments:
    :   - **handle** (`int`) – filehandle returned by [`guest-file-open`](qemu-ga-ref.md#command-QGA-qapi-schema.guest-file-open "QGA:qapi-schema.guest-file-open")
        - **count** (`int`, *optional*) – maximum number of bytes to read (default is 4KB, maximum is
          48MB)

    Return:
    :   [`GuestFileRead`](qemu-ga-ref.md#object-QGA-qapi-schema.GuestFileRead "QGA:qapi-schema.GuestFileRead")

*Object* GuestFileWrite (Since: 0.15.0)
:   Result of guest agent file-write operation

    Members:
    :   - **count** (`int`) – number of bytes written (note: count is actual bytes
          written, after base64-decoding of provided buffer)
        - **eof** (`boolean`) – whether EOF was encountered during write operation.

*Command* guest-file-write (Since: 0.15.0)
:   Write to an open file in the guest.

    Arguments:
    :   - **handle** (`int`) – filehandle returned by [`guest-file-open`](qemu-ga-ref.md#command-QGA-qapi-schema.guest-file-open "QGA:qapi-schema.guest-file-open")
        - **buf-b64** (`string`) – base64-encoded string representing data to be written
        - **count** (`int`, *optional*) – bytes to write (actual bytes, after base64-decode), default
          is all content in buf-b64 buffer after base64 decoding

    Return:
    :   [`GuestFileWrite`](qemu-ga-ref.md#object-QGA-qapi-schema.GuestFileWrite "QGA:qapi-schema.GuestFileWrite")

*Object* GuestFileSeek (Since: 0.15.0)
:   Result of guest agent file-seek operation

    Members:
    :   - **position** (`int`) – current file position
        - **eof** (`boolean`) – whether EOF was encountered during file seek

*Enum* QGASeek (Since: 2.6)
:   Symbolic names for use in [`guest-file-seek`](qemu-ga-ref.md#command-QGA-qapi-schema.guest-file-seek "QGA:qapi-schema.guest-file-seek")

    Values:
    :   - **set** – Set to the specified offset (same effect as ‘whence’:0)
        - **cur** – Add offset to the current location (same effect as ‘whence’:1)
        - **end** – Add offset to the end of the file (same effect as ‘whence’:2)

*Alternate* GuestFileWhence (Since: 2.6)
:   Controls the meaning of offset to [`guest-file-seek`](qemu-ga-ref.md#command-QGA-qapi-schema.guest-file-seek "QGA:qapi-schema.guest-file-seek").

    Alternatives:
    :   - **value** (`int`) – Integral value (0 for set, 1 for cur, 2 for end), available
          for historical reasons, and might differ from the host’s or
          guest’s SEEK_\* values (since: 0.15)
        - **name** ([`QGASeek`](qemu-ga-ref.md#enum-QGA-qapi-schema.QGASeek "QGA:qapi-schema.QGASeek")) – Symbolic name, and preferred interface

*Command* guest-file-seek (Since: 0.15.0)
:   Seek to a position in the file, as with fseek(), and return the
    current file position afterward. Also encapsulates ftell()’s
    functionality, with offset=0 and whence=1.

    Arguments:
    :   - **handle** (`int`) – filehandle returned by [`guest-file-open`](qemu-ga-ref.md#command-QGA-qapi-schema.guest-file-open "QGA:qapi-schema.guest-file-open")
        - **offset** (`int`) – bytes to skip over in the file stream
        - **whence** ([`GuestFileWhence`](qemu-ga-ref.md#alternate-QGA-qapi-schema.GuestFileWhence "QGA:qapi-schema.GuestFileWhence")) – Symbolic or numeric code for interpreting offset

    Return:
    :   [`GuestFileSeek`](qemu-ga-ref.md#object-QGA-qapi-schema.GuestFileSeek "QGA:qapi-schema.GuestFileSeek")

*Command* guest-file-flush (Since: 0.15.0)
:   Write file changes buffered in userspace to disk/kernel buffers

    Arguments:
    :   - **handle** (`int`) – filehandle returned by [`guest-file-open`](qemu-ga-ref.md#command-QGA-qapi-schema.guest-file-open "QGA:qapi-schema.guest-file-open")

*Enum* GuestFsfreezeStatus (Since: 0.15.0)
:   *Availability*: `CONFIG_WIN32 or CONFIG_FSFREEZE`

    An enumeration of filesystem freeze states

    Values:
    :   - **thawed** – filesystems thawed/unfrozen
        - **frozen** – all non-network guest filesystems frozen

*Command* guest-fsfreeze-status (Since: 0.15.0)
:   *Availability*: `CONFIG_WIN32 or CONFIG_FSFREEZE`

    Get guest fsfreeze state.

    > **Note:**
    >
    > This may fail to properly report the current state as a
    > result of some other guest processes having issued an fs
    > freeze/thaw.

    Return:
    :   [`GuestFsfreezeStatus`](qemu-ga-ref.md#enum-QGA-qapi-schema.GuestFsfreezeStatus "QGA:qapi-schema.GuestFsfreezeStatus")

*Command* guest-fsfreeze-freeze (Since: 0.15.0)
:   *Availability*: `CONFIG_WIN32 or CONFIG_FSFREEZE`

    Sync and freeze all freezable, local guest filesystems. If this
    command succeeded, you may call [`guest-fsfreeze-thaw`](qemu-ga-ref.md#command-QGA-qapi-schema.guest-fsfreeze-thaw "QGA:qapi-schema.guest-fsfreeze-thaw") later to
    unfreeze.

    On error, all filesystems will be thawed. If no filesystems are
    frozen as a result of this call, then [`guest-fsfreeze-status`](qemu-ga-ref.md#command-QGA-qapi-schema.guest-fsfreeze-status "QGA:qapi-schema.guest-fsfreeze-status") will
    remain “thawed” and calling [`guest-fsfreeze-thaw`](qemu-ga-ref.md#command-QGA-qapi-schema.guest-fsfreeze-thaw "QGA:qapi-schema.guest-fsfreeze-thaw") is not necessary.

    Return:
    :   `int` – Number of file systems currently frozen.

    > **Note:**
    >
    > On Windows, the command is implemented with the help of a
    > Volume Shadow-copy Service DLL helper. The frozen state is
    > limited for up to 10 seconds by VSS.

*Command* guest-fsfreeze-freeze-list (Since: 2.2)
:   *Availability*: `CONFIG_WIN32 or CONFIG_FSFREEZE`

    Sync and freeze specified guest filesystems. See also
    [`guest-fsfreeze-freeze`](qemu-ga-ref.md#command-QGA-qapi-schema.guest-fsfreeze-freeze "QGA:qapi-schema.guest-fsfreeze-freeze").

    On error, all filesystems will be thawed.

    Arguments:
    :   - **mountpoints** (`[``string``]`, *optional*) – an array of mountpoints of filesystems to be frozen.
          If omitted, every mounted filesystem is frozen. Invalid mount
          points are ignored.

    Return:
    :   `int` – Number of file systems currently frozen.

*Command* guest-fsfreeze-thaw (Since: 0.15.0)
:   *Availability*: `CONFIG_WIN32 or CONFIG_FSFREEZE`

    Unfreeze all frozen guest filesystems

    Return:
    :   `int` – Number of file systems thawed by this call

    > **Note:**
    >
    > If the return value does not match the previous call to
    > [`guest-fsfreeze-freeze`](qemu-ga-ref.md#command-QGA-qapi-schema.guest-fsfreeze-freeze "QGA:qapi-schema.guest-fsfreeze-freeze"), this likely means some freezable
    > filesystems were unfrozen before this call, and that the
    > filesystem state may have changed before issuing this command.

*Object* GuestFilesystemTrimResult (Since: 2.4)
:   *Availability*: `CONFIG_WIN32 or CONFIG_FSTRIM`

    Members:
    :   - **path** (`string`) – path that was trimmed
        - **error** (`string`, *optional*) – an error message when trim failed
        - **trimmed** (`int`, *optional*) – bytes trimmed for this path
        - **minimum** (`int`, *optional*) – reported effective minimum for this path

*Object* GuestFilesystemTrimResponse (Since: 2.4)
:   *Availability*: `CONFIG_WIN32 or CONFIG_FSTRIM`

    Members:
    :   - **paths** (`[`[`GuestFilesystemTrimResult`](qemu-ga-ref.md#object-QGA-qapi-schema.GuestFilesystemTrimResult "QGA:qapi-schema.GuestFilesystemTrimResult")`]`) – list of [`GuestFilesystemTrimResult`](qemu-ga-ref.md#object-QGA-qapi-schema.GuestFilesystemTrimResult "QGA:qapi-schema.GuestFilesystemTrimResult") per path that was
          trimmed

*Command* guest-fstrim (Since: 1.2)
:   *Availability*: `CONFIG_WIN32 or CONFIG_FSTRIM`

    Discard (or “trim”) blocks which are not in use by the filesystem.

    Arguments:
    :   - **minimum** (`int`, *optional*) – Minimum contiguous free range to discard, in bytes. Free
          ranges smaller than this may be ignored (this is a hint and the
          guest may not respect it). By increasing this value, the fstrim
          operation will complete more quickly for filesystems with badly
          fragmented free space, although not all blocks will be
          discarded. The default value is zero, meaning “discard every
          free block”.

    Return:
    :   [`GuestFilesystemTrimResponse`](qemu-ga-ref.md#object-QGA-qapi-schema.GuestFilesystemTrimResponse "QGA:qapi-schema.GuestFilesystemTrimResponse") – status of all trimmed paths. (since 2.4)

*Command* guest-suspend-disk (Since: 1.1)
:   *Availability*: `CONFIG_LINUX or CONFIG_WIN32`

    Suspend guest to disk.

    This command attempts to suspend the guest using three strategies,
    in this order:

    - systemd hibernate
    - pm-utils (via pm-hibernate)
    - manual write into sysfs

    This command does NOT return a response on success. There is a high
    chance the command succeeded if the VM exits with a zero exit status
    or, when running with –no-shutdown, by issuing the [`query-status`](qemu-qmp-ref.md#command-QMP-run-state.query-status "QMP:run-state.query-status")
    QMP command to to confirm the VM status is “shutdown”. However, the
    VM could also exit (or set its status to “shutdown”) due to other
    reasons.

    Errors:
    :   - If suspend to disk is not supported, Unsupported

    > **Note:**
    >
    > It’s strongly recommended to issue the [`guest-sync`](qemu-ga-ref.md#command-QGA-qapi-schema.guest-sync "QGA:qapi-schema.guest-sync")
    > command before sending commands when the guest resumes.

*Command* guest-suspend-ram (Since: 1.1)
:   *Availability*: `CONFIG_LINUX or CONFIG_WIN32`

    Suspend guest to ram.

    This command attempts to suspend the guest using three strategies,
    in this order:

    - systemd hibernate
    - pm-utils (via pm-hibernate)
    - manual write into sysfs

    IMPORTANT: [`guest-suspend-ram`](qemu-ga-ref.md#command-QGA-qapi-schema.guest-suspend-ram "QGA:qapi-schema.guest-suspend-ram") requires working wakeup support in
    QEMU. You should check QMP command [`query-current-machine`](qemu-qmp-ref.md#command-QMP-machine.query-current-machine "QMP:machine.query-current-machine") returns
    wakeup-suspend-support: true before issuing this command. Failure
    in doing so can result in a suspended guest that QEMU will not be
    able to awaken, forcing the user to power cycle the guest to bring
    it back.

    This command does NOT return a response on success. There are two
    options to check for success:

    1. Wait for the [`SUSPEND`](qemu-qmp-ref.md#event-QMP-run-state.SUSPEND "QMP:run-state.SUSPEND") QMP event from QEMU
    2. Issue the [`query-status`](qemu-qmp-ref.md#command-QMP-run-state.query-status "QMP:run-state.query-status") QMP command to confirm the VM status is
       “suspended”

    Errors:
    :   - If suspend to ram is not supported, Unsupported

    > **Note:**
    >
    > It’s strongly recommended to issue the [`guest-sync`](qemu-ga-ref.md#command-QGA-qapi-schema.guest-sync "QGA:qapi-schema.guest-sync")
    > command before sending commands when the guest resumes.

*Command* guest-suspend-hybrid (Since: 1.1)
:   *Availability*: `CONFIG_LINUX`

    Save guest state to disk and suspend to ram.

    This command attempts to suspend the guest by executing, in this
    order:

    - systemd hybrid-sleep
    - pm-utils (via pm-suspend-hybrid)

    IMPORTANT: [`guest-suspend-hybrid`](qemu-ga-ref.md#command-QGA-qapi-schema.guest-suspend-hybrid "QGA:qapi-schema.guest-suspend-hybrid") requires working wakeup support in
    QEMU. You should check QMP command [`query-current-machine`](qemu-qmp-ref.md#command-QMP-machine.query-current-machine "QMP:machine.query-current-machine") returns
    wakeup-suspend-support: true before issuing this command. Failure
    in doing so can result in a suspended guest that QEMU will not be
    able to awaken, forcing the user to power cycle the guest to bring
    it back.

    This command does NOT return a response on success. There are two
    options to check for success:

    1. Wait for the [`SUSPEND`](qemu-qmp-ref.md#event-QMP-run-state.SUSPEND "QMP:run-state.SUSPEND") QMP event from QEMU
    2. Issue the [`query-status`](qemu-qmp-ref.md#command-QMP-run-state.query-status "QMP:run-state.query-status") QMP command to confirm the VM status is
       “suspended”

    Errors:
    :   - If hybrid suspend is not supported, Unsupported

    > **Note:**
    >
    > It’s strongly recommended to issue the [`guest-sync`](qemu-ga-ref.md#command-QGA-qapi-schema.guest-sync "QGA:qapi-schema.guest-sync")
    > command before sending commands when the guest resumes.

*Enum* GuestIpAddressType (Since: 1.1)
:   *Availability*: `CONFIG_WIN32 or HAVE_GETIFADDRS`

    An enumeration of supported IP address types

    Values:
    :   - **ipv4** – IP version 4
        - **ipv6** – IP version 6

*Object* GuestIpAddress (Since: 1.1)
:   *Availability*: `CONFIG_WIN32 or HAVE_GETIFADDRS`

    Members:
    :   - **ip-address** (`string`) – IP address
        - **ip-address-type** ([`GuestIpAddressType`](qemu-ga-ref.md#enum-QGA-qapi-schema.GuestIpAddressType "QGA:qapi-schema.GuestIpAddressType")) – Type of `ip-address` (e.g. ipv4, ipv6)
        - **prefix** (`int`) – Network prefix length of `ip-address`

*Object* GuestNetworkInterfaceStat (Since: 2.11)
:   *Availability*: `CONFIG_WIN32 or HAVE_GETIFADDRS`

    Members:
    :   - **rx-bytes** (`int`) – total bytes received
        - **rx-packets** (`int`) – total packets received
        - **rx-errs** (`int`) – bad packets received
        - **rx-dropped** (`int`) – receiver dropped packets
        - **tx-bytes** (`int`) – total bytes transmitted
        - **tx-packets** (`int`) – total packets transmitted
        - **tx-errs** (`int`) – packet transmit problems
        - **tx-dropped** (`int`) – dropped packets transmitted

*Object* GuestNetworkInterface (Since: 1.1)
:   *Availability*: `CONFIG_WIN32 or HAVE_GETIFADDRS`

    Members:
    :   - **name** (`string`) – The name of interface for which info are being delivered
        - **hardware-address** (`string`, *optional*) – Hardware address of `name`
        - **ip-addresses** (`[`[`GuestIpAddress`](qemu-ga-ref.md#object-QGA-qapi-schema.GuestIpAddress "QGA:qapi-schema.GuestIpAddress")`]`, *optional*) – List of addresses assigned to `name`
        - **statistics** ([`GuestNetworkInterfaceStat`](qemu-ga-ref.md#object-QGA-qapi-schema.GuestNetworkInterfaceStat "QGA:qapi-schema.GuestNetworkInterfaceStat"), *optional*) – various statistic counters related to `name` (since
          2.11)

*Command* guest-network-get-interfaces (Since: 1.1)
:   *Availability*: `CONFIG_WIN32 or HAVE_GETIFADDRS`

    Get list of guest IP addresses, MAC addresses and netmasks.

    Return:
    :   `[`[`GuestNetworkInterface`](qemu-ga-ref.md#object-QGA-qapi-schema.GuestNetworkInterface "QGA:qapi-schema.GuestNetworkInterface")`]`

*Object* GuestLogicalProcessor (Since: 1.5)
:   *Availability*: `CONFIG_LINUX or CONFIG_WIN32`

    Members:
    :   - **logical-id** (`int`) – Arbitrary guest-specific unique identifier of the VCPU.
        - **online** (`boolean`) – Whether the VCPU is enabled.
        - **can-offline** (`boolean`, *optional*) – Whether offlining the VCPU is possible. This member
          is always filled in by the guest agent when the structure is
          returned, and always ignored on input (hence it can be omitted
          then).

*Command* guest-get-vcpus (Since: 1.5)
:   *Availability*: `CONFIG_LINUX or CONFIG_WIN32`

    Retrieve the list of the guest’s logical processors.

    This is a read-only operation.

    Return:
    :   `[`[`GuestLogicalProcessor`](qemu-ga-ref.md#object-QGA-qapi-schema.GuestLogicalProcessor "QGA:qapi-schema.GuestLogicalProcessor")`]` – The list of all VCPUs the guest knows about. Each VCPU is
        put on the list exactly once, but their order is unspecified.

*Command* guest-set-vcpus (Since: 1.5)
:   *Availability*: `CONFIG_LINUX`

    Attempt to reconfigure (currently: enable/disable) logical
    processors inside the guest.

    Arguments:
    :   - **vcpus** (`[`[`GuestLogicalProcessor`](qemu-ga-ref.md#object-QGA-qapi-schema.GuestLogicalProcessor "QGA:qapi-schema.GuestLogicalProcessor")`]`) – The logical processors to be reconfigured. This list is
          processed node by node in order. In each node `logical-id` is
          used to look up the guest VCPU, for which `online` specifies the
          requested state. The set of distinct `logical-id`’s is only
          required to be a subset of the guest-supported identifiers.
          There’s no restriction on list length or on repeating the same
          `logical-id` (with possibly different `online` field). Preferably
          the input list should describe a modified subset of
          [`guest-get-vcpus`](qemu-ga-ref.md#command-QGA-qapi-schema.guest-get-vcpus "QGA:qapi-schema.guest-get-vcpus")’ return value.

    Return:
    :   `int` –

        The length of the initial sublist that has been
        successfully processed. The guest agent maximizes this value.
        Possible cases:

        - 0:
          if the `vcpus` list was empty on input. Guest state has not
          been changed. Otherwise,
        - < length(`vcpus`):
          more than zero initial nodes have been processed, but not the
          entire `vcpus` list. Guest state has changed accordingly. To
          retrieve the error (assuming it persists), repeat the call
          with the successfully processed initial sublist removed.
          Otherwise,
        - length(`vcpus`):
          call successful.

    Errors:
    :   - If the reconfiguration of the first node in `vcpus` failed.
          Guest state has not been changed.

*Enum* GuestDiskBusType (Since: 2.2; 'Unknown' and all entries below since 2.4)
:   *Availability*: `CONFIG_WIN32 or CONFIG_LINUX`

    An enumeration of bus type of disks

    Values:
    :   - **ide** – IDE disks
        - **fdc** – floppy disks
        - **scsi** – SCSI disks
        - **virtio** – virtio disks
        - **xen** – Xen disks
        - **usb** – USB disks
        - **uml** – UML disks
        - **sata** – SATA disks
        - **sd** – SD cards
        - **unknown** – Unknown bus type
        - **ieee1394** – Win IEEE 1394 bus type
        - **ssa** – Win SSA bus type
        - **fibre** – Win fiber channel bus type
        - **raid** – Win RAID bus type
        - **iscsi** – Win iScsi bus type
        - **sas** – Win serial-attaches SCSI bus type
        - **mmc** – Win multimedia card (MMC) bus type
        - **virtual** – Win virtual bus type
        - **file-backed-virtual** – Win file-backed bus type
        - **nvme** – NVMe disks (since 7.1)

*Object* GuestPCIAddress (Since: 2.2)
:   *Availability*: `CONFIG_WIN32 or CONFIG_LINUX`

    Members:
    :   - **domain** (`int`) – domain id
        - **bus** (`int`) – bus id
        - **slot** (`int`) – slot id
        - **function** (`int`) – function id

*Object* GuestCCWAddress (Since: 6.0)
:   *Availability*: `CONFIG_WIN32 or CONFIG_LINUX`

    Members:
    :   - **cssid** (`int`) – channel subsystem image id
        - **ssid** (`int`) – subchannel set id
        - **subchno** (`int`) – subchannel number
        - **devno** (`int`) – device number

*Object* GuestDiskAddress (Since: 2.2)
:   *Availability*: `CONFIG_WIN32 or CONFIG_LINUX`

    Members:
    :   - **pci-controller** ([`GuestPCIAddress`](qemu-ga-ref.md#object-QGA-qapi-schema.GuestPCIAddress "QGA:qapi-schema.GuestPCIAddress")) – controller’s PCI address (fields are set to -1 if
          invalid)
        - **bus-type** ([`GuestDiskBusType`](qemu-ga-ref.md#enum-QGA-qapi-schema.GuestDiskBusType "QGA:qapi-schema.GuestDiskBusType")) – bus type
        - **bus** (`int`) – bus id
        - **target** (`int`) – target id
        - **unit** (`int`) – unit id
        - **serial** (`string`, *optional*) – serial number (since: 3.1)
        - **dev** (`string`, *optional*) – device node (POSIX) or device UNC (Windows) (since: 3.1)
        - **ccw-address** ([`GuestCCWAddress`](qemu-ga-ref.md#object-QGA-qapi-schema.GuestCCWAddress "QGA:qapi-schema.GuestCCWAddress"), *optional*) – CCW address on s390x (since: 6.0)

*Object* GuestNVMeSmart (Since: 7.1)
:   *Availability*: `CONFIG_WIN32 or CONFIG_LIBUDEV`

    NVMe smart information, based on NVMe specification, section
    <SMART / Health Information (Log Identifier 02h)>

    Members:
    :   - **critical-warning** (`int`) – Not documented
        - **temperature** (`int`) – Not documented
        - **available-spare** (`int`) – Not documented
        - **available-spare-threshold** (`int`) – Not documented
        - **percentage-used** (`int`) – Not documented
        - **data-units-read-lo** (`int`) – Not documented
        - **data-units-read-hi** (`int`) – Not documented
        - **data-units-written-lo** (`int`) – Not documented
        - **data-units-written-hi** (`int`) – Not documented
        - **host-read-commands-lo** (`int`) – Not documented
        - **host-read-commands-hi** (`int`) – Not documented
        - **host-write-commands-lo** (`int`) – Not documented
        - **host-write-commands-hi** (`int`) – Not documented
        - **controller-busy-time-lo** (`int`) – Not documented
        - **controller-busy-time-hi** (`int`) – Not documented
        - **power-cycles-lo** (`int`) – Not documented
        - **power-cycles-hi** (`int`) – Not documented
        - **power-on-hours-lo** (`int`) – Not documented
        - **power-on-hours-hi** (`int`) – Not documented
        - **unsafe-shutdowns-lo** (`int`) – Not documented
        - **unsafe-shutdowns-hi** (`int`) – Not documented
        - **media-errors-lo** (`int`) – Not documented
        - **media-errors-hi** (`int`) – Not documented
        - **number-of-error-log-entries-lo** (`int`) – Not documented
        - **number-of-error-log-entries-hi** (`int`) – Not documented

*Object* GuestDiskSmart (Since: 7.1)
:   *Availability*: `CONFIG_WIN32 or CONFIG_LIBUDEV`

    Disk type related smart information.

    Members:
    :   - **type** ([`GuestDiskBusType`](qemu-ga-ref.md#enum-QGA-qapi-schema.GuestDiskBusType "QGA:qapi-schema.GuestDiskBusType")) – disk bus type
        - When `type` is `nvme`: The members of [`GuestNVMeSmart`](qemu-ga-ref.md#object-QGA-qapi-schema.GuestNVMeSmart "QGA:qapi-schema.GuestNVMeSmart").

*Object* GuestDiskInfo (Since: 5.2)
:   *Availability*: `CONFIG_WIN32 or CONFIG_LIBUDEV`

    Members:
    :   - **name** (`string`) – device node (Linux) or device UNC (Windows)
        - **partition** (`boolean`) – whether this is a partition or disk
        - **dependencies** (`[``string``]`, *optional*) – list of device dependencies; e.g. for LVs of the LVM
          this will hold the list of PVs, for LUKS encrypted volume this
          will contain the disk where the volume is placed. (Linux)
        - **address** ([`GuestDiskAddress`](qemu-ga-ref.md#object-QGA-qapi-schema.GuestDiskAddress "QGA:qapi-schema.GuestDiskAddress"), *optional*) – disk address information (only for non-virtual devices)
        - **alias** (`string`, *optional*) – optional alias assigned to the disk, on Linux this is a name
          assigned by device mapper
        - **smart** ([`GuestDiskSmart`](qemu-ga-ref.md#object-QGA-qapi-schema.GuestDiskSmart "QGA:qapi-schema.GuestDiskSmart"), *optional*) – disk smart information (Since 7.1)

*Command* guest-get-disks (Since: 5.2)
:   *Availability*: `CONFIG_WIN32 or CONFIG_LIBUDEV`

    Return:
    :   `[`[`GuestDiskInfo`](qemu-ga-ref.md#object-QGA-qapi-schema.GuestDiskInfo "QGA:qapi-schema.GuestDiskInfo")`]` – The list of disks in the guest. For Windows these are only
        the physical disks. On Linux these are all root block devices
        of non-zero size including e.g. removable devices, loop devices,
        NBD, etc.

*Object* GuestFilesystemInfo (Since: 2.2)
:   *Availability*: `CONFIG_WIN32 or CONFIG_LINUX`

    Members:
    :   - **name** (`string`) – disk name
        - **mountpoint** (`string`) – mount point path
        - **type** (`string`) – file system type string
        - **used-bytes** (`int`, *optional*) – file system used bytes (since 3.0)
        - **total-bytes** (`int`, *optional*) – filesystem capacity in bytes for unprivileged users
          (since 3.0)
        - **total-bytes-privileged** (`int`, *optional*) – filesystem capacity in bytes for privileged
          users (since 9.1)
        - **disk** (`[`[`GuestDiskAddress`](qemu-ga-ref.md#object-QGA-qapi-schema.GuestDiskAddress "QGA:qapi-schema.GuestDiskAddress")`]`) – an array of disk hardware information that the volume lies
          on, which may be empty if the disk type is not supported

*Command* guest-get-fsinfo (Since: 2.2)
:   *Availability*: `CONFIG_WIN32 or CONFIG_LINUX`

    Return:
    :   `[`[`GuestFilesystemInfo`](qemu-ga-ref.md#object-QGA-qapi-schema.GuestFilesystemInfo "QGA:qapi-schema.GuestFilesystemInfo")`]` – The list of filesystems information mounted in the guest.
        The returned mountpoints may be specified to
        [`guest-fsfreeze-freeze-list`](qemu-ga-ref.md#command-QGA-qapi-schema.guest-fsfreeze-freeze-list "QGA:qapi-schema.guest-fsfreeze-freeze-list"). Network filesystems (such as CIFS
        and NFS) are not listed.

*Command* guest-set-user-password (Since: 2.3)
:   *Availability*: `CONFIG_WIN32 or CONFIG_LINUX or CONFIG_FREEBSD`

    Arguments:
    :   - **username** (`string`) – the user account whose password to change
        - **password** (`string`) – the new password entry string, base64 encoded
        - **crypted** (`boolean`) – true if password is already crypt()d, false if raw

    If the `crypted` flag is true, it is the caller’s responsibility to
    ensure the correct crypt() encryption scheme is used. This command
    does not attempt to interpret or report on the encryption scheme.
    Refer to the documentation of the guest operating system in question
    to determine what is supported.

    Not all guest operating systems will support use of the `crypted`
    flag, as they may require the clear-text password

    The `password` parameter must always be base64 encoded before
    transmission, even if already crypt()d, to ensure it is 8-bit safe
    when passed as JSON.

*Object* GuestMemoryBlock (Since: 2.3)
:   *Availability*: `CONFIG_LINUX`

    Members:
    :   - **phys-index** (`int`) – Arbitrary guest-specific unique identifier of the
          MEMORY BLOCK.
        - **online** (`boolean`) – Whether the MEMORY BLOCK is enabled in guest.
        - **can-offline** (`boolean`, *optional*) – Whether offlining the MEMORY BLOCK is possible. This
          member is always filled in by the guest agent when the structure
          is returned, and always ignored on input (hence it can be
          omitted then).

*Command* guest-get-memory-blocks (Since: 2.3)
:   *Availability*: `CONFIG_LINUX`

    Retrieve the list of the guest’s memory blocks.

    This is a read-only operation.

    Return:
    :   `[`[`GuestMemoryBlock`](qemu-ga-ref.md#object-QGA-qapi-schema.GuestMemoryBlock "QGA:qapi-schema.GuestMemoryBlock")`]` – The list of all memory blocks the guest knows about. Each
        memory block is put on the list exactly once, but their order is
        unspecified.

*Enum* GuestMemoryBlockResponseType (Since: 2.3)
:   *Availability*: `CONFIG_LINUX`

    An enumeration of memory block operation result.

    Values:
    :   - **success** – the operation of online/offline memory block is
          successful.
        - **not-found** – can’t find the corresponding memoryXXX directory in
          sysfs.
        - **operation-not-supported** – for some old kernels, it does not support
          online or offline memory block.
        - **operation-failed** – the operation of online/offline memory block
          fails, because of some errors happen.

*Object* GuestMemoryBlockResponse (Since: 2.3)
:   *Availability*: `CONFIG_LINUX`

    Members:
    :   - **phys-index** (`int`) – same with the ‘phys-index’ member of
          [`GuestMemoryBlock`](qemu-ga-ref.md#object-QGA-qapi-schema.GuestMemoryBlock "QGA:qapi-schema.GuestMemoryBlock").
        - **response** ([`GuestMemoryBlockResponseType`](qemu-ga-ref.md#enum-QGA-qapi-schema.GuestMemoryBlockResponseType "QGA:qapi-schema.GuestMemoryBlockResponseType")) – the result of memory block operation.
        - **error-code** (`int`, *optional*) – the error number. When memory block operation fails,
          we assign the value of ‘errno’ to this member, it indicates what
          goes wrong. When the operation succeeds, it will be omitted.

*Command* guest-set-memory-blocks (Since: 2.3)
:   *Availability*: `CONFIG_LINUX`

    Attempt to reconfigure (currently: enable/disable) state of memory
    blocks inside the guest.

    Arguments:
    :   - **mem-blks** (`[`[`GuestMemoryBlock`](qemu-ga-ref.md#object-QGA-qapi-schema.GuestMemoryBlock "QGA:qapi-schema.GuestMemoryBlock")`]`) – The memory blocks to be reconfigured. This list is
          processed node by node in order. In each node `phys-index` is
          used to look up the guest MEMORY BLOCK, for which `online`
          specifies the requested state. The set of distinct
          `phys-index`’s is only required to be a subset of the
          guest-supported identifiers. There’s no restriction on list
          length or on repeating the same `phys-index` (with possibly
          different `online` field). Preferably the input list should
          describe a modified subset of [`guest-get-memory-blocks`](qemu-ga-ref.md#command-QGA-qapi-schema.guest-get-memory-blocks "QGA:qapi-schema.guest-get-memory-blocks")’ return
          value.

    Return:
    :   `[`[`GuestMemoryBlockResponse`](qemu-ga-ref.md#object-QGA-qapi-schema.GuestMemoryBlockResponse "QGA:qapi-schema.GuestMemoryBlockResponse")`]` –

        The operation results, it is a list of
        [`GuestMemoryBlockResponse`](qemu-ga-ref.md#object-QGA-qapi-schema.GuestMemoryBlockResponse "QGA:qapi-schema.GuestMemoryBlockResponse"), which is corresponding to the input
        list.

        Note: it will return an empty list if the `mem-blks` list was
        empty on input, or there is an error, and in this case, guest
        state will not be changed.

*Object* GuestMemoryBlockInfo (Since: 2.3)
:   *Availability*: `CONFIG_LINUX`

    Members:
    :   - **size** (`int`) – the size (in bytes) of the guest memory blocks, which are the
          minimal units of memory block online/offline operations (also
          called Logical Memory Hotplug).

*Command* guest-get-memory-block-info (Since: 2.3)
:   *Availability*: `CONFIG_LINUX`

    Get information relating to guest memory blocks.

    Return:
    :   [`GuestMemoryBlockInfo`](qemu-ga-ref.md#object-QGA-qapi-schema.GuestMemoryBlockInfo "QGA:qapi-schema.GuestMemoryBlockInfo")

*Object* GuestExecStatus (Since: 2.5)
:   Members:
    :   - **exited** (`boolean`) – true if process has already terminated.
        - **exitcode** (`int`, *optional*) – process exit code if it was normally terminated.
        - **signal** (`int`, *optional*) – signal number (linux) or unhandled exception code (windows)
          if the process was abnormally terminated.
        - **out-data** (`string`, *optional*) – base64-encoded stdout of the process. This field will
          only be populated after the process exits.
        - **err-data** (`string`, *optional*) – base64-encoded stderr of the process. Note: `out-data`
          and `err-data` are present only if ‘capture-output’ was specified
          for [`guest-exec`](qemu-ga-ref.md#command-QGA-qapi-schema.guest-exec "QGA:qapi-schema.guest-exec"). This field will only be populated after the
          process exits.
        - **out-truncated** (`boolean`, *optional*) – true if stdout was not fully captured due to size
          limitation.
        - **err-truncated** (`boolean`, *optional*) – true if stderr was not fully captured due to size
          limitation.

*Command* guest-exec-status (Since: 2.5)
:   Check status of process associated with PID retrieved via
    [`guest-exec`](qemu-ga-ref.md#command-QGA-qapi-schema.guest-exec "QGA:qapi-schema.guest-exec"). Reap the process and associated metadata if it has
    exited.

    Arguments:
    :   - **pid** (`int`) – pid returned from [`guest-exec`](qemu-ga-ref.md#command-QGA-qapi-schema.guest-exec "QGA:qapi-schema.guest-exec")

    Return:
    :   [`GuestExecStatus`](qemu-ga-ref.md#object-QGA-qapi-schema.GuestExecStatus "QGA:qapi-schema.GuestExecStatus")

*Object* GuestExec (Since: 2.5)
:   Members:
    :   - **pid** (`int`) – pid of child process in guest OS

*Enum* GuestExecCaptureOutputMode (Since: 8.0)
:   An enumeration of [`guest-exec`](qemu-ga-ref.md#command-QGA-qapi-schema.guest-exec "QGA:qapi-schema.guest-exec") capture modes.

    Values:
    :   - **none** – do not capture any output
        - **stdout** – only capture stdout
        - **stderr** – only capture stderr
        - **separated** – capture both stdout and stderr, but separated into
          [`GuestExecStatus`](qemu-ga-ref.md#object-QGA-qapi-schema.GuestExecStatus "QGA:qapi-schema.GuestExecStatus") out-data and err-data, respectively
        - **merged** – capture both stdout and stderr, but merge together into
          out-data. Not effective on windows guests.

*Alternate* GuestExecCaptureOutput (Since: 8.0)
:   Controls what [`guest-exec`](qemu-ga-ref.md#command-QGA-qapi-schema.guest-exec "QGA:qapi-schema.guest-exec") output gets captures.

    Alternatives:
    :   - **flag** (`boolean`) – captures both stdout and stderr if true. Equivalent to
          [`GuestExecCaptureOutputMode`](qemu-ga-ref.md#enum-QGA-qapi-schema.GuestExecCaptureOutputMode "QGA:qapi-schema.GuestExecCaptureOutputMode")::all. (since 2.5)
        - **mode** ([`GuestExecCaptureOutputMode`](qemu-ga-ref.md#enum-QGA-qapi-schema.GuestExecCaptureOutputMode "QGA:qapi-schema.GuestExecCaptureOutputMode")) – capture mode; preferred interface

*Command* guest-exec (Since: 2.5)
:   Execute a command in the guest

    Arguments:
    :   - **path** (`string`) – path or executable name to execute
        - **arg** (`[``string``]`, *optional*) – argument list to pass to executable
        - **env** (`[``string``]`, *optional*) – environment variables to pass to executable
        - **input-data** (`string`, *optional*) – data to be passed to process stdin (base64 encoded)
        - **capture-output** ([`GuestExecCaptureOutput`](qemu-ga-ref.md#alternate-QGA-qapi-schema.GuestExecCaptureOutput "QGA:qapi-schema.GuestExecCaptureOutput"), *optional*) – bool flag to enable capture of stdout/stderr of
          running process. Defaults to false.

    Return:
    :   [`GuestExec`](qemu-ga-ref.md#object-QGA-qapi-schema.GuestExec "QGA:qapi-schema.GuestExec") – PID

*Object* GuestHostName (Since: 2.10)
:   Members:
    :   - **host-name** (`string`) – Fully qualified domain name of the guest OS

*Command* guest-get-host-name (Since: 2.10)
:   Return a name for the machine.

    The returned name is not necessarily a fully-qualified domain name,
    or even present in DNS or some other name service at all. It need
    not even be unique on your local network or site, but usually it is.

    Return:
    :   [`GuestHostName`](qemu-ga-ref.md#object-QGA-qapi-schema.GuestHostName "QGA:qapi-schema.GuestHostName") – the host name of the machine

*Object* GuestUser (Since: 2.10)
:   *Availability*: `CONFIG_WIN32 or HAVE_UTMPX`

    Members:
    :   - **user** (`string`) – Username
        - **domain** (`string`, *optional*) – Logon domain (windows only)
        - **login-time** (`number`) – Time of login of this user on the computer. If
          multiple instances of the user are logged in, the earliest login
          time is reported. The value is in fractional seconds since
          epoch time.

*Command* guest-get-users (Since: 2.10)
:   *Availability*: `CONFIG_WIN32 or HAVE_UTMPX`

    Retrieves a list of currently active users on the VM.

    Return:
    :   `[`[`GuestUser`](qemu-ga-ref.md#object-QGA-qapi-schema.GuestUser "QGA:qapi-schema.GuestUser")`]` – A unique list of users.

*Object* GuestTimezone (Since: 2.10)
:   Members:
    :   - **zone** (`string`, *optional*) – Timezone name. These values may differ depending on guest/OS
          and should only be used for informational purposes.
        - **offset** (`int`) – Offset to UTC in seconds, negative numbers for time zones
          west of GMT, positive numbers for east

*Command* guest-get-timezone (Since: 2.10)
:   Retrieves the timezone information from the guest.

    Return:
    :   [`GuestTimezone`](qemu-ga-ref.md#object-QGA-qapi-schema.GuestTimezone "QGA:qapi-schema.GuestTimezone")

*Object* GuestOSInfo (Since: 2.10)
:   Members:
    :   - **kernel-release** (`string`, *optional*) –

          - POSIX: release field returned by uname(2)
          - Windows: build number of the OS
        - **kernel-version** (`string`, *optional*) –

          - POSIX: version field returned by uname(2)
          - Windows: version number of the OS
        - **machine** (`string`, *optional*) –

          - POSIX: machine field returned by uname(2)
          - Windows: one of x86, x86_64, arm, ia64
        - **id** (`string`, *optional*) –

          - POSIX: as defined by os-release(5)
          - Windows: contains string “mswindows”
        - **name** (`string`, *optional*) –

          - POSIX: as defined by os-release(5)
          - Windows: contains string “Microsoft Windows”
        - **pretty-name** (`string`, *optional*) –

          - POSIX: as defined by os-release(5)
          - Windows: product name, e.g. “Microsoft Windows 10 Enterprise”
        - **version** (`string`, *optional*) –

          - POSIX: as defined by os-release(5)
          - Windows: long version string, e.g. “Microsoft Windows Server
            2008”
        - **version-id** (`string`, *optional*) –

          - POSIX: as defined by os-release(5)
          - Windows: short version identifier, e.g. “7” or “20012r2”
        - **variant** (`string`, *optional*) –

          - POSIX: as defined by os-release(5)
          - Windows: contains string “server” or “client”
        - **variant-id** (`string`, *optional*) –

          - POSIX: as defined by os-release(5)
          - Windows: contains string “server” or “client”

    > **Note:**
    >
    > On POSIX systems the fields `id`, `name`, `pretty-name`,
    > `version`, `version-id`, `variant` and `variant-id` follow the
    > definition specified in os-release(5). Refer to the manual page
    > for exact description of the fields. Their values are taken from
    > the os-release file. If the file is not present in the system,
    > or the values are not present in the file, the fields are not
    > included.
    >
    > On Windows the values are filled from information gathered from
    > the system.

*Command* guest-get-osinfo (Since: 2.10)
:   Retrieve guest operating system information

    Return:
    :   [`GuestOSInfo`](qemu-ga-ref.md#object-QGA-qapi-schema.GuestOSInfo "QGA:qapi-schema.GuestOSInfo")

*Enum* GuestDeviceType
:   *Availability*: `CONFIG_WIN32`

    Values:
    :   - **pci** – PCI device

*Object* GuestDeviceIdPCI (Since: 5.2)
:   *Availability*: `CONFIG_WIN32`

    Members:
    :   - **vendor-id** (`int`) – vendor ID
        - **device-id** (`int`) – device ID

*Object* GuestDeviceId (Since: 5.2)
:   *Availability*: `CONFIG_WIN32`

    Id of the device

    Members:
    :   - **type** ([`GuestDeviceType`](qemu-ga-ref.md#enum-QGA-qapi-schema.GuestDeviceType "QGA:qapi-schema.GuestDeviceType")) – device type
        - When `type` is `pci`: The members of [`GuestDeviceIdPCI`](qemu-ga-ref.md#object-QGA-qapi-schema.GuestDeviceIdPCI "QGA:qapi-schema.GuestDeviceIdPCI").

*Object* GuestDeviceInfo (Since: 5.2)
:   *Availability*: `CONFIG_WIN32`

    Members:
    :   - **driver-name** (`string`) – name of the associated driver
        - **driver-date** (`int`, *optional*) – driver release date, in nanoseconds since the epoch
        - **driver-version** (`string`, *optional*) – driver version
        - **id** ([`GuestDeviceId`](qemu-ga-ref.md#object-QGA-qapi-schema.GuestDeviceId "QGA:qapi-schema.GuestDeviceId"), *optional*) – device ID

*Command* guest-get-devices (Since: 5.2)
:   *Availability*: `CONFIG_WIN32`

    Retrieve information about device drivers in Windows guest

    Return:
    :   `[`[`GuestDeviceInfo`](qemu-ga-ref.md#object-QGA-qapi-schema.GuestDeviceInfo "QGA:qapi-schema.GuestDeviceInfo")`]`

*Object* GuestAuthorizedKeys (Since: 5.2)
:   Members:
    :   - **keys** (`[``string``]`) – public keys (in OpenSSH/sshd(8) authorized_keys format)

*Command* guest-ssh-get-authorized-keys (Since: 5.2)
:   Return the public keys from user .ssh/authorized_keys on Unix
    systems (not implemented for other systems).

    Arguments:
    :   - **username** (`string`) – the user account to add the authorized keys

    Return:
    :   [`GuestAuthorizedKeys`](qemu-ga-ref.md#object-QGA-qapi-schema.GuestAuthorizedKeys "QGA:qapi-schema.GuestAuthorizedKeys")

*Command* guest-ssh-add-authorized-keys (Since: 5.2)
:   Append public keys to user .ssh/authorized_keys on Unix systems (not
    implemented for other systems).

    Arguments:
    :   - **username** (`string`) – the user account to add the authorized keys
        - **keys** (`[``string``]`) – the public keys to add (in OpenSSH/sshd(8) authorized_keys
          format)
        - **reset** (`boolean`, *optional*) – ignore the existing content, set it with the given keys only

*Command* guest-ssh-remove-authorized-keys (Since: 5.2)
:   Remove public keys from the user .ssh/authorized_keys on Unix
    systems (not implemented for other systems). It’s not an error if
    the key is already missing.

    Arguments:
    :   - **username** (`string`) – the user account to remove the authorized keys
        - **keys** (`[``string``]`) – the public keys to remove (in OpenSSH/sshd(8) authorized_keys
          format)

*Object* GuestDiskStats (Since: 7.1)
:   *Availability*: `CONFIG_LINUX`

    Members:
    :   - **read-sectors** (`int`, *optional*) – sectors read
        - **read-ios** (`int`, *optional*) – reads completed successfully
        - **read-merges** (`int`, *optional*) – read requests merged
        - **write-sectors** (`int`, *optional*) – sectors written
        - **write-ios** (`int`, *optional*) – writes completed
        - **write-merges** (`int`, *optional*) – write requests merged
        - **discard-sectors** (`int`, *optional*) – sectors discarded
        - **discard-ios** (`int`, *optional*) – discards completed successfully
        - **discard-merges** (`int`, *optional*) – discard requests merged
        - **flush-ios** (`int`, *optional*) – flush requests completed successfully
        - **read-ticks** (`int`, *optional*) – time spent reading(ms)
        - **write-ticks** (`int`, *optional*) – time spent writing(ms)
        - **discard-ticks** (`int`, *optional*) – time spent discarding(ms)
        - **flush-ticks** (`int`, *optional*) – time spent flushing(ms)
        - **ios-pgr** (`int`, *optional*) – number of I/Os currently in flight
        - **total-ticks** (`int`, *optional*) – time spent doing I/Os (ms)
        - **weight-ticks** (`int`, *optional*) – weighted time spent doing I/Os since the last update
          of this field(ms)

*Object* GuestDiskStatsInfo
:   *Availability*: `CONFIG_LINUX`

    Members:
    :   - **name** (`string`) – disk name
        - **major** (`int`) – major device number of disk
        - **minor** (`int`) – minor device number of disk
        - **stats** ([`GuestDiskStats`](qemu-ga-ref.md#object-QGA-qapi-schema.GuestDiskStats "QGA:qapi-schema.GuestDiskStats")) – I/O statistics

*Command* guest-get-diskstats (Since: 7.1)
:   *Availability*: `CONFIG_LINUX`

    Retrieve information about disk stats.

    Return:
    :   `[`[`GuestDiskStatsInfo`](qemu-ga-ref.md#object-QGA-qapi-schema.GuestDiskStatsInfo "QGA:qapi-schema.GuestDiskStatsInfo")`]` – List of disk stats of guest.

*Enum* GuestCpuStatsType (Since: 7.1)
:   *Availability*: `CONFIG_LINUX`

    Guest operating systems supporting CPU statistics

    Values:
    :   - **linux** – Linux

*Object* GuestLinuxCpuStats (Since: 7.1)
:   *Availability*: `CONFIG_LINUX`

    CPU statistics of Linux

    Members:
    :   - **cpu** (`int`) – CPU index in guest OS
        - **user** (`int`) – Time spent in user mode
        - **nice** (`int`) – Time spent in user mode with low priority (nice)
        - **system** (`int`) – Time spent in system mode
        - **idle** (`int`) – Time spent in the idle task
        - **iowait** (`int`, *optional*) – Time waiting for I/O to complete (since Linux 2.5.41)
        - **irq** (`int`, *optional*) – Time servicing interrupts (since Linux 2.6.0-test4)
        - **softirq** (`int`, *optional*) – Time servicing softirqs (since Linux 2.6.0-test4)
        - **steal** (`int`, *optional*) – Stolen time by host (since Linux 2.6.11)
        - **guest** (`int`, *optional*) – ime spent running a virtual CPU for guest operating systems
          under the control of the Linux kernel (since Linux 2.6.24)
        - **guestnice** (`int`, *optional*) – Time spent running a niced guest (since Linux 2.6.33)

*Object* GuestCpuStats (Since: 7.1)
:   *Availability*: `CONFIG_LINUX`

    Get statistics of each CPU in millisecond.

    Members:
    :   - **type** ([`GuestCpuStatsType`](qemu-ga-ref.md#enum-QGA-qapi-schema.GuestCpuStatsType "QGA:qapi-schema.GuestCpuStatsType")) – guest operating system
        - When `type` is `linux`: The members of [`GuestLinuxCpuStats`](qemu-ga-ref.md#object-QGA-qapi-schema.GuestLinuxCpuStats "QGA:qapi-schema.GuestLinuxCpuStats").

*Command* guest-get-cpustats (Since: 7.1)
:   *Availability*: `CONFIG_LINUX`

    Retrieve information about CPU stats.

    Return:
    :   `[`[`GuestCpuStats`](qemu-ga-ref.md#object-QGA-qapi-schema.GuestCpuStats "QGA:qapi-schema.GuestCpuStats")`]` – List of CPU stats of guest.

*Object* GuestLoadAverage (Since: 10.0)
:   *Availability*: `CONFIG_WIN32 or CONFIG_GETLOADAVG`

    Statistics about process load information

    Members:
    :   - **load1m** (`number`) – 1-minute load avage
        - **load5m** (`number`) – 5-minute load avage
        - **load15m** (`number`) – 15-minute load avage

*Command* guest-get-load (Since: 10.0)
:   *Availability*: `CONFIG_WIN32 or CONFIG_GETLOADAVG`

    Retrieve CPU process load information

    > **Note:**
    >
    > Windows does not have load average API, so QGA emulates it
    > by calculating the average CPU usage in the last 1, 5, 15 minutes
    > similar as Linux does this. Calculation starts from the first
    > time this command is called.

    Return:
    :   [`GuestLoadAverage`](qemu-ga-ref.md#object-QGA-qapi-schema.GuestLoadAverage "QGA:qapi-schema.GuestLoadAverage") – load information

*Object* GuestNetworkRoute (Since: 9.1 (Linux only); 11.0 (Windows))
:   *Availability*: `CONFIG_LINUX or CONFIG_WIN32`

    Route information. Supported on Linux (since 9.1) and Windows
    (since 11.0).

    Members:
    :   - **iface** (`string`) – The destination network or host’s egress network interface
          in the routing table
        - **destination** (`string`) – The IP address of the target network or host, The
          final destination of the packet
        - **metric** (`int`) – Route metric
        - **gateway** (`string`, *optional*) – The IP address of the next hop router
        - **mask** (`string`, *optional*) – Subnet Mask (IPv4 only)
        - **irtt** (`int`, *optional*) – Initial round-trip delay (not for windows, IPv4 only)
        - **flags** (`int`, *optional*) – Route flags (not for windows)
        - **refcnt** (`int`, *optional*) – The route’s reference count (not for windows)
        - **use** (`int`, *optional*) – Route usage count (not for windows)
        - **window** (`int`, *optional*) – TCP window size, used for flow control (not for windows,
          IPv4 only)
        - **mtu** (`int`, *optional*) – Data link layer maximum packet size (not for windows)
        - **desprefixlen** (`string`, *optional*) – Destination prefix length (for IPv6)
        - **source** (`string`, *optional*) – Source IP address (for IPv6)
        - **srcprefixlen** (`string`, *optional*) – Source prefix length (for IPv6)
        - **nexthop** (`string`, *optional*) – Next hop IP address (for IPv6)
        - **version** (`int`) – IP version (4 or 6)

*Command* guest-network-get-route (Since: 9.1 (Linux only); 11.0 (Windows))
:   *Availability*: `CONFIG_LINUX or CONFIG_WIN32`

    Retrieve information about route of network.

    Return:
    :   `[`[`GuestNetworkRoute`](qemu-ga-ref.md#object-QGA-qapi-schema.GuestNetworkRoute "QGA:qapi-schema.GuestNetworkRoute")`]` – List of route info of guest.
