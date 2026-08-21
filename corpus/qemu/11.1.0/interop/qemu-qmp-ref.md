---
collection: qemu
version: "11.1.0"
title: "QEMU QMP Reference Manual"
source_url: https://www.qemu.org/docs/master/interop/qemu-qmp-ref.html
fetched_at: 2026-08-21T03:22:20+00:00
---
# QEMU QMP Reference Manual

- [Introduction](qemu-qmp-ref.md#introduction)
- [QMP errors](qemu-qmp-ref.md#qmp-errors)
- [Common data types](qemu-qmp-ref.md#common-data-types)
- [Socket data types](qemu-qmp-ref.md#socket-data-types)
- [VM run state](qemu-qmp-ref.md#vm-run-state)
- [Cryptography](qemu-qmp-ref.md#cryptography)
- [Background jobs](qemu-qmp-ref.md#background-jobs)
- [Accelerators](qemu-qmp-ref.md#accelerators)
- [Block devices](qemu-qmp-ref.md#block-devices)

  - [Block core (VM unrelated)](qemu-qmp-ref.md#block-core-vm-unrelated)
  - [Additional block stuff (VM related)](qemu-qmp-ref.md#additional-block-stuff-vm-related)
  - [Block device exports](qemu-qmp-ref.md#block-device-exports)
- [Character devices](qemu-qmp-ref.md#character-devices)
- [Dump guest memory](qemu-qmp-ref.md#dump-guest-memory)
- [Net devices](qemu-qmp-ref.md#net-devices)
- [eBPF Objects](qemu-qmp-ref.md#ebpf-objects)
- [Rocker switch device](qemu-qmp-ref.md#rocker-switch-device)
- [TPM (trusted platform module) devices](qemu-qmp-ref.md#tpm-trusted-platform-module-devices)
- [Remote desktop](qemu-qmp-ref.md#remote-desktop)

  - [Spice](qemu-qmp-ref.md#spice)
  - [VNC](qemu-qmp-ref.md#vnc)
- [Input](qemu-qmp-ref.md#input)
- [User authorization](qemu-qmp-ref.md#user-authorization)
- [Migration](qemu-qmp-ref.md#migration)
- [Transactions](qemu-qmp-ref.md#transactions)
- [Tracing](qemu-qmp-ref.md#tracing)
- [Compatibility policy](qemu-qmp-ref.md#compatibility-policy)
- [QMP monitor control](qemu-qmp-ref.md#qmp-monitor-control)
- [QMP introspection](qemu-qmp-ref.md#qmp-introspection)
- [QEMU Object Model (QOM)](qemu-qmp-ref.md#qemu-object-model-qom)
- [Device infrastructure (qdev)](qemu-qmp-ref.md#device-infrastructure-qdev)
- [Common machine types](qemu-qmp-ref.md#common-machine-types)
- [Machines](qemu-qmp-ref.md#machines)
- [Record/replay](qemu-qmp-ref.md#record-replay)
- [Yank feature](qemu-qmp-ref.md#yank-feature)
- [Miscellanea](qemu-qmp-ref.md#miscellanea)
- [Audio](qemu-qmp-ref.md#audio)
- [ACPI](qemu-qmp-ref.md#acpi)
- [PCI](qemu-qmp-ref.md#pci)
- [Statistics](qemu-qmp-ref.md#statistics)
- [Virtio devices](qemu-qmp-ref.md#virtio-devices)
- [VFIO devices](qemu-qmp-ref.md#vfio-devices)
- [Cryptography devices](qemu-qmp-ref.md#cryptography-devices)
- [CXL devices](qemu-qmp-ref.md#cxl-devices)
- [UEFI Variable Store](qemu-qmp-ref.md#uefi-variable-store)

## [Introduction](qemu-qmp-ref.md#id2)

This manual describes the commands and events supported by the QEMU
Monitor Protocol (QMP).

For locating a particular item, please see the [QMP Index](../qapi-qmp-index.md).

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

## [QMP errors](qemu-qmp-ref.md#id3)

*Enum* QapiErrorClass (Since: 1.2)
:   QEMU error classes

    Values:
    :   - **GenericError** – this is used for errors that don’t require a specific
          error class. This should be the default case for most errors
        - **CommandNotFound** – the requested command has not been found
        - **DeviceNotActive** – a device has failed to be become active
        - **DeviceNotFound** – the requested device has not been found
        - **KVMMissingCap** – the requested operation can’t be fulfilled because a
          required KVM capability is missing

## [Common data types](qemu-qmp-ref.md#id4)

*Enum* IoOperationType (Since: 2.1)
:   An enumeration of the I/O operation types

    Values:
    :   - **read** – read operation
        - **write** – write operation

*Enum* OnOffAuto (Since: 2.2)
:   An enumeration of three options: on, off, and auto

    Values:
    :   - **auto** – QEMU selects the value between on and off
        - **on** – Enabled
        - **off** – Disabled

*Enum* OnOffSplit (Since: 2.6)
:   An enumeration of three values: on, off, and split

    Values:
    :   - **on** – Enabled
        - **off** – Disabled
        - **split** – Mixed

*Alternate* StrOrNull (Since: 2.10)
:   This is a string value or the explicit lack of a string (null
    pointer in C). Intended for cases when ‘optional absent’ already
    has a different meaning.

    Alternatives:
    :   - **s** (`string`) – the string value
        - **n** (`null`) – no string value

*Enum* OffAutoPCIBAR (Since: 2.12)
:   An enumeration of options for specifying a PCI BAR

    Values:
    :   - **off** – The specified feature is disabled
        - **auto** – The PCI BAR for the feature is automatically selected
        - **bar0** – PCI BAR0 is used for the feature
        - **bar1** – PCI BAR1 is used for the feature
        - **bar2** – PCI BAR2 is used for the feature
        - **bar3** – PCI BAR3 is used for the feature
        - **bar4** – PCI BAR4 is used for the feature
        - **bar5** – PCI BAR5 is used for the feature

*Enum* PCIELinkSpeed (Since: 4.0)
:   An enumeration of PCIe link speeds in units of GT/s

    Values:
    :   - **2_5** – 2.5GT/s
        - **5** – 5.0GT/s
        - **8** – 8.0GT/s
        - **16** – 16.0GT/s
        - **32** – 32.0GT/s (since 9.0)
        - **64** – 64.0GT/s (since 9.0)

*Enum* PCIELinkWidth (Since: 4.0)
:   An enumeration of PCIe link width

    Values:
    :   - **1** – x1
        - **2** – x2
        - **4** – x4
        - **8** – x8
        - **12** – x12
        - **16** – x16
        - **32** – x32

*Enum* HostMemPolicy (Since: 2.1)
:   Host memory policy types

    Values:
    :   - **default** – restore default policy, remove any nondefault policy
        - **preferred** – set the preferred host nodes for allocation
        - **bind** – a strict policy that restricts memory allocation to the host
          nodes specified
        - **interleave** – memory allocations are interleaved across the set of
          host nodes specified

*Enum* NetFilterDirection (Since: 2.5)
:   Indicates whether a netfilter is attached to a netdev’s transmit
    queue or receive queue or both.

    Values:
    :   - **all** – the filter is attached both to the receive and the transmit
          queue of the netdev (default).
        - **rx** – the filter is attached to the receive queue of the netdev,
          where it will receive packets sent to the netdev.
        - **tx** – the filter is attached to the transmit queue of the netdev,
          where it will receive packets sent by the netdev.

*Enum* GrabToggleKeys (Since: 4.0)
:   Key combinations to toggle input-linux between host and guest.

    Values:
    :   - **ctrl-ctrl** – left and right control key
        - **alt-alt** – left and right alt key
        - **shift-shift** – left and right shift key
        - **meta-meta** – left and right meta key
        - **scrolllock** – scroll lock key
        - **ctrl-scrolllock** – either control key and scroll lock key

*Object* HumanReadableText (Since: 6.2)
:   Members:
    :   - **human-readable-text** (`string`) – Formatted output intended for humans.

*Enum* EndianMode (Since: 10.0)
:   Values:
    :   - **unspecified** – Endianness not specified
        - **little** – Little endianness
        - **big** – Big endianness

## [Socket data types](qemu-qmp-ref.md#id5)

*Enum* NetworkAddressFamily (Since: 2.1)
:   The network address family

    Values:
    :   - **ipv4** – IPV4 family
        - **ipv6** – IPV6 family
        - **unix** – unix socket
        - **vsock** – vsock family (since 2.8)
        - **unknown** – otherwise

*Object* InetSocketAddressBase
:   Members:
    :   - **host** (`string`) – host part of the address
        - **port** (`string`) – port part of the address

*Object* InetSocketAddress (Since: 1.3)
:   Captures a socket address or address range in the Internet
    namespace.

    Members:
    :   - **numeric** (`boolean`, *optional*) – true if the host/port are guaranteed to be numeric, false
          if name resolution should be attempted. Defaults to false.
          (Since 2.9)
        - **to** (`int`, *optional*) – If present, this is range of possible addresses, with port
          between `port` and `to`.
        - **ipv4** (`boolean`, *optional*) – whether to accept IPv4 addresses, default try both IPv4 and
          IPv6
        - **ipv6** (`boolean`, *optional*) – whether to accept IPv6 addresses, default try both IPv4 and
          IPv6
        - **keep-alive** (`boolean`, *optional*) – enable keep-alive when connecting to/listening on this
          socket.
          (Since 4.2, not supported for listening sockets until 10.1)
        - **keep-alive-count** (`int`, *optional*) – number of keep-alive packets sent before the
          connection is closed. Only supported for TCP sockets on systems
          where TCP_KEEPCNT socket option is defined (this includes Linux,
          Windows, macOS, FreeBSD, but not OpenBSD). When set to 0,
          system setting is used. (Since 10.1)
        - **keep-alive-idle** (`int`, *optional*) – time in seconds the connection needs to be idle
          before sending a keepalive packet. Only supported for TCP
          sockets on systems where TCP_KEEPIDLE socket option is defined
          (this includes Linux, Windows, macOS, FreeBSD, but not OpenBSD).
          When set to 0, system setting is used. (Since 10.1)
        - **keep-alive-interval** (`int`, *optional*) – time in seconds between keep-alive packets.
          Only supported for TCP sockets on systems where TCP_KEEPINTVL is
          defined (this includes Linux, Windows, macOS, FreeBSD, but not
          OpenBSD). When set to 0, system setting is used. (Since 10.1)
        - **mptcp** (`boolean`, *optional*) – enable multi-path TCP. (Since 6.1)
        - The members of [`InetSocketAddressBase`](qemu-qmp-ref.md#object-QMP-sockets.InetSocketAddressBase "QMP:sockets.InetSocketAddressBase").

*Object* UnixSocketAddress (Since: 1.3)
:   Captures a socket address in the local (“Unix socket”) namespace.

    Members:
    :   - **path** (`string`) – filesystem path to use
        - **abstract** (`boolean`, *optional*) – if true, this is a Linux abstract socket address. `path`
          will be prefixed by a null byte, and optionally padded with null
          bytes. Defaults to false. (Since 5.1)
        - **tight** (`boolean`, *optional*) – if false, pad an abstract socket address with enough null
          bytes to make it fill struct sockaddr_un member sun_path.
          Defaults to true. (Since 5.1)

*Object* VsockSocketAddress (Since: 2.8)
:   Captures a socket address in the vsock namespace.

    Members:
    :   - **cid** (`string`) – unique host identifier
        - **port** (`string`) – port

    > **Note:**
    >
    > String types are used to allow for possible future
    > hostname or service resolution support.

*Object* FdSocketAddress (Since: 1.2)
:   A file descriptor name or number.

    Members:
    :   - **str** (`string`) – decimal is for file descriptor number, otherwise it’s a file
          descriptor name. Named file descriptors are permitted in
          monitor commands, in combination with the [`getfd`](qemu-qmp-ref.md#command-QMP-misc.getfd "QMP:misc.getfd") command.
          Decimal file descriptors are permitted at startup or other
          contexts where no monitor context is active.

*Object* InetSocketAddressWrapper (Since: 1.3)
:   Members:
    :   - **data** ([`InetSocketAddress`](qemu-qmp-ref.md#object-QMP-sockets.InetSocketAddress "QMP:sockets.InetSocketAddress")) – internet domain socket address

*Object* UnixSocketAddressWrapper (Since: 1.3)
:   Members:
    :   - **data** ([`UnixSocketAddress`](qemu-qmp-ref.md#object-QMP-sockets.UnixSocketAddress "QMP:sockets.UnixSocketAddress")) – UNIX domain socket address

*Object* VsockSocketAddressWrapper (Since: 2.8)
:   Members:
    :   - **data** ([`VsockSocketAddress`](qemu-qmp-ref.md#object-QMP-sockets.VsockSocketAddress "QMP:sockets.VsockSocketAddress")) – VSOCK domain socket address

*Object* FdSocketAddressWrapper (Since: 1.3)
:   Members:
    :   - **data** ([`FdSocketAddress`](qemu-qmp-ref.md#object-QMP-sockets.FdSocketAddress "QMP:sockets.FdSocketAddress")) – file descriptor name or number

*Object* SocketAddressLegacy (Since: 1.3)
:   Captures the address of a socket, which could also be a named file
    descriptor

    Members:
    :   - **type** ([`SocketAddressType`](qemu-qmp-ref.md#enum-QMP-sockets.SocketAddressType "QMP:sockets.SocketAddressType")) – Transport type
        - When `type` is `inet`: The members of [`InetSocketAddressWrapper`](qemu-qmp-ref.md#object-QMP-sockets.InetSocketAddressWrapper "QMP:sockets.InetSocketAddressWrapper").
        - When `type` is `unix`: The members of [`UnixSocketAddressWrapper`](qemu-qmp-ref.md#object-QMP-sockets.UnixSocketAddressWrapper "QMP:sockets.UnixSocketAddressWrapper").
        - When `type` is `vsock`: The members of [`VsockSocketAddressWrapper`](qemu-qmp-ref.md#object-QMP-sockets.VsockSocketAddressWrapper "QMP:sockets.VsockSocketAddressWrapper").
        - When `type` is `fd`: The members of [`FdSocketAddressWrapper`](qemu-qmp-ref.md#object-QMP-sockets.FdSocketAddressWrapper "QMP:sockets.FdSocketAddressWrapper").

*Enum* SocketAddressType (Since: 2.9)
:   Available [`SocketAddress`](qemu-qmp-ref.md#object-QMP-sockets.SocketAddress "QMP:sockets.SocketAddress") types

    Values:
    :   - **inet** – Internet address
        - **unix** – Unix domain socket
        - **vsock** – VMCI address
        - **fd** – Socket file descriptor

*Object* SocketAddress (Since: 2.9)
:   Captures the address of a socket, which could also be a socket file
    descriptor

    Members:
    :   - **type** ([`SocketAddressType`](qemu-qmp-ref.md#enum-QMP-sockets.SocketAddressType "QMP:sockets.SocketAddressType")) – Transport type
        - When `type` is `inet`: The members of [`InetSocketAddress`](qemu-qmp-ref.md#object-QMP-sockets.InetSocketAddress "QMP:sockets.InetSocketAddress").
        - When `type` is `unix`: The members of [`UnixSocketAddress`](qemu-qmp-ref.md#object-QMP-sockets.UnixSocketAddress "QMP:sockets.UnixSocketAddress").
        - When `type` is `vsock`: The members of [`VsockSocketAddress`](qemu-qmp-ref.md#object-QMP-sockets.VsockSocketAddress "QMP:sockets.VsockSocketAddress").
        - When `type` is `fd`: The members of [`FdSocketAddress`](qemu-qmp-ref.md#object-QMP-sockets.FdSocketAddress "QMP:sockets.FdSocketAddress").

## [VM run state](qemu-qmp-ref.md#id6)

*Enum* RunState
:   An enumeration of VM run states.

    Values:
    :   - **debug** – QEMU is running on a debugger
        - **finish-migrate** – guest is paused to finish the migration process
        - **inmigrate** – guest is paused waiting for an incoming migration. Note
          that this state does not tell whether the machine will start at
          the end of the migration. This depends on the command-line -S
          option and any invocation of [`stop`](qemu-qmp-ref.md#command-QMP-misc.stop "QMP:misc.stop") or [`cont`](qemu-qmp-ref.md#command-QMP-misc.cont "QMP:misc.cont") that has happened
          since QEMU was started.
        - **internal-error** – An internal error that prevents further guest
          execution has occurred
        - **io-error** – the last IOP has failed and the device is configured to
          pause on I/O errors
        - **paused** – guest has been paused via the ‘stop’ command
        - **postmigrate** – guest is paused following a successful ‘migrate’
        - **prelaunch** – QEMU was started with -S and guest has not started
        - **restore-vm** – guest is paused to restore VM state
        - **running** – guest is actively running
        - **save-vm** – guest is paused to save the VM state
        - **shutdown** – guest is shut down (and -no-shutdown is in use)
        - **suspended** – guest is suspended (ACPI S3)
        - **watchdog** – the watchdog action is configured to pause and has been
          triggered
        - **guest-panicked** – guest has been panicked as a result of guest OS
          panic
        - **colo** – guest is paused to save/restore VM state under colo
          checkpoint, VM can not get into this state unless colo
          capability is enabled for migration. (since 2.8)

*Enum* ShutdownCause
:   An enumeration of reasons for a shutdown.

    Values:
    :   - **none** – No shutdown request pending
        - **host-error** – An error prevents further use of guest
        - **host-qmp-quit** – Reaction to the QMP command [`quit`](qemu-qmp-ref.md#command-QMP-control.quit "QMP:control.quit")
        - **host-qmp-system-reset** – Reaction to the QMP command [`system_reset`](qemu-qmp-ref.md#command-QMP-machine.system_reset "QMP:machine.system_reset")
        - **host-signal** – Reaction to a signal, such as SIGINT
        - **host-ui** – Reaction to a UI event, like window close
        - **guest-shutdown** – Guest shutdown/suspend request, via ACPI or other
          hardware-specific means
        - **guest-reset** – Guest reset request, and command line turns that into
          a shutdown
        - **guest-panic** – Guest panicked, and command line turns that into a
          shutdown
        - **subsystem-reset** – Partial guest reset that does not trigger QMP
          events and ignores –no-reboot. This is useful for sanitizing
          hypercalls on s390 that are used during kexec/kdump/boot
        - **snapshot-load** – A snapshot is being loaded by the record & replay
          subsystem. This value is used only within QEMU. It doesn’t
          occur in QMP. (since 7.2)

*Object* StatusInfo (Since: 0.14)
:   Information about VM run state

    Members:
    :   - **running** (`boolean`) – true if all VCPUs are runnable, false if not runnable
        - **status** ([`RunState`](qemu-qmp-ref.md#enum-QMP-run-state.RunState "QMP:run-state.RunState")) – the virtual machine [`RunState`](qemu-qmp-ref.md#enum-QMP-run-state.RunState "QMP:run-state.RunState")

*Command* query-status (Since: 0.14)
:   Query the run status of the VM

    Return:
    :   [`StatusInfo`](qemu-qmp-ref.md#object-QMP-run-state.StatusInfo "QMP:run-state.StatusInfo")

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "query-status" }
    > <- { "return": { "running": true,
    >                  "status": "running" } }
    > ```

*Event* SHUTDOWN (Since: 0.12)
:   Emitted when the virtual machine has shut down, indicating that QEMU
    is about to exit.

    Members:
    :   - **guest** (`boolean`) – If true, the shutdown was triggered by a guest request (such
          as a guest-initiated ACPI shutdown request or other
          hardware-specific action) rather than a host request (such as
          sending QEMU a SIGINT). (since 2.10)
        - **reason** ([`ShutdownCause`](qemu-qmp-ref.md#enum-QMP-run-state.ShutdownCause "QMP:run-state.ShutdownCause")) – The [`ShutdownCause`](qemu-qmp-ref.md#enum-QMP-run-state.ShutdownCause "QMP:run-state.ShutdownCause") which resulted in the [`SHUTDOWN`](qemu-qmp-ref.md#event-QMP-run-state.SHUTDOWN "QMP:run-state.SHUTDOWN").
          (since 4.0)

    > **Note:**
    >
    > If the command-line option `-no-shutdown` has been
    > specified, QEMU will not exit, and a [`STOP`](qemu-qmp-ref.md#event-QMP-run-state.STOP "QMP:run-state.STOP") event will eventually
    > follow the [`SHUTDOWN`](qemu-qmp-ref.md#event-QMP-run-state.SHUTDOWN "QMP:run-state.SHUTDOWN") event.

    > **Example::**
    >
    > ```QMP
    > <- { "event": "SHUTDOWN",
    >      "data": { "guest": true, "reason": "guest-shutdown" },
    >      "timestamp": { "seconds": 1267040730, "microseconds": 682951 } }
    > ```

*Event* POWERDOWN (Since: 0.12)
:   Emitted when the virtual machine is powered down through the power
    control system, such as via ACPI.

    > **Example::**
    >
    > ```QMP
    > <- { "event": "POWERDOWN",
    >      "timestamp": { "seconds": 1267040730, "microseconds": 682951 } }
    > ```

*Event* RESET (Since: 0.12)
:   Emitted when the virtual machine is reset

    Members:
    :   - **guest** (`boolean`) – If true, the reset was triggered by a guest request (such as
          a guest-initiated ACPI reboot request or other hardware-specific
          action) rather than a host request (such as the QMP command
          [`system_reset`](qemu-qmp-ref.md#command-QMP-machine.system_reset "QMP:machine.system_reset")). (since 2.10)
        - **reason** ([`ShutdownCause`](qemu-qmp-ref.md#enum-QMP-run-state.ShutdownCause "QMP:run-state.ShutdownCause")) – The [`ShutdownCause`](qemu-qmp-ref.md#enum-QMP-run-state.ShutdownCause "QMP:run-state.ShutdownCause") of the [`RESET`](qemu-qmp-ref.md#event-QMP-run-state.RESET "QMP:run-state.RESET"). (since 4.0)

    > **Example::**
    >
    > ```QMP
    > <- { "event": "RESET",
    >      "data": { "guest": false, "reason": "guest-reset" },
    >      "timestamp": { "seconds": 1267041653, "microseconds": 9518 } }
    > ```

*Event* STOP (Since: 0.12)
:   Emitted when the virtual machine is stopped

    > **Example::**
    >
    > ```QMP
    > <- { "event": "STOP",
    >      "timestamp": { "seconds": 1267041730, "microseconds": 281295 } }
    > ```

*Event* RESUME (Since: 0.12)
:   Emitted when the virtual machine resumes execution

    > **Example::**
    >
    > ```QMP
    > <- { "event": "RESUME",
    >      "timestamp": { "seconds": 1271770767, "microseconds": 582542 } }
    > ```

*Event* SUSPEND (Since: 1.1)
:   Emitted when guest enters a hardware suspension state, for example,
    S3 state, which is sometimes called standby state

    > **Example::**
    >
    > ```QMP
    > <- { "event": "SUSPEND",
    >      "timestamp": { "seconds": 1344456160, "microseconds": 309119 } }
    > ```

*Event* SUSPEND_DISK (Since: 1.2)
:   Emitted when guest enters a hardware suspension state with data
    saved on disk, for example, S4 state, which is sometimes called
    hibernate state

    > **Note:**
    >
    > QEMU shuts down (similar to event [`SHUTDOWN`](qemu-qmp-ref.md#event-QMP-run-state.SHUTDOWN "QMP:run-state.SHUTDOWN")) when
    > entering this state.

    > **Example::**
    >
    > ```QMP
    > <- { "event": "SUSPEND_DISK",
    >      "timestamp": { "seconds": 1344456160, "microseconds": 309119 } }
    > ```

*Event* WAKEUP (Since: 1.1)
:   Emitted when the guest has woken up from suspend state and is
    running

    > **Example::**
    >
    > ```QMP
    > <- { "event": "WAKEUP",
    >      "timestamp": { "seconds": 1344522075, "microseconds": 745528 } }
    > ```

*Event* WATCHDOG (Since: 0.13)
:   Emitted when the watchdog device’s timer is expired

    Members:
    :   - **action** ([`WatchdogAction`](qemu-qmp-ref.md#enum-QMP-run-state.WatchdogAction "QMP:run-state.WatchdogAction")) – action that has been taken

    > **Note:**
    >
    > If action is “reset”, “shutdown”, or “pause” the
    > [`WATCHDOG`](qemu-qmp-ref.md#event-QMP-run-state.WATCHDOG "QMP:run-state.WATCHDOG") event is followed respectively by the [`RESET`](qemu-qmp-ref.md#event-QMP-run-state.RESET "QMP:run-state.RESET"),
    > [`SHUTDOWN`](qemu-qmp-ref.md#event-QMP-run-state.SHUTDOWN "QMP:run-state.SHUTDOWN"), or [`STOP`](qemu-qmp-ref.md#event-QMP-run-state.STOP "QMP:run-state.STOP") events.

    > **Note:**
    >
    > This event is rate-limited.

    > **Example::**
    >
    > ```QMP
    > <- { "event": "WATCHDOG",
    >      "data": { "action": "reset" },
    >      "timestamp": { "seconds": 1267061043, "microseconds": 959568 } }
    > ```

*Enum* WatchdogAction (Since: 2.1)
:   An enumeration of the actions taken when the watchdog device’s timer
    is expired

    Values:
    :   - **reset** – system resets
        - **shutdown** – system shutdown, note that it is similar to `powerdown`,
          which tries to set to system status and notify guest
        - **poweroff** – system poweroff, the emulator program exits
        - **pause** – system pauses, similar to `stop`
        - **debug** – system enters debug state
        - **none** – nothing is done
        - **inject-nmi** – a non-maskable interrupt is injected (machine
          specific: for example on s390x CCW only the first vCPU
          receives the NMI, but on x86 machines all vCPUs receive
          it). (since 2.4)

*Enum* RebootAction (Since: 6.0)
:   Possible QEMU actions upon guest reboot

    Values:
    :   - **reset** – Reset the VM
        - **shutdown** – Shutdown the VM and exit, according to the shutdown
          action

*Enum* ShutdownAction (Since: 6.0)
:   Possible QEMU actions upon guest shutdown

    Values:
    :   - **poweroff** – Shutdown the VM and exit
        - **pause** – pause the VM

*Enum* PanicAction (Since: 6.0)
:   Values:
    :   - **none** – Continue VM execution
        - **pause** – Pause the VM
        - **shutdown** – Shutdown the VM and exit, according to the shutdown
          action
        - **exit-failure** – Shutdown the VM and exit with nonzero status
          (since 7.1)

*Command* watchdog-set-action (Since: 2.11)
:   Set watchdog action.

    Arguments:
    :   - **action** ([`WatchdogAction`](qemu-qmp-ref.md#enum-QMP-run-state.WatchdogAction "QMP:run-state.WatchdogAction")) – [`WatchdogAction`](qemu-qmp-ref.md#enum-QMP-run-state.WatchdogAction "QMP:run-state.WatchdogAction") action taken when watchdog timer expires.

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "watchdog-set-action",
    >      "arguments": { "action": "inject-nmi" } }
    > <- { "return": {} }
    > ```

*Command* set-action (Since: 6.0)
:   Set the actions that will be taken by the emulator in response to
    guest events.

    Arguments:
    :   - **reboot** ([`RebootAction`](qemu-qmp-ref.md#enum-QMP-run-state.RebootAction "QMP:run-state.RebootAction"), *optional*) – [`RebootAction`](qemu-qmp-ref.md#enum-QMP-run-state.RebootAction "QMP:run-state.RebootAction") action taken on guest reboot.
        - **shutdown** ([`ShutdownAction`](qemu-qmp-ref.md#enum-QMP-run-state.ShutdownAction "QMP:run-state.ShutdownAction"), *optional*) – [`ShutdownAction`](qemu-qmp-ref.md#enum-QMP-run-state.ShutdownAction "QMP:run-state.ShutdownAction") action taken on guest shutdown.
        - **panic** ([`PanicAction`](qemu-qmp-ref.md#enum-QMP-run-state.PanicAction "QMP:run-state.PanicAction"), *optional*) – [`PanicAction`](qemu-qmp-ref.md#enum-QMP-run-state.PanicAction "QMP:run-state.PanicAction") action taken on guest panic.
        - **watchdog** ([`WatchdogAction`](qemu-qmp-ref.md#enum-QMP-run-state.WatchdogAction "QMP:run-state.WatchdogAction"), *optional*) – [`WatchdogAction`](qemu-qmp-ref.md#enum-QMP-run-state.WatchdogAction "QMP:run-state.WatchdogAction") action taken when watchdog timer
          expires.

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "set-action",
    >      "arguments": { "reboot": "shutdown",
    >                     "shutdown" : "pause",
    >                     "panic": "pause",
    >                     "watchdog": "inject-nmi" } }
    > <- { "return": {} }
    > ```

*Event* GUEST_PANICKED (Since: 1.5)
:   Emitted when guest OS panic is detected

    Members:
    :   - **action** ([`GuestPanicAction`](qemu-qmp-ref.md#enum-QMP-run-state.GuestPanicAction "QMP:run-state.GuestPanicAction")) – action that has been taken, currently always “pause”
        - **info** ([`GuestPanicInformation`](qemu-qmp-ref.md#object-QMP-run-state.GuestPanicInformation "QMP:run-state.GuestPanicInformation"), *optional*) – information about a panic (since 2.9)

    > **Example::**
    >
    > ```QMP
    > <- { "event": "GUEST_PANICKED",
    >      "data": { "action": "pause" },
    >      "timestamp": { "seconds": 1648245231, "microseconds": 900001 } }
    > ```

*Event* GUEST_CRASHLOADED (Since: 5.0)
:   Emitted when guest OS crash loaded is detected

    Members:
    :   - **action** ([`GuestPanicAction`](qemu-qmp-ref.md#enum-QMP-run-state.GuestPanicAction "QMP:run-state.GuestPanicAction")) – action that has been taken, currently always “run”
        - **info** ([`GuestPanicInformation`](qemu-qmp-ref.md#object-QMP-run-state.GuestPanicInformation "QMP:run-state.GuestPanicInformation"), *optional*) – information about a panic

    > **Example::**
    >
    > ```QMP
    > <- { "event": "GUEST_CRASHLOADED",
    >      "data": { "action": "run" },
    >      "timestamp": { "seconds": 1648245259, "microseconds": 893771 } }
    > ```

*Event* GUEST_PVSHUTDOWN (Since: 9.1)
:   Emitted when guest submits a shutdown request via pvpanic interface

    > **Example::**
    >
    > ```QMP
    > <- { "event": "GUEST_PVSHUTDOWN",
    >      "timestamp": { "seconds": 1648245259, "microseconds": 893771 } }
    > ```

*Enum* GuestPanicAction (Since: 2.1)
:   An enumeration of the actions taken when guest OS panic is detected

    Values:
    :   - **pause** – system pauses
        - **poweroff** – system powers off (since 2.8)
        - **run** – system continues to run (since 5.0)

*Enum* GuestPanicInformationType (Since: 2.9)
:   An enumeration of the guest panic information types

    Values:
    :   - **hyper-v** – hyper-v guest panic information type
        - **s390** – s390 guest panic information type (Since: 2.12)
        - **tdx** – tdx guest panic information type (Since: 10.1)
        - **sev** – AMD SEV-ES guest termination information type (Since: 11.0)

*Object* GuestPanicInformation (Since: 2.9)
:   Information about a guest panic

    Members:
    :   - **type** ([`GuestPanicInformationType`](qemu-qmp-ref.md#enum-QMP-run-state.GuestPanicInformationType "QMP:run-state.GuestPanicInformationType")) – Crash type that defines the hypervisor specific information
        - When `type` is `hyper-v`: The members of [`GuestPanicInformationHyperV`](qemu-qmp-ref.md#object-QMP-run-state.GuestPanicInformationHyperV "QMP:run-state.GuestPanicInformationHyperV").
        - When `type` is `s390`: The members of [`GuestPanicInformationS390`](qemu-qmp-ref.md#object-QMP-run-state.GuestPanicInformationS390 "QMP:run-state.GuestPanicInformationS390").
        - When `type` is `tdx`: The members of [`GuestPanicInformationTdx`](qemu-qmp-ref.md#object-QMP-run-state.GuestPanicInformationTdx "QMP:run-state.GuestPanicInformationTdx").
        - When `type` is `sev`: The members of [`GuestPanicInformationSev`](qemu-qmp-ref.md#object-QMP-run-state.GuestPanicInformationSev "QMP:run-state.GuestPanicInformationSev").

*Object* GuestPanicInformationHyperV (Since: 2.9)
:   Hyper-V specific guest panic information (HV crash MSRs)

    Members:
    :   - **arg1** (`int`) – for Windows, [`STOP`](qemu-qmp-ref.md#event-QMP-run-state.STOP "QMP:run-state.STOP") code for the guest crash. For Linux,
          an error code.
        - **arg2** (`int`) – for Windows, first argument of the [`STOP`](qemu-qmp-ref.md#event-QMP-run-state.STOP "QMP:run-state.STOP"). For Linux, the
          guest OS ID, which has the kernel version in bits 16-47 and
          0x8100 in bits 48-63.
        - **arg3** (`int`) – for Windows, second argument of the [`STOP`](qemu-qmp-ref.md#event-QMP-run-state.STOP "QMP:run-state.STOP"). For Linux, the
          program counter of the guest.
        - **arg4** (`int`) – for Windows, third argument of the [`STOP`](qemu-qmp-ref.md#event-QMP-run-state.STOP "QMP:run-state.STOP"). For Linux, the
          RAX register (x86) or the stack pointer (aarch64) of the guest.
        - **arg5** (`int`) – for Windows, fourth argument of the [`STOP`](qemu-qmp-ref.md#event-QMP-run-state.STOP "QMP:run-state.STOP"). For x86 Linux,
          the stack pointer of the guest.

*Enum* S390CrashReason (Since: 2.12)
:   Reason why the CPU is in a crashed state.

    Values:
    :   - **unknown** – no crash reason was set
        - **disabled-wait** – the CPU has entered a disabled wait state
        - **extint-loop** – clock comparator or cpu timer interrupt with new PSW
          enabled for external interrupts
        - **pgmint-loop** – program interrupt with BAD new PSW
        - **opint-loop** – operation exception interrupt with invalid code at the
          program interrupt new PSW

*Object* GuestPanicInformationS390 (Since: 2.12)
:   S390 specific guest panic information (PSW)

    Members:
    :   - **core** (`int`) – core id of the CPU that crashed
        - **psw-mask** (`int`) – control fields of guest PSW
        - **psw-addr** (`int`) – guest instruction address
        - **reason** ([`S390CrashReason`](qemu-qmp-ref.md#enum-QMP-run-state.S390CrashReason "QMP:run-state.S390CrashReason")) – guest crash reason

*Object* GuestPanicInformationTdx (Since: 10.1)
:   TDX Guest panic information specific to TDX, as specified in the
    “Guest-Hypervisor Communication Interface (GHCI) Specification”,
    section TDG.VP.VMCALL<ReportFatalError>.

    Members:
    :   - **error-code** (`int`) – TD-specific error code
        - **message** (`string`) – Human-readable error message provided by the guest. Not
          to be trusted.
        - **gpa** (`int`, *optional*) – guest-physical address of a page that contains more verbose
          error information, as zero-terminated string. Present when the
          “GPA valid” bit (bit 63) is set in `error-code`.

*Object* GuestPanicInformationSev (Since: 11.0)
:   Information for AMD SEV-specific termination request (GHCB MSR
    contents)

    Members:
    :   - **set** (`int`) – The reason code set provided by the guest
        - **code** (`int`) – The reason code provided by the guest

*Event* MEMORY_FAILURE (Since: 5.2)
:   Emitted when a memory failure occurs on host side.

    Members:
    :   - **recipient** ([`MemoryFailureRecipient`](qemu-qmp-ref.md#enum-QMP-run-state.MemoryFailureRecipient "QMP:run-state.MemoryFailureRecipient")) – recipient is defined as [`MemoryFailureRecipient`](qemu-qmp-ref.md#enum-QMP-run-state.MemoryFailureRecipient "QMP:run-state.MemoryFailureRecipient").
        - **action** ([`MemoryFailureAction`](qemu-qmp-ref.md#enum-QMP-run-state.MemoryFailureAction "QMP:run-state.MemoryFailureAction")) – action that has been taken.
        - **flags** ([`MemoryFailureFlags`](qemu-qmp-ref.md#object-QMP-run-state.MemoryFailureFlags "QMP:run-state.MemoryFailureFlags")) – flags for [`MemoryFailureAction`](qemu-qmp-ref.md#enum-QMP-run-state.MemoryFailureAction "QMP:run-state.MemoryFailureAction").

    > **Example::**
    >
    > ```QMP
    > <- { "event": "MEMORY_FAILURE",
    >      "data": { "recipient": "hypervisor",
    >                "action": "fatal",
    >                "flags": { "action-required": false,
    >                           "recursive": false } },
    >      "timestamp": { "seconds": 1267061043, "microseconds": 959568 } }
    > ```

*Enum* MemoryFailureRecipient (Since: 5.2)
:   Hardware memory failure occurs, handled by recipient.

    Values:
    :   - **hypervisor** – memory failure at QEMU process address space. (none
          guest memory, but used by QEMU itself).
        - **guest** – memory failure at guest memory,

*Enum* MemoryFailureAction (Since: 5.2)
:   Actions taken by QEMU in response to a hardware memory failure.

    Values:
    :   - **ignore** – the memory failure could be ignored. This will only be the
          case for action-optional failures.
        - **inject** – memory failure occurred in guest memory, the guest enabled
          MCE handling mechanism, and QEMU could inject the MCE into the
          guest successfully.
        - **fatal** – the failure is unrecoverable. This occurs for
          action-required failures if the recipient is the hypervisor;
          QEMU will exit.
        - **reset** – the failure is unrecoverable but confined to the guest.
          This occurs if the recipient is a guest guest which is not ready
          to handle memory failures.

*Object* MemoryFailureFlags (Since: 5.2)
:   Additional information on memory failures.

    Members:
    :   - **action-required** (`boolean`) – whether a memory failure event is action-required
          or action-optional (e.g. a failure during memory scrub).
        - **recursive** (`boolean`) – whether the failure occurred while the previous failure
          was still in progress.

*Enum* NotifyVmexitOption (Since: 7.2)
:   An enumeration of the options specified when enabling notify VM exit

    Values:
    :   - **run** – enable the feature, do nothing and continue if the notify VM
          exit happens.
        - **internal-error** – enable the feature, raise a internal error if the
          notify VM exit happens.
        - **disable** – disable the feature.

## [Cryptography](qemu-qmp-ref.md#id7)

*Enum* QCryptoTLSCredsEndpoint (Since: 2.5)
:   The type of network endpoint that will be using the credentials.
    Most types of credential require different setup / structures
    depending on whether they will be used in a server versus a client.

    Values:
    :   - **client** – the network endpoint is acting as the client
        - **server** – the network endpoint is acting as the server

*Enum* QCryptoSecretFormat (Since: 2.6)
:   The data format that the secret is provided in

    Values:
    :   - **raw** – raw bytes. When encoded in JSON only valid UTF-8 sequences
          can be used
        - **base64** – arbitrary base64 encoded binary data

*Enum* QCryptoHashAlgo (Since: 2.6)
:   The supported algorithms for computing content digests

    Values:
    :   - **md5** – MD5. Should not be used in any new code, legacy compat only
        - **sha1** – SHA-1. Should not be used in any new code, legacy compat
          only
        - **sha224** – SHA-224. (since 2.7)
        - **sha256** – SHA-256. Current recommended strong hash.
        - **sha384** – SHA-384. (since 2.7)
        - **sha512** – SHA-512. (since 2.7)
        - **ripemd160** – RIPEMD-160. (since 2.7)
        - **sm3** – SM3. (since 9.2.0)

*Enum* QCryptoCipherAlgo (Since: 2.6)
:   The supported algorithms for content encryption ciphers

    Values:
    :   - **aes-128** – AES with 128 bit / 16 byte keys
        - **aes-192** – AES with 192 bit / 24 byte keys
        - **aes-256** – AES with 256 bit / 32 byte keys
        - **des** – DES with 56 bit / 8 byte keys. Do not use except in VNC.
          (since 6.1)
        - **3des** – 3DES(EDE) with 192 bit / 24 byte keys (since 2.9)
        - **cast5-128** – Cast5 with 128 bit / 16 byte keys
        - **serpent-128** – Serpent with 128 bit / 16 byte keys
        - **serpent-192** – Serpent with 192 bit / 24 byte keys
        - **serpent-256** – Serpent with 256 bit / 32 byte keys
        - **twofish-128** – Twofish with 128 bit / 16 byte keys
        - **twofish-192** – Twofish with 192 bit / 24 byte keys
        - **twofish-256** – Twofish with 256 bit / 32 byte keys
        - **sm4** – SM4 with 128 bit / 16 byte keys (since 9.0)

*Enum* QCryptoCipherMode (Since: 2.6)
:   The supported modes for content encryption ciphers

    Values:
    :   - **ecb** – Electronic Code Book
        - **cbc** – Cipher Block Chaining
        - **xts** – XEX with tweaked code book and ciphertext stealing
        - **ctr** – Counter (Since 2.8)
        - **gcm** – Galois/Counter Mode (Since 11.2)

*Enum* QCryptoIVGenAlgo (Since: 2.6)
:   The supported algorithms for generating initialization vectors for
    full disk encryption. The ‘plain’ generator should not be used for
    disks with sector numbers larger than 2^32, except where
    compatibility with pre-existing Linux dm-crypt volumes is required.

    Values:
    :   - **plain** – 64-bit sector number truncated to 32-bits
        - **plain64** – 64-bit sector number
        - **essiv** – 64-bit sector number encrypted with a hash of the encryption
          key

*Enum* QCryptoBlockFormat (Since: 2.6)
:   The supported full disk encryption formats

    Values:
    :   - **qcow** – QCow/QCow2 built-in AES-CBC encryption. Use only for
          liberating data from old images.
        - **luks** – LUKS encryption format. Recommended for new images

*Object* QCryptoBlockOptionsBase (Since: 2.6)
:   The common options that apply to all full disk encryption formats

    Members:
    :   - **format** ([`QCryptoBlockFormat`](qemu-qmp-ref.md#enum-QMP-crypto.QCryptoBlockFormat "QMP:crypto.QCryptoBlockFormat")) – the encryption format

*Object* QCryptoBlockOptionsQCow (Since: 2.6)
:   The options that apply to QCow/QCow2 AES-CBC encryption format

    Members:
    :   - **key-secret** (`string`, *optional*) – the ID of a QCryptoSecret object providing the
          decryption key. Mandatory except when probing image for
          metadata only.

*Object* QCryptoBlockOptionsLUKS (Since: 2.6)
:   The options that apply to LUKS encryption format

    Members:
    :   - **key-secret** (`string`, *optional*) – the ID of a QCryptoSecret object providing the
          decryption key. Mandatory except when probing image for
          metadata only.

*Object* QCryptoBlockCreateOptionsLUKS (Since: 2.6)
:   The options that apply to LUKS encryption format initialization

    Members:
    :   - **cipher-alg** ([`QCryptoCipherAlgo`](qemu-qmp-ref.md#enum-QMP-crypto.QCryptoCipherAlgo "QMP:crypto.QCryptoCipherAlgo"), *optional*) – the cipher algorithm for data encryption. Currently
          defaults to ‘aes-256’.
        - **cipher-mode** ([`QCryptoCipherMode`](qemu-qmp-ref.md#enum-QMP-crypto.QCryptoCipherMode "QMP:crypto.QCryptoCipherMode"), *optional*) – the cipher mode for data encryption. Currently
          defaults to ‘xts’
        - **ivgen-alg** ([`QCryptoIVGenAlgo`](qemu-qmp-ref.md#enum-QMP-crypto.QCryptoIVGenAlgo "QMP:crypto.QCryptoIVGenAlgo"), *optional*) – the initialization vector generator. Currently defaults
          to ‘plain64’
        - **ivgen-hash-alg** ([`QCryptoHashAlgo`](qemu-qmp-ref.md#enum-QMP-crypto.QCryptoHashAlgo "QMP:crypto.QCryptoHashAlgo"), *optional*) – the initialization vector generator hash.
          Currently defaults to ‘sha256’
        - **hash-alg** ([`QCryptoHashAlgo`](qemu-qmp-ref.md#enum-QMP-crypto.QCryptoHashAlgo "QMP:crypto.QCryptoHashAlgo"), *optional*) – the master key hash algorithm. Currently defaults to
          ‘sha256’
        - **iter-time** (`int`, *optional*) – number of milliseconds to spend in PBKDF passphrase
          processing. Currently defaults to 2000. (since 2.8)
        - The members of [`QCryptoBlockOptionsLUKS`](qemu-qmp-ref.md#object-QMP-crypto.QCryptoBlockOptionsLUKS "QMP:crypto.QCryptoBlockOptionsLUKS").

*Object* QCryptoBlockOpenOptions (Since: 2.6)
:   The options that are available for all encryption formats when
    opening an existing volume

    Members:
    :   - The members of [`QCryptoBlockOptionsBase`](qemu-qmp-ref.md#object-QMP-crypto.QCryptoBlockOptionsBase "QMP:crypto.QCryptoBlockOptionsBase").
        - When `format` is `qcow`: The members of [`QCryptoBlockOptionsQCow`](qemu-qmp-ref.md#object-QMP-crypto.QCryptoBlockOptionsQCow "QMP:crypto.QCryptoBlockOptionsQCow").
        - When `format` is `luks`: The members of [`QCryptoBlockOptionsLUKS`](qemu-qmp-ref.md#object-QMP-crypto.QCryptoBlockOptionsLUKS "QMP:crypto.QCryptoBlockOptionsLUKS").

*Object* QCryptoBlockCreateOptions (Since: 2.6)
:   The options that are available for all encryption formats when
    initializing a new volume

    Members:
    :   - The members of [`QCryptoBlockOptionsBase`](qemu-qmp-ref.md#object-QMP-crypto.QCryptoBlockOptionsBase "QMP:crypto.QCryptoBlockOptionsBase").
        - When `format` is `qcow`: The members of [`QCryptoBlockOptionsQCow`](qemu-qmp-ref.md#object-QMP-crypto.QCryptoBlockOptionsQCow "QMP:crypto.QCryptoBlockOptionsQCow").
        - When `format` is `luks`: The members of [`QCryptoBlockCreateOptionsLUKS`](qemu-qmp-ref.md#object-QMP-crypto.QCryptoBlockCreateOptionsLUKS "QMP:crypto.QCryptoBlockCreateOptionsLUKS").

*Object* QCryptoBlockInfoBase (Since: 2.7)
:   The common information that applies to all full disk encryption
    formats

    Members:
    :   - **format** ([`QCryptoBlockFormat`](qemu-qmp-ref.md#enum-QMP-crypto.QCryptoBlockFormat "QMP:crypto.QCryptoBlockFormat")) – the encryption format

*Object* QCryptoBlockInfoLUKSSlot (Since: 2.7)
:   Information about the LUKS block encryption key slot options

    Members:
    :   - **active** (`boolean`) – whether the key slot is currently in use
        - **key-offset** (`int`) – offset to the key material in bytes
        - **iters** (`int`, *optional*) – number of PBKDF2 iterations for key material
        - **stripes** (`int`, *optional*) – number of stripes for splitting key material

*Object* QCryptoBlockInfoLUKS (Since: 2.7)
:   Information about the LUKS block encryption options

    Members:
    :   - **cipher-alg** ([`QCryptoCipherAlgo`](qemu-qmp-ref.md#enum-QMP-crypto.QCryptoCipherAlgo "QMP:crypto.QCryptoCipherAlgo")) – the cipher algorithm for data encryption
        - **cipher-mode** ([`QCryptoCipherMode`](qemu-qmp-ref.md#enum-QMP-crypto.QCryptoCipherMode "QMP:crypto.QCryptoCipherMode")) – the cipher mode for data encryption
        - **ivgen-alg** ([`QCryptoIVGenAlgo`](qemu-qmp-ref.md#enum-QMP-crypto.QCryptoIVGenAlgo "QMP:crypto.QCryptoIVGenAlgo")) – the initialization vector generator
        - **ivgen-hash-alg** ([`QCryptoHashAlgo`](qemu-qmp-ref.md#enum-QMP-crypto.QCryptoHashAlgo "QMP:crypto.QCryptoHashAlgo"), *optional*) – the initialization vector generator hash
        - **hash-alg** ([`QCryptoHashAlgo`](qemu-qmp-ref.md#enum-QMP-crypto.QCryptoHashAlgo "QMP:crypto.QCryptoHashAlgo")) – the master key hash algorithm
        - **detached-header** (`boolean`) – whether the LUKS header is detached (Since 9.0)
        - **payload-offset** (`int`) – offset to the payload data in bytes
        - **master-key-iters** (`int`) – number of PBKDF2 iterations for key material
        - **uuid** (`string`) – unique identifier for the volume
        - **slots** (`[`[`QCryptoBlockInfoLUKSSlot`](qemu-qmp-ref.md#object-QMP-crypto.QCryptoBlockInfoLUKSSlot "QMP:crypto.QCryptoBlockInfoLUKSSlot")`]`) – information about each key slot

*Object* QCryptoBlockInfo (Since: 2.7)
:   Information about the block encryption options

    Members:
    :   - The members of [`QCryptoBlockInfoBase`](qemu-qmp-ref.md#object-QMP-crypto.QCryptoBlockInfoBase "QMP:crypto.QCryptoBlockInfoBase").
        - When `format` is `luks`: The members of [`QCryptoBlockInfoLUKS`](qemu-qmp-ref.md#object-QMP-crypto.QCryptoBlockInfoLUKS "QMP:crypto.QCryptoBlockInfoLUKS").

*Enum* QCryptoBlockLUKSKeyslotState (Since: 5.1)
:   Defines state of keyslots that are affected by the update

    Values:
    :   - **active** – The slots contain the given password and marked as active
        - **inactive** – The slots are erased (contain garbage) and marked as
          inactive

*Object* QCryptoBlockAmendOptionsLUKS (Since: 5.1)
:   This struct defines the update parameters that activate/de-activate
    set of keyslots

    Members:
    :   - **state** ([`QCryptoBlockLUKSKeyslotState`](qemu-qmp-ref.md#enum-QMP-crypto.QCryptoBlockLUKSKeyslotState "QMP:crypto.QCryptoBlockLUKSKeyslotState")) – the desired state of the keyslots
        - **new-secret** (`string`, *optional*) – The ID of a QCryptoSecret object providing the password
          to be written into added active keyslots
        - **old-secret** (`string`, *optional*) – Optional (for deactivation only). If given will
          deactivate all keyslots that match password located in
          QCryptoSecret with this ID
        - **iter-time** (`int`, *optional*) – Optional (for activation only). Number of milliseconds
          to spend in PBKDF passphrase processing for the newly activated
          keyslot. Currently defaults to 2000.
        - **keyslot** (`int`, *optional*) –

          Optional. ID of the keyslot to activate/deactivate. For
          keyslot activation, keyslot should not be active already (this
          is unsafe to update an active keyslot), but possible if ‘force’
          parameter is given. If keyslot is not given, first free keyslot
          will be written.

          For keyslot deactivation, this parameter specifies the exact
          keyslot to deactivate
        - **secret** (`string`, *optional*) – Optional. The ID of a QCryptoSecret object providing the
          password to use to retrieve current master key. Defaults to the
          same secret that was used to open the image

*Object* QCryptoBlockAmendOptions (Since: 5.1)
:   The options that are available for all encryption formats when
    amending encryption settings

    Members:
    :   - The members of [`QCryptoBlockOptionsBase`](qemu-qmp-ref.md#object-QMP-crypto.QCryptoBlockOptionsBase "QMP:crypto.QCryptoBlockOptionsBase").
        - When `format` is `luks`: The members of [`QCryptoBlockAmendOptionsLUKS`](qemu-qmp-ref.md#object-QMP-crypto.QCryptoBlockAmendOptionsLUKS "QMP:crypto.QCryptoBlockAmendOptionsLUKS").

*Object* SecretCommonProperties (Since: 2.6)
:   Properties for objects of classes derived from secret-common.

    Members:
    :   - **format** ([`QCryptoSecretFormat`](qemu-qmp-ref.md#enum-QMP-crypto.QCryptoSecretFormat "QMP:crypto.QCryptoSecretFormat"), *optional*) – the data format that the secret is provided in
          (default: raw)
        - **keyid** (`string`, *optional*) – the name of another secret that should be used to decrypt
          the provided data. If not present, the data is assumed to be
          unencrypted.
        - **iv** (`string`, *optional*) – the random initialization vector used for encryption of this
          particular secret. Should be a base64 encrypted string of the
          16-byte IV. Mandatory if `keyid` is given. Ignored if `keyid` is
          absent.

*Object* SecretProperties (Since: 2.6)
:   Properties for secret objects.

    Either `data` or `file` must be provided, but not both.

    Members:
    :   - **data** (`string`, *optional*) – the associated with the secret from
        - **file** (`string`, *optional*) – the filename to load the data associated with the secret from
        - The members of [`SecretCommonProperties`](qemu-qmp-ref.md#object-QMP-crypto.SecretCommonProperties "QMP:crypto.SecretCommonProperties").

*Object* SecretKeyringProperties (Since: 5.1)
:   *Availability*: `CONFIG_SECRET_KEYRING`

    Properties for secret_keyring objects.

    Members:
    :   - **serial** (`int`) – serial number that identifies a key to get from the kernel
        - The members of [`SecretCommonProperties`](qemu-qmp-ref.md#object-QMP-crypto.SecretCommonProperties "QMP:crypto.SecretCommonProperties").

*Object* TlsCredsProperties (Since: 2.5)
:   Properties for objects of classes derived from tls-creds.

    Members:
    :   - **verify-peer** (`boolean`, *optional*) – if true the peer credentials will be verified once the
          handshake is completed. This is a no-op for anonymous
          credentials. (default: true)
        - **dir** (`string`, *optional*) – the path of the directory that contains the credential files
        - **endpoint** ([`QCryptoTLSCredsEndpoint`](qemu-qmp-ref.md#enum-QMP-crypto.QCryptoTLSCredsEndpoint "QMP:crypto.QCryptoTLSCredsEndpoint"), *optional*) – whether the QEMU network backend that uses the
          credentials will be acting as a client or as a server
          (default: client)
        - **priority** (`string`, *optional*) – a gnutls priority string as described at
          <https://gnutls.org/manual/html_node/Priority-Strings.html>

*Object* TlsCredsAnonProperties (Since: 2.5)
:   Properties for tls-creds-anon objects.

    Members:
    :   - The members of [`TlsCredsProperties`](qemu-qmp-ref.md#object-QMP-crypto.TlsCredsProperties "QMP:crypto.TlsCredsProperties").

*Object* TlsCredsPskProperties (Since: 3.0)
:   Properties for tls-creds-psk objects.

    Members:
    :   - **username** (`string`, *optional*) – the username which will be sent to the server. For
          clients only. If absent, “qemu” is sent and the property will
          read back as an empty string.
        - The members of [`TlsCredsProperties`](qemu-qmp-ref.md#object-QMP-crypto.TlsCredsProperties "QMP:crypto.TlsCredsProperties").

*Object* TlsCredsX509Properties (Since: 2.5)
:   Properties for tls-creds-x509 objects.

    Members:
    :   - **sanity-check** (`boolean`, *optional*) – if true, perform some sanity checks before using the
          credentials (default: true)
        - **passwordid** (`string`, *optional*) – For the server-key.pem and client-key.pem files which
          contain sensitive private keys, it is possible to use an
          encrypted version by providing the `passwordid` parameter. This
          provides the ID of a previously created secret object containing
          the password for decryption.
        - The members of [`TlsCredsProperties`](qemu-qmp-ref.md#object-QMP-crypto.TlsCredsProperties "QMP:crypto.TlsCredsProperties").

*Enum* QCryptoAkCipherAlgo (Since: 7.1)
:   The supported algorithms for asymmetric encryption ciphers

    Values:
    :   - **rsa** – RSA algorithm

*Enum* QCryptoAkCipherKeyType (Since: 7.1)
:   The type of asymmetric keys.

    Values:
    :   - **public** – public key
        - **private** – private key

*Enum* QCryptoRSAPaddingAlgo (Since: 7.1)
:   The padding algorithm for RSA.

    Values:
    :   - **raw** – no padding used
        - **pkcs1** – pkcs1#v1.5

*Object* QCryptoAkCipherOptionsRSA (Since: 7.1)
:   Specific parameters for RSA algorithm.

    Members:
    :   - **hash-alg** ([`QCryptoHashAlgo`](qemu-qmp-ref.md#enum-QMP-crypto.QCryptoHashAlgo "QMP:crypto.QCryptoHashAlgo")) – [`QCryptoHashAlgo`](qemu-qmp-ref.md#enum-QMP-crypto.QCryptoHashAlgo "QMP:crypto.QCryptoHashAlgo")
        - **padding-alg** ([`QCryptoRSAPaddingAlgo`](qemu-qmp-ref.md#enum-QMP-crypto.QCryptoRSAPaddingAlgo "QMP:crypto.QCryptoRSAPaddingAlgo")) – [`QCryptoRSAPaddingAlgo`](qemu-qmp-ref.md#enum-QMP-crypto.QCryptoRSAPaddingAlgo "QMP:crypto.QCryptoRSAPaddingAlgo")

*Object* QCryptoAkCipherOptions (Since: 7.1)
:   The options that are available for all asymmetric key algorithms
    when creating a new QCryptoAkCipher.

    Members:
    :   - **alg** ([`QCryptoAkCipherAlgo`](qemu-qmp-ref.md#enum-QMP-crypto.QCryptoAkCipherAlgo "QMP:crypto.QCryptoAkCipherAlgo")) – encryption cipher algorithm
        - When `alg` is `rsa`: The members of [`QCryptoAkCipherOptionsRSA`](qemu-qmp-ref.md#object-QMP-crypto.QCryptoAkCipherOptionsRSA "QMP:crypto.QCryptoAkCipherOptionsRSA").

## [Background jobs](qemu-qmp-ref.md#id8)

*Enum* JobType (Since: 1.7)
:   Type of a background job.

    Values:
    :   - **commit** – block commit job type, see [`block-commit`](qemu-qmp-ref.md#command-QMP-block-core.block-commit "QMP:block-core.block-commit")
        - **stream** – block stream job type, see [`block-stream`](qemu-qmp-ref.md#command-QMP-block-core.block-stream "QMP:block-core.block-stream")
        - **mirror** – drive mirror job type, see [`drive-mirror`](qemu-qmp-ref.md#command-QMP-block-core.drive-mirror "QMP:block-core.drive-mirror")
        - **backup** – drive backup job type, see [`drive-backup`](qemu-qmp-ref.md#command-QMP-block-core.drive-backup "QMP:block-core.drive-backup")
        - **create** – image creation job type, see [`blockdev-create`](qemu-qmp-ref.md#command-QMP-block-core.blockdev-create "QMP:block-core.blockdev-create") (since 3.0)
        - **amend** – image options amend job type, see [`x-blockdev-amend`](qemu-qmp-ref.md#command-QMP-block-core.x-blockdev-amend "QMP:block-core.x-blockdev-amend")
          (since 5.1)
        - **snapshot-load** – snapshot load job type, see [`snapshot-load`](qemu-qmp-ref.md#command-QMP-migration.snapshot-load "QMP:migration.snapshot-load")
          (since 6.0)
        - **snapshot-save** – snapshot save job type, see [`snapshot-save`](qemu-qmp-ref.md#command-QMP-migration.snapshot-save "QMP:migration.snapshot-save")
          (since 6.0)
        - **snapshot-delete** – snapshot delete job type, see [`snapshot-delete`](qemu-qmp-ref.md#command-QMP-migration.snapshot-delete "QMP:migration.snapshot-delete")
          (since 6.0)

*Enum* JobStatus (Since: 2.12)
:   Indicates the present state of a given job in its lifetime.

    Values:
    :   - **undefined** – Erroneous, default state. Should not ever be visible.
        - **created** – The job has been created, but not yet started.
        - **running** – The job is currently running.
        - **paused** – The job is running, but paused. The pause may be requested
          by either the QMP user or by internal processes.
        - **ready** – The job is running, but is ready for the user to signal
          completion. This is used for long-running jobs like mirror that
          are designed to run indefinitely.
        - **standby** – The job is ready, but paused. This is nearly identical to
          `paused`. The job may return to `ready` or otherwise be canceled.
        - **waiting** – The job is waiting for other jobs in the transaction to
          converge to the waiting state. This status will likely not be
          visible for the last job in a transaction.
        - **pending** – The job has finished its work, but has finalization steps
          that it needs to make prior to completing. These changes will
          require manual intervention via [`job-finalize`](qemu-qmp-ref.md#command-QMP-job.job-finalize "QMP:job.job-finalize") if auto-finalize
          was set to false. These pending changes may still fail.
        - **aborting** – The job is in the process of being aborted, and will
          finish with an error. The job will afterwards report that it is
          `concluded`. This status may not be visible to the management
          process.
        - **concluded** – The job has finished all work. If auto-dismiss was set
          to false, the job will remain in this state until it is
          dismissed via [`job-dismiss`](qemu-qmp-ref.md#command-QMP-job.job-dismiss "QMP:job.job-dismiss").
        - **null** – The job is in the process of being dismantled. This state
          should not ever be visible externally.

*Enum* JobVerb (Since: 2.12)
:   Represents command verbs that can be applied to a job.

    Values:
    :   - **cancel** – see [`job-cancel`](qemu-qmp-ref.md#command-QMP-job.job-cancel "QMP:job.job-cancel")
        - **pause** – see [`job-pause`](qemu-qmp-ref.md#command-QMP-job.job-pause "QMP:job.job-pause")
        - **resume** – see [`job-resume`](qemu-qmp-ref.md#command-QMP-job.job-resume "QMP:job.job-resume")
        - **set-speed** – see [`block-job-set-speed`](qemu-qmp-ref.md#command-QMP-block-core.block-job-set-speed "QMP:block-core.block-job-set-speed")
        - **complete** – see [`job-complete`](qemu-qmp-ref.md#command-QMP-job.job-complete "QMP:job.job-complete")
        - **dismiss** – see [`job-dismiss`](qemu-qmp-ref.md#command-QMP-job.job-dismiss "QMP:job.job-dismiss")
        - **finalize** – see [`job-finalize`](qemu-qmp-ref.md#command-QMP-job.job-finalize "QMP:job.job-finalize")
        - **change** – see [`block-job-change`](qemu-qmp-ref.md#command-QMP-block-core.block-job-change "QMP:block-core.block-job-change") (since 8.2)

*Event* JOB_STATUS_CHANGE (Since: 3.0)
:   Emitted when a job transitions to a different status.

    Members:
    :   - **id** (`string`) – The job identifier
        - **status** ([`JobStatus`](qemu-qmp-ref.md#enum-QMP-job.JobStatus "QMP:job.JobStatus")) – The new job status

*Command* job-pause (Since: 3.0)
:   Pause an active job.

    This command returns immediately after marking the active job for
    pausing. Pausing an already paused job is an error.

    The job will pause as soon as possible, which means transitioning
    into the PAUSED state if it was RUNNING, or into STANDBY if it was
    READY. The corresponding [`JOB_STATUS_CHANGE`](qemu-qmp-ref.md#event-QMP-job.JOB_STATUS_CHANGE "QMP:job.JOB_STATUS_CHANGE") event will be emitted.

    Cancelling a paused job automatically resumes it.

    Arguments:
    :   - **id** (`string`) – The job identifier.

*Command* job-resume (Since: 3.0)
:   Resume a paused job.

    This command returns immediately after resuming a paused job.
    Resuming an already running job is an error.

    This command also clears the error status for block-jobs (stream,
    commit, mirror, backup).

    Arguments:
    :   - **id** (`string`) – The job identifier.

*Command* job-cancel (Since: 3.0)
:   Instruct an active background job to cancel at the next opportunity.
    This command returns immediately after marking the active job for
    cancellation.

    The job will cancel as soon as possible and then emit a
    [`JOB_STATUS_CHANGE`](qemu-qmp-ref.md#event-QMP-job.JOB_STATUS_CHANGE "QMP:job.JOB_STATUS_CHANGE") event. Usually, the status will change to
    ABORTING, but it is possible that a job successfully completes (e.g.
    because it was almost done and there was no opportunity to cancel
    earlier than completing the job) and transitions to PENDING instead.

    Arguments:
    :   - **id** (`string`) – The job identifier.

*Command* job-complete (Since: 3.0)
:   Manually trigger completion of an active job in the READY or STANDBY
    state. Completing the job in any other state is an error.

    This is supported only for drive mirroring, where it also switches
    the device to write to the target path only. Note that drive
    mirroring includes [`drive-mirror`](qemu-qmp-ref.md#command-QMP-block-core.drive-mirror "QMP:block-core.drive-mirror"), [`blockdev-mirror`](qemu-qmp-ref.md#command-QMP-block-core.blockdev-mirror "QMP:block-core.blockdev-mirror") and
    [`block-commit`](qemu-qmp-ref.md#command-QMP-block-core.block-commit "QMP:block-core.block-commit") job (only in case of “active commit”, when the node
    being committed is used by the guest). The ability to complete is
    signaled with a [`BLOCK_JOB_READY`](qemu-qmp-ref.md#event-QMP-block-core.BLOCK_JOB_READY "QMP:block-core.BLOCK_JOB_READY") event.

    This command completes an active background block operation
    synchronously. The ordering of this command’s return with the
    [`BLOCK_JOB_COMPLETED`](qemu-qmp-ref.md#event-QMP-block-core.BLOCK_JOB_COMPLETED "QMP:block-core.BLOCK_JOB_COMPLETED") event is not defined. Note that if an I/O
    error occurs during the processing of this command: 1) the command
    itself will fail; 2) the error will be processed according to the
    rerror/werror arguments that were specified when starting the
    operation.

    Arguments:
    :   - **id** (`string`) – The job identifier.

*Command* job-dismiss (Since: 3.0)
:   Deletes a job that is in the CONCLUDED state. This command only
    needs to be run explicitly for jobs that don’t have automatic
    dismiss enabled. In turn, automatic dismiss may be enabled only for
    jobs that have `auto-dismiss` option, which are [`drive-backup`](qemu-qmp-ref.md#command-QMP-block-core.drive-backup "QMP:block-core.drive-backup"),
    [`blockdev-backup`](qemu-qmp-ref.md#command-QMP-block-core.blockdev-backup "QMP:block-core.blockdev-backup"), [`drive-mirror`](qemu-qmp-ref.md#command-QMP-block-core.drive-mirror "QMP:block-core.drive-mirror"), [`blockdev-mirror`](qemu-qmp-ref.md#command-QMP-block-core.blockdev-mirror "QMP:block-core.blockdev-mirror"), [`block-commit`](qemu-qmp-ref.md#command-QMP-block-core.block-commit "QMP:block-core.block-commit")
    and [`block-stream`](qemu-qmp-ref.md#command-QMP-block-core.block-stream "QMP:block-core.block-stream"). `auto-dismiss` is enabled by default for these
    jobs.

    This command will refuse to operate on any job that has not yet
    reached its terminal state, CONCLUDED. For jobs that make use of
    the JOB_READY event, [`job-cancel`](qemu-qmp-ref.md#command-QMP-job.job-cancel "QMP:job.job-cancel") or [`job-complete`](qemu-qmp-ref.md#command-QMP-job.job-complete "QMP:job.job-complete") will still need
    to be used as appropriate.

    Arguments:
    :   - **id** (`string`) – The job identifier.

*Command* job-finalize (Since: 3.0)
:   Instructs all jobs in a transaction (or a single job if it is not
    part of any transaction) to finalize any graph changes and do any
    necessary cleanup. This command requires that all involved jobs are
    in the PENDING state.

    For jobs in a transaction, instructing one job to finalize will
    force ALL jobs in the transaction to finalize, so it is only
    necessary to instruct a single member job to finalize.

    The command is applicable only to jobs which have `auto-finalize`
    option and only when this option is set to false.

    Arguments:
    :   - **id** (`string`) – The identifier of any job in the transaction, or of a job that
          is not part of any transaction.

*Object* JobInfo (Since: 3.0)
:   Information about a job.

    Members:
    :   - **id** (`string`) – The job identifier
        - **type** ([`JobType`](qemu-qmp-ref.md#enum-QMP-job.JobType "QMP:job.JobType")) – The kind of job that is being performed
        - **status** ([`JobStatus`](qemu-qmp-ref.md#enum-QMP-job.JobStatus "QMP:job.JobStatus")) – Current job state/status
        - **current-progress** (`int`) – Progress made until now. The unit is arbitrary
          and the value can only meaningfully be used for the ratio of
          `current-progress` to `total-progress`. The value is
          monotonically increasing.
        - **total-progress** (`int`) – Estimated `current-progress` value at the completion
          of the job. This value can arbitrarily change while the job is
          running, in both directions.
        - **error** (`string`, *optional*) –

          If this field is present, the job failed; if it is still
          missing in the CONCLUDED state, this indicates successful
          completion.

          The value is a human-readable error message to describe the
          reason for the job failure. It should not be parsed by
          applications.

*Command* query-jobs (Since: 3.0)
:   Return information about jobs.

    Return:
    :   `[`[`JobInfo`](qemu-qmp-ref.md#object-QMP-job.JobInfo "QMP:job.JobInfo")`]` – a list with info for each active job

## [Accelerators](qemu-qmp-ref.md#id9)

*Object* KvmInfo (Since: 0.14)
:   Information about support for KVM acceleration

    Members:
    :   - **enabled** (`boolean`) – true if KVM acceleration is active
        - **present** (`boolean`) – true if KVM acceleration is built into this executable

*Command* query-kvm (Since: 0.14)
:   This command is deprecated.

    Return information about KVM acceleration

    Return:
    :   [`KvmInfo`](qemu-qmp-ref.md#object-QMP-accelerator.KvmInfo "QMP:accelerator.KvmInfo")

    Features:
    :   - **deprecated** – This command is deprecated. Use [`query-accelerators`](qemu-qmp-ref.md#command-QMP-accelerator.query-accelerators "QMP:accelerator.query-accelerators")
          instead.

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "query-kvm" }
    > <- { "return": { "enabled": true, "present": true } }
    > ```

*Command* x-accel-stats (Since: 10.1)
:   This command is unstable/experimental.

    Query accelerator statistics

    Features:
    :   - **unstable** – This command is meant for debugging.

    Return:
    :   [`HumanReadableText`](qemu-qmp-ref.md#object-QMP-common.HumanReadableText "QMP:common.HumanReadableText") – accelerator statistics

*Enum* Accelerator (Since: 10.2.0)
:   Information about support for MSHV acceleration

    Values:
    :   - **hvf** – Apple Hypervisor.framework
        - **kvm** – KVM
        - **mshv** – Hyper-V
        - **nvmm** – NetBSD NVMM
        - **qtest** – QTest (dummy accelerator)
        - **tcg** – TCG (dynamic translation)
        - **whpx** – Windows Hypervisor Platform
        - **xen** – Xen

*Object* AcceleratorInfo (Since: 10.2.0)
:   Information about support for various accelerators

    Members:
    :   - **enabled** ([`Accelerator`](qemu-qmp-ref.md#enum-QMP-accelerator.Accelerator "QMP:accelerator.Accelerator")) – the accelerator that is in use
        - **present** (`[`[`Accelerator`](qemu-qmp-ref.md#enum-QMP-accelerator.Accelerator "QMP:accelerator.Accelerator")`]`) – the list of accelerators that are built into this
          executable

*Command* query-accelerators (Since: 10.2.0)
:   Return information about accelerators

    Return:
    :   [`AcceleratorInfo`](qemu-qmp-ref.md#object-QMP-accelerator.AcceleratorInfo "QMP:accelerator.AcceleratorInfo") – `AcceleratorInfo`

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "query-accelerators" }
    > <- { "return": { "enabled": "mshv", "present": ["kvm", "mshv", "qtest", "tcg"] } }
    > ```

## [Block devices](qemu-qmp-ref.md#id10)

### [Block core (VM unrelated)](qemu-qmp-ref.md#id11)

*Object* SnapshotInfo (Since: 1.3)
:   Members:
    :   - **id** (`string`) – unique snapshot id
        - **name** (`string`) – user chosen name
        - **vm-state-size** (`int`) – size of the VM state
        - **date-sec** (`int`) – UTC date of the snapshot in seconds
        - **date-nsec** (`int`) – fractional part in nano seconds to be used with date-sec
        - **vm-clock-sec** (`int`) – VM clock relative to boot in seconds
        - **vm-clock-nsec** (`int`) – fractional part in nano seconds to be used with
          vm-clock-sec
        - **icount** (`int`, *optional*) – Current instruction count. Appears when execution
          record/replay is enabled. Used for “time-traveling” to match
          the moment in the recorded execution with the snapshots. This
          counter may be obtained through [`query-replay`](qemu-qmp-ref.md#command-QMP-replay.query-replay "QMP:replay.query-replay") command
          (since 5.2)

*Object* ImageInfoSpecificQCow2EncryptionBase (Since: 2.10)
:   Members:
    :   - **format** ([`BlockdevQcow2EncryptionFormat`](qemu-qmp-ref.md#enum-QMP-block-core.BlockdevQcow2EncryptionFormat "QMP:block-core.BlockdevQcow2EncryptionFormat")) – The encryption format

*Object* ImageInfoSpecificQCow2Encryption (Since: 2.10)
:   Members:
    :   - The members of [`ImageInfoSpecificQCow2EncryptionBase`](qemu-qmp-ref.md#object-QMP-block-core.ImageInfoSpecificQCow2EncryptionBase "QMP:block-core.ImageInfoSpecificQCow2EncryptionBase").
        - When `format` is `luks`: The members of [`QCryptoBlockInfoLUKS`](qemu-qmp-ref.md#object-QMP-crypto.QCryptoBlockInfoLUKS "QMP:crypto.QCryptoBlockInfoLUKS").

*Object* ImageInfoSpecificQCow2 (Since: 1.7)
:   Members:
    :   - **compat** (`string`) – compatibility level
        - **data-file** (`string`, *optional*) – the filename of the external data file that is stored in
          the image and used as a default for opening the image
          (since: 4.0)
        - **data-file-raw** (`boolean`, *optional*) – True if the external data file must stay valid as a
          standalone (read-only) raw image without looking at qcow2
          metadata (since: 4.0)
        - **extended-l2** (`boolean`, *optional*) – true if the image has extended L2 entries; only valid
          for compat >= 1.1 (since 5.2)
        - **lazy-refcounts** (`boolean`, *optional*) – on or off; only valid for compat >= 1.1
        - **corrupt** (`boolean`, *optional*) – true if the image has been marked corrupt; only valid for
          compat >= 1.1 (since 2.2)
        - **refcount-bits** (`int`) – width of a refcount entry in bits (since 2.3)
        - **encrypt** ([`ImageInfoSpecificQCow2Encryption`](qemu-qmp-ref.md#object-QMP-block-core.ImageInfoSpecificQCow2Encryption "QMP:block-core.ImageInfoSpecificQCow2Encryption"), *optional*) – details about encryption parameters; only set if image is
          encrypted (since 2.10)
        - **bitmaps** (`[`[`Qcow2BitmapInfo`](qemu-qmp-ref.md#object-QMP-block-core.Qcow2BitmapInfo "QMP:block-core.Qcow2BitmapInfo")`]`, *optional*) – A list of qcow2 bitmap details (since 4.0)
        - **compression-type** ([`Qcow2CompressionType`](qemu-qmp-ref.md#enum-QMP-block-core.Qcow2CompressionType "QMP:block-core.Qcow2CompressionType")) – the image cluster compression method (since 5.1)

*Object* ImageInfoSpecificVmdk (Since: 1.7)
:   Members:
    :   - **create-type** (`string`) – The create type of VMDK image
        - **cid** (`int`) – Content id of image
        - **parent-cid** (`int`) – Parent VMDK image’s cid
        - **extents** (`[`[`VmdkExtentInfo`](qemu-qmp-ref.md#object-QMP-block-core.VmdkExtentInfo "QMP:block-core.VmdkExtentInfo")`]`) – List of extent files

*Object* VmdkExtentInfo (Since: 8.0)
:   Information about a VMDK extent file

    Members:
    :   - **filename** (`string`) – Name of the extent file
        - **format** (`string`) – Extent type (e.g. FLAT or SPARSE)
        - **virtual-size** (`int`) – Number of bytes covered by this extent
        - **cluster-size** (`int`, *optional*) – Cluster size in bytes (for non-flat extents)
        - **compressed** (`boolean`, *optional*) – Whether this extent contains compressed data

*Object* ImageInfoSpecificRbd (Since: 6.1)
:   Members:
    :   - **encryption-format** ([`RbdImageEncryptionFormat`](qemu-qmp-ref.md#enum-QMP-block-core.RbdImageEncryptionFormat "QMP:block-core.RbdImageEncryptionFormat"), *optional*) – Image encryption format. If encryption is
          enabled for the image (see encrypted in BlockNodeInfo), this is
          the actual format in which the image is accessed. If encryption
          is not enabled, this is the result of probing when the image was
          opened, to give a suggestion which encryption format could be
          enabled. Note that probing results can be changed by the guest
          by writing a (possibly partial) encryption format header to the
          image, so don’t treat this information as trusted if the guest
          is not trusted.

*Object* ImageInfoSpecificFile (Since: 8.0)
:   Members:
    :   - **extent-size-hint** (`int`, *optional*) – Extent size hint (if available)

*Enum* ImageInfoSpecificKind (Since: 1.7)
:   Values:
    :   - **luks** – Since 2.7
        - **rbd** – Since 6.1
        - **file** – Since 8.0
        - **qcow2** – Not documented
        - **vmdk** – Not documented

*Object* ImageInfoSpecificQCow2Wrapper (Since: 1.7)
:   Members:
    :   - **data** ([`ImageInfoSpecificQCow2`](qemu-qmp-ref.md#object-QMP-block-core.ImageInfoSpecificQCow2 "QMP:block-core.ImageInfoSpecificQCow2")) – image information specific to QCOW2

*Object* ImageInfoSpecificVmdkWrapper (Since: 6.1)
:   Members:
    :   - **data** ([`ImageInfoSpecificVmdk`](qemu-qmp-ref.md#object-QMP-block-core.ImageInfoSpecificVmdk "QMP:block-core.ImageInfoSpecificVmdk")) – image information specific to VMDK

*Object* ImageInfoSpecificLUKSWrapper (Since: 2.7)
:   Members:
    :   - **data** ([`QCryptoBlockInfoLUKS`](qemu-qmp-ref.md#object-QMP-crypto.QCryptoBlockInfoLUKS "QMP:crypto.QCryptoBlockInfoLUKS")) – image information specific to LUKS

*Object* ImageInfoSpecificRbdWrapper (Since: 6.1)
:   Members:
    :   - **data** ([`ImageInfoSpecificRbd`](qemu-qmp-ref.md#object-QMP-block-core.ImageInfoSpecificRbd "QMP:block-core.ImageInfoSpecificRbd")) – image information specific to RBD

*Object* ImageInfoSpecificFileWrapper (Since: 8.0)
:   Members:
    :   - **data** ([`ImageInfoSpecificFile`](qemu-qmp-ref.md#object-QMP-block-core.ImageInfoSpecificFile "QMP:block-core.ImageInfoSpecificFile")) – image information specific to files

*Object* ImageInfoSpecific (Since: 1.7)
:   A discriminated record of image format specific information
    structures.

    Members:
    :   - **type** ([`ImageInfoSpecificKind`](qemu-qmp-ref.md#enum-QMP-block-core.ImageInfoSpecificKind "QMP:block-core.ImageInfoSpecificKind")) – block driver name
        - When `type` is `qcow2`: The members of [`ImageInfoSpecificQCow2Wrapper`](qemu-qmp-ref.md#object-QMP-block-core.ImageInfoSpecificQCow2Wrapper "QMP:block-core.ImageInfoSpecificQCow2Wrapper").
        - When `type` is `vmdk`: The members of [`ImageInfoSpecificVmdkWrapper`](qemu-qmp-ref.md#object-QMP-block-core.ImageInfoSpecificVmdkWrapper "QMP:block-core.ImageInfoSpecificVmdkWrapper").
        - When `type` is `luks`: The members of [`ImageInfoSpecificLUKSWrapper`](qemu-qmp-ref.md#object-QMP-block-core.ImageInfoSpecificLUKSWrapper "QMP:block-core.ImageInfoSpecificLUKSWrapper").
        - When `type` is `rbd`: The members of [`ImageInfoSpecificRbdWrapper`](qemu-qmp-ref.md#object-QMP-block-core.ImageInfoSpecificRbdWrapper "QMP:block-core.ImageInfoSpecificRbdWrapper").
        - When `type` is `file`: The members of [`ImageInfoSpecificFileWrapper`](qemu-qmp-ref.md#object-QMP-block-core.ImageInfoSpecificFileWrapper "QMP:block-core.ImageInfoSpecificFileWrapper").

*Object* BlockLimitsInfo
:   Members:
    :   - **request-alignment** (`int`) – Alignment requirement, in bytes, for
          offset/length of I/O requests.
        - **max-discard** (`int`, *optional*) – Maximum number of bytes that can be discarded at once.
          If not present, there is no specific maximum.
        - **discard-alignment** (`int`, *optional*) – Optimal alignment for discard requests in bytes.
          Note that this doesn’t have to be a power of two. If not
          present, discards don’t have a alignment requirement different
          from `request-alignment`.
        - **max-write-zeroes** (`int`, *optional*) – Maximum number of bytes that can be zeroed out at
          once. If not present, there is no specific maximum.
        - **write-zeroes-alignment** (`int`, *optional*) – Optimal alignment for write zeroes requests
          in bytes. Note that this doesn’t have to be a power of two. If
          not present, write_zeroes doesn’t have a alignment requirement
          different from `request-alignment`.
        - **opt-transfer** (`int`, *optional*) – Optimal transfer length in bytes. If not present,
          there is no preferred size.
        - **max-transfer** (`int`, *optional*) – Maximal transfer length in bytes. If not present,
          there is no specific maximum.
        - **max-hw-transfer** (`int`, *optional*) – Maximal hardware transfer length in bytes.
          Applies whenever transfers to the device bypass the kernel I/O
          scheduler, for example with SG_IO. If not present, there is no
          specific maximum.
        - **max-iov** (`int`) – Maximum number of scatter/gather elements
        - **max-hw-iov** (`int`, *optional*) – Maximum number of scatter/gather elements allowed by
          the hardware. Applies whenever transfers to the device bypass
          the kernel I/O scheduler, for example with SG_IO. If not
          present, the hardware limits is unknown and `max-iov` is always
          used.
        - **min-mem-alignment** (`int`) – Minimal required memory alignment in bytes for
          zero-copy I/O to succeed. For unaligned requests, a bounce
          buffer will be used.
        - **opt-mem-alignment** (`int`) – Optimal memory alignment in bytes. This is the
          alignment used for any buffer allocations QEMU performs
          internally.

*Object* BlockNodeInfo (Since: 8.0)
:   Information about a QEMU image file

    Members:
    :   - **filename** (`string`) – name of the image file
        - **format** (`string`) – format of the image file
        - **virtual-size** (`int`) – maximum capacity in bytes of the image
        - **actual-size** (`int`, *optional*) – actual size on disk in bytes of the image
        - **dirty-flag** (`boolean`, *optional*) – true if image is not cleanly closed
        - **cluster-size** (`int`, *optional*) – size of a cluster in bytes
        - **encrypted** (`boolean`, *optional*) – true if the image is encrypted
        - **compressed** (`boolean`, *optional*) – true if the image is compressed (Since 1.7)
        - **backing-filename** (`string`, *optional*) – name of the backing file
        - **full-backing-filename** (`string`, *optional*) – full path of the backing file
        - **backing-filename-format** (`string`, *optional*) – the format of the backing file
        - **snapshots** (`[`[`SnapshotInfo`](qemu-qmp-ref.md#object-QMP-block-core.SnapshotInfo "QMP:block-core.SnapshotInfo")`]`, *optional*) – list of VM snapshots
        - **limits** ([`BlockLimitsInfo`](qemu-qmp-ref.md#object-QMP-block-core.BlockLimitsInfo "QMP:block-core.BlockLimitsInfo"), *optional*) – block limits that are used for I/O on the node (Since 10.2)
        - **format-specific** ([`ImageInfoSpecific`](qemu-qmp-ref.md#object-QMP-block-core.ImageInfoSpecific "QMP:block-core.ImageInfoSpecific"), *optional*) – structure supplying additional format-specific
          information (since 1.7)

*Object* ImageInfo (Since: 1.3)
:   Information about a QEMU image file, and potentially its backing
    image

    Members:
    :   - **backing-image** ([`ImageInfo`](qemu-qmp-ref.md#object-QMP-block-core.ImageInfo "QMP:block-core.ImageInfo"), *optional*) – info of the backing image
        - The members of [`BlockNodeInfo`](qemu-qmp-ref.md#object-QMP-block-core.BlockNodeInfo "QMP:block-core.BlockNodeInfo").

*Object* BlockChildInfo (Since: 8.0)
:   Information about all nodes in the block graph starting at some
    node, annotated with information about that node in relation to its
    parent.

    Members:
    :   - **name** (`string`) – Child name of the root node in the [`BlockGraphInfo`](qemu-qmp-ref.md#object-QMP-block-core.BlockGraphInfo "QMP:block-core.BlockGraphInfo") struct,
          in its role as the child of some undescribed parent node
        - **info** ([`BlockGraphInfo`](qemu-qmp-ref.md#object-QMP-block-core.BlockGraphInfo "QMP:block-core.BlockGraphInfo")) – Block graph information starting at this node

*Object* BlockGraphInfo (Since: 8.0)
:   Information about all nodes in a block (sub)graph in the form of
    [`BlockNodeInfo`](qemu-qmp-ref.md#object-QMP-block-core.BlockNodeInfo "QMP:block-core.BlockNodeInfo") data. The base [`BlockNodeInfo`](qemu-qmp-ref.md#object-QMP-block-core.BlockNodeInfo "QMP:block-core.BlockNodeInfo") struct contains the
    information for the (sub)graph’s root node.

    Members:
    :   - **children** (`[`[`BlockChildInfo`](qemu-qmp-ref.md#object-QMP-block-core.BlockChildInfo "QMP:block-core.BlockChildInfo")`]`) – Array of links to this node’s child nodes’ information
        - The members of [`BlockNodeInfo`](qemu-qmp-ref.md#object-QMP-block-core.BlockNodeInfo "QMP:block-core.BlockNodeInfo").

*Object* ImageCheck (Since: 1.4)
:   Information about a QEMU image file check

    Members:
    :   - **filename** (`string`) – name of the image file checked
        - **format** (`string`) – format of the image file checked
        - **check-errors** (`int`) – number of unexpected errors occurred during check
        - **image-end-offset** (`int`, *optional*) – offset (in bytes) where the image ends, this
          field is present if the driver for the image format supports it
        - **corruptions** (`int`, *optional*) – number of corruptions found during the check if any
        - **leaks** (`int`, *optional*) – number of leaks found during the check if any
        - **corruptions-fixed** (`int`, *optional*) – number of corruptions fixed during the check if
          any
        - **leaks-fixed** (`int`, *optional*) – number of leaks fixed during the check if any
        - **total-clusters** (`int`, *optional*) – total number of clusters, this field is present if
          the driver for the image format supports it
        - **allocated-clusters** (`int`, *optional*) – total number of allocated clusters, this field
          is present if the driver for the image format supports it
        - **fragmented-clusters** (`int`, *optional*) – total number of fragmented clusters, this
          field is present if the driver for the image format supports it
        - **compressed-clusters** (`int`, *optional*) – total number of compressed clusters, this
          field is present if the driver for the image format supports it

*Object* MapEntry (Since: 2.6)
:   Mapping information from a virtual block range to a host file range

    Members:
    :   - **start** (`int`) – virtual (guest) offset of the first byte described by this
          entry
        - **length** (`int`) – the number of bytes of the mapped virtual range
        - **data** (`boolean`) – reading the image will actually read data from a file (in
          particular, if `offset` is present this means that the sectors
          are not simply preallocated, but contain actual data in raw
          format)
        - **zero** (`boolean`) – whether the virtual blocks read as zeroes
        - **compressed** (`boolean`) – true if the data is stored compressed (since 8.2)
        - **depth** (`int`) – number of layers (0 = top image, 1 = top image’s backing
          file, …, n - 1 = bottom image (where n is the number of images
          in the chain)) before reaching one for which the range is
          allocated
        - **present** (`boolean`) – true if this layer provides the data, false if adding a
          backing layer could impact this region (since 6.1)
        - **offset** (`int`, *optional*) – if present, the image file stores the data for this range
          in raw format at the given (host) offset
        - **filename** (`string`, *optional*) – filename that is referred to by `offset`

*Object* BlockdevCacheInfo (Since: 2.3)
:   Cache mode information for a block device

    Members:
    :   - **writeback** (`boolean`) – true if writeback mode is enabled
        - **direct** (`boolean`) – true if the host page cache is bypassed (O_DIRECT)
        - **no-flush** (`boolean`) – true if flush requests are ignored for the device

*Object* BlockdevChild (Since: 10.1)
:   Members:
    :   - **child** (`string`) – The name of the child, for example ‘file’ or ‘backing’.
        - **node-name** (`string`) – The name of the child’s block driver node.

*Object* BlockDeviceInfo (Since: 0.14)
:   Information about the backing device for a block device.

    Members:
    :   - **file** (`string`) – the filename of the backing device
        - **node-name** (`string`) – the name of the block driver node (Since 2.0)
        - **ro** (`boolean`) – true if the backing device was open read-only
        - **drv** (`string`) – the name of the block format used to open the backing device.
          As of 0.14 this can be: ‘blkdebug’, ‘bochs’, ‘cloop’, ‘cow’,
          ‘dmg’, ‘file’, ‘file’, ‘ftp’, ‘ftps’, ‘host_cdrom’,
          ‘host_device’, ‘http’, ‘https’, ‘luks’, ‘nbd’, ‘parallels’,
          ‘qcow’, ‘qcow2’, ‘raw’, ‘vdi’, ‘vmdk’, ‘vpc’, ‘vvfat’ 2.2:
          ‘archipelago’ added, ‘cow’ dropped 2.3: ‘host_floppy’ deprecated
          2.5: ‘host_floppy’ dropped 2.6: ‘luks’ added 2.8: ‘replication’
          added, ‘tftp’ dropped 2.9: ‘archipelago’ dropped
        - **backing_file** (`string`, *optional*) – the name of the backing file (for copy-on-write)
        - **backing_file_depth** (`int`) – number of files in the backing file chain
          (since: 1.2)
        - **children** (`[`[`BlockdevChild`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevChild "QMP:block-core.BlockdevChild")`]`) – Information about child block nodes. (since: 10.1)
        - **active** (`boolean`) – true if the backend is active; typical cases for inactive
          backends are on the migration source instance after migration
          completes and on the destination before it completes.
          (since: 10.0)
        - **encrypted** (`boolean`) – true if the backing device is encrypted
        - **detect_zeroes** ([`BlockdevDetectZeroesOptions`](qemu-qmp-ref.md#enum-QMP-block-core.BlockdevDetectZeroesOptions "QMP:block-core.BlockdevDetectZeroesOptions")) – detect and optimize zero writes (Since 2.1)
        - **bps** (`int`) – total throughput limit in bytes per second is specified
        - **bps_rd** (`int`) – read throughput limit in bytes per second is specified
        - **bps_wr** (`int`) – write throughput limit in bytes per second is specified
        - **iops** (`int`) – total I/O operations per second is specified
        - **iops_rd** (`int`) – read I/O operations per second is specified
        - **iops_wr** (`int`) – write I/O operations per second is specified
        - **image** ([`ImageInfo`](qemu-qmp-ref.md#object-QMP-block-core.ImageInfo "QMP:block-core.ImageInfo")) – the info of image used (since: 1.6)
        - **bps_max** (`int`, *optional*) – total throughput limit during bursts, in bytes (Since 1.7)
        - **bps_rd_max** (`int`, *optional*) – read throughput limit during bursts, in bytes
          (Since 1.7)
        - **bps_wr_max** (`int`, *optional*) – write throughput limit during bursts, in bytes
          (Since 1.7)
        - **iops_max** (`int`, *optional*) – total I/O operations per second during bursts, in bytes
          (Since 1.7)
        - **iops_rd_max** (`int`, *optional*) – read I/O operations per second during bursts, in bytes
          (Since 1.7)
        - **iops_wr_max** (`int`, *optional*) – write I/O operations per second during bursts, in
          bytes (Since 1.7)
        - **bps_max_length** (`int`, *optional*) – maximum length of the `bps_max` burst period, in
          seconds. (Since 2.6)
        - **bps_rd_max_length** (`int`, *optional*) – maximum length of the `bps_rd_max` burst period,
          in seconds. (Since 2.6)
        - **bps_wr_max_length** (`int`, *optional*) – maximum length of the `bps_wr_max` burst period,
          in seconds. (Since 2.6)
        - **iops_max_length** (`int`, *optional*) – maximum length of the `iops` burst period, in
          seconds. (Since 2.6)
        - **iops_rd_max_length** (`int`, *optional*) – maximum length of the `iops_rd_max` burst
          period, in seconds. (Since 2.6)
        - **iops_wr_max_length** (`int`, *optional*) – maximum length of the `iops_wr_max` burst
          period, in seconds. (Since 2.6)
        - **iops_size** (`int`, *optional*) – an I/O size in bytes (Since 1.7)
        - **group** (`string`, *optional*) – throttle group name (Since 2.4)
        - **cache** ([`BlockdevCacheInfo`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevCacheInfo "QMP:block-core.BlockdevCacheInfo")) – the cache mode used for the block device (since: 2.3)
        - **write_threshold** (`int`) – configured write threshold for the device. 0 if
          disabled. (Since 2.3)
        - **dirty-bitmaps** (`[`[`BlockDirtyInfo`](qemu-qmp-ref.md#object-QMP-block-core.BlockDirtyInfo "QMP:block-core.BlockDirtyInfo")`]`, *optional*) – dirty bitmaps information (only present if node has
          one or more dirty bitmaps) (Since 4.2)

*Enum* BlockDeviceIoStatus (Since: 1.0)
:   An enumeration of block device I/O status.

    Values:
    :   - **ok** – The last I/O operation has succeeded
        - **failed** – The last I/O operation has failed
        - **nospace** – The last I/O operation has failed due to a no-space
          condition

*Object* BlockDirtyInfo (Since: 1.3)
:   Block dirty bitmap information.

    Members:
    :   - **name** (`string`, *optional*) – the name of the dirty bitmap (Since 2.4)
        - **count** (`int`) – number of dirty bytes according to the dirty bitmap
        - **granularity** (`int`) – granularity of the dirty bitmap in bytes (since 1.4)
        - **recording** (`boolean`) – true if the bitmap is recording new writes from the
          guest. (since 4.0)
        - **busy** (`boolean`) – true if the bitmap is in-use by some operation (NBD or jobs)
          and cannot be modified via QMP or used by another operation.
          (since 4.0)
        - **persistent** (`boolean`) – true if the bitmap was stored on disk, is scheduled to
          be stored on disk, or both. (since 4.0)
        - **inconsistent** (`boolean`, *optional*) – true if this is a persistent bitmap that was
          improperly stored. Implies `persistent` to be true; `recording`
          and `busy` to be false. This bitmap cannot be used. To remove
          it, use [`block-dirty-bitmap-remove`](qemu-qmp-ref.md#command-QMP-block-core.block-dirty-bitmap-remove "QMP:block-core.block-dirty-bitmap-remove"). (Since 4.0)

*Enum* Qcow2BitmapInfoFlags (Since: 4.0)
:   An enumeration of flags that a bitmap can report to the user.

    Values:
    :   - **in-use** – This flag is set by any process actively modifying the
          qcow2 file, and cleared when the updated bitmap is flushed to
          the qcow2 image. The presence of this flag in an offline image
          means that the bitmap was not saved correctly after its last
          usage, and may contain inconsistent data.
        - **auto** – The bitmap must reflect all changes of the virtual disk by
          any application that would write to this qcow2 file.

*Object* Qcow2BitmapInfo (Since: 4.0)
:   Qcow2 bitmap information.

    Members:
    :   - **name** (`string`) – the name of the bitmap
        - **granularity** (`int`) – granularity of the bitmap in bytes
        - **flags** (`[`[`Qcow2BitmapInfoFlags`](qemu-qmp-ref.md#enum-QMP-block-core.Qcow2BitmapInfoFlags "QMP:block-core.Qcow2BitmapInfoFlags")`]`) – flags of the bitmap

*Object* BlockLatencyHistogramInfo (Since: 4.0)
:   Block latency histogram.

    Members:
    :   - **boundaries** (`[``int``]`) – list of interval boundary values in nanoseconds, all
          greater than zero and in ascending order. For example, the list
          [10, 50, 100] produces the following histogram intervals: [0,
          10), [10, 50), [50, 100), [100, +inf).
        - **bins** (`[``int``]`) –

          list of io request counts corresponding to histogram
          intervals, one more element than `boundaries` has. For the
          example above, `bins` may be something like [3, 1, 5, 2], and
          corresponding histogram looks like:

          ```
          5|           *
          4|           *
          3| *         *
          2| *         *    *
          1| *    *    *    *
           +------------------
               10   50   100
          ```

*Object* BlockInfo (Since: 0.14)
:   Block device information. This structure describes a virtual device
    and the backing device associated with it.

    Members:
    :   - **device** (`string`) – The device name associated with the virtual device.
        - **qdev** (`string`, *optional*) – The qdev ID, or if no ID is assigned, the QOM path of the
          block device. (since 2.10)
        - **type** (`string`) – This field is returned only for compatibility reasons, it
          should not be used (always returns ‘unknown’)
        - **removable** (`boolean`) – True if the device supports removable media.
        - **locked** (`boolean`) – True if the guest has locked this device from having its
          media removed
        - **tray_open** (`boolean`, *optional*) – True if the device’s tray is open (only present if it
          has a tray)
        - **io-status** ([`BlockDeviceIoStatus`](qemu-qmp-ref.md#enum-QMP-block-core.BlockDeviceIoStatus "QMP:block-core.BlockDeviceIoStatus"), *optional*) – [`BlockDeviceIoStatus`](qemu-qmp-ref.md#enum-QMP-block-core.BlockDeviceIoStatus "QMP:block-core.BlockDeviceIoStatus"). Only present if the device
          supports it and the VM is configured to stop on errors
          (supported device models: virtio-blk, IDE, SCSI except
          scsi-generic)
        - **inserted** ([`BlockDeviceInfo`](qemu-qmp-ref.md#object-QMP-block-core.BlockDeviceInfo "QMP:block-core.BlockDeviceInfo"), *optional*) – [`BlockDeviceInfo`](qemu-qmp-ref.md#object-QMP-block-core.BlockDeviceInfo "QMP:block-core.BlockDeviceInfo") describing the device if media is
          present

*Object* BlockMeasureInfo (Since: 2.10)
:   Image file size calculation information. This structure describes
    the size requirements for creating a new image file.

    The size requirements depend on the new image file format. File
    size always equals virtual disk size for the ‘raw’ format, even for
    sparse POSIX files. Compact formats such as ‘qcow2’ represent
    unallocated and zero regions efficiently so file size may be smaller
    than virtual disk size.

    The values are upper bounds that are guaranteed to fit the new image
    file. Subsequent modification, such as internal snapshot or further
    bitmap creation, may require additional space and is not covered
    here.

    Members:
    :   - **required** (`int`) – Size required for a new image file, in bytes, when
          copying just allocated guest-visible contents.
        - **fully-allocated** (`int`) – Image file size, in bytes, once data has been
          written to all sectors, when copying just guest-visible
          contents.
        - **bitmaps** (`int`, *optional*) – Additional size required if all the top-level bitmap
          metadata in the source image were to be copied to the
          destination, present only when source and destination both
          support persistent bitmaps. (since 5.1)

*Command* query-block (Since: 0.14)
:   Get a list of [`BlockInfo`](qemu-qmp-ref.md#object-QMP-block-core.BlockInfo "QMP:block-core.BlockInfo") for all virtual block devices.

    Arguments:
    :   - **flat** (`boolean`, *optional*) – Omit nested data about the backing image, i.e. [`BlockInfo`](qemu-qmp-ref.md#object-QMP-block-core.BlockInfo "QMP:block-core.BlockInfo")
          member ‘inserted.image.backing-image’ will be absent.
          Default is false. (Since 11.0)

    Return:
    :   `[`[`BlockInfo`](qemu-qmp-ref.md#object-QMP-block-core.BlockInfo "QMP:block-core.BlockInfo")`]` – a list describing each virtual block device. Filter nodes
        that were created implicitly are skipped over.

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "query-block" }
    > <- {
    >       "return":[
    >          {
    >             "io-status": "ok",
    >             "device":"ide0-hd0",
    >             "locked":false,
    >             "removable":false,
    >             "inserted":{
    >                "ro":false,
    >                "drv":"qcow2",
    >                "encrypted":false,
    >                "file":"disks/test.qcow2",
    >                "backing_file_depth":1,
    >                "bps":1000000,
    >                "bps_rd":0,
    >                "bps_wr":0,
    >                "iops":1000000,
    >                "iops_rd":0,
    >                "iops_wr":0,
    >                "bps_max": 8000000,
    >                "bps_rd_max": 0,
    >                "bps_wr_max": 0,
    >                "iops_max": 0,
    >                "iops_rd_max": 0,
    >                "iops_wr_max": 0,
    >                "iops_size": 0,
    >                "detect_zeroes": "on",
    >                "write_threshold": 0,
    >                "image":{
    >                   "filename":"disks/test.qcow2",
    >                   "format":"qcow2",
    >                   "virtual-size":2048000,
    >                   "backing_file":"base.qcow2",
    >                   "full-backing-filename":"disks/base.qcow2",
    >                   "backing-filename-format":"qcow2",
    >                   "snapshots":[
    >                      {
    >                         "id": "1",
    >                         "name": "snapshot1",
    >                         "vm-state-size": 0,
    >                         "date-sec": 10000200,
    >                         "date-nsec": 12,
    >                         "vm-clock-sec": 206,
    >                         "vm-clock-nsec": 30
    >                      }
    >                   ],
    >                   "backing-image":{
    >                       "filename":"disks/base.qcow2",
    >                       "format":"qcow2",
    >                       "virtual-size":2048000
    >                   }
    >                }
    >             },
    >             "qdev": "ide_disk",
    >             "type":"unknown"
    >          },
    >          {
    >             "io-status": "ok",
    >             "device":"ide1-cd0",
    >             "locked":false,
    >             "removable":true,
    >             "qdev": "/machine/unattached/device[23]",
    >             "tray_open": false,
    >             "type":"unknown"
    >          },
    >          {
    >             "device":"floppy0",
    >             "locked":false,
    >             "removable":true,
    >             "qdev": "/machine/unattached/device[20]",
    >             "type":"unknown"
    >          },
    >          {
    >             "device":"sd0",
    >             "locked":false,
    >             "removable":true,
    >             "type":"unknown"
    >          }
    >       ]
    >    }
    > ```

*Object* BlockDeviceTimedStats (Since: 2.5)
:   Statistics of a block device during a given interval of time.

    Members:
    :   - **interval_length** (`int`) – Interval used for calculating the statistics, in
          seconds.
        - **min_rd_latency_ns** (`int`) – Minimum latency of read operations in the
          defined interval, in nanoseconds.
        - **min_wr_latency_ns** (`int`) – Minimum latency of write operations in the
          defined interval, in nanoseconds.
        - **min_zone_append_latency_ns** (`int`) – Minimum latency of zone append
          operations in the defined interval, in nanoseconds (since 8.1)
        - **min_flush_latency_ns** (`int`) – Minimum latency of flush operations in the
          defined interval, in nanoseconds.
        - **max_rd_latency_ns** (`int`) – Maximum latency of read operations in the
          defined interval, in nanoseconds.
        - **max_wr_latency_ns** (`int`) – Maximum latency of write operations in the
          defined interval, in nanoseconds.
        - **max_zone_append_latency_ns** (`int`) – Maximum latency of zone append
          operations in the defined interval, in nanoseconds (since 8.1)
        - **max_flush_latency_ns** (`int`) – Maximum latency of flush operations in the
          defined interval, in nanoseconds.
        - **avg_rd_latency_ns** (`int`) – Average latency of read operations in the
          defined interval, in nanoseconds.
        - **avg_wr_latency_ns** (`int`) – Average latency of write operations in the
          defined interval, in nanoseconds.
        - **avg_zone_append_latency_ns** (`int`) – Average latency of zone append
          operations in the defined interval, in nanoseconds (since 8.1)
        - **avg_flush_latency_ns** (`int`) – Average latency of flush operations in the
          defined interval, in nanoseconds.
        - **avg_rd_queue_depth** (`number`) – Average number of pending read operations in
          the defined interval.
        - **avg_wr_queue_depth** (`number`) – Average number of pending write operations in
          the defined interval.
        - **avg_zone_append_queue_depth** (`number`) – Average number of pending zone append
          operations in the defined interval (since 8.1).

*Object* BlockDeviceStats (Since: 0.14)
:   Statistics of a virtual block device or a block backing device.

    Members:
    :   - **rd_bytes** (`int`) – The number of bytes read by the device.
        - **wr_bytes** (`int`) – The number of bytes written by the device.
        - **zone_append_bytes** (`int`) – The number of bytes appended by the zoned
          devices (since 8.1)
        - **unmap_bytes** (`int`) – The number of bytes unmapped by the device (Since 4.2)
        - **rd_operations** (`int`) – The number of read operations performed by the
          device.
        - **wr_operations** (`int`) – The number of write operations performed by the
          device.
        - **zone_append_operations** (`int`) – The number of zone append operations
          performed by the zoned devices (since 8.1)
        - **flush_operations** (`int`) – The number of cache flush operations performed by
          the device (since 0.15)
        - **unmap_operations** (`int`) – The number of unmap operations performed by the
          device (Since 4.2)
        - **rd_total_time_ns** (`int`) – Total time spent on reads in nanoseconds
          (since 0.15)
        - **wr_total_time_ns** (`int`) – Total time spent on writes in nanoseconds
          (since 0.15)
        - **zone_append_total_time_ns** (`int`) – Total time spent on zone append writes
          in nanoseconds (since 8.1)
        - **flush_total_time_ns** (`int`) – Total time spent on cache flushes in
          nanoseconds (since 0.15).
        - **unmap_total_time_ns** (`int`) – Total time spent on unmap operations in
          nanoseconds (Since 4.2)
        - **wr_highest_offset** (`int`) – The offset after the greatest byte written to
          the device. The intended use of this information is for
          growable sparse files (like qcow2) that are used on top of a
          physical device.
        - **rd_merged** (`int`) – Number of read requests that have been merged into
          another request (Since 2.3).
        - **wr_merged** (`int`) – Number of write requests that have been merged into
          another request (Since 2.3).
        - **zone_append_merged** (`int`) – Number of zone append requests that have been
          merged into another request (since 8.1)
        - **unmap_merged** (`int`) – Number of unmap requests that have been merged into
          another request (Since 4.2)
        - **idle_time_ns** (`int`, *optional*) – Time since the last I/O operation, in nanoseconds.
          If the field is absent it means that there haven’t been any
          operations yet (Since 2.5).
        - **failed_rd_operations** (`int`) – The number of failed read operations
          performed by the device (Since 2.5)
        - **failed_wr_operations** (`int`) – The number of failed write operations
          performed by the device (Since 2.5)
        - **failed_zone_append_operations** (`int`) – The number of failed zone append
          write operations performed by the zoned devices (since 8.1)
        - **failed_flush_operations** (`int`) – The number of failed flush operations
          performed by the device (Since 2.5)
        - **failed_unmap_operations** (`int`) – The number of failed unmap operations
          performed by the device (Since 4.2)
        - **invalid_rd_operations** (`int`) – The number of invalid read operations
          performed by the device (Since 2.5)
        - **invalid_wr_operations** (`int`) – The number of invalid write operations
          performed by the device (Since 2.5)
        - **invalid_zone_append_operations** (`int`) – The number of invalid zone append
          operations performed by the zoned device (since 8.1)
        - **invalid_flush_operations** (`int`) – The number of invalid flush operations
          performed by the device (Since 2.5)
        - **invalid_unmap_operations** (`int`) – The number of invalid unmap operations
          performed by the device (Since 4.2)
        - **account_invalid** (`boolean`) – Whether invalid operations are included in the
          last access statistics (Since 2.5)
        - **account_failed** (`boolean`) – Whether failed operations are included in the
          latency and last access statistics (Since 2.5)
        - **timed_stats** (`[`[`BlockDeviceTimedStats`](qemu-qmp-ref.md#object-QMP-block-core.BlockDeviceTimedStats "QMP:block-core.BlockDeviceTimedStats")`]`) – Statistics specific to the set of previously defined
          intervals of time (Since 2.5)
        - **rd_latency_histogram** ([`BlockLatencyHistogramInfo`](qemu-qmp-ref.md#object-QMP-block-core.BlockLatencyHistogramInfo "QMP:block-core.BlockLatencyHistogramInfo"), *optional*) – [`BlockLatencyHistogramInfo`](qemu-qmp-ref.md#object-QMP-block-core.BlockLatencyHistogramInfo "QMP:block-core.BlockLatencyHistogramInfo"). (Since 4.0)
        - **wr_latency_histogram** ([`BlockLatencyHistogramInfo`](qemu-qmp-ref.md#object-QMP-block-core.BlockLatencyHistogramInfo "QMP:block-core.BlockLatencyHistogramInfo"), *optional*) – [`BlockLatencyHistogramInfo`](qemu-qmp-ref.md#object-QMP-block-core.BlockLatencyHistogramInfo "QMP:block-core.BlockLatencyHistogramInfo"). (Since 4.0)
        - **zone_append_latency_histogram** ([`BlockLatencyHistogramInfo`](qemu-qmp-ref.md#object-QMP-block-core.BlockLatencyHistogramInfo "QMP:block-core.BlockLatencyHistogramInfo"), *optional*) – [`BlockLatencyHistogramInfo`](qemu-qmp-ref.md#object-QMP-block-core.BlockLatencyHistogramInfo "QMP:block-core.BlockLatencyHistogramInfo").
          (since 8.1)
        - **flush_latency_histogram** ([`BlockLatencyHistogramInfo`](qemu-qmp-ref.md#object-QMP-block-core.BlockLatencyHistogramInfo "QMP:block-core.BlockLatencyHistogramInfo"), *optional*) – [`BlockLatencyHistogramInfo`](qemu-qmp-ref.md#object-QMP-block-core.BlockLatencyHistogramInfo "QMP:block-core.BlockLatencyHistogramInfo"). (Since 4.0)

*Object* BlockStatsSpecificFile (Since: 4.2)
:   File driver statistics

    Members:
    :   - **discard-nb-ok** (`int`) – The number of successful discard operations
          performed by the driver.
        - **discard-nb-failed** (`int`) – The number of failed discard operations
          performed by the driver.
        - **discard-bytes-ok** (`int`) – The number of bytes discarded by the driver.

*Object* BlockStatsSpecificNvme (Since: 5.2)
:   NVMe driver statistics

    Members:
    :   - **completion-errors** (`int`) – The number of completion errors.
        - **aligned-accesses** (`int`) – The number of aligned accesses performed by the
          driver.
        - **unaligned-accesses** (`int`) – The number of unaligned accesses performed by
          the driver.

*Object* BlockStatsSpecific (Since: 4.2)
:   Block driver specific statistics

    Members:
    :   - **driver** ([`BlockdevDriver`](qemu-qmp-ref.md#enum-QMP-block-core.BlockdevDriver "QMP:block-core.BlockdevDriver")) – block driver name
        - When `driver` is `file`: The members of [`BlockStatsSpecificFile`](qemu-qmp-ref.md#object-QMP-block-core.BlockStatsSpecificFile "QMP:block-core.BlockStatsSpecificFile").
        - When `driver` is `host_device`: The members of [`BlockStatsSpecificFile`](qemu-qmp-ref.md#object-QMP-block-core.BlockStatsSpecificFile "QMP:block-core.BlockStatsSpecificFile").
        - When `driver` is `nvme`: The members of [`BlockStatsSpecificNvme`](qemu-qmp-ref.md#object-QMP-block-core.BlockStatsSpecificNvme "QMP:block-core.BlockStatsSpecificNvme").

*Object* BlockStats (Since: 0.14)
:   Statistics of a virtual block device or a block backing device.

    Members:
    :   - **device** (`string`, *optional*) – If the stats are for a virtual block device, the name
          corresponding to the virtual block device.
        - **node-name** (`string`, *optional*) – The node name of the device. (Since 2.3)
        - **qdev** (`string`, *optional*) – The qdev ID, or if no ID is assigned, the QOM path of the
          block device. (since 3.0)
        - **stats** ([`BlockDeviceStats`](qemu-qmp-ref.md#object-QMP-block-core.BlockDeviceStats "QMP:block-core.BlockDeviceStats")) – A [`BlockDeviceStats`](qemu-qmp-ref.md#object-QMP-block-core.BlockDeviceStats "QMP:block-core.BlockDeviceStats") for the device.
        - **driver-specific** ([`BlockStatsSpecific`](qemu-qmp-ref.md#object-QMP-block-core.BlockStatsSpecific "QMP:block-core.BlockStatsSpecific"), *optional*) – Optional driver-specific stats. (Since 4.2)
        - **parent** ([`BlockStats`](qemu-qmp-ref.md#object-QMP-block-core.BlockStats "QMP:block-core.BlockStats"), *optional*) – This describes the file block device if it has one.
          Contains recursively the statistics of the underlying protocol
          (e.g. the host file for a qcow2 image). If there is no
          underlying protocol, this field is omitted
        - **backing** ([`BlockStats`](qemu-qmp-ref.md#object-QMP-block-core.BlockStats "QMP:block-core.BlockStats"), *optional*) – This describes the backing block device if it has one.
          (Since 2.0)

*Command* query-blockstats (Since: 0.14)
:   Query the [`BlockStats`](qemu-qmp-ref.md#object-QMP-block-core.BlockStats "QMP:block-core.BlockStats") for all virtual block devices.

    Arguments:
    :   - **query-nodes** (`boolean`, *optional*) – If true, the command will query all the block nodes
          that have a node name, in a list which will include “parent”
          information, but not “backing”. If false or omitted, the
          behavior is as before - query all the device backends,
          recursively including their “parent” and “backing”. Filter
          nodes that were created implicitly are skipped over in this
          mode. (Since 2.3)

    Return:
    :   `[`[`BlockStats`](qemu-qmp-ref.md#object-QMP-block-core.BlockStats "QMP:block-core.BlockStats")`]` – A list of statistics for each virtual block device.

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "query-blockstats" }
    > <- {
    >       "return":[
    >          {
    >             "device":"ide0-hd0",
    >             "parent":{
    >                "stats":{
    >                   "wr_highest_offset":3686448128,
    >                   "wr_bytes":9786368,
    >                   "wr_operations":751,
    >                   "rd_bytes":122567168,
    >                   "rd_operations":36772
    >                   "wr_total_times_ns":313253456
    >                   "rd_total_times_ns":3465673657
    >                   "flush_total_times_ns":49653
    >                   "flush_operations":61,
    >                   "rd_merged":0,
    >                   "wr_merged":0,
    >                   "idle_time_ns":2953431879,
    >                   "account_invalid":true,
    >                   "account_failed":false
    >                }
    >             },
    >             "stats":{
    >                "wr_highest_offset":2821110784,
    >                "wr_bytes":9786368,
    >                "wr_operations":692,
    >                "rd_bytes":122739200,
    >                "rd_operations":36604
    >                "flush_operations":51,
    >                "wr_total_times_ns":313253456
    >                "rd_total_times_ns":3465673657
    >                "flush_total_times_ns":49653,
    >                "rd_merged":0,
    >                "wr_merged":0,
    >                "idle_time_ns":2953431879,
    >                "account_invalid":true,
    >                "account_failed":false
    >             },
    >             "qdev": "/machine/unattached/device[23]"
    >          },
    >          {
    >             "device":"ide1-cd0",
    >             "stats":{
    >                "wr_highest_offset":0,
    >                "wr_bytes":0,
    >                "wr_operations":0,
    >                "rd_bytes":0,
    >                "rd_operations":0
    >                "flush_operations":0,
    >                "wr_total_times_ns":0
    >                "rd_total_times_ns":0
    >                "flush_total_times_ns":0,
    >                "rd_merged":0,
    >                "wr_merged":0,
    >                "account_invalid":false,
    >                "account_failed":false
    >             },
    >             "qdev": "/machine/unattached/device[24]"
    >          },
    >          {
    >             "device":"floppy0",
    >             "stats":{
    >                "wr_highest_offset":0,
    >                "wr_bytes":0,
    >                "wr_operations":0,
    >                "rd_bytes":0,
    >                "rd_operations":0
    >                "flush_operations":0,
    >                "wr_total_times_ns":0
    >                "rd_total_times_ns":0
    >                "flush_total_times_ns":0,
    >                "rd_merged":0,
    >                "wr_merged":0,
    >                "account_invalid":false,
    >                "account_failed":false
    >             },
    >             "qdev": "/machine/unattached/device[16]"
    >          },
    >          {
    >             "device":"sd0",
    >             "stats":{
    >                "wr_highest_offset":0,
    >                "wr_bytes":0,
    >                "wr_operations":0,
    >                "rd_bytes":0,
    >                "rd_operations":0
    >                "flush_operations":0,
    >                "wr_total_times_ns":0
    >                "rd_total_times_ns":0
    >                "flush_total_times_ns":0,
    >                "rd_merged":0,
    >                "wr_merged":0,
    >                "account_invalid":false,
    >                "account_failed":false
    >             }
    >          }
    >       ]
    >    }
    > ```

*Enum* BlockdevOnError (Since: 1.3)
:   An enumeration of possible behaviors for errors on I/O operations.
    The exact meaning depends on whether the I/O was initiated by a
    guest or by a block job

    Values:
    :   - **report** – for guest operations, report the error to the guest; for
          jobs, cancel the job
        - **ignore** – ignore the error, only report a QMP event ([`BLOCK_IO_ERROR`](qemu-qmp-ref.md#event-QMP-block-core.BLOCK_IO_ERROR "QMP:block-core.BLOCK_IO_ERROR")
          or [`BLOCK_JOB_ERROR`](qemu-qmp-ref.md#event-QMP-block-core.BLOCK_JOB_ERROR "QMP:block-core.BLOCK_JOB_ERROR")). The backup, mirror and commit block jobs
          retry the failing request later and may still complete
          successfully. The stream block job continues to stream and will
          complete with an error.
        - **enospc** – same as `stop` on ENOSPC, same as `report` otherwise.
        - **stop** – for guest operations, stop the virtual machine; for jobs,
          pause the job
        - **auto** – inherit the error handling policy of the backend (since: 2.7)

*Enum* MirrorSyncMode (Since: 1.3)
:   An enumeration of possible behaviors for the initial synchronization
    phase of storage mirroring.

    Values:
    :   - **top** – copies data in the topmost image to the destination
        - **full** – copies data from all images to the destination
        - **none** – only copy data written from now on
        - **incremental** – only copy data described by the dirty bitmap.
          (since: 2.4)
        - **bitmap** – only copy data described by the dirty bitmap. Behavior on
          completion is determined by the [`BitmapSyncMode`](qemu-qmp-ref.md#enum-QMP-block-core.BitmapSyncMode "QMP:block-core.BitmapSyncMode"). (since: 4.2)

*Enum* BitmapSyncMode (Since: 4.2)
:   An enumeration of possible behaviors for the synchronization of a
    bitmap when used for data copy operations.

    Values:
    :   - **on-success** – The bitmap is only synced when the operation is
          successful. This is the behavior always used for incremental
          backups.
        - **never** – The bitmap is never synchronized with the operation, and is
          treated solely as a read-only manifest of blocks to copy.
        - **always** – The bitmap is always synchronized with the operation,
          regardless of whether or not the operation was successful.

*Enum* MirrorCopyMode (Since: 3.0)
:   An enumeration whose values tell the mirror block job when to
    trigger writes to the target.

    Values:
    :   - **background** – copy data in background only.
        - **write-blocking** – when data is written to the source, write it
          (synchronously) to the target as well. In addition, data is
          copied in background just like in `background` mode.

*Object* BlockJobInfoMirror (Since: 8.2)
:   Information specific to mirror block jobs.

    Members:
    :   - **actively-synced** (`boolean`) – Whether the source is actively synced to the
          target, i.e. same data and new writes are done synchronously to
          both.

*Object* BlockJobInfo (Since: 1.1)
:   Information about a long-running block device operation.

    Members:
    :   - **type** ([`JobType`](qemu-qmp-ref.md#enum-QMP-job.JobType "QMP:job.JobType")) – the job type (‘stream’ for image streaming)
        - **device** (`string`) – The job identifier. Originally the device name but other
          values are allowed since QEMU 2.7
        - **len** (`int`) – Estimated `offset` value at the completion of the job. This
          value can arbitrarily change while the job is running, in both
          directions.
        - **offset** (`int`) – Progress made until now. The unit is arbitrary and the
          value can only meaningfully be used for the ratio of `offset` to
          `len`. The value is monotonically increasing.
        - **busy** (`boolean`) – false if the job is known to be in a quiescent state, with no
          pending I/O. (Since 1.3)
        - **paused** (`boolean`) – whether the job is paused or, if `busy` is true, will pause
          itself as soon as possible. (Since 1.3)
        - **speed** (`int`) – the rate limit, bytes per second
        - **io-status** ([`BlockDeviceIoStatus`](qemu-qmp-ref.md#enum-QMP-block-core.BlockDeviceIoStatus "QMP:block-core.BlockDeviceIoStatus")) – the status of the job (since 1.3)
        - **ready** (`boolean`) – true if the job may be completed (since 2.2)
        - **status** ([`JobStatus`](qemu-qmp-ref.md#enum-QMP-job.JobStatus "QMP:job.JobStatus")) – Current job state/status (since 2.12)
        - **auto-finalize** (`boolean`) – Job will finalize itself when PENDING, moving to the
          CONCLUDED state. (since 2.12)
        - **auto-dismiss** (`boolean`) – Job will dismiss itself when CONCLUDED, and
          disappear. (since 2.12)
        - **error** (`string`, *optional*) – Error information if the job did not complete successfully.
          Not set if the job completed successfully. (since 2.12.1)
        - When `type` is `mirror`: The members of [`BlockJobInfoMirror`](qemu-qmp-ref.md#object-QMP-block-core.BlockJobInfoMirror "QMP:block-core.BlockJobInfoMirror").

*Command* query-block-jobs (Since: 1.1)
:   Return information about long-running block device operations.

    Return:
    :   `[`[`BlockJobInfo`](qemu-qmp-ref.md#object-QMP-block-core.BlockJobInfo "QMP:block-core.BlockJobInfo")`]` – a list of job info for each active block job

*Command* block_resize (Since: 0.14)
:   Resize a block image while a guest is running.

    Either `device` or `node-name` must be set but not both.

    Arguments:
    :   - **device** (`string`, *optional*) – the name of the device to get the image resized
        - **node-name** (`string`, *optional*) – graph node name to get the image resized (Since 2.0)
        - **size** (`int`) – new image size in bytes

    Errors:
    :   - If `device` is not a valid block device, DeviceNotFound

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "block_resize",
    >      "arguments": { "device": "scratch", "size": 1073741824 } }
    > <- { "return": {} }
    > ```

*Enum* NewImageMode (Since: 1.1)
:   An enumeration that tells QEMU how to set the backing file path in a
    new image file.

    Values:
    :   - **existing** – QEMU should look for an existing image file.
        - **absolute-paths** – QEMU should create a new image with absolute paths
          for the backing file. If there is no backing file available,
          the new image will not be backed either.

*Object* BlockdevSnapshotSync
:   Either `device` or `node-name` must be set but not both.

    Members:
    :   - **device** (`string`, *optional*) – the name of the device to take a snapshot of.
        - **node-name** (`string`, *optional*) – graph node name to generate the snapshot from
          (Since 2.0)
        - **snapshot-file** (`string`) – the target of the new overlay image. If the file
          exists, or if it is a device, the overlay will be created in the
          existing file/device. Otherwise, a new file will be created.
        - **snapshot-node-name** (`string`, *optional*) – the graph node name of the new image
          (Since 2.0)
        - **format** (`string`, *optional*) – the format of the overlay image, default is ‘qcow2’.
        - **mode** ([`NewImageMode`](qemu-qmp-ref.md#enum-QMP-block-core.NewImageMode "QMP:block-core.NewImageMode"), *optional*) – whether and how QEMU should create a new image, default is
          ‘absolute-paths’.

*Object* BlockdevSnapshot (Since: 2.5)
:   Members:
    :   - **node** (`string`) – device or node name that will have a snapshot taken.
        - **overlay** (`string`) – reference to the existing block device that will become
          the overlay of `node`, as part of taking the snapshot. It must
          not have a current backing file (this can be achieved by passing
          “backing”: null to [`blockdev-add`](qemu-qmp-ref.md#command-QMP-block-core.blockdev-add "QMP:block-core.blockdev-add")).

*Object* BackupPerf (Since: 6.0)
:   Optional parameters for backup. These parameters don’t affect
    functionality, but may significantly affect performance.

    Members:
    :   - **use-copy-range** (`boolean`, *optional*) – Use copy offloading. Default false.
        - **max-workers** (`int`, *optional*) – Maximum number of parallel requests for the sustained
          background copying process. Doesn’t influence copy-before-write
          operations. Default 64.
        - **max-chunk** (`int`, *optional*) – Maximum request length for the sustained background
          copying process. Doesn’t influence copy-before-write
          operations. 0 means unlimited. If max-chunk is non-zero then
          it should not be less than job cluster size which is calculated
          as maximum of target image cluster size and 64k. Default 0.
        - **min-cluster-size** (`int`, *optional*) – Minimum size of blocks used by copy-before-write
          and background copy operations. Has to be a power of 2. No
          effect if smaller than the maximum of the target’s cluster size
          and 64 KiB. Default 0. (Since 9.2)

*Object* BackupCommon (Since: 4.2)
:   Members:
    :   - **job-id** (`string`, *optional*) – identifier for the newly-created block job. If omitted,
          the device name will be used. (Since 2.7)
        - **device** (`string`) – the device name or node-name of a root node which should be
          copied.
        - **sync** ([`MirrorSyncMode`](qemu-qmp-ref.md#enum-QMP-block-core.MirrorSyncMode "QMP:block-core.MirrorSyncMode")) – what parts of the disk image should be copied to the
          destination (all the disk, only the sectors allocated in the
          topmost image, from a dirty bitmap, or only new I/O).
        - **speed** (`int`, *optional*) – the maximum speed, in bytes per second. The default is 0,
          for unlimited.
        - **bitmap** (`string`, *optional*) – The name of a dirty bitmap to use. Must be present if sync
          is “bitmap” or “incremental”. Can be present if sync is “full”
          or “top”. Must not be present otherwise.
          (Since 2.4 ([`drive-backup`](qemu-qmp-ref.md#command-QMP-block-core.drive-backup "QMP:block-core.drive-backup")), 3.1 ([`blockdev-backup`](qemu-qmp-ref.md#command-QMP-block-core.blockdev-backup "QMP:block-core.blockdev-backup")))
        - **bitmap-mode** ([`BitmapSyncMode`](qemu-qmp-ref.md#enum-QMP-block-core.BitmapSyncMode "QMP:block-core.BitmapSyncMode"), *optional*) – Specifies the type of data the bitmap should contain
          after the operation concludes. Must be present if a bitmap was
          provided, must **not** be present otherwise. (Since 4.2)
        - **compress** (`boolean`, *optional*) – true to compress data, if the target format supports it.
          (default: false) (since 2.8)
        - **on-source-error** ([`BlockdevOnError`](qemu-qmp-ref.md#enum-QMP-block-core.BlockdevOnError "QMP:block-core.BlockdevOnError"), *optional*) – the action to take on an error on the source,
          default ‘report’. ‘stop’ and ‘enospc’ can only be used if the
          block device supports io-status (see [`BlockInfo`](qemu-qmp-ref.md#object-QMP-block-core.BlockInfo "QMP:block-core.BlockInfo")).
        - **on-target-error** ([`BlockdevOnError`](qemu-qmp-ref.md#enum-QMP-block-core.BlockdevOnError "QMP:block-core.BlockdevOnError"), *optional*) – the action to take on an error on the target,
          default ‘report’ (no limitations, since this applies to a
          different block device than `device`).
        - **on-cbw-error** ([`OnCbwError`](qemu-qmp-ref.md#enum-QMP-block-core.OnCbwError "QMP:block-core.OnCbwError"), *optional*) – policy defining behavior on I/O errors in
          copy-before-write jobs; defaults to break-guest-write.
          (Since 10.1)
        - **auto-finalize** (`boolean`, *optional*) – When false, this job will wait in a PENDING state
          after it has finished its work, waiting for [`job-finalize`](qemu-qmp-ref.md#command-QMP-job.job-finalize "QMP:job.job-finalize")
          before making any block graph changes. When true, this job will
          automatically perform its abort or commit actions. Defaults to
          true. (Since 2.12)
        - **auto-dismiss** (`boolean`, *optional*) – When false, this job will wait in a CONCLUDED state
          after it has completely ceased all work, and awaits
          [`job-dismiss`](qemu-qmp-ref.md#command-QMP-job.job-dismiss "QMP:job.job-dismiss"). When true, this job will automatically disappear
          without user intervention. Defaults to true. (Since 2.12)
        - **filter-node-name** (`string`, *optional*) – the node name that should be assigned to the
          filter driver that the backup job inserts into the graph above
          node specified by `drive`. If this option is not given, a node
          name is autogenerated. (Since: 4.2)
        - **discard-source** (`boolean`, *optional*) – Discard blocks on source which have already been
          copied to the target. (Since 9.1)
        - **x-perf** ([`BackupPerf`](qemu-qmp-ref.md#object-QMP-block-core.BackupPerf "QMP:block-core.BackupPerf"), *optional*) – Performance options. (Since 6.0)

    Features:
    :   - **unstable** – Member `x-perf` is experimental.

    > **Note:**
    >
    > `on-source-error` and `on-target-error` only affect
    > background I/O. If an error occurs during a guest write request,
    > the device’s rerror/werror actions will be used.

*Object* DriveBackup (Since: 1.6)
:   Members:
    :   - **target** (`string`) – the target of the new image. If the file exists, or if it
          is a device, the existing file/device will be used as the new
          destination. If it does not exist, a new file will be created.
        - **format** (`string`, *optional*) – the format of the new destination, default is to probe if
          `mode` is ‘existing’, else the format of the source
        - **mode** ([`NewImageMode`](qemu-qmp-ref.md#enum-QMP-block-core.NewImageMode "QMP:block-core.NewImageMode"), *optional*) – whether and how QEMU should create a new image, default is
          ‘absolute-paths’.
        - The members of [`BackupCommon`](qemu-qmp-ref.md#object-QMP-block-core.BackupCommon "QMP:block-core.BackupCommon").

*Object* BlockdevBackup (Since: 2.3)
:   Members:
    :   - **target** (`string`) – the device name or node-name of the backup target node.
        - The members of [`BackupCommon`](qemu-qmp-ref.md#object-QMP-block-core.BackupCommon "QMP:block-core.BackupCommon").

*Command* blockdev-snapshot-sync (Since: 0.14)
:   Takes a synchronous snapshot of a block device.

    Arguments:
    :   - The members of [`BlockdevSnapshotSync`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevSnapshotSync "QMP:block-core.BlockdevSnapshotSync").

    Errors:
    :   - If `device` is not a valid block device, DeviceNotFound

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "blockdev-snapshot-sync",
    >      "arguments": { "device": "ide-hd0",
    >                     "snapshot-file":
    >                     "/some/place/my-image",
    >                     "format": "qcow2" } }
    > <- { "return": {} }
    > ```

*Command* blockdev-snapshot (Since: 2.5)
:   Takes a snapshot of a block device.

    Take a snapshot, by installing ‘node’ as the backing image of
    ‘overlay’. Additionally, if ‘node’ is associated with a block
    device, the block device changes to using ‘overlay’ as its new
    active image.

    Arguments:
    :   - The members of [`BlockdevSnapshot`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevSnapshot "QMP:block-core.BlockdevSnapshot").

    Features:
    :   - **allow-write-only-overlay** – If present, the check whether this
          operation is safe was relaxed so that it can be used to change
          backing file of a destination of a [`blockdev-mirror`](qemu-qmp-ref.md#command-QMP-block-core.blockdev-mirror "QMP:block-core.blockdev-mirror").
          (since 5.0)

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "blockdev-add",
    >      "arguments": { "driver": "qcow2",
    >                     "node-name": "node1534",
    >                     "file": { "driver": "file",
    >                               "filename": "hd1.qcow2" },
    >                     "backing": null } }
    >
    > <- { "return": {} }
    >
    > -> { "execute": "blockdev-snapshot",
    >      "arguments": { "node": "ide-hd0",
    >                     "overlay": "node1534" } }
    > <- { "return": {} }
    > ```

*Command* change-backing-file (Since: 2.1)
:   Change the backing file in the image file metadata. This does not
    cause QEMU to reopen the image file to reparse the backing filename
    (it may, however, perform a reopen to change permissions from r/o ->
    r/w -> r/o, if needed). The new backing file string is written into
    the image file metadata, and the QEMU internal strings are updated.

    Arguments:
    :   - **image-node-name** (`string`) – The name of the block driver state node of the
          image to modify. The “device” argument is used to verify
          “image-node-name” is in the chain described by “device”.
        - **device** (`string`) – The device name or node-name of the root node that owns
          image-node-name.
        - **backing-file** (`string`) – The string to write as the backing file. This string
          is not validated, so care should be taken when specifying the
          string or the image chain may not be able to be reopened again.

    Errors:
    :   - If “device” does not exist or cannot be determined,
          DeviceNotFound

*Command* block-commit (Since: 1.3)
:   Live commit of data from overlay image nodes into backing nodes -
    i.e., writes data between ‘top’ and ‘base’ into ‘base’.

    If top == base, that is an error. If top has no overlays on top of
    it, or if it is in use by a writer, the job will not be completed by
    itself. The user needs to complete the job with the [`job-complete`](qemu-qmp-ref.md#command-QMP-job.job-complete "QMP:job.job-complete")
    command after getting the ready event. (Since 2.0)

    If the base image is smaller than top, then the base image will be
    resized to be the same size as top. If top is smaller than the base
    image, the base will not be truncated. If you want the base image
    size to match the size of the smaller top, you can safely truncate
    it yourself once the commit operation successfully completes.

    Arguments:
    :   - **job-id** (`string`, *optional*) – identifier for the newly-created block job. If omitted,
          the device name will be used. (Since 2.7)
        - **device** (`string`) – the device name or node-name of a root node
        - **base-node** (`string`, *optional*) – The node name of the backing image to write data into.
          If not specified, this is the deepest backing image.
          (since: 3.1)
        - **base** (`string`, *optional*) – Same as `base-node`, except that it is a file name rather than
          a node name. This must be the exact filename string that was
          used to open the node; other strings, even if addressing the
          same file, are not accepted
        - **top-node** (`string`, *optional*) – The node name of the backing image within the image chain
          which contains the topmost data to be committed down. If not
          specified, this is the active layer. (since: 3.1)
        - **top** (`string`, *optional*) – Same as `top-node`, except that it is a file name rather than a
          node name. This must be the exact filename string that was used
          to open the node; other strings, even if addressing the same
          file, are not accepted
        - **backing-file** (`string`, *optional*) –

          The backing file string to write into the overlay
          image of ‘top’. If ‘top’ does not have an overlay image, or if
          ‘top’ is in use by a writer, specifying a backing file string is
          an error.

          This filename is not validated. If a pathname string is such
          that it cannot be resolved by QEMU, that means that subsequent
          QMP or HMP commands must use node-names for the image in
          question, as filename lookup methods will fail.

          If not specified, QEMU will automatically determine the backing
          file string to use, or error out if there is no obvious choice.
          Care should be taken when specifying the string, to specify a
          valid filename or protocol. (Since 2.1)
        - **backing-mask-protocol** (`boolean`, *optional*) – If true, replace any protocol mentioned in
          the ‘backing file format’ with ‘raw’, rather than storing the
          protocol name as the backing format. Can be used even when no
          image header will be updated (default false; since 9.0).
        - **speed** (`int`, *optional*) – the maximum speed, in bytes per second
        - **on-error** ([`BlockdevOnError`](qemu-qmp-ref.md#enum-QMP-block-core.BlockdevOnError "QMP:block-core.BlockdevOnError"), *optional*) – the action to take on an error. ‘ignore’ means that the
          request should be retried. (default: report; since: 5.0)
        - **filter-node-name** (`string`, *optional*) – the node name that should be assigned to the
          filter driver that the commit job inserts into the graph above
          `top`. If this option is not given, a node name is
          autogenerated. (Since: 2.9)
        - **auto-finalize** (`boolean`, *optional*) – When false, this job will wait in a PENDING state
          after it has finished its work, waiting for [`job-finalize`](qemu-qmp-ref.md#command-QMP-job.job-finalize "QMP:job.job-finalize")
          before making any block graph changes. When true, this job will
          automatically perform its abort or commit actions. Defaults to
          true. (Since 3.1)
        - **auto-dismiss** (`boolean`, *optional*) – When false, this job will wait in a CONCLUDED state
          after it has completely ceased all work, and awaits
          [`job-dismiss`](qemu-qmp-ref.md#command-QMP-job.job-dismiss "QMP:job.job-dismiss"). When true, this job will automatically disappear
          without user intervention. Defaults to true. (Since 3.1)

    Features:
    :   - **deprecated** – Members `base` and `top` are deprecated. Use `base-node`
          and `top-node` instead.

    Errors:
    :   - If `device` does not exist, DeviceNotFound

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "block-commit",
    >      "arguments": { "device": "virtio0",
    >                     "top": "/tmp/snap1.qcow2" } }
    > <- { "return": {} }
    > ```

*Command* drive-backup (Since: 1.6)
:   This command is deprecated.

    Start a point-in-time copy of a block device to a new destination.
    The status of ongoing [`drive-backup`](qemu-qmp-ref.md#command-QMP-block-core.drive-backup "QMP:block-core.drive-backup") operations can be checked with
    [`query-block-jobs`](qemu-qmp-ref.md#command-QMP-block-core.query-block-jobs "QMP:block-core.query-block-jobs") where the [`BlockJobInfo`](qemu-qmp-ref.md#object-QMP-block-core.BlockJobInfo "QMP:block-core.BlockJobInfo").type field has the value
    ‘backup’. The operation can be stopped before it has completed
    using the [`job-cancel`](qemu-qmp-ref.md#command-QMP-job.job-cancel "QMP:job.job-cancel") or [`block-job-cancel`](qemu-qmp-ref.md#command-QMP-block-core.block-job-cancel "QMP:block-core.block-job-cancel") command.

    Arguments:
    :   - The members of [`DriveBackup`](qemu-qmp-ref.md#object-QMP-block-core.DriveBackup "QMP:block-core.DriveBackup").

    Features:
    :   - **deprecated** – This command is deprecated. Use [`blockdev-backup`](qemu-qmp-ref.md#command-QMP-block-core.blockdev-backup "QMP:block-core.blockdev-backup")
          instead.

    Errors:
    :   - If `device` is not a valid block device, GenericError

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "drive-backup",
    >      "arguments": { "device": "drive0",
    >                     "sync": "full",
    >                     "target": "backup.img" } }
    > <- { "return": {} }
    > ```

*Command* blockdev-backup (Since: 2.3)
:   Start a point-in-time copy of a block device to a new destination.
    The status of ongoing [`blockdev-backup`](qemu-qmp-ref.md#command-QMP-block-core.blockdev-backup "QMP:block-core.blockdev-backup") operations can be checked
    with [`query-block-jobs`](qemu-qmp-ref.md#command-QMP-block-core.query-block-jobs "QMP:block-core.query-block-jobs") where the [`BlockJobInfo`](qemu-qmp-ref.md#object-QMP-block-core.BlockJobInfo "QMP:block-core.BlockJobInfo").type field has the
    value ‘backup’. The operation can be stopped before it has
    completed using the [`job-cancel`](qemu-qmp-ref.md#command-QMP-job.job-cancel "QMP:job.job-cancel") or [`block-job-cancel`](qemu-qmp-ref.md#command-QMP-block-core.block-job-cancel "QMP:block-core.block-job-cancel") command.

    Arguments:
    :   - The members of [`BlockdevBackup`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevBackup "QMP:block-core.BlockdevBackup").

    Errors:
    :   - If `device` is not a valid block device, DeviceNotFound

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "blockdev-backup",
    >      "arguments": { "device": "src-id",
    >                     "sync": "full",
    >                     "target": "tgt-id" } }
    > <- { "return": {} }
    > ```

*Command* query-named-block-nodes (Since: 2.0)
:   Get the named block driver list

    Arguments:
    :   - **flat** (`boolean`, *optional*) – Omit the nested data about backing image (“backing-image”
          key) if true. Default is false (Since 5.0)

    Return:
    :   `[`[`BlockDeviceInfo`](qemu-qmp-ref.md#object-QMP-block-core.BlockDeviceInfo "QMP:block-core.BlockDeviceInfo")`]`

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "query-named-block-nodes" }
    > <- { "return": [ { "ro":false,
    >                    "drv":"qcow2",
    >                    "encrypted":false,
    >                    "file":"disks/test.qcow2",
    >                    "node-name": "my-node",
    >                    "backing_file_depth":1,
    >                    "detect_zeroes":"off",
    >                    "bps":1000000,
    >                    "bps_rd":0,
    >                    "bps_wr":0,
    >                    "iops":1000000,
    >                    "iops_rd":0,
    >                    "iops_wr":0,
    >                    "bps_max": 8000000,
    >                    "bps_rd_max": 0,
    >                    "bps_wr_max": 0,
    >                    "iops_max": 0,
    >                    "iops_rd_max": 0,
    >                    "iops_wr_max": 0,
    >                    "iops_size": 0,
    >                    "write_threshold": 0,
    >                    "image":{
    >                       "filename":"disks/test.qcow2",
    >                       "format":"qcow2",
    >                       "virtual-size":2048000,
    >                       "backing_file":"base.qcow2",
    >                       "full-backing-filename":"disks/base.qcow2",
    >                       "backing-filename-format":"qcow2",
    >                       "snapshots":[
    >                          {
    >                             "id": "1",
    >                             "name": "snapshot1",
    >                             "vm-state-size": 0,
    >                             "date-sec": 10000200,
    >                             "date-nsec": 12,
    >                             "vm-clock-sec": 206,
    >                             "vm-clock-nsec": 30
    >                          }
    >                       ],
    >                       "backing-image":{
    >                           "filename":"disks/base.qcow2",
    >                           "format":"qcow2",
    >                           "virtual-size":2048000
    >                       }
    >                    } } ] }
    > ```

*Enum* XDbgBlockGraphNodeType (Since: 4.0)
:   Values:
    :   - **block-backend** – corresponds to BlockBackend
        - **block-job** – corresponds to BlockJob
        - **block-driver** – corresponds to BlockDriverState

*Object* XDbgBlockGraphNode (Since: 4.0)
:   Members:
    :   - **id** (`int`) – Block graph node identifier. This `id` is generated only for
          [`x-debug-query-block-graph`](qemu-qmp-ref.md#command-QMP-block-core.x-debug-query-block-graph "QMP:block-core.x-debug-query-block-graph") and does not relate to any other
          identifiers in QEMU.
        - **type** ([`XDbgBlockGraphNodeType`](qemu-qmp-ref.md#enum-QMP-block-core.XDbgBlockGraphNodeType "QMP:block-core.XDbgBlockGraphNodeType")) – Type of graph node. Can be one of block-backend, block-job
          or block-driver-state.
        - **name** (`string`) – Human readable name of the node. Corresponds to node-name
          for block-driver-state nodes; is not guaranteed to be unique in
          the whole graph (with block-jobs and block-backends).

*Enum* BlockPermission (Since: 4.0)
:   Enum of base block permissions.

    Values:
    :   - **consistent-read** – A user that has the “permission” of consistent
          reads is guaranteed that their view of the contents of the block
          device is complete and self-consistent, representing the
          contents of a disk at a specific point. For most block devices
          (including their backing files) this is true, but the property
          cannot be maintained in a few situations like for intermediate
          nodes of a commit block job.
        - **write** – This permission is required to change the visible disk
          contents.
        - **write-unchanged** – This permission (which is weaker than
          BLK_PERM_WRITE) is both enough and required for writes to the
          block node when the caller promises that the visible disk
          content doesn’t change. As the BLK_PERM_WRITE permission is
          strictly stronger, either is sufficient to perform an unchanging
          write.
        - **resize** – This permission is required to change the size of a block
          node.

*Object* XDbgBlockGraphEdge (Since: 4.0)
:   Block Graph edge description for [`x-debug-query-block-graph`](qemu-qmp-ref.md#command-QMP-block-core.x-debug-query-block-graph "QMP:block-core.x-debug-query-block-graph").

    Members:
    :   - **parent** (`int`) – parent id
        - **child** (`int`) – child id
        - **name** (`string`) – name of the relation (examples are ‘file’ and ‘backing’)
        - **perm** (`[`[`BlockPermission`](qemu-qmp-ref.md#enum-QMP-block-core.BlockPermission "QMP:block-core.BlockPermission")`]`) – granted permissions for the parent operating on the child
        - **shared-perm** (`[`[`BlockPermission`](qemu-qmp-ref.md#enum-QMP-block-core.BlockPermission "QMP:block-core.BlockPermission")`]`) – permissions that can still be granted to other users
          of the child while it is still attached to this parent

*Object* XDbgBlockGraph (Since: 4.0)
:   Block Graph - list of nodes and list of edges.

    Members:
    :   - **nodes** (`[`[`XDbgBlockGraphNode`](qemu-qmp-ref.md#object-QMP-block-core.XDbgBlockGraphNode "QMP:block-core.XDbgBlockGraphNode")`]`) – Not documented
        - **edges** (`[`[`XDbgBlockGraphEdge`](qemu-qmp-ref.md#object-QMP-block-core.XDbgBlockGraphEdge "QMP:block-core.XDbgBlockGraphEdge")`]`) – Not documented

*Command* x-debug-query-block-graph (Since: 4.0)
:   This command is unstable/experimental.

    Get the block graph.

    Return:
    :   [`XDbgBlockGraph`](qemu-qmp-ref.md#object-QMP-block-core.XDbgBlockGraph "QMP:block-core.XDbgBlockGraph")

    Features:
    :   - **unstable** – This command is meant for debugging.

*Command* drive-mirror (Since: 1.3)
:   Start mirroring a block device’s writes to a new destination.
    target specifies the target of the new image. If the file exists,
    or if it is a device, it will be used as the new destination for
    writes. If it does not exist, a new file will be created. `format`
    specifies the format of the mirror image, default is to probe if
    mode=’existing’, else the format of the source.

    Arguments:
    :   - The members of [`DriveMirror`](qemu-qmp-ref.md#object-QMP-block-core.DriveMirror "QMP:block-core.DriveMirror").

    Errors:
    :   - If `device` is not a valid block device, GenericError

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "drive-mirror",
    >      "arguments": { "device": "ide-hd0",
    >                     "target": "/some/place/my-image",
    >                     "sync": "full",
    >                     "format": "qcow2" } }
    > <- { "return": {} }
    > ```

*Object* DriveMirror (Since: 1.3)
:   A set of parameters describing drive mirror setup.

    Members:
    :   - **job-id** (`string`, *optional*) – identifier for the newly-created block job. If omitted,
          the device name will be used. (Since 2.7)
        - **device** (`string`) – the device name or node-name of a root node whose writes
          should be mirrored.
        - **target** (`string`) – the target of the new image. If the file exists, or if it
          is a device, the existing file/device will be used as the new
          destination. If it does not exist, a new file will be created.
        - **format** (`string`, *optional*) – the format of the new destination, default is to probe if
          `mode` is ‘existing’, else the format of the source
        - **node-name** (`string`, *optional*) – the new block driver state node name in the graph
          (Since 2.1)
        - **replaces** (`string`, *optional*) – with sync=full graph node name to be replaced by the new
          image when a whole image copy is done. This can be used to
          repair broken Quorum files. By default, `device` is replaced,
          although implicitly created filters on it are kept. (Since 2.1)
        - **mode** ([`NewImageMode`](qemu-qmp-ref.md#enum-QMP-block-core.NewImageMode "QMP:block-core.NewImageMode"), *optional*) – whether and how QEMU should create a new image, default is
          ‘absolute-paths’.
        - **speed** (`int`, *optional*) – the maximum speed, in bytes per second
        - **sync** ([`MirrorSyncMode`](qemu-qmp-ref.md#enum-QMP-block-core.MirrorSyncMode "QMP:block-core.MirrorSyncMode")) – what parts of the disk image should be copied to the
          destination (all the disk, only the sectors allocated in the
          topmost image, or only new I/O).
        - **granularity** (`int`, *optional*) – granularity of the dirty bitmap, default is 64K if the
          image format doesn’t have clusters, 4K if the clusters are
          smaller than that, else the cluster size. Must be a power of 2
          between 512 and 64M (since 1.4).
        - **buf-size** (`int`, *optional*) – maximum amount of data in flight from source to target
          (since 1.4).
        - **on-source-error** ([`BlockdevOnError`](qemu-qmp-ref.md#enum-QMP-block-core.BlockdevOnError "QMP:block-core.BlockdevOnError"), *optional*) – the action to take on an error on the source,
          default ‘report’. ‘stop’ and ‘enospc’ can only be used if the
          block device supports io-status (see [`BlockInfo`](qemu-qmp-ref.md#object-QMP-block-core.BlockInfo "QMP:block-core.BlockInfo")).
        - **on-target-error** ([`BlockdevOnError`](qemu-qmp-ref.md#enum-QMP-block-core.BlockdevOnError "QMP:block-core.BlockdevOnError"), *optional*) – the action to take on an error on the target,
          default ‘report’ (no limitations, since this applies to a
          different block device than `device`).
        - **unmap** (`boolean`, *optional*) – Whether to try to unmap target sectors where source has only
          zero. If true, and target unallocated sectors will read as
          zero, target image sectors will be unmapped; otherwise, zeroes
          will be written. Both will result in identical contents.
          Default is true. (Since 2.4)
        - **copy-mode** ([`MirrorCopyMode`](qemu-qmp-ref.md#enum-QMP-block-core.MirrorCopyMode "QMP:block-core.MirrorCopyMode"), *optional*) – when to copy data to the destination; defaults to
          ‘background’ (Since: 3.0)
        - **auto-finalize** (`boolean`, *optional*) – When false, this job will wait in a PENDING state
          after it has finished its work, waiting for [`job-finalize`](qemu-qmp-ref.md#command-QMP-job.job-finalize "QMP:job.job-finalize")
          before making any block graph changes. When true, this job will
          automatically perform its abort or commit actions. Defaults to
          true. (Since 3.1)
        - **auto-dismiss** (`boolean`, *optional*) – When false, this job will wait in a CONCLUDED state
          after it has completely ceased all work, and awaits
          [`job-dismiss`](qemu-qmp-ref.md#command-QMP-job.job-dismiss "QMP:job.job-dismiss"). When true, this job will automatically disappear
          without user intervention. Defaults to true. (Since 3.1)

*Object* BlockDirtyBitmap (Since: 2.4)
:   Members:
    :   - **node** (`string`) – name of device/node which the bitmap is tracking
        - **name** (`string`) – name of the dirty bitmap

*Object* BlockDirtyBitmapAdd (Since: 2.4)
:   Members:
    :   - **node** (`string`) – name of device/node which the bitmap is tracking
        - **name** (`string`) – name of the dirty bitmap (must be less than 1024 bytes)
        - **granularity** (`int`, *optional*) – the bitmap granularity, default is 64k for
          [`block-dirty-bitmap-add`](qemu-qmp-ref.md#command-QMP-block-core.block-dirty-bitmap-add "QMP:block-core.block-dirty-bitmap-add")
        - **persistent** (`boolean`, *optional*) – the bitmap is persistent, i.e. it will be saved to the
          corresponding block device image file on its close. For now
          only Qcow2 disks support persistent bitmaps. Default is false
          for [`block-dirty-bitmap-add`](qemu-qmp-ref.md#command-QMP-block-core.block-dirty-bitmap-add "QMP:block-core.block-dirty-bitmap-add"). This fails if the node is
          read-only or inactive, since such a bitmap could never be
          stored. (Since: 2.10)
        - **disabled** (`boolean`, *optional*) – the bitmap is created in the disabled state, which means
          that it will not track drive changes. The bitmap may be enabled
          with [`block-dirty-bitmap-enable`](qemu-qmp-ref.md#command-QMP-block-core.block-dirty-bitmap-enable "QMP:block-core.block-dirty-bitmap-enable"). Default is false.
          (Since: 4.0)

*Alternate* BlockDirtyBitmapOrStr (Since: 4.1)
:   Alternatives:
    :   - **local** (`string`) – name of the bitmap, attached to the same node as target
          bitmap.
        - **external** ([`BlockDirtyBitmap`](qemu-qmp-ref.md#object-QMP-block-core.BlockDirtyBitmap "QMP:block-core.BlockDirtyBitmap")) – bitmap with specified node

*Object* BlockDirtyBitmapMerge (Since: 4.0)
:   Members:
    :   - **node** (`string`) – name of device/node which the `target` bitmap is tracking
        - **target** (`string`) – name of the destination dirty bitmap
        - **bitmaps** (`[`[`BlockDirtyBitmapOrStr`](qemu-qmp-ref.md#alternate-QMP-block-core.BlockDirtyBitmapOrStr "QMP:block-core.BlockDirtyBitmapOrStr")`]`) – name(s) of the source dirty bitmap(s) at `node` and/or
          fully specified [`BlockDirtyBitmap`](qemu-qmp-ref.md#object-QMP-block-core.BlockDirtyBitmap "QMP:block-core.BlockDirtyBitmap") elements. The latter are
          supported since 4.1.

*Command* block-dirty-bitmap-add (Since: 2.4)
:   Create a dirty bitmap with a name on the node, and start tracking
    the writes.

    Arguments:
    :   - The members of [`BlockDirtyBitmapAdd`](qemu-qmp-ref.md#object-QMP-block-core.BlockDirtyBitmapAdd "QMP:block-core.BlockDirtyBitmapAdd").

    Errors:
    :   - If `node` is not a valid block device or node, DeviceNotFound
        - If `name` is already taken, GenericError

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "block-dirty-bitmap-add",
    >      "arguments": { "node": "drive0", "name": "bitmap0" } }
    > <- { "return": {} }
    > ```

*Command* block-dirty-bitmap-remove (Since: 2.4)
:   Stop write tracking and remove the dirty bitmap that was created
    with [`block-dirty-bitmap-add`](qemu-qmp-ref.md#command-QMP-block-core.block-dirty-bitmap-add "QMP:block-core.block-dirty-bitmap-add"). If the bitmap is persistent, remove
    it from its storage too.

    Arguments:
    :   - The members of [`BlockDirtyBitmap`](qemu-qmp-ref.md#object-QMP-block-core.BlockDirtyBitmap "QMP:block-core.BlockDirtyBitmap").

    Errors:
    :   - If `node` is not a valid block device or node, DeviceNotFound
        - If `name` is not found, GenericError
        - if `name` is frozen by an operation, GenericError

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "block-dirty-bitmap-remove",
    >      "arguments": { "node": "drive0", "name": "bitmap0" } }
    > <- { "return": {} }
    > ```

*Command* block-dirty-bitmap-clear (Since: 2.4)
:   Clear (reset) a dirty bitmap on the device, so that an incremental
    backup from this point in time forward will only backup clusters
    modified after this clear operation.

    Arguments:
    :   - The members of [`BlockDirtyBitmap`](qemu-qmp-ref.md#object-QMP-block-core.BlockDirtyBitmap "QMP:block-core.BlockDirtyBitmap").

    Errors:
    :   - If `node` is not a valid block device, DeviceNotFound
        - If `name` is not found, GenericError

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "block-dirty-bitmap-clear",
    >      "arguments": { "node": "drive0", "name": "bitmap0" } }
    > <- { "return": {} }
    > ```

*Command* block-dirty-bitmap-enable (Since: 4.0)
:   Enables a dirty bitmap so that it will begin tracking disk changes.

    Arguments:
    :   - The members of [`BlockDirtyBitmap`](qemu-qmp-ref.md#object-QMP-block-core.BlockDirtyBitmap "QMP:block-core.BlockDirtyBitmap").

    Errors:
    :   - If `node` is not a valid block device, DeviceNotFound
        - If `name` is not found, GenericError

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "block-dirty-bitmap-enable",
    >      "arguments": { "node": "drive0", "name": "bitmap0" } }
    > <- { "return": {} }
    > ```

*Command* block-dirty-bitmap-disable (Since: 4.0)
:   Disables a dirty bitmap so that it will stop tracking disk changes.

    Arguments:
    :   - The members of [`BlockDirtyBitmap`](qemu-qmp-ref.md#object-QMP-block-core.BlockDirtyBitmap "QMP:block-core.BlockDirtyBitmap").

    Errors:
    :   - If `node` is not a valid block device, DeviceNotFound
        - If `name` is not found, GenericError

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "block-dirty-bitmap-disable",
    >      "arguments": { "node": "drive0", "name": "bitmap0" } }
    > <- { "return": {} }
    > ```

*Command* block-dirty-bitmap-merge (Since: 4.0)
:   Merge dirty bitmaps listed in `bitmaps` to the `target` dirty bitmap.
    Dirty bitmaps in `bitmaps` will be unchanged, except if it also
    appears as the `target` bitmap. Any bits already set in `target` will
    still be set after the merge, i.e., this operation does not clear
    the target. On error, `target` is unchanged.

    The resulting bitmap will count as dirty any clusters that were
    dirty in any of the source bitmaps. This can be used to achieve
    backup checkpoints, or in simpler usages, to copy bitmaps.

    Arguments:
    :   - The members of [`BlockDirtyBitmapMerge`](qemu-qmp-ref.md#object-QMP-block-core.BlockDirtyBitmapMerge "QMP:block-core.BlockDirtyBitmapMerge").

    Errors:
    :   - If `node` is not a valid block device, DeviceNotFound
        - If any bitmap in `bitmaps` or `target` is not found,
          GenericError
        - If any of the bitmaps have different sizes or granularities,
          GenericError

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "block-dirty-bitmap-merge",
    >      "arguments": { "node": "drive0", "target": "bitmap0",
    >                     "bitmaps": ["bitmap1"] } }
    > <- { "return": {} }
    > ```

*Object* BlockDirtyBitmapSha256 (Since: 2.10)
:   SHA256 hash of dirty bitmap data

    Members:
    :   - **sha256** (`string`) – ASCII representation of SHA256 bitmap hash

*Command* x-debug-block-dirty-bitmap-sha256 (Since: 2.10)
:   This command is unstable/experimental.

    Get bitmap SHA256.

    Arguments:
    :   - The members of [`BlockDirtyBitmap`](qemu-qmp-ref.md#object-QMP-block-core.BlockDirtyBitmap "QMP:block-core.BlockDirtyBitmap").

    Features:
    :   - **unstable** – This command is meant for debugging.

    Return:
    :   [`BlockDirtyBitmapSha256`](qemu-qmp-ref.md#object-QMP-block-core.BlockDirtyBitmapSha256 "QMP:block-core.BlockDirtyBitmapSha256")

    Errors:
    :   - If `node` is not a valid block device, DeviceNotFound
        - If `name` is not found or if hashing has failed, GenericError

*Command* blockdev-mirror (Since: 2.6)
:   Start mirroring a block device’s writes to a new destination.

    Arguments:
    :   - **job-id** (`string`, *optional*) – identifier for the newly-created block job. If omitted,
          the device name will be used. (Since 2.7)
        - **device** (`string`) – The device name or node-name of a root node whose writes
          should be mirrored.
        - **target** (`string`) – the id or node-name of the block device to mirror to. This
          mustn’t be attached to guest.
        - **replaces** (`string`, *optional*) – with sync=full graph node name to be replaced by the new
          image when a whole image copy is done. This can be used to
          repair broken Quorum files. By default, `device` is replaced,
          although implicitly created filters on it are kept.
        - **speed** (`int`, *optional*) – the maximum speed, in bytes per second
        - **sync** ([`MirrorSyncMode`](qemu-qmp-ref.md#enum-QMP-block-core.MirrorSyncMode "QMP:block-core.MirrorSyncMode")) – what parts of the disk image should be copied to the
          destination (all the disk, only the sectors allocated in the
          topmost image, or only new I/O).
        - **granularity** (`int`, *optional*) – granularity of the dirty bitmap, default is 64K if the
          image format doesn’t have clusters, 4K if the clusters are
          smaller than that, else the cluster size. Must be a power of 2
          between 512 and 64M
        - **buf-size** (`int`, *optional*) – maximum amount of data in flight from source to target
        - **on-source-error** ([`BlockdevOnError`](qemu-qmp-ref.md#enum-QMP-block-core.BlockdevOnError "QMP:block-core.BlockdevOnError"), *optional*) – the action to take on an error on the source,
          default ‘report’. ‘stop’ and ‘enospc’ can only be used if the
          block device supports io-status (see [`BlockInfo`](qemu-qmp-ref.md#object-QMP-block-core.BlockInfo "QMP:block-core.BlockInfo")).
        - **on-target-error** ([`BlockdevOnError`](qemu-qmp-ref.md#enum-QMP-block-core.BlockdevOnError "QMP:block-core.BlockdevOnError"), *optional*) – the action to take on an error on the target,
          default ‘report’ (no limitations, since this applies to a
          different block device than `device`).
        - **filter-node-name** (`string`, *optional*) – the node name that should be assigned to the
          filter driver that the mirror job inserts into the graph above
          `device`. If this option is not given, a node name is
          autogenerated. (Since: 2.9)
        - **copy-mode** ([`MirrorCopyMode`](qemu-qmp-ref.md#enum-QMP-block-core.MirrorCopyMode "QMP:block-core.MirrorCopyMode"), *optional*) – when to copy data to the destination; defaults to
          ‘background’ (Since: 3.0)
        - **auto-finalize** (`boolean`, *optional*) – When false, this job will wait in a PENDING state
          after it has finished its work, waiting for [`job-finalize`](qemu-qmp-ref.md#command-QMP-job.job-finalize "QMP:job.job-finalize")
          before making any block graph changes. When true, this job will
          automatically perform its abort or commit actions. Defaults to
          true. (Since 3.1)
        - **auto-dismiss** (`boolean`, *optional*) – When false, this job will wait in a CONCLUDED state
          after it has completely ceased all work, and awaits
          [`job-dismiss`](qemu-qmp-ref.md#command-QMP-job.job-dismiss "QMP:job.job-dismiss"). When true, this job will automatically disappear
          without user intervention. Defaults to true. (Since 3.1)
        - **target-is-zero** (`boolean`, *optional*) – Assume the destination reads as all zeroes before
          the mirror started. Setting this to true can speed up the
          mirror. Setting this to true when the destination is not
          actually all zero can corrupt the destination. (Since 10.1)

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "blockdev-mirror",
    >      "arguments": { "device": "ide-hd0",
    >                     "target": "target0",
    >                     "sync": "full" } }
    > <- { "return": {} }
    > ```

*Object* BlockIOThrottle (Since: 1.1)
:   A set of parameters describing block throttling.

    Members:
    :   - **device** (`string`, *optional*) – Block device name
        - **id** (`string`, *optional*) – The name or QOM path of the guest device (since: 2.8)
        - **bps** (`int`) – total throughput limit in bytes per second
        - **bps_rd** (`int`) – read throughput limit in bytes per second
        - **bps_wr** (`int`) – write throughput limit in bytes per second
        - **iops** (`int`) – total I/O operations per second
        - **iops_rd** (`int`) – read I/O operations per second
        - **iops_wr** (`int`) – write I/O operations per second
        - **bps_max** (`int`, *optional*) – total throughput limit during bursts, in bytes (Since 1.7)
        - **bps_rd_max** (`int`, *optional*) – read throughput limit during bursts, in bytes
          (Since 1.7)
        - **bps_wr_max** (`int`, *optional*) – write throughput limit during bursts, in bytes
          (Since 1.7)
        - **iops_max** (`int`, *optional*) – total I/O operations per second during bursts, in bytes
          (Since 1.7)
        - **iops_rd_max** (`int`, *optional*) – read I/O operations per second during bursts, in bytes
          (Since 1.7)
        - **iops_wr_max** (`int`, *optional*) – write I/O operations per second during bursts, in
          bytes (Since 1.7)
        - **bps_max_length** (`int`, *optional*) – maximum length of the `bps_max` burst period, in
          seconds. It must only be set if `bps_max` is set as well.
          Defaults to 1. (Since 2.6)
        - **bps_rd_max_length** (`int`, *optional*) – maximum length of the `bps_rd_max` burst period,
          in seconds. It must only be set if `bps_rd_max` is set as well.
          Defaults to 1. (Since 2.6)
        - **bps_wr_max_length** (`int`, *optional*) – maximum length of the `bps_wr_max` burst period,
          in seconds. It must only be set if `bps_wr_max` is set as well.
          Defaults to 1. (Since 2.6)
        - **iops_max_length** (`int`, *optional*) – maximum length of the `iops` burst period, in
          seconds. It must only be set if `iops_max` is set as well.
          Defaults to 1. (Since 2.6)
        - **iops_rd_max_length** (`int`, *optional*) – maximum length of the `iops_rd_max` burst
          period, in seconds. It must only be set if `iops_rd_max` is set
          as well. Defaults to 1. (Since 2.6)
        - **iops_wr_max_length** (`int`, *optional*) – maximum length of the `iops_wr_max` burst
          period, in seconds. It must only be set if `iops_wr_max` is set
          as well. Defaults to 1. (Since 2.6)
        - **iops_size** (`int`, *optional*) – an I/O size in bytes (Since 1.7)
        - **group** (`string`, *optional*) – throttle group name (Since 2.4)

    Features:
    :   - **deprecated** – Member `device` is deprecated. Use `id` instead.

*Object* ThrottleLimits (Since: 2.11)
:   Limit parameters for throttling. Since some limit combinations are
    illegal, limits should always be set in one transaction. All fields
    are optional. When setting limits, if a field is missing the
    current value is not changed.

    Members:
    :   - **iops-total** (`int`, *optional*) – limit total I/O operations per second
        - **iops-total-max** (`int`, *optional*) – I/O operations burst
        - **iops-total-max-length** (`int`, *optional*) – length of the iops-total-max burst period,
          in seconds. It must only be set if `iops-total-max` is set as
          well.
        - **iops-read** (`int`, *optional*) – limit read operations per second
        - **iops-read-max** (`int`, *optional*) – I/O operations read burst
        - **iops-read-max-length** (`int`, *optional*) – length of the iops-read-max burst period, in
          seconds. It must only be set if `iops-read-max` is set as well.
        - **iops-write** (`int`, *optional*) – limit write operations per second
        - **iops-write-max** (`int`, *optional*) – I/O operations write burst
        - **iops-write-max-length** (`int`, *optional*) – length of the iops-write-max burst period,
          in seconds. It must only be set if `iops-write-max` is set as
          well.
        - **bps-total** (`int`, *optional*) – limit total bytes per second
        - **bps-total-max** (`int`, *optional*) – total bytes burst
        - **bps-total-max-length** (`int`, *optional*) – length of the bps-total-max burst period, in
          seconds. It must only be set if `bps-total-max` is set as well.
        - **bps-read** (`int`, *optional*) – limit read bytes per second
        - **bps-read-max** (`int`, *optional*) – total bytes read burst
        - **bps-read-max-length** (`int`, *optional*) – length of the bps-read-max burst period, in
          seconds. It must only be set if `bps-read-max` is set as well.
        - **bps-write** (`int`, *optional*) – limit write bytes per second
        - **bps-write-max** (`int`, *optional*) – total bytes write burst
        - **bps-write-max-length** (`int`, *optional*) – length of the bps-write-max burst period, in
          seconds. It must only be set if `bps-write-max` is set as well.
        - **iops-size** (`int`, *optional*) – when limiting by iops max size of an I/O in bytes

*Object* ThrottleGroupProperties (Since: 2.11)
:   Properties for throttle-group objects.

    Members:
    :   - **limits** ([`ThrottleLimits`](qemu-qmp-ref.md#object-QMP-block-core.ThrottleLimits "QMP:block-core.ThrottleLimits"), *optional*) – limits to apply for this throttle group
        - **x-iops-total** (`int`, *optional*) – Not documented
        - **x-iops-total-max** (`int`, *optional*) – Not documented
        - **x-iops-total-max-length** (`int`, *optional*) – Not documented
        - **x-iops-read** (`int`, *optional*) – Not documented
        - **x-iops-read-max** (`int`, *optional*) – Not documented
        - **x-iops-read-max-length** (`int`, *optional*) – Not documented
        - **x-iops-write** (`int`, *optional*) – Not documented
        - **x-iops-write-max** (`int`, *optional*) – Not documented
        - **x-iops-write-max-length** (`int`, *optional*) – Not documented
        - **x-bps-total** (`int`, *optional*) – Not documented
        - **x-bps-total-max** (`int`, *optional*) – Not documented
        - **x-bps-total-max-length** (`int`, *optional*) – Not documented
        - **x-bps-read** (`int`, *optional*) – Not documented
        - **x-bps-read-max** (`int`, *optional*) – Not documented
        - **x-bps-read-max-length** (`int`, *optional*) – Not documented
        - **x-bps-write** (`int`, *optional*) – Not documented
        - **x-bps-write-max** (`int`, *optional*) – Not documented
        - **x-bps-write-max-length** (`int`, *optional*) – Not documented
        - **x-iops-size** (`int`, *optional*) – Not documented

    Features:
    :   - **unstable** – All members starting with x- are aliases for the same key
          without x- in the `limits` object. This is not a stable
          interface and may be removed or changed incompatibly in the
          future. Use `limits` for a supported stable interface.

*Command* block-stream (Since: 1.1)
:   Copy data from a backing file into a block device.

    The block streaming operation is performed in the background until
    the entire backing file has been copied. This command returns
    immediately once streaming has started. The status of ongoing block
    streaming operations can be checked with [`query-block-jobs`](qemu-qmp-ref.md#command-QMP-block-core.query-block-jobs "QMP:block-core.query-block-jobs"). The
    operation can be stopped before it has completed using the
    [`job-cancel`](qemu-qmp-ref.md#command-QMP-job.job-cancel "QMP:job.job-cancel") or [`block-job-cancel`](qemu-qmp-ref.md#command-QMP-block-core.block-job-cancel "QMP:block-core.block-job-cancel") command.

    The node that receives the data is called the top image, can be
    located in any part of the chain (but always above the base image;
    see below) and can be specified using its device or node name.
    Earlier QEMU versions only allowed ‘device’ to name the top level
    node; presence of the ‘base-node’ parameter during introspection can
    be used as a witness of the enhanced semantics of ‘device’.

    If a base file is specified then sectors are not copied from that
    base file and its backing chain. This can be used to stream a
    subset of the backing file chain instead of flattening the entire
    image. When streaming completes the image file will have the base
    file as its backing file, unless that node was changed while the job
    was running. In that case, base’s parent’s backing (or filtered,
    whichever exists) child (i.e., base at the beginning of the job)
    will be the new backing file.

    On successful completion the image file is updated to drop the
    backing file and the [`BLOCK_JOB_COMPLETED`](qemu-qmp-ref.md#event-QMP-block-core.BLOCK_JOB_COMPLETED "QMP:block-core.BLOCK_JOB_COMPLETED") event is emitted.

    In case `device` is a filter node, [`block-stream`](qemu-qmp-ref.md#command-QMP-block-core.block-stream "QMP:block-core.block-stream") modifies the first
    non-filter overlay node below it to point to the new backing node
    instead of modifying `device` itself.

    Arguments:
    :   - **job-id** (`string`, *optional*) – identifier for the newly-created block job. If omitted,
          the device name will be used. (Since 2.7)
        - **device** (`string`) – the device or node name of the top image
        - **base** (`string`, *optional*) – the common backing file name. It cannot be set if `base-node`
          or `bottom` is also set.
        - **base-node** (`string`, *optional*) – the node name of the backing file. It cannot be set if
          `base` or `bottom` is also set. (Since 2.8)
        - **bottom** (`string`, *optional*) – the last node in the chain that should be streamed into
          top. It cannot be set if `base` or `base-node` is also set. It
          cannot be filter node. (Since 6.0)
        - **backing-file** (`string`, *optional*) –

          The backing file string to write into the top image.
          This filename is not validated.

          If a pathname string is such that it cannot be resolved by QEMU,
          that means that subsequent QMP or HMP commands must use
          node-names for the image in question, as filename lookup methods
          will fail.

          If not specified, QEMU will automatically determine the backing
          file string to use, or error out if there is no obvious choice.
          Care should be taken when specifying the string, to specify a
          valid filename or protocol. (Since 2.1)
        - **backing-mask-protocol** (`boolean`, *optional*) – If true, replace any protocol mentioned in
          the ‘backing file format’ with ‘raw’, rather than storing the
          protocol name as the backing format. Can be used even when no
          image header will be updated (default false; since 9.0).
        - **speed** (`int`, *optional*) – the maximum speed, in bytes per second
        - **on-error** ([`BlockdevOnError`](qemu-qmp-ref.md#enum-QMP-block-core.BlockdevOnError "QMP:block-core.BlockdevOnError"), *optional*) – the action to take on an error (default report). ‘stop’
          and ‘enospc’ can only be used if the block device supports
          io-status (see [`BlockInfo`](qemu-qmp-ref.md#object-QMP-block-core.BlockInfo "QMP:block-core.BlockInfo")). (Since 1.3)
        - **filter-node-name** (`string`, *optional*) – the node name that should be assigned to the
          filter driver that the stream job inserts into the graph above
          `device`. If this option is not given, a node name is
          autogenerated. (Since: 6.0)
        - **auto-finalize** (`boolean`, *optional*) – When false, this job will wait in a PENDING state
          after it has finished its work, waiting for [`job-finalize`](qemu-qmp-ref.md#command-QMP-job.job-finalize "QMP:job.job-finalize")
          before making any block graph changes. When true, this job will
          automatically perform its abort or commit actions. Defaults to
          true. (Since 3.1)
        - **auto-dismiss** (`boolean`, *optional*) – When false, this job will wait in a CONCLUDED state
          after it has completely ceased all work, and awaits
          [`job-dismiss`](qemu-qmp-ref.md#command-QMP-job.job-dismiss "QMP:job.job-dismiss"). When true, this job will automatically disappear
          without user intervention. Defaults to true. (Since 3.1)

    Errors:
    :   - If `device` does not exist, DeviceNotFound.

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "block-stream",
    >      "arguments": { "device": "virtio0",
    >                     "base": "/tmp/master.qcow2" } }
    > <- { "return": {} }
    > ```

*Command* block-job-set-speed (Since: 1.1)
:   Set maximum speed for a background block operation.

    This command can only be issued when there is an active block job.

    Throttling can be disabled by setting the speed to 0.

    Arguments:
    :   - **device** (`string`) – The job identifier. This used to be a device name (hence
          the name of the parameter), but since QEMU 2.7 it can have other
          values.
        - **speed** (`int`) – the maximum speed, in bytes per second, or 0 for unlimited.
          Defaults to 0.

    Errors:
    :   - If no background operation is active on this device,
          DeviceNotActive

*Command* block-job-cancel (Since: 1.1)
:   Stop an active background block operation.

    This command returns immediately after marking the active background
    block operation for cancellation. It is an error to call this
    command if no operation is in progress.

    The operation will cancel as soon as possible and then emit the
    [`BLOCK_JOB_CANCELLED`](qemu-qmp-ref.md#event-QMP-block-core.BLOCK_JOB_CANCELLED "QMP:block-core.BLOCK_JOB_CANCELLED") event. Before that happens the job is still
    visible when enumerated using [`query-block-jobs`](qemu-qmp-ref.md#command-QMP-block-core.query-block-jobs "QMP:block-core.query-block-jobs").

    Note that if you issue [`block-job-cancel`](qemu-qmp-ref.md#command-QMP-block-core.block-job-cancel "QMP:block-core.block-job-cancel") after [`drive-mirror`](qemu-qmp-ref.md#command-QMP-block-core.drive-mirror "QMP:block-core.drive-mirror") has
    indicated (via the event [`BLOCK_JOB_READY`](qemu-qmp-ref.md#event-QMP-block-core.BLOCK_JOB_READY "QMP:block-core.BLOCK_JOB_READY")) that the source and
    destination are synchronized, then the event triggered by this
    command changes to [`BLOCK_JOB_COMPLETED`](qemu-qmp-ref.md#event-QMP-block-core.BLOCK_JOB_COMPLETED "QMP:block-core.BLOCK_JOB_COMPLETED"), to indicate that the
    mirroring has ended and the destination now has a point-in-time copy
    tied to the time of the cancellation.

    For streaming, the image file retains its backing file unless the
    streaming operation happens to complete just as it is being
    cancelled. A new streaming operation can be started at a later time
    to finish copying all data from the backing file.

    Arguments:
    :   - **device** (`string`) – The job identifier. This used to be a device name (hence
          the name of the parameter), but since QEMU 2.7 it can have other
          values.
        - **force** (`boolean`, *optional*) – If true, and the job has already emitted the event
          [`BLOCK_JOB_READY`](qemu-qmp-ref.md#event-QMP-block-core.BLOCK_JOB_READY "QMP:block-core.BLOCK_JOB_READY"), abandon the job immediately (even if it is
          paused) instead of waiting for the destination to complete its
          final synchronization (since 1.3)

    Errors:
    :   - If no background operation is active on this device,
          DeviceNotActive

*Command* block-job-pause (Since: 1.3)
:   This command is deprecated.

    Pause an active background block operation.

    This command returns immediately after marking the active job for
    pausing. Pausing an already paused job is an error.

    The job will pause as soon as possible, which means transitioning
    into the PAUSED state if it was RUNNING, or into STANDBY if it was
    READY. The corresponding [`JOB_STATUS_CHANGE`](qemu-qmp-ref.md#event-QMP-job.JOB_STATUS_CHANGE "QMP:job.JOB_STATUS_CHANGE") event will be emitted.

    Cancelling a paused job automatically resumes it.

    Arguments:
    :   - **device** (`string`) – The job identifier. This used to be a device name (hence
          the name of the parameter), but since QEMU 2.7 it can have other
          values.

    Features:
    :   - **deprecated** – This command is deprecated. Use [`job-pause`](qemu-qmp-ref.md#command-QMP-job.job-pause "QMP:job.job-pause")
          instead.

    Errors:
    :   - If no background operation is active on this device,
          DeviceNotActive

*Command* block-job-resume (Since: 1.3)
:   This command is deprecated.

    Resume an active background block operation.

    This command returns immediately after resuming a paused job.
    Resuming an already running job is an error.

    This command also clears the error status of the job.

    Arguments:
    :   - **device** (`string`) – The job identifier. This used to be a device name (hence
          the name of the parameter), but since QEMU 2.7 it can have other
          values.

    Features:
    :   - **deprecated** – This command is deprecated. Use [`job-resume`](qemu-qmp-ref.md#command-QMP-job.job-resume "QMP:job.job-resume")
          instead.

    Errors:
    :   - If no background operation is active on this device,
          DeviceNotActive

*Command* block-job-complete (Since: 1.3)
:   This command is deprecated.

    Manually trigger completion of an active job in the READY or STANDBY
    state. Completing the job in any other state is an error.

    This is supported only for drive mirroring, where it also switches
    the device to write to the target path only. Note that drive
    mirroring includes [`drive-mirror`](qemu-qmp-ref.md#command-QMP-block-core.drive-mirror "QMP:block-core.drive-mirror"), [`blockdev-mirror`](qemu-qmp-ref.md#command-QMP-block-core.blockdev-mirror "QMP:block-core.blockdev-mirror") and
    [`block-commit`](qemu-qmp-ref.md#command-QMP-block-core.block-commit "QMP:block-core.block-commit") job (only in case of “active commit”, when the node
    being committed is used by the guest). The ability to complete is
    signaled with a [`BLOCK_JOB_READY`](qemu-qmp-ref.md#event-QMP-block-core.BLOCK_JOB_READY "QMP:block-core.BLOCK_JOB_READY") event.

    This command completes an active background block operation
    synchronously. The ordering of this command’s return with the
    [`BLOCK_JOB_COMPLETED`](qemu-qmp-ref.md#event-QMP-block-core.BLOCK_JOB_COMPLETED "QMP:block-core.BLOCK_JOB_COMPLETED") event is not defined. Note that if an I/O
    error occurs during the processing of this command: 1) the command
    itself will fail; 2) the error will be processed according to the
    rerror/werror arguments that were specified when starting the
    operation.

    Arguments:
    :   - **device** (`string`) – The job identifier. This used to be a device name (hence
          the name of the parameter), but since QEMU 2.7 it can have other
          values.

    Features:
    :   - **deprecated** – This command is deprecated. Use [`job-complete`](qemu-qmp-ref.md#command-QMP-job.job-complete "QMP:job.job-complete")
          instead.

    Errors:
    :   - If no background operation is active on this device,
          DeviceNotActive

*Command* block-job-dismiss (Since: 2.12)
:   This command is deprecated.

    Deletes a job that is in the CONCLUDED state. This command only
    needs to be run explicitly for jobs that don’t have automatic
    dismiss enabled. In turn, automatic dismiss may be enabled only for
    jobs that have `auto-dismiss` option, which are [`drive-backup`](qemu-qmp-ref.md#command-QMP-block-core.drive-backup "QMP:block-core.drive-backup"),
    [`blockdev-backup`](qemu-qmp-ref.md#command-QMP-block-core.blockdev-backup "QMP:block-core.blockdev-backup"), [`drive-mirror`](qemu-qmp-ref.md#command-QMP-block-core.drive-mirror "QMP:block-core.drive-mirror"), [`blockdev-mirror`](qemu-qmp-ref.md#command-QMP-block-core.blockdev-mirror "QMP:block-core.blockdev-mirror"), [`block-commit`](qemu-qmp-ref.md#command-QMP-block-core.block-commit "QMP:block-core.block-commit")
    and [`block-stream`](qemu-qmp-ref.md#command-QMP-block-core.block-stream "QMP:block-core.block-stream"). `auto-dismiss` is enabled by default for these
    jobs.

    This command will refuse to operate on any job that has not yet
    reached its terminal state, CONCLUDED. For jobs that make use of
    the [`BLOCK_JOB_READY`](qemu-qmp-ref.md#event-QMP-block-core.BLOCK_JOB_READY "QMP:block-core.BLOCK_JOB_READY") event, [`job-cancel`](qemu-qmp-ref.md#command-QMP-job.job-cancel "QMP:job.job-cancel"), [`block-job-cancel`](qemu-qmp-ref.md#command-QMP-block-core.block-job-cancel "QMP:block-core.block-job-cancel") or
    [`job-complete`](qemu-qmp-ref.md#command-QMP-job.job-complete "QMP:job.job-complete") will still need to be used as appropriate.

    Arguments:
    :   - **id** (`string`) – The job identifier.

    Features:
    :   - **deprecated** – This command is deprecated. Use [`job-dismiss`](qemu-qmp-ref.md#command-QMP-job.job-dismiss "QMP:job.job-dismiss")
          instead.

*Command* block-job-finalize (Since: 2.12)
:   This command is deprecated.

    Instructs all jobs in a transaction (or a single job if it is not
    part of any transaction) to finalize any graph changes and do any
    necessary cleanup. This command requires that all involved jobs are
    in the PENDING state.

    For jobs in a transaction, instructing one job to finalize will
    force ALL jobs in the transaction to finalize, so it is only
    necessary to instruct a single member job to finalize.

    The command is applicable only to jobs which have `auto-finalize`
    option and only when this option is set to false.

    Arguments:
    :   - **id** (`string`) – The job identifier.

    Features:
    :   - **deprecated** – This command is deprecated. Use [`job-finalize`](qemu-qmp-ref.md#command-QMP-job.job-finalize "QMP:job.job-finalize")
          instead.

*Object* BlockJobChangeOptionsMirror (Since: 8.2)
:   Members:
    :   - **copy-mode** ([`MirrorCopyMode`](qemu-qmp-ref.md#enum-QMP-block-core.MirrorCopyMode "QMP:block-core.MirrorCopyMode")) – Switch to this copy mode. Currently, only the switch
          from ‘background’ to ‘write-blocking’ is implemented.

*Object* BlockJobChangeOptions (Since: 8.2)
:   Block job options that can be changed after job creation.

    Members:
    :   - **id** (`string`) – The job identifier
        - **type** ([`JobType`](qemu-qmp-ref.md#enum-QMP-job.JobType "QMP:job.JobType")) – The job type
        - When `type` is `mirror`: The members of [`BlockJobChangeOptionsMirror`](qemu-qmp-ref.md#object-QMP-block-core.BlockJobChangeOptionsMirror "QMP:block-core.BlockJobChangeOptionsMirror").

*Command* block-job-change (Since: 8.2)
:   Change the block job’s options.

    Arguments:
    :   - The members of [`BlockJobChangeOptions`](qemu-qmp-ref.md#object-QMP-block-core.BlockJobChangeOptions "QMP:block-core.BlockJobChangeOptions").

*Enum* BlockdevDiscardOptions (Since: 2.9)
:   Determines how to handle discard requests.

    Values:
    :   - **ignore** – Ignore the request
        - **unmap** – Forward as an unmap request

*Enum* BlockdevDetectZeroesOptions (Since: 2.1)
:   Describes the operation mode for the automatic conversion of plain
    zero writes by the OS to driver specific optimized zero write
    commands.

    Values:
    :   - **off** – Disabled (default)
        - **on** – Enabled
        - **unmap** – Enabled and even try to unmap blocks if possible. This
          requires also that [`BlockdevDiscardOptions`](qemu-qmp-ref.md#enum-QMP-block-core.BlockdevDiscardOptions "QMP:block-core.BlockdevDiscardOptions") is set to unmap for
          this device.

*Enum* BlockdevAioOptions (Since: 2.9)
:   Selects the AIO backend to handle I/O requests

    Values:
    :   - **threads** – Use QEMU’s thread pool
        - **native** – Use native AIO backend (only Linux and Windows)
        - **io_uring** – Use linux io_uring (since 5.0)

*Object* BlockdevCacheOptions (Since: 2.9)
:   Includes cache-related options for block devices

    Members:
    :   - **direct** (`boolean`, *optional*) – enables use of O_DIRECT (bypass the host page cache;
          default: false)
        - **no-flush** (`boolean`, *optional*) – ignore any flush requests for the device (default: false)

*Enum* BlockdevDriver (Since: 2.9)
:   Drivers that are supported in block device operations.

    Values:
    :   - **throttle** – Since 2.11
        - **nvme** – Since 2.12
        - **copy-on-read** – Since 3.0
        - **blklogwrites** – Since 3.0
        - **blkreplay** – Since 4.2
        - **compress** – Since 5.0
        - **copy-before-write** – Since 6.2
        - **snapshot-access** – Since 7.0
        - **blkdebug** – Not documented
        - **blkverify** – Not documented
        - **bochs** – Not documented
        - **cloop** – Not documented
        - **dmg** – Not documented
        - **file** – Not documented
        - **ftp** – Not documented
        - **ftps** – Not documented
        - **host_cdrom** – Not documented
        - **host_device** – Not documented
        - **http** – Not documented
        - **https** – Not documented
        - **io_uring** – Not documented
        - **iscsi** – Not documented
        - **luks** – Not documented
        - **nbd** – Not documented
        - **nfs** – Not documented
        - **null-aio** – Not documented
        - **null-co** – Not documented
        - **nvme-io_uring** – Not documented
        - **parallels** – Not documented
        - **preallocate** – Not documented
        - **qcow** – Not documented
        - **qcow2** – Not documented
        - **qed** – Not documented
        - **quorum** – Not documented
        - **raw** – Not documented
        - **rbd** – Not documented
        - **replication** – Not documented
        - **ssh** – Not documented
        - **vdi** – Not documented
        - **vhdx** – Not documented
        - **virtio-blk-vfio-pci** – Not documented
        - **virtio-blk-vhost-user** – Not documented
        - **virtio-blk-vhost-vdpa** – Not documented
        - **vmdk** – Not documented
        - **vpc** – Not documented
        - **vvfat** – Not documented

*Object* BlockdevOptionsFile (Since: 2.9)
:   Driver specific block device options for the file backend.

    Members:
    :   - **filename** (`string`) – path to the image file
        - **pr-manager** (`string`, *optional*) – the id for the object that will handle persistent
          reservations for this device (default: none, forward the
          commands via SG_IO; since 2.11)
        - **aio** ([`BlockdevAioOptions`](qemu-qmp-ref.md#enum-QMP-block-core.BlockdevAioOptions "QMP:block-core.BlockdevAioOptions"), *optional*) – AIO backend (default: threads) (since: 2.8)
        - **aio-max-batch** (`int`, *optional*) – maximum number of requests to batch together into a
          single submission in the AIO backend. The smallest value
          between this and the aio-max-batch value of the IOThread object
          is chosen. 0 means that the AIO backend will handle it
          automatically. (default: 0, since 6.2)
        - **locking** ([`OnOffAuto`](qemu-qmp-ref.md#enum-QMP-common.OnOffAuto "QMP:common.OnOffAuto"), *optional*) – whether to enable file locking. If set to ‘auto’, only
          enable when Open File Descriptor (OFD) locking API is available
          (default: auto, since 2.10)
        - **drop-cache** (`boolean`, *optional*) – invalidate page cache during live migration. This
          prevents stale data on the migration destination with
          cache.direct=off. Currently only supported on Linux hosts.
          (default: on, since: 4.0)
        - **x-check-cache-dropped** (`boolean`, *optional*) – whether to check that page cache was dropped
          on live migration. May cause noticeable delays if the image
          file is large, do not use in production. (default: off)
          (since: 3.0)

    Features:
    :   - **dynamic-auto-read-only** – If present, enabled auto-read-only means
          that the driver will open the image read-only at first,
          dynamically reopen the image file read-write when the first
          writer is attached to the node and reopen read-only when the
          last writer is detached. This allows giving QEMU write
          permissions only on demand when an operation actually needs
          write access.
        - **unstable** – Member x-check-cache-dropped is meant for debugging.

*Object* BlockdevOptionsNull (Since: 2.9)
:   Driver specific block device options for the null backend.

    Members:
    :   - **size** (`int`, *optional*) – size of the device in bytes.
        - **latency-ns** (`int`, *optional*) – emulated latency (in nanoseconds) in processing
          requests. Default to zero which completes requests immediately.
          (Since 2.4)
        - **read-zeroes** (`boolean`, *optional*) – if true, reads from the device produce zeroes; if
          false, the buffer is left unchanged.
          (default: false; since: 4.1)

*Object* BlockdevOptionsNVMe (Since: 2.12)
:   Driver specific block device options for the NVMe backend.

    Members:
    :   - **device** (`string`) – PCI controller address of the NVMe device in format
          hhhh:bb:ss.f (host:bus:slot.function)
        - **namespace** (`int`) – namespace number of the device, starting from 1.

    Note that the PCI `device` must have been unbound from any host
    kernel driver before instructing QEMU to add the blockdev.

*Object* BlockdevOptionsVVFAT (Since: 2.9)
:   Driver specific block device options for the vvfat protocol.

    Members:
    :   - **dir** (`string`) – directory to be exported as FAT image
        - **fat-type** (`int`, *optional*) – FAT type: 12, 16 or 32
        - **floppy** (`boolean`, *optional*) – whether to export a floppy image (true) or partitioned hard
          disk (false; default)
        - **label** (`string`, *optional*) – set the volume label, limited to 11 bytes. FAT16 and FAT32
          traditionally have some restrictions on labels, which are
          ignored by most operating systems. Defaults to “QEMU VVFAT”.
          (since 2.4)
        - **rw** (`boolean`, *optional*) – whether to allow write operations (default: false)

*Object* BlockdevOptionsGenericFormat (Since: 2.9)
:   Driver specific block device options for image format that have no
    option besides their data source.

    Members:
    :   - **file** ([`BlockdevRef`](qemu-qmp-ref.md#alternate-QMP-block-core.BlockdevRef "QMP:block-core.BlockdevRef")) – reference to or definition of the data source block device

*Object* BlockdevOptionsLUKS (Since: 2.9)
:   Driver specific block device options for LUKS.

    Members:
    :   - **key-secret** (`string`, *optional*) – the ID of a QCryptoSecret object providing the
          decryption key. Mandatory except when doing a metadata-only
          probe of the image. (since 2.6)
        - **header** ([`BlockdevRef`](qemu-qmp-ref.md#alternate-QMP-block-core.BlockdevRef "QMP:block-core.BlockdevRef"), *optional*) – block device holding a detached LUKS header. (since 9.0)
        - The members of [`BlockdevOptionsGenericFormat`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsGenericFormat "QMP:block-core.BlockdevOptionsGenericFormat").

*Object* BlockdevOptionsGenericCOWFormat (Since: 2.9)
:   Driver specific block device options for image format that have no
    option besides their data source and an optional backing file.

    Members:
    :   - **backing** ([`BlockdevRefOrNull`](qemu-qmp-ref.md#alternate-QMP-block-core.BlockdevRefOrNull "QMP:block-core.BlockdevRefOrNull"), *optional*) – reference to or definition of the backing file block
          device, null disables the backing file entirely. Defaults to
          the backing file stored the image file.
        - The members of [`BlockdevOptionsGenericFormat`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsGenericFormat "QMP:block-core.BlockdevOptionsGenericFormat").

*Enum* Qcow2OverlapCheckMode (Since: 2.9)
:   General overlap check modes.

    Values:
    :   - **none** – Do not perform any checks
        - **constant** – Perform only checks which can be done in constant time
          and without reading anything from disk
        - **cached** – Perform only checks which can be done without reading
          anything from disk
        - **all** – Perform all available overlap checks

*Object* Qcow2OverlapCheckFlags (Since: 2.9)
:   Structure of flags for each metadata structure. Setting a field to
    ‘true’ makes QEMU guard that Qcow2 format structure against
    unintended overwriting. See Qcow2 format specification for detailed
    information on these structures. The default value is chosen
    according to the template given.

    Members:
    :   - **template** ([`Qcow2OverlapCheckMode`](qemu-qmp-ref.md#enum-QMP-block-core.Qcow2OverlapCheckMode "QMP:block-core.Qcow2OverlapCheckMode"), *optional*) – Specifies a template mode which can be adjusted using the
          other flags, defaults to ‘cached’
        - **main-header** (`boolean`, *optional*) – Qcow2 format header
        - **active-l1** (`boolean`, *optional*) – Qcow2 active L1 table
        - **active-l2** (`boolean`, *optional*) – Qcow2 active L2 table
        - **refcount-table** (`boolean`, *optional*) – Qcow2 refcount table
        - **refcount-block** (`boolean`, *optional*) – Qcow2 refcount blocks
        - **snapshot-table** (`boolean`, *optional*) – Qcow2 snapshot table
        - **inactive-l1** (`boolean`, *optional*) – Qcow2 inactive L1 tables
        - **inactive-l2** (`boolean`, *optional*) – Qcow2 inactive L2 tables
        - **bitmap-directory** (`boolean`, *optional*) – Qcow2 bitmap directory (since 3.0)

*Alternate* Qcow2OverlapChecks (Since: 2.9)
:   Specifies which metadata structures should be guarded against
    unintended overwriting.

    Alternatives:
    :   - **flags** ([`Qcow2OverlapCheckFlags`](qemu-qmp-ref.md#object-QMP-block-core.Qcow2OverlapCheckFlags "QMP:block-core.Qcow2OverlapCheckFlags")) – set of flags for separate specification of each metadata
          structure type
        - **mode** ([`Qcow2OverlapCheckMode`](qemu-qmp-ref.md#enum-QMP-block-core.Qcow2OverlapCheckMode "QMP:block-core.Qcow2OverlapCheckMode")) – named mode which chooses a specific set of flags

*Enum* BlockdevQcowEncryptionFormat (Since: 2.10)
:   Values:
    :   - **aes** – AES-CBC with plain64 initialization vectors

*Object* BlockdevQcowEncryption (Since: 2.10)
:   Members:
    :   - **format** ([`BlockdevQcowEncryptionFormat`](qemu-qmp-ref.md#enum-QMP-block-core.BlockdevQcowEncryptionFormat "QMP:block-core.BlockdevQcowEncryptionFormat")) – encryption format
        - When `format` is `aes`: The members of [`QCryptoBlockOptionsQCow`](qemu-qmp-ref.md#object-QMP-crypto.QCryptoBlockOptionsQCow "QMP:crypto.QCryptoBlockOptionsQCow").

*Object* BlockdevOptionsQcow (Since: 2.10)
:   Driver specific block device options for qcow.

    Members:
    :   - **encrypt** ([`BlockdevQcowEncryption`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevQcowEncryption "QMP:block-core.BlockdevQcowEncryption"), *optional*) – Image decryption options. Mandatory for encrypted images,
          except when doing a metadata-only probe of the image.
        - The members of [`BlockdevOptionsGenericCOWFormat`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsGenericCOWFormat "QMP:block-core.BlockdevOptionsGenericCOWFormat").

*Enum* BlockdevQcow2EncryptionFormat (Since: 2.10)
:   Values:
    :   - **aes** – AES-CBC with plain64 initialization vectors
        - **luks** – Not documented

*Object* BlockdevQcow2Encryption (Since: 2.10)
:   Members:
    :   - **format** ([`BlockdevQcow2EncryptionFormat`](qemu-qmp-ref.md#enum-QMP-block-core.BlockdevQcow2EncryptionFormat "QMP:block-core.BlockdevQcow2EncryptionFormat")) – encryption format
        - When `format` is `aes`: The members of [`QCryptoBlockOptionsQCow`](qemu-qmp-ref.md#object-QMP-crypto.QCryptoBlockOptionsQCow "QMP:crypto.QCryptoBlockOptionsQCow").
        - When `format` is `luks`: The members of [`QCryptoBlockOptionsLUKS`](qemu-qmp-ref.md#object-QMP-crypto.QCryptoBlockOptionsLUKS "QMP:crypto.QCryptoBlockOptionsLUKS").

*Object* BlockdevOptionsPreallocate (Since: 6.0)
:   Filter driver intended to be inserted between format and protocol
    node and do preallocation in protocol node on write.

    Members:
    :   - **prealloc-align** (`int`, *optional*) – on preallocation, align file length to this number,
          default 1048576 (1M)
        - **prealloc-size** (`int`, *optional*) – how much to preallocate, default 134217728 (128M)
        - The members of [`BlockdevOptionsGenericFormat`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsGenericFormat "QMP:block-core.BlockdevOptionsGenericFormat").

*Object* BlockdevOptionsQcow2 (Since: 2.9)
:   Driver specific block device options for qcow2.

    Members:
    :   - **lazy-refcounts** (`boolean`, *optional*) – whether to enable the lazy refcounts feature
          (default is taken from the image file)
        - **pass-discard-request** (`boolean`, *optional*) – whether discard requests to the qcow2 device
          should be forwarded to the data source
        - **pass-discard-snapshot** (`boolean`, *optional*) – whether discard requests for the data source
          should be issued when a snapshot operation (e.g. deleting a
          snapshot) frees clusters in the qcow2 file
        - **pass-discard-other** (`boolean`, *optional*) – whether discard requests for the data source
          should be issued on other occasions where a cluster gets freed
        - **discard-no-unref** (`boolean`, *optional*) – when enabled, data clusters will remain
          preallocated when they are no longer used, e.g. because they are
          discarded or converted to zero clusters. As usual, whether the
          old data is discarded or kept on the protocol level (i.e. in the
          image file) depends on the setting of the pass-discard-request
          option. Keeping the clusters preallocated prevents qcow2
          fragmentation that would otherwise be caused by freeing and
          re-allocating them later. Besides potential performance
          degradation, such fragmentation can lead to increased allocation
          of clusters past the end of the image file, resulting in image
          files whose file length can grow much larger than their guest
          disk size would suggest. If image file length is of concern
          (e.g. when storing qcow2 images directly on block devices), you
          should consider enabling this option. (since 8.1)
        - **overlap-check** ([`Qcow2OverlapChecks`](qemu-qmp-ref.md#alternate-QMP-block-core.Qcow2OverlapChecks "QMP:block-core.Qcow2OverlapChecks"), *optional*) – which overlap checks to perform for writes to the
          image, defaults to ‘cached’ (since 2.2)
        - **cache-size** (`int`, *optional*) – the maximum total size of the L2 table and refcount
          block caches in bytes (since 2.2)
        - **l2-cache-size** (`int`, *optional*) – the maximum size of the L2 table cache in bytes
          (since 2.2)
        - **l2-cache-entry-size** (`int`, *optional*) – the size of each entry in the L2 cache in
          bytes. It must be a power of two between 512 and the cluster
          size. The default value is the cluster size (since 2.12)
        - **refcount-cache-size** (`int`, *optional*) – the maximum size of the refcount block cache
          in bytes (since 2.2)
        - **cache-clean-interval** (`int`, *optional*) – clean unused entries in the L2 and refcount
          caches. The interval is in seconds. The default value is 600
          on supporting platforms, and 0 on other platforms. 0 disables
          this feature. (since 2.5)
        - **encrypt** ([`BlockdevQcow2Encryption`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevQcow2Encryption "QMP:block-core.BlockdevQcow2Encryption"), *optional*) – Image decryption options. Mandatory for encrypted images,
          except when doing a metadata-only probe of the image.
          (since 2.10)
        - **data-file** ([`BlockdevRef`](qemu-qmp-ref.md#alternate-QMP-block-core.BlockdevRef "QMP:block-core.BlockdevRef"), *optional*) – reference to or definition of the external data file.
          This may only be specified for images that require an external
          data file. If it is not specified for such an image, the data
          file name is loaded from the image file. (since 4.0)
        - The members of [`BlockdevOptionsGenericCOWFormat`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsGenericCOWFormat "QMP:block-core.BlockdevOptionsGenericCOWFormat").

*Enum* SshHostKeyCheckMode (Since: 2.12)
:   Values:
    :   - **none** – Don’t check the host key at all
        - **hash** – Compare the host key with a given hash
        - **known_hosts** – Check the host key against the known_hosts file

*Enum* SshHostKeyCheckHashType (Since: 2.12)
:   Values:
    :   - **md5** – The given hash is an md5 hash
        - **sha1** – The given hash is an sha1 hash
        - **sha256** – The given hash is an sha256 hash

*Object* SshHostKeyHash (Since: 2.12)
:   Members:
    :   - **type** ([`SshHostKeyCheckHashType`](qemu-qmp-ref.md#enum-QMP-block-core.SshHostKeyCheckHashType "QMP:block-core.SshHostKeyCheckHashType")) – The hash algorithm used for the hash
        - **hash** (`string`) – The expected hash value

*Object* SshHostKeyCheck (Since: 2.12)
:   Members:
    :   - **mode** ([`SshHostKeyCheckMode`](qemu-qmp-ref.md#enum-QMP-block-core.SshHostKeyCheckMode "QMP:block-core.SshHostKeyCheckMode")) – How to check the host key
        - When `mode` is `hash`: The members of [`SshHostKeyHash`](qemu-qmp-ref.md#object-QMP-block-core.SshHostKeyHash "QMP:block-core.SshHostKeyHash").

*Object* BlockdevOptionsSsh (Since: 2.9)
:   Members:
    :   - **server** ([`InetSocketAddress`](qemu-qmp-ref.md#object-QMP-sockets.InetSocketAddress "QMP:sockets.InetSocketAddress")) – host address
        - **path** (`string`) – path to the image on the host
        - **user** (`string`, *optional*) – user as which to connect, defaults to current local user name
        - **host-key-check** ([`SshHostKeyCheck`](qemu-qmp-ref.md#object-QMP-block-core.SshHostKeyCheck "QMP:block-core.SshHostKeyCheck"), *optional*) – Defines how and what to check the host key against
          (default: known_hosts)

*Enum* BlkdebugEvent (Since: 2.9)
:   Trigger events supported by blkdebug.

    Values:
    :   - **l1_shrink_write_table** – write zeros to the l1 table to shrink image.
          (since 2.11)
        - **l1_shrink_free_l2_clusters** – discard the l2 tables. (since 2.11)
        - **cor_write** – a write due to copy-on-read (since 2.11)
        - **cluster_alloc_space** – an allocation of file space for a cluster
          (since 4.1)
        - **none** – triggers once at creation of the blkdebug node (since 4.1)
        - **l1_update** – Not documented
        - **l1_grow_alloc_table** – Not documented
        - **l1_grow_write_table** – Not documented
        - **l1_grow_activate_table** – Not documented
        - **l2_load** – Not documented
        - **l2_update** – Not documented
        - **l2_update_compressed** – Not documented
        - **l2_alloc_cow_read** – Not documented
        - **l2_alloc_write** – Not documented
        - **read_aio** – Not documented
        - **read_backing_aio** – Not documented
        - **read_compressed** – Not documented
        - **write_aio** – Not documented
        - **write_compressed** – Not documented
        - **vmstate_load** – Not documented
        - **vmstate_save** – Not documented
        - **cow_read** – Not documented
        - **cow_write** – Not documented
        - **reftable_load** – Not documented
        - **reftable_grow** – Not documented
        - **reftable_update** – Not documented
        - **refblock_load** – Not documented
        - **refblock_update** – Not documented
        - **refblock_update_part** – Not documented
        - **refblock_alloc** – Not documented
        - **refblock_alloc_hookup** – Not documented
        - **refblock_alloc_write** – Not documented
        - **refblock_alloc_write_blocks** – Not documented
        - **refblock_alloc_write_table** – Not documented
        - **refblock_alloc_switch_table** – Not documented
        - **cluster_alloc** – Not documented
        - **cluster_alloc_bytes** – Not documented
        - **cluster_free** – Not documented
        - **flush_to_os** – Not documented
        - **flush_to_disk** – Not documented
        - **pwritev_rmw_head** – Not documented
        - **pwritev_rmw_after_head** – Not documented
        - **pwritev_rmw_tail** – Not documented
        - **pwritev_rmw_after_tail** – Not documented
        - **pwritev** – Not documented
        - **pwritev_zero** – Not documented
        - **pwritev_done** – Not documented
        - **empty_image_prepare** – Not documented

*Enum* BlkdebugIOType (Since: 4.1)
:   Kinds of I/O that blkdebug can inject errors in.

    Values:
    :   - **read** – .bdrv_co_preadv()
        - **write** – .bdrv_co_pwritev()
        - **write-zeroes** – .bdrv_co_pwrite_zeroes()
        - **discard** – .bdrv_co_pdiscard()
        - **flush** – .bdrv_co_flush_to_disk()
        - **block-status** – .bdrv_co_block_status()

*Object* BlkdebugInjectErrorOptions (Since: 2.9)
:   Describes a single error injection for blkdebug.

    Members:
    :   - **event** ([`BlkdebugEvent`](qemu-qmp-ref.md#enum-QMP-block-core.BlkdebugEvent "QMP:block-core.BlkdebugEvent")) – trigger event
        - **state** (`int`, *optional*) – the state identifier blkdebug needs to be in to actually
          trigger the event; defaults to “any”
        - **iotype** ([`BlkdebugIOType`](qemu-qmp-ref.md#enum-QMP-block-core.BlkdebugIOType "QMP:block-core.BlkdebugIOType"), *optional*) – the type of I/O operations on which this error should be
          injected; defaults to “all read, write, write-zeroes, discard,
          and flush operations” (since: 4.1)
        - **errno** (`int`, *optional*) – error identifier (errno) to be returned; defaults to EIO
        - **delay-ns** (`int`, *optional*) – request delay before completion in nanoseconds
          (default: 0, since: 11.1)
        - **sector** (`int`, *optional*) – specifies the sector index which has to be affected in
          order to actually trigger the event; defaults to “any sector”
        - **once** (`boolean`, *optional*) – disables further events after this one has been triggered;
          defaults to false
        - **immediately** (`boolean`, *optional*) – fail immediately; defaults to false

*Object* BlkdebugSetStateOptions (Since: 2.9)
:   Describes a single state-change event for blkdebug.

    Members:
    :   - **event** ([`BlkdebugEvent`](qemu-qmp-ref.md#enum-QMP-block-core.BlkdebugEvent "QMP:block-core.BlkdebugEvent")) – trigger event
        - **state** (`int`, *optional*) – the current state identifier blkdebug needs to be in;
          defaults to “any”
        - **new_state** (`int`) – the state identifier blkdebug is supposed to assume if
          this event is triggered

*Object* BlockdevOptionsBlkdebug (Since: 2.9)
:   Driver specific block device options for blkdebug.

    Members:
    :   - **image** ([`BlockdevRef`](qemu-qmp-ref.md#alternate-QMP-block-core.BlockdevRef "QMP:block-core.BlockdevRef")) – underlying raw block device (or image file)
        - **config** (`string`, *optional*) – filename of the configuration file
        - **align** (`int`, *optional*) – required alignment for requests in bytes, must be positive
          power of 2, or 0 for default
        - **max-transfer** (`int`, *optional*) – maximum size for I/O transfers in bytes, must be
          positive multiple of `align` and of the underlying file’s request
          alignment (but need not be a power of 2), or 0 for default
          (since 2.10)
        - **opt-write-zero** (`int`, *optional*) – preferred alignment for write zero requests in
          bytes, must be positive multiple of `align` and of the underlying
          file’s request alignment (but need not be a power of 2), or 0
          for default (since 2.10)
        - **max-write-zero** (`int`, *optional*) – maximum size for write zero requests in bytes, must
          be positive multiple of `align`, of `opt-write-zero`, and of the
          underlying file’s request alignment (but need not be a power of
          2), or 0 for default (since 2.10)
        - **opt-discard** (`int`, *optional*) – preferred alignment for discard requests in bytes,
          must be positive multiple of `align` and of the underlying file’s
          request alignment (but need not be a power of 2), or 0 for
          default (since 2.10)
        - **max-discard** (`int`, *optional*) – maximum size for discard requests in bytes, must be
          positive multiple of `align`, of `opt-discard`, and of the
          underlying file’s request alignment (but need not be a power of
          2), or 0 for default (since 2.10)
        - **inject-error** (`[`[`BlkdebugInjectErrorOptions`](qemu-qmp-ref.md#object-QMP-block-core.BlkdebugInjectErrorOptions "QMP:block-core.BlkdebugInjectErrorOptions")`]`, *optional*) – array of error injection descriptions
        - **set-state** (`[`[`BlkdebugSetStateOptions`](qemu-qmp-ref.md#object-QMP-block-core.BlkdebugSetStateOptions "QMP:block-core.BlkdebugSetStateOptions")`]`, *optional*) – array of state-change descriptions
        - **take-child-perms** (`[`[`BlockPermission`](qemu-qmp-ref.md#enum-QMP-block-core.BlockPermission "QMP:block-core.BlockPermission")`]`, *optional*) – Permissions to take on `image` in addition to what
          is necessary anyway (which depends on how the blkdebug node is
          used). Defaults to none. (since 5.0)
        - **unshare-child-perms** (`[`[`BlockPermission`](qemu-qmp-ref.md#enum-QMP-block-core.BlockPermission "QMP:block-core.BlockPermission")`]`, *optional*) – Permissions not to share on `image` in addition
          to what cannot be shared anyway (which depends on how the
          blkdebug node is used). Defaults to none. (since 5.0)

*Object* BlockdevOptionsBlklogwrites (Since: 3.0)
:   Driver specific block device options for blklogwrites.

    Members:
    :   - **file** ([`BlockdevRef`](qemu-qmp-ref.md#alternate-QMP-block-core.BlockdevRef "QMP:block-core.BlockdevRef")) – block device
        - **log** ([`BlockdevRef`](qemu-qmp-ref.md#alternate-QMP-block-core.BlockdevRef "QMP:block-core.BlockdevRef")) – block device used to log writes to `file`
        - **log-sector-size** (`int`, *optional*) – sector size used in logging writes to `file`,
          determines granularity of offsets and sizes of writes
          (default: 512)
        - **log-append** (`boolean`, *optional*) – append to an existing log (default: false)
        - **log-super-update-interval** (`int`, *optional*) – interval of write requests after which
          the log super block is updated to disk (default: 4096)

*Object* BlockdevOptionsBlkverify (Since: 2.9)
:   Driver specific block device options for blkverify.

    Members:
    :   - **test** ([`BlockdevRef`](qemu-qmp-ref.md#alternate-QMP-block-core.BlockdevRef "QMP:block-core.BlockdevRef")) – block device to be tested
        - **raw** ([`BlockdevRef`](qemu-qmp-ref.md#alternate-QMP-block-core.BlockdevRef "QMP:block-core.BlockdevRef")) – raw image used for verification

*Object* BlockdevOptionsBlkreplay (Since: 4.2)
:   Driver specific block device options for blkreplay.

    Members:
    :   - **image** ([`BlockdevRef`](qemu-qmp-ref.md#alternate-QMP-block-core.BlockdevRef "QMP:block-core.BlockdevRef")) – disk image which should be controlled with blkreplay

*Enum* QuorumReadPattern (Since: 2.9)
:   An enumeration of quorum read patterns.

    Values:
    :   - **quorum** – read all the children and do a quorum vote on reads
        - **fifo** – read only from the first child that has not failed

*Object* BlockdevOptionsQuorum (Since: 2.9)
:   Driver specific block device options for Quorum

    Members:
    :   - **blkverify** (`boolean`, *optional*) – true if the driver must print content mismatch set to
          false by default
        - **children** (`[`[`BlockdevRef`](qemu-qmp-ref.md#alternate-QMP-block-core.BlockdevRef "QMP:block-core.BlockdevRef")`]`) – the children block devices to use
        - **vote-threshold** (`int`) – the vote limit under which a read will fail
        - **rewrite-corrupted** (`boolean`, *optional*) – rewrite corrupted data when quorum is reached
          (Since 2.1)
        - **read-pattern** ([`QuorumReadPattern`](qemu-qmp-ref.md#enum-QMP-block-core.QuorumReadPattern "QMP:block-core.QuorumReadPattern"), *optional*) – choose read pattern and set to quorum by default
          (Since 2.2)

*Object* BlockdevOptionsIoUring (Since: 7.2)
:   *Availability*: `CONFIG_BLKIO`

    Driver specific block device options for the io_uring backend.

    Members:
    :   - **filename** (`string`) – path to the image file

*Object* BlockdevOptionsNvmeIoUring (Since: 7.2)
:   *Availability*: `CONFIG_BLKIO`

    Driver specific block device options for the nvme-io_uring backend.

    Members:
    :   - **path** (`string`) – path to the NVMe namespace’s character device (e.g.
          /dev/ng0n1).

*Object* BlockdevOptionsVirtioBlkVfioPci (Since: 7.2)
:   *Availability*: `CONFIG_BLKIO`

    Driver specific block device options for the virtio-blk-vfio-pci
    backend.

    Members:
    :   - **path** (`string`) – path to the PCI device’s sysfs directory (e.g.
          /sys/bus/pci/devices/0000:00:01.0).

*Object* BlockdevOptionsVirtioBlkVhostUser (Since: 7.2)
:   *Availability*: `CONFIG_BLKIO`

    Driver specific block device options for the virtio-blk-vhost-user
    backend.

    Members:
    :   - **path** (`string`) – path to the vhost-user UNIX domain socket.

*Object* BlockdevOptionsVirtioBlkVhostVdpa (Since: 7.2)
:   *Availability*: `CONFIG_BLKIO`

    Driver specific block device options for the virtio-blk-vhost-vdpa
    backend.

    Members:
    :   - **path** (`string`) – path to the vhost-vdpa character device.

    Features:
    :   - **fdset** – Member `path` supports the special “/dev/fdset/N” path
          (since 8.1)

*Enum* IscsiTransport (Since: 2.9)
:   An enumeration of libiscsi transport types

    Values:
    :   - **tcp** – Not documented
        - **iser** – Not documented

*Enum* IscsiHeaderDigest (Since: 2.9)
:   An enumeration of header digests supported by libiscsi

    Values:
    :   - **crc32c** – Not documented
        - **none** – Not documented
        - **crc32c-none** – Not documented
        - **none-crc32c** – Not documented

*Object* BlockdevOptionsIscsi (Since: 2.9)
:   Driver specific block device options for iscsi

    Members:
    :   - **transport** ([`IscsiTransport`](qemu-qmp-ref.md#enum-QMP-block-core.IscsiTransport "QMP:block-core.IscsiTransport")) – The iscsi transport type
        - **portal** (`string`) – The address of the iscsi portal
        - **target** (`string`) – The target iqn name
        - **lun** (`int`, *optional*) – LUN to connect to. Defaults to 0.
        - **user** (`string`, *optional*) – User name to log in with. If omitted, no CHAP authentication
          is performed.
        - **password-secret** (`string`, *optional*) – The ID of a QCryptoSecret object providing the
          password for the login. This option is required if `user` is
          specified.
        - **initiator-name** (`string`, *optional*) – The iqn name we want to identify to the target as.
          If this option is not specified, an initiator name is generated
          automatically.
        - **header-digest** ([`IscsiHeaderDigest`](qemu-qmp-ref.md#enum-QMP-block-core.IscsiHeaderDigest "QMP:block-core.IscsiHeaderDigest"), *optional*) – The desired header digest. Defaults to none-crc32c.
        - **timeout** (`int`, *optional*) – Timeout in seconds after which a request will timeout. 0
          means no timeout and is the default.

*Enum* RbdAuthMode (Since: 3.0)
:   Values:
    :   - **cephx** – Not documented
        - **none** – Not documented

*Enum* RbdImageEncryptionFormat (Since: 6.1)
:   Values:
    :   - **luks-any** – Used for opening either luks or luks2 (Since 8.0)
        - **luks** – Not documented
        - **luks2** – Not documented

*Object* RbdEncryptionOptionsLUKSBase (Since: 6.1)
:   Members:
    :   - **key-secret** (`string`) – ID of a QCryptoSecret object providing a passphrase for
          unlocking the encryption

*Object* RbdEncryptionCreateOptionsLUKSBase (Since: 6.1)
:   Members:
    :   - **cipher-alg** ([`QCryptoCipherAlgo`](qemu-qmp-ref.md#enum-QMP-crypto.QCryptoCipherAlgo "QMP:crypto.QCryptoCipherAlgo"), *optional*) – The encryption algorithm
        - The members of [`RbdEncryptionOptionsLUKSBase`](qemu-qmp-ref.md#object-QMP-block-core.RbdEncryptionOptionsLUKSBase "QMP:block-core.RbdEncryptionOptionsLUKSBase").

*Object* RbdEncryptionOptionsLUKS (Since: 6.1)
:   Members:
    :   - The members of [`RbdEncryptionOptionsLUKSBase`](qemu-qmp-ref.md#object-QMP-block-core.RbdEncryptionOptionsLUKSBase "QMP:block-core.RbdEncryptionOptionsLUKSBase").

*Object* RbdEncryptionOptionsLUKS2 (Since: 6.1)
:   Members:
    :   - The members of [`RbdEncryptionOptionsLUKSBase`](qemu-qmp-ref.md#object-QMP-block-core.RbdEncryptionOptionsLUKSBase "QMP:block-core.RbdEncryptionOptionsLUKSBase").

*Object* RbdEncryptionOptionsLUKSAny (Since: 8.0)
:   Members:
    :   - The members of [`RbdEncryptionOptionsLUKSBase`](qemu-qmp-ref.md#object-QMP-block-core.RbdEncryptionOptionsLUKSBase "QMP:block-core.RbdEncryptionOptionsLUKSBase").

*Object* RbdEncryptionCreateOptionsLUKS (Since: 6.1)
:   Members:
    :   - The members of [`RbdEncryptionCreateOptionsLUKSBase`](qemu-qmp-ref.md#object-QMP-block-core.RbdEncryptionCreateOptionsLUKSBase "QMP:block-core.RbdEncryptionCreateOptionsLUKSBase").

*Object* RbdEncryptionCreateOptionsLUKS2 (Since: 6.1)
:   Members:
    :   - The members of [`RbdEncryptionCreateOptionsLUKSBase`](qemu-qmp-ref.md#object-QMP-block-core.RbdEncryptionCreateOptionsLUKSBase "QMP:block-core.RbdEncryptionCreateOptionsLUKSBase").

*Object* RbdEncryptionOptions (Since: 6.1)
:   Members:
    :   - **format** ([`RbdImageEncryptionFormat`](qemu-qmp-ref.md#enum-QMP-block-core.RbdImageEncryptionFormat "QMP:block-core.RbdImageEncryptionFormat")) – Encryption format.
        - **parent** ([`RbdEncryptionOptions`](qemu-qmp-ref.md#object-QMP-block-core.RbdEncryptionOptions "QMP:block-core.RbdEncryptionOptions"), *optional*) – Parent image encryption options (for cloned images). Can
          be left unspecified if this cloned image is encrypted using the
          same format and secret as its parent image (i.e. not explicitly
          formatted) or if its parent image is not encrypted. (Since 8.0)
        - When `format` is `luks`: The members of [`RbdEncryptionOptionsLUKS`](qemu-qmp-ref.md#object-QMP-block-core.RbdEncryptionOptionsLUKS "QMP:block-core.RbdEncryptionOptionsLUKS").
        - When `format` is `luks2`: The members of [`RbdEncryptionOptionsLUKS2`](qemu-qmp-ref.md#object-QMP-block-core.RbdEncryptionOptionsLUKS2 "QMP:block-core.RbdEncryptionOptionsLUKS2").
        - When `format` is `luks-any`: The members of [`RbdEncryptionOptionsLUKSAny`](qemu-qmp-ref.md#object-QMP-block-core.RbdEncryptionOptionsLUKSAny "QMP:block-core.RbdEncryptionOptionsLUKSAny").

*Object* RbdEncryptionCreateOptions (Since: 6.1)
:   Members:
    :   - **format** ([`RbdImageEncryptionFormat`](qemu-qmp-ref.md#enum-QMP-block-core.RbdImageEncryptionFormat "QMP:block-core.RbdImageEncryptionFormat")) – Encryption format.
        - When `format` is `luks`: The members of [`RbdEncryptionCreateOptionsLUKS`](qemu-qmp-ref.md#object-QMP-block-core.RbdEncryptionCreateOptionsLUKS "QMP:block-core.RbdEncryptionCreateOptionsLUKS").
        - When `format` is `luks2`: The members of [`RbdEncryptionCreateOptionsLUKS2`](qemu-qmp-ref.md#object-QMP-block-core.RbdEncryptionCreateOptionsLUKS2 "QMP:block-core.RbdEncryptionCreateOptionsLUKS2").

*Object* BlockdevOptionsRbd (Since: 2.9)
:   Members:
    :   - **pool** (`string`) – Ceph pool name.
        - **namespace** (`string`, *optional*) – Rados namespace name in the Ceph pool. (Since 5.0)
        - **image** (`string`) – Image name in the Ceph pool.
        - **conf** (`string`, *optional*) – path to Ceph configuration file. Values in the configuration
          file will be overridden by options specified via QAPI.
        - **snapshot** (`string`, *optional*) – Ceph snapshot name.
        - **encrypt** ([`RbdEncryptionOptions`](qemu-qmp-ref.md#object-QMP-block-core.RbdEncryptionOptions "QMP:block-core.RbdEncryptionOptions"), *optional*) – Image encryption options. (Since 6.1)
        - **user** (`string`, *optional*) – Ceph id name.
        - **auth-client-required** (`[`[`RbdAuthMode`](qemu-qmp-ref.md#enum-QMP-block-core.RbdAuthMode "QMP:block-core.RbdAuthMode")`]`, *optional*) – Acceptable authentication modes. This maps
          to Ceph configuration option “auth_client_required”.
          (Since 3.0)
        - **key-secret** (`string`, *optional*) – ID of a QCryptoSecret object providing a key for cephx
          authentication. This maps to Ceph configuration option “key”.
          (Since 3.0)
        - **server** (`[`[`InetSocketAddressBase`](qemu-qmp-ref.md#object-QMP-sockets.InetSocketAddressBase "QMP:sockets.InetSocketAddressBase")`]`, *optional*) – Monitor host address and port. This maps to the “mon_host”
          Ceph option.

*Enum* ReplicationMode (Since: 2.9)
:   *Availability*: `CONFIG_REPLICATION`

    An enumeration of replication modes.

    Values:
    :   - **primary** – Primary mode, the vm’s state will be sent to secondary
          QEMU.
        - **secondary** – Secondary mode, receive the vm’s state from primary
          QEMU.

*Object* BlockdevOptionsReplication (Since: 2.9)
:   *Availability*: `CONFIG_REPLICATION`

    Driver specific block device options for replication

    Members:
    :   - **mode** ([`ReplicationMode`](qemu-qmp-ref.md#enum-QMP-block-core.ReplicationMode "QMP:block-core.ReplicationMode")) – the replication mode
        - **top-id** (`string`, *optional*) – In secondary mode, node name or device ID of the root node
          who owns the replication node chain. Must not be given in
          primary mode.
        - The members of [`BlockdevOptionsGenericFormat`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsGenericFormat "QMP:block-core.BlockdevOptionsGenericFormat").

*Enum* NFSTransport (Since: 2.9)
:   An enumeration of NFS transport types

    Values:
    :   - **inet** – TCP transport

*Object* NFSServer (Since: 2.9)
:   Captures the address of the socket

    Members:
    :   - **type** ([`NFSTransport`](qemu-qmp-ref.md#enum-QMP-block-core.NFSTransport "QMP:block-core.NFSTransport")) – transport type used for NFS (only TCP supported)
        - **host** (`string`) – host address for NFS server

*Object* BlockdevOptionsNfs (Since: 2.9)
:   Driver specific block device option for NFS

    Members:
    :   - **server** ([`NFSServer`](qemu-qmp-ref.md#object-QMP-block-core.NFSServer "QMP:block-core.NFSServer")) – host address
        - **path** (`string`) – path of the image on the host
        - **user** (`int`, *optional*) – UID value to use when talking to the server (defaults to
          65534 on Windows and getuid() on unix)
        - **group** (`int`, *optional*) – GID value to use when talking to the server (defaults to
          65534 on Windows and getgid() in unix)
        - **tcp-syn-count** (`int`, *optional*) – number of SYNs during the session establishment
          (defaults to libnfs default)
        - **readahead-size** (`int`, *optional*) – set the readahead size in bytes (defaults to libnfs
          default)
        - **page-cache-size** (`int`, *optional*) – set the pagecache size in bytes (defaults to
          libnfs default)
        - **debug** (`int`, *optional*) – set the NFS debug level (max 2) (defaults to libnfs default)

*Object* BlockdevOptionsCurlBase (Since: 2.9)
:   Driver specific block device options shared by all protocols
    supported by the curl backend.

    Members:
    :   - **url** (`string`) – URL of the image file
        - **readahead** (`int`, *optional*) – Size of the read-ahead cache; must be a multiple of 512
          (defaults to 256 kB)
        - **timeout** (`int`, *optional*) – Timeout for connections, in seconds (defaults to 5)
        - **username** (`string`, *optional*) – Username for authentication (defaults to none)
        - **password-secret** (`string`, *optional*) – ID of a QCryptoSecret object providing a password
          for authentication (defaults to no password)
        - **proxy-username** (`string`, *optional*) – Username for proxy authentication (defaults to
          none)
        - **proxy-password-secret** (`string`, *optional*) – ID of a QCryptoSecret object providing a
          password for proxy authentication (defaults to no password)

*Object* BlockdevOptionsCurlHttp (Since: 2.9)
:   Driver specific block device options for HTTP connections over the
    curl backend. URLs must start with “<http://>”.

    Members:
    :   - **cookie** (`string`, *optional*) – List of cookies to set; format is “name1=content1;
          name2=content2;” as explained by CURLOPT_COOKIE(3). Defaults to
          no cookies.
        - **cookie-secret** (`string`, *optional*) – ID of a QCryptoSecret object providing the cookie
          data in a secure way. See `cookie` for the format. (since 2.10)
        - **force-range** (`boolean`, *optional*) – Don’t issue a HEAD HTTP request to discover if the
          http server supports range requests and rely only on GET
          requests. This is especially useful for S3 presigned URLs where
          HEAD requests are unauthorized. (default: false; since 11.0)
        - The members of [`BlockdevOptionsCurlBase`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsCurlBase "QMP:block-core.BlockdevOptionsCurlBase").

*Object* BlockdevOptionsCurlHttps (Since: 2.9)
:   Driver specific block device options for HTTPS connections over the
    curl backend. URLs must start with “[https://](qemu-qmp-ref.md)”.

    Members:
    :   - **sslverify** (`boolean`, *optional*) – Whether to verify the SSL certificate’s validity
          (defaults to true)
        - The members of [`BlockdevOptionsCurlHttp`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsCurlHttp "QMP:block-core.BlockdevOptionsCurlHttp").

*Object* BlockdevOptionsCurlFtp (Since: 2.9)
:   Driver specific block device options for FTP connections over the
    curl backend. URLs must start with “<ftp://>”.

    Members:
    :   - The members of [`BlockdevOptionsCurlBase`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsCurlBase "QMP:block-core.BlockdevOptionsCurlBase").

*Object* BlockdevOptionsCurlFtps (Since: 2.9)
:   Driver specific block device options for FTPS connections over the
    curl backend. URLs must start with “ftps://”.

    Members:
    :   - **sslverify** (`boolean`, *optional*) – Whether to verify the SSL certificate’s validity
          (defaults to true)
        - The members of [`BlockdevOptionsCurlBase`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsCurlBase "QMP:block-core.BlockdevOptionsCurlBase").

*Object* BlockdevOptionsNbd (Since: 2.9)
:   Driver specific block device options for NBD.

    Members:
    :   - **server** ([`SocketAddress`](qemu-qmp-ref.md#object-QMP-sockets.SocketAddress "QMP:sockets.SocketAddress")) – NBD server address
        - **export** (`string`, *optional*) – export name
        - **tls-creds** (`string`, *optional*) – TLS credentials ID
        - **tls-hostname** (`string`, *optional*) – TLS hostname override for certificate validation
          (Since 7.0)
        - **x-dirty-bitmap** (`string`, *optional*) – A metadata context name such as
          “qemu:dirty-bitmap:NAME” or “qemu:allocation-depth” to query in
          place of the traditional “base:allocation” block status (see
          NBD_OPT_LIST_META_CONTEXT in the NBD protocol; and yes, naming
          this option x-context would have made more sense) (since 3.0)
        - **reconnect-delay** (`int`, *optional*) – On an unexpected disconnect, the nbd client tries
          to connect again until succeeding or encountering a serious
          error. During the first `reconnect-delay` seconds, all requests
          are paused and will be rerun on a successful reconnect. After
          that time, any delayed requests and all future requests before a
          successful reconnect will immediately fail. Default 0
          (Since 4.2)
        - **open-timeout** (`int`, *optional*) – In seconds. If zero, the nbd driver tries the
          connection only once, and fails to open if the connection fails.
          If non-zero, the nbd driver will repeat connection attempts
          until successful or until `open-timeout` seconds have elapsed.
          Default 0 (Since 7.0)

    Features:
    :   - **unstable** – Member `x-dirty-bitmap` is experimental.

*Object* BlockdevOptionsRaw (Since: 2.9)
:   Driver specific block device options for the raw driver.

    Members:
    :   - **offset** (`int`, *optional*) – position where the block device starts
        - **size** (`int`, *optional*) – the assumed size of the device
        - The members of [`BlockdevOptionsGenericFormat`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsGenericFormat "QMP:block-core.BlockdevOptionsGenericFormat").

*Object* BlockdevOptionsThrottle (Since: 2.11)
:   Driver specific block device options for the throttle driver

    Members:
    :   - **throttle-group** (`string`) – the name of the throttle-group object to use. It
          must already exist.
        - **file** ([`BlockdevRef`](qemu-qmp-ref.md#alternate-QMP-block-core.BlockdevRef "QMP:block-core.BlockdevRef")) – reference to or definition of the data source block device

*Object* BlockdevOptionsCor (Since: 6.0)
:   Driver specific block device options for the copy-on-read driver.

    Members:
    :   - **bottom** (`string`, *optional*) – The name of a non-filter node (allocation-bearing layer)
          that limits the COR operations in the backing chain (inclusive),
          so that no data below this node will be copied by this filter.
          If option is absent, the limit is not applied, so that data from
          all backing layers may be copied.
        - The members of [`BlockdevOptionsGenericFormat`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsGenericFormat "QMP:block-core.BlockdevOptionsGenericFormat").

*Enum* OnCbwError (Since: 7.1)
:   An enumeration of possible behaviors for copy-before-write operation
    failures.

    Values:
    :   - **break-guest-write** – report the error to the guest. This way, the
          guest will not be able to overwrite areas that cannot be backed
          up, so the backup process remains valid.
        - **break-snapshot** – continue guest write. Doing so will make the
          provided snapshot state invalid and any backup or export process
          based on it will finally fail.

*Object* BlockdevOptionsCbw (Since: 6.2)
:   Driver specific block device options for the copy-before-write
    driver, which does so called copy-before-write operations: when data
    is written to the filter, the filter first reads corresponding
    blocks from its file child and copies them to `target` child. After
    successfully copying, the write request is propagated to file child.
    If copying fails, the original write request is failed too and no
    data is written to file child.

    Members:
    :   - **target** ([`BlockdevRef`](qemu-qmp-ref.md#alternate-QMP-block-core.BlockdevRef "QMP:block-core.BlockdevRef")) – The target for copy-before-write operations.
        - **bitmap** ([`BlockDirtyBitmap`](qemu-qmp-ref.md#object-QMP-block-core.BlockDirtyBitmap "QMP:block-core.BlockDirtyBitmap"), *optional*) – If specified, copy-before-write filter will do
          copy-before-write operations only for dirty regions of the
          bitmap. Bitmap size must be equal to length of file and target
          child of the filter. Note also, that bitmap is used only to
          initialize internal bitmap of the process, so further
          modifications (or removing) of specified bitmap doesn’t
          influence the filter. (Since 7.0)
        - **on-cbw-error** ([`OnCbwError`](qemu-qmp-ref.md#enum-QMP-block-core.OnCbwError "QMP:block-core.OnCbwError"), *optional*) – Behavior on failure of copy-before-write operation.
          Default is `break-guest-write`. (Since 7.1)
        - **cbw-timeout** (`int`, *optional*) – Zero means no limit. Non-zero sets the timeout in
          seconds for copy-before-write operation. When a timeout occurs,
          the respective copy-before-write operation will fail, and the
          `on-cbw-error` parameter will decide how this failure is handled.
          Default 0. (Since 7.1)
        - **min-cluster-size** (`int`, *optional*) – Minimum size of blocks used by copy-before-write
          operations. Has to be a power of 2. No effect if smaller than
          the maximum of the target’s cluster size and 64 KiB. Default 0.
          (Since 9.2)
        - The members of [`BlockdevOptionsGenericFormat`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsGenericFormat "QMP:block-core.BlockdevOptionsGenericFormat").

*Object* BlockdevOptions (Since: 2.9)
:   Options for creating a block device. Many options are available for
    all block devices, independent of the block driver:

    Members:
    :   - **driver** ([`BlockdevDriver`](qemu-qmp-ref.md#enum-QMP-block-core.BlockdevDriver "QMP:block-core.BlockdevDriver")) – block driver name
        - **node-name** (`string`, *optional*) – the node name of the new node. This option is required
          on the top level of [`blockdev-add`](qemu-qmp-ref.md#command-QMP-block-core.blockdev-add "QMP:block-core.blockdev-add"). Valid node names start with
          an alphabetic character and may contain only alphanumeric
          characters, ‘-’, ‘.’ and ‘_’. Their maximum length is 31
          characters. (Since 2.0)
        - **discard** ([`BlockdevDiscardOptions`](qemu-qmp-ref.md#enum-QMP-block-core.BlockdevDiscardOptions "QMP:block-core.BlockdevDiscardOptions"), *optional*) – discard-related options (default: ignore)
        - **cache** ([`BlockdevCacheOptions`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevCacheOptions "QMP:block-core.BlockdevCacheOptions"), *optional*) – cache-related options
        - **active** (`boolean`, *optional*) – whether the block node should be activated (default: true).
          Having inactive block nodes is useful primarily for migration
          because it allows opening an image on the destination while the
          source is still holding locks for it. (Since 10.0)
        - **read-only** (`boolean`, *optional*) – whether the block device should be read-only (default:
          false). Note that some block drivers support only read-only
          access, either generally or in certain configurations. In this
          case, the default value does not work and the option must be
          specified explicitly.
        - **auto-read-only** (`boolean`, *optional*) – if true and `read-only` is false, QEMU may
          automatically decide not to open the image read-write as
          requested, but fall back to read-only instead (and switch
          between the modes later), e.g. depending on whether the image
          file is writable or whether a writing user is attached to the
          node (default: false, since 3.1)
        - **detect-zeroes** ([`BlockdevDetectZeroesOptions`](qemu-qmp-ref.md#enum-QMP-block-core.BlockdevDetectZeroesOptions "QMP:block-core.BlockdevDetectZeroesOptions"), *optional*) – detect and optimize zero writes (Since 2.1)
          (default: off)
        - **force-share** (`boolean`, *optional*) – force share all permission on added nodes. Requires
          read-only=true. (Since 2.10)
        - When `driver` is `blkdebug`: The members of [`BlockdevOptionsBlkdebug`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsBlkdebug "QMP:block-core.BlockdevOptionsBlkdebug").
        - When `driver` is `blklogwrites`: The members of [`BlockdevOptionsBlklogwrites`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsBlklogwrites "QMP:block-core.BlockdevOptionsBlklogwrites").
        - When `driver` is `blkverify`: The members of [`BlockdevOptionsBlkverify`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsBlkverify "QMP:block-core.BlockdevOptionsBlkverify").
        - When `driver` is `blkreplay`: The members of [`BlockdevOptionsBlkreplay`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsBlkreplay "QMP:block-core.BlockdevOptionsBlkreplay").
        - When `driver` is `bochs`: The members of [`BlockdevOptionsGenericFormat`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsGenericFormat "QMP:block-core.BlockdevOptionsGenericFormat").
        - When `driver` is `cloop`: The members of [`BlockdevOptionsGenericFormat`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsGenericFormat "QMP:block-core.BlockdevOptionsGenericFormat").
        - When `driver` is `compress`: The members of [`BlockdevOptionsGenericFormat`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsGenericFormat "QMP:block-core.BlockdevOptionsGenericFormat").
        - When `driver` is `copy-before-write`: The members of [`BlockdevOptionsCbw`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsCbw "QMP:block-core.BlockdevOptionsCbw").
        - When `driver` is `copy-on-read`: The members of [`BlockdevOptionsCor`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsCor "QMP:block-core.BlockdevOptionsCor").
        - When `driver` is `dmg`: The members of [`BlockdevOptionsGenericFormat`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsGenericFormat "QMP:block-core.BlockdevOptionsGenericFormat").
        - When `driver` is `file`: The members of [`BlockdevOptionsFile`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsFile "QMP:block-core.BlockdevOptionsFile").
        - When `driver` is `ftp`: The members of [`BlockdevOptionsCurlFtp`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsCurlFtp "QMP:block-core.BlockdevOptionsCurlFtp").
        - When `driver` is `ftps`: The members of [`BlockdevOptionsCurlFtps`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsCurlFtps "QMP:block-core.BlockdevOptionsCurlFtps").
        - When `driver` is `host_cdrom`: The members of [`BlockdevOptionsFile`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsFile "QMP:block-core.BlockdevOptionsFile").
        - When `driver` is `host_device`: The members of [`BlockdevOptionsFile`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsFile "QMP:block-core.BlockdevOptionsFile").
        - When `driver` is `http`: The members of [`BlockdevOptionsCurlHttp`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsCurlHttp "QMP:block-core.BlockdevOptionsCurlHttp").
        - When `driver` is `https`: The members of [`BlockdevOptionsCurlHttps`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsCurlHttps "QMP:block-core.BlockdevOptionsCurlHttps").
        - When `driver` is `io_uring`: The members of [`BlockdevOptionsIoUring`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsIoUring "QMP:block-core.BlockdevOptionsIoUring").
        - When `driver` is `iscsi`: The members of [`BlockdevOptionsIscsi`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsIscsi "QMP:block-core.BlockdevOptionsIscsi").
        - When `driver` is `luks`: The members of [`BlockdevOptionsLUKS`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsLUKS "QMP:block-core.BlockdevOptionsLUKS").
        - When `driver` is `nbd`: The members of [`BlockdevOptionsNbd`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsNbd "QMP:block-core.BlockdevOptionsNbd").
        - When `driver` is `nfs`: The members of [`BlockdevOptionsNfs`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsNfs "QMP:block-core.BlockdevOptionsNfs").
        - When `driver` is `null-aio`: The members of [`BlockdevOptionsNull`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsNull "QMP:block-core.BlockdevOptionsNull").
        - When `driver` is `null-co`: The members of [`BlockdevOptionsNull`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsNull "QMP:block-core.BlockdevOptionsNull").
        - When `driver` is `nvme`: The members of [`BlockdevOptionsNVMe`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsNVMe "QMP:block-core.BlockdevOptionsNVMe").
        - When `driver` is `nvme-io_uring`: The members of [`BlockdevOptionsNvmeIoUring`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsNvmeIoUring "QMP:block-core.BlockdevOptionsNvmeIoUring").
        - When `driver` is `parallels`: The members of [`BlockdevOptionsGenericFormat`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsGenericFormat "QMP:block-core.BlockdevOptionsGenericFormat").
        - When `driver` is `preallocate`: The members of [`BlockdevOptionsPreallocate`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsPreallocate "QMP:block-core.BlockdevOptionsPreallocate").
        - When `driver` is `qcow2`: The members of [`BlockdevOptionsQcow2`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsQcow2 "QMP:block-core.BlockdevOptionsQcow2").
        - When `driver` is `qcow`: The members of [`BlockdevOptionsQcow`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsQcow "QMP:block-core.BlockdevOptionsQcow").
        - When `driver` is `qed`: The members of [`BlockdevOptionsGenericCOWFormat`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsGenericCOWFormat "QMP:block-core.BlockdevOptionsGenericCOWFormat").
        - When `driver` is `quorum`: The members of [`BlockdevOptionsQuorum`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsQuorum "QMP:block-core.BlockdevOptionsQuorum").
        - When `driver` is `raw`: The members of [`BlockdevOptionsRaw`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsRaw "QMP:block-core.BlockdevOptionsRaw").
        - When `driver` is `rbd`: The members of [`BlockdevOptionsRbd`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsRbd "QMP:block-core.BlockdevOptionsRbd").
        - When `driver` is `replication`: The members of [`BlockdevOptionsReplication`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsReplication "QMP:block-core.BlockdevOptionsReplication").
        - When `driver` is `snapshot-access`: The members of [`BlockdevOptionsGenericFormat`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsGenericFormat "QMP:block-core.BlockdevOptionsGenericFormat").
        - When `driver` is `ssh`: The members of [`BlockdevOptionsSsh`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsSsh "QMP:block-core.BlockdevOptionsSsh").
        - When `driver` is `throttle`: The members of [`BlockdevOptionsThrottle`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsThrottle "QMP:block-core.BlockdevOptionsThrottle").
        - When `driver` is `vdi`: The members of [`BlockdevOptionsGenericFormat`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsGenericFormat "QMP:block-core.BlockdevOptionsGenericFormat").
        - When `driver` is `vhdx`: The members of [`BlockdevOptionsGenericFormat`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsGenericFormat "QMP:block-core.BlockdevOptionsGenericFormat").
        - When `driver` is `virtio-blk-vfio-pci`: The members of [`BlockdevOptionsVirtioBlkVfioPci`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsVirtioBlkVfioPci "QMP:block-core.BlockdevOptionsVirtioBlkVfioPci").
        - When `driver` is `virtio-blk-vhost-user`: The members of [`BlockdevOptionsVirtioBlkVhostUser`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsVirtioBlkVhostUser "QMP:block-core.BlockdevOptionsVirtioBlkVhostUser").
        - When `driver` is `virtio-blk-vhost-vdpa`: The members of [`BlockdevOptionsVirtioBlkVhostVdpa`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsVirtioBlkVhostVdpa "QMP:block-core.BlockdevOptionsVirtioBlkVhostVdpa").
        - When `driver` is `vmdk`: The members of [`BlockdevOptionsGenericCOWFormat`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsGenericCOWFormat "QMP:block-core.BlockdevOptionsGenericCOWFormat").
        - When `driver` is `vpc`: The members of [`BlockdevOptionsGenericFormat`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsGenericFormat "QMP:block-core.BlockdevOptionsGenericFormat").
        - When `driver` is `vvfat`: The members of [`BlockdevOptionsVVFAT`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsVVFAT "QMP:block-core.BlockdevOptionsVVFAT").

*Alternate* BlockdevRef (Since: 2.9)
:   Reference to a block device.

    Alternatives:
    :   - **definition** ([`BlockdevOptions`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptions "QMP:block-core.BlockdevOptions")) – defines a new block device inline
        - **reference** (`string`) – references the ID of an existing block device

*Alternate* BlockdevRefOrNull (Since: 2.9)
:   Reference to a block device.

    Alternatives:
    :   - **definition** ([`BlockdevOptions`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptions "QMP:block-core.BlockdevOptions")) – defines a new block device inline
        - **reference** (`string`) – references the ID of an existing block device. An empty
          string means that no block device should be referenced.
          Deprecated; use null instead.
        - **null** (`null`) – No block device should be referenced (since 2.10)

*Command* blockdev-add (Since: 2.9)
:   Creates a new block device.

    Arguments:
    :   - The members of [`BlockdevOptions`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptions "QMP:block-core.BlockdevOptions").

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "blockdev-add",
    >      "arguments": {
    >           "driver": "qcow2",
    >           "node-name": "test1",
    >           "file": {
    >               "driver": "file",
    >               "filename": "test.qcow2"
    >            }
    >       }
    >     }
    > <- { "return": {} }
    > ```

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "blockdev-add",
    >      "arguments": {
    >           "driver": "qcow2",
    >           "node-name": "node0",
    >           "discard": "unmap",
    >           "cache": {
    >              "direct": true
    >            },
    >            "file": {
    >              "driver": "file",
    >              "filename": "/tmp/test.qcow2"
    >            },
    >            "backing": {
    >               "driver": "raw",
    >               "file": {
    >                  "driver": "file",
    >                  "filename": "/dev/fdset/4"
    >                }
    >            }
    >        }
    >      }
    >
    > <- { "return": {} }
    > ```

*Command* blockdev-reopen (Since: 6.1)
:   Reopens one or more block devices using the given set of options.
    Any option not specified will be reset to its default value
    regardless of its previous status. If an option cannot be changed
    or a particular driver does not support reopening then the command
    will return an error. All devices in the list are reopened in one
    transaction, so if one of them fails then the whole transaction is
    cancelled.

    The command receives a list of block devices to reopen. For each
    one of them, the top-level `node-name` option (from
    [`BlockdevOptions`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptions "QMP:block-core.BlockdevOptions")) must be specified and is used to select the block
    device to be reopened. Other `node-name` options must be either
    omitted or set to the current name of the appropriate node. This
    command won’t change any node name and any attempt to do it will
    result in an error.

    In the case of options that refer to child nodes, the behavior of
    this command depends on the value:

    > 1. A set of options ([`BlockdevOptions`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptions "QMP:block-core.BlockdevOptions")): the child is reopened with
    >    the specified set of options.
    > 2. A reference to the current child: the child is reopened using
    >    its existing set of options.
    > 3. A reference to a different node: the current child is replaced
    >    with the specified one.
    > 4. null: the current child (if any) is detached.

    Options (1) and (2) are supported in all cases. Option (3) is
    supported for `file` and `backing`, and option (4) for `backing` only.

    Unlike with [`blockdev-add`](qemu-qmp-ref.md#command-QMP-block-core.blockdev-add "QMP:block-core.blockdev-add"), the `backing` option must always be
    present unless the node being reopened does not have a backing file
    and its image does not have a default backing file name as part of
    its metadata.

    Arguments:
    :   - **options** (`[`[`BlockdevOptions`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptions "QMP:block-core.BlockdevOptions")`]`) – Not documented

*Command* blockdev-del (Since: 2.9)
:   Deletes a block device that has been added using [`blockdev-add`](qemu-qmp-ref.md#command-QMP-block-core.blockdev-add "QMP:block-core.blockdev-add").
    The command will fail if the node is attached to a device or is
    otherwise being used.

    Arguments:
    :   - **node-name** (`string`) – Name of the graph node to delete.

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "blockdev-add",
    >      "arguments": {
    >           "driver": "qcow2",
    >           "node-name": "node0",
    >           "file": {
    >               "driver": "file",
    >               "filename": "test.qcow2"
    >           }
    >      }
    >    }
    > <- { "return": {} }
    >
    > -> { "execute": "blockdev-del",
    >      "arguments": { "node-name": "node0" }
    >    }
    > <- { "return": {} }
    > ```

*Command* blockdev-set-active (Since: 10.0)
:   Activate or deactivate a block device. Use this to manage the
    handover of block devices on migration with qemu-storage-daemon.

    Activating a node automatically activates all of its child nodes
    first. Deactivating a node automatically deactivates any of its
    child nodes that are not in use by a still active node.

    Arguments:
    :   - **node-name** (`string`, *optional*) – Name of the graph node to activate or deactivate. By
          default, all nodes are affected by the operation.
        - **active** (`boolean`) – true if the nodes should be active when the command returns
          success, false if they should be inactive.

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "blockdev-set-active",
    >      "arguments": {
    >           "node-name": "node0",
    >           "active": false
    >      }
    >    }
    > <- { "return": {} }
    > ```

*Object* BlockdevCreateOptionsFile (Since: 2.12)
:   Driver specific image creation options for file.

    Members:
    :   - **filename** (`string`) – Filename for the new image file
        - **size** (`int`) – Size of the virtual disk in bytes
        - **preallocation** ([`PreallocMode`](qemu-qmp-ref.md#enum-QMP-block-core.PreallocMode "QMP:block-core.PreallocMode"), *optional*) – Preallocation mode for the new image (default: off;
          allowed values: off, falloc (if CONFIG_POSIX_FALLOCATE), full
          (if CONFIG_POSIX))
        - **nocow** (`boolean`, *optional*) – Turn off copy-on-write (valid only on btrfs; default: off)
        - **extent-size-hint** (`int`, *optional*) – Extent size hint to add to the image file; 0 for
          not adding an extent size hint (default: 1 MB, since 5.1)

*Object* BlockdevCreateOptionsLUKS (Since: 2.12)
:   Driver specific image creation options for LUKS.

    Members:
    :   - **file** ([`BlockdevRef`](qemu-qmp-ref.md#alternate-QMP-block-core.BlockdevRef "QMP:block-core.BlockdevRef"), *optional*) – Node to create the image format on, mandatory except when
          ‘preallocation’ is not requested
        - **header** ([`BlockdevRef`](qemu-qmp-ref.md#alternate-QMP-block-core.BlockdevRef "QMP:block-core.BlockdevRef"), *optional*) – Block device holding a detached LUKS header. (since 9.0)
        - **size** (`int`) – Size of the virtual disk in bytes
        - **preallocation** ([`PreallocMode`](qemu-qmp-ref.md#enum-QMP-block-core.PreallocMode "QMP:block-core.PreallocMode"), *optional*) – Preallocation mode for the new image (since: 4.2)
          (default: off; allowed values: off, metadata, falloc, full)
        - The members of [`QCryptoBlockCreateOptionsLUKS`](qemu-qmp-ref.md#object-QMP-crypto.QCryptoBlockCreateOptionsLUKS "QMP:crypto.QCryptoBlockCreateOptionsLUKS").

*Object* BlockdevCreateOptionsNfs (Since: 2.12)
:   Driver specific image creation options for NFS.

    Members:
    :   - **location** ([`BlockdevOptionsNfs`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsNfs "QMP:block-core.BlockdevOptionsNfs")) – Where to store the new image file
        - **size** (`int`) – Size of the virtual disk in bytes

*Object* BlockdevCreateOptionsParallels (Since: 2.12)
:   Driver specific image creation options for parallels.

    Members:
    :   - **file** ([`BlockdevRef`](qemu-qmp-ref.md#alternate-QMP-block-core.BlockdevRef "QMP:block-core.BlockdevRef")) – Node to create the image format on
        - **size** (`int`) – Size of the virtual disk in bytes
        - **cluster-size** (`int`, *optional*) – Cluster size in bytes (default: 1 MB)

*Object* BlockdevCreateOptionsQcow (Since: 2.12)
:   Driver specific image creation options for qcow.

    Members:
    :   - **file** ([`BlockdevRef`](qemu-qmp-ref.md#alternate-QMP-block-core.BlockdevRef "QMP:block-core.BlockdevRef")) – Node to create the image format on
        - **size** (`int`) – Size of the virtual disk in bytes
        - **backing-file** (`string`, *optional*) – File name of the backing file if a backing file
          should be used
        - **encrypt** ([`QCryptoBlockCreateOptions`](qemu-qmp-ref.md#object-QMP-crypto.QCryptoBlockCreateOptions "QMP:crypto.QCryptoBlockCreateOptions"), *optional*) – Encryption options if the image should be encrypted

*Enum* BlockdevQcow2Version (Since: 2.12)
:   Values:
    :   - **v2** – The original QCOW2 format as introduced in QEMU 0.10 (version
          2)
        - **v3** – The extended QCOW2 format as introduced in QEMU 1.1 (version 3)

*Enum* Qcow2CompressionType (Since: 5.1)
:   Compression type used in qcow2 image file

    Values:
    :   - **zlib** – zlib compression, see <<http://zlib.net/>>
        - **zstd** – zstd compression, see <<http://github.com/facebook/zstd>>

*Object* BlockdevCreateOptionsQcow2 (Since: 2.12)
:   Driver specific image creation options for qcow2.

    Members:
    :   - **file** ([`BlockdevRef`](qemu-qmp-ref.md#alternate-QMP-block-core.BlockdevRef "QMP:block-core.BlockdevRef")) – Node to create the image format on
        - **data-file** ([`BlockdevRef`](qemu-qmp-ref.md#alternate-QMP-block-core.BlockdevRef "QMP:block-core.BlockdevRef"), *optional*) – Node to use as an external data file in which all guest
          data is stored so that only metadata remains in the qcow2 file
          (since: 4.0)
        - **data-file-raw** (`boolean`, *optional*) – True if the external data file must stay valid as a
          standalone (read-only) raw image without looking at qcow2
          metadata (default: false; since: 4.0)
        - **extended-l2** (`boolean`, *optional*) – True to make the image have extended L2 entries
          (default: false; since 5.2)
        - **size** (`int`) – Size of the virtual disk in bytes
        - **version** ([`BlockdevQcow2Version`](qemu-qmp-ref.md#enum-QMP-block-core.BlockdevQcow2Version "QMP:block-core.BlockdevQcow2Version"), *optional*) – Compatibility level (default: v3)
        - **backing-file** (`string`, *optional*) – File name of the backing file if a backing file
          should be used
        - **backing-fmt** ([`BlockdevDriver`](qemu-qmp-ref.md#enum-QMP-block-core.BlockdevDriver "QMP:block-core.BlockdevDriver"), *optional*) – Name of the block driver to use for the backing file
        - **encrypt** ([`QCryptoBlockCreateOptions`](qemu-qmp-ref.md#object-QMP-crypto.QCryptoBlockCreateOptions "QMP:crypto.QCryptoBlockCreateOptions"), *optional*) – Encryption options if the image should be encrypted
        - **cluster-size** (`int`, *optional*) – qcow2 cluster size in bytes (default: 65536)
        - **preallocation** ([`PreallocMode`](qemu-qmp-ref.md#enum-QMP-block-core.PreallocMode "QMP:block-core.PreallocMode"), *optional*) – Preallocation mode for the new image (default: off;
          allowed values: off, falloc, full, metadata)
        - **lazy-refcounts** (`boolean`, *optional*) – True if refcounts may be updated lazily
          (default: off)
        - **refcount-bits** (`int`, *optional*) – Width of reference counts in bits (default: 16)
        - **compression-type** ([`Qcow2CompressionType`](qemu-qmp-ref.md#enum-QMP-block-core.Qcow2CompressionType "QMP:block-core.Qcow2CompressionType"), *optional*) – The image cluster compression method
          (default: zlib, since 5.1)

*Object* BlockdevCreateOptionsQed (Since: 2.12)
:   Driver specific image creation options for qed.

    Members:
    :   - **file** ([`BlockdevRef`](qemu-qmp-ref.md#alternate-QMP-block-core.BlockdevRef "QMP:block-core.BlockdevRef")) – Node to create the image format on
        - **size** (`int`) – Size of the virtual disk in bytes
        - **backing-file** (`string`, *optional*) – File name of the backing file if a backing file
          should be used
        - **backing-fmt** ([`BlockdevDriver`](qemu-qmp-ref.md#enum-QMP-block-core.BlockdevDriver "QMP:block-core.BlockdevDriver"), *optional*) – Name of the block driver to use for the backing file
        - **cluster-size** (`int`, *optional*) – Cluster size in bytes (default: 65536)
        - **table-size** (`int`, *optional*) – L1/L2 table size (in clusters)

*Object* BlockdevCreateOptionsRbd (Since: 2.12)
:   Driver specific image creation options for rbd/Ceph.

    Members:
    :   - **location** ([`BlockdevOptionsRbd`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsRbd "QMP:block-core.BlockdevOptionsRbd")) – Where to store the new image file. This location cannot
          point to a snapshot.
        - **size** (`int`) – Size of the virtual disk in bytes
        - **cluster-size** (`int`, *optional*) – RBD object size
        - **encrypt** ([`RbdEncryptionCreateOptions`](qemu-qmp-ref.md#object-QMP-block-core.RbdEncryptionCreateOptions "QMP:block-core.RbdEncryptionCreateOptions"), *optional*) – Image encryption options. (Since 6.1)

*Enum* BlockdevVmdkSubformat (Since: 4.0)
:   Subformat options for VMDK images

    Values:
    :   - **monolithicSparse** – Single file image with sparse cluster allocation
        - **monolithicFlat** – Single flat data image and a descriptor file
        - **twoGbMaxExtentSparse** – Data is split into 2GB (per virtual LBA)
          sparse extent files, in addition to a descriptor file
        - **twoGbMaxExtentFlat** – Data is split into 2GB (per virtual LBA) flat
          extent files, in addition to a descriptor file
        - **streamOptimized** – Single file image sparse cluster allocation,
          optimized for streaming over network.

*Enum* BlockdevVmdkAdapterType (Since: 4.0)
:   Adapter type info for VMDK images

    Values:
    :   - **ide** – Not documented
        - **buslogic** – Not documented
        - **lsilogic** – Not documented
        - **legacyESX** – Not documented

*Object* BlockdevCreateOptionsVmdk (Since: 4.0)
:   Driver specific image creation options for VMDK.

    Members:
    :   - **file** ([`BlockdevRef`](qemu-qmp-ref.md#alternate-QMP-block-core.BlockdevRef "QMP:block-core.BlockdevRef")) – Where to store the new image file. This refers to the image
          file for monolithcSparse and streamOptimized format, or the
          descriptor file for other formats.
        - **size** (`int`) – Size of the virtual disk in bytes
        - **extents** (`[`[`BlockdevRef`](qemu-qmp-ref.md#alternate-QMP-block-core.BlockdevRef "QMP:block-core.BlockdevRef")`]`, *optional*) – Where to store the data extents. Required for
          monolithcFlat, twoGbMaxExtentSparse and twoGbMaxExtentFlat
          formats. For monolithicFlat, only one entry is required; for
          twoGbMaxExtent\* formats, the number of entries required is
          calculated as extent_number = virtual_size / 2GB. Providing
          more extents than will be used is an error.
        - **subformat** ([`BlockdevVmdkSubformat`](qemu-qmp-ref.md#enum-QMP-block-core.BlockdevVmdkSubformat "QMP:block-core.BlockdevVmdkSubformat"), *optional*) – The subformat of the VMDK image. Default:
          “monolithicSparse”.
        - **backing-file** (`string`, *optional*) – The path of backing file. Default: no backing file
          is used.
        - **adapter-type** ([`BlockdevVmdkAdapterType`](qemu-qmp-ref.md#enum-QMP-block-core.BlockdevVmdkAdapterType "QMP:block-core.BlockdevVmdkAdapterType"), *optional*) – The adapter type used to fill in the descriptor.
          Default: ide.
        - **hwversion** (`string`, *optional*) – Hardware version. The meaningful options are “4” or
          “6”. Default: “4”.
        - **toolsversion** (`string`, *optional*) – VMware guest tools version. Default: “2147483647”
          (Since 6.2)
        - **zeroed-grain** (`boolean`, *optional*) – Whether to enable zeroed-grain feature for sparse
          subformats. Default: false.

*Object* BlockdevCreateOptionsSsh (Since: 2.12)
:   Driver specific image creation options for SSH.

    Members:
    :   - **location** ([`BlockdevOptionsSsh`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevOptionsSsh "QMP:block-core.BlockdevOptionsSsh")) – Where to store the new image file
        - **size** (`int`) – Size of the virtual disk in bytes

*Object* BlockdevCreateOptionsVdi (Since: 2.12)
:   Driver specific image creation options for VDI.

    Members:
    :   - **file** ([`BlockdevRef`](qemu-qmp-ref.md#alternate-QMP-block-core.BlockdevRef "QMP:block-core.BlockdevRef")) – Node to create the image format on
        - **size** (`int`) – Size of the virtual disk in bytes
        - **preallocation** ([`PreallocMode`](qemu-qmp-ref.md#enum-QMP-block-core.PreallocMode "QMP:block-core.PreallocMode"), *optional*) – Preallocation mode for the new image (default: off;
          allowed values: off, metadata)

*Enum* BlockdevVhdxSubformat (Since: 2.12)
:   Values:
    :   - **dynamic** – Growing image file
        - **fixed** – Preallocated fixed-size image file

*Object* BlockdevCreateOptionsVhdx (Since: 2.12)
:   Driver specific image creation options for vhdx.

    Members:
    :   - **file** ([`BlockdevRef`](qemu-qmp-ref.md#alternate-QMP-block-core.BlockdevRef "QMP:block-core.BlockdevRef")) – Node to create the image format on
        - **size** (`int`) – Size of the virtual disk in bytes
        - **log-size** (`int`, *optional*) – Log size in bytes, must be a multiple of 1 MB (default: 1
          MB)
        - **block-size** (`int`, *optional*) – Block size in bytes, must be a multiple of 1 MB and not
          larger than 256 MB (default: automatically choose a block size
          depending on the image size)
        - **subformat** ([`BlockdevVhdxSubformat`](qemu-qmp-ref.md#enum-QMP-block-core.BlockdevVhdxSubformat "QMP:block-core.BlockdevVhdxSubformat"), *optional*) – vhdx subformat (default: dynamic)
        - **block-state-zero** (`boolean`, *optional*) – Force use of payload blocks of type ‘ZERO’.
          Non-standard, but default. Do not set to ‘off’ when using
          ‘qemu-img convert’ with subformat=dynamic.

*Enum* BlockdevVpcSubformat (Since: 2.12)
:   Values:
    :   - **dynamic** – Growing image file
        - **fixed** – Preallocated fixed-size image file

*Object* BlockdevCreateOptionsVpc (Since: 2.12)
:   Driver specific image creation options for vpc (VHD).

    Members:
    :   - **file** ([`BlockdevRef`](qemu-qmp-ref.md#alternate-QMP-block-core.BlockdevRef "QMP:block-core.BlockdevRef")) – Node to create the image format on
        - **size** (`int`) – Size of the virtual disk in bytes
        - **subformat** ([`BlockdevVpcSubformat`](qemu-qmp-ref.md#enum-QMP-block-core.BlockdevVpcSubformat "QMP:block-core.BlockdevVpcSubformat"), *optional*) – vhdx subformat (default: dynamic)
        - **force-size** (`boolean`, *optional*) – Force use of the exact byte size instead of rounding to
          the next size that can be represented in CHS geometry
          (default: false)

*Object* BlockdevCreateOptions (Since: 2.12)
:   Options for creating an image format on a given node.

    Members:
    :   - **driver** ([`BlockdevDriver`](qemu-qmp-ref.md#enum-QMP-block-core.BlockdevDriver "QMP:block-core.BlockdevDriver")) – block driver to create the image format
        - When `driver` is `file`: The members of [`BlockdevCreateOptionsFile`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevCreateOptionsFile "QMP:block-core.BlockdevCreateOptionsFile").
        - When `driver` is `luks`: The members of [`BlockdevCreateOptionsLUKS`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevCreateOptionsLUKS "QMP:block-core.BlockdevCreateOptionsLUKS").
        - When `driver` is `nfs`: The members of [`BlockdevCreateOptionsNfs`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevCreateOptionsNfs "QMP:block-core.BlockdevCreateOptionsNfs").
        - When `driver` is `parallels`: The members of [`BlockdevCreateOptionsParallels`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevCreateOptionsParallels "QMP:block-core.BlockdevCreateOptionsParallels").
        - When `driver` is `qcow`: The members of [`BlockdevCreateOptionsQcow`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevCreateOptionsQcow "QMP:block-core.BlockdevCreateOptionsQcow").
        - When `driver` is `qcow2`: The members of [`BlockdevCreateOptionsQcow2`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevCreateOptionsQcow2 "QMP:block-core.BlockdevCreateOptionsQcow2").
        - When `driver` is `qed`: The members of [`BlockdevCreateOptionsQed`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevCreateOptionsQed "QMP:block-core.BlockdevCreateOptionsQed").
        - When `driver` is `rbd`: The members of [`BlockdevCreateOptionsRbd`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevCreateOptionsRbd "QMP:block-core.BlockdevCreateOptionsRbd").
        - When `driver` is `ssh`: The members of [`BlockdevCreateOptionsSsh`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevCreateOptionsSsh "QMP:block-core.BlockdevCreateOptionsSsh").
        - When `driver` is `vdi`: The members of [`BlockdevCreateOptionsVdi`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevCreateOptionsVdi "QMP:block-core.BlockdevCreateOptionsVdi").
        - When `driver` is `vhdx`: The members of [`BlockdevCreateOptionsVhdx`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevCreateOptionsVhdx "QMP:block-core.BlockdevCreateOptionsVhdx").
        - When `driver` is `vmdk`: The members of [`BlockdevCreateOptionsVmdk`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevCreateOptionsVmdk "QMP:block-core.BlockdevCreateOptionsVmdk").
        - When `driver` is `vpc`: The members of [`BlockdevCreateOptionsVpc`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevCreateOptionsVpc "QMP:block-core.BlockdevCreateOptionsVpc").

*Command* blockdev-create (Since: 3.0)
:   Starts a job to create an image format on a given node. The job is
    automatically finalized, but a manual [`job-dismiss`](qemu-qmp-ref.md#command-QMP-job.job-dismiss "QMP:job.job-dismiss") is required.

    Arguments:
    :   - **job-id** (`string`) – Identifier for the newly created job.
        - **options** ([`BlockdevCreateOptions`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevCreateOptions "QMP:block-core.BlockdevCreateOptions")) – Options for the image creation.

*Object* BlockdevAmendOptionsLUKS (Since: 5.1)
:   Driver specific image amend options for LUKS.

    Members:
    :   - The members of [`QCryptoBlockAmendOptionsLUKS`](qemu-qmp-ref.md#object-QMP-crypto.QCryptoBlockAmendOptionsLUKS "QMP:crypto.QCryptoBlockAmendOptionsLUKS").

*Object* BlockdevAmendOptionsQcow2 (Since: 5.1)
:   Driver specific image amend options for qcow2. For now, only
    encryption options can be amended

    Members:
    :   - **encrypt** ([`QCryptoBlockAmendOptions`](qemu-qmp-ref.md#object-QMP-crypto.QCryptoBlockAmendOptions "QMP:crypto.QCryptoBlockAmendOptions"), *optional*) – Encryption options to be amended

*Object* BlockdevAmendOptions (Since: 5.1)
:   Options for amending an image format

    Members:
    :   - **driver** ([`BlockdevDriver`](qemu-qmp-ref.md#enum-QMP-block-core.BlockdevDriver "QMP:block-core.BlockdevDriver")) – Block driver of the node to amend.
        - When `driver` is `luks`: The members of [`BlockdevAmendOptionsLUKS`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevAmendOptionsLUKS "QMP:block-core.BlockdevAmendOptionsLUKS").
        - When `driver` is `qcow2`: The members of [`BlockdevAmendOptionsQcow2`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevAmendOptionsQcow2 "QMP:block-core.BlockdevAmendOptionsQcow2").

*Command* x-blockdev-amend (Since: 5.1)
:   This command is unstable/experimental.

    Starts a job to amend format specific options of an existing open
    block device. The job is automatically finalized, but a manual
    [`job-dismiss`](qemu-qmp-ref.md#command-QMP-job.job-dismiss "QMP:job.job-dismiss") is required.

    Arguments:
    :   - **job-id** (`string`) – Identifier for the newly created job.
        - **node-name** (`string`) – Name of the block node to work on
        - **options** ([`BlockdevAmendOptions`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevAmendOptions "QMP:block-core.BlockdevAmendOptions")) – Options (driver specific)
        - **force** (`boolean`, *optional*) – Allow unsafe operations, format specific. For luks that
          allows erase of the last active keyslot (permanent loss of
          data), and replacement of an active keyslot (possible loss of
          data if IO error happens)

    Features:
    :   - **unstable** – This command is experimental.

*Enum* BlockErrorAction (Since: 2.1)
:   An enumeration of action that has been taken when a DISK I/O occurs

    Values:
    :   - **ignore** – error has been ignored
        - **report** – error has been reported to the device
        - **stop** – error caused VM to be stopped

*Event* BLOCK_IMAGE_CORRUPTED (Since: 1.7)
:   Emitted when a disk image is being marked corrupt. The image can be
    identified by its device or node name. The ‘device’ field is always
    present for compatibility reasons, but it can be empty (“”) if the
    image does not have a device name associated.

    Members:
    :   - **device** (`string`) – device name. This is always present for compatibility
          reasons, but it can be empty (“”) if the image does not have a
          device name associated.
        - **node-name** (`string`, *optional*) – node name (Since: 2.4)
        - **msg** (`string`) – informative message for human consumption, such as the kind of
          corruption being detected. It should not be parsed by machine
          as it is not guaranteed to be stable
        - **offset** (`int`, *optional*) – if the corruption resulted from an image access, this is
          the host’s access offset into the image
        - **size** (`int`, *optional*) – if the corruption resulted from an image access, this is the
          access size
        - **fatal** (`boolean`) – if set, the image is marked corrupt and therefore unusable
          after this event and must be repaired (Since 2.2; before, every
          [`BLOCK_IMAGE_CORRUPTED`](qemu-qmp-ref.md#event-QMP-block-core.BLOCK_IMAGE_CORRUPTED "QMP:block-core.BLOCK_IMAGE_CORRUPTED") event was fatal)

    > **Note:**
    >
    > If action is “stop”, a [`STOP`](qemu-qmp-ref.md#event-QMP-run-state.STOP "QMP:run-state.STOP") event will eventually follow
    > the [`BLOCK_IO_ERROR`](qemu-qmp-ref.md#event-QMP-block-core.BLOCK_IO_ERROR "QMP:block-core.BLOCK_IO_ERROR") event.

    > **Example::**
    >
    > ```QMP
    > <- { "event": "BLOCK_IMAGE_CORRUPTED",
    >      "data": { "device": "", "node-name": "drive", "fatal": false,
    >                "msg": "L2 table offset 0x2a2a2a00 unaligned (L1 index: 0)" },
    >      "timestamp": { "seconds": 1648243240, "microseconds": 906060 } }
    > ```

*Event* BLOCK_IO_ERROR (Since: 0.13)
:   Emitted when a disk I/O error occurs

    Members:
    :   - **qom-path** (`string`) – path to the device object in the QOM tree (since 9.2)
        - **device** (`string`) – device name. This is always present for compatibility
          reasons, but it can be empty (“”) if the image does not have a
          device name associated.
        - **node-name** (`string`, *optional*) – node name. Note that errors may be reported for the
          root node that is directly attached to a guest device rather
          than for the node where the error occurred. The node name is
          not present if the drive is empty. (Since: 2.8)
        - **operation** ([`IoOperationType`](qemu-qmp-ref.md#enum-QMP-common.IoOperationType "QMP:common.IoOperationType")) – I/O operation
        - **action** ([`BlockErrorAction`](qemu-qmp-ref.md#enum-QMP-block-core.BlockErrorAction "QMP:block-core.BlockErrorAction")) – action that has been taken
        - **nospace** (`boolean`, *optional*) – true if I/O error was caused due to a no-space condition.
          This key is only present if query-block’s io-status is present,
          please see [`query-block`](qemu-qmp-ref.md#command-QMP-block-core.query-block "QMP:block-core.query-block") documentation for more information
          (since: 2.2)
        - **reason** (`string`) – human readable string describing the error cause. (This
          field is a debugging aid for humans, it should not be parsed by
          applications) (since: 2.2)

    > **Note:**
    >
    > If action is “stop”, a [`STOP`](qemu-qmp-ref.md#event-QMP-run-state.STOP "QMP:run-state.STOP") event will eventually follow
    > the [`BLOCK_IO_ERROR`](qemu-qmp-ref.md#event-QMP-block-core.BLOCK_IO_ERROR "QMP:block-core.BLOCK_IO_ERROR") event.

    > **Note:**
    >
    > This event is rate-limited, except if action is “stop”.

    > **Example::**
    >
    > ```QMP
    > <- { "event": "BLOCK_IO_ERROR",
    >      "data": { "qom-path": "/machine/unattached/device[0]",
    >                "device": "ide0-hd1",
    >                "node-name": "#block212",
    >                "operation": "write",
    >                "action": "stop",
    >                "reason": "No space left on device" },
    >      "timestamp": { "seconds": 1265044230, "microseconds": 450486 } }
    > ```

*Event* BLOCK_JOB_COMPLETED (Since: 1.1)
:   Emitted when a block job has completed

    Members:
    :   - **type** ([`JobType`](qemu-qmp-ref.md#enum-QMP-job.JobType "QMP:job.JobType")) – job type
        - **device** (`string`) – The job identifier. Originally the device name but other
          values are allowed since QEMU 2.7
        - **len** (`int`) – maximum progress value
        - **offset** (`int`) – current progress value. On success this is equal to len.
          On failure this is less than len
        - **speed** (`int`) – rate limit, bytes per second
        - **error** (`string`, *optional*) – error message. Only present on failure. This field
          contains a human-readable error message. There are no semantics
          other than that streaming has failed and clients should not try
          to interpret the error string

    > **Example::**
    >
    > ```QMP
    > <- { "event": "BLOCK_JOB_COMPLETED",
    >      "data": { "type": "stream", "device": "virtio-disk0",
    >                "len": 10737418240, "offset": 10737418240,
    >                "speed": 0 },
    >      "timestamp": { "seconds": 1267061043, "microseconds": 959568 } }
    > ```

*Event* BLOCK_JOB_CANCELLED (Since: 1.1)
:   Emitted when a block job has been cancelled

    Members:
    :   - **type** ([`JobType`](qemu-qmp-ref.md#enum-QMP-job.JobType "QMP:job.JobType")) – job type
        - **device** (`string`) – The job identifier. Originally the device name but other
          values are allowed since QEMU 2.7
        - **len** (`int`) – maximum progress value
        - **offset** (`int`) – current progress value. On success this is equal to len.
          On failure this is less than len
        - **speed** (`int`) – rate limit, bytes per second

    > **Example::**
    >
    > ```QMP
    > <- { "event": "BLOCK_JOB_CANCELLED",
    >      "data": { "type": "stream", "device": "virtio-disk0",
    >                "len": 10737418240, "offset": 134217728,
    >                "speed": 0 },
    >      "timestamp": { "seconds": 1267061043, "microseconds": 959568 } }
    > ```

*Event* BLOCK_JOB_ERROR (Since: 1.3)
:   Emitted when a block job encounters an error

    Members:
    :   - **device** (`string`) – The job identifier. Originally the device name but other
          values are allowed since QEMU 2.7
        - **operation** ([`IoOperationType`](qemu-qmp-ref.md#enum-QMP-common.IoOperationType "QMP:common.IoOperationType")) – I/O operation
        - **action** ([`BlockErrorAction`](qemu-qmp-ref.md#enum-QMP-block-core.BlockErrorAction "QMP:block-core.BlockErrorAction")) – action that has been taken

    > **Example::**
    >
    > ```QMP
    > <- { "event": "BLOCK_JOB_ERROR",
    >      "data": { "device": "ide0-hd1",
    >                "operation": "write",
    >                "action": "stop" },
    >      "timestamp": { "seconds": 1265044230, "microseconds": 450486 } }
    > ```

*Event* BLOCK_JOB_READY (Since: 1.3)
:   Emitted when a block job is ready to complete

    Members:
    :   - **type** ([`JobType`](qemu-qmp-ref.md#enum-QMP-job.JobType "QMP:job.JobType")) – job type
        - **device** (`string`) – The job identifier. Originally the device name but other
          values are allowed since QEMU 2.7
        - **len** (`int`) – maximum progress value
        - **offset** (`int`) – current progress value. On success this is equal to len.
          On failure this is less than len
        - **speed** (`int`) – rate limit, bytes per second

    > **Note:**
    >
    > The “ready to complete” status is always reset by a
    > [`BLOCK_JOB_ERROR`](qemu-qmp-ref.md#event-QMP-block-core.BLOCK_JOB_ERROR "QMP:block-core.BLOCK_JOB_ERROR") event.

    > **Example::**
    >
    > ```QMP
    > <- { "event": "BLOCK_JOB_READY",
    >      "data": { "device": "drive0", "type": "mirror", "speed": 0,
    >                "len": 2097152, "offset": 2097152 },
    >      "timestamp": { "seconds": 1265044230, "microseconds": 450486 } }
    > ```

*Event* BLOCK_JOB_PENDING (Since: 2.12)
:   Emitted when a block job is awaiting explicit authorization to
    finalize graph changes via [`job-finalize`](qemu-qmp-ref.md#command-QMP-job.job-finalize "QMP:job.job-finalize"). If this job is part of a
    transaction, it will not emit this event until the transaction has
    converged first.

    Members:
    :   - **type** ([`JobType`](qemu-qmp-ref.md#enum-QMP-job.JobType "QMP:job.JobType")) – job type
        - **id** (`string`) – The job identifier.

    > **Example::**
    >
    > ```QMP
    > <- { "event": "BLOCK_JOB_PENDING",
    >      "data": { "type": "mirror", "id": "backup_1" },
    >      "timestamp": { "seconds": 1265044230, "microseconds": 450486 } }
    > ```

*Enum* PreallocMode (Since: 2.2)
:   Preallocation mode of QEMU image file

    Values:
    :   - **off** – no preallocation
        - **metadata** – preallocate only for metadata
        - **falloc** – like `full` preallocation but allocate disk space by
          posix_fallocate() rather than writing data.
        - **full** – preallocate all data by writing it to the device to ensure
          disk space is really available. This data may or may not be
          zero, depending on the image format and storage. `full`
          preallocation also sets up metadata correctly.

*Event* BLOCK_WRITE_THRESHOLD (Since: 2.3)
:   Emitted when writes on block device reaches or exceeds the
    configured write threshold. For thin-provisioned devices, this
    means the device should be extended to avoid pausing for disk
    exhaustion. The event is one shot. Once triggered, it needs to be
    re-registered with another [`block-set-write-threshold`](qemu-qmp-ref.md#command-QMP-block-core.block-set-write-threshold "QMP:block-core.block-set-write-threshold") command.

    Members:
    :   - **node-name** (`string`) – graph node name on which the threshold was exceeded.
        - **amount-exceeded** (`int`) – amount of data which exceeded the threshold, in
          bytes.
        - **write-threshold** (`int`) – last configured threshold, in bytes.

*Command* block-set-write-threshold (Since: 2.3)
:   Change the write threshold for a block drive. An event will be
    delivered if a write to this block drive crosses the configured
    threshold. The threshold is an offset, thus must be non-negative.
    Default is no write threshold. Setting the threshold to zero
    disables it.

    This is useful to transparently resize thin-provisioned drives
    without the guest OS noticing.

    Arguments:
    :   - **node-name** (`string`) – graph node name on which the threshold must be set.
        - **write-threshold** (`int`) – configured threshold for the block device, bytes.
          Use 0 to disable the threshold.

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "block-set-write-threshold",
    >      "arguments": { "node-name": "mydev",
    >                     "write-threshold": 17179869184 } }
    > <- { "return": {} }
    > ```

*Command* x-blockdev-change (Since: 2.7)
:   This command is unstable/experimental.

    Dynamically reconfigure the block driver state graph.

    Currently only supports adding and deleting quorum children. A
    child will be added at the end of the list of children. Its
    contents *must* be consistent with the other childrens’ contents.
    Deleting a child that is not last in the list of children is
    problematic, because it “renumbers” the children following it.

    Arguments:
    :   - **parent** (`string`) – the id or name of the parent node.
        - **child** (`string`, *optional*) – the name of a child to be deleted. Mutually exclusive with
          `node`.
        - **node** (`string`, *optional*) – the name of the node to be added. Mutually exclusive with
          `child`.

    Features:
    :   - **unstable** – This command is experimental.

    > **Example: Add a new node to a quorum:**
    >
    > ```QMP
    >  -> { "execute": "blockdev-add",
    >       "arguments": {
    >           "driver": "raw",
    >           "node-name": "new_node",
    >           "file": { "driver": "file",
    >                     "filename": "test.raw" } } }
    >  <- { "return": {} }
    >  -> { "execute": "x-blockdev-change",
    >       "arguments": { "parent": "disk1",
    >                      "node": "new_node" } }
    >  <- { "return": {} }
    > ```

    > **Example: Delete a quorum’s node:**
    >
    > ```QMP
    >  -> { "execute": "x-blockdev-change",
    >       "arguments": { "parent": "disk1",
    >                      "child": "children.1" } }
    >  <- { "return": {} }
    > ```

*Command* x-blockdev-set-iothread (Since: 2.12)
:   This command is unstable/experimental.

    Move `node` and its children into the `iothread`. If `iothread` is
    null then move `node` and its children into the main loop.

    The node must not be attached to a BlockBackend.

    Arguments:
    :   - **node-name** (`string`) – the name of the block driver node
        - **iothread** ([`StrOrNull`](qemu-qmp-ref.md#alternate-QMP-common.StrOrNull "QMP:common.StrOrNull")) – the name of the IOThread object or null for the main loop
        - **force** (`boolean`, *optional*) – true if the node and its children should be moved when a
          BlockBackend is already attached

    Features:
    :   - **unstable** – This command is experimental and intended for test cases
          that need control over IOThreads only.

    > **Example: Move a node into an IOThread:**
    >
    > ```QMP
    >  -> { "execute": "x-blockdev-set-iothread",
    >       "arguments": { "node-name": "disk1",
    >                      "iothread": "iothread0" } }
    >  <- { "return": {} }
    > ```

    > **Example: Move a node into the main loop:**
    >
    > ```QMP
    >  -> { "execute": "x-blockdev-set-iothread",
    >       "arguments": { "node-name": "disk1",
    >                      "iothread": null } }
    >  <- { "return": {} }
    > ```

*Enum* QuorumOpType (Since: 2.6)
:   An enumeration of the quorum operation types

    Values:
    :   - **read** – read operation
        - **write** – write operation
        - **flush** – flush operation

*Event* QUORUM_FAILURE (Since: 2.0)
:   Emitted by the Quorum block driver if it fails to establish a quorum

    Members:
    :   - **reference** (`string`) – device name if defined else node name
        - **sector-num** (`int`) – number of the first sector of the failed read operation
        - **sectors-count** (`int`) – failed read operation sector count

    > **Note:**
    >
    > This event is rate-limited.

    > **Example::**
    >
    > ```QMP
    > <- { "event": "QUORUM_FAILURE",
    >      "data": { "reference": "usr1", "sector-num": 345435, "sectors-count": 5 },
    >      "timestamp": { "seconds": 1344522075, "microseconds": 745528 } }
    > ```

*Event* QUORUM_REPORT_BAD (Since: 2.0)
:   Emitted to report a corruption of a Quorum file

    Members:
    :   - **type** ([`QuorumOpType`](qemu-qmp-ref.md#enum-QMP-block-core.QuorumOpType "QMP:block-core.QuorumOpType")) – quorum operation type (Since 2.6)
        - **error** (`string`, *optional*) – error message. Only present on failure. This field
          contains a human-readable error message. There are no semantics
          other than that the block layer reported an error and clients
          should not try to interpret the error string.
        - **node-name** (`string`) – the graph node name of the block driver state
        - **sector-num** (`int`) – number of the first sector of the failed read operation
        - **sectors-count** (`int`) – failed read operation sector count

    > **Note:**
    >
    > This event is rate-limited.

    > **Example: Read operation:**
    >
    > ```QMP
    >  <- { "event": "QUORUM_REPORT_BAD",
    >       "data": { "node-name": "node0", "sector-num": 345435, "sectors-count": 5,
    >                 "type": "read" },
    >       "timestamp": { "seconds": 1344522075, "microseconds": 745528 } }
    > ```

    > **Example: Flush operation:**
    >
    > ```QMP
    >  <- { "event": "QUORUM_REPORT_BAD",
    >       "data": { "node-name": "node0", "sector-num": 0, "sectors-count": 2097120,
    >                 "type": "flush", "error": "Broken pipe" },
    >       "timestamp": { "seconds": 1456406829, "microseconds": 291763 } }
    > ```

*Object* BlockdevSnapshotInternal (Since: 1.7)
:   Members:
    :   - **device** (`string`) – the device name or node-name of a root node to generate the
          snapshot from
        - **name** (`string`) – the name of the internal snapshot to be created

*Command* blockdev-snapshot-internal-sync (Since: 1.7)
:   Synchronously take an internal snapshot of a block device, when the
    format of the image used supports it. If the name is an empty
    string, or a snapshot with name already exists, the operation will
    fail.

    Arguments:
    :   - The members of [`BlockdevSnapshotInternal`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevSnapshotInternal "QMP:block-core.BlockdevSnapshotInternal").

    Errors:
    :   - If `device` is not a valid block device, GenericError
        - If any snapshot matching `name` exists, or `name` is empty,
          GenericError
        - If the format of the image used does not support it,
          GenericError

    > **Note:**
    >
    > Only some image formats such as qcow2 and rbd support
    > internal snapshots.

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "blockdev-snapshot-internal-sync",
    >      "arguments": { "device": "ide-hd0",
    >                     "name": "snapshot0" }
    >    }
    > <- { "return": {} }
    > ```

*Command* blockdev-snapshot-delete-internal-sync (Since: 1.7)
:   Synchronously delete an internal snapshot of a block device, when
    the format of the image used support it. The snapshot is identified
    by name or id or both. One of the name or id is required. Return
    [`SnapshotInfo`](qemu-qmp-ref.md#object-QMP-block-core.SnapshotInfo "QMP:block-core.SnapshotInfo") for the successfully deleted snapshot.

    Arguments:
    :   - **device** (`string`) – the device name or node-name of a root node to delete the
          snapshot from
        - **id** (`string`, *optional*) – optional the snapshot’s ID to be deleted
        - **name** (`string`, *optional*) – optional the snapshot’s name to be deleted

    Return:
    :   [`SnapshotInfo`](qemu-qmp-ref.md#object-QMP-block-core.SnapshotInfo "QMP:block-core.SnapshotInfo")

    Errors:
    :   - If `device` is not a valid block device, GenericError
        - If snapshot not found, GenericError
        - If the format of the image used does not support it,
          GenericError
        - If `id` and `name` are both not specified, GenericError

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "blockdev-snapshot-delete-internal-sync",
    >      "arguments": { "device": "ide-hd0",
    >                     "name": "snapshot0" }
    >    }
    > <- { "return": {
    >                    "id": "1",
    >                    "name": "snapshot0",
    >                    "vm-state-size": 0,
    >                    "date-sec": 1000012,
    >                    "date-nsec": 10,
    >                    "vm-clock-sec": 100,
    >                    "vm-clock-nsec": 20,
    >                    "icount": 220414
    >      }
    >    }
    > ```

*Object* DummyBlockCoreForceArrays (Since: 8.0)
:   Not used by QMP; hack to let us use BlockGraphInfoList internally

    Members:
    :   - **unused-block-graph-info** (`[`[`BlockGraphInfo`](qemu-qmp-ref.md#object-QMP-block-core.BlockGraphInfo "QMP:block-core.BlockGraphInfo")`]`) – Not documented

### [Additional block stuff (VM related)](qemu-qmp-ref.md#id12)

*Enum* BiosAtaTranslation (Since: 2.0)
:   Policy that BIOS should use to interpret cylinder/head/sector
    addresses. Note that Bochs BIOS and SeaBIOS will not actually
    translate logical CHS to physical; instead, they will use logical
    block addressing.

    Values:
    :   - **auto** – If cylinder/heads/sizes are passed, choose between none and
          LBA depending on the size of the disk. If they are not passed,
          choose none if QEMU can guess that the disk had 16 or fewer
          heads, large if QEMU can guess that the disk had 131072 or fewer
          tracks across all heads (i.e. cylinders\*heads<131072), otherwise
          LBA.
        - **none** – The physical disk geometry is equal to the logical geometry.
        - **lba** – Assume 63 sectors per track and one of 16, 32, 64, 128 or 255
          heads (if fewer than 255 are enough to cover the whole disk with
          1024 cylinders/head). The number of cylinders/head is then
          computed based on the number of sectors and heads.
        - **large** – The number of cylinders per head is scaled down to 1024 by
          correspondingly scaling up the number of heads.
        - **rechs** – Same as `large`, but first convert a 16-head geometry to
          15-head, by proportionally scaling up the number of
          cylinders/head.

*Enum* FloppyDriveType (Since: 2.6)
:   Type of floppy drive to be emulated by the Floppy Disk Controller.

    Values:
    :   - **144** – 1.44MB 3.5” drive
        - **288** – 2.88MB 3.5” drive
        - **120** – 1.2MB 5.25” drive
        - **none** – No drive connected
        - **auto** – Automatically determined by inserted media at boot

*Object* PRManagerInfo (Since: 3.0)
:   Information about a persistent reservation manager

    Members:
    :   - **id** (`string`) – the identifier of the persistent reservation manager
        - **connected** (`boolean`) – true if the persistent reservation manager is connected
          to the underlying storage or helper

*Command* query-pr-managers (Since: 3.0)
:   Return a list of information about each persistent reservation
    manager.

    Return:
    :   `[`[`PRManagerInfo`](qemu-qmp-ref.md#object-QMP-block-core.PRManagerInfo "QMP:block-core.PRManagerInfo")`]` – a list of manager info for each persistent reservation
        manager

*Command* eject (Since: 0.14)
:   Ejects the medium from a removable drive.

    Arguments:
    :   - **device** (`string`, *optional*) – Block device name
        - **id** (`string`, *optional*) – The name or QOM path of the guest device (since: 2.8)
        - **force** (`boolean`, *optional*) – If true, eject regardless of whether the drive is locked.
          If not specified, the default value is false.

    Features:
    :   - **deprecated** – Member `device` is deprecated. Use `id` instead.

    Errors:
    :   - If `device` is not a valid block device, DeviceNotFound

    > **Note:**
    >
    > Ejecting a device with no media results in success.

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "eject", "arguments": { "id": "ide1-0-1" } }
    > <- { "return": {} }
    > ```

*Command* blockdev-open-tray (Since: 2.5)
:   Opens a block device’s tray. If there is a block driver state tree
    inserted as a medium, it will become inaccessible to the guest (but
    it will remain associated to the block device, so closing the tray
    will make it accessible again).

    If the tray was already open before, this will be a no-op.

    Once the tray opens, a [`DEVICE_TRAY_MOVED`](qemu-qmp-ref.md#event-QMP-block-core.DEVICE_TRAY_MOVED "QMP:block-core.DEVICE_TRAY_MOVED") event is emitted. There
    are cases in which no such event will be generated, these include:

    - if the guest has locked the tray, `force` is false and the guest
      does not respond to the eject request
    - if the BlockBackend denoted by `device` does not have a guest
      device attached to it
    - if the guest device does not have an actual tray

    Arguments:
    :   - **device** (`string`, *optional*) – Block device name
        - **id** (`string`, *optional*) – The name or QOM path of the guest device (since: 2.8)
        - **force** (`boolean`, *optional*) – if false (the default), an eject request will be sent to the
          guest if it has locked the tray (and the tray will not be opened
          immediately); if true, the tray will be opened regardless of
          whether it is locked

    Features:
    :   - **deprecated** – Member `device` is deprecated. Use `id` instead.

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "blockdev-open-tray",
    >      "arguments": { "id": "ide0-1-0" } }
    >
    > <- { "timestamp": { "seconds": 1418751016,
    >                     "microseconds": 716996 },
    >      "event": "DEVICE_TRAY_MOVED",
    >      "data": { "device": "ide1-cd0",
    >                "id": "ide0-1-0",
    >                "tray-open": true } }
    >
    > <- { "return": {} }
    > ```

*Command* blockdev-close-tray (Since: 2.5)
:   Closes a block device’s tray. If there is a block driver state tree
    associated with the block device (which is currently ejected), that
    tree will be loaded as the medium.

    If the tray was already closed before, this will be a no-op.

    Arguments:
    :   - **device** (`string`, *optional*) – Block device name
        - **id** (`string`, *optional*) – The name or QOM path of the guest device (since: 2.8)

    Features:
    :   - **deprecated** – Member `device` is deprecated. Use `id` instead.

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "blockdev-close-tray",
    >      "arguments": { "id": "ide0-1-0" } }
    >
    > <- { "timestamp": { "seconds": 1418751345,
    >                     "microseconds": 272147 },
    >      "event": "DEVICE_TRAY_MOVED",
    >      "data": { "device": "ide1-cd0",
    >                "id": "ide0-1-0",
    >                "tray-open": false } }
    >
    > <- { "return": {} }
    > ```

*Command* blockdev-remove-medium (Since: 2.12)
:   Removes a medium (a block driver state tree) from a block device.
    That block device’s tray must currently be open (unless there is no
    attached guest device).

    If the tray is open and there is no medium inserted, this will be a
    no-op.

    Arguments:
    :   - **id** (`string`) – The name or QOM path of the guest device

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "blockdev-remove-medium",
    >      "arguments": { "id": "ide0-1-0" } }
    >
    > <- { "error": { "class": "GenericError",
    >                 "desc": "Tray of device 'ide0-1-0' is not open" } }
    >
    > -> { "execute": "blockdev-open-tray",
    >      "arguments": { "id": "ide0-1-0" } }
    >
    > <- { "timestamp": { "seconds": 1418751627,
    >                     "microseconds": 549958 },
    >      "event": "DEVICE_TRAY_MOVED",
    >      "data": { "device": "ide1-cd0",
    >                "id": "ide0-1-0",
    >                "tray-open": true } }
    >
    > <- { "return": {} }
    >
    > -> { "execute": "blockdev-remove-medium",
    >      "arguments": { "id": "ide0-1-0" } }
    >
    > <- { "return": {} }
    > ```

*Command* blockdev-insert-medium (Since: 2.12)
:   Inserts a medium (a block driver state tree) into a block device.
    That block device’s tray must currently be open (unless there is no
    attached guest device) and there must be no medium inserted already.

    Arguments:
    :   - **id** (`string`) – The name or QOM path of the guest device
        - **node-name** (`string`) – name of a node in the block driver state graph

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "blockdev-add",
    >      "arguments": {
    >          "node-name": "node0",
    >          "driver": "raw",
    >          "file": { "driver": "file",
    >                    "filename": "fedora.iso" } } }
    > <- { "return": {} }
    >
    > -> { "execute": "blockdev-insert-medium",
    >      "arguments": { "id": "ide0-1-0",
    >                     "node-name": "node0" } }
    >
    > <- { "return": {} }
    > ```

*Enum* BlockdevChangeReadOnlyMode (Since: 2.3)
:   Specifies the new read-only mode of a block device subject to the
    [`blockdev-change-medium`](qemu-qmp-ref.md#command-QMP-block-core.blockdev-change-medium "QMP:block-core.blockdev-change-medium") command.

    Values:
    :   - **retain** – Retains the current read-only mode
        - **read-only** – Makes the device read-only
        - **read-write** – Makes the device writable

*Command* blockdev-change-medium (Since: 2.5)
:   Changes the medium inserted into a block device by ejecting the
    current medium and loading a new image file which is inserted as the
    new medium (this command combines [`blockdev-open-tray`](qemu-qmp-ref.md#command-QMP-block-core.blockdev-open-tray "QMP:block-core.blockdev-open-tray"),
    [`blockdev-remove-medium`](qemu-qmp-ref.md#command-QMP-block-core.blockdev-remove-medium "QMP:block-core.blockdev-remove-medium"), [`blockdev-insert-medium`](qemu-qmp-ref.md#command-QMP-block-core.blockdev-insert-medium "QMP:block-core.blockdev-insert-medium") and
    [`blockdev-close-tray`](qemu-qmp-ref.md#command-QMP-block-core.blockdev-close-tray "QMP:block-core.blockdev-close-tray")).

    Arguments:
    :   - **device** (`string`, *optional*) – Block device name
        - **id** (`string`, *optional*) – The name or QOM path of the guest device (since: 2.8)
        - **filename** (`string`) – filename of the new image to be loaded
        - **format** (`string`, *optional*) – format to open the new image with (defaults to the probed
          format)
        - **read-only-mode** ([`BlockdevChangeReadOnlyMode`](qemu-qmp-ref.md#enum-QMP-block-core.BlockdevChangeReadOnlyMode "QMP:block-core.BlockdevChangeReadOnlyMode"), *optional*) – change the read-only mode of the device; defaults
          to ‘retain’
        - **force** (`boolean`, *optional*) – if false (the default), an eject request through
          [`blockdev-open-tray`](qemu-qmp-ref.md#command-QMP-block-core.blockdev-open-tray "QMP:block-core.blockdev-open-tray") will be sent to the guest if it has locked
          the tray (and the tray will not be opened immediately); if true,
          the tray will be opened regardless of whether it is locked.
          (since 7.1)

    Features:
    :   - **deprecated** – Member `device` is deprecated. Use `id` instead.

    > **Example: Change a removable medium:**
    >
    > ```QMP
    >  -> { "execute": "blockdev-change-medium",
    >       "arguments": { "id": "ide0-1-0",
    >                      "filename": "/srv/images/Fedora-12-x86_64-DVD.iso",
    >                      "format": "raw" } }
    >  <- { "return": {} }
    > ```

    > **Example: Load a read-only medium into a writable drive:**
    >
    > ```QMP
    >  -> { "execute": "blockdev-change-medium",
    >       "arguments": { "id": "floppyA",
    >                      "filename": "/srv/images/ro.img",
    >                      "format": "raw",
    >                      "read-only-mode": "retain" } }
    >
    >  <- { "error":
    >       { "class": "GenericError",
    >         "desc": "Could not open '/srv/images/ro.img': Permission denied" } }
    >
    >  -> { "execute": "blockdev-change-medium",
    >       "arguments": { "id": "floppyA",
    >                      "filename": "/srv/images/ro.img",
    >                      "format": "raw",
    >                      "read-only-mode": "read-only" } }
    >
    >  <- { "return": {} }
    > ```

*Event* DEVICE_TRAY_MOVED (Since: 1.1)
:   Emitted whenever the tray of a removable device is moved by the
    guest or by HMP/QMP commands

    Members:
    :   - **device** (`string`) – Block device name. This is always present for
          compatibility reasons, but it can be empty (“”) if the image
          does not have a device name associated.
        - **id** (`string`) – The name or QOM path of the guest device (since 2.8)
        - **tray-open** (`boolean`) – true if the tray has been opened or false if it has been
          closed

    > **Example::**
    >
    > ```QMP
    > <- { "event": "DEVICE_TRAY_MOVED",
    >      "data": { "device": "ide1-cd0",
    >                "id": "/machine/unattached/device[22]",
    >                "tray-open": true
    >      },
    >      "timestamp": { "seconds": 1265044230, "microseconds": 450486 } }
    > ```

*Event* PR_MANAGER_STATUS_CHANGED (Since: 3.0)
:   Emitted whenever the connected status of a persistent reservation
    manager changes.

    Members:
    :   - **id** (`string`) – The id of the PR manager object
        - **connected** (`boolean`) – true if the PR manager is connected to a backend

    > **Example::**
    >
    > ```QMP
    > <- { "event": "PR_MANAGER_STATUS_CHANGED",
    >      "data": { "id": "pr-helper0",
    >                "connected": true
    >      },
    >      "timestamp": { "seconds": 1519840375, "microseconds": 450486 } }
    > ```

*Command* block_set_io_throttle (Since: 1.1)
:   Change I/O throttle limits for a block drive.

    Since QEMU 2.4, each device with I/O limits is member of a throttle
    group.

    If two or more devices are members of the same group, the limits
    will apply to the combined I/O of the whole group in a round-robin
    fashion. Therefore, setting new I/O limits to a device will affect
    the whole group.

    The name of the group can be specified using the ‘group’ parameter.
    If the parameter is unset, it is assumed to be the current group of
    that device. If it’s not in any group yet, the name of the device
    will be used as the name for its group.

    The ‘group’ parameter can also be used to move a device to a
    different group. In this case the limits specified in the
    parameters will be applied to the new group only.

    I/O limits can be disabled by setting all of them to 0. In this
    case the device will be removed from its group and the rest of its
    members will not be affected. The ‘group’ parameter is ignored.

    Arguments:
    :   - The members of [`BlockIOThrottle`](qemu-qmp-ref.md#object-QMP-block-core.BlockIOThrottle "QMP:block-core.BlockIOThrottle").

    Errors:
    :   - If `device` is not a valid block device, DeviceNotFound

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "block_set_io_throttle",
    >      "arguments": { "id": "virtio-blk-pci0/virtio-backend",
    >                     "bps": 0,
    >                     "bps_rd": 0,
    >                     "bps_wr": 0,
    >                     "iops": 512,
    >                     "iops_rd": 0,
    >                     "iops_wr": 0,
    >                     "bps_max": 0,
    >                     "bps_rd_max": 0,
    >                     "bps_wr_max": 0,
    >                     "iops_max": 0,
    >                     "iops_rd_max": 0,
    >                     "iops_wr_max": 0,
    >                     "bps_max_length": 0,
    >                     "iops_size": 0 } }
    > <- { "return": {} }
    > ```

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "block_set_io_throttle",
    >      "arguments": { "id": "ide0-1-0",
    >                     "bps": 1000000,
    >                     "bps_rd": 0,
    >                     "bps_wr": 0,
    >                     "iops": 0,
    >                     "iops_rd": 0,
    >                     "iops_wr": 0,
    >                     "bps_max": 8000000,
    >                     "bps_rd_max": 0,
    >                     "bps_wr_max": 0,
    >                     "iops_max": 0,
    >                     "iops_rd_max": 0,
    >                     "iops_wr_max": 0,
    >                     "bps_max_length": 60,
    >                     "iops_size": 0 } }
    > <- { "return": {} }
    > ```

*Command* block-latency-histogram-set (Since: 4.0)
:   Manage read, write and flush latency histograms for the device.

    If only `id` parameter is specified, remove all present latency
    histograms for the device. Otherwise, add/reset some of (or all)
    latency histograms.

    Arguments:
    :   - **id** (`string`) – The name or QOM path of the guest device.
        - **boundaries** (`[``int``]`, *optional*) – list of interval boundary values (see description in
          [`BlockLatencyHistogramInfo`](qemu-qmp-ref.md#object-QMP-block-core.BlockLatencyHistogramInfo "QMP:block-core.BlockLatencyHistogramInfo") definition). If specified, all
          latency histograms are removed, and empty ones created for all
          io types with intervals corresponding to `boundaries` (except for
          io types, for which specific boundaries are set through the
          following parameters).
        - **boundaries-read** (`[``int``]`, *optional*) – list of interval boundary values for read latency
          histogram. If specified, old read latency histogram is removed,
          and empty one created with intervals corresponding to
          `boundaries-read`. The parameter has higher priority then
          `boundaries`.
        - **boundaries-write** (`[``int``]`, *optional*) – list of interval boundary values for write
          latency histogram.
        - **boundaries-zap** (`[``int``]`, *optional*) – list of interval boundary values for zone append
          write latency histogram.
        - **boundaries-flush** (`[``int``]`, *optional*) – list of interval boundary values for flush
          latency histogram.

    Errors:
    :   - if device is not found or any boundary arrays are invalid.

    > **Example::**
    >
    > Set new histograms for all io types with intervals
    > [0, 10), [10, 50), [50, 100), [100, +inf):
    >
    > ```QMP
    > -> { "execute": "block-latency-histogram-set",
    >      "arguments": { "id": "drive0",
    >                     "boundaries": [10, 50, 100] } }
    > <- { "return": {} }
    > ```

    > **Example::**
    >
    > Set new histogram only for write, other histograms will remain
    > not changed (or not created):
    >
    > ```QMP
    > -> { "execute": "block-latency-histogram-set",
    >      "arguments": { "id": "drive0",
    >                     "boundaries-write": [10, 50, 100] } }
    > <- { "return": {} }
    > ```

    > **Example::**
    >
    > Set new histograms with the following intervals:
    >
    > - read, flush: [0, 10), [10, 50), [50, 100), [100, +inf)
    > - write: [0, 1000), [1000, 5000), [5000, +inf)
    >
    > ```QMP
    > -> { "execute": "block-latency-histogram-set",
    >      "arguments": { "id": "drive0",
    >                     "boundaries": [10, 50, 100],
    >                     "boundaries-write": [1000, 5000] } }
    > <- { "return": {} }
    > ```

    > **Example::**
    >
    > Remove all latency histograms:
    >
    > ```QMP
    > -> { "execute": "block-latency-histogram-set",
    >      "arguments": { "id": "drive0" } }
    > <- { "return": {} }
    > ```

### [Block device exports](qemu-qmp-ref.md#id13)

*Object* NbdServerOptionsBase
:   Members:
    :   - **handshake-max-seconds** (`int`, *optional*) – Time limit, in seconds, at which a client
          that has not completed the negotiation handshake will be
          disconnected, or 0 for no limit (since 10.0; default: 10).
        - **tls-creds** (`string`, *optional*) – ID of the TLS credentials object (since 2.6).
        - **tls-authz** (`string`, *optional*) – ID of the QAuthZ authorization object used to validate
          the client’s x509 distinguished name. This object is is only
          resolved at time of use, so can be deleted and recreated on the
          fly while the NBD server is active. If missing, it will default
          to denying access (since 4.0).
        - **max-connections** (`int`, *optional*) – The maximum number of connections to allow at the
          same time, 0 for unlimited. Setting this to 1 also stops the
          server from advertising multiple client support (since 5.2;
          default: 100).

*Object* NbdServerOptions
:   Keep this type consistent with the [`NbdServerOptionsLegacy`](qemu-qmp-ref.md#object-QMP-block-export.NbdServerOptionsLegacy "QMP:block-export.NbdServerOptionsLegacy") type.
    The only intended difference is using [`SocketAddress`](qemu-qmp-ref.md#object-QMP-sockets.SocketAddress "QMP:sockets.SocketAddress") instead of
    [`SocketAddressLegacy`](qemu-qmp-ref.md#object-QMP-sockets.SocketAddressLegacy "QMP:sockets.SocketAddressLegacy").

    Members:
    :   - **addr** ([`SocketAddress`](qemu-qmp-ref.md#object-QMP-sockets.SocketAddress "QMP:sockets.SocketAddress")) – Address on which to listen (since 4.2).
        - The members of [`NbdServerOptionsBase`](qemu-qmp-ref.md#object-QMP-block-export.NbdServerOptionsBase "QMP:block-export.NbdServerOptionsBase").

*Object* NbdServerOptionsLegacy
:   Keep this type consistent with the [`NbdServerOptions`](qemu-qmp-ref.md#object-QMP-block-export.NbdServerOptions "QMP:block-export.NbdServerOptions") type. The
    only intended difference is using [`SocketAddressLegacy`](qemu-qmp-ref.md#object-QMP-sockets.SocketAddressLegacy "QMP:sockets.SocketAddressLegacy") instead of
    [`SocketAddress`](qemu-qmp-ref.md#object-QMP-sockets.SocketAddress "QMP:sockets.SocketAddress").

    Members:
    :   - **addr** ([`SocketAddressLegacy`](qemu-qmp-ref.md#object-QMP-sockets.SocketAddressLegacy "QMP:sockets.SocketAddressLegacy")) – Address on which to listen (since 1.3).
        - The members of [`NbdServerOptionsBase`](qemu-qmp-ref.md#object-QMP-block-export.NbdServerOptionsBase "QMP:block-export.NbdServerOptionsBase").

*Command* nbd-server-start (Since: 1.3)
:   Start an NBD server listening on the given host and port. Block
    devices can then be exported using [`nbd-server-add`](qemu-qmp-ref.md#command-QMP-block-export.nbd-server-add "QMP:block-export.nbd-server-add"). The NBD server
    will present them as named exports; for example, another QEMU
    instance could refer to them as “nbd:HOST:PORT:exportname=NAME”.

    Arguments:
    :   - The members of [`NbdServerOptionsLegacy`](qemu-qmp-ref.md#object-QMP-block-export.NbdServerOptionsLegacy "QMP:block-export.NbdServerOptionsLegacy").

    Errors:
    :   - if the server is already running

*Object* BlockExportOptionsNbdBase (Since: 5.0)
:   An NBD block export (common options shared between [`nbd-server-add`](qemu-qmp-ref.md#command-QMP-block-export.nbd-server-add "QMP:block-export.nbd-server-add")
    and the NBD branch of [`block-export-add`](qemu-qmp-ref.md#command-QMP-block-export.block-export-add "QMP:block-export.block-export-add")).

    Members:
    :   - **name** (`string`, *optional*) – Export name. If unspecified, the `device` parameter is used
          as the export name. (Since 2.12)
        - **description** (`string`, *optional*) – Free-form description of the export, up to 4096 bytes.
          (Since 5.0)

*Object* BlockExportOptionsNbd (Since: 5.2)
:   An NBD block export (distinct options used in the NBD branch of
    [`block-export-add`](qemu-qmp-ref.md#command-QMP-block-export.block-export-add "QMP:block-export.block-export-add")).

    Members:
    :   - **bitmaps** (`[`[`BlockDirtyBitmapOrStr`](qemu-qmp-ref.md#alternate-QMP-block-core.BlockDirtyBitmapOrStr "QMP:block-core.BlockDirtyBitmapOrStr")`]`, *optional*) – Also export each of the named dirty bitmaps reachable from
          `device`, so the NBD client can use NBD_OPT_SET_META_CONTEXT with
          the metadata context name “qemu:dirty-bitmap:BITMAP” to inspect
          each bitmap. Since 7.1 bitmap may be specified by node/name
          pair.
        - **allocation-depth** (`boolean`, *optional*) – Also export the allocation depth map for `device`,
          so the NBD client can use NBD_OPT_SET_META_CONTEXT with the
          metadata context name “qemu:allocation-depth” to inspect
          allocation details. (since 5.2)
        - The members of [`BlockExportOptionsNbdBase`](qemu-qmp-ref.md#object-QMP-block-export.BlockExportOptionsNbdBase "QMP:block-export.BlockExportOptionsNbdBase").

*Object* BlockExportOptionsVhostUserBlk (Since: 5.2)
:   A vhost-user-blk block export.

    Members:
    :   - **addr** ([`SocketAddress`](qemu-qmp-ref.md#object-QMP-sockets.SocketAddress "QMP:sockets.SocketAddress")) – The vhost-user socket on which to listen. Both ‘unix’ and
          ‘fd’ [`SocketAddress`](qemu-qmp-ref.md#object-QMP-sockets.SocketAddress "QMP:sockets.SocketAddress") types are supported. Passed fds must be
          UNIX domain sockets.
        - **logical-block-size** (`int`, *optional*) – Logical block size in bytes. Defaults to 512
          bytes.
        - **num-queues** (`int`, *optional*) – Number of request virtqueues. Must be greater than 0.
          Defaults to 1.

*Enum* FuseExportAllowOther (Since: 6.1)
:   Possible allow_other modes for FUSE exports.

    Values:
    :   - **off** – Do not pass allow_other as a mount option.
        - **on** – Pass allow_other as a mount option.
        - **auto** – Try mounting with allow_other first, and if that fails, retry
          without allow_other.

*Object* BlockExportOptionsFuse (Since: 6.0)
:   *Availability*: `CONFIG_FUSE`

    Options for exporting a block graph node on some (file) mountpoint
    as a raw image.

    Multi-threading note: The FUSE export supports multi-threading.
    Currently, requests are distributed across these threads in a
    round-robin fashion, i.e. independently of the CPU core from which a
    request originates.

    Members:
    :   - **mountpoint** (`string`) – Path on which to export the block device via FUSE.
          This must point to an existing regular file.
        - **growable** (`boolean`, *optional*) – Whether writes beyond the EOF should grow the block node
          accordingly. (default: false)
        - **allow-other** ([`FuseExportAllowOther`](qemu-qmp-ref.md#enum-QMP-block-export.FuseExportAllowOther "QMP:block-export.FuseExportAllowOther"), *optional*) – If this is off, only QEMU’s user is allowed access to
          this export. That cannot be changed even with chmod or chown.
          Enabling this option will allow other users access to the export
          with the FUSE mount option “allow_other”. Note that using
          allow_other as a non-root user requires user_allow_other to be
          enabled in the global fuse.conf configuration file. In auto
          mode (the default), the FUSE export driver will first attempt to
          mount the export with allow_other, and if that fails, try again
          without. (since 6.1; default: auto)

*Object* BlockExportOptionsVduseBlk (Since: 7.1)
:   A vduse-blk block export.

    Members:
    :   - **name** (`string`) – the name of VDUSE device (must be unique across the host).
        - **num-queues** (`int`, *optional*) – the number of virtqueues. Defaults to 1.
        - **queue-size** (`int`, *optional*) – the size of virtqueue. Defaults to 256.
        - **logical-block-size** (`int`, *optional*) – Logical block size in bytes. Range [512,
          PAGE_SIZE] and must be power of 2. Defaults to 512 bytes.
        - **serial** (`string`, *optional*) – the serial number of virtio block device. Defaults to
          empty string.

*Object* NbdServerAddOptions (Since: 5.0)
:   An NBD block export, per legacy [`nbd-server-add`](qemu-qmp-ref.md#command-QMP-block-export.nbd-server-add "QMP:block-export.nbd-server-add") command.

    Members:
    :   - **device** (`string`) – The device name or node name of the node to be exported
        - **writable** (`boolean`, *optional*) – Whether clients should be able to write to the device via
          the NBD connection (default false).
        - **bitmap** (`string`, *optional*) – Also export a single dirty bitmap reachable from `device`,
          so the NBD client can use NBD_OPT_SET_META_CONTEXT with the
          metadata context name “qemu:dirty-bitmap:BITMAP” to inspect the
          bitmap (since 4.0).
        - The members of [`BlockExportOptionsNbdBase`](qemu-qmp-ref.md#object-QMP-block-export.BlockExportOptionsNbdBase "QMP:block-export.BlockExportOptionsNbdBase").

*Command* nbd-server-add (Since: 1.3)
:   This command is deprecated.

    Export a block node to QEMU’s embedded NBD server.

    The export name will be used as the id for the resulting block
    export.

    Arguments:
    :   - The members of [`NbdServerAddOptions`](qemu-qmp-ref.md#object-QMP-block-export.NbdServerAddOptions "QMP:block-export.NbdServerAddOptions").

    Features:
    :   - **deprecated** – This command is deprecated. Use [`block-export-add`](qemu-qmp-ref.md#command-QMP-block-export.block-export-add "QMP:block-export.block-export-add")
          instead.

    Errors:
    :   - if the server is not running
        - if an export with the same name already exists

*Enum* BlockExportRemoveMode (Since: 2.12)
:   Mode for removing a block export.

    Values:
    :   - **safe** – Remove export if there are no existing connections, fail
          otherwise.
        - **hard** – Drop all connections immediately and remove export.

*Command* nbd-server-remove (Since: 2.12)
:   This command is deprecated.

    Remove NBD export by name.

    Arguments:
    :   - **name** (`string`) – Block export id.
        - **mode** ([`BlockExportRemoveMode`](qemu-qmp-ref.md#enum-QMP-block-export.BlockExportRemoveMode "QMP:block-export.BlockExportRemoveMode"), *optional*) – Mode of command operation. See [`BlockExportRemoveMode`](qemu-qmp-ref.md#enum-QMP-block-export.BlockExportRemoveMode "QMP:block-export.BlockExportRemoveMode")
          description. Default is ‘safe’.

    Features:
    :   - **deprecated** – This command is deprecated. Use [`block-export-del`](qemu-qmp-ref.md#command-QMP-block-export.block-export-del "QMP:block-export.block-export-del")
          instead.

    Errors:
    :   - if the server is not running
        - if export is not found
        - if mode is ‘safe’ and there are existing connections

*Command* nbd-server-stop (Since: 1.3)
:   Stop QEMU’s embedded NBD server, and unregister all devices
    previously added via [`nbd-server-add`](qemu-qmp-ref.md#command-QMP-block-export.nbd-server-add "QMP:block-export.nbd-server-add").

*Enum* BlockExportType (Since: 4.2)
:   An enumeration of block export types

    Values:
    :   - **nbd** – NBD export
        - **vhost-user-blk** – vhost-user-blk export (since 5.2)
        - **fuse** – FUSE export (since: 6.0)
        - **vduse-blk** – vduse-blk export (since 7.1)

*Object* BlockExportOptions (Since: 4.2)
:   Describes a block export, i.e. how single node should be exported on
    an external interface.

    Members:
    :   - **type** ([`BlockExportType`](qemu-qmp-ref.md#enum-QMP-block-export.BlockExportType "QMP:block-export.BlockExportType")) – Block export type
        - **id** (`string`) – A unique identifier for the block export (across all export
          types)
        - **node-name** (`string`) – The node name of the block node to be exported
          (since: 5.2)
        - **writable** (`boolean`, *optional*) – True if clients should be able to write to the export
          (default false)
        - **writethrough** (`boolean`, *optional*) – If true, caches are flushed after every write request
          to the export before completion is signalled. (since: 5.2;
          default: false)
        - **iothread** ([`BlockExportIothreads`](qemu-qmp-ref.md#alternate-QMP-block-export.BlockExportIothreads "QMP:block-export.BlockExportIothreads"), *optional*) – The name(s) of one or more iothread object(s) where the
          export will run. The default is to use the thread currently
          associated with the block node. (since: 5.2; multi-threading
          since 10.1)
        - **fixed-iothread** (`boolean`, *optional*) – True prevents the block node from being moved to
          another thread while the export is active. If true and
          `iothread` is given, export creation fails if the block node
          cannot be moved to the iothread. Must not be true when giving
          multiple iothreads for `iothread`. The default is false.
          (since: 5.2)
        - **allow-inactive** (`boolean`, *optional*) – If true, the export allows the exported node to be
          inactive. If it is created for an inactive block node, the node
          remains inactive. If the export type doesn’t support running on
          an inactive node, an error is returned. If false, inactive
          block nodes are automatically activated before creating the
          export and trying to inactivate them later fails.
          (since: 10.0; default: false)
        - When `type` is `nbd`: The members of [`BlockExportOptionsNbd`](qemu-qmp-ref.md#object-QMP-block-export.BlockExportOptionsNbd "QMP:block-export.BlockExportOptionsNbd").
        - When `type` is `vhost-user-blk`: The members of [`BlockExportOptionsVhostUserBlk`](qemu-qmp-ref.md#object-QMP-block-export.BlockExportOptionsVhostUserBlk "QMP:block-export.BlockExportOptionsVhostUserBlk").
        - When `type` is `fuse`: The members of [`BlockExportOptionsFuse`](qemu-qmp-ref.md#object-QMP-block-export.BlockExportOptionsFuse "QMP:block-export.BlockExportOptionsFuse").
        - When `type` is `vduse-blk`: The members of [`BlockExportOptionsVduseBlk`](qemu-qmp-ref.md#object-QMP-block-export.BlockExportOptionsVduseBlk "QMP:block-export.BlockExportOptionsVduseBlk").

*Alternate* BlockExportIothreads (Since: 10.1)
:   Specify a single or multiple I/O threads in which to run a block
    export’s I/O.

    Alternatives:
    :   - **single** (`string`) – Run the export’s I/O in the given single I/O thread.
        - **multi** (`[``string``]`) – Use multi-threading across the given set of I/O threads,
          which must not be empty. Note: Passing a single I/O thread via
          this variant is still treated as multi-threading, which is
          different from using the `single` variant. In particular, even
          if there only is a single I/O thread in the set, export types
          that do not support multi-threading will generally reject this
          variant, and BlockExportOptions.fixed-iothread is always
          incompatible with it.

*Command* block-export-add (Since: 5.2)
:   Creates a new block export.

    Arguments:
    :   - The members of [`BlockExportOptions`](qemu-qmp-ref.md#object-QMP-block-export.BlockExportOptions "QMP:block-export.BlockExportOptions").

*Command* block-export-del (Since: 5.2)
:   Request to remove a block export. This drops the user’s reference
    to the export, but the export may still stay around after this
    command returns until the shutdown of the export has completed.

    Arguments:
    :   - **id** (`string`) – Block export id.
        - **mode** ([`BlockExportRemoveMode`](qemu-qmp-ref.md#enum-QMP-block-export.BlockExportRemoveMode "QMP:block-export.BlockExportRemoveMode"), *optional*) – Mode of command operation. See [`BlockExportRemoveMode`](qemu-qmp-ref.md#enum-QMP-block-export.BlockExportRemoveMode "QMP:block-export.BlockExportRemoveMode")
          description. Default is ‘safe’.

    Errors:
    :   - if the export is not found
        - if `mode` is ‘safe’ and the export is still in use (e.g. by
          existing client connections)

*Event* BLOCK_EXPORT_DELETED (Since: 5.2)
:   Emitted when a block export is removed and its id can be reused.

    Members:
    :   - **id** (`string`) – Block export id.

*Object* BlockExportInfo (Since: 5.2)
:   Information about a single block export.

    Members:
    :   - **id** (`string`) – The unique identifier for the block export
        - **type** ([`BlockExportType`](qemu-qmp-ref.md#enum-QMP-block-export.BlockExportType "QMP:block-export.BlockExportType")) – The block export type
        - **node-name** (`string`) – The node name of the block node that is exported
        - **shutting-down** (`boolean`) – True if the export is shutting down (e.g. after a
          [`block-export-del`](qemu-qmp-ref.md#command-QMP-block-export.block-export-del "QMP:block-export.block-export-del") command, but before the shutdown has
          completed)

*Command* query-block-exports (Since: 5.2)
:   Return:
    :   `[`[`BlockExportInfo`](qemu-qmp-ref.md#object-QMP-block-export.BlockExportInfo "QMP:block-export.BlockExportInfo")`]` – A list describing all block exports

## [Character devices](qemu-qmp-ref.md#id14)

*Object* ChardevInfo (Since: 0.14)
:   Information about a character device.

    Members:
    :   - **label** (`string`) – the label of the character device
        - **filename** (`string`) – the filename of the character device
        - **frontend-open** (`boolean`) – shows whether the frontend device attached to this
          backend (e.g. with the chardev=… option) is in open or closed
          state (since 2.1)

    > **Note:**
    >
    > `filename` is encoded using the QEMU command line character
    > device encoding. See the QEMU man page for details.

*Command* query-chardev (Since: 0.14)
:   Return information about current character devices.

    Return:
    :   `[`[`ChardevInfo`](qemu-qmp-ref.md#object-QMP-char.ChardevInfo "QMP:char.ChardevInfo")`]`

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "query-chardev" }
    > <- {
    >       "return": [
    >          {
    >             "label": "charchannel0",
    >             "filename": "unix:/var/lib/libvirt/qemu/seabios.rhel6.agent,server=on",
    >             "frontend-open": false
    >          },
    >          {
    >             "label": "charmonitor",
    >             "filename": "unix:/var/lib/libvirt/qemu/seabios.rhel6.monitor,server=on",
    >             "frontend-open": true
    >          },
    >          {
    >             "label": "charserial0",
    >             "filename": "pty:/dev/pts/2",
    >             "frontend-open": true
    >          }
    >       ]
    >    }
    > ```

*Object* ChardevBackendInfo (Since: 2.0)
:   Information about a character device backend

    Members:
    :   - **name** (`string`) – The backend name

*Command* query-chardev-backends (Since: 2.0)
:   Return information about character device backends.

    Return:
    :   `[`[`ChardevBackendInfo`](qemu-qmp-ref.md#object-QMP-char.ChardevBackendInfo "QMP:char.ChardevBackendInfo")`]`

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "query-chardev-backends" }
    > <- {
    >       "return":[
    >          {
    >             "name":"udp"
    >          },
    >          {
    >             "name":"tcp"
    >          },
    >          {
    >             "name":"unix"
    >          },
    >          {
    >             "name":"spiceport"
    >          }
    >       ]
    >    }
    > ```

*Enum* DataFormat (Since: 1.4)
:   An enumeration of data format.

    Values:
    :   - **utf8** – Data is a UTF-8 string (RFC 3629)
        - **base64** – Data is Base64 encoded binary (RFC 3548)

*Command* ringbuf-write (Since: 1.4)
:   Write to a ring buffer character device.

    Arguments:
    :   - **device** (`string`) – the ring buffer character device name
        - **data** (`string`) – data to write
        - **format** ([`DataFormat`](qemu-qmp-ref.md#enum-QMP-char.DataFormat "QMP:char.DataFormat"), *optional*) –

          data encoding (default ‘utf8’).

          - base64: data must be base64 encoded text. Its binary decoding
            gets written.
          - utf8: data’s UTF-8 encoding is written
          - data itself is always Unicode regardless of format, like any
            other string.

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "ringbuf-write",
    >      "arguments": { "device": "foo",
    >                     "data": "abcdefgh",
    >                     "format": "utf8" } }
    > <- { "return": {} }
    > ```

*Command* ringbuf-read (Since: 1.4)
:   Read from a ring buffer character device.

    Arguments:
    :   - **device** (`string`) – the ring buffer character device name
        - **size** (`int`) – how many bytes to read at most
        - **format** ([`DataFormat`](qemu-qmp-ref.md#enum-QMP-char.DataFormat "QMP:char.DataFormat"), *optional*) –

          data encoding (default ‘utf8’).

          - base64: the data read is returned in base64 encoding.
          - utf8: the data read is interpreted as UTF-8.
            Bug: can screw up when the buffer contains invalid UTF-8
            sequences, NUL characters, after the ring buffer lost data,
            and when reading stops because the size limit is reached.
          - The return value is always Unicode regardless of format, like
            any other string.

    Return:
    :   `string` – data read from the device

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "ringbuf-read",
    >      "arguments": { "device": "foo",
    >                     "size": 1000,
    >                     "format": "utf8" } }
    > <- { "return": "abcdefgh" }
    > ```

*Object* ChardevCommon (Since: 2.6)
:   Configuration shared across all chardev backends

    Members:
    :   - **logfile** (`string`, *optional*) – The name of a logfile to save output
        - **logappend** (`boolean`, *optional*) – true to append instead of truncate (default to false to
          truncate)
        - **logtimestamp** (`boolean`, *optional*) – true to insert timestamps into logfile
          (default false) (since 11.0)

*Object* ChardevFile (Since: 1.4)
:   Configuration info for file chardevs.

    Members:
    :   - **in** (`string`, *optional*) – The name of the input file
        - **out** (`string`) – The name of the output file
        - **append** (`boolean`, *optional*) – Open the file in append mode (default false to truncate)
          (Since 2.6)
        - The members of [`ChardevCommon`](qemu-qmp-ref.md#object-QMP-char.ChardevCommon "QMP:char.ChardevCommon").

*Object* ChardevHostdev (Since: 1.4)
:   Configuration info for device and pipe chardevs.

    Members:
    :   - **device** (`string`) – The name of the special file for the device, i.e.
          /dev/ttyS0 on Unix or COM1: on Windows
        - The members of [`ChardevCommon`](qemu-qmp-ref.md#object-QMP-char.ChardevCommon "QMP:char.ChardevCommon").

*Object* ChardevSocket (Since: 1.4)
:   Configuration info for (stream) socket chardevs.

    Members:
    :   - **addr** ([`SocketAddressLegacy`](qemu-qmp-ref.md#object-QMP-sockets.SocketAddressLegacy "QMP:sockets.SocketAddressLegacy")) – socket address to listen on (server=true) or connect to
          (server=false)
        - **tls-creds** (`string`, *optional*) – the ID of the TLS credentials object (since 2.6)
        - **tls-authz** (`string`, *optional*) – the ID of the QAuthZ authorization object against which
          the client’s x509 distinguished name will be validated. This
          object is only resolved at time of use, so can be deleted and
          recreated on the fly while the chardev server is active. If
          missing, it will default to denying access (since 4.0)
        - **server** (`boolean`, *optional*) – create server socket (default: true)
        - **wait** (`boolean`, *optional*) – wait for incoming connection on server sockets (default:
          false). Silently ignored with server: false. This use is
          deprecated.
        - **nodelay** (`boolean`, *optional*) – set TCP_NODELAY socket option (default: false)
        - **telnet** (`boolean`, *optional*) – enable telnet protocol on server sockets (default: false)
        - **tn3270** (`boolean`, *optional*) – enable tn3270 protocol on server sockets (default: false)
          (Since: 2.10)
        - **websocket** (`boolean`, *optional*) – enable websocket protocol on server sockets
          (default: false) (Since: 3.1)
        - **reconnect-ms** (`int`, *optional*) – For a client socket, if a socket is disconnected,
          then attempt a reconnect after the given number of milliseconds.
          Setting this to zero disables this function.
          (default: 0) (Since: 9.2)
        - The members of [`ChardevCommon`](qemu-qmp-ref.md#object-QMP-char.ChardevCommon "QMP:char.ChardevCommon").

*Object* ChardevUdp (Since: 1.5)
:   Configuration info for datagram socket chardevs.

    Members:
    :   - **remote** ([`SocketAddressLegacy`](qemu-qmp-ref.md#object-QMP-sockets.SocketAddressLegacy "QMP:sockets.SocketAddressLegacy")) – remote address
        - **local** ([`SocketAddressLegacy`](qemu-qmp-ref.md#object-QMP-sockets.SocketAddressLegacy "QMP:sockets.SocketAddressLegacy"), *optional*) – local address
        - The members of [`ChardevCommon`](qemu-qmp-ref.md#object-QMP-char.ChardevCommon "QMP:char.ChardevCommon").

*Object* ChardevMux (Since: 1.5)
:   Configuration info for mux chardevs.

    Members:
    :   - **chardev** (`string`) – name of the base chardev.
        - The members of [`ChardevCommon`](qemu-qmp-ref.md#object-QMP-char.ChardevCommon "QMP:char.ChardevCommon").

*Object* ChardevHub (Since: 10.0)
:   Configuration info for hub chardevs.

    Members:
    :   - **chardevs** (`[``string``]`) – IDs to be added to this hub (maximum 4 devices).
        - The members of [`ChardevCommon`](qemu-qmp-ref.md#object-QMP-char.ChardevCommon "QMP:char.ChardevCommon").

*Object* ChardevStdio (Since: 1.5)
:   Configuration info for stdio chardevs.

    Members:
    :   - **signal** (`boolean`, *optional*) – Allow signals (such as SIGINT triggered by ^C) be delivered
          to QEMU. Default: true.
        - The members of [`ChardevCommon`](qemu-qmp-ref.md#object-QMP-char.ChardevCommon "QMP:char.ChardevCommon").

*Object* ChardevSpiceChannel (Since: 1.5)
:   *Availability*: `CONFIG_SPICE`

    Configuration info for spice vm channel chardevs.

    Members:
    :   - **type** (`string`) – kind of channel (for example vdagent).
        - The members of [`ChardevCommon`](qemu-qmp-ref.md#object-QMP-char.ChardevCommon "QMP:char.ChardevCommon").

*Object* ChardevSpicePort (Since: 1.5)
:   *Availability*: `CONFIG_SPICE`

    Configuration info for spice port chardevs.

    Members:
    :   - **fqdn** (`string`) – name of the channel (see docs/spice-port-fqdn.txt)
        - The members of [`ChardevCommon`](qemu-qmp-ref.md#object-QMP-char.ChardevCommon "QMP:char.ChardevCommon").

*Enum* ChardevVCEncoding (Since: 11.1)
:   Character encoding expected from the guest on a virtual console.

    Values:
    :   - **cp437** – CP437 (8-bit Extended ASCII / VGA). Every byte maps
          directly to a glyph; suitable for DOS or other guests that
          output raw CP437.
        - **utf8** – UTF-8. Multi-byte sequences are decoded and then mapped
          back to CP437 glyphs for display; unmappable codepoints are
          shown as ‘?’. Suitable for modern Linux guests.

*Object* ChardevDBus (Since: 7.0)
:   *Availability*: `CONFIG_DBUS_DISPLAY`

    Configuration info for DBus chardevs.

    Members:
    :   - **name** (`string`) – name of the channel (following docs/spice-port-fqdn.txt)
        - **encoding** ([`ChardevVCEncoding`](qemu-qmp-ref.md#enum-QMP-char.ChardevVCEncoding "QMP:char.ChardevVCEncoding"), *optional*) – character encoding the guest is expected to use
          (since 11.1)
        - The members of [`ChardevCommon`](qemu-qmp-ref.md#object-QMP-char.ChardevCommon "QMP:char.ChardevCommon").

*Object* ChardevVC (Since: 1.5)
:   Configuration info for virtual console chardevs.

    Members:
    :   - **width** (`int`, *optional*) – console width, in pixels
        - **height** (`int`, *optional*) – console height, in pixels
        - **cols** (`int`, *optional*) – console width, in chars
        - **rows** (`int`, *optional*) – console height, in chars
        - **encoding** ([`ChardevVCEncoding`](qemu-qmp-ref.md#enum-QMP-char.ChardevVCEncoding "QMP:char.ChardevVCEncoding"), *optional*) – character encoding the guest is expected to use
          (since 11.1)
        - The members of [`ChardevCommon`](qemu-qmp-ref.md#object-QMP-char.ChardevCommon "QMP:char.ChardevCommon").

    > **Note:**
    >
    > The options are only effective when the VNC or SDL
    > graphical display backend is active. They are ignored with the
    > GTK, Spice, VNC and D-Bus display backends.

*Object* ChardevRingbuf (Since: 1.5)
:   Configuration info for ring buffer chardevs.

    Members:
    :   - **size** (`int`, *optional*) – ring buffer size, must be power of two, default is 65536
        - The members of [`ChardevCommon`](qemu-qmp-ref.md#object-QMP-char.ChardevCommon "QMP:char.ChardevCommon").

*Object* ChardevQemuVDAgent (Since: 6.1)
:   *Availability*: `CONFIG_SPICE_PROTOCOL`

    Configuration info for QEMU vdagent implementation.

    Members:
    :   - **mouse** (`boolean`, *optional*) – enable/disable mouse, default is enabled.
        - **clipboard** (`boolean`, *optional*) – enable/disable clipboard, default is disabled.
        - The members of [`ChardevCommon`](qemu-qmp-ref.md#object-QMP-char.ChardevCommon "QMP:char.ChardevCommon").

*Object* ChardevPty (Since: 9.2)
:   Configuration info for pty implementation.

    Members:
    :   - **path** (`string`, *optional*) – optional path to create a symbolic link that points to the
          allocated PTY
        - The members of [`ChardevCommon`](qemu-qmp-ref.md#object-QMP-char.ChardevCommon "QMP:char.ChardevCommon").

*Enum* ChardevBackendKind (Since: 1.4)
:   Values:
    :   - **file** – regular files
        - **serial** – serial host device
        - **parallel** – parallel host device
        - **pipe** – pipes (since 1.5)
        - **socket** – stream socket
        - **udp** – datagram socket (since 1.5)
        - **pty** – pseudo-terminal
        - **null** – provides no input, throws away output
        - **mux** – (since 1.5)
        - **hub** – (since 10.0)
        - **msmouse** – emulated Microsoft serial mouse (since 1.5)
        - **wctablet** – emulated Wacom Penpartner serial tablet (since 2.9)
        - **braille** – Baum Braille device (since 1.5)
        - **testdev** – device for test-suite control (since 2.2)
        - **stdio** – standard I/O (since 1.5)
        - **console** – Windows console (since 1.5)
        - **spicevmc** – spice vm channel (since 1.5)
        - **spiceport** – Spice port channel (since 1.5)
        - **qemu-vdagent** – Spice vdagent (since 6.1)
        - **dbus** – D-Bus channel (since 7.0)
        - **vc** – virtual console (since 1.5)
        - **ringbuf** – memory ring buffer (since 1.6)
        - **memory** – synonym for `ringbuf` (since 1.5)

    Features:
    :   - **deprecated** – Member `memory` is deprecated. Use `ringbuf` instead.

*Object* ChardevFileWrapper (Since: 1.4)
:   Members:
    :   - **data** ([`ChardevFile`](qemu-qmp-ref.md#object-QMP-char.ChardevFile "QMP:char.ChardevFile")) – Configuration info for file chardevs

*Object* ChardevHostdevWrapper (Since: 1.4)
:   Members:
    :   - **data** ([`ChardevHostdev`](qemu-qmp-ref.md#object-QMP-char.ChardevHostdev "QMP:char.ChardevHostdev")) – Configuration info for device and pipe chardevs

*Object* ChardevSocketWrapper (Since: 1.4)
:   Members:
    :   - **data** ([`ChardevSocket`](qemu-qmp-ref.md#object-QMP-char.ChardevSocket "QMP:char.ChardevSocket")) – Configuration info for (stream) socket chardevs

*Object* ChardevUdpWrapper (Since: 1.5)
:   Members:
    :   - **data** ([`ChardevUdp`](qemu-qmp-ref.md#object-QMP-char.ChardevUdp "QMP:char.ChardevUdp")) – Configuration info for datagram socket chardevs

*Object* ChardevCommonWrapper (Since: 2.6)
:   Members:
    :   - **data** ([`ChardevCommon`](qemu-qmp-ref.md#object-QMP-char.ChardevCommon "QMP:char.ChardevCommon")) – Configuration shared across all chardev backends

*Object* ChardevMuxWrapper (Since: 1.5)
:   Members:
    :   - **data** ([`ChardevMux`](qemu-qmp-ref.md#object-QMP-char.ChardevMux "QMP:char.ChardevMux")) – Configuration info for mux chardevs

*Object* ChardevHubWrapper (Since: 10.0)
:   Members:
    :   - **data** ([`ChardevHub`](qemu-qmp-ref.md#object-QMP-char.ChardevHub "QMP:char.ChardevHub")) – Configuration info for hub chardevs

*Object* ChardevStdioWrapper (Since: 1.5)
:   Members:
    :   - **data** ([`ChardevStdio`](qemu-qmp-ref.md#object-QMP-char.ChardevStdio "QMP:char.ChardevStdio")) – Configuration info for stdio chardevs

*Object* ChardevSpiceChannelWrapper (Since: 1.5)
:   *Availability*: `CONFIG_SPICE`

    Members:
    :   - **data** ([`ChardevSpiceChannel`](qemu-qmp-ref.md#object-QMP-char.ChardevSpiceChannel "QMP:char.ChardevSpiceChannel")) – Configuration info for spice vm channel chardevs

*Object* ChardevSpicePortWrapper (Since: 1.5)
:   *Availability*: `CONFIG_SPICE`

    Members:
    :   - **data** ([`ChardevSpicePort`](qemu-qmp-ref.md#object-QMP-char.ChardevSpicePort "QMP:char.ChardevSpicePort")) – Configuration info for spice port chardevs

*Object* ChardevQemuVDAgentWrapper (Since: 6.1)
:   *Availability*: `CONFIG_SPICE_PROTOCOL`

    Members:
    :   - **data** ([`ChardevQemuVDAgent`](qemu-qmp-ref.md#object-QMP-char.ChardevQemuVDAgent "QMP:char.ChardevQemuVDAgent")) – Configuration info for QEMU vdagent implementation

*Object* ChardevDBusWrapper (Since: 7.0)
:   *Availability*: `CONFIG_DBUS_DISPLAY`

    Members:
    :   - **data** ([`ChardevDBus`](qemu-qmp-ref.md#object-QMP-char.ChardevDBus "QMP:char.ChardevDBus")) – Configuration info for DBus chardevs

*Object* ChardevVCWrapper (Since: 1.5)
:   Members:
    :   - **data** ([`ChardevVC`](qemu-qmp-ref.md#object-QMP-char.ChardevVC "QMP:char.ChardevVC")) – Configuration info for virtual console chardevs

*Object* ChardevRingbufWrapper (Since: 1.5)
:   Members:
    :   - **data** ([`ChardevRingbuf`](qemu-qmp-ref.md#object-QMP-char.ChardevRingbuf "QMP:char.ChardevRingbuf")) – Configuration info for ring buffer chardevs

*Object* ChardevPtyWrapper (Since: 9.2)
:   Members:
    :   - **data** ([`ChardevPty`](qemu-qmp-ref.md#object-QMP-char.ChardevPty "QMP:char.ChardevPty")) – Configuration info for pty chardevs

*Object* ChardevBackend (Since: 1.4)
:   Configuration info for the new chardev backend.

    Members:
    :   - **type** ([`ChardevBackendKind`](qemu-qmp-ref.md#enum-QMP-char.ChardevBackendKind "QMP:char.ChardevBackendKind")) – backend type
        - When `type` is `file`: The members of [`ChardevFileWrapper`](qemu-qmp-ref.md#object-QMP-char.ChardevFileWrapper "QMP:char.ChardevFileWrapper").
        - When `type` is `serial`: The members of [`ChardevHostdevWrapper`](qemu-qmp-ref.md#object-QMP-char.ChardevHostdevWrapper "QMP:char.ChardevHostdevWrapper").
        - When `type` is `parallel`: The members of [`ChardevHostdevWrapper`](qemu-qmp-ref.md#object-QMP-char.ChardevHostdevWrapper "QMP:char.ChardevHostdevWrapper").
        - When `type` is `pipe`: The members of [`ChardevHostdevWrapper`](qemu-qmp-ref.md#object-QMP-char.ChardevHostdevWrapper "QMP:char.ChardevHostdevWrapper").
        - When `type` is `socket`: The members of [`ChardevSocketWrapper`](qemu-qmp-ref.md#object-QMP-char.ChardevSocketWrapper "QMP:char.ChardevSocketWrapper").
        - When `type` is `udp`: The members of [`ChardevUdpWrapper`](qemu-qmp-ref.md#object-QMP-char.ChardevUdpWrapper "QMP:char.ChardevUdpWrapper").
        - When `type` is `pty`: The members of [`ChardevPtyWrapper`](qemu-qmp-ref.md#object-QMP-char.ChardevPtyWrapper "QMP:char.ChardevPtyWrapper").
        - When `type` is `null`: The members of [`ChardevCommonWrapper`](qemu-qmp-ref.md#object-QMP-char.ChardevCommonWrapper "QMP:char.ChardevCommonWrapper").
        - When `type` is `mux`: The members of [`ChardevMuxWrapper`](qemu-qmp-ref.md#object-QMP-char.ChardevMuxWrapper "QMP:char.ChardevMuxWrapper").
        - When `type` is `hub`: The members of [`ChardevHubWrapper`](qemu-qmp-ref.md#object-QMP-char.ChardevHubWrapper "QMP:char.ChardevHubWrapper").
        - When `type` is `msmouse`: The members of [`ChardevCommonWrapper`](qemu-qmp-ref.md#object-QMP-char.ChardevCommonWrapper "QMP:char.ChardevCommonWrapper").
        - When `type` is `wctablet`: The members of [`ChardevCommonWrapper`](qemu-qmp-ref.md#object-QMP-char.ChardevCommonWrapper "QMP:char.ChardevCommonWrapper").
        - When `type` is `braille`: The members of [`ChardevCommonWrapper`](qemu-qmp-ref.md#object-QMP-char.ChardevCommonWrapper "QMP:char.ChardevCommonWrapper").
        - When `type` is `testdev`: The members of [`ChardevCommonWrapper`](qemu-qmp-ref.md#object-QMP-char.ChardevCommonWrapper "QMP:char.ChardevCommonWrapper").
        - When `type` is `stdio`: The members of [`ChardevStdioWrapper`](qemu-qmp-ref.md#object-QMP-char.ChardevStdioWrapper "QMP:char.ChardevStdioWrapper").
        - When `type` is `console`: The members of [`ChardevCommonWrapper`](qemu-qmp-ref.md#object-QMP-char.ChardevCommonWrapper "QMP:char.ChardevCommonWrapper").
        - When `type` is `spicevmc`: The members of [`ChardevSpiceChannelWrapper`](qemu-qmp-ref.md#object-QMP-char.ChardevSpiceChannelWrapper "QMP:char.ChardevSpiceChannelWrapper").
        - When `type` is `spiceport`: The members of [`ChardevSpicePortWrapper`](qemu-qmp-ref.md#object-QMP-char.ChardevSpicePortWrapper "QMP:char.ChardevSpicePortWrapper").
        - When `type` is `qemu-vdagent`: The members of [`ChardevQemuVDAgentWrapper`](qemu-qmp-ref.md#object-QMP-char.ChardevQemuVDAgentWrapper "QMP:char.ChardevQemuVDAgentWrapper").
        - When `type` is `dbus`: The members of [`ChardevDBusWrapper`](qemu-qmp-ref.md#object-QMP-char.ChardevDBusWrapper "QMP:char.ChardevDBusWrapper").
        - When `type` is `vc`: The members of [`ChardevVCWrapper`](qemu-qmp-ref.md#object-QMP-char.ChardevVCWrapper "QMP:char.ChardevVCWrapper").
        - When `type` is `ringbuf`: The members of [`ChardevRingbufWrapper`](qemu-qmp-ref.md#object-QMP-char.ChardevRingbufWrapper "QMP:char.ChardevRingbufWrapper").
        - When `type` is `memory`: The members of [`ChardevRingbufWrapper`](qemu-qmp-ref.md#object-QMP-char.ChardevRingbufWrapper "QMP:char.ChardevRingbufWrapper").

*Object* ChardevReturn (Since: 1.4)
:   Return info about the chardev backend just created.

    Members:
    :   - **pty** (`string`, *optional*) – name of the slave pseudoterminal device, present if and only
          if a chardev of type ‘pty’ was created

*Command* chardev-add (Since: 1.4)
:   Add a character device backend

    Arguments:
    :   - **id** (`string`) – the chardev’s ID, must be unique
        - **backend** ([`ChardevBackend`](qemu-qmp-ref.md#object-QMP-char.ChardevBackend "QMP:char.ChardevBackend")) – backend type and parameters

    Return:
    :   [`ChardevReturn`](qemu-qmp-ref.md#object-QMP-char.ChardevReturn "QMP:char.ChardevReturn")

    > **Example::**
    >
    > ```QMP
    > -> { "execute" : "chardev-add",
    >      "arguments" : { "id" : "foo",
    >                      "backend" : { "type" : "null", "data" : {} } } }
    > <- { "return": {} }
    > ```

    > **Example::**
    >
    > ```QMP
    > -> { "execute" : "chardev-add",
    >      "arguments" : { "id" : "bar",
    >                      "backend" : { "type" : "file",
    >                                    "data" : { "out" : "/tmp/bar.log" } } } }
    > <- { "return": {} }
    > ```

    > **Example::**
    >
    > ```QMP
    > -> { "execute" : "chardev-add",
    >      "arguments" : { "id" : "baz",
    >                      "backend" : { "type" : "pty", "data" : {} } } }
    > <- { "return": { "pty" : "/dev/pty/42" } }
    > ```

*Command* chardev-change (Since: 2.10)
:   Change a character device backend

    Arguments:
    :   - **id** (`string`) – the chardev’s ID
        - **backend** ([`ChardevBackend`](qemu-qmp-ref.md#object-QMP-char.ChardevBackend "QMP:char.ChardevBackend")) – new backend type and parameters

    Return:
    :   [`ChardevReturn`](qemu-qmp-ref.md#object-QMP-char.ChardevReturn "QMP:char.ChardevReturn")

    > **Example::**
    >
    > ```QMP
    > -> { "execute" : "chardev-change",
    >      "arguments" : { "id" : "baz",
    >                      "backend" : { "type" : "pty", "data" : {} } } }
    > <- { "return": { "pty" : "/dev/pty/42" } }
    > ```

    > **Example::**
    >
    > ```QMP
    > -> {"execute" : "chardev-change",
    >     "arguments" : {
    >         "id" : "charchannel2",
    >         "backend" : {
    >             "type" : "socket",
    >             "data" : {
    >                 "addr" : {
    >                     "type" : "unix" ,
    >                     "data" : {
    >                         "path" : "/tmp/charchannel2.socket"
    >                     }
    >                  },
    >                  "server" : true,
    >                  "wait" : false }}}}
    > <- {"return": {}}
    > ```

*Command* chardev-remove (Since: 1.4)
:   Remove a character device backend

    Arguments:
    :   - **id** (`string`) – the chardev’s ID, must not be in use

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "chardev-remove", "arguments": { "id" : "foo" } }
    > <- { "return": {} }
    > ```

*Command* chardev-send-break (Since: 2.10)
:   Send a break to a character device

    Arguments:
    :   - **id** (`string`) – the chardev’s ID

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "chardev-send-break", "arguments": { "id" : "foo" } }
    > <- { "return": {} }
    > ```

*Event* VSERPORT_CHANGE (Since: 2.1)
:   Emitted when the guest opens or closes a virtio-serial port.

    Members:
    :   - **id** (`string`) – device identifier of the virtio-serial port
        - **open** (`boolean`) – true if the guest has opened the virtio-serial port

    > **Note:**
    >
    > This event is rate-limited.

    > **Example::**
    >
    > ```QMP
    > <- { "event": "VSERPORT_CHANGE",
    >      "data": { "id": "channel0", "open": true },
    >      "timestamp": { "seconds": 1401385907, "microseconds": 422329 } }
    > ```

## [Dump guest memory](qemu-qmp-ref.md#id15)

*Enum* DumpGuestMemoryFormat (Since: 2.0)
:   An enumeration of guest-memory-dump’s format.

    Values:
    :   - **elf** – elf format
        - **kdump-zlib** – makedumpfile flattened, kdump-compressed format with
          zlib compression
        - **kdump-lzo** – makedumpfile flattened, kdump-compressed format with lzo
          compression
        - **kdump-snappy** – makedumpfile flattened, kdump-compressed format with
          snappy compression
        - **kdump-raw-zlib** – raw assembled kdump-compressed format with zlib
          compression (since 8.2)
        - **kdump-raw-lzo** – raw assembled kdump-compressed format with lzo
          compression (since 8.2)
        - **kdump-raw-snappy** – raw assembled kdump-compressed format with snappy
          compression (since 8.2)
        - **win-dmp** – Windows full crashdump format, can be used instead of ELF
          converting (since 2.13)

    Features:
    :   - **allowed-by-guest** – If present, `win-dmp` is listed by
          [`query-dump-guest-memory-capability`](qemu-qmp-ref.md#command-QMP-dump.query-dump-guest-memory-capability "QMP:dump.query-dump-guest-memory-capability"), and accepted by
          [`dump-guest-memory`](qemu-qmp-ref.md#command-QMP-dump.dump-guest-memory "QMP:dump.dump-guest-memory"), only when the guest has published a Windows
          dump header through the vmcoreinfo device (since 11.1)

*Command* dump-guest-memory (Since: 1.2)
:   Dump guest’s memory to vmcore. It is a synchronous operation that
    can take very long depending on the amount of guest memory.

    Arguments:
    :   - **paging** (`boolean`) –

          if true, do paging to get guest’s memory mapping. This
          allows using gdb to process the core file.

          **Important**: this option can make QEMU allocate several
          gigabytes of RAM. This can happen for a large guest, or a
          malicious guest pretending to be large.

          Also, paging=true has the following limitations:

          1. The guest may be in a catastrophic state or can have
             corrupted memory, which cannot be trusted
          2. The guest can be in real-mode even if paging is enabled. For
             example, the guest uses ACPI to sleep, and ACPI sleep state
             goes in real-mode
          3. Currently only supported on i386 and x86_64.
        - **protocol** (`string`) –

          the filename or file descriptor of the vmcore. The
          supported protocols are:

          1. file: the protocol starts with “file:”, and the following
             string is the file’s path.
          2. fd: the protocol starts with “fd:”, and the following string
             is the fd’s name.
        - **detach** (`boolean`, *optional*) – if true, QMP will return immediately rather than waiting
          for the dump to finish. The user can track progress using
          [`query-dump`](qemu-qmp-ref.md#command-QMP-dump.query-dump "QMP:dump.query-dump"). (since 2.6).
        - **begin** (`int`, *optional*) – if specified, the starting physical address.
        - **length** (`int`, *optional*) – if specified, the memory size, in bytes. If you don’t want
          to dump all guest’s memory, please specify the start `begin` and
          `length`
        - **format** ([`DumpGuestMemoryFormat`](qemu-qmp-ref.md#enum-QMP-dump.DumpGuestMemoryFormat "QMP:dump.DumpGuestMemoryFormat"), *optional*) – if specified, the format of guest memory dump. But non-elf
          format is conflict with paging and filter, ie. `paging`, `begin`
          and `length` is not allowed to be specified with non-elf `format`
          at the same time (since 2.0)

    > **Note:**
    >
    > All boolean arguments default to false.

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "dump-guest-memory",
    >      "arguments": { "paging": false, "protocol": "fd:dump" } }
    > <- { "return": {} }
    > ```

*Enum* DumpStatus (Since: 2.6)
:   Describe the status of a long-running background guest memory dump.

    Values:
    :   - **none** – no [`dump-guest-memory`](qemu-qmp-ref.md#command-QMP-dump.dump-guest-memory "QMP:dump.dump-guest-memory") has started yet.
        - **active** – there is one dump running in background.
        - **completed** – the last dump has finished successfully.
        - **failed** – the last dump has failed.

*Object* DumpQueryResult (Since: 2.6)
:   The result format for [`query-dump`](qemu-qmp-ref.md#command-QMP-dump.query-dump "QMP:dump.query-dump").

    Members:
    :   - **status** ([`DumpStatus`](qemu-qmp-ref.md#enum-QMP-dump.DumpStatus "QMP:dump.DumpStatus")) – enum of [`DumpStatus`](qemu-qmp-ref.md#enum-QMP-dump.DumpStatus "QMP:dump.DumpStatus"), which shows current dump status
        - **completed** (`int`) – bytes written in latest dump (uncompressed)
        - **total** (`int`) – total bytes to be written in latest dump (uncompressed)

*Command* query-dump (Since: 2.6)
:   Query latest dump status.

    Return:
    :   [`DumpQueryResult`](qemu-qmp-ref.md#object-QMP-dump.DumpQueryResult "QMP:dump.DumpQueryResult") – An object showing the dump status.

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "query-dump" }
    > <- { "return": { "status": "active", "completed": 1024000,
    >                  "total": 2048000 } }
    > ```

*Event* DUMP_COMPLETED (Since: 2.6)
:   Emitted when background dump has completed

    Members:
    :   - **result** ([`DumpQueryResult`](qemu-qmp-ref.md#object-QMP-dump.DumpQueryResult "QMP:dump.DumpQueryResult")) – final dump status
        - **error** (`string`, *optional*) – human-readable error string that provides hint on why dump
          failed. Only presents on failure. The user should not try to
          interpret the error string.

    > **Example::**
    >
    > ```QMP
    > <- { "event": "DUMP_COMPLETED",
    >      "data": { "result": { "total": 1090650112, "status": "completed",
    >                            "completed": 1090650112 } },
    >      "timestamp": { "seconds": 1648244171, "microseconds": 950316 } }
    > ```

*Object* DumpGuestMemoryCapability (Since: 2.0)
:   Members:
    :   - **formats** (`[`[`DumpGuestMemoryFormat`](qemu-qmp-ref.md#enum-QMP-dump.DumpGuestMemoryFormat "QMP:dump.DumpGuestMemoryFormat")`]`) – the available formats for [`dump-guest-memory`](qemu-qmp-ref.md#command-QMP-dump.dump-guest-memory "QMP:dump.dump-guest-memory")

*Command* query-dump-guest-memory-capability (Since: 2.0)
:   Return the available formats for [`dump-guest-memory`](qemu-qmp-ref.md#command-QMP-dump.dump-guest-memory "QMP:dump.dump-guest-memory")

    Return:
    :   [`DumpGuestMemoryCapability`](qemu-qmp-ref.md#object-QMP-dump.DumpGuestMemoryCapability "QMP:dump.DumpGuestMemoryCapability") – An object listing available formats for [`dump-guest-memory`](qemu-qmp-ref.md#command-QMP-dump.dump-guest-memory "QMP:dump.dump-guest-memory")

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "query-dump-guest-memory-capability" }
    > <- { "return": { "formats":
    >                  ["elf", "kdump-zlib", "kdump-lzo", "kdump-snappy"] } }
    > ```

## [Net devices](qemu-qmp-ref.md#id16)

*Command* set_link (Since: 0.14)
:   Sets the link status of a virtual network adapter.

    Arguments:
    :   - **name** (`string`) – the device name of the virtual network adapter
        - **up** (`boolean`) – true to set the link status to be up

    Errors:
    :   - If `name` is not a valid network device, DeviceNotFound

    > **Note:**
    >
    > Not all network adapters support setting link status.
    > This command will succeed even if the network adapter does not
    > support link status notification.

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "set_link",
    >      "arguments": { "name": "e1000.0", "up": false } }
    > <- { "return": {} }
    > ```

*Command* netdev_add (Since: 0.14)
:   Add a network backend.

    Additional arguments depend on the type.

    Arguments:
    :   - The members of [`Netdev`](qemu-qmp-ref.md#object-QMP-net.Netdev "QMP:net.Netdev").

    Errors:
    :   - If `type` is not a valid network backend, DeviceNotFound

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "netdev_add",
    >      "arguments": { "type": "user", "id": "netdev1",
    >                     "dnssearch": [ { "str": "example.org" } ] } }
    > <- { "return": {} }
    > ```

*Command* netdev_del (Since: 0.14)
:   Remove a network backend.

    Arguments:
    :   - **id** (`string`) – the name of the network backend to remove

    Errors:
    :   - If `id` is not a valid network backend, DeviceNotFound

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "netdev_del", "arguments": { "id": "netdev1" } }
    > <- { "return": {} }
    > ```

*Object* NetLegacyNicOptions (Since: 1.2)
:   Create a new Network Interface Card.

    Members:
    :   - **netdev** (`string`, *optional*) – id of -netdev to connect to
        - **macaddr** (`string`, *optional*) – MAC address
        - **model** (`string`, *optional*) – device model (e1000, rtl8139, virtio etc.)
        - **addr** (`string`, *optional*) – PCI device address
        - **vectors** (`int`, *optional*) – number of MSI-x vectors, 0 to disable MSI-X

*Object* PasstSearch (Since: 10.1)
:   Members:
    :   - **str** (`string`) – DNS domain name suffix for host name lookup, or “none”. See
          passt(1) option –search.

*Object* PasstPortForward (Since: 10.1)
:   Members:
    :   - **str** (`string`) – passt port forwarding specification, see passt(1) option
          –tcp-ports and –udp-ports.

*Object* PasstParameter (Since: 10.1)
:   Members:
    :   - **str** (`string`) – Additional arguments for the passt executable, see passt(1)

*Object* NetdevPasstOptions (Since: 10.1)
:   *Availability*: `CONFIG_PASST`

    Unprivileged user-mode network connectivity using passt

    Members:
    :   - **path** (`string`, *optional*) – Filename of the passt program to run (by default ‘passt’, and
          use PATH)
        - **quiet** (`boolean`, *optional*) – don’t print informational messages (default, passed as
          ‘–quiet’)
        - **vhost-user** (`boolean`, *optional*) – enable vhost-user
        - **mtu** (`int`, *optional*) – assign MTU via DHCP/NDP
        - **address** (`string`, *optional*) – IPv4 or IPv6 address
        - **netmask** (`string`, *optional*) – IPv4 mask
        - **mac** (`string`, *optional*) – source MAC address
        - **gateway** (`string`, *optional*) – IPv4 or IPv6 address as gateway
        - **interface** (`string`, *optional*) – interface for addresses and routes
        - **outbound** (`string`, *optional*) – bind to address as outbound source
        - **outbound-if4** (`string`, *optional*) – bind to outbound interface for IPv4
        - **outbound-if6** (`string`, *optional*) – bind to outbound interface for IPv6
        - **dns** (`string`, *optional*) – IPv4 or IPv6 address as DNS
        - **search** (`[`[`PasstSearch`](qemu-qmp-ref.md#object-QMP-net.PasstSearch "QMP:net.PasstSearch")`]`, *optional*) – search domains
        - **fqdn** (`string`, *optional*) – FQDN to configure client with
        - **dhcp-dns** (`boolean`, *optional*) – enable/disable DNS list in DHCP/DHCPv6/NDP
        - **dhcp-search** (`boolean`, *optional*) – enable/disable list in DHCP/DHCPv6/NDP
        - **map-host-loopback** (`string`, *optional*) – addresse to refer to host
        - **map-guest-addr** (`string`, *optional*) – addr to translate to guest’s address
        - **dns-forward** (`string`, *optional*) – forward DNS queries sent to
        - **dns-host** (`string`, *optional*) – host nameserver to direct queries to
        - **tcp** (`boolean`, *optional*) – enable/disable TCP
        - **udp** (`boolean`, *optional*) – enable/disable UDP
        - **icmp** (`boolean`, *optional*) – enable/disable ICMP
        - **dhcp** (`boolean`, *optional*) – enable/disable DHCP
        - **ndp** (`boolean`, *optional*) – enable/disable NDP
        - **dhcpv6** (`boolean`, *optional*) – enable/disable DHCPv6
        - **ra** (`boolean`, *optional*) – enable/disable route advertisements
        - **freebind** (`boolean`, *optional*) – bind to any address for forwarding
        - **ipv4** (`boolean`, *optional*) – enable/disable IPv4
        - **ipv6** (`boolean`, *optional*) – enable/disable IPv6
        - **tcp-ports** (`[`[`PasstPortForward`](qemu-qmp-ref.md#object-QMP-net.PasstPortForward "QMP:net.PasstPortForward")`]`, *optional*) – TCP ports to forward
        - **udp-ports** (`[`[`PasstPortForward`](qemu-qmp-ref.md#object-QMP-net.PasstPortForward "QMP:net.PasstPortForward")`]`, *optional*) – UDP ports to forward
        - **param** (`[`[`PasstParameter`](qemu-qmp-ref.md#object-QMP-net.PasstParameter "QMP:net.PasstParameter")`]`, *optional*) – parameter to pass to passt command

*Object* NetdevUserDomainSuffix (Since: 1.2)
:   Members:
    :   - **str** (`string`) – DNS domain name suffix for host name lookup, similar to
          resolv.conf(5)

*Object* NetdevUserHostForward (Since: 1.2)
:   Members:
    :   - **str** (`string`) – Host port forwarding rule

*Object* NetdevUserGuestForward (Since: 1.2)
:   Members:
    :   - **str** (`string`) – Guest port forwarding rule

*Object* NetdevUserOptions (Since: 1.2)
:   Use the user mode network stack which requires no administrator
    privilege to run.

    Members:
    :   - **hostname** (`string`, *optional*) – client hostname reported by the builtin DHCP server
        - **restrict** (`boolean`, *optional*) – isolate the guest from the host
        - **ipv4** (`boolean`, *optional*) – whether to support IPv4, default true for enabled (since 2.6)
        - **ipv6** (`boolean`, *optional*) – whether to support IPv6, default true for enabled (since 2.6)
        - **ip** (`string`, *optional*) – legacy parameter, use net= instead
        - **net** (`string`, *optional*) – IP network address that the guest will see, in the form
          addr[/netmask] The netmask is optional, and can be either in the
          form a.b.c.d or as a number of valid top-most bits. Default is
          10.0.2.0/24.
        - **host** (`string`, *optional*) – guest-visible address of the host
        - **tftp** (`string`, *optional*) – root directory of the built-in TFTP server
        - **bootfile** (`string`, *optional*) – BOOTP filename, for use with tftp=
        - **dhcpstart** (`string`, *optional*) – the first of the 16 IPs the built-in DHCP server can
          assign
        - **dns** (`string`, *optional*) – guest-visible address of the virtual nameserver
        - **dnssearch** (`[`[`NetdevUserDomainSuffix`](qemu-qmp-ref.md#object-QMP-net.NetdevUserDomainSuffix "QMP:net.NetdevUserDomainSuffix")`]`, *optional*) – list of DNS suffixes to search, passed as DHCP option to
          the guest
        - **domainname** (`string`, *optional*) – guest-visible domain name of the virtual nameserver
          (since 3.0)
        - **ipv6-prefix** (`string`, *optional*) – IPv6 network prefix (default is fec0::). The network
          prefix is given in the usual hexadecimal IPv6 address notation.
          (since 2.6)
        - **ipv6-prefixlen** (`int`, *optional*) – IPv6 network prefix length (default is 64)
          (since 2.6)
        - **ipv6-host** (`string`, *optional*) – guest-visible IPv6 address of the host (since 2.6)
        - **ipv6-dns** (`string`, *optional*) – guest-visible IPv6 address of the virtual nameserver
          (since 2.6)
        - **smb** (`string`, *optional*) – root directory of the built-in SMB server
        - **smbserver** (`string`, *optional*) – IP address of the built-in SMB server
        - **hostfwd** (`[`[`NetdevUserHostForward`](qemu-qmp-ref.md#object-QMP-net.NetdevUserHostForward "QMP:net.NetdevUserHostForward")`]`, *optional*) – redirect incoming TCP, UDP or UNIX host connections to
          guest endpoints
        - **guestfwd** (`[`[`NetdevUserGuestForward`](qemu-qmp-ref.md#object-QMP-net.NetdevUserGuestForward "QMP:net.NetdevUserGuestForward")`]`, *optional*) – forward guest TCP connections
        - **tftp-server-name** (`string`, *optional*) – RFC2132 “TFTP server name” string (Since 3.1)

*Object* NetdevTapOptions (Since: 1.2)
:   Used to configure a host TAP network interface backend.

    Members:
    :   - **ifname** (`string`, *optional*) – interface name
        - **fd** (`string`, *optional*) – file descriptor of an already opened tap
        - **fds** (`string`, *optional*) – multiple file descriptors of already opened multiqueue capable
          tap
        - **script** (`string`, *optional*) – script to initialize the interface
        - **downscript** (`string`, *optional*) – script to shut down the interface
        - **br** (`string`, *optional*) – bridge name (since 2.8)
        - **helper** (`string`, *optional*) – command to execute to configure bridge
        - **sndbuf** (`int`, *optional*) – send buffer limit. Understands [TGMKkb] suffixes.
        - **vnet_hdr** (`boolean`, *optional*) – enable the IFF_VNET_HDR flag on the tap interface
        - **vhost** (`boolean`, *optional*) – enable vhost-net network accelerator
        - **vhostfd** (`string`, *optional*) – file descriptor of an already opened vhost net device
        - **vhostfds** (`string`, *optional*) – file descriptors of multiple already opened vhost net
          devices
        - **vhostforce** (`boolean`, *optional*) – vhost on for non-MSIX virtio guests
        - **queues** (`int`, *optional*) – number of queues to be created for multiqueue capable tap
        - **poll-us** (`int`, *optional*) – maximum number of microseconds that could be spent on busy
          polling for tap (since 2.7)

*Object* NetdevSocketOptions (Since: 1.2)
:   Socket netdevs are used to establish a network connection to another
    QEMU virtual machine via a TCP socket.

    Members:
    :   - **fd** (`string`, *optional*) – file descriptor of an already opened socket
        - **listen** (`string`, *optional*) – port number, and optional hostname, to listen on
        - **connect** (`string`, *optional*) – port number, and optional hostname, to connect to
        - **mcast** (`string`, *optional*) – UDP multicast address and port number
        - **localaddr** (`string`, *optional*) – source address and port for multicast and udp packets
        - **udp** (`string`, *optional*) – UDP unicast address and port number

*Object* NetdevL2TPv3Options (Since: 2.1)
:   Configure an Ethernet over L2TPv3 tunnel.

    Members:
    :   - **src** (`string`) – source address
        - **dst** (`string`) – destination address
        - **srcport** (`string`, *optional*) – source port - mandatory for udp, optional for ip
        - **dstport** (`string`, *optional*) – destination port - mandatory for udp, optional for ip
        - **ipv6** (`boolean`, *optional*) – force the use of ipv6
        - **udp** (`boolean`, *optional*) – use the udp version of l2tpv3 encapsulation
        - **cookie64** (`boolean`, *optional*) – use 64 bit cookies
        - **counter** (`boolean`, *optional*) – have sequence counter
        - **pincounter** (`boolean`, *optional*) – pin sequence counter to zero - workaround for buggy
          implementations or networks with packet reorder
        - **txcookie** (`int`, *optional*) – 32 or 64 bit transmit cookie
        - **rxcookie** (`int`, *optional*) – 32 or 64 bit receive cookie
        - **txsession** (`int`) – 32 bit transmit session
        - **rxsession** (`int`, *optional*) – 32 bit receive session - if not specified set to the
          same value as transmit
        - **offset** (`int`, *optional*) – additional offset - allows the insertion of additional
          application-specific data before the packet payload

*Object* NetdevVdeOptions (Since: 1.2)
:   Connect to a vde switch running on the host.

    Members:
    :   - **sock** (`string`, *optional*) – socket path
        - **port** (`int`, *optional*) – port number
        - **group** (`string`, *optional*) – group owner of socket
        - **mode** (`int`, *optional*) – permissions for socket

*Object* NetdevBridgeOptions (Since: 1.2)
:   Connect a host TAP network interface to a host bridge device.

    Members:
    :   - **br** (`string`, *optional*) – bridge name
        - **helper** (`string`, *optional*) – command to execute to configure bridge

*Object* NetdevHubPortOptions (Since: 1.2)
:   Connect two or more net clients through a software hub.

    Members:
    :   - **hubid** (`int`) – hub identifier number
        - **netdev** (`string`, *optional*) – used to connect hub to a netdev instead of a device
          (since 2.12)

*Object* NetdevNetmapOptions (Since: 2.0)
:   Connect a client to a netmap-enabled NIC or to a VALE switch port

    Members:
    :   - **ifname** (`string`) – Either the name of an existing network interface supported
          by netmap, or the name of a VALE port (created on the fly). A
          VALE port name is in the form ‘valeXXX:YYY’, where XXX and YYY
          are non-negative integers. XXX identifies a switch and YYY
          identifies a port of the switch. VALE ports having the same XXX
          are therefore connected to the same switch.
        - **devname** (`string`, *optional*) – path of the netmap device (default: ‘/dev/netmap’).

*Enum* AFXDPMode (Since: 8.2)
:   *Availability*: `CONFIG_AF_XDP`

    Attach mode for a default XDP program

    Values:
    :   - **skb** – generic mode, no driver support necessary
        - **native** – DRV mode, program is attached to a driver, packets are
          passed to the socket without allocation of skb.

*Object* NetdevAFXDPOptions (Since: 8.2)
:   *Availability*: `CONFIG_AF_XDP`

    AF_XDP network backend

    Members:
    :   - **ifname** (`string`) – The name of an existing network interface.
        - **mode** ([`AFXDPMode`](qemu-qmp-ref.md#enum-QMP-net.AFXDPMode "QMP:net.AFXDPMode"), *optional*) – Attach mode for a default XDP program. If not specified,
          then ‘native’ will be tried first, then ‘skb’.
        - **force-copy** (`boolean`, *optional*) – Force XDP copy mode even if device supports zero-copy.
          (default: false)
        - **queues** (`int`, *optional*) – number of queues to be used for multiqueue interfaces
          (default: 1).
        - **start-queue** (`int`, *optional*) – Use `queues` starting from this queue number
          (default: 0).
        - **inhibit** (`boolean`, *optional*) – Don’t load a default XDP program, use one already loaded
          to the interface (default: false). Requires `sock-fds` or
          `map-path`.
        - **sock-fds** (`string`, *optional*) – A colon (:) separated list of file descriptors for
          already open but not bound AF_XDP sockets in the queue order.
          One fd per queue. These descriptors should already be added
          into XDP socket map for corresponding queues. `sock-fds` and
          `map-path` are mutually exclusive. Requires `inhibit`.
        - **map-path** (`string`, *optional*) – The path to a pinned xsk map to push file descriptors
          for bound AF_XDP sockets into. `map-path` and `sock-fds` are
          mutually exclusive. Requires `inhibit`. (Since 10.1)
        - **map-start-index** (`int`, *optional*) – Use `map-path` to insert xsk sockets starting from
          this index number (default: 0). Requires `map-path`.
          (Since 10.1)

*Object* NetdevVhostUserOptions (Since: 2.1)
:   Vhost-user network backend

    Members:
    :   - **chardev** (`string`) – name of a unix socket chardev
        - **vhostforce** (`boolean`, *optional*) – vhost on for non-MSIX virtio guests (default: false).
        - **queues** (`int`, *optional*) – number of queues to be created for multiqueue vhost-user
          (default: 1) (Since 2.5)

*Object* NetdevVhostVDPAOptions (Since: 5.1)
:   Vhost-vdpa network backend

    vDPA device is a device that uses a datapath which complies with the
    virtio specifications with a vendor specific control path.

    Members:
    :   - **vhostdev** (`string`, *optional*) – path of vhost-vdpa device (default:’/dev/vhost-vdpa-0’)
        - **vhostfd** (`string`, *optional*) – file descriptor of an already opened vhost vdpa device
        - **queues** (`int`, *optional*) – number of queues to be created for multiqueue vhost-vdpa
          (default: 1)
        - **x-svq** (`boolean`, *optional*) – Start device with (experimental) shadow virtqueue.
          (Since 7.1) (default: false)

    Features:
    :   - **unstable** – Member `x-svq` is experimental.

*Object* NetdevVmnetHostOptions (Since: 7.1)
:   *Availability*: `CONFIG_VMNET`

    vmnet (host mode) network backend.

    Allows the vmnet interface to communicate with other vmnet
    interfaces that are in host mode and also with the host.

    Members:
    :   - **start-address** (`string`, *optional*) – The starting IPv4 address to use for the interface.
          Must be in the private IP range (RFC 1918). Must be specified
          along with `end-address` and `subnet-mask`. This address is used
          as the gateway address. The subsequent address up to and
          including end-address are placed in the DHCP pool.
        - **end-address** (`string`, *optional*) – The DHCP IPv4 range end address to use for the
          interface. Must be in the private IP range (RFC 1918). Must be
          specified along with `start-address` and `subnet-mask`.
        - **subnet-mask** (`string`, *optional*) – The IPv4 subnet mask to use on the interface. Must be
          specified along with `start-address` and `subnet-mask`.
        - **isolated** (`boolean`, *optional*) – Enable isolation for this interface. Interface isolation
          ensures that vmnet interface is not able to communicate with any
          other vmnet interfaces. Only communication with host is
          allowed. Requires at least macOS Big Sur 11.0.
        - **net-uuid** (`string`, *optional*) – The identifier (UUID) to uniquely identify the isolated
          network vmnet interface should be added to. If set, no DHCP
          service is provided for this interface and network communication
          is allowed only with other interfaces added to this network
          identified by the UUID. Requires at least macOS Big Sur 11.0.

*Object* NetdevVmnetSharedOptions (Since: 7.1)
:   *Availability*: `CONFIG_VMNET`

    vmnet (shared mode) network backend.

    Allows traffic originating from the vmnet interface to reach the
    Internet through a network address translator (NAT). The vmnet
    interface can communicate with the host and with other shared mode
    interfaces on the same subnet. If no DHCP settings, subnet mask and
    IPv6 prefix specified, the interface can communicate with any of
    other interfaces in shared mode.

    Members:
    :   - **start-address** (`string`, *optional*) – The starting IPv4 address to use for the interface.
          Must be in the private IP range (RFC 1918). Must be specified
          along with `end-address` and `subnet-mask`. This address is used
          as the gateway address. The subsequent address up to and
          including end-address are placed in the DHCP pool.
        - **end-address** (`string`, *optional*) – The DHCP IPv4 range end address to use for the
          interface. Must be in the private IP range (RFC 1918). Must be
          specified along with `start-address` and `subnet-mask`.
        - **subnet-mask** (`string`, *optional*) – The IPv4 subnet mask to use on the interface. Must be
          specified along with `start-address` and `subnet-mask`.
        - **isolated** (`boolean`, *optional*) – Enable isolation for this interface. Interface isolation
          ensures that vmnet interface is not able to communicate with any
          other vmnet interfaces. Only communication with host is
          allowed. Requires at least macOS Big Sur 11.0.
        - **nat66-prefix** (`string`, *optional*) – The IPv6 prefix to use into guest network. Must be a
          unique local address i.e. start with fd00::/8 and have length of
          64.

*Object* NetdevVmnetBridgedOptions (Since: 7.1)
:   *Availability*: `CONFIG_VMNET`

    vmnet (bridged mode) network backend.

    Bridges the vmnet interface with a physical network interface.

    Members:
    :   - **ifname** (`string`) – The name of the physical interface to be bridged.
        - **isolated** (`boolean`, *optional*) – Enable isolation for this interface. Interface isolation
          ensures that vmnet interface is not able to communicate with any
          other vmnet interfaces. Only communication with host is
          allowed. Requires at least macOS Big Sur 11.0.

*Object* NetdevStreamOptions (Since: 7.2)
:   Configuration info for stream socket netdev

    Members:
    :   - **addr** ([`SocketAddress`](qemu-qmp-ref.md#object-QMP-sockets.SocketAddress "QMP:sockets.SocketAddress")) – socket address to listen on (server=true) or connect to
          (server=false)
        - **server** (`boolean`, *optional*) – create server socket (default: false)
        - **reconnect-ms** (`int`, *optional*) – For a client socket, if a socket is disconnected,
          then attempt a reconnect after the given number of milliseconds.
          Setting this to zero disables this function.
          (default: 0) (Since: 9.2)

    Only [`SocketAddress`](qemu-qmp-ref.md#object-QMP-sockets.SocketAddress "QMP:sockets.SocketAddress") types ‘unix’, ‘inet’ and ‘fd’ are supported.

*Object* NetdevDgramOptions (Since: 7.2)
:   Configuration info for datagram socket netdev.

    Members:
    :   - **remote** ([`SocketAddress`](qemu-qmp-ref.md#object-QMP-sockets.SocketAddress "QMP:sockets.SocketAddress"), *optional*) – remote address
        - **local** ([`SocketAddress`](qemu-qmp-ref.md#object-QMP-sockets.SocketAddress "QMP:sockets.SocketAddress"), *optional*) – local address

    Only [`SocketAddress`](qemu-qmp-ref.md#object-QMP-sockets.SocketAddress "QMP:sockets.SocketAddress") types ‘unix’, ‘inet’ and ‘fd’ are supported.

    If remote address is present and it’s a multicast address, local
    address is optional. Otherwise local address is required and remote
    address is optional.

    Valid parameters combination table

    | remote | local | okay? |
    | --- | --- | --- |
    | absent | absent | no |
    | absent | not fd | no |
    | absent | fd | yes |
    | multicast | absent | yes |
    | multicast | present | yes |
    | not multicast | absent | no |
    | not multicast | present | yes |

*Enum* NetClientDriver (Since: 2.7)
:   Available netdev drivers.

    Values:
    :   - **l2tpv3** – since 2.1
        - **vhost-vdpa** – since 5.1
        - **vmnet-host** – since 7.1
        - **vmnet-shared** – since 7.1
        - **vmnet-bridged** – since 7.1
        - **stream** – since 7.2
        - **dgram** – since 7.2
        - **af-xdp** – since 8.2
        - **passt** – since 10.1
        - **none** – Not documented
        - **nic** – Not documented
        - **user** – Not documented
        - **tap** – Not documented
        - **socket** – Not documented
        - **vde** – Not documented
        - **bridge** – Not documented
        - **hubport** – Not documented
        - **netmap** – Not documented
        - **vhost-user** – Not documented

*Object* Netdev (Since: 1.2)
:   Captures the configuration of a network device.

    Members:
    :   - **id** (`string`) – identifier for monitor commands.
        - **type** ([`NetClientDriver`](qemu-qmp-ref.md#enum-QMP-net.NetClientDriver "QMP:net.NetClientDriver")) – Specify the driver used for interpreting remaining arguments.
        - When `type` is `nic`: The members of [`NetLegacyNicOptions`](qemu-qmp-ref.md#object-QMP-net.NetLegacyNicOptions "QMP:net.NetLegacyNicOptions").
        - When `type` is `passt`: The members of [`NetdevPasstOptions`](qemu-qmp-ref.md#object-QMP-net.NetdevPasstOptions "QMP:net.NetdevPasstOptions").
        - When `type` is `user`: The members of [`NetdevUserOptions`](qemu-qmp-ref.md#object-QMP-net.NetdevUserOptions "QMP:net.NetdevUserOptions").
        - When `type` is `tap`: The members of [`NetdevTapOptions`](qemu-qmp-ref.md#object-QMP-net.NetdevTapOptions "QMP:net.NetdevTapOptions").
        - When `type` is `l2tpv3`: The members of [`NetdevL2TPv3Options`](qemu-qmp-ref.md#object-QMP-net.NetdevL2TPv3Options "QMP:net.NetdevL2TPv3Options").
        - When `type` is `socket`: The members of [`NetdevSocketOptions`](qemu-qmp-ref.md#object-QMP-net.NetdevSocketOptions "QMP:net.NetdevSocketOptions").
        - When `type` is `stream`: The members of [`NetdevStreamOptions`](qemu-qmp-ref.md#object-QMP-net.NetdevStreamOptions "QMP:net.NetdevStreamOptions").
        - When `type` is `dgram`: The members of [`NetdevDgramOptions`](qemu-qmp-ref.md#object-QMP-net.NetdevDgramOptions "QMP:net.NetdevDgramOptions").
        - When `type` is `vde`: The members of [`NetdevVdeOptions`](qemu-qmp-ref.md#object-QMP-net.NetdevVdeOptions "QMP:net.NetdevVdeOptions").
        - When `type` is `bridge`: The members of [`NetdevBridgeOptions`](qemu-qmp-ref.md#object-QMP-net.NetdevBridgeOptions "QMP:net.NetdevBridgeOptions").
        - When `type` is `hubport`: The members of [`NetdevHubPortOptions`](qemu-qmp-ref.md#object-QMP-net.NetdevHubPortOptions "QMP:net.NetdevHubPortOptions").
        - When `type` is `netmap`: The members of [`NetdevNetmapOptions`](qemu-qmp-ref.md#object-QMP-net.NetdevNetmapOptions "QMP:net.NetdevNetmapOptions").
        - When `type` is `af-xdp`: The members of [`NetdevAFXDPOptions`](qemu-qmp-ref.md#object-QMP-net.NetdevAFXDPOptions "QMP:net.NetdevAFXDPOptions").
        - When `type` is `vhost-user`: The members of [`NetdevVhostUserOptions`](qemu-qmp-ref.md#object-QMP-net.NetdevVhostUserOptions "QMP:net.NetdevVhostUserOptions").
        - When `type` is `vhost-vdpa`: The members of [`NetdevVhostVDPAOptions`](qemu-qmp-ref.md#object-QMP-net.NetdevVhostVDPAOptions "QMP:net.NetdevVhostVDPAOptions").
        - When `type` is `vmnet-host`: The members of [`NetdevVmnetHostOptions`](qemu-qmp-ref.md#object-QMP-net.NetdevVmnetHostOptions "QMP:net.NetdevVmnetHostOptions").
        - When `type` is `vmnet-shared`: The members of [`NetdevVmnetSharedOptions`](qemu-qmp-ref.md#object-QMP-net.NetdevVmnetSharedOptions "QMP:net.NetdevVmnetSharedOptions").
        - When `type` is `vmnet-bridged`: The members of [`NetdevVmnetBridgedOptions`](qemu-qmp-ref.md#object-QMP-net.NetdevVmnetBridgedOptions "QMP:net.NetdevVmnetBridgedOptions").

*Enum* RxState (Since: 1.6)
:   Packets receiving state

    Values:
    :   - **normal** – filter assigned packets according to the mac-table
        - **none** – don’t receive any assigned packet
        - **all** – receive all assigned packets

*Object* RxFilterInfo (Since: 1.6)
:   Rx-filter information for a NIC.

    Members:
    :   - **name** (`string`) – net client name
        - **promiscuous** (`boolean`) – whether promiscuous mode is enabled
        - **multicast** ([`RxState`](qemu-qmp-ref.md#enum-QMP-net.RxState "QMP:net.RxState")) – multicast receive state
        - **unicast** ([`RxState`](qemu-qmp-ref.md#enum-QMP-net.RxState "QMP:net.RxState")) – unicast receive state
        - **vlan** ([`RxState`](qemu-qmp-ref.md#enum-QMP-net.RxState "QMP:net.RxState")) – vlan receive state (Since 2.0)
        - **broadcast-allowed** (`boolean`) – whether to receive broadcast
        - **multicast-overflow** (`boolean`) – multicast table is overflowed or not
        - **unicast-overflow** (`boolean`) – unicast table is overflowed or not
        - **main-mac** (`string`) – the main macaddr string
        - **vlan-table** (`[``int``]`) – a list of active vlan id
        - **unicast-table** (`[``string``]`) – a list of unicast macaddr string
        - **multicast-table** (`[``string``]`) – a list of multicast macaddr string

*Command* query-rx-filter (Since: 1.6)
:   Return rx-filter information for all NICs (or for the given NIC).

    Arguments:
    :   - **name** (`string`, *optional*) – net client name

    Return:
    :   `[`[`RxFilterInfo`](qemu-qmp-ref.md#object-QMP-net.RxFilterInfo "QMP:net.RxFilterInfo")`]` – list of info for all NICs (or for the given NIC).

    Errors:
    :   - if the given `name` doesn’t exist
        - if the given NIC doesn’t support rx-filter querying
        - if the given net client isn’t a NIC

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "query-rx-filter", "arguments": { "name": "vnet0" } }
    > <- { "return": [
    >         {
    >             "promiscuous": true,
    >             "name": "vnet0",
    >             "main-mac": "52:54:00:12:34:56",
    >             "unicast": "normal",
    >             "vlan": "normal",
    >             "vlan-table": [
    >                 4,
    >                 0
    >             ],
    >             "unicast-table": [
    >             ],
    >             "multicast": "normal",
    >             "multicast-overflow": false,
    >             "unicast-overflow": false,
    >             "multicast-table": [
    >                 "01:00:5e:00:00:01",
    >                 "33:33:00:00:00:01",
    >                 "33:33:ff:12:34:56"
    >             ],
    >             "broadcast-allowed": false
    >         }
    >       ]
    >    }
    > ```

*Event* NIC_RX_FILTER_CHANGED (Since: 1.6)
:   Emitted once until the [`query-rx-filter`](qemu-qmp-ref.md#command-QMP-net.query-rx-filter "QMP:net.query-rx-filter") command is executed, the
    first event will always be emitted

    Members:
    :   - **name** (`string`, *optional*) – net client name
        - **path** (`string`) – device path

    > **Example::**
    >
    > ```QMP
    > <- { "event": "NIC_RX_FILTER_CHANGED",
    >      "data": { "name": "vnet0",
    >                "path": "/machine/peripheral/vnet0/virtio-backend" },
    >      "timestamp": { "seconds": 1368697518, "microseconds": 326866 } }
    > ```

*Object* AnnounceParameters (Since: 4.0)
:   Parameters for self-announce timers

    Members:
    :   - **initial** (`int`) – Initial delay (in ms) before sending the first GARP/RARP
          announcement
        - **max** (`int`) – Maximum delay (in ms) between GARP/RARP announcement packets
        - **rounds** (`int`) – Number of self-announcement attempts
        - **step** (`int`) – Delay increase (in ms) after each self-announcement attempt
        - **interfaces** (`[``string``]`, *optional*) – An optional list of interface names, which restricts
          the announcement to the listed interfaces. (Since 4.1)
        - **id** (`string`, *optional*) – A name to be used to identify an instance of announce-timers
          and to allow it to modified later. Not for use as part of the
          migration parameters. (Since 4.1)

*Command* announce-self (Since: 4.0)
:   Trigger generation of broadcast RARP frames to update network
    switches. This can be useful when network bonds fail-over the
    active slave.

    Arguments:
    :   - The members of [`AnnounceParameters`](qemu-qmp-ref.md#object-QMP-net.AnnounceParameters "QMP:net.AnnounceParameters").

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "announce-self",
    >      "arguments": {
    >          "initial": 50, "max": 550, "rounds": 10, "step": 50,
    >          "interfaces": ["vn2", "vn3"], "id": "bob" } }
    > <- { "return": {} }
    > ```

*Event* FAILOVER_NEGOTIATED (Since: 4.2)
:   Emitted when VIRTIO_NET_F_STANDBY was enabled during feature
    negotiation. Failover primary devices which were hidden (not
    hotplugged when requested) before will now be hotplugged by the
    virtio-net standby device.

    Members:
    :   - **device-id** (`string`) – QEMU device id of the unplugged device

    > **Example::**
    >
    > ```QMP
    > <- { "event": "FAILOVER_NEGOTIATED",
    >      "data": { "device-id": "net1" },
    >      "timestamp": { "seconds": 1368697518, "microseconds": 326866 } }
    > ```

*Event* NETDEV_STREAM_CONNECTED (Since: 7.2)
:   Emitted when the netdev stream backend is connected

    Members:
    :   - **netdev-id** (`string`) – QEMU netdev id that is connected
        - **addr** ([`SocketAddress`](qemu-qmp-ref.md#object-QMP-sockets.SocketAddress "QMP:sockets.SocketAddress")) – The destination address

    > **Example::**
    >
    > ```QMP
    > <- { "event": "NETDEV_STREAM_CONNECTED",
    >      "data": { "netdev-id": "netdev0",
    >                "addr": { "port": "47666", "ipv6": true,
    >                          "host": "::1", "type": "inet" } },
    >      "timestamp": { "seconds": 1666269863, "microseconds": 311222 } }
    > ```

    > **Example::**
    >
    > ```QMP
    > <- { "event": "NETDEV_STREAM_CONNECTED",
    >      "data": { "netdev-id": "netdev0",
    >                "addr": { "path": "/tmp/qemu0", "type": "unix" } },
    >      "timestamp": { "seconds": 1666269706, "microseconds": 413651 } }
    > ```

*Event* NETDEV_STREAM_DISCONNECTED (Since: 7.2)
:   Emitted when the netdev stream backend is disconnected

    Members:
    :   - **netdev-id** (`string`) – QEMU netdev id that is disconnected

    > **Example::**
    >
    > ```QMP
    > <- { "event": "NETDEV_STREAM_DISCONNECTED",
    >      "data": {"netdev-id": "netdev0"},
    >      "timestamp": {"seconds": 1663330937, "microseconds": 526695} }
    > ```

*Event* NETDEV_VHOST_USER_CONNECTED (Since: 10.0)
:   Emitted when the vhost-user chardev is connected

    Members:
    :   - **netdev-id** (`string`) – QEMU netdev id that is connected
        - **chardev-id** (`string`) – The character device id used by the QEMU netdev

    > **Example::**
    >
    > ```QMP
    > <- { "timestamp": {"seconds": 1739538638, "microseconds": 354181 },
    >      "event": "NETDEV_VHOST_USER_CONNECTED",
    >      "data": { "netdev-id": "netdev0", "chardev-id": "chr0" } }
    > ```

*Event* NETDEV_VHOST_USER_DISCONNECTED (Since: 10.0)
:   Emitted when the vhost-user chardev is disconnected

    Members:
    :   - **netdev-id** (`string`) – QEMU netdev id that is disconnected

    > **Example::**
    >
    > ```QMP
    > <- { "timestamp": { "seconds": 1739538634, "microseconds": 920450 },
    >      "event": "NETDEV_VHOST_USER_DISCONNECTED",
    >      "data": { "netdev-id": "netdev0" } }
    > ```

## [eBPF Objects](qemu-qmp-ref.md#id17)

eBPF object is an ELF binary that contains the eBPF program and eBPF
map description(BTF). Overall, eBPF object should contain the
program and enough metadata to create/load eBPF with libbpf. As the
eBPF maps/program should correspond to QEMU, the eBPF can’t be used
from different QEMU build.

Currently, there is a possible eBPF for receive-side scaling (RSS).

*Object* EbpfObject (Since: 9.0)
:   *Availability*: `CONFIG_EBPF`

    An eBPF ELF object.

    Members:
    :   - **object** (`string`) – the eBPF object encoded in base64

*Enum* EbpfProgramID (Since: 9.0)
:   *Availability*: `CONFIG_EBPF`

    The eBPF programs that can be gotten with [`request-ebpf`](qemu-qmp-ref.md#command-QMP-ebpf.request-ebpf "QMP:ebpf.request-ebpf").

    Values:
    :   - **rss** – Receive side scaling, technology that allows steering traffic
          between queues by calculation hash. Users may set up
          indirection table and hash/packet types configurations. Used
          with virtio-net.

*Command* request-ebpf (Since: 9.0)
:   *Availability*: `CONFIG_EBPF`

    Retrieve an eBPF object that can be loaded with libbpf. Management
    applications (e.g. libvirt) may load it and pass file descriptors to
    QEMU, so they can run running QEMU without BPF capabilities.

    Arguments:
    :   - **id** ([`EbpfProgramID`](qemu-qmp-ref.md#enum-QMP-ebpf.EbpfProgramID "QMP:ebpf.EbpfProgramID")) – The ID of the program to return.

    Return:
    :   [`EbpfObject`](qemu-qmp-ref.md#object-QMP-ebpf.EbpfObject "QMP:ebpf.EbpfObject") – eBPF object encoded in base64.

## [Rocker switch device](qemu-qmp-ref.md#id18)

*Object* RockerSwitch (Since: 2.4)
:   Rocker switch information.

    Members:
    :   - **name** (`string`) – switch name
        - **id** (`int`) – switch ID
        - **ports** (`int`) – number of front-panel ports

*Command* query-rocker (Since: 2.4)
:   Return rocker switch information.

    Arguments:
    :   - **name** (`string`) – switch name

    Return:
    :   [`RockerSwitch`](qemu-qmp-ref.md#object-QMP-rocker.RockerSwitch "QMP:rocker.RockerSwitch")

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "query-rocker", "arguments": { "name": "sw1" } }
    > <- { "return": {"name": "sw1", "ports": 2, "id": 1327446905938}}
    > ```

*Enum* RockerPortDuplex (Since: 2.4)
:   An enumeration of port duplex states.

    Values:
    :   - **half** – half duplex
        - **full** – full duplex

*Enum* RockerPortAutoneg (Since: 2.4)
:   An enumeration of port autoneg states.

    Values:
    :   - **off** – autoneg is off
        - **on** – autoneg is on

*Object* RockerPort (Since: 2.4)
:   Rocker switch port information.

    Members:
    :   - **name** (`string`) – port name
        - **enabled** (`boolean`) – port is enabled for I/O
        - **link-up** (`boolean`) – physical link is UP on port
        - **speed** (`int`) – port link speed in Mbps
        - **duplex** ([`RockerPortDuplex`](qemu-qmp-ref.md#enum-QMP-rocker.RockerPortDuplex "QMP:rocker.RockerPortDuplex")) – port link duplex
        - **autoneg** ([`RockerPortAutoneg`](qemu-qmp-ref.md#enum-QMP-rocker.RockerPortAutoneg "QMP:rocker.RockerPortAutoneg")) – port link autoneg

*Command* query-rocker-ports (Since: 2.4)
:   Return rocker switch port information.

    Arguments:
    :   - **name** (`string`) – port name

    Return:
    :   `[`[`RockerPort`](qemu-qmp-ref.md#object-QMP-rocker.RockerPort "QMP:rocker.RockerPort")`]`

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "query-rocker-ports", "arguments": { "name": "sw1" } }
    > <- { "return": [ {"duplex": "full", "enabled": true, "name": "sw1.1",
    >                   "autoneg": "off", "link-up": true, "speed": 10000},
    >                  {"duplex": "full", "enabled": true, "name": "sw1.2",
    >                   "autoneg": "off", "link-up": true, "speed": 10000}
    >    ]}
    > ```

*Object* RockerOfDpaFlowKey (Since: 2.4)
:   Rocker switch OF-DPA flow key

    Members:
    :   - **priority** (`int`) – key priority, 0 being lowest priority
        - **tbl-id** (`int`) – flow table ID
        - **in-pport** (`int`, *optional*) – physical input port
        - **tunnel-id** (`int`, *optional*) – tunnel ID
        - **vlan-id** (`int`, *optional*) – VLAN ID
        - **eth-type** (`int`, *optional*) – Ethernet header type
        - **eth-src** (`string`, *optional*) – Ethernet header source MAC address
        - **eth-dst** (`string`, *optional*) – Ethernet header destination MAC address
        - **ip-proto** (`int`, *optional*) – IP Header protocol field
        - **ip-tos** (`int`, *optional*) – IP header TOS field
        - **ip-dst** (`string`, *optional*) – IP header destination address

    > **Note:**
    >
    > Optional members may or may not appear in the flow key
    > depending if they’re relevant to the flow key.

*Object* RockerOfDpaFlowMask (Since: 2.4)
:   Rocker switch OF-DPA flow mask

    Members:
    :   - **in-pport** (`int`, *optional*) – physical input port
        - **tunnel-id** (`int`, *optional*) – tunnel ID
        - **vlan-id** (`int`, *optional*) – VLAN ID
        - **eth-src** (`string`, *optional*) – Ethernet header source MAC address
        - **eth-dst** (`string`, *optional*) – Ethernet header destination MAC address
        - **ip-proto** (`int`, *optional*) – IP Header protocol field
        - **ip-tos** (`int`, *optional*) – IP header TOS field

    > **Note:**
    >
    > Optional members may or may not appear in the flow mask
    > depending if they’re relevant to the flow mask.

*Object* RockerOfDpaFlowAction (Since: 2.4)
:   Rocker switch OF-DPA flow action

    Members:
    :   - **goto-tbl** (`int`, *optional*) – next table ID
        - **group-id** (`int`, *optional*) – group ID
        - **tunnel-lport** (`int`, *optional*) – tunnel logical port ID
        - **vlan-id** (`int`, *optional*) – VLAN ID
        - **new-vlan-id** (`int`, *optional*) – new VLAN ID
        - **out-pport** (`int`, *optional*) – physical output port

    > **Note:**
    >
    > Optional members may or may not appear in the flow action
    > depending if they’re relevant to the flow action.

*Object* RockerOfDpaFlow (Since: 2.4)
:   Rocker switch OF-DPA flow

    Members:
    :   - **cookie** (`int`) – flow unique cookie ID
        - **hits** (`int`) – count of matches (hits) on flow
        - **key** ([`RockerOfDpaFlowKey`](qemu-qmp-ref.md#object-QMP-rocker.RockerOfDpaFlowKey "QMP:rocker.RockerOfDpaFlowKey")) – flow key
        - **mask** ([`RockerOfDpaFlowMask`](qemu-qmp-ref.md#object-QMP-rocker.RockerOfDpaFlowMask "QMP:rocker.RockerOfDpaFlowMask")) – flow mask
        - **action** ([`RockerOfDpaFlowAction`](qemu-qmp-ref.md#object-QMP-rocker.RockerOfDpaFlowAction "QMP:rocker.RockerOfDpaFlowAction")) – flow action

*Command* query-rocker-of-dpa-flows (Since: 2.4)
:   Return rocker OF-DPA flow information.

    Arguments:
    :   - **name** (`string`) – switch name
        - **tbl-id** (`int`, *optional*) – flow table ID. If tbl-id is not specified, returns flow
          information for all tables.

    Return:
    :   `[`[`RockerOfDpaFlow`](qemu-qmp-ref.md#object-QMP-rocker.RockerOfDpaFlow "QMP:rocker.RockerOfDpaFlow")`]` – rocker OF-DPA flow information

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "query-rocker-of-dpa-flows",
    >      "arguments": { "name": "sw1" } }
    > <- { "return": [ {"key": {"in-pport": 0, "priority": 1, "tbl-id": 0},
    >                   "hits": 138,
    >                   "cookie": 0,
    >                   "action": {"goto-tbl": 10},
    >                   "mask": {"in-pport": 4294901760}
    >                  },
    >                  ...
    >    ]}
    > ```

*Object* RockerOfDpaGroup (Since: 2.4)
:   Rocker switch OF-DPA group

    Members:
    :   - **id** (`int`) – group unique ID
        - **type** (`int`) – group type
        - **vlan-id** (`int`, *optional*) – VLAN ID
        - **pport** (`int`, *optional*) – physical port number
        - **index** (`int`, *optional*) – group index, unique with group type
        - **out-pport** (`int`, *optional*) – output physical port number
        - **group-id** (`int`, *optional*) – next group ID
        - **set-vlan-id** (`int`, *optional*) – VLAN ID to set
        - **pop-vlan** (`int`, *optional*) – pop VLAN headr from packet
        - **group-ids** (`[``int``]`, *optional*) – list of next group IDs
        - **set-eth-src** (`string`, *optional*) – set source MAC address in Ethernet header
        - **set-eth-dst** (`string`, *optional*) – set destination MAC address in Ethernet header
        - **ttl-check** (`int`, *optional*) – perform TTL check

    > **Note:**
    >
    > Optional members may or may not appear in the group
    > depending if they’re relevant to the group type.

*Command* query-rocker-of-dpa-groups (Since: 2.4)
:   Return rocker OF-DPA group information.

    Arguments:
    :   - **name** (`string`) – switch name
        - **type** (`int`, *optional*) – group type. If type is not specified, returns group
          information for all group types.

    Return:
    :   `[`[`RockerOfDpaGroup`](qemu-qmp-ref.md#object-QMP-rocker.RockerOfDpaGroup "QMP:rocker.RockerOfDpaGroup")`]` – rocker OF-DPA group information

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "query-rocker-of-dpa-groups",
    >      "arguments": { "name": "sw1" } }
    > <- { "return": [ {"type": 0, "out-pport": 2,
    >                   "pport": 2, "vlan-id": 3841,
    >                   "pop-vlan": 1, "id": 251723778},
    >                  {"type": 0, "out-pport": 0,
    >                   "pport": 0, "vlan-id": 3841,
    >                   "pop-vlan": 1, "id": 251723776},
    >                  {"type": 0, "out-pport": 1,
    >                   "pport": 1, "vlan-id": 3840,
    >                   "pop-vlan": 1, "id": 251658241},
    >                  {"type": 0, "out-pport": 0,
    >                   "pport": 0, "vlan-id": 3840,
    >                   "pop-vlan": 1, "id": 251658240}
    >    ]}
    > ```

## [TPM (trusted platform module) devices](qemu-qmp-ref.md#id19)

*Enum* TpmModel (Since: 1.5)
:   *Availability*: `CONFIG_TPM`

    An enumeration of TPM models

    Values:
    :   - **tpm-tis** – TPM TIS model
        - **tpm-crb** – TPM CRB model (since 2.12)
        - **tpm-spapr** – TPM SPAPR model (since 5.0)

*Command* query-tpm-models (Since: 1.5)
:   *Availability*: `CONFIG_TPM`

    Return a list of supported TPM models

    Return:
    :   `[`[`TpmModel`](qemu-qmp-ref.md#enum-QMP-tpm.TpmModel "QMP:tpm.TpmModel")`]`

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "query-tpm-models" }
    > <- { "return": [ "tpm-tis", "tpm-crb", "tpm-spapr" ] }
    > ```

*Enum* TpmType (Since: 1.5)
:   *Availability*: `CONFIG_TPM`

    An enumeration of TPM types

    Values:
    :   - **passthrough** – TPM passthrough type
        - **emulator** – Software Emulator TPM type (since 2.11)

*Command* query-tpm-types (Since: 1.5)
:   *Availability*: `CONFIG_TPM`

    Return a list of supported TPM types

    Return:
    :   `[`[`TpmType`](qemu-qmp-ref.md#enum-QMP-tpm.TpmType "QMP:tpm.TpmType")`]`

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "query-tpm-types" }
    > <- { "return": [ "passthrough", "emulator" ] }
    > ```

*Object* TPMPassthroughOptions (Since: 1.5)
:   *Availability*: `CONFIG_TPM`

    Information about the TPM passthrough type

    Members:
    :   - **path** (`string`, *optional*) – string describing the path used for accessing the TPM device
        - **cancel-path** (`string`, *optional*) – string showing the TPM’s sysfs cancel file for
          cancellation of TPM commands while they are executing

*Object* TPMEmulatorOptions (Since: 2.11)
:   *Availability*: `CONFIG_TPM`

    Information about the TPM emulator type

    Members:
    :   - **chardev** (`string`) – Name of a unix socket chardev

*Object* TPMPassthroughOptionsWrapper (Since: 1.5)
:   *Availability*: `CONFIG_TPM`

    Members:
    :   - **data** ([`TPMPassthroughOptions`](qemu-qmp-ref.md#object-QMP-tpm.TPMPassthroughOptions "QMP:tpm.TPMPassthroughOptions")) – Information about the TPM passthrough type

*Object* TPMEmulatorOptionsWrapper (Since: 2.11)
:   *Availability*: `CONFIG_TPM`

    Members:
    :   - **data** ([`TPMEmulatorOptions`](qemu-qmp-ref.md#object-QMP-tpm.TPMEmulatorOptions "QMP:tpm.TPMEmulatorOptions")) – Information about the TPM emulator type

*Object* TpmTypeOptions (Since: 1.5)
:   *Availability*: `CONFIG_TPM`

    A union referencing different TPM backend types’ configuration
    options

    Members:
    :   - **type** ([`TpmType`](qemu-qmp-ref.md#enum-QMP-tpm.TpmType "QMP:tpm.TpmType")) –

          - ‘passthrough’ The configuration options for the TPM
            passthrough type
          - ’emulator’ The configuration options for TPM emulator backend
            type
        - When `type` is `passthrough`: The members of [`TPMPassthroughOptionsWrapper`](qemu-qmp-ref.md#object-QMP-tpm.TPMPassthroughOptionsWrapper "QMP:tpm.TPMPassthroughOptionsWrapper").
        - When `type` is `emulator`: The members of [`TPMEmulatorOptionsWrapper`](qemu-qmp-ref.md#object-QMP-tpm.TPMEmulatorOptionsWrapper "QMP:tpm.TPMEmulatorOptionsWrapper").

*Object* TPMInfo (Since: 1.5)
:   *Availability*: `CONFIG_TPM`

    Information about the TPM

    Members:
    :   - **id** (`string`) – The Id of the TPM
        - **model** ([`TpmModel`](qemu-qmp-ref.md#enum-QMP-tpm.TpmModel "QMP:tpm.TpmModel")) – The TPM frontend model
        - **options** ([`TpmTypeOptions`](qemu-qmp-ref.md#object-QMP-tpm.TpmTypeOptions "QMP:tpm.TpmTypeOptions")) – The TPM (backend) type configuration options

*Command* query-tpm (Since: 1.5)
:   *Availability*: `CONFIG_TPM`

    Return information about the TPM device

    Return:
    :   `[`[`TPMInfo`](qemu-qmp-ref.md#object-QMP-tpm.TPMInfo "QMP:tpm.TPMInfo")`]`

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "query-tpm" }
    > <- { "return":
    >      [
    >        { "model": "tpm-tis",
    >          "options":
    >            { "type": "passthrough",
    >              "data":
    >                { "cancel-path": "/sys/class/misc/tpm0/device/cancel",
    >                  "path": "/dev/tpm0"
    >                }
    >            },
    >          "id": "tpm0"
    >        }
    >      ]
    >    }
    > ```

## [Remote desktop](qemu-qmp-ref.md#id20)

*Enum* DisplayProtocol (Since: 7.0)
:   Display protocols which support changing password options.

    Values:
    :   - **vnc** – Not documented
        - **spice** – Not documented

*Enum* SetPasswordAction (Since: 7.0)
:   An action to take on changing a password on a connection with active
    clients.

    Values:
    :   - **keep** – maintain existing clients
        - **fail** – fail the command if clients are connected
        - **disconnect** – disconnect existing clients

*Object* SetPasswordOptions (Since: 7.0)
:   Options for [`set_password`](qemu-qmp-ref.md#command-QMP-ui.set_password "QMP:ui.set_password").

    Members:
    :   - **protocol** ([`DisplayProtocol`](qemu-qmp-ref.md#enum-QMP-ui.DisplayProtocol "QMP:ui.DisplayProtocol")) –

          - ‘vnc’ to modify the VNC server password
          - ’spice’ to modify the Spice server password
        - **password** (`string`) – the new password
        - **connected** ([`SetPasswordAction`](qemu-qmp-ref.md#enum-QMP-ui.SetPasswordAction "QMP:ui.SetPasswordAction"), *optional*) – How to handle existing clients when changing the
          password. If nothing is specified, defaults to ‘keep’. For
          VNC, only ‘keep’ is currently implemented.
        - When `protocol` is `vnc`: The members of [`SetPasswordOptionsVnc`](qemu-qmp-ref.md#object-QMP-ui.SetPasswordOptionsVnc "QMP:ui.SetPasswordOptionsVnc").

*Object* SetPasswordOptionsVnc (Since: 7.0)
:   Options for [`set_password`](qemu-qmp-ref.md#command-QMP-ui.set_password "QMP:ui.set_password") specific to the VNC protocol.

    Members:
    :   - **display** (`string`, *optional*) – The id of the display where the password should be
          changed. Defaults to the first.

*Command* set_password (Since: 0.14)
:   Set the password of a remote display server.

    Arguments:
    :   - The members of [`SetPasswordOptions`](qemu-qmp-ref.md#object-QMP-ui.SetPasswordOptions "QMP:ui.SetPasswordOptions").

    Errors:
    :   - If Spice is not enabled, DeviceNotFound

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "set_password", "arguments": { "protocol": "vnc",
    >                                                "password": "secret" } }
    > <- { "return": {} }
    > ```

*Object* ExpirePasswordOptions (Since: 7.0)
:   General options for [`expire_password`](qemu-qmp-ref.md#command-QMP-ui.expire_password "QMP:ui.expire_password").

    Members:
    :   - **protocol** ([`DisplayProtocol`](qemu-qmp-ref.md#enum-QMP-ui.DisplayProtocol "QMP:ui.DisplayProtocol")) –

          - ‘vnc’ to modify the VNC server expiration
          - ’spice’ to modify the Spice server expiration
        - **time** (`string`) –

          when to expire the password.

          - ’now’ to expire the password immediately
          - ’never’ to cancel password expiration
          - ’+INT’ where INT is the number of seconds from now (integer)
          - ’INT’ where INT is the absolute time in seconds
        - When `protocol` is `vnc`: The members of [`ExpirePasswordOptionsVnc`](qemu-qmp-ref.md#object-QMP-ui.ExpirePasswordOptionsVnc "QMP:ui.ExpirePasswordOptionsVnc").

    > **Note:**
    >
    > Time is relative to the server and currently there is no
    > way to coordinate server time with client time. It is not
    > recommended to use the absolute time version of the `time`
    > parameter unless you’re sure you are on the same machine as the
    > QEMU instance.

*Object* ExpirePasswordOptionsVnc (Since: 7.0)
:   Options for [`expire_password`](qemu-qmp-ref.md#command-QMP-ui.expire_password "QMP:ui.expire_password") specific to the VNC protocol.

    Members:
    :   - **display** (`string`, *optional*) – The id of the display where the expiration should be
          changed. Defaults to the first.

*Command* expire_password (Since: 0.14)
:   Expire the password of a remote display server.

    Arguments:
    :   - The members of [`ExpirePasswordOptions`](qemu-qmp-ref.md#object-QMP-ui.ExpirePasswordOptions "QMP:ui.ExpirePasswordOptions").

    Errors:
    :   - If `protocol` is ‘spice’ and Spice is not active,
          DeviceNotFound

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "expire_password", "arguments": { "protocol": "vnc",
    >                                                   "time": "+60" } }
    > <- { "return": {} }
    > ```

*Enum* ImageFormat (Since: 7.1)
:   Supported image format types.

    Values:
    :   - **png** – PNG format
        - **ppm** – PPM format

*Command* screendump (Since: 0.14)
:   *Availability*: `CONFIG_PIXMAN`

    Capture the contents of a screen and write it to a file.

    Arguments:
    :   - **filename** (`string`) – the path of a new file to store the image
        - **device** (`string`, *optional*) – ID of the display device that should be dumped. If this
          parameter is missing, the primary display will be used.
          (Since 2.12)
        - **head** (`int`, *optional*) – head to use in case the device supports multiple heads. If
          this parameter is missing, head #0 will be used. Also note that
          the head can only be specified in conjunction with the device
          ID. (Since 2.12)
        - **format** ([`ImageFormat`](qemu-qmp-ref.md#enum-QMP-ui.ImageFormat "QMP:ui.ImageFormat"), *optional*) – image format for [`screendump`](qemu-qmp-ref.md#command-QMP-ui.screendump "QMP:ui.screendump"). (default: ppm) (Since 7.1)

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "screendump",
    >      "arguments": { "filename": "/tmp/image" } }
    > <- { "return": {} }
    > ```

### [Spice](qemu-qmp-ref.md#id21)

*Object* SpiceBasicInfo (Since: 2.1)
:   *Availability*: `CONFIG_SPICE`

    The basic information for SPICE network connection

    Members:
    :   - **host** (`string`) – IP address
        - **port** (`string`) – port number
        - **family** ([`NetworkAddressFamily`](qemu-qmp-ref.md#enum-QMP-sockets.NetworkAddressFamily "QMP:sockets.NetworkAddressFamily")) – address family

*Object* SpiceServerInfo (Since: 2.1)
:   *Availability*: `CONFIG_SPICE`

    Information about a SPICE server

    Members:
    :   - **auth** (`string`, *optional*) – authentication method
        - The members of [`SpiceBasicInfo`](qemu-qmp-ref.md#object-QMP-ui.SpiceBasicInfo "QMP:ui.SpiceBasicInfo").

*Object* SpiceChannel (Since: 0.14)
:   *Availability*: `CONFIG_SPICE`

    Information about a SPICE client channel.

    Members:
    :   - **connection-id** (`int`) – SPICE connection id number. All channels with the
          same id belong to the same SPICE session.
        - **channel-type** (`int`) – SPICE channel type number. “1” is the main control
          channel, filter for this one if you want to track spice sessions
          only
        - **channel-id** (`int`) – SPICE channel ID number. Usually “0”, might be
          different when multiple channels of the same type exist, such as
          multiple display channels in a multihead setup
        - **tls** (`boolean`) – true if the channel is encrypted, false otherwise.
        - The members of [`SpiceBasicInfo`](qemu-qmp-ref.md#object-QMP-ui.SpiceBasicInfo "QMP:ui.SpiceBasicInfo").

*Enum* SpiceQueryMouseMode (Since: 1.1)
:   *Availability*: `CONFIG_SPICE`

    An enumeration of Spice mouse states.

    Values:
    :   - **client** – Mouse cursor position is determined by the client.
        - **server** – Mouse cursor position is determined by the server.
        - **unknown** – No information is available about mouse mode used by the
          spice server.

*Object* SpiceInfo (Since: 0.14)
:   *Availability*: `CONFIG_SPICE`

    Information about the SPICE session.

    Members:
    :   - **enabled** (`boolean`) – true if the SPICE server is enabled, false otherwise
        - **migrated** (`boolean`) – true if the last guest migration completed and spice
          migration had completed as well, false otherwise (since 1.4)
        - **host** (`string`, *optional*) – The hostname the SPICE server is bound to. This depends on
          the name resolution on the host and may be an IP address.
        - **port** (`int`, *optional*) – The SPICE server’s port number.
        - **compiled-version** (`string`, *optional*) – SPICE server version.
        - **tls-port** (`int`, *optional*) – The SPICE server’s TLS port number.
        - **auth** (`string`, *optional*) –

          the current authentication type used by the server

          - ’none’ if no authentication is being used
          - ’spice’ uses SASL or direct TLS authentication, depending on
            command line options
        - **mouse-mode** ([`SpiceQueryMouseMode`](qemu-qmp-ref.md#enum-QMP-ui.SpiceQueryMouseMode "QMP:ui.SpiceQueryMouseMode")) – The mode in which the mouse cursor is displayed
          currently. Can be determined by the client or the server, or
          unknown if spice server doesn’t provide this information.
          (since: 1.1)
        - **channels** (`[`[`SpiceChannel`](qemu-qmp-ref.md#object-QMP-ui.SpiceChannel "QMP:ui.SpiceChannel")`]`, *optional*) – a list of [`SpiceChannel`](qemu-qmp-ref.md#object-QMP-ui.SpiceChannel "QMP:ui.SpiceChannel") for each active spice channel

*Command* query-spice (Since: 0.14)
:   *Availability*: `CONFIG_SPICE`

    Return information about the current SPICE server

    Return:
    :   [`SpiceInfo`](qemu-qmp-ref.md#object-QMP-ui.SpiceInfo "QMP:ui.SpiceInfo")

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "query-spice" }
    > <- { "return": {
    >          "enabled": true,
    >          "auth": "spice",
    >          "port": 5920,
    >          "migrated":false,
    >          "tls-port": 5921,
    >          "host": "0.0.0.0",
    >          "mouse-mode":"client",
    >          "channels": [
    >             {
    >                "port": "54924",
    >                "family": "ipv4",
    >                "channel-type": 1,
    >                "connection-id": 1804289383,
    >                "host": "127.0.0.1",
    >                "channel-id": 0,
    >                "tls": true
    >             },
    >             {
    >                "port": "36710",
    >                "family": "ipv4",
    >                "channel-type": 4,
    >                "connection-id": 1804289383,
    >                "host": "127.0.0.1",
    >                "channel-id": 0,
    >                "tls": false
    >             },
    >             ...
    >          ]
    >       }
    >    }
    > ```

*Event* SPICE_CONNECTED (Since: 0.14)
:   *Availability*: `CONFIG_SPICE`

    Emitted when a SPICE client establishes a connection

    Members:
    :   - **server** ([`SpiceBasicInfo`](qemu-qmp-ref.md#object-QMP-ui.SpiceBasicInfo "QMP:ui.SpiceBasicInfo")) – server information
        - **client** ([`SpiceBasicInfo`](qemu-qmp-ref.md#object-QMP-ui.SpiceBasicInfo "QMP:ui.SpiceBasicInfo")) – client information

    > **Example::**
    >
    > ```QMP
    > <- { "timestamp": {"seconds": 1290688046, "microseconds": 388707},
    >      "event": "SPICE_CONNECTED",
    >      "data": {
    >        "server": { "port": "5920", "family": "ipv4", "host": "127.0.0.1"},
    >        "client": {"port": "52873", "family": "ipv4", "host": "127.0.0.1"}
    >    }}
    > ```

*Event* SPICE_INITIALIZED (Since: 0.14)
:   *Availability*: `CONFIG_SPICE`

    Emitted after initial handshake and authentication takes place (if
    any) and the SPICE channel is up and running

    Members:
    :   - **server** ([`SpiceServerInfo`](qemu-qmp-ref.md#object-QMP-ui.SpiceServerInfo "QMP:ui.SpiceServerInfo")) – server information
        - **client** ([`SpiceChannel`](qemu-qmp-ref.md#object-QMP-ui.SpiceChannel "QMP:ui.SpiceChannel")) – client information

    > **Example::**
    >
    > ```QMP
    > <- { "timestamp": {"seconds": 1290688046, "microseconds": 417172},
    >      "event": "SPICE_INITIALIZED",
    >      "data": {"server": {"auth": "spice", "port": "5921",
    >                          "family": "ipv4", "host": "127.0.0.1"},
    >               "client": {"port": "49004", "family": "ipv4", "channel-type": 3,
    >                          "connection-id": 1804289383, "host": "127.0.0.1",
    >                          "channel-id": 0, "tls": true}
    >    }}
    > ```

*Event* SPICE_DISCONNECTED (Since: 0.14)
:   *Availability*: `CONFIG_SPICE`

    Emitted when the SPICE connection is closed

    Members:
    :   - **server** ([`SpiceBasicInfo`](qemu-qmp-ref.md#object-QMP-ui.SpiceBasicInfo "QMP:ui.SpiceBasicInfo")) – server information
        - **client** ([`SpiceBasicInfo`](qemu-qmp-ref.md#object-QMP-ui.SpiceBasicInfo "QMP:ui.SpiceBasicInfo")) – client information

    > **Example::**
    >
    > ```QMP
    > <- { "timestamp": {"seconds": 1290688046, "microseconds": 388707},
    >      "event": "SPICE_DISCONNECTED",
    >      "data": {
    >        "server": { "port": "5920", "family": "ipv4", "host": "127.0.0.1"},
    >        "client": {"port": "52873", "family": "ipv4", "host": "127.0.0.1"}
    >    }}
    > ```

*Event* SPICE_MIGRATE_COMPLETED (Since: 1.3)
:   *Availability*: `CONFIG_SPICE`

    Emitted when SPICE migration has completed

    > **Example::**
    >
    > ```QMP
    > <- { "timestamp": {"seconds": 1290688046, "microseconds": 417172},
    >      "event": "SPICE_MIGRATE_COMPLETED" }
    > ```

### [VNC](qemu-qmp-ref.md#id22)

*Object* VncBasicInfo (Since: 2.1)
:   *Availability*: `CONFIG_VNC`

    The basic information for vnc network connection

    Members:
    :   - **host** (`string`) – IP address
        - **service** (`string`) – The service name of the vnc port. This may depend on the
          host system’s service database so symbolic names should not be
          relied on.
        - **family** ([`NetworkAddressFamily`](qemu-qmp-ref.md#enum-QMP-sockets.NetworkAddressFamily "QMP:sockets.NetworkAddressFamily")) – address family
        - **websocket** (`boolean`) – true in case the socket is a websocket (since 2.3).

*Object* VncServerInfo (Since: 2.1)
:   *Availability*: `CONFIG_VNC`

    The network connection information for server

    Members:
    :   - **auth** (`string`, *optional*) – authentication method used for the plain (non-websocket) VNC
          server
        - The members of [`VncBasicInfo`](qemu-qmp-ref.md#object-QMP-ui.VncBasicInfo "QMP:ui.VncBasicInfo").

*Object* VncClientInfo (Since: 0.14)
:   *Availability*: `CONFIG_VNC`

    Information about a connected VNC client.

    Members:
    :   - **x509_dname** (`string`, *optional*) – If x509 authentication is in use, the Distinguished
          Name of the client.
        - **sasl_username** (`string`, *optional*) – If SASL authentication is in use, the SASL username
          used for authentication.
        - The members of [`VncBasicInfo`](qemu-qmp-ref.md#object-QMP-ui.VncBasicInfo "QMP:ui.VncBasicInfo").

*Object* VncInfo (Since: 0.14)
:   *Availability*: `CONFIG_VNC`

    Information about the VNC session.

    Members:
    :   - **enabled** (`boolean`) – true if the VNC server is enabled, false otherwise
        - **host** (`string`, *optional*) – The hostname the VNC server is bound to. This depends on the
          name resolution on the host and may be an IP address.
        - **family** ([`NetworkAddressFamily`](qemu-qmp-ref.md#enum-QMP-sockets.NetworkAddressFamily "QMP:sockets.NetworkAddressFamily"), *optional*) –

          - ‘ipv6’ if the host is listening for IPv6 connections
          - ’ipv4’ if the host is listening for IPv4 connections
          - ’unix’ if the host is listening on a unix domain socket
          - ’unknown’ otherwise
        - **service** (`string`, *optional*) – The service name of the server’s port. This may depends
          on the host system’s service database so symbolic names should
          not be relied on.
        - **auth** (`string`, *optional*) –

          the current authentication type used by the server

          - ’none’ if no authentication is being used
          - ’vnc’ if VNC authentication is being used
          - ’vencrypt+plain’ if VEncrypt is used with plain text
            authentication
          - ’vencrypt+tls+none’ if VEncrypt is used with TLS and no
            authentication
          - ’vencrypt+tls+vnc’ if VEncrypt is used with TLS and VNC
            authentication
          - ’vencrypt+tls+plain’ if VEncrypt is used with TLS and plain
            text auth
          - ’vencrypt+x509+none’ if VEncrypt is used with x509 and no auth
          - ’vencrypt+x509+vnc’ if VEncrypt is used with x509 and VNC auth
          - ’vencrypt+x509+plain’ if VEncrypt is used with x509 and plain
            text auth
          - ’vencrypt+tls+sasl’ if VEncrypt is used with TLS and SASL auth
          - ’vencrypt+x509+sasl’ if VEncrypt is used with x509 and SASL
            auth
        - **clients** (`[`[`VncClientInfo`](qemu-qmp-ref.md#object-QMP-ui.VncClientInfo "QMP:ui.VncClientInfo")`]`, *optional*) – a list of [`VncClientInfo`](qemu-qmp-ref.md#object-QMP-ui.VncClientInfo "QMP:ui.VncClientInfo") of all currently connected
          clients

*Enum* VncPrimaryAuth (Since: 2.3)
:   *Availability*: `CONFIG_VNC`

    vnc primary authentication method.

    Values:
    :   - **none** – Not documented
        - **vnc** – Not documented
        - **ra2** – Not documented
        - **ra2ne** – Not documented
        - **tight** – Not documented
        - **ultra** – Not documented
        - **tls** – Not documented
        - **vencrypt** – Not documented
        - **sasl** – Not documented

*Enum* VncVencryptSubAuth (Since: 2.3)
:   *Availability*: `CONFIG_VNC`

    vnc sub authentication method with vencrypt.

    Values:
    :   - **plain** – Not documented
        - **tls-none** – Not documented
        - **x509-none** – Not documented
        - **tls-vnc** – Not documented
        - **x509-vnc** – Not documented
        - **tls-plain** – Not documented
        - **x509-plain** – Not documented
        - **tls-sasl** – Not documented
        - **x509-sasl** – Not documented

*Object* VncServerInfo2 (Since: 2.9)
:   *Availability*: `CONFIG_VNC`

    The network connection information for server

    Members:
    :   - **auth** ([`VncPrimaryAuth`](qemu-qmp-ref.md#enum-QMP-ui.VncPrimaryAuth "QMP:ui.VncPrimaryAuth")) – The current authentication type used by the servers
        - **vencrypt** ([`VncVencryptSubAuth`](qemu-qmp-ref.md#enum-QMP-ui.VncVencryptSubAuth "QMP:ui.VncVencryptSubAuth"), *optional*) – The vencrypt sub authentication type used by the servers,
          only specified in case auth == vencrypt.
        - The members of [`VncBasicInfo`](qemu-qmp-ref.md#object-QMP-ui.VncBasicInfo "QMP:ui.VncBasicInfo").

*Object* VncInfo2 (Since: 2.3)
:   *Availability*: `CONFIG_VNC`

    Information about a vnc server

    Members:
    :   - **id** (`string`) – vnc server name.
        - **server** (`[`[`VncServerInfo2`](qemu-qmp-ref.md#object-QMP-ui.VncServerInfo2 "QMP:ui.VncServerInfo2")`]`) – A list of [`VncBasicInfo`](qemu-qmp-ref.md#object-QMP-ui.VncBasicInfo "QMP:ui.VncBasicInfo") describing all listening sockets.
          The list can be empty (in case the vnc server is disabled). It
          also may have multiple entries: normal + websocket, possibly
          also ipv4 + ipv6 in the future.
        - **clients** (`[`[`VncClientInfo`](qemu-qmp-ref.md#object-QMP-ui.VncClientInfo "QMP:ui.VncClientInfo")`]`) – A list of [`VncClientInfo`](qemu-qmp-ref.md#object-QMP-ui.VncClientInfo "QMP:ui.VncClientInfo") of all currently connected
          clients. The list can be empty, for obvious reasons.
        - **auth** ([`VncPrimaryAuth`](qemu-qmp-ref.md#enum-QMP-ui.VncPrimaryAuth "QMP:ui.VncPrimaryAuth")) – The current authentication type used by the non-websockets
          servers
        - **vencrypt** ([`VncVencryptSubAuth`](qemu-qmp-ref.md#enum-QMP-ui.VncVencryptSubAuth "QMP:ui.VncVencryptSubAuth"), *optional*) – The vencrypt authentication type used by the servers,
          only specified in case auth == vencrypt.
        - **display** (`string`, *optional*) – The display device the vnc server is linked to.

*Command* query-vnc (Since: 0.14)
:   *Availability*: `CONFIG_VNC`

    Return information about the current VNC server

    Return:
    :   [`VncInfo`](qemu-qmp-ref.md#object-QMP-ui.VncInfo "QMP:ui.VncInfo")

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "query-vnc" }
    > <- { "return": {
    >          "enabled":true,
    >          "host":"0.0.0.0",
    >          "service":"50402",
    >          "auth":"vnc",
    >          "family":"ipv4",
    >          "clients":[
    >             {
    >                "host":"127.0.0.1",
    >                "service":"50401",
    >                "family":"ipv4",
    >                "websocket":false
    >             }
    >          ]
    >       }
    >    }
    > ```

*Command* query-vnc-servers (Since: 2.3)
:   *Availability*: `CONFIG_VNC`

    Return a list of vnc servers. The list can be empty.

    Return:
    :   `[`[`VncInfo2`](qemu-qmp-ref.md#object-QMP-ui.VncInfo2 "QMP:ui.VncInfo2")`]`

*Command* change-vnc-password (Since: 1.1)
:   *Availability*: `CONFIG_VNC`

    Change the VNC server password.

    Arguments:
    :   - **password** (`string`) – the new password to use with VNC authentication

    > **Note:**
    >
    > An empty password in this command will set the password to
    > the empty string. Existing clients are unaffected by executing
    > this command.

*Event* VNC_CONNECTED (Since: 0.13)
:   *Availability*: `CONFIG_VNC`

    Emitted when a VNC client establishes a connection

    Members:
    :   - **server** ([`VncServerInfo`](qemu-qmp-ref.md#object-QMP-ui.VncServerInfo "QMP:ui.VncServerInfo")) – server information
        - **client** ([`VncBasicInfo`](qemu-qmp-ref.md#object-QMP-ui.VncBasicInfo "QMP:ui.VncBasicInfo")) – client information

    > **Note:**
    >
    > This event is emitted before any authentication takes
    > place, thus the authentication ID is not provided.

    > **Example::**
    >
    > ```QMP
    > <- { "event": "VNC_CONNECTED",
    >      "data": {
    >            "server": { "auth": "sasl", "family": "ipv4", "websocket": false,
    >                        "service": "5901", "host": "0.0.0.0" },
    >            "client": { "family": "ipv4", "service": "58425",
    >                        "host": "127.0.0.1", "websocket": false } },
    >      "timestamp": { "seconds": 1262976601, "microseconds": 975795 } }
    > ```

*Event* VNC_INITIALIZED (Since: 0.13)
:   *Availability*: `CONFIG_VNC`

    Emitted after authentication takes place (if any) and the VNC
    session is made active

    Members:
    :   - **server** ([`VncServerInfo`](qemu-qmp-ref.md#object-QMP-ui.VncServerInfo "QMP:ui.VncServerInfo")) – server information
        - **client** ([`VncClientInfo`](qemu-qmp-ref.md#object-QMP-ui.VncClientInfo "QMP:ui.VncClientInfo")) – client information

    > **Example::**
    >
    > ```QMP
    > <-  { "event": "VNC_INITIALIZED",
    >       "data": {
    >            "server": { "auth": "sasl", "family": "ipv4", "websocket": false,
    >                        "service": "5901", "host": "0.0.0.0"},
    >            "client": { "family": "ipv4", "service": "46089", "websocket": false,
    >                        "host": "127.0.0.1", "sasl_username": "luiz" } },
    >       "timestamp": { "seconds": 1263475302, "microseconds": 150772 } }
    > ```

*Event* VNC_DISCONNECTED (Since: 0.13)
:   *Availability*: `CONFIG_VNC`

    Emitted when the connection is closed

    Members:
    :   - **server** ([`VncServerInfo`](qemu-qmp-ref.md#object-QMP-ui.VncServerInfo "QMP:ui.VncServerInfo")) – server information
        - **client** ([`VncClientInfo`](qemu-qmp-ref.md#object-QMP-ui.VncClientInfo "QMP:ui.VncClientInfo")) – client information

    > **Example::**
    >
    > ```QMP
    > <- { "event": "VNC_DISCONNECTED",
    >      "data": {
    >            "server": { "auth": "sasl", "family": "ipv4", "websocket": false,
    >                        "service": "5901", "host": "0.0.0.0" },
    >            "client": { "family": "ipv4", "service": "58425", "websocket": false,
    >                        "host": "127.0.0.1", "sasl_username": "luiz" } },
    >      "timestamp": { "seconds": 1262976601, "microseconds": 975795 } }
    > ```

## [Input](qemu-qmp-ref.md#id23)

*Object* MouseInfo (Since: 0.14)
:   Information about a mouse device.

    Members:
    :   - **name** (`string`) – the name of the mouse device
        - **index** (`int`) – the index of the mouse device
        - **current** (`boolean`) – true if this device is currently receiving mouse events
        - **absolute** (`boolean`) – true if this device supports absolute coordinates as
          input

*Command* query-mice (Since: 0.14)
:   Return information about each active mouse device

    Return:
    :   `[`[`MouseInfo`](qemu-qmp-ref.md#object-QMP-ui.MouseInfo "QMP:ui.MouseInfo")`]` – a list of info for each device

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "query-mice" }
    > <- { "return": [
    >          {
    >             "name":"QEMU Microsoft Mouse",
    >             "index":0,
    >             "current":false,
    >             "absolute":false
    >          },
    >          {
    >             "name":"QEMU PS/2 Mouse",
    >             "index":1,
    >             "current":true,
    >             "absolute":true
    >          }
    >       ]
    >    }
    > ```

*Enum* QKeyCode (Since: 1.3)
:   An enumeration of key name.

    This is used by the [`send-key`](qemu-qmp-ref.md#command-QMP-ui.send-key "QMP:ui.send-key") command.

    Values:
    :   - **unmapped** – since 2.0
        - **pause** – since 2.0
        - **ro** – since 2.4
        - **kp_comma** – since 2.4
        - **kp_equals** – since 2.6
        - **power** – since 2.6
        - **hiragana** – since 2.9
        - **henkan** – since 2.9
        - **yen** – since 2.9
        - **sleep** – since 2.10
        - **wake** – since 2.10
        - **audionext** – since 2.10
        - **audioprev** – since 2.10
        - **audiostop** – since 2.10
        - **audioplay** – since 2.10
        - **audiomute** – since 2.10
        - **volumeup** – since 2.10
        - **volumedown** – since 2.10
        - **mediaselect** – since 2.10
        - **mail** – since 2.10
        - **calculator** – since 2.10
        - **computer** – since 2.10
        - **ac_home** – since 2.10
        - **ac_back** – since 2.10
        - **ac_forward** – since 2.10
        - **ac_refresh** – since 2.10
        - **ac_bookmarks** – since 2.10
        - **muhenkan** – since 2.12
        - **katakanahiragana** – since 2.12
        - **lang1** – since 6.1
        - **lang2** – since 6.1
        - **f13** – since 8.0
        - **f14** – since 8.0
        - **f15** – since 8.0
        - **f16** – since 8.0
        - **f17** – since 8.0
        - **f18** – since 8.0
        - **f19** – since 8.0
        - **f20** – since 8.0
        - **f21** – since 8.0
        - **f22** – since 8.0
        - **f23** – since 8.0
        - **f24** – since 8.0
        - **shift** – Not documented
        - **shift_r** – Not documented
        - **alt** – Not documented
        - **alt_r** – Not documented
        - **ctrl** – Not documented
        - **ctrl_r** – Not documented
        - **menu** – Not documented
        - **esc** – Not documented
        - **1** – Not documented
        - **2** – Not documented
        - **3** – Not documented
        - **4** – Not documented
        - **5** – Not documented
        - **6** – Not documented
        - **7** – Not documented
        - **8** – Not documented
        - **9** – Not documented
        - **0** – Not documented
        - **minus** – Not documented
        - **equal** – Not documented
        - **backspace** – Not documented
        - **tab** – Not documented
        - **q** – Not documented
        - **w** – Not documented
        - **e** – Not documented
        - **r** – Not documented
        - **t** – Not documented
        - **y** – Not documented
        - **u** – Not documented
        - **i** – Not documented
        - **o** – Not documented
        - **p** – Not documented
        - **bracket_left** – Not documented
        - **bracket_right** – Not documented
        - **ret** – Not documented
        - **a** – Not documented
        - **s** – Not documented
        - **d** – Not documented
        - **f** – Not documented
        - **g** – Not documented
        - **h** – Not documented
        - **j** – Not documented
        - **k** – Not documented
        - **l** – Not documented
        - **semicolon** – Not documented
        - **apostrophe** – Not documented
        - **grave_accent** – Not documented
        - **backslash** – Not documented
        - **z** – Not documented
        - **x** – Not documented
        - **c** – Not documented
        - **v** – Not documented
        - **b** – Not documented
        - **n** – Not documented
        - **m** – Not documented
        - **comma** – Not documented
        - **dot** – Not documented
        - **slash** – Not documented
        - **asterisk** – Not documented
        - **spc** – Not documented
        - **caps_lock** – Not documented
        - **f1** – Not documented
        - **f2** – Not documented
        - **f3** – Not documented
        - **f4** – Not documented
        - **f5** – Not documented
        - **f6** – Not documented
        - **f7** – Not documented
        - **f8** – Not documented
        - **f9** – Not documented
        - **f10** – Not documented
        - **num_lock** – Not documented
        - **scroll_lock** – Not documented
        - **kp_divide** – Not documented
        - **kp_multiply** – Not documented
        - **kp_subtract** – Not documented
        - **kp_add** – Not documented
        - **kp_enter** – Not documented
        - **kp_decimal** – Not documented
        - **sysrq** – Not documented
        - **kp_0** – Not documented
        - **kp_1** – Not documented
        - **kp_2** – Not documented
        - **kp_3** – Not documented
        - **kp_4** – Not documented
        - **kp_5** – Not documented
        - **kp_6** – Not documented
        - **kp_7** – Not documented
        - **kp_8** – Not documented
        - **kp_9** – Not documented
        - **less** – Not documented
        - **f11** – Not documented
        - **f12** – Not documented
        - **print** – Not documented
        - **home** – Not documented
        - **pgup** – Not documented
        - **pgdn** – Not documented
        - **end** – Not documented
        - **left** – Not documented
        - **up** – Not documented
        - **down** – Not documented
        - **right** – Not documented
        - **insert** – Not documented
        - **delete** – Not documented
        - **stop** – Not documented
        - **again** – Not documented
        - **props** – Not documented
        - **undo** – Not documented
        - **front** – Not documented
        - **copy** – Not documented
        - **open** – Not documented
        - **paste** – Not documented
        - **find** – Not documented
        - **cut** – Not documented
        - **lf** – Not documented
        - **help** – Not documented
        - **meta_l** – Not documented
        - **meta_r** – Not documented
        - **compose** – Not documented

    ‘sysrq’ was mistakenly added to hack around the fact that the ps2
    driver was not generating correct scancodes sequences when
    ‘alt+print’ was pressed. This flaw is now fixed and the ‘sysrq’ key
    serves no further purpose. Any further use of ‘sysrq’ will be
    transparently changed to ‘print’, so they are effectively synonyms.

*Enum* KeyValueKind (Since: 1.3)
:   Values:
    :   - **number** – Not documented
        - **qcode** – Not documented

*Object* IntWrapper (Since: 1.3)
:   Members:
    :   - **data** (`int`) – a numeric key code

*Object* QKeyCodeWrapper (Since: 1.3)
:   Members:
    :   - **data** ([`QKeyCode`](qemu-qmp-ref.md#enum-QMP-ui.QKeyCode "QMP:ui.QKeyCode")) – An enumeration of key name

*Object* KeyValue (Since: 1.3)
:   Represents a keyboard key.

    Members:
    :   - **type** ([`KeyValueKind`](qemu-qmp-ref.md#enum-QMP-ui.KeyValueKind "QMP:ui.KeyValueKind")) – key encoding
        - When `type` is `number`: The members of [`IntWrapper`](qemu-qmp-ref.md#object-QMP-ui.IntWrapper "QMP:ui.IntWrapper").
        - When `type` is `qcode`: The members of [`QKeyCodeWrapper`](qemu-qmp-ref.md#object-QMP-ui.QKeyCodeWrapper "QMP:ui.QKeyCodeWrapper").

*Command* send-key (Since: 1.3)
:   Send keys to guest.

    Arguments:
    :   - **keys** (`[`[`KeyValue`](qemu-qmp-ref.md#object-QMP-ui.KeyValue "QMP:ui.KeyValue")`]`) – An array of [`KeyValue`](qemu-qmp-ref.md#object-QMP-ui.KeyValue "QMP:ui.KeyValue") elements. All `KeyValues` in this
          array are simultaneously sent to the guest. A [`KeyValue`](qemu-qmp-ref.md#object-QMP-ui.KeyValue "QMP:ui.KeyValue").number
          value is sent directly to the guest, while [`KeyValue`](qemu-qmp-ref.md#object-QMP-ui.KeyValue "QMP:ui.KeyValue").qcode must
          be a valid [`QKeyCode`](qemu-qmp-ref.md#enum-QMP-ui.QKeyCode "QMP:ui.QKeyCode") value
        - **hold-time** (`int`, *optional*) – time to delay key up events, milliseconds. Defaults to
          100

    Errors:
    :   - If key is unknown or redundant, GenericError

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "send-key",
    >      "arguments": { "keys": [ { "type": "qcode", "data": "ctrl" },
    >                               { "type": "qcode", "data": "alt" },
    >                               { "type": "qcode", "data": "delete" } ] } }
    > <- { "return": {} }
    > ```

*Enum* InputButton (Since: 2.0)
:   Button of a pointer input device (mouse, tablet).

    Values:
    :   - **side** – front side button of a 5-button mouse (since 2.9)
        - **extra** – rear side button of a 5-button mouse (since 2.9)
        - **touch** – screen contact on a multi-touch device (since 8.1)
        - **left** – Not documented
        - **middle** – Not documented
        - **right** – Not documented
        - **wheel-up** – Not documented
        - **wheel-down** – Not documented
        - **wheel-left** – Not documented
        - **wheel-right** – Not documented

*Enum* InputAxis (Since: 2.0)
:   Position axis of a pointer input device (mouse, tablet).

    Values:
    :   - **x** – Not documented
        - **y** – Not documented

*Enum* InputMultiTouchType (Since: 8.1)
:   Type of a multi-touch event.

    Values:
    :   - **begin** – A new touch event sequence has just started.
        - **update** – A touch event sequence has been updated.
        - **end** – A touch event sequence has finished.
        - **cancel** – A touch event sequence has been canceled.
        - **data** – Absolute position data.

*Object* InputKeyEvent (Since: 2.0)
:   Keyboard input event.

    Members:
    :   - **key** ([`KeyValue`](qemu-qmp-ref.md#object-QMP-ui.KeyValue "QMP:ui.KeyValue")) – Which key this event is for.
        - **down** (`boolean`) – True for key-down and false for key-up events.

*Object* InputBtnEvent (Since: 2.0)
:   Pointer button input event.

    Members:
    :   - **button** ([`InputButton`](qemu-qmp-ref.md#enum-QMP-ui.InputButton "QMP:ui.InputButton")) – Which button this event is for.
        - **down** (`boolean`) – True for key-down and false for key-up events.

*Object* InputMoveEvent (Since: 2.0)
:   Pointer motion input event.

    Members:
    :   - **axis** ([`InputAxis`](qemu-qmp-ref.md#enum-QMP-ui.InputAxis "QMP:ui.InputAxis")) – Which axis is referenced by `value`.
        - **value** (`int`) – Pointer position. For absolute coordinates the valid range
          is 0 to 0x7fff.

*Object* InputMultiTouchEvent (Since: 8.1)
:   MultiTouch input event.

    Members:
    :   - **type** ([`InputMultiTouchType`](qemu-qmp-ref.md#enum-QMP-ui.InputMultiTouchType "QMP:ui.InputMultiTouchType")) – The type of multi-touch event.
        - **slot** (`int`) – Which slot has generated the event.
        - **tracking-id** (`int`) – ID to correlate this event with previously generated
          events.
        - **axis** ([`InputAxis`](qemu-qmp-ref.md#enum-QMP-ui.InputAxis "QMP:ui.InputAxis")) – Which axis is referenced by `value`.
        - **value** (`int`) – Contact position.

*Enum* InputEventKind (Since: 2.0)
:   Values:
    :   - **key** – a keyboard input event
        - **btn** – a pointer button input event
        - **rel** – a relative pointer motion input event
        - **abs** – an absolute pointer motion input event
        - **mtt** – a multi-touch input event

*Object* InputKeyEventWrapper (Since: 2.0)
:   Members:
    :   - **data** ([`InputKeyEvent`](qemu-qmp-ref.md#object-QMP-ui.InputKeyEvent "QMP:ui.InputKeyEvent")) – Keyboard input event

*Object* InputBtnEventWrapper (Since: 2.0)
:   Members:
    :   - **data** ([`InputBtnEvent`](qemu-qmp-ref.md#object-QMP-ui.InputBtnEvent "QMP:ui.InputBtnEvent")) – Pointer button input event

*Object* InputMoveEventWrapper (Since: 2.0)
:   Members:
    :   - **data** ([`InputMoveEvent`](qemu-qmp-ref.md#object-QMP-ui.InputMoveEvent "QMP:ui.InputMoveEvent")) – Pointer motion input event

*Object* InputMultiTouchEventWrapper (Since: 8.1)
:   Members:
    :   - **data** ([`InputMultiTouchEvent`](qemu-qmp-ref.md#object-QMP-ui.InputMultiTouchEvent "QMP:ui.InputMultiTouchEvent")) – MultiTouch input event

*Object* InputEvent (Since: 2.0)
:   Input event union.

    Members:
    :   - **type** ([`InputEventKind`](qemu-qmp-ref.md#enum-QMP-ui.InputEventKind "QMP:ui.InputEventKind")) – the type of input event
        - When `type` is `key`: The members of [`InputKeyEventWrapper`](qemu-qmp-ref.md#object-QMP-ui.InputKeyEventWrapper "QMP:ui.InputKeyEventWrapper").
        - When `type` is `btn`: The members of [`InputBtnEventWrapper`](qemu-qmp-ref.md#object-QMP-ui.InputBtnEventWrapper "QMP:ui.InputBtnEventWrapper").
        - When `type` is `rel`: The members of [`InputMoveEventWrapper`](qemu-qmp-ref.md#object-QMP-ui.InputMoveEventWrapper "QMP:ui.InputMoveEventWrapper").
        - When `type` is `abs`: The members of [`InputMoveEventWrapper`](qemu-qmp-ref.md#object-QMP-ui.InputMoveEventWrapper "QMP:ui.InputMoveEventWrapper").
        - When `type` is `mtt`: The members of [`InputMultiTouchEventWrapper`](qemu-qmp-ref.md#object-QMP-ui.InputMultiTouchEventWrapper "QMP:ui.InputMultiTouchEventWrapper").

*Command* input-send-event (Since: 2.6)
:   Send input event(s) to guest.

    The `device` and `head` parameters can be used to send the input event
    to specific input devices in case (a) multiple input devices of the
    same kind are added to the virtual machine and (b) you have
    configured input routing (see docs/multiseat.txt) for those input
    devices. The parameters work exactly like the device and head
    properties of input devices. If `device` is missing, only devices
    that have no input routing config are admissible. If `device` is
    specified, both input devices with and without input routing config
    are admissible, but devices with input routing config take
    precedence.

    Arguments:
    :   - **device** (`string`, *optional*) – display device to send event(s) to.
        - **head** (`int`, *optional*) – head to send event(s) to, in case the display device supports
          multiple scanouts.
        - **events** (`[`[`InputEvent`](qemu-qmp-ref.md#object-QMP-ui.InputEvent "QMP:ui.InputEvent")`]`) – List of [`InputEvent`](qemu-qmp-ref.md#object-QMP-ui.InputEvent "QMP:ui.InputEvent") union.

    > **Note:**
    >
    > The consoles are visible in the qom tree, under
    > `/backend/console[$index]`. They have a device link and head
    > property, so it is possible to map which console belongs to which
    > device and display.

    > **Example: Press left mouse button:**
    >
    > ```QMP
    >  -> { "execute": "input-send-event",
    >      "arguments": { "device": "video0",
    >                     "events": [ { "type": "btn",
    >                     "data" : { "down": true, "button": "left" } } ] } }
    >  <- { "return": {} }
    >
    >  -> { "execute": "input-send-event",
    >      "arguments": { "device": "video0",
    >                     "events": [ { "type": "btn",
    >                     "data" : { "down": false, "button": "left" } } ] } }
    >  <- { "return": {} }
    > ```

    > **Example: Press ctrl-alt-del:**
    >
    > ```QMP
    >  -> { "execute": "input-send-event",
    >       "arguments": { "events": [
    >          { "type": "key", "data" : { "down": true,
    >            "key": {"type": "qcode", "data": "ctrl" } } },
    >          { "type": "key", "data" : { "down": true,
    >            "key": {"type": "qcode", "data": "alt" } } },
    >          { "type": "key", "data" : { "down": true,
    >            "key": {"type": "qcode", "data": "delete" } } } ] } }
    >  <- { "return": {} }
    > ```

    > **Example: Move mouse pointer to absolute coordinates:**
    >
    > ```QMP
    >  -> { "execute": "input-send-event" ,
    >    "arguments": { "events": [
    >                 { "type": "abs", "data" : { "axis": "x", "value" : 20000 } },
    >                 { "type": "abs", "data" : { "axis": "y", "value" : 400 } } ] } }
    >  <- { "return": {} }
    > ```

*Object* DisplayGTK (Since: 2.12)
:   GTK display options.

    Members:
    :   - **clipboard** (`boolean`, *optional*) – Enable host-guest clipboard sharing. Defaults to “off”.
          (Since 11.1)
        - **grab-on-hover** (`boolean`, *optional*) – Grab keyboard input on mouse hover.
        - **zoom-to-fit** (`boolean`, *optional*) – Zoom guest display to fit into the host window. When
          turned off the host window will be resized instead. In case the
          display device can notify the guest on window resizes
          (virtio-gpu) this will default to “on”, assuming the guest will
          resize the display to match the window size then. Otherwise it
          defaults to “off”. (Since 3.1)
        - **show-tabs** (`boolean`, *optional*) – Display the tab bar for switching between the various
          graphical interfaces (e.g. VGA and virtual console character
          devices) by default. (Since 7.1)
        - **show-menubar** (`boolean`, *optional*) – Display the main window menubar. Defaults to “on”.
          (Since 8.0)
        - **keep-aspect-ratio** (`boolean`, *optional*) – Keep width/height aspect ratio of guest content
          when resizing host window. Defaults to “on”. (Since 10.1)
        - **scale** (`number`, *optional*) – Set preferred scale of the display. Defaults to 1.0.
          (Since 10.1)

*Object* DisplayEGLHeadless (Since: 3.1)
:   EGL headless display options.

    Members:
    :   - **rendernode** (`string`, *optional*) – Which DRM render node should be used. Default is the
          first available node on the host.

*Object* DisplayDBus (Since: 7.0)
:   DBus display options.

    Members:
    :   - **addr** (`string`, *optional*) – The D-Bus bus address (default to the session bus).
        - **rendernode** (`string`, *optional*) – Which DRM render node should be used. Default is the
          first available node on the host.
        - **p2p** (`boolean`, *optional*) – Whether to use peer-to-peer connections (accepted through
          [`add_client`](qemu-qmp-ref.md#command-QMP-misc.add_client "QMP:misc.add_client")).
        - **audiodev** (`string`, *optional*) – Use the specified DBus audiodev to export audio.

*Enum* DisplayGLMode (Since: 3.0)
:   Display OpenGL mode.

    Values:
    :   - **off** – Disable OpenGL (default).
        - **on** – Use OpenGL, pick context type automatically. Would better be
          named ‘auto’ but is called ‘on’ for backward compatibility with
          bool type.
        - **core** – Use OpenGL with Core (desktop) Context.
        - **es** – Use OpenGL with ES (embedded systems) Context.

*Object* DisplayCurses (Since: 4.0)
:   Curses display options.

    Members:
    :   - **charset** (`string`, *optional*) – Font charset used by guest (default: CP437).

*Object* DisplayCocoa (Since: 7.0)
:   Cocoa display options.

    Members:
    :   - **left-command-key** (`boolean`, *optional*) – Enable/disable forwarding of left command key to
          guest. Allows command-tab window switching on the host without
          sending this key to the guest when “off”. Defaults to “on”
        - **full-grab** (`boolean`, *optional*) – Capture all key presses, including system combos. This
          requires accessibility permissions, since it performs a global
          grab on key events. (default: off) See
          <https://support.apple.com/en-in/guide/mac-help/mh32356/mac>
        - **swap-opt-cmd** (`boolean`, *optional*) – Swap the Option and Command keys so that their key
          codes match their position on non-Mac keyboards and you can use
          Meta/Super and Alt where you expect them. (default: off)
        - **zoom-to-fit** (`boolean`, *optional*) – Zoom guest display to fit into the host window. When
          turned off the host window will be resized instead. Defaults to
          “off”. (Since 8.2)
        - **zoom-interpolation** (`boolean`, *optional*) – Apply interpolation to smooth output when
          zoom-to-fit is enabled. Defaults to “off”. (Since 9.0)

*Enum* HotKeyMod (Since: 7.1)
:   Set of modifier keys that need to be held for shortcut key actions.

    Values:
    :   - **lctrl-lalt** – Not documented
        - **lshift-lctrl-lalt** – Not documented
        - **rctrl** – Not documented

*Object* DisplaySDL (Since: 7.1)
:   SDL2 display options.

    Members:
    :   - **grab-mod** ([`HotKeyMod`](qemu-qmp-ref.md#enum-QMP-ui.HotKeyMod "QMP:ui.HotKeyMod"), *optional*) – Modifier keys that should be pressed together with the
          “G” key to release the mouse grab.

*Enum* DisplayType (Since: 2.12)
:   Display (user interface) type.

    Values:
    :   - **default** – The default user interface, selecting from the first
          available of gtk, sdl, cocoa, and vnc.
        - **none** – No user interface or video output display. The guest will
          still see an emulated graphics card, but its output will not be
          displayed to the QEMU user.
        - **gtk** – The GTK user interface.
        - **sdl** – The SDL user interface.
        - **egl-headless** – No user interface, offload GL operations to a local
          DRI device. Graphical display need to be paired with VNC or
          Spice. (Since 3.1)
        - **curses** – Display video output via curses. For graphics device
          models which support a text mode, QEMU can display this output
          using a curses/ncurses interface. Nothing is displayed when the
          graphics device is in graphical mode or if the graphics device
          does not support a text mode. Generally only the VGA device
          models support text mode.
        - **cocoa** – The Cocoa user interface.
        - **spice-app** – Set up a Spice server and run the default associated
          application to connect to it. The server will redirect the
          serial console and QEMU monitors. (Since 4.0)
        - **dbus** – Start a D-Bus service for the display. (Since 7.0)

*Object* DisplayOptions (Since: 2.12)
:   Display (user interface) options.

    Members:
    :   - **type** ([`DisplayType`](qemu-qmp-ref.md#enum-QMP-ui.DisplayType "QMP:ui.DisplayType")) – Which [`DisplayType`](qemu-qmp-ref.md#enum-QMP-ui.DisplayType "QMP:ui.DisplayType") QEMU should use.
        - **full-screen** (`boolean`, *optional*) – Start user interface in fullscreen mode
          (default: off).
        - **window-close** (`boolean`, *optional*) – Allow to quit QEMU with window close button
          (default: on).
        - **show-cursor** (`boolean`, *optional*) – Force showing the mouse cursor (default: off).
          (since: 5.0)
        - **gl** ([`DisplayGLMode`](qemu-qmp-ref.md#enum-QMP-ui.DisplayGLMode "QMP:ui.DisplayGLMode"), *optional*) – Enable OpenGL support (default: off).
        - When `type` is `gtk`: The members of [`DisplayGTK`](qemu-qmp-ref.md#object-QMP-ui.DisplayGTK "QMP:ui.DisplayGTK").
        - When `type` is `cocoa`: The members of [`DisplayCocoa`](qemu-qmp-ref.md#object-QMP-ui.DisplayCocoa "QMP:ui.DisplayCocoa").
        - When `type` is `curses`: The members of [`DisplayCurses`](qemu-qmp-ref.md#object-QMP-ui.DisplayCurses "QMP:ui.DisplayCurses").
        - When `type` is `egl-headless`: The members of [`DisplayEGLHeadless`](qemu-qmp-ref.md#object-QMP-ui.DisplayEGLHeadless "QMP:ui.DisplayEGLHeadless").
        - When `type` is `dbus`: The members of [`DisplayDBus`](qemu-qmp-ref.md#object-QMP-ui.DisplayDBus "QMP:ui.DisplayDBus").
        - When `type` is `sdl`: The members of [`DisplaySDL`](qemu-qmp-ref.md#object-QMP-ui.DisplaySDL "QMP:ui.DisplaySDL").

*Command* query-display-options (Since: 3.1)
:   Return information about display configuration

    Return:
    :   [`DisplayOptions`](qemu-qmp-ref.md#object-QMP-ui.DisplayOptions "QMP:ui.DisplayOptions")

*Enum* DisplayReloadType (Since: 6.0)
:   Available DisplayReload types.

    Values:
    :   - **vnc** – VNC display

*Object* DisplayReloadOptionsVNC (Since: 6.0)
:   Specify the VNC reload options.

    Members:
    :   - **tls-certs** (`boolean`, *optional*) – reload tls certs or not.

*Object* DisplayReloadOptions (Since: 6.0)
:   Options of the display configuration reload.

    Members:
    :   - **type** ([`DisplayReloadType`](qemu-qmp-ref.md#enum-QMP-ui.DisplayReloadType "QMP:ui.DisplayReloadType")) – Specify the display type.
        - When `type` is `vnc`: The members of [`DisplayReloadOptionsVNC`](qemu-qmp-ref.md#object-QMP-ui.DisplayReloadOptionsVNC "QMP:ui.DisplayReloadOptionsVNC").

*Command* display-reload (Since: 6.0)
:   Reload display configuration.

    Arguments:
    :   - The members of [`DisplayReloadOptions`](qemu-qmp-ref.md#object-QMP-ui.DisplayReloadOptions "QMP:ui.DisplayReloadOptions").

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "display-reload",
    >      "arguments": { "type": "vnc", "tls-certs": true  } }
    > <- { "return": {} }
    > ```

*Enum* DisplayUpdateType (Since: 7.1)
:   Available DisplayUpdate types.

    Values:
    :   - **vnc** – VNC display

*Object* DisplayUpdateOptionsVNC (Since: 7.1)
:   Specify the VNC reload options.

    Members:
    :   - **addresses** (`[`[`SocketAddress`](qemu-qmp-ref.md#object-QMP-sockets.SocketAddress "QMP:sockets.SocketAddress")`]`, *optional*) – If specified, change set of addresses to listen for
          connections. Addresses configured for websockets are not
          touched.

*Object* DisplayUpdateOptions (Since: 7.1)
:   Options of the display configuration reload.

    Members:
    :   - **type** ([`DisplayUpdateType`](qemu-qmp-ref.md#enum-QMP-ui.DisplayUpdateType "QMP:ui.DisplayUpdateType")) – Specify the display type.
        - When `type` is `vnc`: The members of [`DisplayUpdateOptionsVNC`](qemu-qmp-ref.md#object-QMP-ui.DisplayUpdateOptionsVNC "QMP:ui.DisplayUpdateOptionsVNC").

*Command* display-update (Since: 7.1)
:   Update display configuration.

    Arguments:
    :   - The members of [`DisplayUpdateOptions`](qemu-qmp-ref.md#object-QMP-ui.DisplayUpdateOptions "QMP:ui.DisplayUpdateOptions").

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "display-update",
    >      "arguments": { "type": "vnc", "addresses":
    >                     [ { "type": "inet", "host": "0.0.0.0",
    >                         "port": "5901" } ] } }
    > <- { "return": {} }
    > ```

*Command* client_migrate_info (Since: 0.14)
:   Set migration information for remote display. This makes the server
    ask the client to automatically reconnect using the new parameters
    once migration finished successfully. Only implemented for SPICE.

    Arguments:
    :   - **protocol** (`string`) – must be “spice”
        - **hostname** (`string`) – migration target hostname
        - **port** (`int`, *optional*) – spice tcp port for plaintext channels
        - **tls-port** (`int`, *optional*) – spice tcp port for tls-secured channels
        - **cert-subject** (`string`, *optional*) – server certificate subject

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "client_migrate_info",
    >      "arguments": { "protocol": "spice",
    >                     "hostname": "virt42.lab.kraxel.org",
    >                     "port": 1234 } }
    > <- { "return": {} }
    > ```

## [User authorization](qemu-qmp-ref.md#id24)

*Enum* QAuthZListPolicy (Since: 4.0)
:   The authorization policy result

    Values:
    :   - **deny** – deny access
        - **allow** – allow access

*Enum* QAuthZListFormat (Since: 4.0)
:   The authorization policy match format

    Values:
    :   - **exact** – an exact string match
        - **glob** – string with ? and \* shell wildcard support

*Object* QAuthZListRule (Since: 4.0)
:   A single authorization rule.

    Members:
    :   - **match** (`string`) – a string or glob to match against a user identity
        - **policy** ([`QAuthZListPolicy`](qemu-qmp-ref.md#enum-QMP-authz.QAuthZListPolicy "QMP:authz.QAuthZListPolicy")) – the result to return if `match` evaluates to true
        - **format** ([`QAuthZListFormat`](qemu-qmp-ref.md#enum-QMP-authz.QAuthZListFormat "QMP:authz.QAuthZListFormat"), *optional*) – the format of the `match` rule (default ‘exact’)

*Object* AuthZListProperties (Since: 4.0)
:   Properties for authz-list objects.

    Members:
    :   - **policy** ([`QAuthZListPolicy`](qemu-qmp-ref.md#enum-QMP-authz.QAuthZListPolicy "QMP:authz.QAuthZListPolicy"), *optional*) – Default policy to apply when no rule matches (default:
          deny)
        - **rules** (`[`[`QAuthZListRule`](qemu-qmp-ref.md#object-QMP-authz.QAuthZListRule "QMP:authz.QAuthZListRule")`]`, *optional*) – Authorization rules based on matching user

*Object* AuthZListFileProperties (Since: 4.0)
:   Properties for authz-listfile objects.

    Members:
    :   - **filename** (`string`) – File name to load the configuration from. The file must
          contain valid JSON for [`AuthZListProperties`](qemu-qmp-ref.md#object-QMP-authz.AuthZListProperties "QMP:authz.AuthZListProperties").
        - **refresh** (`boolean`, *optional*) – If true, inotify is used to monitor the file,
          automatically reloading changes. If an error occurs during
          reloading, all authorizations will fail until the file is next
          successfully loaded. (default: true if the binary was built
          with CONFIG_INOTIFY1, false otherwise)

*Object* AuthZPAMProperties (Since: 4.0)
:   Properties for authz-pam objects.

    Members:
    :   - **service** (`string`) – PAM service name to use for authorization

*Object* AuthZSimpleProperties (Since: 4.0)
:   Properties for authz-simple objects.

    Members:
    :   - **identity** (`string`) – Identifies the allowed user. Its format depends on the
          network service that authorization object is associated with.
          For authorizing based on TLS x509 certificates, the identity
          must be the x509 distinguished name.

## [Migration](qemu-qmp-ref.md#id25)

*Object* MigrationRAMStats (Since: 0.14)
:   Detailed migration status.

    Members:
    :   - **transferred** (`int`) – amount of bytes already transferred to the target VM
        - **remaining** (`int`) – amount of bytes remaining to be transferred to the
          target VM
        - **total** (`int`) – total amount of bytes involved in the migration process
        - **duplicate** (`int`) – number of duplicate (zero) pages (since 1.2)
        - **normal** (`int`) – number of normal pages (since 1.2)
        - **normal-bytes** (`int`) – number of normal bytes sent (since 1.2)
        - **dirty-pages-rate** (`int`) – number of pages dirtied by second by the guest
          (since 1.3)
        - **mbps** (`number`) – throughput in megabits/sec. (since 1.6)
        - **dirty-sync-count** (`int`) – number of times that dirty ram was synchronized
          (since 2.1)
        - **postcopy-requests** (`int`) – The number of page requests received from the
          destination (since 2.7)
        - **page-size** (`int`) – The number of bytes per page for the various page-based
          statistics (since 2.10)
        - **multifd-bytes** (`int`) – The number of bytes sent through multifd (since 3.0)
        - **pages-per-second** (`int`) – the number of memory pages transferred per second
          (Since 4.0)
        - **precopy-bytes** (`int`) – The number of bytes sent in the pre-copy phase
          (since 7.0).
        - **downtime-bytes** (`int`) – The number of bytes sent while the guest is paused
          (since 7.0).
        - **postcopy-bytes** (`int`) – The number of bytes sent during the post-copy phase
          (since 7.0).
        - **dirty-sync-missed-zero-copy** (`int`) – Number of times dirty RAM
          synchronization could not avoid copying dirty pages. This is
          between 0 and `dirty-sync-count` \* `multifd-channels`.
          (since 7.1)

*Object* XBZRLECacheStats (Since: 1.2)
:   Detailed XBZRLE migration cache statistics

    Members:
    :   - **cache-size** (`int`) – XBZRLE cache size
        - **bytes** (`int`) – amount of bytes already transferred to the target VM
        - **pages** (`int`) – amount of pages transferred to the target VM
        - **cache-miss** (`int`) – number of cache miss
        - **cache-miss-rate** (`number`) – rate of cache miss (since 2.1)
        - **encoding-rate** (`number`) – rate of encoded bytes (since 5.1)
        - **overflow** (`int`) – number of overflows

*Object* CompressionStats (Since: 3.1)
:   Detailed migration compression statistics

    Members:
    :   - **pages** (`int`) – amount of pages compressed and transferred to the target VM
        - **busy** (`int`) – count of times that no free thread was available to compress
          data
        - **busy-rate** (`number`) – rate of thread busy
        - **compressed-size** (`int`) – amount of bytes after compression
        - **compression-rate** (`number`) – rate of compressed size

*Enum* MigrationStatus (Since: 2.3)
:   An enumeration of migration status.

    Values:
    :   - **none** – no migration has ever happened.
        - **setup** – migration process has been initiated.
        - **cancelling** – in the process of cancelling migration.
        - **cancelled** – cancelling migration is finished.
        - **active** – in the process of doing migration.
        - **postcopy-active** – like active, but now in postcopy mode.
          (since 2.5)
        - **postcopy-device** – like postcopy-active, but the destination is still
          loading device state and is not running yet. If migration fails
          during this state, the source side will resume. If there is no
          return-path from destination to source, this state is skipped.
          (since 10.2)
        - **postcopy-paused** – during postcopy but paused. (since 3.0)
        - **postcopy-recover-setup** – setup phase for a postcopy recovery
          process, preparing for a recovery phase to start. (since 9.1)
        - **postcopy-recover** – trying to recover from a paused postcopy.
          (since 3.0)
        - **completed** – migration is finished.
        - **failing** – error occurred during migration, clean-up underway.
          (since 11.0)
        - **failed** – error occurred during migration, clean-up done.
        - **colo** – VM is in the process of fault tolerance, VM can not get into
          this state unless colo capability is enabled for migration.
          (since 2.8)
        - **pre-switchover** – Paused before device serialisation. (since 2.11)
        - **device** – During device serialisation (also known as switchover
          phase). Before 9.2, this is only used when (1) in precopy, and
          (2) when pre-switchover capability is enabled. After 10.0, this
          state will always be present for every migration procedure as
          the switchover phase. (since 2.11)
        - **wait-unplug** – wait for device unplug request by guest OS to be
          completed. (since 4.2)

*Object* VfioStats (Since: 5.2)
:   Detailed VFIO devices migration statistics

    Members:
    :   - **transferred** (`int`) – amount of bytes transferred to the target VM by VFIO
          devices

*Object* MigrationInfo (Since: 0.14)
:   Information about current migration process.

    Members:
    :   - **status** ([`MigrationStatus`](qemu-qmp-ref.md#enum-QMP-migration.MigrationStatus "QMP:migration.MigrationStatus"), *optional*) – [`MigrationStatus`](qemu-qmp-ref.md#enum-QMP-migration.MigrationStatus "QMP:migration.MigrationStatus") describing the current migration status.
          If this field is not returned, no migration process has been
          initiated
        - **ram** ([`MigrationRAMStats`](qemu-qmp-ref.md#object-QMP-migration.MigrationRAMStats "QMP:migration.MigrationRAMStats"), *optional*) – Detailed migration RAM statistics, only returned if migration
          is in progress or completed (since 1.2)
        - **xbzrle-cache** ([`XBZRLECacheStats`](qemu-qmp-ref.md#object-QMP-migration.XBZRLECacheStats "QMP:migration.XBZRLECacheStats"), *optional*) – [`XBZRLECacheStats`](qemu-qmp-ref.md#object-QMP-migration.XBZRLECacheStats "QMP:migration.XBZRLECacheStats") containing detailed XBZRLE
          migration statistics, only returned if XBZRLE feature is on and
          status is ‘active’ or ‘completed’ (since 1.2)
        - **total-time** (`int`, *optional*) – total amount of milliseconds since migration started.
          If migration has ended, it returns the total migration time.
          (since 1.2)
        - **downtime** (`int`, *optional*) – only present when migration finishes correctly total
          downtime in milliseconds for the guest. (since 1.3)
        - **expected-downtime** (`int`, *optional*) – only present while migration is active expected
          downtime in milliseconds for the guest in last walk of the dirty
          bitmap. (since 1.3)
        - **setup-time** (`int`, *optional*) – amount of setup time in milliseconds *before* the
          iterations begin but *after* the QMP command is issued. This is
          designed to provide an accounting of any activities (such as
          RDMA pinning) which may be expensive, but do not actually occur
          during the iterative migration rounds themselves. (since 1.6)
        - **cpu-throttle-percentage** (`int`, *optional*) – percentage of time guest cpus are being
          throttled during auto-converge. This is only present when
          auto-converge has started throttling guest cpus. (Since 2.7)
        - **error-desc** (`string`, *optional*) – the human readable error description string. Clients
          should not attempt to parse the error strings. (Since 2.7)
        - **postcopy-blocktime** (`int`, *optional*) – total time when all vCPU were blocked during
          postcopy live migration. This is only present when the
          postcopy-blocktime migration capability is enabled. (Since 3.0)
        - **postcopy-vcpu-blocktime** (`[``int``]`, *optional*) – list of the postcopy blocktime per vCPU.
          This is only present when the postcopy-blocktime migration
          capability is enabled. (Since 3.0)
        - **postcopy-latency** (`int`, *optional*) – average remote page fault latency (in ns). Note
          that this doesn’t include all faults, but only the ones that
          require a remote page request. So it should be always bigger
          than the real average page fault latency. This is only present
          when the postcopy-blocktime migration capability is enabled.
          (Since 10.1)
        - **postcopy-latency-dist** (`[``int``]`, *optional*) – remote page fault latency distributions.
          Each element of the array is the number of faults that fall into
          the bucket period. For the N-th bucket (N>=0), the latency
          window is [2^Nus, 2^(N+1)us). For example, the 8th element
          stores how many remote faults got resolved within [256us, 512us)
          window. This is only present when the postcopy-blocktime
          migration capability is enabled. (Since 10.1)
        - **postcopy-vcpu-latency** (`[``int``]`, *optional*) – average remote page fault latency per vCPU
          (in ns). It has the same definition of `postcopy-latency`, but
          instead this is the per-vCPU statistics. This is only present
          when the postcopy-blocktime migration capability is enabled.
          (Since 10.1)
        - **postcopy-non-vcpu-latency** (`int`, *optional*) – average remote page fault latency for
          all faults happened in non-vCPU threads (in ns). It has the
          same definition of `postcopy-latency` but this only provides
          statistics to non-vCPU faults. This is only present when the
          postcopy-blocktime migration capability is enabled.
          (Since 10.1)
        - **socket-address** (`[`[`SocketAddress`](qemu-qmp-ref.md#object-QMP-sockets.SocketAddress "QMP:sockets.SocketAddress")`]`, *optional*) – Only used for tcp, to know what the real port is
          (Since 4.0)
        - **vfio** ([`VfioStats`](qemu-qmp-ref.md#object-QMP-migration.VfioStats "QMP:migration.VfioStats"), *optional*) – [`VfioStats`](qemu-qmp-ref.md#object-QMP-migration.VfioStats "QMP:migration.VfioStats") containing detailed VFIO devices migration
          statistics, only returned if VFIO device is present, migration
          is supported by all VFIO devices and status is ‘active’ or
          ‘completed’ (since 5.2)
        - **blocked-reasons** (`[``string``]`, *optional*) – A list of reasons an outgoing migration is
          blocked. Present and non-empty when migration is blocked.
          (since 6.0)
        - **dirty-limit-throttle-time-per-round** (`int`, *optional*) – Maximum throttle time (in
          microseconds) of virtual CPUs each dirty ring full round, which
          shows how [`MigrationCapability`](qemu-qmp-ref.md#enum-QMP-migration.MigrationCapability "QMP:migration.MigrationCapability") dirty-limit affects the guest
          during live migration. (Since 8.1)
        - **dirty-limit-ring-full-time** (`int`, *optional*) – Estimated average dirty ring full time
          (in microseconds) for each dirty ring full round. The value
          equals the dirty ring memory size divided by the average dirty
          page rate of the virtual CPU, which can be used to observe the
          average memory load of the virtual CPU indirectly. Note that
          zero means guest doesn’t dirty memory. (Since 8.1)
        - **remaining** (`int`, *optional*) – amount of bytes remaining to be migrated system-wide,
          includes both RAM and all devices (like VFIO). (Since 11.1)

    Features:
    :   - **unstable** – Members `postcopy-latency`, `postcopy-vcpu-latency`,
          `postcopy-latency-dist`, `postcopy-non-vcpu-latency` are
          experimental.

*Command* query-migrate (Since: 0.14)
:   Return information about current migration process. If migration is
    active there will be another json-object with RAM migration status.

    Return:
    :   [`MigrationInfo`](qemu-qmp-ref.md#object-QMP-migration.MigrationInfo "QMP:migration.MigrationInfo")

    > **Example: Before the first migration:**
    >
    > ```QMP
    >  -> { "execute": "query-migrate" }
    >  <- { "return": {} }
    > ```

    > **Example: Migration is done and has succeeded:**
    >
    > ```QMP
    >  -> { "execute": "query-migrate" }
    >  <- { "return": {
    >          "status": "completed",
    >          "total-time":12345,
    >          "setup-time":12345,
    >          "downtime":12345,
    >          "ram":{
    >            "transferred":123,
    >            "remaining":123,
    >            "total":246,
    >            "duplicate":123,
    >            "normal":123,
    >            "normal-bytes":123456,
    >            "dirty-sync-count":15
    >          }
    >       }
    >     }
    > ```

    > **Example: Migration is done and has failed:**
    >
    > ```QMP
    >  -> { "execute": "query-migrate" }
    >  <- { "return": { "status": "failed" } }
    > ```

    > **Example: Migration is being performed:**
    >
    > ```QMP
    >  -> { "execute": "query-migrate" }
    >  <- {
    >        "return":{
    >           "status":"active",
    >           "total-time":12345,
    >           "setup-time":12345,
    >           "expected-downtime":12345,
    >           "ram":{
    >              "transferred":123,
    >              "remaining":123,
    >              "total":246,
    >              "duplicate":123,
    >              "normal":123,
    >              "normal-bytes":123456,
    >              "dirty-sync-count":15
    >           }
    >        }
    >     }
    > ```

    > **Example: Migration is being performed and XBZRLE is active:**
    >
    > ```QMP
    >  -> { "execute": "query-migrate" }
    >  <- {
    >        "return":{
    >           "status":"active",
    >           "total-time":12345,
    >           "setup-time":12345,
    >           "expected-downtime":12345,
    >           "ram":{
    >              "total":1057024,
    >              "remaining":1053304,
    >              "transferred":3720,
    >              "duplicate":10,
    >              "normal":3333,
    >              "normal-bytes":3412992,
    >              "dirty-sync-count":15
    >           },
    >           "xbzrle-cache":{
    >              "cache-size":67108864,
    >              "bytes":20971520,
    >              "pages":2444343,
    >              "cache-miss":2244,
    >              "cache-miss-rate":0.123,
    >              "encoding-rate":80.1,
    >              "overflow":34434
    >           }
    >        }
    >     }
    > ```

*Enum* MigrationCapability (Since: 1.2)
:   Migration capabilities enumeration

    Values:
    :   - **xbzrle** – Migration supports xbzrle (Xor Based Zero Run Length
          Encoding). This feature allows us to minimize migration traffic
          for certain work loads, by sending compressed difference of the
          pages
        - **rdma-pin-all** – Controls whether or not the entire VM memory
          footprint is mlock()’d on demand or all at once. Refer to
          docs/rdma.txt for usage. Disabled by default. (since 2.0)
        - **events** – generate events for each migration state change (since 2.4)
        - **auto-converge** – If enabled, QEMU will automatically throttle down
          the guest to speed up convergence of RAM migration. (since 1.6)
        - **postcopy-ram** – Start executing on the migration target before all of
          RAM has been migrated, pulling the remaining pages along as
          needed. The capacity must have the same setting on both source
          and target or migration will not even start. **Note:** if the
          migration fails during postcopy the VM will fail. (since 2.6)
        - **x-colo** – If enabled, migration will never end, and the state of the
          VM on the primary side will be migrated continuously to the VM
          on secondary side, this process is called COarse-Grain LOck
          Stepping (COLO) for Non-stop Service. (since 2.8)
        - **release-ram** – if enabled, QEMU will free the migrated ram pages on
          the source during postcopy-ram migration. (since 2.9)
        - **return-path** – If enabled, migration will use the return path even
          for precopy. (since 2.10)
        - **pause-before-switchover** – Pause outgoing migration before
          serialising device state and before disabling block IO
          (since 2.11)
        - **multifd** – Use more than one fd for migration (since 4.0)
        - **dirty-bitmaps** – If enabled, QEMU will migrate named dirty bitmaps.
          (since 2.12)
        - **postcopy-blocktime** – Calculate downtime for postcopy live migration
          (since 3.0)
        - **late-block-activate** – If enabled, the destination will not activate
          block devices (and thus take locks) immediately at the end of
          migration. (since 3.0)
        - **x-ignore-shared** – If enabled, QEMU will not migrate shared memory
          that is accessible on the destination machine. (since 4.0)
        - **validate-uuid** – Send the UUID of the source to allow the destination
          to ensure it is the same. (since 4.2)
        - **background-snapshot** – If enabled, the migration stream will be a
          snapshot of the VM exactly at the point when the migration
          procedure starts. The VM RAM is saved with running VM.
          (since 6.0)
        - **zero-copy-send** – Controls behavior on sending memory pages on
          migration. When true, enables a zero-copy mechanism for sending
          memory pages, if host supports it. Requires that QEMU be
          permitted to use locked memory for guest RAM pages. (since 7.1)
        - **postcopy-preempt** – If enabled, the migration process will allow
          postcopy requests to preempt precopy stream, so postcopy
          requests will be handled faster. This is a performance feature
          and should not affect the correctness of postcopy migration.
          (since 7.1)
        - **switchover-ack** – If enabled, migration will not stop the source VM
          and complete the migration until the destination has
          acknowledged that it is OK to switch over. The acknowledgement
          may depend, for example, on some device’s data being loaded in
          the destination before doing switchover. This can reduce
          downtime if devices that support this capability are present.
          Capability `return-path` must be enabled to use it. (since 8.1)
        - **dirty-limit** – If enabled, migration will throttle vCPUs as needed to
          keep their dirty page rate within `vcpu-dirty-limit`. This can
          improve responsiveness of large guests during live migration,
          and can result in more stable read performance. Requires KVM
          with accelerator property “dirty-ring-size” set. (Since 8.1)
        - **mapped-ram** – Migrate using fixed offsets in the migration file for
          each RAM page. Requires a migration URI that supports seeking,
          such as a file. (since 9.0)

    Features:
    :   - **unstable** – Members `x-colo` and `x-ignore-shared` are experimental.

*Object* MigrationCapabilityStatus (Since: 1.2)
:   Migration capability information

    Members:
    :   - **capability** ([`MigrationCapability`](qemu-qmp-ref.md#enum-QMP-migration.MigrationCapability "QMP:migration.MigrationCapability")) – capability enum
        - **state** (`boolean`) – capability state bool

*Command* migrate-set-capabilities (Since: 1.2)
:   Enable/Disable the following migration capabilities (like xbzrle)

    Arguments:
    :   - **capabilities** (`[`[`MigrationCapabilityStatus`](qemu-qmp-ref.md#object-QMP-migration.MigrationCapabilityStatus "QMP:migration.MigrationCapabilityStatus")`]`) – json array of capability modifications to make

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "migrate-set-capabilities" , "arguments":
    >      { "capabilities": [ { "capability": "xbzrle", "state": true } ] } }
    > <- { "return": {} }
    > ```

*Command* query-migrate-capabilities (Since: 1.2)
:   Return information about the current migration capabilities status

    Return:
    :   `[`[`MigrationCapabilityStatus`](qemu-qmp-ref.md#object-QMP-migration.MigrationCapabilityStatus "QMP:migration.MigrationCapabilityStatus")`]`

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "query-migrate-capabilities" }
    > <- { "return": [
    >       {"state": false, "capability": "xbzrle"},
    >       {"state": false, "capability": "rdma-pin-all"},
    >       {"state": false, "capability": "auto-converge"},
    >       {"state": true, "capability": "events"},
    >       {"state": false, "capability": "postcopy-ram"},
    >       {"state": false, "capability": "x-colo"}
    >    ]}
    > ```

*Enum* MultiFDCompression (Since: 5.0)
:   An enumeration of multifd compression methods.

    Values:
    :   - **none** – no compression.
        - **zlib** – use zlib compression method.
        - **zstd** – use zstd compression method.
        - **qatzip** – use qatzip compression method. (Since 9.2)
        - **qpl** – use qpl compression method. Query Processing Library(qpl) is
          based on the deflate compression algorithm and use the Intel
          In-Memory Analytics Accelerator(IAA) accelerated compression and
          decompression. (Since 9.1)
        - **uadk** – use UADK library compression method. (Since 9.1)

*Enum* MigMode
:   Values:
    :   - **normal** – the original form of migration. (since 8.2)
        - **cpr-reboot** –

          The [`migrate`](qemu-qmp-ref.md#command-QMP-migration.migrate "QMP:migration.migrate") command stops the VM and saves state to
          the URI. After quitting QEMU, the user resumes by running QEMU
          -incoming.

          This mode allows the user to quit QEMU, optionally update and
          reboot the OS, and restart QEMU. If the user reboots, the URI
          must persist across the reboot, such as by using a file.

          Unlike normal mode, the use of certain local storage options
          does not block the migration, but the user must not modify the
          contents of guest block devices between the quit and restart.

          This mode supports VFIO devices provided the user first puts the
          guest in the suspended runstate, such as by issuing
          [`guest-suspend-ram`](qemu-ga-ref.md#command-QGA-qapi-schema.guest-suspend-ram "QGA:qapi-schema.guest-suspend-ram") to the QEMU guest agent.

          Best performance is achieved when the memory backend is shared
          and the `x-ignore-shared` migration capability is set, but this
          is not required. Further, if the user reboots before restarting
          such a configuration, the shared memory must persist across the
          reboot, such as by backing it with a dax device.

          `cpr-reboot` may not be used with postcopy, background-snapshot,
          or COLO.

          (since 8.2)
        - **cpr-transfer** –

          This mode allows the user to transfer a guest to a
          new QEMU instance on the same host with minimal guest pause
          time by preserving guest RAM in place.

          Devices and their pinned pages are also preserved for VFIO and
          IOMMUFD. (since 10.1)

          The user starts new QEMU on the same host as old QEMU, with
          command-line arguments to create the same machine, plus the
          -incoming option for the main migration channel, like normal
          live migration. In addition, the user adds a second -incoming
          option with channel type “cpr”. This CPR channel must support
          file descriptor transfer with SCM_RIGHTS, i.e. it must be a UNIX
          domain socket.

          To initiate CPR, the user issues a migrate command to old QEMU,
          adding a second migration channel of type “cpr” in the channels
          argument. Old QEMU stops the VM, saves state to the migration
          channels, and enters the postmigrate state. Execution resumes
          in new QEMU.

          New QEMU reads the CPR channel before opening a monitor, hence
          the CPR channel cannot be specified in the list of channels for
          a [`migrate-incoming`](qemu-qmp-ref.md#command-QMP-migration.migrate-incoming "QMP:migration.migrate-incoming") command. It may only be specified on the
          command line.

          The main channel address cannot be a file type, and for an
          inet socket, the port cannot be 0 (meaning dynamically choose
          a port).

          Memory-backend objects must have the share=on attribute, but
          memory-backend-epc is not supported. The VM must be started
          with the ‘-machine aux-ram-share=on’ option.

          When using -incoming defer, you must issue the [`migrate`](qemu-qmp-ref.md#command-QMP-migration.migrate "QMP:migration.migrate") command
          to old QEMU before issuing any monitor commands to new QEMU.
          However, new QEMU does not open and read the migration stream
          until you issue the [`migrate-incoming`](qemu-qmp-ref.md#command-QMP-migration.migrate-incoming "QMP:migration.migrate-incoming") command.

          (since 10.0)
        - **cpr-exec** –

          The migrate command stops the VM, saves state to the
          migration channel, directly exec’s a new version of QEMU on the
          same host, replacing the original process while retaining its
          PID, and loads state from the channel. Guest RAM is preserved
          in place. Devices and their pinned pages are also preserved for
          VFIO and IOMMUFD.

          Old QEMU starts new QEMU by exec’ing the command specified by
          the `cpr-exec-command` parameter. The command may be a direct
          invocation of new QEMU, or may be a wrapper that exec’s the new
          QEMU binary.

          Because old QEMU terminates when new QEMU starts, one cannot
          stream data between the two, so the channel must be a type, such
          as a file, that accepts all data before old QEMU exits.
          Otherwise, old QEMU may quietly block writing to the channel.

          Memory-backend objects must have the share=on attribute, but
          memory-backend-epc is not supported. The VM must be started
          with the ‘-machine aux-ram-share=on’ option.

          (since 10.2)

*Enum* ZeroPageDetection (Since: 9.0)
:   Values:
    :   - **none** – Do not perform zero page checking.
        - **legacy** – Perform zero page checking in main migration thread.
        - **multifd** – Perform zero page checking in multifd sender thread if
          multifd migration is enabled, else in the main migration thread
          as for `legacy`.

*Object* BitmapMigrationBitmapAliasTransform (Since: 6.0)
:   Members:
    :   - **persistent** (`boolean`, *optional*) – If present, the bitmap will be made persistent or
          transient depending on this parameter.

*Object* BitmapMigrationBitmapAlias (Since: 5.2)
:   Members:
    :   - **name** (`string`) – The name of the bitmap.
        - **alias** (`string`) – An alias name for migration (for example the bitmap name on
          the opposite site).
        - **transform** ([`BitmapMigrationBitmapAliasTransform`](qemu-qmp-ref.md#object-QMP-migration.BitmapMigrationBitmapAliasTransform "QMP:migration.BitmapMigrationBitmapAliasTransform"), *optional*) – Allows the modification of the migrated bitmap.
          (since 6.0)

*Object* BitmapMigrationNodeAlias (Since: 5.2)
:   Maps a block node name and the bitmaps it has to aliases for dirty
    bitmap migration.

    Members:
    :   - **node-name** (`string`) – A block node name.
        - **alias** (`string`) – An alias block node name for migration (for example the node
          name on the opposite site).
        - **bitmaps** (`[`[`BitmapMigrationBitmapAlias`](qemu-qmp-ref.md#object-QMP-migration.BitmapMigrationBitmapAlias "QMP:migration.BitmapMigrationBitmapAlias")`]`) – Mappings for the bitmaps on this node.

*Enum* MigrationParameter (Since: 2.4)
:   Migration parameters enumeration. The enumeration values mirror the
    members of `MigrationParameters`.

    Values:
    :   - **announce-initial** – Not documented
        - **announce-max** – Not documented
        - **announce-rounds** – Not documented
        - **announce-step** – Not documented
        - **throttle-trigger-threshold** – Not documented
        - **cpu-throttle-initial** – Not documented
        - **cpu-throttle-increment** – Not documented
        - **cpu-throttle-tailslow** – Not documented
        - **tls-creds** – Not documented
        - **tls-hostname** – Not documented
        - **tls-authz** – Not documented
        - **max-bandwidth** – Not documented
        - **avail-switchover-bandwidth** – Not documented
        - **downtime-limit** – Not documented
        - **x-checkpoint-delay** – Not documented
        - **multifd-channels** – Not documented
        - **xbzrle-cache-size** – Not documented
        - **max-postcopy-bandwidth** – Not documented
        - **max-cpu-throttle** – Not documented
        - **multifd-compression** – Not documented
        - **multifd-zlib-level** – Not documented
        - **multifd-zstd-level** – Not documented
        - **multifd-qatzip-level** – Not documented
        - **block-bitmap-mapping** – Not documented
        - **x-vcpu-dirty-limit-period** – Not documented
        - **vcpu-dirty-limit** – Not documented
        - **mode** – Not documented
        - **zero-page-detection** – Not documented
        - **direct-io** – Not documented
        - **x-rdma-chunk-size** – Not documented
        - **cpr-exec-command** – Not documented

    Features:
    :   - **unstable** – Members `x-checkpoint-delay`, `x-rdma-chunk-size`, and
          `x-vcpu-dirty-limit-period` are experimental.

*Command* migrate-set-parameters (Since: 2.4)
:   Set migration parameters. All arguments are optional.

    Arguments:
    :   - The members of [`MigrationParameters`](qemu-qmp-ref.md#object-QMP-migration.MigrationParameters "QMP:migration.MigrationParameters").

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "migrate-set-parameters" ,
    >      "arguments": { "multifd-channels": 5 } }
    > <- { "return": {} }
    > ```

*Object* MigrationParameters (Since: 2.4)
:   Members:
    :   - **announce-initial** (`int`, *optional*) – Initial delay (in milliseconds) before sending
          the first announce (Since 4.0)
        - **announce-max** (`int`, *optional*) – Maximum delay (in milliseconds) between packets in
          the announcement (Since 4.0)
        - **announce-rounds** (`int`, *optional*) – Number of self-announce packets sent after
          migration (Since 4.0)
        - **announce-step** (`int`, *optional*) – Increase in delay (in milliseconds) between
          subsequent packets in the announcement (Since 4.0)
        - **throttle-trigger-threshold** (`int`, *optional*) – The ratio of bytes_dirty_period and
          bytes_xfer_period to trigger throttling. It is expressed as
          percentage. The default value is 50. (Since 5.0)
        - **cpu-throttle-initial** (`int`, *optional*) – Initial percentage of time guest cpus are
          throttled when migration auto-converge is activated. The
          default value is 20. (Since 2.7)
        - **cpu-throttle-increment** (`int`, *optional*) – throttle percentage increase each time
          auto-converge detects that migration is not making progress.
          The default value is 10. (Since 2.7)
        - **cpu-throttle-tailslow** (`boolean`, *optional*) – Make CPU throttling slower at tail stage.
          At the tail stage of throttling, the Guest is very sensitive to
          CPU percentage while the `cpu-throttle` -increment is excessive
          usually at tail stage. If this parameter is true, we will
          compute the ideal CPU percentage used by the Guest, which may
          exactly make the dirty rate match the dirty rate threshold.
          Then we will choose a smaller throttle increment between the one
          specified by `cpu-throttle-increment` and the one generated by
          ideal CPU percentage. Therefore, it is compatible to
          traditional throttling, meanwhile the throttle increment won’t
          be excessive at tail stage. The default value is false.
          (Since 5.1)
        - **tls-creds** ([`StrOrNull`](qemu-qmp-ref.md#alternate-QMP-common.StrOrNull "QMP:common.StrOrNull"), *optional*) – ID of the ‘tls-creds’ object that provides credentials
          for establishing a TLS connection over the migration data
          channel. On the outgoing side of the migration, the credentials
          must be for a ‘client’ endpoint, while for the incoming side the
          credentials must be for a ‘server’ endpoint. Setting this to a
          non-empty string enables TLS for all migrations. An empty
          string means that QEMU will use plain text mode for migration,
          rather than TLS. This is the default. (Since 2.7)
        - **tls-hostname** ([`StrOrNull`](qemu-qmp-ref.md#alternate-QMP-common.StrOrNull "QMP:common.StrOrNull"), *optional*) –

          migration target’s hostname for validating the
          server’s x509 certificate identity. If empty, QEMU will use the
          hostname from the migration URI, if any. A non-empty value is
          required when using x509 based TLS credentials and the migration
          URI does not include a hostname, such as fd: or exec: based
          migration. (Since 2.7)

          Note: empty value works only since 2.9.
        - **tls-authz** ([`StrOrNull`](qemu-qmp-ref.md#alternate-QMP-common.StrOrNull "QMP:common.StrOrNull"), *optional*) – ID of the ‘authz’ object subclass that provides access
          control checking of the TLS x509 certificate distinguished name.
          This object is only resolved at time of use, so can be deleted
          and recreated on the fly while the migration server is active.
          If missing, it will default to denying access (Since 4.0)
        - **max-bandwidth** (`int`, *optional*) – maximum speed for migration, in bytes per second.
          (Since 2.8)
        - **avail-switchover-bandwidth** (`int`, *optional*) – to set the available bandwidth that
          migration can use during switchover phase, in bytes per
          second. **Note:** this does not limit the bandwidth during
          switchover, but only for calculations when making decisions to
          switch over. By default, this value is zero, which means QEMU
          will estimate the bandwidth automatically. This can be set
          when the estimated value is not accurate, while the user is
          able to guarantee such bandwidth is available when switching
          over. When specified correctly, this can make the switchover
          decision much more accurate. (Since 8.2)
        - **downtime-limit** (`int`, *optional*) – set maximum tolerated downtime for migration.
          maximum downtime in milliseconds (Since 2.8)
        - **x-checkpoint-delay** (`int`, *optional*) – The delay time (in ms) between two COLO
          checkpoints in periodic mode. (Since 2.8)
        - **multifd-channels** (`int`, *optional*) – Number of channels used to migrate data in
          parallel. This is the same number that the number of sockets
          used for migration. The default value is 2 (since 4.0)
        - **xbzrle-cache-size** (`int`, *optional*) – cache size to be used by XBZRLE migration. It
          needs to be a multiple of the target page size and a power of 2
          (Since 2.11)
        - **max-postcopy-bandwidth** (`int`, *optional*) – Background transfer bandwidth during
          postcopy. Defaults to 0 (unlimited). In bytes per second.
          (Since 3.0)
        - **max-cpu-throttle** (`int`, *optional*) – maximum cpu throttle percentage. Defaults to 99.
          (Since 3.1)
        - **multifd-compression** ([`MultiFDCompression`](qemu-qmp-ref.md#enum-QMP-migration.MultiFDCompression "QMP:migration.MultiFDCompression"), *optional*) – Which compression method to use. Defaults to
          none. (Since 5.0)
        - **multifd-zlib-level** (`int`, *optional*) – Set the compression level to be used in live
          migration, the compression level is an integer between 0 and 9,
          where 0 means no compression, 1 means the best compression
          speed, and 9 means best compression ratio which will consume
          more CPU. Defaults to 1. (Since 5.0)
        - **multifd-qatzip-level** (`int`, *optional*) – Set the compression level to be used in live
          migration. The level is an integer between 1 and 9, where 1
          means the best compression speed, and 9 means the best
          compression ratio which will consume more CPU. Defaults to 1.
          (Since 9.2)
        - **multifd-zstd-level** (`int`, *optional*) – Set the compression level to be used in live
          migration, the compression level is an integer between 0 and 20,
          where 0 means no compression, 1 means the best compression
          speed, and 20 means best compression ratio which will consume
          more CPU. Defaults to 1. (Since 5.0)
        - **block-bitmap-mapping** (`[`[`BitmapMigrationNodeAlias`](qemu-qmp-ref.md#object-QMP-migration.BitmapMigrationNodeAlias "QMP:migration.BitmapMigrationNodeAlias")`]`, *optional*) – Maps block nodes and bitmaps on them to
          aliases for the purpose of dirty bitmap migration. Such aliases
          may for example be the corresponding names on the opposite site.
          The mapping must be one-to-one, but not necessarily complete: On
          the source, unmapped bitmaps and all bitmaps on unmapped nodes
          will be ignored. On the destination, encountering an unmapped
          alias in the incoming migration stream will result in a report,
          and all further bitmap migration data will then be discarded.
          Note that the destination does not know about bitmaps it does
          not receive, so there is no limitation or requirement regarding
          the number of bitmaps received, or how they are named, or on
          which nodes they are placed. By default (when this parameter
          has never been set), bitmap names are mapped to themselves.
          Nodes are mapped to their block device name if there is one, and
          to their node name otherwise. (Since 5.2)
        - **x-vcpu-dirty-limit-period** (`int`, *optional*) – Periodic time (in milliseconds) of dirty
          limit during live migration. Should be in the range 1 to
          1000ms. Defaults to 1000ms. (Since 8.1)
        - **vcpu-dirty-limit** (`int`, *optional*) – Dirtyrate limit (MB/s) during live migration.
          Defaults to 1. (Since 8.1)
        - **mode** ([`MigMode`](qemu-qmp-ref.md#enum-QMP-migration.MigMode "QMP:migration.MigMode"), *optional*) – Migration mode. See description in [`MigMode`](qemu-qmp-ref.md#enum-QMP-migration.MigMode "QMP:migration.MigMode"). Default is
          ‘normal’. (Since 8.2)
        - **zero-page-detection** ([`ZeroPageDetection`](qemu-qmp-ref.md#enum-QMP-migration.ZeroPageDetection "QMP:migration.ZeroPageDetection"), *optional*) – Whether and how to detect zero pages. See
          description in [`ZeroPageDetection`](qemu-qmp-ref.md#enum-QMP-migration.ZeroPageDetection "QMP:migration.ZeroPageDetection"). Default is ‘multifd’.
          (since 9.0)
        - **direct-io** (`boolean`, *optional*) – Open migration files with O_DIRECT when possible. This
          only has effect if the `mapped-ram` capability is enabled.
          (Since 9.1)
        - **cpr-exec-command** (`[``string``]`, *optional*) – Command to start the new QEMU process when `mode`
          is `cpr-exec`. The first list element is the program’s filename,
          the remainder its arguments. (Since 10.2)
        - **x-rdma-chunk-size** (`int`, *optional*) – RDMA memory registration chunk size in bytes.
          Default is 1MiB. Must be a power of 2 in the range
          [1MiB, 1024MiB]. Only applies when migrating via RDMA.
          Must be set to the same value on both source and destination
          before migration starts. (Since 11.1)

    Features:
    :   - **unstable** – Members `x-checkpoint-delay`, `x-rdma-chunk-size`, and
          `x-vcpu-dirty-limit-period` are experimental.

*Command* query-migrate-parameters (Since: 2.4)
:   Return information about the current migration parameters. Optional
    members of the return value are always present, except
    `block-bitmap-mapping`, which is only present if it has been
    previously set.

    Return:
    :   [`MigrationParameters`](qemu-qmp-ref.md#object-QMP-migration.MigrationParameters "QMP:migration.MigrationParameters")

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "query-migrate-parameters" }
    > <- { "return": {
    >          "multifd-channels": 2,
    >          "cpu-throttle-increment": 10,
    >          "cpu-throttle-initial": 20,
    >          "max-bandwidth": 33554432,
    >          "downtime-limit": 300
    >       }
    >    }
    > ```

*Command* migrate-start-postcopy (Since: 2.5)
:   Followup to a migration command to switch the migration to postcopy
    mode. The postcopy-ram capability must be set on both source and
    destination before the original migration command.

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "migrate-start-postcopy" }
    > <- { "return": {} }
    > ```

*Event* MIGRATION (Since: 2.4)
:   Emitted when a migration event happens

    Members:
    :   - **status** ([`MigrationStatus`](qemu-qmp-ref.md#enum-QMP-migration.MigrationStatus "QMP:migration.MigrationStatus")) – [`MigrationStatus`](qemu-qmp-ref.md#enum-QMP-migration.MigrationStatus "QMP:migration.MigrationStatus") describing the current migration status.

    > **Example::**
    >
    > ```QMP
    > <- {"timestamp": {"seconds": 1432121972, "microseconds": 744001},
    >     "event": "MIGRATION",
    >     "data": {"status": "completed"} }
    > ```

*Event* MIGRATION_PASS (Since: 2.6)
:   Emitted from the source side of a migration at the start of each
    pass (when it syncs the dirty bitmap)

    Members:
    :   - **pass** (`int`) – An incrementing count (starting at 1 on the first pass)

    > **Example::**
    >
    > ```QMP
    > <- { "timestamp": {"seconds": 1449669631, "microseconds": 239225},
    >       "event": "MIGRATION_PASS", "data": {"pass": 2} }
    > ```

*Enum* COLOMessage (Since: 2.8)
:   The message transmission between Primary side and Secondary side.

    Values:
    :   - **checkpoint-ready** – Secondary VM (SVM) is ready for checkpointing
        - **checkpoint-request** – Primary VM (PVM) tells SVM to prepare for
          checkpointing
        - **checkpoint-reply** – SVM gets PVM’s checkpoint request
        - **vmstate-send** – VM’s state will be sent by PVM.
        - **vmstate-size** – The total size of VMstate.
        - **vmstate-received** – VM’s state has been received by SVM.
        - **vmstate-loaded** – VM’s state has been loaded by SVM.

*Enum* COLOMode (Since: 2.8)
:   The COLO current mode.

    Values:
    :   - **none** – COLO is disabled.
        - **primary** – COLO node in primary side.
        - **secondary** – COLO node in slave side.

*Enum* FailoverStatus (Since: 2.8)
:   An enumeration of COLO failover status

    Values:
    :   - **none** – no failover has ever happened
        - **require** – got failover requirement but not handled
        - **active** – in the process of doing failover
        - **completed** – finish the process of failover
        - **relaunch** – restart the failover process, from ‘none’ -> ‘completed’
          (Since 2.9)

*Event* COLO_EXIT (Since: 3.1)
:   Emitted when VM finishes COLO mode due to some errors happening or
    at the request of users.

    Members:
    :   - **mode** ([`COLOMode`](qemu-qmp-ref.md#enum-QMP-migration.COLOMode "QMP:migration.COLOMode")) – report COLO mode when COLO exited.
        - **reason** ([`COLOExitReason`](qemu-qmp-ref.md#enum-QMP-migration.COLOExitReason "QMP:migration.COLOExitReason")) – describes the reason for the COLO exit.

    > **Example::**
    >
    > ```QMP
    > <- { "timestamp": {"seconds": 2032141960, "microseconds": 417172},
    >      "event": "COLO_EXIT", "data": {"mode": "primary", "reason": "request" } }
    > ```

*Enum* COLOExitReason (Since: 3.1)
:   The reason for a COLO exit.

    Values:
    :   - **none** – failover has never happened. This state does not occur in
          the [`COLO_EXIT`](qemu-qmp-ref.md#event-QMP-migration.COLO_EXIT "QMP:migration.COLO_EXIT") event, and is only visible in the result of
          [`query-colo-status`](qemu-qmp-ref.md#command-QMP-migration.query-colo-status "QMP:migration.query-colo-status").
        - **request** – COLO exit is due to an external request.
        - **error** – COLO exit is due to an internal error.
        - **processing** – COLO is currently handling a failover (since 4.0).

*Command* x-colo-lost-heartbeat (Since: 2.8)
:   This command is unstable/experimental.

    *Availability*: `CONFIG_REPLICATION`

    Tell QEMU that heartbeat is lost, request it to do takeover
    procedures. If this command is sent to the PVM, the Primary side
    will exit COLO mode. If sent to the Secondary, the Secondary side
    will run failover work, then takes over server operation to become
    the service VM.

    Features:
    :   - **unstable** – This command is experimental.

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "x-colo-lost-heartbeat" }
    > <- { "return": {} }
    > ```

*Command* migrate_cancel (Since: 0.14)
:   Cancel the currently executing migration process. Allows a new
    migration to be started right after. When postcopy-ram is in use,
    cancelling is not allowed after the postcopy phase has started.

    > **Note:**
    >
    > This command succeeds even if there is no migration
    > process running.

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "migrate_cancel" }
    > <- { "return": {} }
    > ```

*Command* migrate-continue (Since: 2.11)
:   Continue migration when it’s in a paused state.

    Arguments:
    :   - **state** ([`MigrationStatus`](qemu-qmp-ref.md#enum-QMP-migration.MigrationStatus "QMP:migration.MigrationStatus")) – The state the migration is currently expected to be in

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "migrate-continue" , "arguments":
    >      { "state": "pre-switchover" } }
    > <- { "return": {} }
    > ```

*Enum* MigrationAddressType (Since: 8.2)
:   The migration stream transport mechanisms.

    Values:
    :   - **socket** – Migrate via socket.
        - **exec** – Direct the migration stream to another process.
        - **rdma** – Migrate via RDMA.
        - **file** – Direct the migration stream to a file.

*Object* FileMigrationArgs (Since: 8.2)
:   Members:
    :   - **filename** (`string`) – The file to receive the migration stream
        - **offset** (`int`) – The file offset where the migration stream will start

*Object* MigrationExecCommand (Since: 8.2)
:   Members:
    :   - **args** (`[``string``]`) – command (list head) and arguments to execute.

*Object* MigrationAddress (Since: 8.2)
:   Migration endpoint configuration.

    Members:
    :   - **transport** ([`MigrationAddressType`](qemu-qmp-ref.md#enum-QMP-migration.MigrationAddressType "QMP:migration.MigrationAddressType")) – The migration stream transport mechanism
        - When `transport` is `socket`: The members of [`SocketAddress`](qemu-qmp-ref.md#object-QMP-sockets.SocketAddress "QMP:sockets.SocketAddress").
        - When `transport` is `exec`: The members of [`MigrationExecCommand`](qemu-qmp-ref.md#object-QMP-migration.MigrationExecCommand "QMP:migration.MigrationExecCommand").
        - When `transport` is `rdma`: The members of [`InetSocketAddress`](qemu-qmp-ref.md#object-QMP-sockets.InetSocketAddress "QMP:sockets.InetSocketAddress").
        - When `transport` is `file`: The members of [`FileMigrationArgs`](qemu-qmp-ref.md#object-QMP-migration.FileMigrationArgs "QMP:migration.FileMigrationArgs").

*Enum* MigrationChannelType (Since: 8.1)
:   The migration channel-type request options.

    Values:
    :   - **main** – Main outbound migration channel.
        - **cpr** – Checkpoint and restart state channel.

*Object* MigrationChannel (Since: 8.1)
:   Migration stream channel parameters.

    Members:
    :   - **channel-type** ([`MigrationChannelType`](qemu-qmp-ref.md#enum-QMP-migration.MigrationChannelType "QMP:migration.MigrationChannelType")) – Channel type for transferring packet information.
        - **addr** ([`MigrationAddress`](qemu-qmp-ref.md#object-QMP-migration.MigrationAddress "QMP:migration.MigrationAddress")) – Migration endpoint configuration on destination interface.

*Command* migrate (Since: 0.14)
:   Migrates the current running guest to another Virtual Machine.

    Arguments:
    :   - **uri** (`string`, *optional*) – the Uniform Resource Identifier of the destination VM
        - **channels** (`[`[`MigrationChannel`](qemu-qmp-ref.md#object-QMP-migration.MigrationChannel "QMP:migration.MigrationChannel")`]`, *optional*) – list of migration stream channels with each stream in the
          list connected to a destination interface endpoint.
        - **resume** (`boolean`, *optional*) – when set, use the new uri/channels specified to resume
          paused postcopy migration. This flag should only be used if
          the previous postcopy migration was interrupted. The command
          will fail unless migration is in “postcopy-paused” state.
          (default: false, since 3.0)

    > **Notes:**
    >
    > 1. The [`query-migrate`](qemu-qmp-ref.md#command-QMP-migration.query-migrate "QMP:migration.query-migrate") command should be used to check
    >    migration’s progress and final result (this information is
    >    provided by the ‘status’ member).
    > 2. The uri argument should have the Uniform Resource Identifier
    >    of default destination VM. This connection will be bound to
    >    default network.
    > 3. For now, number of migration streams is restricted to one,
    >    i.e. number of items in ‘channels’ list is just 1.
    > 4. The ‘uri’ and ‘channels’ arguments are mutually exclusive;
    >    exactly one of the two should be present.

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "migrate", "arguments": { "uri": "tcp:0:4446" } }
    > <- { "return": {} }
    >
    > -> { "execute": "migrate",
    >      "arguments": {
    >          "channels": [ { "channel-type": "main",
    >                          "addr": { "transport": "socket",
    >                                    "type": "inet",
    >                                    "host": "10.12.34.9",
    >                                    "port": "1050" } } ] } }
    > <- { "return": {} }
    >
    > -> { "execute": "migrate",
    >      "arguments": {
    >          "channels": [ { "channel-type": "main",
    >                          "addr": { "transport": "exec",
    >                                    "args": [ "/bin/nc", "-p", "6000",
    >                                              "/some/sock" ] } } ] } }
    > <- { "return": {} }
    >
    > -> { "execute": "migrate",
    >      "arguments": {
    >          "channels": [ { "channel-type": "main",
    >                          "addr": { "transport": "rdma",
    >                                    "host": "10.12.34.9",
    >                                    "port": "1050" } } ] } }
    > <- { "return": {} }
    >
    > -> { "execute": "migrate",
    >      "arguments": {
    >          "channels": [ { "channel-type": "main",
    >                          "addr": { "transport": "file",
    >                                    "filename": "/tmp/migfile",
    >                                    "offset": "0x1000" } } ] } }
    > <- { "return": {} }
    > ```

*Command* migrate-incoming (Since: 2.3)
:   Start an incoming migration. QEMU must have been started with
    -incoming defer.

    Arguments:
    :   - **uri** (`string`, *optional*) – The Uniform Resource Identifier identifying the source or
          address to listen on
        - **channels** (`[`[`MigrationChannel`](qemu-qmp-ref.md#object-QMP-migration.MigrationChannel "QMP:migration.MigrationChannel")`]`, *optional*) – list of migration stream channels with each stream in the
          list connected to a destination interface endpoint.
        - **exit-on-error** (`boolean`, *optional*) – Exit on incoming migration failure. Default true.
          When set to false, the failure triggers a
          [`MIGRATION`](qemu-qmp-ref.md#event-QMP-migration.MIGRATION "QMP:migration.MIGRATION") event, and error details could be
          retrieved with [`query-migrate`](qemu-qmp-ref.md#command-QMP-migration.query-migrate "QMP:migration.query-migrate"). (since 9.1)

    > **Notes:**
    >
    > 1. It’s a bad idea to use a string for the uri, but it needs to
    >    stay compatible with -incoming and the format of the uri is
    >    already exposed above libvirt.
    > 2. QEMU must be started with -incoming defer to allow
    >    [`migrate-incoming`](qemu-qmp-ref.md#command-QMP-migration.migrate-incoming "QMP:migration.migrate-incoming") to be used.
    > 3. The uri format is the same as for -incoming
    > 4. For now, number of migration streams is restricted to one,
    >    i.e. number of items in ‘channels’ list is just 1.
    > 5. The ‘uri’ and ‘channels’ arguments are mutually exclusive;
    >    exactly one of the two should be present.

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "migrate-incoming",
    >      "arguments": { "uri": "tcp:0:4446" } }
    > <- { "return": {} }
    >
    > -> { "execute": "migrate-incoming",
    >      "arguments": {
    >          "channels": [ { "channel-type": "main",
    >                          "addr": { "transport": "socket",
    >                                    "type": "inet",
    >                                    "host": "10.12.34.9",
    >                                    "port": "1050" } } ] } }
    > <- { "return": {} }
    >
    > -> { "execute": "migrate-incoming",
    >      "arguments": {
    >          "channels": [ { "channel-type": "main",
    >                          "addr": { "transport": "exec",
    >                                    "args": [ "/bin/nc", "-p", "6000",
    >                                              "/some/sock" ] } } ] } }
    > <- { "return": {} }
    >
    > -> { "execute": "migrate-incoming",
    >      "arguments": {
    >          "channels": [ { "channel-type": "main",
    >                          "addr": { "transport": "rdma",
    >                                    "host": "10.12.34.9",
    >                                    "port": "1050" } } ] } }
    > <- { "return": {} }
    > ```

*Command* xen-save-devices-state (Since: 1.1)
:   Save the state of all devices to file. The RAM and the block
    devices of the VM are not saved by this command.

    Arguments:
    :   - **filename** (`string`) – the file to save the state of the devices to as binary
          data. See [`xen-save-devices-state`](qemu-qmp-ref.md#command-QMP-migration.xen-save-devices-state "QMP:migration.xen-save-devices-state").txt for a description of the
          binary format.
        - **live** (`boolean`, *optional*) – Optional argument to ask QEMU to treat this command as part
          of a live migration. Default to true. (since 2.11)

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "xen-save-devices-state",
    >      "arguments": { "filename": "/tmp/save" } }
    > <- { "return": {} }
    > ```

*Command* xen-set-global-dirty-log (Since: 1.3)
:   Enable or disable the global dirty log mode.

    Arguments:
    :   - **enable** (`boolean`) – true to enable, false to disable.

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "xen-set-global-dirty-log",
    >      "arguments": { "enable": true } }
    > <- { "return": {} }
    > ```

*Command* xen-load-devices-state (Since: 2.7)
:   Load the state of all devices from file. The RAM and the block
    devices of the VM are not loaded by this command.

    Arguments:
    :   - **filename** (`string`) – the file to load the state of the devices from as binary
          data. See [`xen-save-devices-state`](qemu-qmp-ref.md#command-QMP-migration.xen-save-devices-state "QMP:migration.xen-save-devices-state").txt for a description of the
          binary format.

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "xen-load-devices-state",
    >      "arguments": { "filename": "/tmp/resume" } }
    > <- { "return": {} }
    > ```

*Command* xen-set-replication (Since: 2.9)
:   *Availability*: `CONFIG_REPLICATION`

    Enable or disable replication.

    Arguments:
    :   - **enable** (`boolean`) – true to enable, false to disable.
        - **primary** (`boolean`) – true for primary or false for secondary.
        - **failover** (`boolean`, *optional*) – true to do failover, false to stop. Cannot be specified
          if ‘enable’ is true. Default value is false.

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "xen-set-replication",
    >      "arguments": {"enable": true, "primary": false} }
    > <- { "return": {} }
    > ```

*Object* ReplicationStatus (Since: 2.9)
:   *Availability*: `CONFIG_REPLICATION`

    The result format for [`query-xen-replication-status`](qemu-qmp-ref.md#command-QMP-migration.query-xen-replication-status "QMP:migration.query-xen-replication-status").

    Members:
    :   - **error** (`boolean`) – true if an error happened, false if replication is normal.
        - **desc** (`string`, *optional*) – the human readable error description string, when `error` is
          ‘true’.

*Command* query-xen-replication-status (Since: 2.9)
:   *Availability*: `CONFIG_REPLICATION`

    Query replication status while the vm is running.

    Return:
    :   [`ReplicationStatus`](qemu-qmp-ref.md#object-QMP-migration.ReplicationStatus "QMP:migration.ReplicationStatus")

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "query-xen-replication-status" }
    > <- { "return": { "error": false } }
    > ```

*Command* xen-colo-do-checkpoint (Since: 2.9)
:   *Availability*: `CONFIG_REPLICATION`

    Xen uses this command to notify replication to trigger a checkpoint.

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "xen-colo-do-checkpoint" }
    > <- { "return": {} }
    > ```

*Object* COLOStatus (Since: 3.1)
:   *Availability*: `CONFIG_REPLICATION`

    The result format for [`query-colo-status`](qemu-qmp-ref.md#command-QMP-migration.query-colo-status "QMP:migration.query-colo-status").

    Members:
    :   - **mode** ([`COLOMode`](qemu-qmp-ref.md#enum-QMP-migration.COLOMode "QMP:migration.COLOMode")) – COLO running mode. If COLO is running, this field will
          return ‘primary’ or ‘secondary’.
        - **last-mode** ([`COLOMode`](qemu-qmp-ref.md#enum-QMP-migration.COLOMode "QMP:migration.COLOMode")) – COLO last running mode. If COLO is running, this field
          will return same like mode field, after failover we can use this
          field to get last colo mode. (since 4.0)
        - **reason** ([`COLOExitReason`](qemu-qmp-ref.md#enum-QMP-migration.COLOExitReason "QMP:migration.COLOExitReason")) – describes the reason for the COLO exit.

*Command* query-colo-status (Since: 3.1)
:   *Availability*: `CONFIG_REPLICATION`

    Query COLO status while the vm is running.

    Return:
    :   [`COLOStatus`](qemu-qmp-ref.md#object-QMP-migration.COLOStatus "QMP:migration.COLOStatus")

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "query-colo-status" }
    > <- { "return": { "mode": "primary", "last-mode": "none", "reason": "request" } }
    > ```

*Command* migrate-recover (Since: 3.0)
:   Provide a recovery migration stream URI.

    Arguments:
    :   - **uri** (`string`) – the URI to be used for the recovery of migration stream.

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "migrate-recover",
    >      "arguments": { "uri": "tcp:192.168.1.200:12345" } }
    > <- { "return": {} }
    > ```

*Command* migrate-pause (Since: 3.0)
:   Pause a migration. Currently it only supports postcopy.

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "migrate-pause" }
    > <- { "return": {} }
    > ```

*Event* UNPLUG_PRIMARY (Since: 4.2)
:   Emitted from source side of a migration when migration state is
    WAIT_UNPLUG. Device was unplugged by guest operating system.
    Device resources in QEMU are kept on standby to be able to re-plug
    it in case of migration failure.

    Members:
    :   - **device-id** (`string`) – QEMU device id of the unplugged device

    > **Example::**
    >
    > ```QMP
    > <- { "event": "UNPLUG_PRIMARY",
    >      "data": { "device-id": "hostdev0" },
    >      "timestamp": { "seconds": 1265044230, "microseconds": 450486 } }
    > ```

*Object* DirtyRateVcpu (Since: 6.2)
:   Dirty rate of vcpu.

    Members:
    :   - **id** (`int`) – vcpu index.
        - **dirty-rate** (`int`) – dirty rate.

*Enum* DirtyRateStatus (Since: 5.2)
:   Dirty page rate measurement status.

    Values:
    :   - **unstarted** – measuring thread has not been started yet
        - **measuring** – measuring thread is running
        - **measured** – dirty page rate is measured and the results are available

*Enum* DirtyRateMeasureMode (Since: 6.2)
:   Method used to measure dirty page rate. Differences between
    available methods are explained in [`calc-dirty-rate`](qemu-qmp-ref.md#command-QMP-migration.calc-dirty-rate "QMP:migration.calc-dirty-rate").

    Values:
    :   - **page-sampling** – use page sampling
        - **dirty-ring** – use dirty ring
        - **dirty-bitmap** – use dirty bitmap

*Enum* TimeUnit (Since: 8.2)
:   Specifies unit in which time-related value is specified.

    Values:
    :   - **second** – value is in seconds
        - **millisecond** – value is in milliseconds

*Object* DirtyRateInfo (Since: 5.2)
:   Information about measured dirty page rate.

    Members:
    :   - **dirty-rate** (`int`, *optional*) – an estimate of the dirty page rate of the VM in units
          of MiB/s. Value is present only when `status` is ‘measured’.
        - **status** ([`DirtyRateStatus`](qemu-qmp-ref.md#enum-QMP-migration.DirtyRateStatus "QMP:migration.DirtyRateStatus")) – current status of dirty page rate measurements
        - **start-time** (`int`) – start time in units of second for calculation
        - **calc-time** (`int`) – time period for which dirty page rate was measured,
          expressed and rounded down to `calc-time-unit`.
        - **calc-time-unit** ([`TimeUnit`](qemu-qmp-ref.md#enum-QMP-migration.TimeUnit "QMP:migration.TimeUnit")) – time unit of `calc-time` (Since 8.2)
        - **sample-pages** (`int`) – number of sampled pages per GiB of guest memory.
          Valid only in page-sampling mode (Since 6.1)
        - **mode** ([`DirtyRateMeasureMode`](qemu-qmp-ref.md#enum-QMP-migration.DirtyRateMeasureMode "QMP:migration.DirtyRateMeasureMode")) – mode that was used to measure dirty page rate (Since 6.2)
        - **vcpu-dirty-rate** (`[`[`DirtyRateVcpu`](qemu-qmp-ref.md#object-QMP-migration.DirtyRateVcpu "QMP:migration.DirtyRateVcpu")`]`, *optional*) – dirty rate for each vCPU if dirty-ring mode was
          specified (Since 6.2)

*Command* calc-dirty-rate (Since: 5.2)
:   Start measuring dirty page rate of the VM. Results can be retrieved
    with [`query-dirty-rate`](qemu-qmp-ref.md#command-QMP-migration.query-dirty-rate "QMP:migration.query-dirty-rate") after measurements are completed.

    Dirty page rate is the number of pages changed in a given time
    period expressed in MiB/s. The following methods of calculation are
    available:

    1. In page sampling mode, a random subset of pages are selected and
       hashed twice: once at the beginning of measurement time period,
       and once again at the end. If two hashes for some page are
       different, the page is counted as changed. Since this method
       relies on sampling and hashing, calculated dirty page rate is
       only an estimate of its true value. Increasing `sample-pages`
       improves estimation quality at the cost of higher computational
       overhead.
    2. Dirty bitmap mode captures writes to memory (for example by
       temporarily revoking write access to all pages) and counting page
       faults. Information about modified pages is collected into a
       bitmap, where each bit corresponds to one guest page. This mode
       requires that KVM accelerator property “dirty-ring-size” is *not*
       set.
    3. Dirty ring mode is similar to dirty bitmap mode, but the
       information about modified pages is collected into ring buffer.
       This mode tracks page modification per each vCPU separately. It
       requires that KVM accelerator property “dirty-ring-size” is set.

    Arguments:
    :   - **calc-time** (`int`) – time period for which dirty page rate is calculated. By
          default it is specified in seconds, but the unit can be set
          explicitly with `calc-time-unit`. Note that larger `calc-time`
          values will typically result in smaller dirty page rates because
          page dirtying is a one-time event. Once some page is counted as
          dirty during `calc-time` period, further writes to this page will
          not increase dirty page rate anymore.
        - **calc-time-unit** ([`TimeUnit`](qemu-qmp-ref.md#enum-QMP-migration.TimeUnit "QMP:migration.TimeUnit"), *optional*) – time unit in which `calc-time` is specified. By
          default it is seconds. (Since 8.2)
        - **sample-pages** (`int`, *optional*) – number of sampled pages per each GiB of guest memory.
          Default value is 512. For 4KiB guest pages this corresponds to
          sampling ratio of 0.2%. This argument is used only in page
          sampling mode. (Since 6.1)
        - **mode** ([`DirtyRateMeasureMode`](qemu-qmp-ref.md#enum-QMP-migration.DirtyRateMeasureMode "QMP:migration.DirtyRateMeasureMode"), *optional*) – mechanism for tracking dirty pages. Default value is
          ‘page-sampling’. Others are ‘dirty-bitmap’ and ‘dirty-ring’.
          (Since 6.1)

    > **Example::**
    >
    > ```QMP
    > -> {"execute": "calc-dirty-rate", "arguments": {"calc-time": 1,
    >                                                 "sample-pages": 512} }
    > <- { "return": {} }
    > ```

    > **Example::**
    >
    > Measure dirty rate using dirty bitmap for 500 milliseconds:
    >
    > ```QMP
    > -> {"execute": "calc-dirty-rate", "arguments": {"calc-time": 500,
    >     "calc-time-unit": "millisecond", "mode": "dirty-bitmap"} }
    >
    > <- { "return": {} }
    > ```

*Command* query-dirty-rate (Since: 5.2)
:   Query results of the most recent invocation of [`calc-dirty-rate`](qemu-qmp-ref.md#command-QMP-migration.calc-dirty-rate "QMP:migration.calc-dirty-rate").

    Arguments:
    :   - **calc-time-unit** ([`TimeUnit`](qemu-qmp-ref.md#enum-QMP-migration.TimeUnit "QMP:migration.TimeUnit"), *optional*) – time unit in which to report calculation time.
          By default it is reported in seconds. (Since 8.2)

    Return:
    :   [`DirtyRateInfo`](qemu-qmp-ref.md#object-QMP-migration.DirtyRateInfo "QMP:migration.DirtyRateInfo")

    > **Example: Measurement is in progress:**
    >
    > ```QMP
    >  <- {"status": "measuring", "sample-pages": 512,
    >      "mode": "page-sampling", "start-time": 1693900454, "calc-time": 10,
    >      "calc-time-unit": "second"}
    > ```

    > **Example: Measurement has been completed:**
    >
    > ```QMP
    >  <- {"status": "measured", "sample-pages": 512, "dirty-rate": 108,
    >      "mode": "page-sampling", "start-time": 1693900454, "calc-time": 10,
    >      "calc-time-unit": "second"}
    > ```

*Object* DirtyLimitInfo (Since: 7.1)
:   Dirty page rate limit information of a virtual CPU.

    Members:
    :   - **cpu-index** (`int`) – index of a virtual CPU.
        - **limit-rate** (`int`) – upper limit of dirty page rate (MB/s) for a virtual
          CPU, 0 means unlimited.
        - **current-rate** (`int`) – current dirty page rate (MB/s) for a virtual CPU.

*Command* set-vcpu-dirty-limit (Since: 7.1)
:   Set the upper limit of dirty page rate for virtual CPUs.

    Requires KVM with accelerator property “dirty-ring-size” set. A
    virtual CPU’s dirty page rate is a measure of its memory load. To
    observe dirty page rates, use [`calc-dirty-rate`](qemu-qmp-ref.md#command-QMP-migration.calc-dirty-rate "QMP:migration.calc-dirty-rate").

    Arguments:
    :   - **cpu-index** (`int`, *optional*) – index of a virtual CPU, default is all.
        - **dirty-rate** (`int`) – upper limit of dirty page rate (MB/s) for virtual CPUs.

    > **Example::**
    >
    > ```QMP
    > -> {"execute": "set-vcpu-dirty-limit"}
    >     "arguments": { "dirty-rate": 200,
    >                    "cpu-index": 1 } }
    > <- { "return": {} }
    > ```

*Command* cancel-vcpu-dirty-limit (Since: 7.1)
:   Cancel the upper limit of dirty page rate for virtual CPUs.

    Cancel the dirty page limit for the vCPU which has been set with
    [`set-vcpu-dirty-limit`](qemu-qmp-ref.md#command-QMP-migration.set-vcpu-dirty-limit "QMP:migration.set-vcpu-dirty-limit") command. Note that this command requires
    support from dirty ring, same as the [`set-vcpu-dirty-limit`](qemu-qmp-ref.md#command-QMP-migration.set-vcpu-dirty-limit "QMP:migration.set-vcpu-dirty-limit").

    Arguments:
    :   - **cpu-index** (`int`, *optional*) – index of a virtual CPU, default is all.

    > **Example::**
    >
    > ```QMP
    > -> {"execute": "cancel-vcpu-dirty-limit"},
    >     "arguments": { "cpu-index": 1 } }
    > <- { "return": {} }
    > ```

*Command* query-vcpu-dirty-limit (Since: 7.1)
:   Return information about virtual CPU dirty page rate limits, if any.

    Return:
    :   `[`[`DirtyLimitInfo`](qemu-qmp-ref.md#object-QMP-migration.DirtyLimitInfo "QMP:migration.DirtyLimitInfo")`]`

    > **Example::**
    >
    > ```QMP
    > -> {"execute": "query-vcpu-dirty-limit"}
    > <- {"return": [
    >        { "limit-rate": 60, "current-rate": 3, "cpu-index": 0},
    >        { "limit-rate": 60, "current-rate": 3, "cpu-index": 1}]}
    > ```

*Command* snapshot-save (Since: 6.0)
:   Save a VM snapshot

    Arguments:
    :   - **job-id** (`string`) – identifier for the newly created job
        - **tag** (`string`) – name of the snapshot to create
        - **vmstate** (`string`) – block device node name to save vmstate to
        - **devices** (`[``string``]`) – list of block device node names to save a snapshot to

    Applications should not assume that the snapshot save is complete
    when this command returns. The job commands / events must be used
    to determine completion and to fetch details of any errors that
    arise.

    Note that execution of the guest CPUs may be stopped during the time
    it takes to save the snapshot. A future version of QEMU may ensure
    CPUs are executing continuously.

    It is strongly recommended that `devices` contain all writable block
    device nodes if a consistent snapshot is required.

    If `tag` already exists, an error will be reported

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "snapshot-save",
    >      "arguments": {
    >         "job-id": "snapsave0",
    >         "tag": "my-snap",
    >         "vmstate": "disk0",
    >         "devices": ["disk0", "disk1"]
    >      }
    >    }
    > <- { "return": { } }
    > <- {"event": "JOB_STATUS_CHANGE",
    >     "timestamp": {"seconds": 1432121972, "microseconds": 744001},
    >     "data": {"status": "created", "id": "snapsave0"}}
    > <- {"event": "JOB_STATUS_CHANGE",
    >     "timestamp": {"seconds": 1432122172, "microseconds": 744001},
    >     "data": {"status": "running", "id": "snapsave0"}}
    > <- {"event": "STOP",
    >     "timestamp": {"seconds": 1432122372, "microseconds": 744001} }
    > <- {"event": "RESUME",
    >     "timestamp": {"seconds": 1432122572, "microseconds": 744001} }
    > <- {"event": "JOB_STATUS_CHANGE",
    >     "timestamp": {"seconds": 1432122772, "microseconds": 744001},
    >     "data": {"status": "waiting", "id": "snapsave0"}}
    > <- {"event": "JOB_STATUS_CHANGE",
    >     "timestamp": {"seconds": 1432122972, "microseconds": 744001},
    >     "data": {"status": "pending", "id": "snapsave0"}}
    > <- {"event": "JOB_STATUS_CHANGE",
    >     "timestamp": {"seconds": 1432123172, "microseconds": 744001},
    >     "data": {"status": "concluded", "id": "snapsave0"}}
    > -> {"execute": "query-jobs"}
    > <- {"return": [{"current-progress": 1,
    >                 "status": "concluded",
    >                 "total-progress": 1,
    >                 "type": "snapshot-save",
    >                 "id": "snapsave0"}]}
    > ```

*Command* snapshot-load (Since: 6.0)
:   Load a VM snapshot

    Arguments:
    :   - **job-id** (`string`) – identifier for the newly created job
        - **tag** (`string`) – name of the snapshot to load.
        - **vmstate** (`string`) – block device node name to load vmstate from
        - **devices** (`[``string``]`) – list of block device node names to load a snapshot from

    Applications should not assume that the snapshot load is complete
    when this command returns. The job commands / events must be used
    to determine completion and to fetch details of any errors that
    arise.

    Note that execution of the guest CPUs will be stopped during the
    time it takes to load the snapshot.

    It is strongly recommended that `devices` contain all writable block
    device nodes that can have changed since the original
    [`snapshot-save`](qemu-qmp-ref.md#command-QMP-migration.snapshot-save "QMP:migration.snapshot-save") command execution.

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "snapshot-load",
    >      "arguments": {
    >         "job-id": "snapload0",
    >         "tag": "my-snap",
    >         "vmstate": "disk0",
    >         "devices": ["disk0", "disk1"]
    >      }
    >    }
    > <- { "return": { } }
    > <- {"event": "JOB_STATUS_CHANGE",
    >     "timestamp": {"seconds": 1472124172, "microseconds": 744001},
    >     "data": {"status": "created", "id": "snapload0"}}
    > <- {"event": "JOB_STATUS_CHANGE",
    >     "timestamp": {"seconds": 1472125172, "microseconds": 744001},
    >     "data": {"status": "running", "id": "snapload0"}}
    > <- {"event": "STOP",
    >     "timestamp": {"seconds": 1472125472, "microseconds": 744001} }
    > <- {"event": "RESUME",
    >     "timestamp": {"seconds": 1472125872, "microseconds": 744001} }
    > <- {"event": "JOB_STATUS_CHANGE",
    >     "timestamp": {"seconds": 1472126172, "microseconds": 744001},
    >     "data": {"status": "waiting", "id": "snapload0"}}
    > <- {"event": "JOB_STATUS_CHANGE",
    >     "timestamp": {"seconds": 1472127172, "microseconds": 744001},
    >     "data": {"status": "pending", "id": "snapload0"}}
    > <- {"event": "JOB_STATUS_CHANGE",
    >     "timestamp": {"seconds": 1472128172, "microseconds": 744001},
    >     "data": {"status": "concluded", "id": "snapload0"}}
    > -> {"execute": "query-jobs"}
    > <- {"return": [{"current-progress": 1,
    >                 "status": "concluded",
    >                 "total-progress": 1,
    >                 "type": "snapshot-load",
    >                 "id": "snapload0"}]}
    > ```

*Command* snapshot-delete (Since: 6.0)
:   Delete a VM snapshot

    Arguments:
    :   - **job-id** (`string`) – identifier for the newly created job
        - **tag** (`string`) – name of the snapshot to delete.
        - **devices** (`[``string``]`) – list of block device node names to delete a snapshot from

    Applications should not assume that the snapshot delete is complete
    when this command returns. The job commands / events must be used
    to determine completion and to fetch details of any errors that
    arise.

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "snapshot-delete",
    >      "arguments": {
    >         "job-id": "snapdelete0",
    >         "tag": "my-snap",
    >         "devices": ["disk0", "disk1"]
    >      }
    >    }
    > <- { "return": { } }
    > <- {"event": "JOB_STATUS_CHANGE",
    >     "timestamp": {"seconds": 1442124172, "microseconds": 744001},
    >     "data": {"status": "created", "id": "snapdelete0"}}
    > <- {"event": "JOB_STATUS_CHANGE",
    >     "timestamp": {"seconds": 1442125172, "microseconds": 744001},
    >     "data": {"status": "running", "id": "snapdelete0"}}
    > <- {"event": "JOB_STATUS_CHANGE",
    >     "timestamp": {"seconds": 1442126172, "microseconds": 744001},
    >     "data": {"status": "waiting", "id": "snapdelete0"}}
    > <- {"event": "JOB_STATUS_CHANGE",
    >     "timestamp": {"seconds": 1442127172, "microseconds": 744001},
    >     "data": {"status": "pending", "id": "snapdelete0"}}
    > <- {"event": "JOB_STATUS_CHANGE",
    >     "timestamp": {"seconds": 1442128172, "microseconds": 744001},
    >     "data": {"status": "concluded", "id": "snapdelete0"}}
    > -> {"execute": "query-jobs"}
    > <- {"return": [{"current-progress": 1,
    >                 "status": "concluded",
    >                 "total-progress": 1,
    >                 "type": "snapshot-delete",
    >                 "id": "snapdelete0"}]}
    > ```

## [Transactions](qemu-qmp-ref.md#id26)

*Object* Abort (Since: 1.6)
:   This action can be used to test transaction failure.

*Enum* ActionCompletionMode (Since: 2.5)
:   An enumeration of transactional completion modes.

    Values:
    :   - **individual** – Do not attempt to cancel any other Actions if any
          Actions fail after the Transaction request succeeds. All
          Actions that can complete successfully will do so without
          waiting on others. This is the default.
        - **grouped** – If any Action fails after the Transaction succeeds, cancel
          all Actions. Actions do not complete until all Actions are
          ready to complete. May be rejected by Actions that do not
          support this completion mode.

*Enum* TransactionActionKind (Since: 1.1)
:   Values:
    :   - **abort** – Since 1.6
        - **block-dirty-bitmap-add** – Since 2.5
        - **block-dirty-bitmap-remove** – Since 4.2
        - **block-dirty-bitmap-clear** – Since 2.5
        - **block-dirty-bitmap-enable** – Since 4.0
        - **block-dirty-bitmap-disable** – Since 4.0
        - **block-dirty-bitmap-merge** – Since 4.0
        - **blockdev-backup** – Since 2.3
        - **blockdev-snapshot** – Since 2.5
        - **blockdev-snapshot-internal-sync** – Since 1.7
        - **blockdev-snapshot-sync** – since 1.1
        - **drive-backup** – Since 1.6

    Features:
    :   - **deprecated** – Member [`drive-backup`](qemu-qmp-ref.md#command-QMP-block-core.drive-backup "QMP:block-core.drive-backup") is deprecated. Use member
          [`blockdev-backup`](qemu-qmp-ref.md#command-QMP-block-core.blockdev-backup "QMP:block-core.blockdev-backup") instead.

*Object* AbortWrapper (Since: 1.6)
:   Members:
    :   - **data** ([`Abort`](qemu-qmp-ref.md#object-QMP-transaction.Abort "QMP:transaction.Abort")) – Not documented

*Object* BlockDirtyBitmapAddWrapper (Since: 2.5)
:   Members:
    :   - **data** ([`BlockDirtyBitmapAdd`](qemu-qmp-ref.md#object-QMP-block-core.BlockDirtyBitmapAdd "QMP:block-core.BlockDirtyBitmapAdd")) – Not documented

*Object* BlockDirtyBitmapWrapper (Since: 2.5)
:   Members:
    :   - **data** ([`BlockDirtyBitmap`](qemu-qmp-ref.md#object-QMP-block-core.BlockDirtyBitmap "QMP:block-core.BlockDirtyBitmap")) – Not documented

*Object* BlockDirtyBitmapMergeWrapper (Since: 4.0)
:   Members:
    :   - **data** ([`BlockDirtyBitmapMerge`](qemu-qmp-ref.md#object-QMP-block-core.BlockDirtyBitmapMerge "QMP:block-core.BlockDirtyBitmapMerge")) – Not documented

*Object* BlockdevBackupWrapper (Since: 2.3)
:   Members:
    :   - **data** ([`BlockdevBackup`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevBackup "QMP:block-core.BlockdevBackup")) – Not documented

*Object* BlockdevSnapshotWrapper (Since: 2.5)
:   Members:
    :   - **data** ([`BlockdevSnapshot`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevSnapshot "QMP:block-core.BlockdevSnapshot")) – Not documented

*Object* BlockdevSnapshotInternalWrapper (Since: 1.7)
:   Members:
    :   - **data** ([`BlockdevSnapshotInternal`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevSnapshotInternal "QMP:block-core.BlockdevSnapshotInternal")) – Not documented

*Object* BlockdevSnapshotSyncWrapper (Since: 1.1)
:   Members:
    :   - **data** ([`BlockdevSnapshotSync`](qemu-qmp-ref.md#object-QMP-block-core.BlockdevSnapshotSync "QMP:block-core.BlockdevSnapshotSync")) – Not documented

*Object* DriveBackupWrapper (Since: 1.6)
:   Members:
    :   - **data** ([`DriveBackup`](qemu-qmp-ref.md#object-QMP-block-core.DriveBackup "QMP:block-core.DriveBackup")) – Not documented

*Object* TransactionAction (Since: 1.1)
:   A discriminated record of operations that can be performed with
    [`transaction`](qemu-qmp-ref.md#command-QMP-transaction.transaction "QMP:transaction.transaction").

    Members:
    :   - **type** ([`TransactionActionKind`](qemu-qmp-ref.md#enum-QMP-transaction.TransactionActionKind "QMP:transaction.TransactionActionKind")) – the operation to be performed
        - When `type` is `abort`: The members of [`AbortWrapper`](qemu-qmp-ref.md#object-QMP-transaction.AbortWrapper "QMP:transaction.AbortWrapper").
        - When `type` is `block-dirty-bitmap-add`: The members of [`BlockDirtyBitmapAddWrapper`](qemu-qmp-ref.md#object-QMP-transaction.BlockDirtyBitmapAddWrapper "QMP:transaction.BlockDirtyBitmapAddWrapper").
        - When `type` is `block-dirty-bitmap-remove`: The members of [`BlockDirtyBitmapWrapper`](qemu-qmp-ref.md#object-QMP-transaction.BlockDirtyBitmapWrapper "QMP:transaction.BlockDirtyBitmapWrapper").
        - When `type` is `block-dirty-bitmap-clear`: The members of [`BlockDirtyBitmapWrapper`](qemu-qmp-ref.md#object-QMP-transaction.BlockDirtyBitmapWrapper "QMP:transaction.BlockDirtyBitmapWrapper").
        - When `type` is `block-dirty-bitmap-enable`: The members of [`BlockDirtyBitmapWrapper`](qemu-qmp-ref.md#object-QMP-transaction.BlockDirtyBitmapWrapper "QMP:transaction.BlockDirtyBitmapWrapper").
        - When `type` is `block-dirty-bitmap-disable`: The members of [`BlockDirtyBitmapWrapper`](qemu-qmp-ref.md#object-QMP-transaction.BlockDirtyBitmapWrapper "QMP:transaction.BlockDirtyBitmapWrapper").
        - When `type` is `block-dirty-bitmap-merge`: The members of [`BlockDirtyBitmapMergeWrapper`](qemu-qmp-ref.md#object-QMP-transaction.BlockDirtyBitmapMergeWrapper "QMP:transaction.BlockDirtyBitmapMergeWrapper").
        - When `type` is `blockdev-backup`: The members of [`BlockdevBackupWrapper`](qemu-qmp-ref.md#object-QMP-transaction.BlockdevBackupWrapper "QMP:transaction.BlockdevBackupWrapper").
        - When `type` is `blockdev-snapshot`: The members of [`BlockdevSnapshotWrapper`](qemu-qmp-ref.md#object-QMP-transaction.BlockdevSnapshotWrapper "QMP:transaction.BlockdevSnapshotWrapper").
        - When `type` is `blockdev-snapshot-internal-sync`: The members of [`BlockdevSnapshotInternalWrapper`](qemu-qmp-ref.md#object-QMP-transaction.BlockdevSnapshotInternalWrapper "QMP:transaction.BlockdevSnapshotInternalWrapper").
        - When `type` is `blockdev-snapshot-sync`: The members of [`BlockdevSnapshotSyncWrapper`](qemu-qmp-ref.md#object-QMP-transaction.BlockdevSnapshotSyncWrapper "QMP:transaction.BlockdevSnapshotSyncWrapper").
        - When `type` is `drive-backup`: The members of [`DriveBackupWrapper`](qemu-qmp-ref.md#object-QMP-transaction.DriveBackupWrapper "QMP:transaction.DriveBackupWrapper").

*Object* TransactionProperties (Since: 2.5)
:   Optional arguments to modify the behavior of a Transaction.

    Members:
    :   - **completion-mode** ([`ActionCompletionMode`](qemu-qmp-ref.md#enum-QMP-transaction.ActionCompletionMode "QMP:transaction.ActionCompletionMode"), *optional*) – Controls how jobs launched asynchronously by
          Actions will complete or fail as a group. See
          [`ActionCompletionMode`](qemu-qmp-ref.md#enum-QMP-transaction.ActionCompletionMode "QMP:transaction.ActionCompletionMode") for details.

*Command* transaction (Since: 1.1)
:   Executes a number of transactionable QMP commands atomically. If
    any operation fails, then the entire set of actions will be
    abandoned and the appropriate error returned.

    For external snapshots, the dictionary contains the device, the file
    to use for the new snapshot, and the format. The default format, if
    not specified, is qcow2.

    Each new snapshot defaults to being created by QEMU (wiping any
    contents if the file already exists), but it is also possible to
    reuse an externally-created file. In the latter case, you should
    ensure that the new image file has the same contents as the current
    one; QEMU cannot perform any meaningful check. Typically this is
    achieved by using the current image file as the backing file for the
    new image.

    On failure, the original disks pre-snapshot attempt will be used.

    For internal snapshots, the dictionary contains the device and the
    snapshot’s name. If an internal snapshot matching name already
    exists, the request will be rejected. Only some image formats
    support it, for example, qcow2, and rbd,

    On failure, QEMU will try delete the newly created internal snapshot
    in the transaction. When an I/O error occurs during deletion, the
    user needs to fix it later with qemu-img or other command.

    Arguments:
    :   - **actions** (`[`[`TransactionAction`](qemu-qmp-ref.md#object-QMP-transaction.TransactionAction "QMP:transaction.TransactionAction")`]`) – List of [`TransactionAction`](qemu-qmp-ref.md#object-QMP-transaction.TransactionAction "QMP:transaction.TransactionAction"); information needed for the
          respective operations.
        - **properties** ([`TransactionProperties`](qemu-qmp-ref.md#object-QMP-transaction.TransactionProperties "QMP:transaction.TransactionProperties"), *optional*) – structure of additional options to control the
          execution of the transaction. See [`TransactionProperties`](qemu-qmp-ref.md#object-QMP-transaction.TransactionProperties "QMP:transaction.TransactionProperties") for
          additional detail.

    Errors:
    :   - Any errors from commands in the transaction

    > **Note:**
    >
    > The transaction aborts on the first failure. Therefore,
    > there will be information on only one failed operation returned
    > in an error condition, and subsequent actions will not have been
    > attempted.

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "transaction",
    >      "arguments": { "actions": [
    >          { "type": "blockdev-snapshot-sync", "data" : { "device": "ide-hd0",
    >                                      "snapshot-file": "/some/place/my-image",
    >                                      "format": "qcow2" } },
    >          { "type": "blockdev-snapshot-sync", "data" : { "node-name": "myfile",
    >                                      "snapshot-file": "/some/place/my-image2",
    >                                      "snapshot-node-name": "node3432",
    >                                      "mode": "existing",
    >                                      "format": "qcow2" } },
    >          { "type": "blockdev-snapshot-sync", "data" : { "device": "ide-hd1",
    >                                      "snapshot-file": "/some/place/my-image2",
    >                                      "mode": "existing",
    >                                      "format": "qcow2" } },
    >          { "type": "blockdev-snapshot-internal-sync", "data" : {
    >                                      "device": "ide-hd2",
    >                                      "name": "snapshot0" } } ] } }
    > <- { "return": {} }
    > ```

## [Tracing](qemu-qmp-ref.md#id27)

*Enum* TraceEventState (Since: 2.2)
:   State of a tracing event.

    Values:
    :   - **unavailable** – The event is statically disabled.
        - **disabled** – The event is dynamically disabled.
        - **enabled** – The event is dynamically enabled.

*Object* TraceEventInfo (Since: 2.2)
:   Information of a tracing event.

    Members:
    :   - **name** (`string`) – Event name.
        - **state** ([`TraceEventState`](qemu-qmp-ref.md#enum-QMP-trace.TraceEventState "QMP:trace.TraceEventState")) – Tracing state.

*Command* trace-event-get-state (Since: 2.2)
:   Query the state of events.

    Arguments:
    :   - **name** (`string`) – Event name pattern (case-sensitive glob).

    Return:
    :   `[`[`TraceEventInfo`](qemu-qmp-ref.md#object-QMP-trace.TraceEventInfo "QMP:trace.TraceEventInfo")`]` – a list of info for the matching events

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "trace-event-get-state",
    >      "arguments": { "name": "qemu_memalign" } }
    > <- { "return": [ { "name": "qemu_memalign", "state": "disabled", "vcpu": false } ] }
    > ```

*Command* trace-event-set-state (Since: 2.2)
:   Set the dynamic tracing state of events.

    Arguments:
    :   - **name** (`string`) – Event name pattern (case-sensitive glob).
        - **enable** (`boolean`) – Whether to enable tracing.
        - **ignore-unavailable** (`boolean`, *optional*) – Do not match unavailable events with `name`.

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "trace-event-set-state",
    >      "arguments": { "name": "qemu_memalign", "enable": true } }
    > <- { "return": {} }
    > ```

## [Compatibility policy](qemu-qmp-ref.md#id28)

*Enum* CompatPolicyInput (Since: 6.0)
:   Policy for handling “funny” input.

    Values:
    :   - **accept** – Accept silently
        - **reject** – Reject with an error
        - **crash** – abort() the process

*Enum* CompatPolicyOutput (Since: 6.0)
:   Policy for handling “funny” output.

    Values:
    :   - **accept** – Pass on unchanged
        - **hide** – Filter out

*Object* CompatPolicy (Since: 6.0)
:   Policy for handling deprecated management interfaces.

    This is intended for testing users of the management interfaces.

    Limitation: covers only syntactic aspects of QMP, i.e. stuff tagged
    with feature ‘deprecated’ or ‘unstable’. We may want to extend it
    to cover semantic aspects and CLI.

    Limitation: deprecated-output policy `hide` is not implemented for
    enumeration values. They behave the same as with policy `accept`.

    Members:
    :   - **deprecated-input** ([`CompatPolicyInput`](qemu-qmp-ref.md#enum-QMP-compat.CompatPolicyInput "QMP:compat.CompatPolicyInput"), *optional*) – how to handle deprecated input (default ‘accept’)
        - **deprecated-output** ([`CompatPolicyOutput`](qemu-qmp-ref.md#enum-QMP-compat.CompatPolicyOutput "QMP:compat.CompatPolicyOutput"), *optional*) – how to handle deprecated output (default
          ‘accept’)
        - **unstable-input** ([`CompatPolicyInput`](qemu-qmp-ref.md#enum-QMP-compat.CompatPolicyInput "QMP:compat.CompatPolicyInput"), *optional*) – how to handle unstable input (default ‘accept’)
          (since 6.2)
        - **unstable-output** ([`CompatPolicyOutput`](qemu-qmp-ref.md#enum-QMP-compat.CompatPolicyOutput "QMP:compat.CompatPolicyOutput"), *optional*) – how to handle unstable output (default ‘accept’)
          (since 6.2)

## [QMP monitor control](qemu-qmp-ref.md#id29)

*Command* qmp_capabilities (Since: 0.13)
:   Enable QMP capabilities.

    Arguments:
    :   - **enable** (`[`[`QMPCapability`](qemu-qmp-ref.md#enum-QMP-control.QMPCapability "QMP:control.QMPCapability")`]`, *optional*) – An optional list of [`QMPCapability`](qemu-qmp-ref.md#enum-QMP-control.QMPCapability "QMP:control.QMPCapability") values to enable. The
          client must not enable any capability that is not mentioned in
          the QMP greeting message. If the field is not provided, it
          means no QMP capabilities will be enabled. (since 2.12)

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "qmp_capabilities",
    >      "arguments": { "enable": [ "oob" ] } }
    > <- { "return": {} }
    > ```

    > **Note:**
    >
    > This command is valid exactly when first connecting: it
    > must be issued before any other command will be accepted, and
    > will fail once the monitor is accepting other commands. (see
    > [QEMU Machine Protocol Specification](qmp-spec.md))

    > **Note:**
    >
    > The QMP client needs to explicitly enable QMP
    > capabilities, otherwise all the QMP capabilities will be turned
    > off by default.

*Enum* QMPCapability (Since: 2.12)
:   Enumeration of capabilities to be advertised during initial client
    connection, used for agreeing on particular QMP extension behaviors.

    Values:
    :   - **oob** – QMP ability to support out-of-band requests. (Please refer to
          qmp-spec.rst for more information on OOB)

*Object* VersionTriple (Since: 2.4)
:   A three-part version number.

    Members:
    :   - **major** (`int`) – The major version number.
        - **minor** (`int`) – The minor version number.
        - **micro** (`int`) – The micro version number.

*Object* VersionInfo (Since: 0.14)
:   A description of QEMU’s version.

    Members:
    :   - **qemu** ([`VersionTriple`](qemu-qmp-ref.md#object-QMP-control.VersionTriple "QMP:control.VersionTriple")) – The version of QEMU. By current convention, a micro version
          of 50 signifies a development branch. A micro version greater
          than or equal to 90 signifies a release candidate for the next
          minor version. A micro version of less than 50 signifies a
          stable release.
        - **package** (`string`) – QEMU will always set this field to an empty string.
          Downstream versions of QEMU should set this to a non-empty
          string. The exact format depends on the downstream however it
          highly recommended that a unique name is used.

*Command* query-version (Since: 0.14)
:   Return the current version of QEMU.

    Return:
    :   [`VersionInfo`](qemu-qmp-ref.md#object-QMP-control.VersionInfo "QMP:control.VersionInfo") – An object describing the current version of QEMU.

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "query-version" }
    > <- {
    >       "return":{
    >          "qemu":{
    >             "major":0,
    >             "minor":11,
    >             "micro":5
    >          },
    >          "package":""
    >       }
    >    }
    > ```

*Object* CommandInfo (Since: 0.14)
:   Information about a QMP command

    Members:
    :   - **name** (`string`) – The command name

*Command* query-commands (Since: 0.14)
:   Return a list of supported QMP commands by this server

    Return:
    :   `[`[`CommandInfo`](qemu-qmp-ref.md#object-QMP-control.CommandInfo "QMP:control.CommandInfo")`]` – A list of all supported commands

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "query-commands" }
    > <- {
    >      "return":[
    >         {
    >            "name":"query-balloon"
    >         },
    >         {
    >            "name":"system_powerdown"
    >         },
    >         ...
    >      ]
    >    }
    > ```

    This example has been shortened as the real response is too long.

*Command* quit (Since: 0.14)
:   Request graceful QEMU process termination.

    While every attempt is made to send the QMP response before
    terminating, this is not guaranteed. When using this interface, a
    premature EOF would not be unexpected.

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "quit" }
    > <- { "return": {} }
    > ```

*Enum* MonitorMode (Since: 5.0)
:   An enumeration of monitor modes.

    Values:
    :   - **readline** – HMP monitor (human-oriented command line interface)
        - **control** – QMP monitor (JSON-based machine interface)

*Object* MonitorOptions (Since: 5.0)
:   Options to be used for adding a new monitor.

    Members:
    :   - **id** (`string`, *optional*) – Name of the monitor
        - **mode** ([`MonitorMode`](qemu-qmp-ref.md#enum-QMP-control.MonitorMode "QMP:control.MonitorMode"), *optional*) – Selects the monitor mode (default: readline in the system
          emulator, control in qemu-storage-daemon)
        - **pretty** (`boolean`, *optional*) – Enables pretty printing (QMP only)
        - **chardev** (`string`) – Name of a character device to expose the monitor on

## [QMP introspection](qemu-qmp-ref.md#id30)

*Command* query-qmp-schema (Since: 2.5)
:   Command [`query-qmp-schema`](qemu-qmp-ref.md#command-QMP-introspect.query-qmp-schema "QMP:introspect.query-qmp-schema") exposes the QMP wire ABI as an array of
    [`SchemaInfo`](qemu-qmp-ref.md#object-QMP-introspect.SchemaInfo "QMP:introspect.SchemaInfo"). This lets QMP clients figure out what commands and
    events are available in this QEMU, and their parameters and results.

    However, the [`SchemaInfo`](qemu-qmp-ref.md#object-QMP-introspect.SchemaInfo "QMP:introspect.SchemaInfo") can’t reflect all the rules and
    restrictions that apply to QMP. It’s interface introspection
    (figuring out what’s there), not interface specification. The
    specification is in the QAPI schema.

    Furthermore, while we strive to keep the QMP wire format
    backwards-compatible across QEMU versions, the introspection output
    is not guaranteed to have the same stability. For example, one
    version of QEMU may list an object member as an optional
    non-variant, while another lists the same member only through the
    object’s variants; or the type of a member may change from a generic
    string into a specific enum or from one specific type into an
    alternate that includes the original type alongside something else.

    Return:
    :   `[`[`SchemaInfo`](qemu-qmp-ref.md#object-QMP-introspect.SchemaInfo "QMP:introspect.SchemaInfo")`]` –

        an array where each element describes an entity in the ABI:
        command, event, type, …

        The order of the various elements is unspecified; however, all
        names are guaranteed to be unique (no name will be duplicated
        with different meta-types).

    > **Note:**
    >
    > The QAPI schema is also used to help define *internal*
    > interfaces, by defining QAPI types. These are not part of the
    > QMP wire ABI, and therefore not returned by this command.

*Enum* SchemaMetaType (Since: 2.5)
:   This is a [`SchemaInfo`](qemu-qmp-ref.md#object-QMP-introspect.SchemaInfo "QMP:introspect.SchemaInfo")’s meta type, i.e. the kind of entity it
    describes.

    Values:
    :   - **builtin** – a predefined type such as ‘int’ or ‘bool’.
        - **enum** – an enumeration type
        - **array** – an array type
        - **object** – an object type (struct or union)
        - **alternate** – an alternate type
        - **command** – a QMP command
        - **event** – a QMP event

*Object* SchemaInfo (Since: 2.5)
:   Members:
    :   - **name** (`string`) – the entity’s name, inherited from `base`. The [`SchemaInfo`](qemu-qmp-ref.md#object-QMP-introspect.SchemaInfo "QMP:introspect.SchemaInfo") is
          always referenced by this name. Commands and events have the
          name defined in the QAPI schema. Unlike command and event
          names, type names are not part of the wire ABI. Consequently,
          type names are meaningless strings here, although they are still
          guaranteed unique regardless of `meta-type`.
        - **meta-type** ([`SchemaMetaType`](qemu-qmp-ref.md#enum-QMP-introspect.SchemaMetaType "QMP:introspect.SchemaMetaType")) – the entity’s meta type, inherited from `base`.
        - **features** (`[``string``]`, *optional*) – names of features associated with the entity, in no
          particular order. (since 4.1 for object types, 4.2 for
          commands, 5.0 for the rest)
        - When `meta-type` is `builtin`: The members of [`SchemaInfoBuiltin`](qemu-qmp-ref.md#object-QMP-introspect.SchemaInfoBuiltin "QMP:introspect.SchemaInfoBuiltin").
        - When `meta-type` is `enum`: The members of [`SchemaInfoEnum`](qemu-qmp-ref.md#object-QMP-introspect.SchemaInfoEnum "QMP:introspect.SchemaInfoEnum").
        - When `meta-type` is `array`: The members of [`SchemaInfoArray`](qemu-qmp-ref.md#object-QMP-introspect.SchemaInfoArray "QMP:introspect.SchemaInfoArray").
        - When `meta-type` is `object`: The members of [`SchemaInfoObject`](qemu-qmp-ref.md#object-QMP-introspect.SchemaInfoObject "QMP:introspect.SchemaInfoObject").
        - When `meta-type` is `alternate`: The members of [`SchemaInfoAlternate`](qemu-qmp-ref.md#object-QMP-introspect.SchemaInfoAlternate "QMP:introspect.SchemaInfoAlternate").
        - When `meta-type` is `command`: The members of [`SchemaInfoCommand`](qemu-qmp-ref.md#object-QMP-introspect.SchemaInfoCommand "QMP:introspect.SchemaInfoCommand").
        - When `meta-type` is `event`: The members of [`SchemaInfoEvent`](qemu-qmp-ref.md#object-QMP-introspect.SchemaInfoEvent "QMP:introspect.SchemaInfoEvent").

*Object* SchemaInfoBuiltin (Since: 2.5)
:   Additional [`SchemaInfo`](qemu-qmp-ref.md#object-QMP-introspect.SchemaInfo "QMP:introspect.SchemaInfo") members for meta-type ‘builtin’.

    Members:
    :   - **json-type** ([`JSONType`](qemu-qmp-ref.md#enum-QMP-introspect.JSONType "QMP:introspect.JSONType")) – the JSON type used for this type on the wire.

*Enum* JSONType (Since: 2.5)
:   The four primitive and two structured types according to RFC 8259
    section 1, plus ‘int’ (split off ‘number’), plus the obvious top
    type ‘value’.

    Values:
    :   - **string** – JSON string
        - **number** – JSON number
        - **int** – JSON number that is an integer
        - **boolean** – literal `false` or `true`
        - **null** – literal `null`
        - **object** – JSON object
        - **array** – JSON array
        - **value** – any JSON value

*Object* SchemaInfoEnum (Since: 2.5)
:   Additional [`SchemaInfo`](qemu-qmp-ref.md#object-QMP-introspect.SchemaInfo "QMP:introspect.SchemaInfo") members for meta-type ‘enum’.

    Members:
    :   - **members** (`[`[`SchemaInfoEnumMember`](qemu-qmp-ref.md#object-QMP-introspect.SchemaInfoEnumMember "QMP:introspect.SchemaInfoEnumMember")`]`) – the enum type’s members, in no particular order.
          (since 6.2)
        - **values** (`[``string``]`) – the enumeration type’s member names, in no particular
          order. Redundant with `members`. Just for backward
          compatibility.

    Features:
    :   - **deprecated** – Member `values` is deprecated. Use `members` instead.

    Values of this type are JSON string on the wire.

*Object* SchemaInfoEnumMember (Since: 6.2)
:   An object member.

    Members:
    :   - **name** (`string`) – the member’s name, as defined in the QAPI schema.
        - **features** (`[``string``]`, *optional*) – names of features associated with the member, in no
          particular order.

*Object* SchemaInfoArray (Since: 2.5)
:   Additional [`SchemaInfo`](qemu-qmp-ref.md#object-QMP-introspect.SchemaInfo "QMP:introspect.SchemaInfo") members for meta-type ‘array’.

    Members:
    :   - **element-type** (`string`) – the array type’s element type.

    Values of this type are JSON array on the wire.

*Object* SchemaInfoObject (Since: 2.5)
:   Additional [`SchemaInfo`](qemu-qmp-ref.md#object-QMP-introspect.SchemaInfo "QMP:introspect.SchemaInfo") members for meta-type ‘object’.

    Members:
    :   - **members** (`[`[`SchemaInfoObjectMember`](qemu-qmp-ref.md#object-QMP-introspect.SchemaInfoObjectMember "QMP:introspect.SchemaInfoObjectMember")`]`) – the object type’s (non-variant) members, in no particular
          order.
        - **tag** (`string`, *optional*) – the name of the member serving as type tag. An element of
          `members` with this name must exist.
        - **variants** (`[`[`SchemaInfoObjectVariant`](qemu-qmp-ref.md#object-QMP-introspect.SchemaInfoObjectVariant "QMP:introspect.SchemaInfoObjectVariant")`]`, *optional*) – variant members, i.e. additional members that depend on
          the type tag’s value. Present exactly when `tag` is present.
          The variants are in no particular order, and may even differ
          from the order of the values of the enum type of the `tag`.

    Values of this type are JSON object on the wire.

*Object* SchemaInfoObjectMember (Since: 2.5)
:   An object member.

    Members:
    :   - **name** (`string`) – the member’s name, as defined in the QAPI schema.
        - **type** (`string`) – the name of the member’s type.
        - **default** (`value`, *optional*) – default when used as command parameter. If absent, the
          parameter is mandatory. If present, the value must be null.
          The parameter is optional, and behavior when it’s missing is not
          specified here. Future extension: if present and non-null, the
          parameter is optional, and defaults to this value.
        - **features** (`[``string``]`, *optional*) – names of features associated with the member, in no
          particular order. (since 5.0)

*Object* SchemaInfoObjectVariant (Since: 2.5)
:   The variant members for a value of the type tag.

    Members:
    :   - **case** (`string`) – a value of the type tag.
        - **type** (`string`) – the name of the object type that provides the variant members
          when the type tag has value `case`.

*Object* SchemaInfoAlternate (Since: 2.5)
:   Additional [`SchemaInfo`](qemu-qmp-ref.md#object-QMP-introspect.SchemaInfo "QMP:introspect.SchemaInfo") members for meta-type ‘alternate’.

    Members:
    :   - **members** (`[`[`SchemaInfoAlternateMember`](qemu-qmp-ref.md#object-QMP-introspect.SchemaInfoAlternateMember "QMP:introspect.SchemaInfoAlternateMember")`]`) – the alternate type’s members, in no particular order. The
          members’ wire encoding is distinct, see
          [How to use the QAPI code generator](../devel/qapi-code-gen.md) section Alternate types.

    On the wire, this can be any of the members.

*Object* SchemaInfoAlternateMember (Since: 2.5)
:   An alternate member.

    Members:
    :   - **type** (`string`) – the name of the member’s type.

*Object* SchemaInfoCommand (Since: 2.5)
:   Additional [`SchemaInfo`](qemu-qmp-ref.md#object-QMP-introspect.SchemaInfo "QMP:introspect.SchemaInfo") members for meta-type ‘command’.

    Members:
    :   - **arg-type** (`string`) – the name of the object type that provides the command’s
          parameters.
        - **ret-type** (`string`) – the name of the command’s result type.
        - **allow-oob** (`boolean`, *optional*) – whether the command allows out-of-band execution,
          defaults to false (Since: 2.12)

*Object* SchemaInfoEvent (Since: 2.5)
:   Additional [`SchemaInfo`](qemu-qmp-ref.md#object-QMP-introspect.SchemaInfo "QMP:introspect.SchemaInfo") members for meta-type ‘event’.

    Members:
    :   - **arg-type** (`string`) – the name of the object type that provides the event’s
          parameters.

## [QEMU Object Model (QOM)](qemu-qmp-ref.md#id31)

*Object* ObjectPropertyInfo (Since: 1.2)
:   Members:
    :   - **name** (`string`) – the name of the property
        - **type** (`string`) –

          the type of the property. This will typically come in one of
          four forms:

          1. A primitive type such as ‘u8’, ‘u16’, ‘bool’, ‘str’, or
             ‘double’. These types are mapped to the appropriate JSON
             type.
          2. A child type in the form ‘child<subtype>’ where subtype is a
             qdev device type name. Child properties create the
             composition tree.
          3. A link type in the form ‘link<subtype>’ where subtype is a
             qdev device type name. Link properties form the device model
             graph.
        - **description** (`string`, *optional*) – if specified, the description of the property.
        - **default-value** (`value`, *optional*) – the default value, if any (since 5.0)

*Object* ObjectPropertyValue (Since: 10.1)
:   Members:
    :   - **name** (`string`) – the name of the property.
        - **type** (`string`) – the type of the property, as described in
          [`ObjectPropertyInfo`](qemu-qmp-ref.md#object-QMP-qom.ObjectPropertyInfo "QMP:qom.ObjectPropertyInfo").
        - **value** (`value`, *optional*) – the value of the property. Absent when the property cannot
          be read.

*Object* ObjectPropertiesValues (Since: 10.1)
:   Members:
    :   - **properties** (`[`[`ObjectPropertyValue`](qemu-qmp-ref.md#object-QMP-qom.ObjectPropertyValue "QMP:qom.ObjectPropertyValue")`]`) – a list of properties.

*Command* qom-list (Since: 1.2)
:   List properties of a object given a path in the object model.

    Arguments:
    :   - **path** (`string`) – the path within the object model. See [`qom-get`](qemu-qmp-ref.md#command-QMP-qom.qom-get "QMP:qom.qom-get") for a
          description of this parameter.

    Return:
    :   `[`[`ObjectPropertyInfo`](qemu-qmp-ref.md#object-QMP-qom.ObjectPropertyInfo "QMP:qom.ObjectPropertyInfo")`]` – a list that describe the properties of the object.

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "qom-list",
    >      "arguments": { "path": "/chardevs" } }
    > <- { "return": [ { "name": "type", "type": "string" },
    >                  { "name": "parallel0", "type": "child<chardev-vc>" },
    >                  { "name": "serial0", "type": "child<chardev-vc>" },
    >                  { "name": "mon0", "type": "child<chardev-stdio>" } ] }
    > ```

*Command* qom-get (Since: 1.2)
:   Get a property value.

    Arguments:
    :   - **path** (`string`) –

          The path within the object model. There are two forms of
          supported paths–absolute and partial paths.

          Absolute paths are derived from the root object and can follow
          child<> or link<> properties. Since they can follow link<>
          properties, they can be arbitrarily long. Absolute paths look
          like absolute filenames and are prefixed with a leading slash.

          Partial paths look like relative filenames. They do not begin
          with a prefix. The matching rules for partial paths are subtle
          but designed to make specifying objects easy. At each level of
          the composition tree, the partial path is matched as an absolute
          path. The first match is not returned. At least two matches
          are searched for. A successful result is only returned if only
          one match is found. If more than one match is found, a flag is
          return to indicate that the match was ambiguous.
        - **property** (`string`) – The property name to read

    Return:
    :   `value` – The property value. The type depends on the property type.
        child<> and link<> properties are returned as #str pathnames.
        All integer property types (u8, u16, etc) are returned as #int.

    > **Example: Use absolute path:**
    >
    > ```QMP
    >  -> { "execute": "qom-get",
    >       "arguments": { "path": "/machine/unattached/device[0]",
    >                      "property": "hotplugged" } }
    >  <- { "return": false }
    > ```

    > **Example: Use partial path:**
    >
    > ```QMP
    >  -> { "execute": "qom-get",
    >       "arguments": { "path": "unattached/sysbus",
    >                      "property": "type" } }
    >  <- { "return": "System" }
    > ```

*Command* qom-list-get (Since: 10.1)
:   List properties and their values for each object path in the input
    list.

    Arguments:
    :   - **paths** (`[``string``]`) – The absolute or partial path for each object, as described
          in [`qom-get`](qemu-qmp-ref.md#command-QMP-qom.qom-get "QMP:qom.qom-get").

    Errors:
    :   - If any path is not valid or is ambiguous

    Return:
    :   `[`[`ObjectPropertiesValues`](qemu-qmp-ref.md#object-QMP-qom.ObjectPropertiesValues "QMP:qom.ObjectPropertiesValues")`]` – A list where each element is the result for the
        corresponding element of `paths`.

*Command* qom-set (Since: 1.2)
:   Set a property value.

    Arguments:
    :   - **path** (`string`) – see [`qom-get`](qemu-qmp-ref.md#command-QMP-qom.qom-get "QMP:qom.qom-get") for a description of this parameter
        - **property** (`string`) – the property name to set
        - **value** (`value`) – a value who’s type is appropriate for the property type.
          See [`qom-get`](qemu-qmp-ref.md#command-QMP-qom.qom-get "QMP:qom.qom-get") for a description of type mapping.

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "qom-set",
    >      "arguments": { "path": "/machine",
    >                     "property": "graphics",
    >                     "value": false } }
    > <- { "return": {} }
    > ```

*Object* ObjectTypeInfo (Since: 1.1)
:   This structure describes a search result from [`qom-list-types`](qemu-qmp-ref.md#command-QMP-qom.qom-list-types "QMP:qom.qom-list-types")

    Members:
    :   - **name** (`string`) – the type name found in the search
        - **abstract** (`boolean`, *optional*) – the type is abstract and can’t be directly instantiated.
          Omitted if false. (since 2.10)
        - **parent** (`string`, *optional*) – Name of parent type, if any (since 2.10)

*Command* qom-list-types (Since: 1.1)
:   Return a list of types given search parameters.

    Arguments:
    :   - **implements** (`string`, *optional*) – if specified, only return types that implement this
          type name
        - **abstract** (`boolean`, *optional*) – if true, include abstract types in the results

    Return:
    :   `[`[`ObjectTypeInfo`](qemu-qmp-ref.md#object-QMP-qom.ObjectTypeInfo "QMP:qom.ObjectTypeInfo")`]` – a list of types, or an empty list if no results are found

*Command* qom-list-properties (Since: 2.12)
:   List properties associated with a QOM object.

    Arguments:
    :   - **typename** (`string`) – the type name of an object

    > **Note:**
    >
    > Objects can create properties at runtime, for example to
    > describe links between different devices and/or objects. These
    > properties are not included in the output of this command.

    Return:
    :   `[`[`ObjectPropertyInfo`](qemu-qmp-ref.md#object-QMP-qom.ObjectPropertyInfo "QMP:qom.ObjectPropertyInfo")`]` – a list describing object properties

*Object* CanHostSocketcanProperties (Since: 2.12)
:   *Availability*: `CONFIG_LINUX`

    Properties for can-host-socketcan objects.

    Members:
    :   - **if** (`string`) – interface name of the host system CAN bus to connect to
        - **canbus** (`string`) – object ID of the can-bus object to connect to the host
          interface

*Object* ColoCompareProperties (Since: 2.8)
:   Properties for colo-compare objects.

    Members:
    :   - **primary_in** (`string`) – name of the character device backend to use for the
          primary input (incoming packets are redirected to `outdev`)
        - **secondary_in** (`string`) – name of the character device backend to use for
          secondary input (incoming packets are only compared to the input
          on `primary_in` and then dropped)
        - **outdev** (`string`) – name of the character device backend to use for output
        - **iothread** (`string`) – name of the iothread to run in
        - **notify_dev** (`string`, *optional*) – name of the character device backend to be used to
          communicate with the remote colo-frame (only for Xen COLO)
        - **compare_timeout** (`int`, *optional*) – the maximum time to hold a packet from `primary_in`
          for comparison with an incoming packet on `secondary_in` in
          milliseconds (default: 3000)
        - **expired_scan_cycle** (`int`, *optional*) – the interval at which colo-compare checks
          whether packets from `primary` have timed out, in milliseconds
          (default: 3000)
        - **max_queue_size** (`int`, *optional*) – the maximum number of packets to keep in the queue
          for comparing with incoming packets from `secondary_in`. If the
          queue is full and additional packets are received, the
          additional packets are dropped. (default: 1024)
        - **vnet_hdr_support** (`boolean`, *optional*) – if true, vnet header support is enabled
          (default: false)

*Object* CryptodevBackendProperties (Since: 2.8)
:   Properties for cryptodev-backend and cryptodev-backend-builtin
    objects.

    Members:
    :   - **queues** (`int`, *optional*) – the number of queues for the cryptodev backend. Ignored
          for cryptodev-backend and must be 1 for
          cryptodev-backend-builtin. (default: 1)
        - **throttle-bps** (`int`, *optional*) – limit total bytes per second (Since 8.0)
        - **throttle-ops** (`int`, *optional*) – limit total operations per second (Since 8.0)

*Object* CryptodevVhostUserProperties (Since: 2.12)
:   *Availability*: `CONFIG_VHOST_CRYPTO`

    Properties for cryptodev-vhost-user objects.

    Members:
    :   - **chardev** (`string`) – the name of a Unix domain socket character device that
          connects to the vhost-user server
        - The members of [`CryptodevBackendProperties`](qemu-qmp-ref.md#object-QMP-qom.CryptodevBackendProperties "QMP:qom.CryptodevBackendProperties").

*Object* DBusVMStateProperties (Since: 5.0)
:   Properties for dbus-vmstate objects.

    Members:
    :   - **addr** (`string`) – the name of the DBus bus to connect to
        - **id-list** (`string`, *optional*) – a comma separated list of DBus IDs of helpers whose data
          should be included in the VM state on migration

*Enum* NetfilterInsert (Since: 5.0)
:   Indicates where to insert a netfilter relative to a given other
    filter.

    Values:
    :   - **before** – insert before the specified filter
        - **behind** – insert behind the specified filter

*Object* NetfilterProperties (Since: 2.5)
:   Properties for objects of classes derived from netfilter.

    Members:
    :   - **netdev** (`string`) – id of the network device backend to filter
        - **queue** ([`NetFilterDirection`](qemu-qmp-ref.md#enum-QMP-common.NetFilterDirection "QMP:common.NetFilterDirection"), *optional*) – indicates which queue(s) to filter (default: all)
        - **status** (`string`, *optional*) – indicates whether the filter is enabled (“on”) or disabled
          (“off”) (default: “on”)
        - **position** (`string`, *optional*) – specifies where the filter should be inserted in the
          filter list. “head” means the filter is inserted at the head of
          the filter list, before any existing filters. “tail” means the
          filter is inserted at the tail of the filter list, behind any
          existing filters (default). “id=<id>” means the filter is
          inserted before or behind the filter specified by <id>,
          depending on the `insert` property. (default: “tail”)
        - **insert** ([`NetfilterInsert`](qemu-qmp-ref.md#enum-QMP-qom.NetfilterInsert "QMP:qom.NetfilterInsert"), *optional*) – where to insert the filter relative to the filter given in
          `position`. Ignored if `position` is “head” or “tail”.
          (default: behind)

*Object* FilterBufferProperties (Since: 2.5)
:   Properties for filter-buffer objects.

    Members:
    :   - **interval** (`int`) – a non-zero interval in microseconds. All packets
          arriving in the given interval are delayed until the end of the
          interval.
        - The members of [`NetfilterProperties`](qemu-qmp-ref.md#object-QMP-qom.NetfilterProperties "QMP:qom.NetfilterProperties").

*Object* FilterDumpProperties (Since: 2.5)
:   Properties for filter-dump objects.

    Members:
    :   - **file** (`string`) – the filename where the dumped packets should be stored
        - **maxlen** (`int`, *optional*) – maximum number of bytes in a packet that are stored
          (default: 65536)
        - The members of [`NetfilterProperties`](qemu-qmp-ref.md#object-QMP-qom.NetfilterProperties "QMP:qom.NetfilterProperties").

*Object* FilterMirrorProperties (Since: 2.6)
:   Properties for filter-mirror objects.

    Members:
    :   - **outdev** (`string`) – the name of a character device backend to which all
          incoming packets are mirrored
        - **vnet_hdr_support** (`boolean`, *optional*) – if true, vnet header support is enabled
          (default: false)
        - The members of [`NetfilterProperties`](qemu-qmp-ref.md#object-QMP-qom.NetfilterProperties "QMP:qom.NetfilterProperties").

*Object* FilterRedirectorProperties (Since: 2.6)
:   Properties for filter-redirector objects.

    At least one of `indev` or `outdev` must be present. If both are
    present, they must not refer to the same character device backend.

    Members:
    :   - **indev** (`string`, *optional*) – the name of a character device backend from which packets
          are received and redirected to the filtered network device
        - **outdev** (`string`, *optional*) – the name of a character device backend to which all
          incoming packets are redirected
        - **vnet_hdr_support** (`boolean`, *optional*) – if true, vnet header support is enabled
          (default: false)
        - The members of [`NetfilterProperties`](qemu-qmp-ref.md#object-QMP-qom.NetfilterProperties "QMP:qom.NetfilterProperties").

*Object* FilterRewriterProperties (Since: 2.8)
:   Properties for filter-rewriter objects.

    Members:
    :   - **vnet_hdr_support** (`boolean`, *optional*) – if true, vnet header support is enabled
          (default: false)
        - The members of [`NetfilterProperties`](qemu-qmp-ref.md#object-QMP-qom.NetfilterProperties "QMP:qom.NetfilterProperties").

*Object* InputBarrierProperties (Since: 4.2)
:   Properties for input-barrier objects.

    Members:
    :   - **name** (`string`) – the screen name as declared in the screens section of
          barrier.conf
        - **server** (`string`, *optional*) – hostname of the Barrier server (default: “localhost”)
        - **port** (`string`, *optional*) – TCP port of the Barrier server (default: “24800”)
        - **x-origin** (`string`, *optional*) – x coordinate of the leftmost pixel on the guest screen
          (default: “0”)
        - **y-origin** (`string`, *optional*) – y coordinate of the topmost pixel on the guest screen
          (default: “0”)
        - **width** (`string`, *optional*) – the width of secondary screen in pixels (default: “1920”)
        - **height** (`string`, *optional*) – the height of secondary screen in pixels (default: “1080”)

*Object* InputLinuxProperties (Since: 2.6)
:   *Availability*: `CONFIG_LINUX`

    Properties for input-linux objects.

    Members:
    :   - **evdev** (`string`) – the path of the host evdev device to use
        - **grab_all** (`boolean`, *optional*) – if true, grab is toggled for all devices (e.g. both
          keyboard and mouse) instead of just one device (default: false)
        - **repeat** (`boolean`, *optional*) – enables auto-repeat events (default: false)
        - **grab-toggle** ([`GrabToggleKeys`](qemu-qmp-ref.md#enum-QMP-common.GrabToggleKeys "QMP:common.GrabToggleKeys"), *optional*) – the key or key combination that toggles device grab
          (default: ctrl-ctrl)

*Object* EventLoopBaseProperties (Since: 7.1)
:   Common properties for event loops

    Members:
    :   - **aio-max-batch** (`int`, *optional*) – maximum number of requests in a batch for the AIO
          engine, 0 means that the engine will use its default.
          (default: 0)
        - **thread-pool-min** (`int`, *optional*) – minimum number of threads reserved in the thread
          pool (default:0)
        - **thread-pool-max** (`int`, *optional*) – maximum number of threads the thread pool can
          contain (default:64)

*Object* IothreadProperties (Since: 2.0)
:   Properties for iothread objects.

    Members:
    :   - **poll-max-ns** (`int`, *optional*) – the maximum number of nanoseconds to busy wait for
          events. 0 means polling is disabled (default: 32768 on POSIX
          hosts, 0 otherwise)
        - **poll-grow** (`int`, *optional*) – the multiplier used to increase the polling time when
          the algorithm detects it is missing events due to not polling
          long enough. 0 selects a default behaviour (default: 0)
        - **poll-shrink** (`int`, *optional*) – the divisor used to decrease the polling time when the
          algorithm detects it is spending too long polling without
          encountering events. 0 selects a default behaviour (default: 0)
        - **poll-weight** (`int`, *optional*) – the weight factor for adaptive polling. Determines
          how much the most recent event interval affects the next
          polling duration calculation. If set to 0, the system default
          value of 3 is used. Typical values: 1 (high weight on recent
          interval), 2-4 (moderate weight on recent interval).
          (default: 0) (since 11.1)
        - The members of [`EventLoopBaseProperties`](qemu-qmp-ref.md#object-QMP-qom.EventLoopBaseProperties "QMP:qom.EventLoopBaseProperties").

    The `aio-max-batch` option is available since 6.1.

*Object* MainLoopProperties (Since: 7.1)
:   Properties for the main-loop object.

    Members:
    :   - The members of [`EventLoopBaseProperties`](qemu-qmp-ref.md#object-QMP-qom.EventLoopBaseProperties "QMP:qom.EventLoopBaseProperties").

*Object* MemoryBackendProperties (Since: 2.1)
:   Properties for objects of classes derived from memory-backend.

    Members:
    :   - **merge** (`boolean`, *optional*) – if true, mark the memory as mergeable (default depends on
          the machine type)
        - **dump** (`boolean`, *optional*) – if true, include the memory in core dumps (default depends on
          the machine type)
        - **host-nodes** (`[``int``]`, *optional*) – the list of NUMA host nodes to bind the memory to
        - **policy** ([`HostMemPolicy`](qemu-qmp-ref.md#enum-QMP-common.HostMemPolicy "QMP:common.HostMemPolicy"), *optional*) – the NUMA policy (default: ‘default’)
        - **prealloc** (`boolean`, *optional*) – if true, preallocate memory (default: false)
        - **prealloc-threads** (`int`, *optional*) – number of CPU threads to use for prealloc
          (default: 1)
        - **prealloc-context** (`string`, *optional*) – thread context to use for creation of
          preallocation threads (default: none) (since 7.2)
        - **share** (`boolean`, *optional*) – if false, the memory is private to QEMU; if true, it is
          shared (default false for backends memory-backend-file and
          memory-backend-ram, true for backends memory-backend-epc,
          memory-backend-memfd, and memory-backend-shm)
        - **reserve** (`boolean`, *optional*) – if true, reserve swap space (or huge pages) if applicable
          (default: true) (since 6.1)
        - **size** (`int`) – size of the memory region in bytes
        - **x-use-canonical-path-for-ramblock-id** (`boolean`, *optional*) – if true, the canonical path
          is used for ramblock-id. Disable this for 4.0 machine types or
          older to allow migration with newer QEMU versions.
          (default: false generally, but true for machine types <= 4.0)

    > **Note:**
    >
    > prealloc=true and reserve=false cannot be set at the same
    > time. With reserve=true, the behavior depends on the operating
    > system: for example, Linux will not reserve swap space for shared
    > file mappings – “not applicable”. In contrast, reserve=false
    > will bail out if it cannot be configured accordingly.

*Object* MemoryBackendFileProperties (Since: 2.1)
:   Properties for memory-backend-file objects.

    Members:
    :   - **align** (`int`, *optional*) – the base address alignment when QEMU mmap(2)s `mem-path`.
          Some backend stores specified by `mem-path` require an alignment
          different than the default one used by QEMU, e.g. the device DAX
          /dev/dax0.0 requires 2M alignment rather than 4K. In such
          cases, users can specify the required alignment via this option.
          0 selects a default alignment (currently the page size).
          (default: 0)
        - **offset** (`int`, *optional*) – the offset into the target file that the region starts at.
          You can use this option to back multiple regions with a single
          file. Must be a multiple of the page size.
          (default: 0) (since 8.1)
        - **discard-data** (`boolean`, *optional*) – if true, the file contents can be destroyed when QEMU
          exits, to avoid unnecessarily flushing data to the backing file.
          Note that `discard-data` is only an optimization, and QEMU might
          not discard file contents if it aborts unexpectedly or is
          terminated using SIGKILL. (default: false)
        - **mem-path** (`string`) – the path to either a shared memory or huge page
          filesystem mount
        - **pmem** (`boolean`, *optional*) – specifies whether the backing file specified by `mem-path` is
          in host persistent memory that can be accessed using the SNIA
          NVM programming model (e.g. Intel NVDIMM).
        - **readonly** (`boolean`, *optional*) – if true, the backing file is opened read-only; if false,
          it is opened read-write. (default: false)
        - **rom** ([`OnOffAuto`](qemu-qmp-ref.md#enum-QMP-common.OnOffAuto "QMP:common.OnOffAuto"), *optional*) – whether to create Read Only Memory (ROM) that cannot be
          modified by the VM. Any write attempts to such ROM will be
          denied. Most use cases want writable RAM instead of ROM.
          However, selected use cases, like R/O NVDIMMs, can benefit from
          ROM. If set to ‘on’, create ROM; if set to ‘off’, create
          writable RAM; if set to ‘auto’, the value of the `readonly`
          property is used. This property is primarily helpful when we
          want to have proper RAM in configurations that would
          traditionally create ROM before this property was introduced: VM
          templating, where we want to open a file readonly (`readonly` set
          to true) and mark the memory to be private for QEMU (`share` set
          to false). For this use case, we need writable RAM instead of
          ROM, and want to set this property to ‘off’. (default: auto,
          since 8.2)
        - The members of [`MemoryBackendProperties`](qemu-qmp-ref.md#object-QMP-qom.MemoryBackendProperties "QMP:qom.MemoryBackendProperties").

*Object* MemoryBackendMemfdProperties (Since: 2.12)
:   *Availability*: `CONFIG_LINUX`

    Properties for memory-backend-memfd objects.

    Members:
    :   - **hugetlb** (`boolean`, *optional*) – if true, the file to be created resides in the hugetlbfs
          filesystem (default: false)
        - **hugetlbsize** (`int`, *optional*) – the hugetlb page size on systems that support multiple
          hugetlb page sizes (it must be a power of 2 value supported by
          the system). 0 selects a default page size. This option is
          ignored if `hugetlb` is false. (default: 0)
        - **seal** (`boolean`, *optional*) – if true, create a sealed-file, which will block further
          resizing of the memory (default: true)
        - The members of [`MemoryBackendProperties`](qemu-qmp-ref.md#object-QMP-qom.MemoryBackendProperties "QMP:qom.MemoryBackendProperties").

*Object* MemoryBackendShmProperties (Since: 9.1)
:   *Availability*: `CONFIG_POSIX`

    Properties for memory-backend-shm objects.

    This memory backend supports only shared memory, which is the
    default.

    Members:
    :   - The members of [`MemoryBackendProperties`](qemu-qmp-ref.md#object-QMP-qom.MemoryBackendProperties "QMP:qom.MemoryBackendProperties").

*Object* MemoryBackendEpcProperties (Since: 6.2)
:   *Availability*: `CONFIG_LINUX`

    Properties for memory-backend-epc objects.

    The `merge` boolean option is false by default with epc

    The `dump` boolean option is false by default with epc

    Members:
    :   - The members of [`MemoryBackendProperties`](qemu-qmp-ref.md#object-QMP-qom.MemoryBackendProperties "QMP:qom.MemoryBackendProperties").

*Object* PrManagerHelperProperties (Since: 2.11)
:   *Availability*: `CONFIG_LINUX`

    Properties for pr-manager-helper objects.

    Members:
    :   - **path** (`string`) – the path to a Unix domain socket for connecting to the
          external helper

*Object* QtestProperties (Since: 6.0)
:   Properties for qtest objects.

    Members:
    :   - **chardev** (`string`) – the chardev to be used to receive qtest commands on.
        - **log** (`string`, *optional*) – the path to a log file

*Object* RemoteObjectProperties (Since: 6.0)
:   Properties for x-remote-object objects.

    Members:
    :   - **fd** (`string`) – file descriptor name previously passed via [`getfd`](qemu-qmp-ref.md#command-QMP-misc.getfd "QMP:misc.getfd") command
        - **devid** (`string`) – the id of the device to be associated with the file
          descriptor

*Object* VfioUserServerProperties (Since: 7.1)
:   Properties for x-vfio-user-server objects.

    Members:
    :   - **socket** ([`SocketAddress`](qemu-qmp-ref.md#object-QMP-sockets.SocketAddress "QMP:sockets.SocketAddress")) – socket to be used by the libvfio-user library
        - **device** (`string`) – the ID of the device to be emulated at the server

*Object* IOMMUFDProperties (Since: 9.0)
:   Properties for iommufd objects.

    Members:
    :   - **fd** (`string`, *optional*) – file descriptor name previously passed via [`getfd`](qemu-qmp-ref.md#command-QMP-misc.getfd "QMP:misc.getfd") command,
          which represents a pre-opened /dev/iommu. This allows the
          iommufd object to be shared across several subsystems (VFIO,
          VDPA, …), and the file descriptor to be shared with other
          process, e.g. DPDK. (default: QEMU opens /dev/iommu by itself)

*Object* AcpiGenericInitiatorProperties (Since: 9.0)
:   Properties for acpi-generic-initiator objects.

    Members:
    :   - **pci-dev** (`string`) – PCI device ID to be associated with the node
        - **node** (`int`) – NUMA node associated with the PCI device

*Object* AcpiGenericPortProperties (Since: 9.2)
:   Properties for acpi-generic-port objects.

    Members:
    :   - **pci-bus** (`string`) – QOM path of the PCI bus of the hostbridge associated with
          this SRAT Generic Port Affinity Structure. This is the same as
          the bus parameter for the root ports attached to this host
          bridge. The resulting SRAT Generic Port Affinity Structure will
          refer to the ACPI object in DSDT that represents the host bridge
          (e.g. ACPI0016 for CXL host bridges). See ACPI 6.5 Section
          5.2.16.7 for more information.
        - **node** (`int`) – Similar to a NUMA node ID, but instead of providing a
          reference point used for defining NUMA distances and access
          characteristics to memory or from an initiator (e.g. CPU), this
          node defines the boundary point between non-discoverable system
          buses which must be described by firmware, and a discoverable
          bus. NUMA distances and access characteristics are defined to
          and from that point. For system software to establish full
          initiator to target characteristics this information must be
          combined with information retrieved from the discoverable part
          of the path. An example would use CDAT (see UEFI.org)
          information read from devices and switches in conjunction with
          link characteristics read from PCIe Configuration space. To get
          the full path latency from CPU to CXL attached DRAM CXL device:
          Add the latency from CPU to Generic Port (from HMAT indexed via
          the node ID in this SRAT structure) to that for CXL bus links,
          the latency across intermediate switches and from the EP port to
          the actual memory. Bandwidth is more complex as there may be
          interleaving across multiple devices and shared links in the
          path.

*Object* RngProperties (Since: 1.3)
:   Properties for objects of classes derived from rng.

    Members:
    :   - **opened** (`boolean`, *optional*) – if true, the device is opened immediately when applying
          this option and will probably fail when processing the next
          option. Don’t use; only provided for compatibility.
          (default: false)

    Features:
    :   - **deprecated** – Member `opened` is deprecated. Setting true doesn’t
          make sense, and false is already the default.

*Object* RngEgdProperties (Since: 1.3)
:   Properties for rng-egd objects.

    Members:
    :   - **chardev** (`string`) – the name of a character device backend that provides the
          connection to the RNG daemon
        - The members of [`RngProperties`](qemu-qmp-ref.md#object-QMP-qom.RngProperties "QMP:qom.RngProperties").

*Object* RngRandomProperties (Since: 1.3)
:   *Availability*: `CONFIG_POSIX`

    Properties for rng-random objects.

    Members:
    :   - **filename** (`string`, *optional*) – the filename of the device on the host to obtain entropy
          from (default: “/dev/urandom”)
        - The members of [`RngProperties`](qemu-qmp-ref.md#object-QMP-qom.RngProperties "QMP:qom.RngProperties").

*Object* IgvmCfgProperties (Since: 10.1)
:   *Availability*: `CONFIG_IGVM`

    Properties common to objects that handle IGVM files.

    Members:
    :   - **file** (`string`) – IGVM file to use to configure guest

*Object* SevCommonProperties (Since: 9.1)
:   Properties common to objects that are derivatives of sev-common.

    Members:
    :   - **sev-device** (`string`, *optional*) – SEV device to use (default: “/dev/sev”)
        - **cbitpos** (`int`, *optional*) – C-bit location in page table entry (default: 0)
        - **reduced-phys-bits** (`int`) – number of bits in physical addresses that become
          unavailable when SEV is enabled
        - **kernel-hashes** (`boolean`, *optional*) – if true, add hashes of kernel/initrd/cmdline to a
          designated guest firmware page for measured boot with -kernel
          (default: false) (since 6.2)
        - **debug-swap** (`boolean`, *optional*) – enable virtualization of debug registers,
          only supported on SEV-ES and SEV-SNP guests
          (default: false) (since 11.1)

    Features:
    :   - **confidential-guest-reset** – If present, the hypervisor supports
          confidential guest resets (since 11.0).

*Object* SevGuestProperties (Since: 2.12)
:   Properties for sev-guest objects.

    Members:
    :   - **dh-cert-file** (`string`, *optional*) – guest owners DH certificate (encoded with base64)
        - **session-file** (`string`, *optional*) – guest owners session parameters (encoded with base64)
        - **policy** (`int`, *optional*) – SEV policy value (default: 0x1)
        - **handle** (`int`, *optional*) – SEV firmware handle (default: 0)
        - **legacy-vm-type** ([`OnOffAuto`](qemu-qmp-ref.md#enum-QMP-common.OnOffAuto "QMP:common.OnOffAuto"), *optional*) – Use legacy KVM_SEV_INIT KVM interface for creating
          the VM. The newer KVM_SEV_INIT2 interface, from Linux >= 6.10,
          syncs additional vCPU state when initializing the VMSA
          structures, which will result in a different guest measurement.
          Set this to ‘on’ to force compatibility with older QEMU or kernel
          versions that rely on legacy KVM_SEV_INIT behavior. ‘auto’ will
          behave identically to ‘on’, but will automatically switch to
          using KVM_SEV_INIT2 if the user specifies any additional options
          that require it. If set to ‘off’, QEMU will require
          KVM_SEV_INIT2 unconditionally. (default: off) (since 9.1)
        - The members of [`SevCommonProperties`](qemu-qmp-ref.md#object-QMP-qom.SevCommonProperties "QMP:qom.SevCommonProperties").

*Object* SevSnpGuestProperties (Since: 9.1)
:   Properties for sev-snp-guest objects. Most of these are direct
    arguments for the KVM_SNP_\* interfaces documented in the Linux
    kernel source under
    Documentation/arch/x86/amd-memory-encryption.rst, which are in turn
    closely coupled with the SNP_INIT/SNP_LAUNCH_\* firmware commands
    documented in the SEV-SNP Firmware ABI Specification (Rev 0.9).

    More usage information is also available in the QEMU source tree
    under docs/amd-memory-encryption.

    Members:
    :   - **policy** (`int`, *optional*) – the ‘POLICY’ parameter to the SNP_LAUNCH_START command, as
          defined in the SEV-SNP firmware ABI (default: 0x30000)
        - **guest-visible-workarounds** (`string`, *optional*) – 16-byte, base64-encoded blob to report
          hypervisor-defined workarounds, corresponding to the ‘GOSVW’
          parameter of the SNP_LAUNCH_START command defined in the SEV-SNP
          firmware ABI (default: all-zero)
        - **id-block** (`string`, *optional*) – 96-byte, base64-encoded blob to provide the ‘ID Block’
          structure for the SNP_LAUNCH_FINISH command defined in the
          SEV-SNP firmware ABI (default: all-zero)
        - **id-auth** (`string`, *optional*) – 4096-byte, base64-encoded blob to provide the ‘ID
          Authentication Information Structure’ for the SNP_LAUNCH_FINISH
          command defined in the SEV-SNP firmware ABI (default: all-zero)
        - **author-key-enabled** (`boolean`, *optional*) – true if ‘id-auth’ blob contains the
          ‘AUTHOR_KEY’ field defined SEV-SNP firmware ABI (default: false)
        - **host-data** (`string`, *optional*) – 32-byte, base64-encoded, user-defined blob to provide to
          the guest, as documented for the ‘HOST_DATA’ parameter of the
          SNP_LAUNCH_FINISH command in the SEV-SNP firmware ABI (default:
          all-zero)
        - **vcek-disabled** (`boolean`, *optional*) – Guests are by default allowed to choose between VLEK
          (Versioned Loaded Endorsement Key) or VCEK (Versioned Chip
          Endorsement Key) when requesting attestation reports from
          firmware. Set this to true to disable the use of VCEK.
          (default: false) (since: 9.1)
        - **secure-tsc** (`boolean`, *optional*) – enable Secure TSC
          (default: false) (since 11.1)
        - **tsc-frequency** (`int`, *optional*) – set secure TSC frequency. Only valid if Secure TSC
          is enabled (default: zero) (since 11.1)
        - The members of [`SevCommonProperties`](qemu-qmp-ref.md#object-QMP-qom.SevCommonProperties "QMP:qom.SevCommonProperties").

*Object* TdxGuestProperties (Since: 10.1)
:   Properties for tdx-guest objects.

    Members:
    :   - **attributes** (`int`, *optional*) – The ‘attributes’ of a TD guest that is passed to
          KVM_TDX_INIT_VM
        - **sept-ve-disable** (`boolean`, *optional*) – toggle bit 28 of TD attributes to control
          disabling of EPT violation conversion to #VE on guest TD access
          of PENDING pages. Some guest OS (e.g., Linux TD guest) may
          require this to be set, otherwise they refuse to boot.
        - **mrconfigid** (`string`, *optional*) – ID for non-owner-defined configuration of the guest TD,
          e.g., run-time or OS configuration (base64 encoded SHA384
          digest). Defaults to all zeros.
        - **mrowner** (`string`, *optional*) – ID for the guest TD’s owner (base64 encoded SHA384
          digest). Defaults to all zeros.
        - **mrownerconfig** (`string`, *optional*) – ID for owner-defined configuration of the guest TD,
          e.g., specific to the workload rather than the run-time or OS
          (base64 encoded SHA384 digest). Defaults to all zeros.
        - **quote-generation-socket** ([`SocketAddress`](qemu-qmp-ref.md#object-QMP-sockets.SocketAddress "QMP:sockets.SocketAddress"), *optional*) – socket address for Quote Generation
          Service (QGS). QGS is a daemon running on the host. Without
          it, the guest will not be able to get a TD quote for
          attestation.

    Features:
    :   - **confidential-guest-reset** – If present, the hypervisor supports
          confidential guest resets (since 11.0).

*Object* ThreadContextProperties (Since: 7.2)
:   Properties for thread context objects.

    Members:
    :   - **cpu-affinity** (`[``int``]`, *optional*) – the list of host CPU numbers used as CPU affinity for
          all threads created in the thread context (default: QEMU main
          thread CPU affinity)
        - **node-affinity** (`[``int``]`, *optional*) – the list of host node numbers that will be resolved
          to a list of host CPU numbers used as CPU affinity. This is a
          shortcut for specifying the list of host CPU numbers belonging
          to the host nodes manually by setting `cpu-affinity`.
          (default: QEMU main thread affinity)

*Object* MonitorProperties (Since: 11.1)
:   Properties for all monitors

    Members:
    :   - **chardev** (`string`) – ID of the character device providing the monitor transport

*Object* MonitorHMPProperties (Since: 11.1)
:   Properties for the HMP monitor

    Members:
    :   - **readline** (`boolean`, *optional*) – whether to enable readline for line editing
          (default: true)
        - The members of [`MonitorProperties`](qemu-qmp-ref.md#object-QMP-qom.MonitorProperties "QMP:qom.MonitorProperties").

*Enum* MonitorQMPCloseAction (Since: 11.1)
:   Action to take when the character device backend is closed.

    Values:
    :   - **none** – take no action
        - **delete** – delete both the ‘monitor-qmp’ object and its associated
          character device backend object

*Object* MonitorQMPProperties (Since: 11.1)
:   Properties for the QMP monitor

    Members:
    :   - **pretty** (`boolean`, *optional*) – whether to pretty print JSON responses (default: false)
        - **close-action** ([`MonitorQMPCloseAction`](qemu-qmp-ref.md#enum-QMP-qom.MonitorQMPCloseAction "QMP:qom.MonitorQMPCloseAction"), *optional*) – action to take when the character device backend is
          closed (default: none)
        - The members of [`MonitorProperties`](qemu-qmp-ref.md#object-QMP-qom.MonitorProperties "QMP:qom.MonitorProperties").

*Enum* ObjectType (Since: 6.0)
:   Values:
    :   - **acpi-generic-initiator** – Not documented
        - **acpi-generic-port** – Not documented
        - **authz-list** – Not documented
        - **authz-listfile** – Not documented
        - **authz-pam** – Not documented
        - **authz-simple** – Not documented
        - **can-bus** – Not documented
        - **can-host-socketcan** – Not documented
        - **colo-compare** – Not documented
        - **cryptodev-backend** – Not documented
        - **cryptodev-backend-builtin** – Not documented
        - **cryptodev-backend-lkcf** – Not documented
        - **cryptodev-vhost-user** – Not documented
        - **dbus-vmstate** – Not documented
        - **filter-buffer** – Not documented
        - **filter-dump** – Not documented
        - **filter-mirror** – Not documented
        - **filter-redirector** – Not documented
        - **filter-replay** – Not documented
        - **filter-rewriter** – Not documented
        - **igvm-cfg** – Not documented
        - **input-barrier** – Not documented
        - **input-linux** – Not documented
        - **iommufd** – Not documented
        - **iothread** – Not documented
        - **main-loop** – Not documented
        - **memory-backend-epc** – Not documented
        - **memory-backend-file** – Not documented
        - **memory-backend-memfd** – Not documented
        - **memory-backend-ram** – Not documented
        - **memory-backend-shm** – Not documented
        - **monitor-hmp** – Not documented
        - **monitor-qmp** – Not documented
        - **pef-guest** – Not documented
        - **pr-manager-helper** – Not documented
        - **qtest** – Not documented
        - **rng-builtin** – Not documented
        - **rng-egd** – Not documented
        - **rng-random** – Not documented
        - **secret** – Not documented
        - **secret_keyring** – Not documented
        - **sev-guest** – Not documented
        - **sev-snp-guest** – Not documented
        - **thread-context** – Not documented
        - **s390-pv-guest** – Not documented
        - **tdx-guest** – Not documented
        - **throttle-group** – Not documented
        - **tls-creds-anon** – Not documented
        - **tls-creds-psk** – Not documented
        - **tls-creds-x509** – Not documented
        - **tls-cipher-suites** – Not documented
        - **x-remote-object** – Not documented
        - **x-vfio-user-server** – Not documented

    Features:
    :   - **unstable** – Members `x-remote-object` and `x-vfio-user-server` are
          experimental.

*Object* ObjectOptions (Since: 6.0)
:   Describes the options of a user creatable QOM object.

    Members:
    :   - **qom-type** ([`ObjectType`](qemu-qmp-ref.md#enum-QMP-qom.ObjectType "QMP:qom.ObjectType")) – the class name for the object to be created
        - **id** (`string`) – the name of the new object
        - When `qom-type` is `acpi-generic-initiator`: The members of [`AcpiGenericInitiatorProperties`](qemu-qmp-ref.md#object-QMP-qom.AcpiGenericInitiatorProperties "QMP:qom.AcpiGenericInitiatorProperties").
        - When `qom-type` is `acpi-generic-port`: The members of [`AcpiGenericPortProperties`](qemu-qmp-ref.md#object-QMP-qom.AcpiGenericPortProperties "QMP:qom.AcpiGenericPortProperties").
        - When `qom-type` is `authz-list`: The members of [`AuthZListProperties`](qemu-qmp-ref.md#object-QMP-authz.AuthZListProperties "QMP:authz.AuthZListProperties").
        - When `qom-type` is `authz-listfile`: The members of [`AuthZListFileProperties`](qemu-qmp-ref.md#object-QMP-authz.AuthZListFileProperties "QMP:authz.AuthZListFileProperties").
        - When `qom-type` is `authz-pam`: The members of [`AuthZPAMProperties`](qemu-qmp-ref.md#object-QMP-authz.AuthZPAMProperties "QMP:authz.AuthZPAMProperties").
        - When `qom-type` is `authz-simple`: The members of [`AuthZSimpleProperties`](qemu-qmp-ref.md#object-QMP-authz.AuthZSimpleProperties "QMP:authz.AuthZSimpleProperties").
        - When `qom-type` is `can-host-socketcan`: The members of [`CanHostSocketcanProperties`](qemu-qmp-ref.md#object-QMP-qom.CanHostSocketcanProperties "QMP:qom.CanHostSocketcanProperties").
        - When `qom-type` is `colo-compare`: The members of [`ColoCompareProperties`](qemu-qmp-ref.md#object-QMP-qom.ColoCompareProperties "QMP:qom.ColoCompareProperties").
        - When `qom-type` is `cryptodev-backend`: The members of [`CryptodevBackendProperties`](qemu-qmp-ref.md#object-QMP-qom.CryptodevBackendProperties "QMP:qom.CryptodevBackendProperties").
        - When `qom-type` is `cryptodev-backend-builtin`: The members of [`CryptodevBackendProperties`](qemu-qmp-ref.md#object-QMP-qom.CryptodevBackendProperties "QMP:qom.CryptodevBackendProperties").
        - When `qom-type` is `cryptodev-backend-lkcf`: The members of [`CryptodevBackendProperties`](qemu-qmp-ref.md#object-QMP-qom.CryptodevBackendProperties "QMP:qom.CryptodevBackendProperties").
        - When `qom-type` is `cryptodev-vhost-user`: The members of [`CryptodevVhostUserProperties`](qemu-qmp-ref.md#object-QMP-qom.CryptodevVhostUserProperties "QMP:qom.CryptodevVhostUserProperties").
        - When `qom-type` is `dbus-vmstate`: The members of [`DBusVMStateProperties`](qemu-qmp-ref.md#object-QMP-qom.DBusVMStateProperties "QMP:qom.DBusVMStateProperties").
        - When `qom-type` is `filter-buffer`: The members of [`FilterBufferProperties`](qemu-qmp-ref.md#object-QMP-qom.FilterBufferProperties "QMP:qom.FilterBufferProperties").
        - When `qom-type` is `filter-dump`: The members of [`FilterDumpProperties`](qemu-qmp-ref.md#object-QMP-qom.FilterDumpProperties "QMP:qom.FilterDumpProperties").
        - When `qom-type` is `filter-mirror`: The members of [`FilterMirrorProperties`](qemu-qmp-ref.md#object-QMP-qom.FilterMirrorProperties "QMP:qom.FilterMirrorProperties").
        - When `qom-type` is `filter-redirector`: The members of [`FilterRedirectorProperties`](qemu-qmp-ref.md#object-QMP-qom.FilterRedirectorProperties "QMP:qom.FilterRedirectorProperties").
        - When `qom-type` is `filter-replay`: The members of [`NetfilterProperties`](qemu-qmp-ref.md#object-QMP-qom.NetfilterProperties "QMP:qom.NetfilterProperties").
        - When `qom-type` is `filter-rewriter`: The members of [`FilterRewriterProperties`](qemu-qmp-ref.md#object-QMP-qom.FilterRewriterProperties "QMP:qom.FilterRewriterProperties").
        - When `qom-type` is `igvm-cfg`: The members of [`IgvmCfgProperties`](qemu-qmp-ref.md#object-QMP-qom.IgvmCfgProperties "QMP:qom.IgvmCfgProperties").
        - When `qom-type` is `input-barrier`: The members of [`InputBarrierProperties`](qemu-qmp-ref.md#object-QMP-qom.InputBarrierProperties "QMP:qom.InputBarrierProperties").
        - When `qom-type` is `input-linux`: The members of [`InputLinuxProperties`](qemu-qmp-ref.md#object-QMP-qom.InputLinuxProperties "QMP:qom.InputLinuxProperties").
        - When `qom-type` is `iommufd`: The members of [`IOMMUFDProperties`](qemu-qmp-ref.md#object-QMP-qom.IOMMUFDProperties "QMP:qom.IOMMUFDProperties").
        - When `qom-type` is `iothread`: The members of [`IothreadProperties`](qemu-qmp-ref.md#object-QMP-qom.IothreadProperties "QMP:qom.IothreadProperties").
        - When `qom-type` is `main-loop`: The members of [`MainLoopProperties`](qemu-qmp-ref.md#object-QMP-qom.MainLoopProperties "QMP:qom.MainLoopProperties").
        - When `qom-type` is `memory-backend-epc`: The members of [`MemoryBackendEpcProperties`](qemu-qmp-ref.md#object-QMP-qom.MemoryBackendEpcProperties "QMP:qom.MemoryBackendEpcProperties").
        - When `qom-type` is `memory-backend-file`: The members of [`MemoryBackendFileProperties`](qemu-qmp-ref.md#object-QMP-qom.MemoryBackendFileProperties "QMP:qom.MemoryBackendFileProperties").
        - When `qom-type` is `memory-backend-memfd`: The members of [`MemoryBackendMemfdProperties`](qemu-qmp-ref.md#object-QMP-qom.MemoryBackendMemfdProperties "QMP:qom.MemoryBackendMemfdProperties").
        - When `qom-type` is `memory-backend-ram`: The members of [`MemoryBackendProperties`](qemu-qmp-ref.md#object-QMP-qom.MemoryBackendProperties "QMP:qom.MemoryBackendProperties").
        - When `qom-type` is `memory-backend-shm`: The members of [`MemoryBackendShmProperties`](qemu-qmp-ref.md#object-QMP-qom.MemoryBackendShmProperties "QMP:qom.MemoryBackendShmProperties").
        - When `qom-type` is `monitor-hmp`: The members of [`MonitorHMPProperties`](qemu-qmp-ref.md#object-QMP-qom.MonitorHMPProperties "QMP:qom.MonitorHMPProperties").
        - When `qom-type` is `monitor-qmp`: The members of [`MonitorQMPProperties`](qemu-qmp-ref.md#object-QMP-qom.MonitorQMPProperties "QMP:qom.MonitorQMPProperties").
        - When `qom-type` is `pr-manager-helper`: The members of [`PrManagerHelperProperties`](qemu-qmp-ref.md#object-QMP-qom.PrManagerHelperProperties "QMP:qom.PrManagerHelperProperties").
        - When `qom-type` is `qtest`: The members of [`QtestProperties`](qemu-qmp-ref.md#object-QMP-qom.QtestProperties "QMP:qom.QtestProperties").
        - When `qom-type` is `rng-builtin`: The members of [`RngProperties`](qemu-qmp-ref.md#object-QMP-qom.RngProperties "QMP:qom.RngProperties").
        - When `qom-type` is `rng-egd`: The members of [`RngEgdProperties`](qemu-qmp-ref.md#object-QMP-qom.RngEgdProperties "QMP:qom.RngEgdProperties").
        - When `qom-type` is `rng-random`: The members of [`RngRandomProperties`](qemu-qmp-ref.md#object-QMP-qom.RngRandomProperties "QMP:qom.RngRandomProperties").
        - When `qom-type` is `secret`: The members of [`SecretProperties`](qemu-qmp-ref.md#object-QMP-crypto.SecretProperties "QMP:crypto.SecretProperties").
        - When `qom-type` is `secret_keyring`: The members of [`SecretKeyringProperties`](qemu-qmp-ref.md#object-QMP-crypto.SecretKeyringProperties "QMP:crypto.SecretKeyringProperties").
        - When `qom-type` is `sev-guest`: The members of [`SevGuestProperties`](qemu-qmp-ref.md#object-QMP-qom.SevGuestProperties "QMP:qom.SevGuestProperties").
        - When `qom-type` is `sev-snp-guest`: The members of [`SevSnpGuestProperties`](qemu-qmp-ref.md#object-QMP-qom.SevSnpGuestProperties "QMP:qom.SevSnpGuestProperties").
        - When `qom-type` is `tdx-guest`: The members of [`TdxGuestProperties`](qemu-qmp-ref.md#object-QMP-qom.TdxGuestProperties "QMP:qom.TdxGuestProperties").
        - When `qom-type` is `thread-context`: The members of [`ThreadContextProperties`](qemu-qmp-ref.md#object-QMP-qom.ThreadContextProperties "QMP:qom.ThreadContextProperties").
        - When `qom-type` is `throttle-group`: The members of [`ThrottleGroupProperties`](qemu-qmp-ref.md#object-QMP-block-core.ThrottleGroupProperties "QMP:block-core.ThrottleGroupProperties").
        - When `qom-type` is `tls-creds-anon`: The members of [`TlsCredsAnonProperties`](qemu-qmp-ref.md#object-QMP-crypto.TlsCredsAnonProperties "QMP:crypto.TlsCredsAnonProperties").
        - When `qom-type` is `tls-creds-psk`: The members of [`TlsCredsPskProperties`](qemu-qmp-ref.md#object-QMP-crypto.TlsCredsPskProperties "QMP:crypto.TlsCredsPskProperties").
        - When `qom-type` is `tls-creds-x509`: The members of [`TlsCredsX509Properties`](qemu-qmp-ref.md#object-QMP-crypto.TlsCredsX509Properties "QMP:crypto.TlsCredsX509Properties").
        - When `qom-type` is `tls-cipher-suites`: The members of [`TlsCredsProperties`](qemu-qmp-ref.md#object-QMP-crypto.TlsCredsProperties "QMP:crypto.TlsCredsProperties").
        - When `qom-type` is `x-remote-object`: The members of [`RemoteObjectProperties`](qemu-qmp-ref.md#object-QMP-qom.RemoteObjectProperties "QMP:qom.RemoteObjectProperties").
        - When `qom-type` is `x-vfio-user-server`: The members of [`VfioUserServerProperties`](qemu-qmp-ref.md#object-QMP-qom.VfioUserServerProperties "QMP:qom.VfioUserServerProperties").

*Command* object-add (Since: 2.0)
:   Create a QOM object.

    Arguments:
    :   - The members of [`ObjectOptions`](qemu-qmp-ref.md#object-QMP-qom.ObjectOptions "QMP:qom.ObjectOptions").

    Errors:
    :   - If `qom-type` is not a valid class name

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "object-add",
    >      "arguments": { "qom-type": "rng-random", "id": "rng1",
    >                     "filename": "/dev/hwrng" } }
    > <- { "return": {} }
    > ```

*Command* object-del (Since: 2.0)
:   Remove a QOM object.

    Arguments:
    :   - **id** (`string`) – the name of the QOM object to remove

    Errors:
    :   - If `id` is not a valid id for a QOM object

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "object-del", "arguments": { "id": "rng1" } }
    > <- { "return": {} }
    > ```

## [Device infrastructure (qdev)](qemu-qmp-ref.md#id32)

*Command* device-list-properties (Since: 1.2)
:   List properties associated with a device.

    Arguments:
    :   - **typename** (`string`) – the type name of a device

    Return:
    :   `[`[`ObjectPropertyInfo`](qemu-qmp-ref.md#object-QMP-qom.ObjectPropertyInfo "QMP:qom.ObjectPropertyInfo")`]` – a list describing a devices properties

    > **Note:**
    >
    > Objects can create properties at runtime, for example to
    > describe links between different devices and/or objects. These
    > properties are not included in the output of this command.

*Command* device_add (Since: 0.13)
:   Add a device.

    Arguments:
    :   - **driver** (`string`) – the name of the new device’s driver
        - **bus** (`string`, *optional*) – the device’s parent bus (device tree path)
        - **id** (`string`, *optional*) – the device’s ID, must be unique

    Features:
    :   - **json-cli** – If present, the “-device” command line option supports
          JSON syntax with a structure identical to the arguments of this
          command.
        - **json-cli-hotplug** – If present, the “-device” command line option
          supports JSON syntax without the reference counting leak that
          broke hot-unplug

    > **Notes:**
    >
    > 1. Additional arguments depend on the type.
    > 2. For detailed information about this command, please refer to
    >    the ‘docs/qdev-device-use.txt’ file.
    > 3. It’s possible to list device properties by running QEMU with
    >    the `-device DEVICE,help` command-line argument, where
    >    DEVICE is the device’s name.

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "device_add",
    >      "arguments": { "driver": "e1000", "id": "net1",
    >                     "bus": "pci.0",
    >                     "mac": "52:54:00:12:34:56" } }
    > <- { "return": {} }
    > ```

*Command* device_del (Since: 0.14)
:   Remove a device from a guest

    Arguments:
    :   - **id** (`string`) – the device’s ID or QOM path

    Errors:
    :   - If `id` is not a valid device, DeviceNotFound

    > **Note:**
    >
    > When this command completes, the device may not be removed
    > from the guest. Hot removal is an operation that requires guest
    > cooperation. This command merely requests that the guest begin
    > the hot removal process. Completion of the device removal
    > process is signaled with a [`DEVICE_DELETED`](qemu-qmp-ref.md#event-QMP-qdev.DEVICE_DELETED "QMP:qdev.DEVICE_DELETED") event. Guest reset
    > will automatically complete removal for all devices. If a
    > guest-side error in the hot removal process is detected, the
    > device will not be removed and a [`DEVICE_UNPLUG_GUEST_ERROR`](qemu-qmp-ref.md#event-QMP-qdev.DEVICE_UNPLUG_GUEST_ERROR "QMP:qdev.DEVICE_UNPLUG_GUEST_ERROR")
    > event is sent. Some errors cannot be detected.

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "device_del",
    >      "arguments": { "id": "net1" } }
    > <- { "return": {} }
    > ```

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "device_del",
    >      "arguments": { "id": "/machine/peripheral-anon/device[0]" } }
    > <- { "return": {} }
    > ```

*Event* DEVICE_DELETED (Since: 1.5)
:   Emitted whenever the device removal completion is acknowledged by
    the guest. At this point, it’s safe to reuse the specified device
    ID. Device removal can be initiated by the guest or by HMP/QMP
    commands.

    Members:
    :   - **device** (`string`, *optional*) – the device’s ID if it has one
        - **path** (`string`) – the device’s QOM path

    > **Example::**
    >
    > ```QMP
    > <- { "event": "DEVICE_DELETED",
    >      "data": { "device": "virtio-net-pci-0",
    >                "path": "/machine/peripheral/virtio-net-pci-0" },
    >      "timestamp": { "seconds": 1265044230, "microseconds": 450486 } }
    > ```

*Event* DEVICE_UNPLUG_GUEST_ERROR (Since: 6.2)
:   Emitted when a device hot unplug fails due to a guest reported
    error.

    Members:
    :   - **device** (`string`, *optional*) – the device’s ID if it has one
        - **path** (`string`) – the device’s QOM path

    > **Example::**
    >
    > ```QMP
    > <- { "event": "DEVICE_UNPLUG_GUEST_ERROR",
    >      "data": { "device": "core1",
    >                "path": "/machine/peripheral/core1" },
    >      "timestamp": { "seconds": 1615570772, "microseconds": 202844 } }
    > ```

*Command* device-sync-config (Since: 9.2)
:   This command is unstable/experimental.

    Synchronize device configuration from host to guest part. First,
    copy the configuration from the host part (backend) to the guest
    part (frontend). Then notify guest software that device
    configuration changed.

    The command may be used to notify the guest about block device
    capacity change. Currently only vhost-user-blk device supports
    this.

    Arguments:
    :   - **id** (`string`) – the device’s ID or QOM path

    Features:
    :   - **unstable** – The command is experimental.

## [Common machine types](qemu-qmp-ref.md#id33)

*Enum* S390CpuEntitlement (Since: 8.2)
:   An enumeration of CPU entitlements that can be assumed by a virtual
    S390 CPU

    Values:
    :   - **auto** – Not documented
        - **low** – Not documented
        - **medium** – Not documented
        - **high** – Not documented

*Enum* CpuTopologyLevel (Since: 9.2)
:   An enumeration of CPU topology levels.

    Values:
    :   - **thread** – thread level, which would also be called SMT level or
          logical processor level. The `threads` option in
          [`SMPConfiguration`](qemu-qmp-ref.md#object-QMP-machine.SMPConfiguration "QMP:machine.SMPConfiguration") is used to configure the topology of this
          level.
        - **core** – core level. The `cores` option in [`SMPConfiguration`](qemu-qmp-ref.md#object-QMP-machine.SMPConfiguration "QMP:machine.SMPConfiguration") is used
          to configure the topology of this level.
        - **module** – module level. The `modules` option in [`SMPConfiguration`](qemu-qmp-ref.md#object-QMP-machine.SMPConfiguration "QMP:machine.SMPConfiguration") is
          used to configure the topology of this level.
        - **cluster** – cluster level. The `clusters` option in [`SMPConfiguration`](qemu-qmp-ref.md#object-QMP-machine.SMPConfiguration "QMP:machine.SMPConfiguration")
          is used to configure the topology of this level.
        - **die** – die level. The `dies` option in [`SMPConfiguration`](qemu-qmp-ref.md#object-QMP-machine.SMPConfiguration "QMP:machine.SMPConfiguration") is used to
          configure the topology of this level.
        - **socket** – socket level, which would also be called package level.
          The `sockets` option in [`SMPConfiguration`](qemu-qmp-ref.md#object-QMP-machine.SMPConfiguration "QMP:machine.SMPConfiguration") is used to configure
          the topology of this level.
        - **book** – book level. The `books` option in [`SMPConfiguration`](qemu-qmp-ref.md#object-QMP-machine.SMPConfiguration "QMP:machine.SMPConfiguration") is used
          to configure the topology of this level.
        - **drawer** – drawer level. The `drawers` option in [`SMPConfiguration`](qemu-qmp-ref.md#object-QMP-machine.SMPConfiguration "QMP:machine.SMPConfiguration") is
          used to configure the topology of this level.
        - **default** – default level. Some architectures will have default
          topology settings (e.g., cache topology), and this special
          level means following the architecture-specific settings.

*Enum* CacheLevelAndType (Since: 9.2)
:   Caches a system may have. The enumeration value here is the
    combination of cache level and cache type.

    Values:
    :   - **l1d** – L1 data cache.
        - **l1i** – L1 instruction cache.
        - **l2** – L2 (unified) cache.
        - **l3** – L3 (unified) cache

*Object* SmpCacheProperties (Since: 9.2)
:   Cache information for SMP system.

    Members:
    :   - **cache** ([`CacheLevelAndType`](qemu-qmp-ref.md#enum-QMP-machine-common.CacheLevelAndType "QMP:machine-common.CacheLevelAndType")) – Cache name, which is the combination of cache level and
          cache type.
        - **topology** ([`CpuTopologyLevel`](qemu-qmp-ref.md#enum-QMP-machine-common.CpuTopologyLevel "QMP:machine-common.CpuTopologyLevel")) – Cache topology level. It accepts the CPU topology
          enumeration as the parameter, i.e., CPUs in the same
          topology container share the same cache.

*Object* SmpCachePropertiesWrapper (Since: 9.2)
:   List wrapper of [`SmpCacheProperties`](qemu-qmp-ref.md#object-QMP-machine-common.SmpCacheProperties "QMP:machine-common.SmpCacheProperties").

    Members:
    :   - **caches** (`[`[`SmpCacheProperties`](qemu-qmp-ref.md#object-QMP-machine-common.SmpCacheProperties "QMP:machine-common.SmpCacheProperties")`]`) – the list of [`SmpCacheProperties`](qemu-qmp-ref.md#object-QMP-machine-common.SmpCacheProperties "QMP:machine-common.SmpCacheProperties").

## [Machines](qemu-qmp-ref.md#id34)

*Enum* SysEmuTarget (Since: 3.0)
:   The comprehensive enumeration of QEMU system emulation (“softmmu”)
    targets. Run “./configure –help” in the project root directory,
    and look for the \*-softmmu targets near the “–target-list” option.
    The individual target constants are not documented here, for the
    time being.

    Values:
    :   - **rx** – since 5.0
        - **avr** – since 5.1
        - **loongarch64** – since 7.1
        - **hexagon** – since 11.0
        - **aarch64** – Not documented
        - **alpha** – Not documented
        - **arm** – Not documented
        - **hppa** – Not documented
        - **i386** – Not documented
        - **m68k** – Not documented
        - **microblaze** – Not documented
        - **mips** – Not documented
        - **mips64** – Not documented
        - **mips64el** – Not documented
        - **mipsel** – Not documented
        - **or1k** – Not documented
        - **ppc** – Not documented
        - **ppc64** – Not documented
        - **riscv32** – Not documented
        - **riscv64** – Not documented
        - **s390x** – Not documented
        - **sh4** – Not documented
        - **sh4eb** – Not documented
        - **sparc** – Not documented
        - **sparc64** – Not documented
        - **tricore** – Not documented
        - **x86_64** – Not documented
        - **xtensa** – Not documented
        - **xtensaeb** – Not documented

    > **Note:**
    >
    > The resulting QMP strings can be appended to the
    > “qemu-system-” prefix to produce the corresponding QEMU
    > executable name. This is true even for “qemu-system-x86_64”.

*Enum* S390CpuState (Since: 2.12)
:   An enumeration of cpu states that can be assumed by a virtual S390
    CPU

    Values:
    :   - **uninitialized** – Not documented
        - **stopped** – Not documented
        - **check-stop** – Not documented
        - **operating** – Not documented
        - **load** – Not documented

*Object* CpuInfoS390 (Since: 2.12)
:   Additional information about a virtual S390 CPU

    Members:
    :   - **cpu-state** ([`S390CpuState`](qemu-qmp-ref.md#enum-QMP-machine.S390CpuState "QMP:machine.S390CpuState")) – the virtual CPU’s state
        - **dedicated** (`boolean`, *optional*) – the virtual CPU’s dedication (since 8.2)
        - **entitlement** ([`S390CpuEntitlement`](qemu-qmp-ref.md#enum-QMP-machine-common.S390CpuEntitlement "QMP:machine-common.S390CpuEntitlement"), *optional*) – the virtual CPU’s entitlement (since 8.2)

*Object* CpuInfoFast (Since: 2.12)
:   Information about a virtual CPU

    Members:
    :   - **cpu-index** (`int`) – index of the virtual CPU
        - **qom-type** (`string`) – QOM type name of the CPU (since 10.1)
        - **qom-path** (`string`) – path to the CPU object in the QOM tree
        - **thread-id** (`int`) – ID of the underlying host thread
        - **props** ([`CpuInstanceProperties`](qemu-qmp-ref.md#object-QMP-machine.CpuInstanceProperties "QMP:machine.CpuInstanceProperties"), *optional*) – properties associated with a virtual CPU, e.g. the socket id
        - **target** ([`SysEmuTarget`](qemu-qmp-ref.md#enum-QMP-machine.SysEmuTarget "QMP:machine.SysEmuTarget")) – the QEMU system emulation target, which determines which
          additional fields will be listed (since 3.0)
        - When `target` is `s390x`: The members of [`CpuInfoS390`](qemu-qmp-ref.md#object-QMP-machine.CpuInfoS390 "QMP:machine.CpuInfoS390").

*Command* query-cpus-fast (Since: 2.12)
:   Return information about all virtual CPUs.

    Return:
    :   `[`[`CpuInfoFast`](qemu-qmp-ref.md#object-QMP-machine.CpuInfoFast "QMP:machine.CpuInfoFast")`]`

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "query-cpus-fast" }
    > <- { "return": [
    >         {
    >             "thread-id": 25627,
    >             "props": {
    >                 "core-id": 0,
    >                 "thread-id": 0,
    >                 "socket-id": 0
    >             },
    >             "qom-path": "/machine/unattached/device[0]",
    >             "target":"x86_64",
    >             "cpu-index": 0
    >         },
    >         {
    >             "thread-id": 25628,
    >             "props": {
    >                 "core-id": 0,
    >                 "thread-id": 0,
    >                 "socket-id": 1
    >             },
    >             "qom-path": "/machine/unattached/device[2]",
    >             "target":"x86_64",
    >             "cpu-index": 1
    >         }
    >     ]
    > }
    > ```

*Object* CompatProperty (Since: 9.1)
:   Property default values specific to a machine type, for use by
    scripts/compare-machine-types.

    Members:
    :   - **qom-type** (`string`) – name of the QOM type to which the default applies
        - **property** (`string`) – name of its property to which the default applies
        - **value** (`string`) – the default value (machine-specific default can overwrite
          the “default” default, to avoid this use -machine none)

*Object* MachineInfo (Since: 1.2)
:   Information describing a machine.

    Members:
    :   - **name** (`string`) – the name of the machine
        - **alias** (`string`, *optional*) – an alias for the machine name
        - **is-default** (`boolean`, *optional*) – whether the machine is default
        - **cpu-max** (`int`) – maximum number of CPUs supported by the machine type
          (since 1.5)
        - **hotpluggable-cpus** (`boolean`) – cpu hotplug via -device is supported (since 2.7)
        - **numa-mem-supported** (`boolean`) – true if ‘-numa node,mem’ option is supported by
          the machine type and false otherwise (since 4.1)
        - **deprecated** (`boolean`) – if true, the machine type is deprecated and may be
          removed in future versions of QEMU according to the QEMU
          deprecation policy (since 4.1)
        - **default-cpu-type** (`string`, *optional*) – default CPU model typename if none is requested
          via the -cpu argument. (since 4.2)
        - **default-ram-id** (`string`, *optional*) – the default ID of initial RAM memory backend
          (since 5.2)
        - **acpi** (`boolean`) – machine type supports ACPI (since 8.0)
        - **compat-props** (`[`[`CompatProperty`](qemu-qmp-ref.md#object-QMP-machine.CompatProperty "QMP:machine.CompatProperty")`]`, *optional*) – The machine type’s compatibility properties. Only
          present when [`query-machines`](qemu-qmp-ref.md#command-QMP-machine.query-machines "QMP:machine.query-machines") argument `compat-props` is true.
          (since 9.1)

    Features:
    :   - **unstable** – Member `compat-props` is experimental.

*Command* query-machines (Since: 1.2)
:   Return a list of supported machines

    Arguments:
    :   - **compat-props** (`boolean`, *optional*) – if true, also return compatibility properties.
          (default: false) (since 9.1)

    Return:
    :   `[`[`MachineInfo`](qemu-qmp-ref.md#object-QMP-machine.MachineInfo "QMP:machine.MachineInfo")`]`

    Features:
    :   - **unstable** – Argument `compat-props` is experimental.

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "query-machines", "arguments": { "compat-props": true } }
    > <- { "return": [
    >           {
    >              "hotpluggable-cpus": true,
    >              "name": "pc-q35-6.2",
    >              "compat-props": [
    >                   {
    >                      "qom-type": "virtio-mem",
    >                      "property": "unplugged-inaccessible",
    >                      "value": "off"
    >                   }
    >               ],
    >               "numa-mem-supported": false,
    >               "default-cpu-type": "qemu64-x86_64-cpu",
    >               "cpu-max": 288,
    >               "deprecated": false,
    >               "default-ram-id": "pc.ram"
    >           },
    >           ...
    >    }
    > ```

*Object* CurrentMachineParams (Since: 4.0)
:   Information describing the running machine parameters.

    Members:
    :   - **wakeup-suspend-support** (`boolean`) – true if the machine supports wake up from
          suspend

*Command* query-current-machine (Since: 4.0)
:   Return information on the current virtual machine.

    Return:
    :   [`CurrentMachineParams`](qemu-qmp-ref.md#object-QMP-machine.CurrentMachineParams "QMP:machine.CurrentMachineParams")

*Object* QemuTargetInfo (Since: 1.2)
:   Information on the target configuration built into the QEMU binary.

    Members:
    :   - **arch** ([`SysEmuTarget`](qemu-qmp-ref.md#enum-QMP-machine.SysEmuTarget "QMP:machine.SysEmuTarget")) – the target architecture

*Command* query-target (Since: 1.2)
:   Return information about the target for this QEMU

    Return:
    :   [`QemuTargetInfo`](qemu-qmp-ref.md#object-QMP-machine.QemuTargetInfo "QMP:machine.QemuTargetInfo")

*Object* UuidInfo (Since: 0.14)
:   Guest UUID information (Universally Unique Identifier).

    Members:
    :   - **UUID** (`string`) – the UUID of the guest

    > **Note:**
    >
    > If no UUID was specified for the guest, the nil UUID (all
    > zeroes) is returned.

*Command* query-uuid (Since: 0.14)
:   Query the guest UUID information.

    Return:
    :   [`UuidInfo`](qemu-qmp-ref.md#object-QMP-machine.UuidInfo "QMP:machine.UuidInfo")

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "query-uuid" }
    > <- { "return": { "UUID": "550e8400-e29b-41d4-a716-446655440000" } }
    > ```

*Object* GuidInfo (Since: 2.9)
:   GUID information.

    Members:
    :   - **guid** (`string`) – the globally unique identifier

*Command* query-vm-generation-id (Since: 2.9)
:   Show Virtual Machine Generation ID

    Return:
    :   [`GuidInfo`](qemu-qmp-ref.md#object-QMP-machine.GuidInfo "QMP:machine.GuidInfo")

*Command* system_reset (Since: 0.14)
:   Performs a hard reset of a guest.

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "system_reset" }
    > <- { "return": {} }
    > ```

*Command* system_powerdown (Since: 0.14)
:   Requests that a guest perform a powerdown operation.

    > **Note:**
    >
    > A guest may or may not respond to this command. This
    > command returning does not indicate that a guest has accepted the
    > request or that it has shut down. Many guests will respond to
    > this command by prompting the user in some way.

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "system_powerdown" }
    > <- { "return": {} }
    > ```

*Command* system_wakeup (Since: 1.1)
:   Wake up guest from suspend. If the guest has wake-up from suspend
    support enabled (wakeup-suspend-support flag from
    [`query-current-machine`](qemu-qmp-ref.md#command-QMP-machine.query-current-machine "QMP:machine.query-current-machine")), wake-up guest from suspend if the guest is
    in SUSPENDED state. Return an error otherwise.

    > **Note:**
    >
    > Prior to 4.0, this command does nothing in case the guest
    > isn’t suspended.

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "system_wakeup" }
    > <- { "return": {} }
    > ```

*Enum* LostTickPolicy (Since: 2.0)
:   Policy for handling lost ticks in timer devices. Ticks end up
    getting lost when, for example, the guest is paused.

    Values:
    :   - **discard** – throw away the missed ticks and continue with future
          injection normally. The guest OS will see the timer jump ahead
          by a potentially quite significant amount all at once, as if the
          intervening chunk of time had simply not existed; needless to
          say, such a sudden jump can easily confuse a guest OS which is
          not specifically prepared to deal with it. Assuming the guest
          OS can deal correctly with the time jump, the time in the guest
          and in the host should now match.
        - **delay** – continue to deliver ticks at the normal rate. The guest OS
          will not notice anything is amiss, as from its point of view
          time will have continued to flow normally. The time in the
          guest should now be behind the time in the host by exactly the
          amount of time during which ticks have been missed.
        - **slew** – deliver ticks at a higher rate to catch up with the missed
          ticks. The guest OS will not notice anything is amiss, as from
          its point of view time will have continued to flow normally.
          Once the timer has managed to catch up with all the missing
          ticks, the time in the guest and in the host should match.

*Command* inject-nmi (Since: 0.14)
:   Injects a Non-Maskable Interrupt (machine specific: for example on
    s390x CCW only the first vCPU receives the NMI, but on x86 machines
    all vCPUs receive it). The command fails when the guest doesn’t
    support injecting.

    > **Note:**
    >
    > Prior to 2.1, this command was only supported for x86 and
    > s390 VMs.

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "inject-nmi" }
    > <- { "return": {} }
    > ```

*Enum* NumaOptionsType (Since: 2.1)
:   Values:
    :   - **node** – NUMA nodes configuration
        - **dist** – NUMA distance configuration (since 2.10)
        - **cpu** – property based CPU(s) to node mapping (Since: 2.10)
        - **hmat-lb** – memory latency and bandwidth information (Since: 5.0)
        - **hmat-cache** – memory side cache information (Since: 5.0)

*Object* NumaOptions (Since: 2.1)
:   A discriminated record of NUMA options. (for OptsVisitor)

    Members:
    :   - **type** ([`NumaOptionsType`](qemu-qmp-ref.md#enum-QMP-machine.NumaOptionsType "QMP:machine.NumaOptionsType")) – NUMA option type
        - When `type` is `node`: The members of [`NumaNodeOptions`](qemu-qmp-ref.md#object-QMP-machine.NumaNodeOptions "QMP:machine.NumaNodeOptions").
        - When `type` is `dist`: The members of [`NumaDistOptions`](qemu-qmp-ref.md#object-QMP-machine.NumaDistOptions "QMP:machine.NumaDistOptions").
        - When `type` is `cpu`: The members of [`NumaCpuOptions`](qemu-qmp-ref.md#object-QMP-machine.NumaCpuOptions "QMP:machine.NumaCpuOptions").
        - When `type` is `hmat-lb`: The members of [`NumaHmatLBOptions`](qemu-qmp-ref.md#object-QMP-machine.NumaHmatLBOptions "QMP:machine.NumaHmatLBOptions").
        - When `type` is `hmat-cache`: The members of [`NumaHmatCacheOptions`](qemu-qmp-ref.md#object-QMP-machine.NumaHmatCacheOptions "QMP:machine.NumaHmatCacheOptions").

*Object* NumaNodeOptions (Since: 2.1)
:   Create a guest NUMA node. (for OptsVisitor)

    Members:
    :   - **nodeid** (`int`, *optional*) – NUMA node ID (increase by 1 from 0 if omitted)
        - **cpus** (`[``int``]`, *optional*) – VCPUs belonging to this node (assign VCPUS round-robin if
          omitted)
        - **mem** (`int`, *optional*) – memory size of this node; mutually exclusive with `memdev`.
          Equally divide total memory among nodes if both `mem` and `memdev`
          are omitted.
        - **memdev** (`string`, *optional*) – memory backend object. If specified for one node, it must
          be specified for all nodes.
        - **initiator** (`int`, *optional*) – defined in ACPI 6.3 Chapter 5.2.27.3 Table 5-145, points
          to the nodeid which has the memory controller responsible for
          this NUMA node. This field provides additional information as
          to the initiator node that is closest (as in directly attached)
          to this node, and therefore has the best performance (since 5.0)

*Object* NumaDistOptions (Since: 2.10)
:   Set the distance between 2 NUMA nodes.

    Members:
    :   - **src** (`int`) – source NUMA node.
        - **dst** (`int`) – destination NUMA node.
        - **val** (`int`) – NUMA distance from source node to destination node. When a
          node is unreachable from another node, set the distance between
          them to 255.

*Object* CXLFixedMemoryWindowOptions (Since: 7.1)
:   Create a CXL Fixed Memory Window

    Members:
    :   - **size** (`int`) – Size of the Fixed Memory Window in bytes. Must be a multiple
          of 256MiB.
        - **interleave-granularity** (`int`, *optional*) – Number of contiguous bytes for which
          accesses will go to a given interleave target. Accepted values
          [256, 512, 1k, 2k, 4k, 8k, 16k]
        - **targets** (`[``string``]`) – Target root bridge IDs from -device …,id=<ID> for each
          root bridge.

*Object* CXLFMWProperties (Since: 7.1)
:   List of CXL Fixed Memory Windows.

    Members:
    :   - **cxl-fmw** (`[`[`CXLFixedMemoryWindowOptions`](qemu-qmp-ref.md#object-QMP-machine.CXLFixedMemoryWindowOptions "QMP:machine.CXLFixedMemoryWindowOptions")`]`) – List of [`CXLFixedMemoryWindowOptions`](qemu-qmp-ref.md#object-QMP-machine.CXLFixedMemoryWindowOptions "QMP:machine.CXLFixedMemoryWindowOptions")

*Enum* X86CPURegister32 (Since: 1.5)
:   A X86 32-bit register

    Values:
    :   - **EAX** – Not documented
        - **EBX** – Not documented
        - **ECX** – Not documented
        - **EDX** – Not documented
        - **ESP** – Not documented
        - **EBP** – Not documented
        - **ESI** – Not documented
        - **EDI** – Not documented

*Object* X86CPUFeatureWordInfo (Since: 1.5)
:   Information about a X86 CPU feature word

    Members:
    :   - **cpuid-input-eax** (`int`) – Input EAX value for CPUID instruction for that
          feature word
        - **cpuid-input-ecx** (`int`, *optional*) – Input ECX value for CPUID instruction for that
          feature word
        - **cpuid-register** ([`X86CPURegister32`](qemu-qmp-ref.md#enum-QMP-machine.X86CPURegister32 "QMP:machine.X86CPURegister32")) – Output register containing the feature bits
        - **features** (`int`) – value of output register, containing the feature bits

*Object* DummyForceArrays (Since: 2.5)
:   Not used by QMP; hack to let us use X86CPUFeatureWordInfoList
    internally

    Members:
    :   - **unused** (`[`[`X86CPUFeatureWordInfo`](qemu-qmp-ref.md#object-QMP-machine.X86CPUFeatureWordInfo "QMP:machine.X86CPUFeatureWordInfo")`]`) – Not documented

*Object* NumaCpuOptions (Since: 2.10)
:   Option “-numa cpu” overrides default cpu to node mapping. It
    accepts the same set of cpu properties as returned by
    [`query-hotpluggable-cpus[].props`](qemu-qmp-ref.md#command-QMP-machine.query-hotpluggable-cpus "QMP:machine.query-hotpluggable-cpus"), where
    node-id could be used to override default node mapping.

    Members:
    :   - The members of [`CpuInstanceProperties`](qemu-qmp-ref.md#object-QMP-machine.CpuInstanceProperties "QMP:machine.CpuInstanceProperties").

*Enum* HmatLBMemoryHierarchy (Since: 5.0)
:   The memory hierarchy in the System Locality Latency and Bandwidth
    Information Structure of HMAT (Heterogeneous Memory Attribute Table)

    For more information about [`HmatLBMemoryHierarchy`](qemu-qmp-ref.md#enum-QMP-machine.HmatLBMemoryHierarchy "QMP:machine.HmatLBMemoryHierarchy"), see chapter
    5.2.27.4: Table 5-146: Field “Flags” of ACPI 6.3 spec.

    Values:
    :   - **memory** – the structure represents the memory performance
        - **first-level** – first level of memory side cache
        - **second-level** – second level of memory side cache
        - **third-level** – third level of memory side cache

*Enum* HmatLBDataType (Since: 5.0)
:   Data type in the System Locality Latency and Bandwidth Information
    Structure of HMAT (Heterogeneous Memory Attribute Table)

    For more information about [`HmatLBDataType`](qemu-qmp-ref.md#enum-QMP-machine.HmatLBDataType "QMP:machine.HmatLBDataType"), see chapter 5.2.27.4:
    Table 5-146: Field “Data Type” of ACPI 6.3 spec.

    Values:
    :   - **access-latency** – access latency (nanoseconds)
        - **read-latency** – read latency (nanoseconds)
        - **write-latency** – write latency (nanoseconds)
        - **access-bandwidth** – access bandwidth (Bytes per second)
        - **read-bandwidth** – read bandwidth (Bytes per second)
        - **write-bandwidth** – write bandwidth (Bytes per second)

*Object* NumaHmatLBOptions (Since: 5.0)
:   Set the system locality latency and bandwidth information between
    Initiator and Target proximity Domains.

    For more information about [`NumaHmatLBOptions`](qemu-qmp-ref.md#object-QMP-machine.NumaHmatLBOptions "QMP:machine.NumaHmatLBOptions"), see chapter
    5.2.27.4: Table 5-146 of ACPI 6.3 spec.

    Members:
    :   - **initiator** (`int`) – the Initiator Proximity Domain.
        - **target** (`int`) – the Target Proximity Domain.
        - **hierarchy** ([`HmatLBMemoryHierarchy`](qemu-qmp-ref.md#enum-QMP-machine.HmatLBMemoryHierarchy "QMP:machine.HmatLBMemoryHierarchy")) – the Memory Hierarchy. Indicates the performance of
          memory or side cache.
        - **data-type** ([`HmatLBDataType`](qemu-qmp-ref.md#enum-QMP-machine.HmatLBDataType "QMP:machine.HmatLBDataType")) – presents the type of data, access/read/write latency or
          hit latency.
        - **latency** (`int`, *optional*) – the value of latency from `initiator` to `target` proximity
          domain, the latency unit is “ns(nanosecond)”.
        - **bandwidth** (`int`, *optional*) – the value of bandwidth between `initiator` and `target`
          proximity domain, the bandwidth unit is “Bytes per second”.

*Enum* HmatCacheAssociativity (Since: 5.0)
:   Cache associativity in the Memory Side Cache Information Structure
    of HMAT

    For more information of [`HmatCacheAssociativity`](qemu-qmp-ref.md#enum-QMP-machine.HmatCacheAssociativity "QMP:machine.HmatCacheAssociativity"), see chapter
    5.2.27.5: Table 5-147 of ACPI 6.3 spec.

    Values:
    :   - **none** – None (no memory side cache in this proximity domain, or cache
          associativity unknown)
        - **direct** – Direct Mapped
        - **complex** – Complex Cache Indexing (implementation specific)

*Enum* HmatCacheWritePolicy (Since: 5.0)
:   Cache write policy in the Memory Side Cache Information Structure of
    HMAT

    For more information of [`HmatCacheWritePolicy`](qemu-qmp-ref.md#enum-QMP-machine.HmatCacheWritePolicy "QMP:machine.HmatCacheWritePolicy"), see chapter
    5.2.27.5: Table 5-147: Field “Cache Attributes” of ACPI 6.3 spec.

    Values:
    :   - **none** – None (no memory side cache in this proximity domain, or cache
          write policy unknown)
        - **write-back** – Write Back (WB)
        - **write-through** – Write Through (WT)

*Object* NumaHmatCacheOptions (Since: 5.0)
:   Set the memory side cache information for a given memory domain.

    For more information of [`NumaHmatCacheOptions`](qemu-qmp-ref.md#object-QMP-machine.NumaHmatCacheOptions "QMP:machine.NumaHmatCacheOptions"), see chapter
    5.2.27.5: Table 5-147: Field “Cache Attributes” of ACPI 6.3 spec.

    Members:
    :   - **node-id** (`int`) – the memory proximity domain to which the memory belongs.
        - **size** (`int`) – the size of memory side cache in bytes.
        - **level** (`int`) – the cache level described in this structure.
        - **associativity** ([`HmatCacheAssociativity`](qemu-qmp-ref.md#enum-QMP-machine.HmatCacheAssociativity "QMP:machine.HmatCacheAssociativity")) – the cache associativity,
          none/direct-mapped/complex(complex cache indexing).
        - **policy** ([`HmatCacheWritePolicy`](qemu-qmp-ref.md#enum-QMP-machine.HmatCacheWritePolicy "QMP:machine.HmatCacheWritePolicy")) – the write policy, none/write-back/write-through.
        - **line** (`int`) – the cache line size in bytes.

*Command* memsave (Since: 0.14)
:   Save a portion of guest memory to a file.

    Arguments:
    :   - **val** (`int`) – the virtual address of the guest to start from
        - **size** (`int`) – the size of memory region to save
        - **filename** (`string`) – the file to save the memory to as binary data
        - **cpu-index** (`int`, *optional*) – the index of the virtual CPU to use for translating the
          virtual address (defaults to CPU 0)

    > **Caution:**
    >
    > Errors were not reliably returned until 1.1.

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "memsave",
    >      "arguments": { "val": 10,
    >                     "size": 100,
    >                     "filename": "/tmp/virtual-mem-dump" } }
    > <- { "return": {} }
    > ```

*Command* pmemsave (Since: 0.14)
:   Save a portion of guest physical memory to a file.

    Arguments:
    :   - **val** (`int`) – the physical address of the guest to start from
        - **size** (`int`) – the size of memory region to save
        - **filename** (`string`) – the file to save the memory to as binary data

    > **Caution:**
    >
    > Errors were not reliably returned until 1.1.

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "pmemsave",
    >      "arguments": { "val": 10,
    >                     "size": 100,
    >                     "filename": "/tmp/physical-mem-dump" } }
    > <- { "return": {} }
    > ```

*Object* Memdev (Since: 2.1)
:   Information about memory backend

    Members:
    :   - **id** (`string`, *optional*) – backend’s ID if backend has ‘id’ property (since 2.9)
        - **size** (`int`) – memory backend size
        - **merge** (`boolean`) – whether memory merge support is enabled
        - **dump** (`boolean`) – whether memory backend’s memory is included in a core dump
        - **prealloc** (`boolean`) – whether memory was preallocated
        - **share** (`boolean`) – whether memory is private to QEMU or shared (since 6.1)
        - **reserve** (`boolean`, *optional*) – whether swap space (or huge pages) was reserved if
          applicable. This corresponds to the user configuration and not
          the actual behavior implemented in the OS to perform the
          reservation. For example, Linux will never reserve swap space
          for shared file mappings. (since 6.1)
        - **host-nodes** (`[``int``]`) – host nodes for its memory policy
        - **policy** ([`HostMemPolicy`](qemu-qmp-ref.md#enum-QMP-common.HostMemPolicy "QMP:common.HostMemPolicy")) – memory policy of memory backend

*Command* query-memdev (Since: 2.1)
:   Return information for all memory backends.

    Return:
    :   `[`[`Memdev`](qemu-qmp-ref.md#object-QMP-machine.Memdev "QMP:machine.Memdev")`]`

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "query-memdev" }
    > <- { "return": [
    >        {
    >          "id": "mem1",
    >          "size": 536870912,
    >          "merge": false,
    >          "dump": true,
    >          "prealloc": false,
    >          "share": false,
    >          "host-nodes": [0, 1],
    >          "policy": "bind"
    >        },
    >        {
    >          "size": 536870912,
    >          "merge": false,
    >          "dump": true,
    >          "prealloc": true,
    >          "share": false,
    >          "host-nodes": [2, 3],
    >          "policy": "preferred"
    >        }
    >      ]
    >    }
    > ```

*Object* CpuInstanceProperties (Since: 2.7)
:   Properties identifying a CPU.

    Which members are optional and which mandatory depends on the
    architecture and board.

    For s390x see [CPU topology on s390x](../system/s390x/cpu-topology.md#cpu-topology-s390x).

    The ids other than the node-id specify the position of the CPU
    within the CPU topology (as defined by the machine property “smp”,
    thus see also type [`SMPConfiguration`](qemu-qmp-ref.md#object-QMP-machine.SMPConfiguration "QMP:machine.SMPConfiguration"))

    Members:
    :   - **node-id** (`int`, *optional*) – NUMA node ID the CPU belongs to
        - **drawer-id** (`int`, *optional*) – drawer number within CPU topology the CPU belongs to
          (since 8.2)
        - **book-id** (`int`, *optional*) – book number within parent container the CPU belongs to
          (since 8.2)
        - **socket-id** (`int`, *optional*) – socket number within parent container the CPU belongs to
        - **die-id** (`int`, *optional*) – die number within the parent container the CPU belongs to
          (since 4.1)
        - **cluster-id** (`int`, *optional*) – cluster number within the parent container the CPU
          belongs to (since 7.1)
        - **module-id** (`int`, *optional*) – module number within the parent container the CPU
          belongs to (since 9.1)
        - **core-id** (`int`, *optional*) – core number within the parent container the CPU belongs to
        - **thread-id** (`int`, *optional*) – thread number within the core the CPU belongs to

*Object* HotpluggableCPU (Since: 2.7)
:   Members:
    :   - **type** (`string`) – CPU object type for usage with [`device_add`](qemu-qmp-ref.md#command-QMP-qdev.device_add "QMP:qdev.device_add") command
        - **props** ([`CpuInstanceProperties`](qemu-qmp-ref.md#object-QMP-machine.CpuInstanceProperties "QMP:machine.CpuInstanceProperties")) – list of properties to pass for hotplugging a CPU with
          [`device_add`](qemu-qmp-ref.md#command-QMP-qdev.device_add "QMP:qdev.device_add")
        - **vcpus-count** (`int`) – number of logical VCPU threads [`HotpluggableCPU`](qemu-qmp-ref.md#object-QMP-machine.HotpluggableCPU "QMP:machine.HotpluggableCPU")
          provides
        - **qom-path** (`string`, *optional*) – link to existing CPU object if CPU is present or omitted
          if CPU is not present.

    > **Note:**
    >
    > Management should be prepared to pass through additional
    > properties with [`device_add`](qemu-qmp-ref.md#command-QMP-qdev.device_add "QMP:qdev.device_add").

*Command* query-hotpluggable-cpus (Since: 2.7)
:   Return:
    :   `[`[`HotpluggableCPU`](qemu-qmp-ref.md#object-QMP-machine.HotpluggableCPU "QMP:machine.HotpluggableCPU")`]`

    > **Example::**
    >
    > For pseries machine type started with
    > `-smp 2,cores=2,maxcpus=4 -cpu POWER8`:
    >
    > ```QMP
    > -> { "execute": "query-hotpluggable-cpus" }
    > <- {"return": [
    >      { "props": { "core-id": 8 }, "type": "POWER8-spapr-cpu-core",
    >        "vcpus-count": 1 },
    >      { "props": { "core-id": 0 }, "type": "POWER8-spapr-cpu-core",
    >        "vcpus-count": 1, "qom-path": "/machine/unattached/device[0]"}
    >    ]}
    > ```

    > **Example::**
    >
    > For pc machine type started with `-smp 1,maxcpus=2`:
    >
    > ```QMP
    > -> { "execute": "query-hotpluggable-cpus" }
    > <- {"return": [
    >      {
    >         "type": "qemu64-x86_64-cpu", "vcpus-count": 1,
    >         "props": {"core-id": 0, "socket-id": 1, "thread-id": 0}
    >      },
    >      {
    >         "qom-path": "/machine/unattached/device[0]",
    >         "type": "qemu64-x86_64-cpu", "vcpus-count": 1,
    >         "props": {"core-id": 0, "socket-id": 0, "thread-id": 0}
    >      }
    >    ]}
    > ```

    > **Example::**
    >
    > For s390x-virtio-ccw machine type started with
    > `-smp 1,maxcpus=2 -cpu qemu`:
    >
    > ```QMP
    > -> { "execute": "query-hotpluggable-cpus" }
    > <- {"return": [
    >      {
    >         "type": "qemu-s390x-cpu", "vcpus-count": 1,
    >         "props": { "core-id": 1 }
    >      },
    >      {
    >         "qom-path": "/machine/unattached/device[0]",
    >         "type": "qemu-s390x-cpu", "vcpus-count": 1,
    >         "props": { "core-id": 0 }
    >      }
    >    ]}
    > ```

*Command* set-numa-node (Since: 3.0)
:   Runtime equivalent of ‘-numa’ CLI option, available at preconfigure
    stage to configure numa mapping before initializing machine.

    Arguments:
    :   - The members of [`NumaOptions`](qemu-qmp-ref.md#object-QMP-machine.NumaOptions "QMP:machine.NumaOptions").

*Command* balloon (Since: 0.14)
:   Request the balloon driver to change its balloon size.

    Arguments:
    :   - **value** (`int`) –

          the target logical size of the VM in bytes. We can deduce
          the size of the balloon using this formula:

          > logical_vm_size = vm_ram_size - balloon_size

          From it we have: balloon_size = vm_ram_size - `value`

    Errors:
    :   - If the balloon driver is enabled but not functional because
          the KVM kernel module cannot support it, KVMMissingCap
        - If no balloon device is present, DeviceNotActive

    > **Note:**
    >
    > This command just issues a request to the guest. When it
    > returns, the balloon size may not have changed. A guest can
    > change the balloon size independent of this command.

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "balloon", "arguments": { "value": 536870912 } }
    > <- { "return": {} }
    > ```
    >
    > With a 2.5GiB guest this command inflated the ballon to 3GiB.

*Object* BalloonInfo (Since: 0.14)
:   Information about the guest balloon device.

    Members:
    :   - **actual** (`int`) – the logical size of the VM in bytes. Formula used:
          logical_vm_size = vm_ram_size - balloon_size

*Command* query-balloon (Since: 0.14)
:   Return information about the balloon device.

    Return:
    :   [`BalloonInfo`](qemu-qmp-ref.md#object-QMP-machine.BalloonInfo "QMP:machine.BalloonInfo")

    Errors:
    :   - If the balloon driver is enabled but not functional because
          the KVM kernel module cannot support it, KVMMissingCap
        - If no balloon device is present, DeviceNotActive

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "query-balloon" }
    > <- { "return": {
    >          "actual": 1073741824
    >       }
    >    }
    > ```

*Event* BALLOON_CHANGE (Since: 1.2)
:   Emitted when the guest changes the actual BALLOON level. This value
    is equivalent to the `actual` field return by the [`query-balloon`](qemu-qmp-ref.md#command-QMP-machine.query-balloon "QMP:machine.query-balloon")
    command

    Members:
    :   - **actual** (`int`) – the logical size of the VM in bytes. Formula used:
          logical_vm_size = vm_ram_size - balloon_size

    > **Note:**
    >
    > This event is rate-limited.

    > **Example::**
    >
    > ```QMP
    > <- { "event": "BALLOON_CHANGE",
    >      "data": { "actual": 944766976 },
    >      "timestamp": { "seconds": 1267020223, "microseconds": 435656 } }
    > ```

*Object* HvBalloonInfo (Since: 8.2)
:   hv-balloon guest-provided memory status information.

    Members:
    :   - **committed** (`int`) – the amount of memory in use inside the guest plus the
          amount of the memory unusable inside the guest (ballooned out,
          offline, etc.)
        - **available** (`int`) – the amount of the memory inside the guest available for
          new allocations (“free”)

*Command* query-hv-balloon-status-report (Since: 8.2)
:   Return the hv-balloon driver data contained in the last received
    “STATUS” message from the guest.

    Return:
    :   [`HvBalloonInfo`](qemu-qmp-ref.md#object-QMP-machine.HvBalloonInfo "QMP:machine.HvBalloonInfo")

    Errors:
    :   - If no hv-balloon device is present, guest memory status
          reporting is not enabled or no guest memory status report
          received yet, GenericError

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "query-hv-balloon-status-report" }
    > <- { "return": {
    >          "committed": 816640000,
    >          "available": 3333054464
    >       }
    >    }
    > ```

*Event* HV_BALLOON_STATUS_REPORT (Since: 8.2)
:   Emitted when the hv-balloon driver receives a “STATUS” message from
    the guest.

    > **Note:**
    >
    > This event is rate-limited.

    Members:
    :   - The members of [`HvBalloonInfo`](qemu-qmp-ref.md#object-QMP-machine.HvBalloonInfo "QMP:machine.HvBalloonInfo").

    > **Example::**
    >
    > ```QMP
    > <- { "event": "HV_BALLOON_STATUS_REPORT",
    >      "data": { "committed": 816640000, "available": 3333054464 },
    >      "timestamp": { "seconds": 1600295492, "microseconds": 661044 } }
    > ```

*Object* MemoryInfo (Since: 2.11)
:   Actual memory information in bytes.

    Members:
    :   - **base-memory** (`int`) – size of “base” memory specified with command line
          option -m.
        - **plugged-memory** (`int`, *optional*) – size of memory that can be hot-unplugged. This
          field is omitted if target doesn’t support memory hotplug (i.e.
          CONFIG_MEM_DEVICE not defined at build time).

*Command* query-memory-size-summary (Since: 2.11)
:   Return the amount of initially allocated and present hotpluggable
    (if enabled) memory in bytes.

    Return:
    :   [`MemoryInfo`](qemu-qmp-ref.md#object-QMP-machine.MemoryInfo "QMP:machine.MemoryInfo")

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "query-memory-size-summary" }
    > <- { "return": { "base-memory": 4294967296, "plugged-memory": 0 } }
    > ```

*Object* PCDIMMDeviceInfo (Since: 2.1)
:   PCDIMMDevice state information

    Members:
    :   - **id** (`string`, *optional*) – device’s ID
        - **addr** (`int`) – physical address, where device is mapped
        - **size** (`int`) – size of memory that the device provides
        - **slot** (`int`) – slot number at which device is plugged in
        - **node** (`int`) – NUMA node number where device is plugged in
        - **memdev** (`string`) – memory backend linked with device
        - **hotplugged** (`boolean`) – true if device was hotplugged
        - **hotpluggable** (`boolean`) – true if device if could be added/removed while
          machine is running

*Object* VirtioPMEMDeviceInfo (Since: 4.1)
:   VirtioPMEM state information

    Members:
    :   - **id** (`string`, *optional*) – device’s ID
        - **memaddr** (`int`) – physical address in memory, where device is mapped
        - **size** (`int`) – size of memory that the device provides
        - **memdev** (`string`) – memory backend linked with device

*Object* VirtioMEMDeviceInfo (Since: 5.1)
:   VirtioMEMDevice state information

    Members:
    :   - **id** (`string`, *optional*) – device’s ID
        - **memaddr** (`int`) – physical address in memory, where device is mapped
        - **requested-size** (`int`) – the user requested size of the device
        - **size** (`int`) – the (current) size of memory that the device provides
        - **max-size** (`int`) – the maximum size of memory that the device can provide
        - **block-size** (`int`) – the block size of memory that the device provides
        - **node** (`int`) – NUMA node number where device is assigned to
        - **memdev** (`string`) – memory backend linked with the region

*Object* SgxEPCDeviceInfo (Since: 6.2)
:   Sgx EPC state information

    Members:
    :   - **id** (`string`, *optional*) – device’s ID
        - **memaddr** (`int`) – physical address in memory, where device is mapped
        - **size** (`int`) – size of memory that the device provides
        - **memdev** (`string`) – memory backend linked with device
        - **node** (`int`) – the numa node (Since: 7.0)

*Object* HvBalloonDeviceInfo (Since: 8.2)
:   hv-balloon provided memory state information

    Members:
    :   - **id** (`string`, *optional*) – device’s ID
        - **memaddr** (`int`, *optional*) – physical address in memory, where device is mapped
        - **max-size** (`int`) – the maximum size of memory that the device can provide
        - **memdev** (`string`, *optional*) – memory backend linked with device

*Object* SpMemDeviceInfo (Since: 11.1)
:   sp-mem device state information

    Members:
    :   - **id** (`string`, *optional*) – device’s ID
        - **addr** (`int`) – physical address, where device is mapped
        - **size** (`int`) – size of memory that the device provides, in bytes
        - **node** (`int`) – NUMA proximity domain to which the device is assigned
        - **memdev** (`string`) – memory backend linked with device

*Enum* MemoryDeviceInfoKind (Since: 2.1)
:   Values:
    :   - **nvdimm** – since 2.12
        - **virtio-pmem** – since 4.1
        - **virtio-mem** – since 5.1
        - **sgx-epc** – since 6.2.
        - **hv-balloon** – since 8.2.
        - **sp-mem** – since 11.1.
        - **dimm** – Not documented

*Object* PCDIMMDeviceInfoWrapper (Since: 2.1)
:   Members:
    :   - **data** ([`PCDIMMDeviceInfo`](qemu-qmp-ref.md#object-QMP-machine.PCDIMMDeviceInfo "QMP:machine.PCDIMMDeviceInfo")) – PCDIMMDevice state information

*Object* VirtioPMEMDeviceInfoWrapper (Since: 2.1)
:   Members:
    :   - **data** ([`VirtioPMEMDeviceInfo`](qemu-qmp-ref.md#object-QMP-machine.VirtioPMEMDeviceInfo "QMP:machine.VirtioPMEMDeviceInfo")) – VirtioPMEM state information

*Object* VirtioMEMDeviceInfoWrapper (Since: 2.1)
:   Members:
    :   - **data** ([`VirtioMEMDeviceInfo`](qemu-qmp-ref.md#object-QMP-machine.VirtioMEMDeviceInfo "QMP:machine.VirtioMEMDeviceInfo")) – VirtioMEMDevice state information

*Object* SgxEPCDeviceInfoWrapper (Since: 6.2)
:   Members:
    :   - **data** ([`SgxEPCDeviceInfo`](qemu-qmp-ref.md#object-QMP-machine.SgxEPCDeviceInfo "QMP:machine.SgxEPCDeviceInfo")) – Sgx EPC state information

*Object* HvBalloonDeviceInfoWrapper (Since: 8.2)
:   Members:
    :   - **data** ([`HvBalloonDeviceInfo`](qemu-qmp-ref.md#object-QMP-machine.HvBalloonDeviceInfo "QMP:machine.HvBalloonDeviceInfo")) – hv-balloon provided memory state information

*Object* SpMemDeviceInfoWrapper (Since: 11.1)
:   Members:
    :   - **data** ([`SpMemDeviceInfo`](qemu-qmp-ref.md#object-QMP-machine.SpMemDeviceInfo "QMP:machine.SpMemDeviceInfo")) – sp-mem device state information

*Object* MemoryDeviceInfo (Since: 2.1)
:   Union containing information about a memory device

    Members:
    :   - **type** ([`MemoryDeviceInfoKind`](qemu-qmp-ref.md#enum-QMP-machine.MemoryDeviceInfoKind "QMP:machine.MemoryDeviceInfoKind")) – memory device type
        - When `type` is `dimm`: The members of [`PCDIMMDeviceInfoWrapper`](qemu-qmp-ref.md#object-QMP-machine.PCDIMMDeviceInfoWrapper "QMP:machine.PCDIMMDeviceInfoWrapper").
        - When `type` is `nvdimm`: The members of [`PCDIMMDeviceInfoWrapper`](qemu-qmp-ref.md#object-QMP-machine.PCDIMMDeviceInfoWrapper "QMP:machine.PCDIMMDeviceInfoWrapper").
        - When `type` is `virtio-pmem`: The members of [`VirtioPMEMDeviceInfoWrapper`](qemu-qmp-ref.md#object-QMP-machine.VirtioPMEMDeviceInfoWrapper "QMP:machine.VirtioPMEMDeviceInfoWrapper").
        - When `type` is `virtio-mem`: The members of [`VirtioMEMDeviceInfoWrapper`](qemu-qmp-ref.md#object-QMP-machine.VirtioMEMDeviceInfoWrapper "QMP:machine.VirtioMEMDeviceInfoWrapper").
        - When `type` is `sgx-epc`: The members of [`SgxEPCDeviceInfoWrapper`](qemu-qmp-ref.md#object-QMP-machine.SgxEPCDeviceInfoWrapper "QMP:machine.SgxEPCDeviceInfoWrapper").
        - When `type` is `hv-balloon`: The members of [`HvBalloonDeviceInfoWrapper`](qemu-qmp-ref.md#object-QMP-machine.HvBalloonDeviceInfoWrapper "QMP:machine.HvBalloonDeviceInfoWrapper").
        - When `type` is `sp-mem`: The members of [`SpMemDeviceInfoWrapper`](qemu-qmp-ref.md#object-QMP-machine.SpMemDeviceInfoWrapper "QMP:machine.SpMemDeviceInfoWrapper").

*Object* SgxEPC (Since: 6.2)
:   Sgx EPC cmdline information

    Members:
    :   - **memdev** (`string`) – memory backend linked with device
        - **node** (`int`) – the numa node (Since: 7.0)

*Object* SgxEPCProperties (Since: 6.2)
:   SGX properties of machine types.

    Members:
    :   - **sgx-epc** (`[`[`SgxEPC`](qemu-qmp-ref.md#object-QMP-machine.SgxEPC "QMP:machine.SgxEPC")`]`) – list of ids of memory-backend-epc objects.

*Command* query-memory-devices (Since: 2.1)
:   Lists available memory devices and their state

    Return:
    :   `[`[`MemoryDeviceInfo`](qemu-qmp-ref.md#object-QMP-machine.MemoryDeviceInfo "QMP:machine.MemoryDeviceInfo")`]`

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "query-memory-devices" }
    > <- { "return": [ { "data":
    >                       { "addr": 5368709120,
    >                         "hotpluggable": true,
    >                         "hotplugged": true,
    >                         "id": "d1",
    >                         "memdev": "/objects/memX",
    >                         "node": 0,
    >                         "size": 1073741824,
    >                         "slot": 0},
    >                    "type": "dimm"
    >                  } ] }
    > ```

*Event* MEMORY_DEVICE_SIZE_CHANGE (Since: 5.1)
:   Emitted when the size of a memory device changes. Only emitted for
    memory devices that can actually change the size (e.g., virtio-mem
    due to guest action).

    Members:
    :   - **id** (`string`, *optional*) – device’s ID
        - **size** (`int`) – the new size of memory that the device provides
        - **qom-path** (`string`) – path to the device object in the QOM tree (since 6.2)

    > **Note:**
    >
    > This event is rate-limited.

    > **Example::**
    >
    > ```QMP
    > <- { "event": "MEMORY_DEVICE_SIZE_CHANGE",
    >      "data": { "id": "vm0", "size": 1073741824,
    >                "qom-path": "/machine/unattached/device[2]" },
    >      "timestamp": { "seconds": 1588168529, "microseconds": 201316 } }
    > ```

*Object* BootConfiguration (Since: 7.1)
:   Schema for virtual machine boot configuration.

    Members:
    :   - **order** (`string`, *optional*) – Boot order (a=floppy, c=hard disk, d=CD-ROM, n=network)
        - **once** (`string`, *optional*) – Boot order to apply on first boot
        - **menu** (`boolean`, *optional*) – Whether to show a boot menu
        - **splash** (`string`, *optional*) – The name of the file to be passed to the firmware as logo
          picture, if `menu` is true.
        - **splash-time** (`int`, *optional*) – How long to show the logo picture, in milliseconds
        - **reboot-timeout** (`int`, *optional*) – Timeout before guest reboots after boot fails
        - **strict** (`boolean`, *optional*) – Whether to attempt booting from devices not included in the
          boot order

*Object* SMPConfiguration (Since: 6.1)
:   Schema for CPU topology configuration. A missing value lets QEMU
    figure out a suitable value based on the ones that are provided.

    The members other than `cpus` and `maxcpus` define a topology of
    containers.

    The ordering from highest/coarsest to lowest/finest is: `drawers`,
    `books`, `sockets`, `dies`, `clusters`, `cores`, `threads`.

    Different architectures support different subsets of topology
    containers.

    For example, s390x does not have clusters and dies, and the socket
    is the parent container of cores.

    Members:
    :   - **cpus** (`int`, *optional*) – number of virtual CPUs in the virtual machine
        - **maxcpus** (`int`, *optional*) – maximum number of hotpluggable virtual CPUs in the virtual
          machine
        - **drawers** (`int`, *optional*) – number of drawers in the CPU topology (since 8.2)
        - **books** (`int`, *optional*) – number of books in the CPU topology (since 8.2)
        - **sockets** (`int`, *optional*) – number of sockets per parent container
        - **dies** (`int`, *optional*) – number of dies per parent container
        - **clusters** (`int`, *optional*) – number of clusters per parent container (since 7.0)
        - **modules** (`int`, *optional*) – number of modules per parent container (since 9.1)
        - **cores** (`int`, *optional*) – number of cores per parent container
        - **threads** (`int`, *optional*) – number of threads per core

*Command* x-query-irq (Since: 6.2)
:   This command is unstable/experimental.

    Query interrupt statistics

    Features:
    :   - **unstable** – This command is meant for debugging.

    Return:
    :   [`HumanReadableText`](qemu-qmp-ref.md#object-QMP-common.HumanReadableText "QMP:common.HumanReadableText") – interrupt statistics

*Command* x-query-jit (Since: 6.2)
:   This command is unstable/experimental.

    *Availability*: `CONFIG_TCG`

    Query TCG compiler statistics

    Features:
    :   - **unstable** – This command is meant for debugging.

    Return:
    :   [`HumanReadableText`](qemu-qmp-ref.md#object-QMP-common.HumanReadableText "QMP:common.HumanReadableText") – TCG compiler statistics

*Command* x-query-numa (Since: 6.2)
:   This command is unstable/experimental.

    Query NUMA topology information

    Features:
    :   - **unstable** – This command is meant for debugging.

    Return:
    :   [`HumanReadableText`](qemu-qmp-ref.md#object-QMP-common.HumanReadableText "QMP:common.HumanReadableText") – topology information

*Command* x-query-ramblock (Since: 6.2)
:   This command is unstable/experimental.

    Query system ramblock information

    Features:
    :   - **unstable** – This command is meant for debugging.

    Return:
    :   [`HumanReadableText`](qemu-qmp-ref.md#object-QMP-common.HumanReadableText "QMP:common.HumanReadableText") – system ramblock information

*Command* x-query-roms (Since: 6.2)
:   This command is unstable/experimental.

    Query information on the registered ROMS

    Features:
    :   - **unstable** – This command is meant for debugging.

    Return:
    :   [`HumanReadableText`](qemu-qmp-ref.md#object-QMP-common.HumanReadableText "QMP:common.HumanReadableText") – registered ROMs

*Command* x-query-usb (Since: 6.2)
:   This command is unstable/experimental.

    Query information on the USB devices

    Features:
    :   - **unstable** – This command is meant for debugging.

    Return:
    :   [`HumanReadableText`](qemu-qmp-ref.md#object-QMP-common.HumanReadableText "QMP:common.HumanReadableText") – USB device information

*Enum* SmbiosEntryPointType (Since: 7.0)
:   Values:
    :   - **32** – SMBIOS version 2.1 (32-bit) Entry Point
        - **64** – SMBIOS version 3.0 (64-bit) Entry Point
        - **auto** – Either 2.x or 3.x SMBIOS version, 2.x if configuration can be
          described by it and 3.x otherwise (since: 9.0)

*Object* MemorySizeConfiguration (Since: 7.1)
:   Schema for memory size configuration.

    Members:
    :   - **size** (`int`, *optional*) – memory size in bytes
        - **max-size** (`int`, *optional*) – maximum hotpluggable memory size in bytes
        - **slots** (`int`, *optional*) – number of available memory slots for hotplug

*Command* dumpdtb (Since: 7.2)
:   *Availability*: `CONFIG_FDT`

    Save the FDT in dtb format.

    Arguments:
    :   - **filename** (`string`) – name of the dtb file to be created

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "dumpdtb" }
    >      "arguments": { "filename": "fdt.dtb" } }
    > <- { "return": {} }
    > ```

*Command* x-query-interrupt-controllers (Since: 9.1)
:   This command is unstable/experimental.

    Query information on interrupt controller devices

    Features:
    :   - **unstable** – This command is meant for debugging.

    Return:
    :   [`HumanReadableText`](qemu-qmp-ref.md#object-QMP-common.HumanReadableText "QMP:common.HumanReadableText") – Interrupt controller devices information

*Object* FirmwareLog (Since: 10.2)
:   Members:
    :   - **version** (`string`, *optional*) – Firmware version.
        - **log** (`string`) – Firmware debug log, in base64 encoding. First and last log
          line might be incomplete.

*Command* query-firmware-log (Since: 10.2)
:   Find firmware memory log buffer in guest memory, return content.

    Arguments:
    :   - **max-size** (`int`, *optional*) – limit the amount of log data returned. Up to 1 MiB of
          log data is allowed. In case the amount of log data is larger
          than `max-size` the tail of the log is returned.

    Return:
    :   [`FirmwareLog`](qemu-qmp-ref.md#object-QMP-machine.FirmwareLog "QMP:machine.FirmwareLog")

*Command* dump-skeys (Since: 2.5)
:   Dump the storage keys for an s390x guest

    Arguments:
    :   - **filename** (`string`) – the path to the file to dump to

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "dump-skeys",
    >      "arguments": { "filename": "/tmp/skeys" } }
    > <- { "return": {} }
    > ```

*Object* CpuModelInfo (Since: 2.8)
:   Virtual CPU model.

    A CPU model consists of the name of a CPU definition, to which delta
    changes are applied (e.g. features added/removed). Most magic
    values that an architecture might require should be hidden behind
    the name. However, if required, architectures can expose relevant
    properties.

    Members:
    :   - **name** (`string`) – the name of the CPU definition the model is based on
        - **props** (`value`, *optional*) – a dictionary of QOM properties to be applied

*Enum* CpuModelExpansionType (Since: 2.8)
:   An enumeration of CPU model expansion types.

    Values:
    :   - **static** – Expand to a static CPU model, a combination of a static
          base model name and property delta changes. As the static base
          model will never change, the expanded CPU model will be the
          same, independent of QEMU version, machine type, machine
          options, and accelerator options. Therefore, the resulting
          model can be used by tooling without having to specify a
          compatibility machine - e.g. when displaying the “host” model.
          The `static` CPU models are migration-safe.
        - **full** – Expand all properties. The produced model is not guaranteed
          to be migration-safe, but allows tooling to get an insight and
          work with model details.

    > **Note:**
    >
    > When a non-migration-safe CPU model is expanded in static
    > mode, some features enabled by the CPU model may be omitted,
    > because they can’t be implemented by a static CPU model
    > definition (e.g. cache info passthrough and PMU passthrough in
    > x86). If you need an accurate representation of the features
    > enabled by a non-migration-safe CPU model, use `full`. If you
    > need a static representation that will keep ABI compatibility
    > even when changing QEMU version or machine-type, use `static` (but
    > keep in mind that some features may be omitted).

*Enum* CpuModelCompareResult (Since: 2.8)
:   An enumeration of CPU model comparison results. The result is
    usually calculated using e.g. CPU features or CPU generations.

    Values:
    :   - **incompatible** – If model A is incompatible to model B, model A is not
          guaranteed to run where model B runs and the other way around.
        - **identical** – If model A is identical to model B, model A is
          guaranteed to run where model B runs and the other way around.
        - **superset** – If model A is a superset of model B, model B is
          guaranteed to run where model A runs. There are no guarantees
          about the other way.
        - **subset** – If model A is a subset of model B, model A is guaranteed to
          run where model B runs. There are no guarantees about the other
          way.

*Object* CpuModelBaselineInfo (Since: 2.8)
:   The result of a CPU model baseline.

    Members:
    :   - **model** ([`CpuModelInfo`](qemu-qmp-ref.md#object-QMP-machine.CpuModelInfo "QMP:machine.CpuModelInfo")) – the baselined [`CpuModelInfo`](qemu-qmp-ref.md#object-QMP-machine.CpuModelInfo "QMP:machine.CpuModelInfo").

*Object* CpuModelCompareInfo (Since: 2.8)
:   The result of a CPU model comparison.

    Members:
    :   - **result** ([`CpuModelCompareResult`](qemu-qmp-ref.md#enum-QMP-machine.CpuModelCompareResult "QMP:machine.CpuModelCompareResult")) – The result of the compare operation.
        - **responsible-properties** (`[``string``]`) – List of properties that led to the
          comparison result not being identical.

    `responsible-properties` is a list of QOM property names that led to
    both CPUs not being detected as identical. For identical models,
    this list is empty. If a QOM property is read-only, that means
    there’s no known way to make the CPU models identical. If the
    special property name “type” is included, the models are by
    definition not identical and cannot be made identical.

*Command* query-cpu-model-comparison (Since: 2.8)
:   Compares two CPU models, `modela` and `modelb`, returning how they
    compare in a specific configuration. The results indicates how both
    models compare regarding runnability. This result can be used by
    tooling to make decisions if a certain CPU model will run in a
    certain configuration or if a compatible CPU model has to be created
    by baselining.

    Usually, a CPU model is compared against the maximum possible CPU
    model of a certain configuration (e.g. the “host” model for KVM).
    If that CPU model is identical or a subset, it will run in that
    configuration.

    The result returned by this command may be affected by:

    - QEMU version: CPU models may look different depending on the QEMU
      version. (Except for CPU models reported as “static” in
      [`query-cpu-definitions`](qemu-qmp-ref.md#command-QMP-machine.query-cpu-definitions "QMP:machine.query-cpu-definitions").)
    - machine-type: CPU model may look different depending on the
      machine-type. (Except for CPU models reported as “static” in
      [`query-cpu-definitions`](qemu-qmp-ref.md#command-QMP-machine.query-cpu-definitions "QMP:machine.query-cpu-definitions").)
    - machine options (including accelerator): in some architectures,
      CPU models may look different depending on machine and accelerator
      options. (Except for CPU models reported as “static” in
      [`query-cpu-definitions`](qemu-qmp-ref.md#command-QMP-machine.query-cpu-definitions "QMP:machine.query-cpu-definitions").)
    - “-cpu” arguments and global properties: arguments to the -cpu
      option and global properties may affect expansion of CPU models.
      Using [`query-cpu-model-expansion`](qemu-qmp-ref.md#command-QMP-machine.query-cpu-model-expansion "QMP:machine.query-cpu-model-expansion") while using these is not
      advised.

    Some architectures may not support comparing CPU models. s390x
    supports comparing CPU models.

    Arguments:
    :   - **modela** ([`CpuModelInfo`](qemu-qmp-ref.md#object-QMP-machine.CpuModelInfo "QMP:machine.CpuModelInfo")) – description of the first CPU model to compare, referred to
          as “model A” in [`CpuModelCompareResult`](qemu-qmp-ref.md#enum-QMP-machine.CpuModelCompareResult "QMP:machine.CpuModelCompareResult")
        - **modelb** ([`CpuModelInfo`](qemu-qmp-ref.md#object-QMP-machine.CpuModelInfo "QMP:machine.CpuModelInfo")) – description of the second CPU model to compare, referred to
          as “model B” in [`CpuModelCompareResult`](qemu-qmp-ref.md#enum-QMP-machine.CpuModelCompareResult "QMP:machine.CpuModelCompareResult")

    Return:
    :   [`CpuModelCompareInfo`](qemu-qmp-ref.md#object-QMP-machine.CpuModelCompareInfo "QMP:machine.CpuModelCompareInfo") – a [`CpuModelCompareInfo`](qemu-qmp-ref.md#object-QMP-machine.CpuModelCompareInfo "QMP:machine.CpuModelCompareInfo") describing how both CPU models
        compare

    Errors:
    :   - if comparing CPU models is not supported by the target
        - if a model cannot be used
        - if a model contains an unknown cpu definition name, unknown
          properties or properties with wrong types.

*Command* query-cpu-model-baseline (Since: 2.8)
:   Baseline two CPU models, `modela` and `modelb`, creating a compatible
    third model. The created model will always be a static,
    migration-safe CPU model (see “static” CPU model expansion for
    details).

    This interface can be used by tooling to create a compatible CPU
    model out two CPU models. The created CPU model will be identical
    to or a subset of both CPU models when comparing them. Therefore,
    the created CPU model is guaranteed to run where the given CPU
    models run.

    The result returned by this command may be affected by:

    - QEMU version: CPU models may look different depending on the QEMU
      version. (Except for CPU models reported as “static” in
      [`query-cpu-definitions`](qemu-qmp-ref.md#command-QMP-machine.query-cpu-definitions "QMP:machine.query-cpu-definitions").)
    - machine-type: CPU model may look different depending on the
      machine-type. (Except for CPU models reported as “static” in
      [`query-cpu-definitions`](qemu-qmp-ref.md#command-QMP-machine.query-cpu-definitions "QMP:machine.query-cpu-definitions").)
    - machine options (including accelerator): in some architectures,
      CPU models may look different depending on machine and accelerator
      options. (Except for CPU models reported as “static” in
      [`query-cpu-definitions`](qemu-qmp-ref.md#command-QMP-machine.query-cpu-definitions "QMP:machine.query-cpu-definitions").)
    - “-cpu” arguments and global properties: arguments to the -cpu
      option and global properties may affect expansion of CPU models.
      Using [`query-cpu-model-expansion`](qemu-qmp-ref.md#command-QMP-machine.query-cpu-model-expansion "QMP:machine.query-cpu-model-expansion") while using these is not
      advised.

    Some architectures may not support baselining CPU models. s390x
    supports baselining CPU models.

    Arguments:
    :   - **modela** ([`CpuModelInfo`](qemu-qmp-ref.md#object-QMP-machine.CpuModelInfo "QMP:machine.CpuModelInfo")) – description of the first CPU model to baseline
        - **modelb** ([`CpuModelInfo`](qemu-qmp-ref.md#object-QMP-machine.CpuModelInfo "QMP:machine.CpuModelInfo")) – description of the second CPU model to baseline

    Return:
    :   [`CpuModelBaselineInfo`](qemu-qmp-ref.md#object-QMP-machine.CpuModelBaselineInfo "QMP:machine.CpuModelBaselineInfo") – a [`CpuModelBaselineInfo`](qemu-qmp-ref.md#object-QMP-machine.CpuModelBaselineInfo "QMP:machine.CpuModelBaselineInfo") describing the baselined CPU model

    Errors:
    :   - if baselining CPU models is not supported by the target
        - if a model cannot be used
        - if a model contains an unknown cpu definition name, unknown
          properties or properties with wrong types.

*Object* CpuModelExpansionInfo (Since: 2.8)
:   The result of a cpu model expansion.

    Members:
    :   - **model** ([`CpuModelInfo`](qemu-qmp-ref.md#object-QMP-machine.CpuModelInfo "QMP:machine.CpuModelInfo")) – the expanded [`CpuModelInfo`](qemu-qmp-ref.md#object-QMP-machine.CpuModelInfo "QMP:machine.CpuModelInfo").
        - **deprecated-props** (`[``string``]`, *optional*) – an optional list of properties that are flagged
          as deprecated by the CPU vendor. The list depends on the
          [`CpuModelExpansionType`](qemu-qmp-ref.md#enum-QMP-machine.CpuModelExpansionType "QMP:machine.CpuModelExpansionType"): “static” properties are a subset of the
          enabled-properties for the expanded model; “full” properties are
          a set of properties that are deprecated across all models for
          the architecture. (since: 10.1 – since 9.1 on s390x –).

*Command* query-cpu-model-expansion (Since: 2.8)
:   Expands a given CPU model, `model`, (or a combination of CPU model +
    additional options) to different granularities, specified by `type`,
    allowing tooling to get an understanding what a specific CPU model
    looks like in QEMU under a certain configuration.

    This interface can be used to query the “host” CPU model.

    The data returned by this command may be affected by:

    - QEMU version: CPU models may look different depending on the QEMU
      version. (Except for CPU models reported as “static” in
      [`query-cpu-definitions`](qemu-qmp-ref.md#command-QMP-machine.query-cpu-definitions "QMP:machine.query-cpu-definitions").)
    - machine-type: CPU model may look different depending on the
      machine-type. (Except for CPU models reported as “static” in
      [`query-cpu-definitions`](qemu-qmp-ref.md#command-QMP-machine.query-cpu-definitions "QMP:machine.query-cpu-definitions").)
    - machine options (including accelerator): in some architectures,
      CPU models may look different depending on machine and accelerator
      options. (Except for CPU models reported as “static” in
      [`query-cpu-definitions`](qemu-qmp-ref.md#command-QMP-machine.query-cpu-definitions "QMP:machine.query-cpu-definitions").)
    - “-cpu” arguments and global properties: arguments to the -cpu
      option and global properties may affect expansion of CPU models.
      Using [`query-cpu-model-expansion`](qemu-qmp-ref.md#command-QMP-machine.query-cpu-model-expansion "QMP:machine.query-cpu-model-expansion") while using these is not
      advised.

    Some architectures may not support all expansion types. s390x
    supports “full” and “static”. Arm only supports “full”.

    Arguments:
    :   - **model** ([`CpuModelInfo`](qemu-qmp-ref.md#object-QMP-machine.CpuModelInfo "QMP:machine.CpuModelInfo")) – description of the CPU model to expand
        - **type** ([`CpuModelExpansionType`](qemu-qmp-ref.md#enum-QMP-machine.CpuModelExpansionType "QMP:machine.CpuModelExpansionType")) – expansion type, specifying how to expand the CPU model

    Return:
    :   [`CpuModelExpansionInfo`](qemu-qmp-ref.md#object-QMP-machine.CpuModelExpansionInfo "QMP:machine.CpuModelExpansionInfo") – a [`CpuModelExpansionInfo`](qemu-qmp-ref.md#object-QMP-machine.CpuModelExpansionInfo "QMP:machine.CpuModelExpansionInfo") describing the expanded CPU model

    Errors:
    :   - if expanding CPU models is not supported
        - if the model cannot be expanded
        - if the model contains an unknown CPU definition name, unknown
          properties or properties with a wrong type
        - if an expansion type is not supported

*Object* CpuDefinitionInfo (Since: 1.2)
:   Virtual CPU definition.

    Members:
    :   - **name** (`string`) – the name of the CPU definition
        - **migration-safe** (`boolean`, *optional*) – whether a CPU definition can be safely used for
          migration in combination with a QEMU compatibility machine when
          migrating between different QEMU versions and between hosts with
          different sets of (hardware or software) capabilities. If not
          provided, information is not available and callers should not
          assume the CPU definition to be migration-safe. (since 2.8)
        - **static** (`boolean`) – whether a CPU definition is static and will not change
          depending on QEMU version, machine type, machine options and
          accelerator options. A static model is always migration-safe.
          (since 2.8)
        - **unavailable-features** (`[``string``]`, *optional*) – List of properties that prevent the CPU model
          from running in the current host. (since 2.8)
        - **typename** (`string`) – Type name that can be used as argument to
          [`device-list-properties`](qemu-qmp-ref.md#command-QMP-qdev.device-list-properties "QMP:qdev.device-list-properties"), to introspect properties configurable
          using -cpu or -global. (since 2.9)
        - **alias-of** (`string`, *optional*) – Name of CPU model this model is an alias for. The target
          of the CPU model alias may change depending on the machine type.
          Management software is supposed to translate CPU model aliases
          in the VM configuration, because aliases may stop being
          migration-safe in the future (since 4.1)
        - **deprecated** (`boolean`) – If true, this CPU model is deprecated and may be
          removed in some future version of QEMU according to the QEMU
          deprecation policy. (since 5.2)

    `unavailable-features` is a list of QOM property names that represent
    CPU model attributes that prevent the CPU from running. If the QOM
    property is read-only, that means there’s no known way to make the
    CPU model run in the current host. Implementations that choose not
    to provide specific information return the property name “type”. If
    the property is read-write, it means that it MAY be possible to run
    the CPU model in the current host if that property is changed.
    Management software can use it as hints to suggest or choose an
    alternative for the user, or just to generate meaningful error
    messages explaining why the CPU model can’t be used. If
    `unavailable-features` is an empty list, the CPU model is runnable
    using the current host and machine-type. If `unavailable-features`
    is not present, runnability information for the CPU is not
    available.

*Command* query-cpu-definitions (Since: 1.2)
:   Return a list of supported virtual CPU definitions

    Return:
    :   `[`[`CpuDefinitionInfo`](qemu-qmp-ref.md#object-QMP-machine.CpuDefinitionInfo "QMP:machine.CpuDefinitionInfo")`]`

*Enum* S390CpuPolarization (Since: 8.2)
:   An enumeration of CPU polarization that can be assumed by a virtual
    S390 CPU

    Values:
    :   - **horizontal** – Not documented
        - **vertical** – Not documented

*Command* set-cpu-topology (Since: 8.2)
:   This command is unstable/experimental.

    Modify the topology by moving the CPU inside the topology tree, or
    by changing a modifier attribute of a CPU. Absent values will not
    be modified.

    Arguments:
    :   - **core-id** (`int`) – the vCPU ID to be moved
        - **socket-id** (`int`, *optional*) – destination socket to move the vCPU to
        - **book-id** (`int`, *optional*) – destination book to move the vCPU to
        - **drawer-id** (`int`, *optional*) – destination drawer to move the vCPU to
        - **entitlement** ([`S390CpuEntitlement`](qemu-qmp-ref.md#enum-QMP-machine-common.S390CpuEntitlement "QMP:machine-common.S390CpuEntitlement"), *optional*) – entitlement to set
        - **dedicated** (`boolean`, *optional*) – whether the provisioning of real to virtual CPU is
          dedicated

    Features:
    :   - **unstable** – This command is experimental.

*Event* CPU_POLARIZATION_CHANGE (Since: 8.2)
:   This event is unstable/experimental.

    Emitted when the guest asks to change the polarization.

    The guest can tell the host (via the PTF instruction) whether the
    CPUs should be provisioned using horizontal or vertical
    polarization.

    On horizontal polarization the host is expected to provision all
    vCPUs equally.

    On vertical polarization the host can provision each vCPU
    differently. The guest will get information on the details of the
    provisioning the next time it uses the STSI(15) instruction.

    Members:
    :   - **polarization** ([`S390CpuPolarization`](qemu-qmp-ref.md#enum-QMP-machine-s390x.S390CpuPolarization "QMP:machine-s390x.S390CpuPolarization")) – polarization specified by the guest

    Features:
    :   - **unstable** – This event is experimental.

    > **Example::**
    >
    > ```QMP
    > <- { "event": "CPU_POLARIZATION_CHANGE",
    >      "data": { "polarization": "horizontal" },
    >      "timestamp": { "seconds": 1401385907, "microseconds": 422329 } }
    > ```

*Object* CpuPolarizationInfo (Since: 8.2)
:   The result of a CPU polarization query.

    Members:
    :   - **polarization** ([`S390CpuPolarization`](qemu-qmp-ref.md#enum-QMP-machine-s390x.S390CpuPolarization "QMP:machine-s390x.S390CpuPolarization")) – the CPU polarization

*Command* query-s390x-cpu-polarization (Since: 8.2)
:   This command is unstable/experimental.

    Features:
    :   - **unstable** – This command is experimental.

    Return:
    :   [`CpuPolarizationInfo`](qemu-qmp-ref.md#object-QMP-machine-s390x.CpuPolarizationInfo "QMP:machine-s390x.CpuPolarizationInfo") – the machine’s CPU polarization

*Event* SCLP_CPI_INFO_AVAILABLE (Since: 10.2)
:   This event is unstable/experimental.

    Emitted when the Control-Program Identification data is available in
    the QOM tree.

    Features:
    :   - **unstable** – This event is experimental.

    > **Example::**
    >
    > ```QMP
    > <- { "event": "SCLP_CPI_INFO_AVAILABLE",
    >      "timestamp": { "seconds": 1401385907, "microseconds": 422329 } }
    > ```

## [Record/replay](qemu-qmp-ref.md#id35)

*Enum* ReplayMode (Since: 2.5)
:   Mode of the replay subsystem.

    Values:
    :   - **none** – normal execution mode. Replay or record are not enabled.
        - **record** – record mode. All non-deterministic data is written into
          the replay log.
        - **play** – replay mode. Non-deterministic data required for system
          execution is read from the log.

*Object* ReplayInfo (Since: 5.2)
:   Record/replay information.

    Members:
    :   - **mode** ([`ReplayMode`](qemu-qmp-ref.md#enum-QMP-replay.ReplayMode "QMP:replay.ReplayMode")) – current mode.
        - **filename** (`string`, *optional*) – name of the record/replay log file. It is present only
          in record or replay modes, when the log is recorded or replayed.
        - **icount** (`int`) – current number of executed instructions.

*Command* query-replay (Since: 5.2)
:   Retrieve the record/replay information. It includes current
    instruction count which may be used for [`replay-break`](qemu-qmp-ref.md#command-QMP-replay.replay-break "QMP:replay.replay-break") and
    [`replay-seek`](qemu-qmp-ref.md#command-QMP-replay.replay-seek "QMP:replay.replay-seek") commands.

    Return:
    :   [`ReplayInfo`](qemu-qmp-ref.md#object-QMP-replay.ReplayInfo "QMP:replay.ReplayInfo") – record/replay information.

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "query-replay" }
    > <- { "return": { "mode": "play", "filename": "log.rr", "icount": 220414 } }
    > ```

*Command* replay-break (Since: 5.2)
:   Set replay breakpoint at instruction count `icount`. Execution stops
    when the specified instruction is reached. There can be at most one
    breakpoint. When breakpoint is set, any prior one is removed. The
    breakpoint may be set only in replay mode and only “in the future”,
    i.e. at instruction counts greater than the current one. The
    current instruction count can be observed with [`query-replay`](qemu-qmp-ref.md#command-QMP-replay.query-replay "QMP:replay.query-replay").

    Arguments:
    :   - **icount** (`int`) – instruction count to stop at

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "replay-break", "arguments": { "icount": 220414 } }
    > <- { "return": {} }
    > ```

*Command* replay-delete-break (Since: 5.2)
:   Remove replay breakpoint which was set with [`replay-break`](qemu-qmp-ref.md#command-QMP-replay.replay-break "QMP:replay.replay-break"). The
    command is ignored when there are no replay breakpoints.

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "replay-delete-break" }
    > <- { "return": {} }
    > ```

*Command* replay-seek (Since: 5.2)
:   Automatically proceed to the instruction count `icount`, when
    replaying the execution. The command automatically loads nearest
    snapshot and replays the execution to find the desired instruction.
    When there is no preceding snapshot or the execution is not
    replayed, then the command fails. Instruction count can be obtained
    with the [`query-replay`](qemu-qmp-ref.md#command-QMP-replay.query-replay "QMP:replay.query-replay") command.

    Arguments:
    :   - **icount** (`int`) – target instruction count

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "replay-seek", "arguments": { "icount": 220414 } }
    > <- { "return": {} }
    > ```

## [Yank feature](qemu-qmp-ref.md#id36)

*Enum* YankInstanceType (Since: 6.0)
:   An enumeration of yank instance types. See [`YankInstance`](qemu-qmp-ref.md#object-QMP-yank.YankInstance "QMP:yank.YankInstance") for more
    information.

    Values:
    :   - **block-node** – Not documented
        - **chardev** – Not documented
        - **migration** – Not documented

*Object* YankInstanceBlockNode (Since: 6.0)
:   Specifies which block graph node to yank. See [`YankInstance`](qemu-qmp-ref.md#object-QMP-yank.YankInstance "QMP:yank.YankInstance") for
    more information.

    Members:
    :   - **node-name** (`string`) – the name of the block graph node

*Object* YankInstanceChardev (Since: 6.0)
:   Specifies which character device to yank. See [`YankInstance`](qemu-qmp-ref.md#object-QMP-yank.YankInstance "QMP:yank.YankInstance") for
    more information.

    Members:
    :   - **id** (`string`) – the chardev’s ID

*Object* YankInstance (Since: 6.0)
:   A yank instance can be yanked with the [`yank`](qemu-qmp-ref.md#command-QMP-yank.yank "QMP:yank.yank") qmp command to recover
    from a hanging QEMU.

    Members:
    :   - **type** ([`YankInstanceType`](qemu-qmp-ref.md#enum-QMP-yank.YankInstanceType "QMP:yank.YankInstanceType")) – yank instance type
        - When `type` is `block-node`: The members of [`YankInstanceBlockNode`](qemu-qmp-ref.md#object-QMP-yank.YankInstanceBlockNode "QMP:yank.YankInstanceBlockNode").
        - When `type` is `chardev`: The members of [`YankInstanceChardev`](qemu-qmp-ref.md#object-QMP-yank.YankInstanceChardev "QMP:yank.YankInstanceChardev").

    Currently implemented yank instances:

    - nbd block device: Yanking it will shut down the connection to the
      nbd server without attempting to reconnect.
    - socket chardev: Yanking it will shut down the connected socket.
    - migration: Yanking it will shut down all migration connections.
      Unlike [`migrate_cancel`](qemu-qmp-ref.md#command-QMP-migration.migrate_cancel "QMP:migration.migrate_cancel"), it will not notify the migration process,
      so migration will go into `failed` state, instead of `cancelled`
      state. [`yank`](qemu-qmp-ref.md#command-QMP-yank.yank "QMP:yank.yank") should be used to recover from hangs.

*Command* yank (Since: 6.0)
:   Try to recover from hanging QEMU by yanking the specified instances.
    See [`YankInstance`](qemu-qmp-ref.md#object-QMP-yank.YankInstance "QMP:yank.YankInstance") for more information.

    Arguments:
    :   - **instances** (`[`[`YankInstance`](qemu-qmp-ref.md#object-QMP-yank.YankInstance "QMP:yank.YankInstance")`]`) – the instances to be yanked

    Errors:
    :   - If any of the YankInstances doesn’t exist, DeviceNotFound

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "yank",
    >      "arguments": {
    >          "instances": [
    >               { "type": "block-node",
    >                 "node-name": "nbd0" }
    >          ] } }
    > <- { "return": {} }
    > ```

*Command* query-yank (Since: 6.0)
:   Query yank instances. See [`YankInstance`](qemu-qmp-ref.md#object-QMP-yank.YankInstance "QMP:yank.YankInstance") for more information.

    Return:
    :   `[`[`YankInstance`](qemu-qmp-ref.md#object-QMP-yank.YankInstance "QMP:yank.YankInstance")`]`

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "query-yank" }
    > <- { "return": [
    >          { "type": "block-node",
    >            "node-name": "nbd0" }
    >      ] }
    > ```

## [Miscellanea](qemu-qmp-ref.md#id37)

*Command* add_client (Since: 0.14)
:   Allow client connections for VNC, Spice and socket based character
    devices to be passed in to QEMU via SCM_RIGHTS.

    If the FD associated with `fdname` is not a socket, the command will
    fail and the FD will be closed.

    Arguments:
    :   - **protocol** (`string`) – protocol name. Valid names are “vnc”, “spice”,
          “`dbus-display`” or the name of a character device (e.g. from
          -chardev id=XXXX)
        - **fdname** (`string`) – file descriptor name previously passed via [`getfd`](qemu-qmp-ref.md#command-QMP-misc.getfd "QMP:misc.getfd") command
        - **skipauth** (`boolean`, *optional*) – whether to skip authentication. Only applies to “vnc”
          and “spice” protocols
        - **tls** (`boolean`, *optional*) – whether to perform TLS. Only applies to the “spice” protocol

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "add_client", "arguments": { "protocol": "vnc",
    >                                              "fdname": "myclient" } }
    > <- { "return": {} }
    > ```

*Object* NameInfo (Since: 0.14)
:   Guest name information.

    Members:
    :   - **name** (`string`, *optional*) – The name of the guest

*Command* query-name (Since: 0.14)
:   Return the name information of a guest.

    Return:
    :   [`NameInfo`](qemu-qmp-ref.md#object-QMP-misc.NameInfo "QMP:misc.NameInfo")

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "query-name" }
    > <- { "return": { "name": "qemu-name" } }
    > ```

*Object* IOThreadInfo (Since: 2.0)
:   Information about an iothread

    Members:
    :   - **id** (`string`) – the identifier of the iothread
        - **thread-id** (`int`) – ID of the underlying host thread
        - **poll-max-ns** (`int`) – maximum polling time in ns, 0 means polling is
          disabled (since 2.9)
        - **poll-grow** (`int`) – how many ns will be added to polling time, 0 means that
          it’s not configured (since 2.9)
        - **poll-shrink** (`int`) – how many ns will be removed from polling time, 0 means
          that it’s not configured (since 2.9)
        - **poll-weight** (`int`) – the weight factor for adaptive polling.
          Determines how much the current event interval contributes to
          the next polling time calculation. Valid values are 1 or
          greater (since 11.1)
        - **aio-max-batch** (`int`) – maximum number of requests in a batch for the AIO
          engine, 0 means that the engine will use its default (since 6.1)

*Command* query-iothreads (Since: 2.0)
:   Return a list of information about each iothread.

    > **Note:**
    >
    > This list excludes the QEMU main loop thread, which is not
    > declared using the `-object iothread` command-line option. It
    > is always the main thread of the process.

    Return:
    :   `[`[`IOThreadInfo`](qemu-qmp-ref.md#object-QMP-misc.IOThreadInfo "QMP:misc.IOThreadInfo")`]` – a list of info for each iothread

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "query-iothreads" }
    > <- { "return": [
    >          {
    >             "id":"iothread0",
    >             "thread-id":3134
    >          },
    >          {
    >             "id":"iothread1",
    >             "thread-id":3135
    >          }
    >       ]
    >    }
    > ```

*Command* stop (Since: 0.14)
:   Stop guest VM execution.

    > **Note:**
    >
    > This function will succeed even if the guest is already in
    > the stopped state. In “inmigrate” state, it will ensure that the
    > guest remains paused once migration finishes, as if the `-S`
    > option was passed on the command line.
    >
    > In the “suspended” state, it will completely stop the VM and
    > cause a transition to the “paused” state. (Since 9.0)

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "stop" }
    > <- { "return": {} }
    > ```

*Command* cont (Since: 0.14)
:   Resume guest VM execution.

    > **Note:**
    >
    > This command will succeed if the guest is currently
    > running. It will also succeed if the guest is in the “inmigrate”
    > state; in this case, the effect of the command is to make sure
    > the guest starts once migration finishes, removing the effect of
    > the `-S` command line option if it was passed.
    >
    > If the VM was previously suspended, and not been reset or woken,
    > this command will transition back to the “suspended” state.
    > (Since 9.0)

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "cont" }
    > <- { "return": {} }
    > ```

*Command* x-exit-preconfig (Since: 3.0)
:   This command is unstable/experimental.

    Exit from “preconfig” state

    This command makes QEMU exit the preconfig state and proceed with VM
    initialization using configuration data provided on the command line
    and via the QMP monitor during the preconfig state. The command is
    only available during the preconfig state (i.e. when the –preconfig
    command line option was in use).

    Features:
    :   - **unstable** – This command is experimental.

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "x-exit-preconfig" }
    > <- { "return": {} }
    > ```

*Command* human-monitor-command (Since: 0.14)
:   Execute a command on the human monitor and return the output.

    Arguments:
    :   - **command-line** (`string`) – the command to execute in the human monitor
        - **cpu-index** (`int`, *optional*) – The CPU to use for commands that require an implicit CPU

    Features:
    :   - **savevm-monitor-nodes** – If present, HMP command savevm only snapshots
          monitor-owned nodes if they have no parents. This allows the
          use of ‘savevm’ with -blockdev. (since 4.2)

    Return:
    :   `string` – the output of the command as a string

    > **Note:**
    >
    > This command only exists as a stop-gap. Its use is highly
    > discouraged. The semantics of this command are not guaranteed:
    > this means that command names, arguments and responses can change
    > or be removed at **any** time. Applications that rely on long
    > term stability guarantees should **not** use this command.
    >
    > Known limitations:
    >
    > - This command is stateless, this means that commands that depend
    >   on state information (such as [`getfd`](qemu-qmp-ref.md#command-QMP-misc.getfd "QMP:misc.getfd")) might not work.
    > - Commands that prompt the user for data don’t currently work.

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "human-monitor-command",
    >      "arguments": { "command-line": "info kvm" } }
    > <- { "return": "kvm support: enabled\r\n" }
    > ```

*Command* getfd (Since: 0.14)
:   *Availability*: `CONFIG_POSIX`

    Receive a file descriptor via SCM rights and assign it a name

    Arguments:
    :   - **fdname** (`string`) – file descriptor name

    > **Note:**
    >
    > If `fdname` already exists, the file descriptor assigned to
    > it will be closed and replaced by the received file descriptor.
    >
    > The [`closefd`](qemu-qmp-ref.md#command-QMP-misc.closefd "QMP:misc.closefd") command can be used to explicitly close the file
    > descriptor when it is no longer needed.

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "getfd", "arguments": { "fdname": "fd1" } }
    > <- { "return": {} }
    > ```

*Command* get-win32-socket (Since: 8.0)
:   *Availability*: `CONFIG_WIN32`

    Add a socket that was duplicated to QEMU process with
    WSADuplicateSocketW() via WSASocket() & WSAPROTOCOL_INFOW structure
    and assign it a name (the SOCKET is associated with a CRT file
    descriptor)

    Arguments:
    :   - **info** (`string`) – the WSAPROTOCOL_INFOW structure (encoded in base64)
        - **fdname** (`string`) – file descriptor name

    > **Note:**
    >
    > If `fdname` already exists, the file descriptor assigned to
    > it will be closed and replaced by the received file descriptor.
    >
    > The [`closefd`](qemu-qmp-ref.md#command-QMP-misc.closefd "QMP:misc.closefd") command can be used to explicitly close the file
    > descriptor when it is no longer needed.

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "get-win32-socket",
    >      "arguments": { "info": "abcd123..", "fdname": "skclient" } }
    > <- { "return": {} }
    > ```

*Command* closefd (Since: 0.14)
:   Close a file descriptor previously passed via SCM rights

    Arguments:
    :   - **fdname** (`string`) – file descriptor name

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "closefd", "arguments": { "fdname": "fd1" } }
    > <- { "return": {} }
    > ```

*Object* AddfdInfo (Since: 1.2)
:   Information about a file descriptor that was added to an fd set.

    Members:
    :   - **fdset-id** (`int`) – The ID of the fd set that `fd` was added to.
        - **fd** (`int`) – The file descriptor that was received via SCM rights and added
          to the fd set.

*Command* add-fd (Since: 1.2)
:   Add a file descriptor, that was passed via SCM rights, to an fd set.

    Arguments:
    :   - **fdset-id** (`int`, *optional*) – The ID of the fd set to add the file descriptor to.
        - **opaque** (`string`, *optional*) – A free-form string that can be used to describe the fd.

    Return:
    :   [`AddfdInfo`](qemu-qmp-ref.md#object-QMP-misc.AddfdInfo "QMP:misc.AddfdInfo")

    Errors:
    :   - If file descriptor was not received, GenericError
        - If `fdset-id` is a negative value, GenericError

    > **Note:**
    >
    > The list of fd sets is shared by all monitor connections.

    > **Note:**
    >
    > If `fdset-id` is not specified, a new fd set will be
    > created.

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "add-fd", "arguments": { "fdset-id": 1 } }
    > <- { "return": { "fdset-id": 1, "fd": 3 } }
    > ```

*Command* remove-fd (Since: 1.2)
:   Remove a file descriptor from an fd set.

    Arguments:
    :   - **fdset-id** (`int`) – The ID of the fd set that the file descriptor belongs to.
        - **fd** (`int`, *optional*) – The file descriptor that is to be removed.

    Errors:
    :   - If `fdset-id` or `fd` is not found, GenericError

    > **Note:**
    >
    > The list of fd sets is shared by all monitor connections.

    > **Note:**
    >
    > If `fd` is not specified, all file descriptors in `fdset-id`
    > will be removed.

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "remove-fd", "arguments": { "fdset-id": 1, "fd": 3 } }
    > <- { "return": {} }
    > ```

*Object* FdsetFdInfo (Since: 1.2)
:   Information about a file descriptor that belongs to an fd set.

    Members:
    :   - **fd** (`int`) – The file descriptor value.
        - **opaque** (`string`, *optional*) – A free-form string that can be used to describe the fd.

*Object* FdsetInfo (Since: 1.2)
:   Information about an fd set.

    Members:
    :   - **fdset-id** (`int`) – The ID of the fd set.
        - **fds** (`[`[`FdsetFdInfo`](qemu-qmp-ref.md#object-QMP-misc.FdsetFdInfo "QMP:misc.FdsetFdInfo")`]`) – A list of file descriptors that belong to this fd set.

*Command* query-fdsets (Since: 1.2)
:   Return information describing all fd sets.

    Return:
    :   `[`[`FdsetInfo`](qemu-qmp-ref.md#object-QMP-misc.FdsetInfo "QMP:misc.FdsetInfo")`]`

    > **Note:**
    >
    > The list of fd sets is shared by all monitor connections.

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "query-fdsets" }
    > <- { "return": [
    >        {
    >          "fds": [
    >            {
    >              "fd": 30,
    >              "opaque": "rdonly:/path/to/file"
    >            },
    >            {
    >              "fd": 24,
    >              "opaque": "rdwr:/path/to/file"
    >            }
    >          ],
    >          "fdset-id": 1
    >        },
    >        {
    >          "fds": [
    >            {
    >              "fd": 28
    >            },
    >            {
    >              "fd": 29
    >            }
    >          ],
    >          "fdset-id": 0
    >        }
    >      ]
    >    }
    > ```

*Enum* CommandLineParameterType (Since: 1.5)
:   Possible types for an option parameter.

    Values:
    :   - **string** – accepts a character string
        - **boolean** – accepts “on” or “off”
        - **number** – accepts a number
        - **size** – accepts a number followed by an optional suffix (K)ilo,
          (M)ega, (G)iga, (T)era

*Object* CommandLineParameterInfo (Since: 1.5)
:   Details about a single parameter of a command line option.

    Members:
    :   - **name** (`string`) – parameter name
        - **type** ([`CommandLineParameterType`](qemu-qmp-ref.md#enum-QMP-misc.CommandLineParameterType "QMP:misc.CommandLineParameterType")) – parameter [`CommandLineParameterType`](qemu-qmp-ref.md#enum-QMP-misc.CommandLineParameterType "QMP:misc.CommandLineParameterType")
        - **help** (`string`, *optional*) – human readable text string, not suitable for parsing.
        - **default** (`string`, *optional*) – default value string (since 2.1)

*Object* CommandLineOptionInfo (Since: 1.5)
:   Details about a command line option, including its list of parameter
    details

    Members:
    :   - **option** (`string`) – option name
        - **parameters** (`[`[`CommandLineParameterInfo`](qemu-qmp-ref.md#object-QMP-misc.CommandLineParameterInfo "QMP:misc.CommandLineParameterInfo")`]`) – an array of [`CommandLineParameterInfo`](qemu-qmp-ref.md#object-QMP-misc.CommandLineParameterInfo "QMP:misc.CommandLineParameterInfo")

*Command* query-command-line-options (Since: 1.5)
:   Query command line option schema.

    Arguments:
    :   - **option** (`string`, *optional*) – option name

    Return:
    :   `[`[`CommandLineOptionInfo`](qemu-qmp-ref.md#object-QMP-misc.CommandLineOptionInfo "QMP:misc.CommandLineOptionInfo")`]` – list of objects for all options (or for the given `option`).

    Errors:
    :   - if the given `option` doesn’t exist

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "query-command-line-options",
    >      "arguments": { "option": "option-rom" } }
    > <- { "return": [
    >         {
    >             "parameters": [
    >                 {
    >                     "name": "romfile",
    >                     "type": "string"
    >                 },
    >                 {
    >                     "name": "bootindex",
    >                     "type": "number"
    >                 }
    >             ],
    >             "option": "option-rom"
    >         }
    >      ]
    >    }
    > ```

*Event* RTC_CHANGE (Since: 0.13)
:   Emitted when the guest changes the RTC time.

    Members:
    :   - **offset** (`int`) – offset in seconds between base RTC clock (as specified by
          -rtc base), and new RTC clock value
        - **qom-path** (`string`) – path to the RTC object in the QOM tree

    > **Note:**
    >
    > This event is rate-limited. It is not guaranteed that the
    > RTC in the system implements this event, or even that the system
    > has an RTC at all.

    > **Example::**
    >
    > ```QMP
    > <- { "event": "RTC_CHANGE",
    >      "data": { "offset": 78 },
    >      "timestamp": { "seconds": 1267020223, "microseconds": 435656 } }
    > ```

*Event* VFU_CLIENT_HANGUP (Since: 7.1)
:   Emitted when the client of a TYPE_VFIO_USER_SERVER closes the
    communication channel

    Members:
    :   - **vfu-id** (`string`) – ID of the TYPE_VFIO_USER_SERVER object. It is the last
          component of `vfu-qom-path` referenced below
        - **vfu-qom-path** (`string`) – path to the TYPE_VFIO_USER_SERVER object in the QOM
          tree
        - **dev-id** (`string`) – ID of attached PCI device
        - **dev-qom-path** (`string`) – path to attached PCI device in the QOM tree

    > **Example::**
    >
    > ```QMP
    > <- { "event": "VFU_CLIENT_HANGUP",
    >      "data": { "vfu-id": "vfu1",
    >                "vfu-qom-path": "/objects/vfu1",
    >                "dev-id": "sas1",
    >                "dev-qom-path": "/machine/peripheral/sas1" },
    >      "timestamp": { "seconds": 1265044230, "microseconds": 450486 } }
    > ```

*Object* GICCapability (Since: 2.6)
:   The struct describes capability for a specific GIC (Generic
    Interrupt Controller) version. These bits are not only decided by
    QEMU/KVM software version, but also decided by the hardware that the
    program is running upon.

    Members:
    :   - **version** (`int`) – version of GIC to be described. Currently, only 2 and 3
          are supported.
        - **emulated** (`boolean`) – whether current QEMU/hardware supports emulated GIC
          device in user space.
        - **kernel** (`boolean`) – whether current QEMU/hardware supports hardware accelerated
          GIC device in kernel.

*Command* query-gic-capabilities (Since: 2.6)
:   It will return a list of [`GICCapability`](qemu-qmp-ref.md#object-QMP-misc-arm.GICCapability "QMP:misc-arm.GICCapability") objects that describe its
    capability bits.

    On non-ARM targets this command will report an error as the GIC
    technology is not applicable.

    Return:
    :   `[`[`GICCapability`](qemu-qmp-ref.md#object-QMP-misc-arm.GICCapability "QMP:misc-arm.GICCapability")`]`

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "query-gic-capabilities" }
    > <- { "return": [{ "version": 2, "emulated": true, "kernel": false },
    >                 { "version": 3, "emulated": false, "kernel": true } ] }
    > ```

*Enum* SsidSizeMode (Since: 11.0)
:   SMMUv3 SubstreamID size configuration mode.

    Values:
    :   - **auto** – derive from host IOMMU capabilities
        - **0** – Not documented
        - **1** – Not documented
        - **2** – Not documented
        - **3** – Not documented
        - **4** – Not documented
        - **5** – Not documented
        - **6** – Not documented
        - **7** – Not documented
        - **8** – Not documented
        - **9** – Not documented
        - **10** – Not documented
        - **11** – Not documented
        - **12** – Not documented
        - **13** – Not documented
        - **14** – Not documented
        - **15** – Not documented
        - **16** – Not documented
        - **17** – Not documented
        - **18** – Not documented
        - **19** – Not documented
        - **20** – Not documented

    Values 0-20: SSIDSIZE value in bits. 0 disables SubstreamID.

*Enum* OasMode (Since: 11.0)
:   SMMUv3 Output Address Size configuration mode.

    Values:
    :   - **auto** – derive from host IOMMU capabilities
        - **32** – 32-bit output address size
        - **36** – 36-bit output address size
        - **40** – 40-bit output address size
        - **42** – 42-bit output address size
        - **44** – 44-bit output address size
        - **48** – 48-bit output address size
        - **52** – 52-bit output address size
        - **56** – 56-bit output address size

*Command* rtc-reset-reinjection (Since: 2.1)
:   Reset the RTC interrupt reinjection backlog. Can be used if another
    mechanism to synchronize guest time is in effect, for example QEMU
    guest agent’s [`guest-set-time`](qemu-ga-ref.md#command-QGA-qapi-schema.guest-set-time "QGA:qapi-schema.guest-set-time") command.

    Use of this command is only applicable for x86 machines with an RTC,
    and on other machines will silently return without performing any
    action.

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "rtc-reset-reinjection" }
    > <- { "return": {} }
    > ```

*Enum* SevState (Since: 2.12)
:   An enumeration of SEV state information used during [`query-sev`](qemu-qmp-ref.md#command-QMP-misc-i386.query-sev "QMP:misc-i386.query-sev").

    Values:
    :   - **uninit** – The guest is uninitialized.
        - **launch-update** – The guest is currently being launched; plaintext
          data and register state is being imported.
        - **launch-secret** – The guest is currently being launched; ciphertext
          data is being imported.
        - **running** – The guest is fully launched or migrated in.
        - **send-update** – The guest is currently being migrated out to another
          machine.
        - **receive-update** – The guest is currently being migrated from another
          machine.

*Enum* SevGuestType (Since: 6.2)
:   An enumeration indicating the type of SEV guest being run.

    Values:
    :   - **sev** – The guest is a legacy SEV or SEV-ES guest.
        - **sev-snp** – The guest is an SEV-SNP guest.

*Object* SevGuestInfo (Since: 2.12)
:   Information specific to legacy SEV/SEV-ES guests.

    Members:
    :   - **policy** (`int`) – SEV policy value
        - **handle** (`int`) – SEV firmware handle

*Object* SevSnpGuestInfo (Since: 9.1)
:   Information specific to SEV-SNP guests.

    Members:
    :   - **snp-policy** (`int`) – SEV-SNP policy value

*Object* SevInfo (Since: 2.12)
:   Information about Secure Encrypted Virtualization (SEV) support

    Members:
    :   - **enabled** (`boolean`) – true if SEV is active
        - **api-major** (`int`) – SEV API major version
        - **api-minor** (`int`) – SEV API minor version
        - **build-id** (`int`) – SEV FW build id
        - **state** ([`SevState`](qemu-qmp-ref.md#enum-QMP-misc-i386.SevState "QMP:misc-i386.SevState")) – SEV guest state
        - **sev-type** ([`SevGuestType`](qemu-qmp-ref.md#enum-QMP-misc-i386.SevGuestType "QMP:misc-i386.SevGuestType")) – Type of SEV guest being run
        - When `sev-type` is `sev`: The members of [`SevGuestInfo`](qemu-qmp-ref.md#object-QMP-misc-i386.SevGuestInfo "QMP:misc-i386.SevGuestInfo").
        - When `sev-type` is `sev-snp`: The members of [`SevSnpGuestInfo`](qemu-qmp-ref.md#object-QMP-misc-i386.SevSnpGuestInfo "QMP:misc-i386.SevSnpGuestInfo").

*Command* query-sev (Since: 2.12)
:   Return information about SEV/SEV-ES/SEV-SNP.

    If unavailable due to an incompatible configuration the returned
    `enabled` field is set to ‘false’ and the state of all other fields
    is unspecified.

    Return:
    :   [`SevInfo`](qemu-qmp-ref.md#object-QMP-misc-i386.SevInfo "QMP:misc-i386.SevInfo")

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "query-sev" }
    > <- { "return": { "enabled": true, "api-major" : 0, "api-minor" : 0,
    >                  "build-id" : 0, "policy" : 0, "state" : "running",
    >                  "handle" : 1 } }
    > ```

*Object* SevLaunchMeasureInfo (Since: 2.12)
:   SEV Guest Launch measurement information

    Members:
    :   - **data** (`string`) – the measurement value encoded in base64

*Command* query-sev-launch-measure (Since: 2.12)
:   Query the SEV/SEV-ES guest launch information.

    This is only valid on x86 machines configured with KVM and the
    ‘sev-guest’ confidential virtualization object. The launch
    measurement for SEV-SNP guests is only available within the guest.

    Return:
    :   [`SevLaunchMeasureInfo`](qemu-qmp-ref.md#object-QMP-misc-i386.SevLaunchMeasureInfo "QMP:misc-i386.SevLaunchMeasureInfo") – The guest’s SEV guest launch measurement info

    Errors:
    :   - If the launch measurement is unavailable, either due to an
          invalid guest configuration or if the guest has not reached
          the required SEV state, GenericError

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "query-sev-launch-measure" }
    > <- { "return": { "data": "4l8LXeNlSPUDlXPJG5966/8%YZ" } }
    > ```

*Object* SevCapability (Since: 2.12)
:   The struct describes capability for a Secure Encrypted
    Virtualization feature.

    Members:
    :   - **pdh** (`string`) – Platform Diffie-Hellman key (base64 encoded)
        - **cert-chain** (`string`) – PDH certificate chain (base64 encoded)
        - **cpu0-id** (`string`) – Unique ID of CPU0 (base64 encoded) (since 7.1)
        - **cbitpos** (`int`) – C-bit location in page table entry
        - **reduced-phys-bits** (`int`) – Number of physical address bit reduction when
          SEV is enabled

*Command* query-sev-capabilities (Since: 2.12)
:   Get SEV capabilities.

    This is only supported on AMD X86 platforms with KVM enabled.

    Return:
    :   [`SevCapability`](qemu-qmp-ref.md#object-QMP-misc-i386.SevCapability "QMP:misc-i386.SevCapability")

    Errors:
    :   - If SEV is not available on the platform, GenericError

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "query-sev-capabilities" }
    > <- { "return": { "pdh": "8CCDD8DDD", "cert-chain": "888CCCDDDEE",
    >                  "cpu0-id": "2lvmGwo+...61iEinw==",
    >                  "cbitpos": 47, "reduced-phys-bits": 1}}
    > ```

*Command* sev-inject-launch-secret (Since: 6.0)
:   Inject a secret blob into a SEV/SEV-ES guest’s memory.

    This is only valid on x86 machines configured with KVM and the
    ‘sev-guest’ confidential virtualization object. SEV-SNP guests do
    not support launch secret injection.

    Arguments:
    :   - **packet-header** (`string`) – the launch secret packet header encoded in base64
        - **secret** (`string`) – the launch secret data to be injected encoded in base64
        - **gpa** (`int`, *optional*) – the guest physical address where secret will be injected.

    Errors:
    :   - If launch secret injection is not possible, either due to
          an invalid guest configuration, or if the guest has not
          reached the required SEV state, GenericError

*Object* SevAttestationReport (Since: 6.1)
:   The struct describes attestation report for a Secure Encrypted
    Virtualization feature.

    Members:
    :   - **data** (`string`) – guest attestation report (base64 encoded)

*Command* query-sev-attestation-report (Since: 6.1)
:   Get the SEV attestation report.

    This is only valid on x86 machines configured with KVM and the
    ‘sev-guest’ confidential virtualization object. The attestation
    report for SEV-SNP guests is only available within the guest.

    Arguments:
    :   - **mnonce** (`string`) – a random 16 bytes value encoded in base64 (it will be
          included in report)

    Return:
    :   [`SevAttestationReport`](qemu-qmp-ref.md#object-QMP-misc-i386.SevAttestationReport "QMP:misc-i386.SevAttestationReport")

    Errors:
    :   - If the attestation report is unavailable, either due to an
          invalid guest configuration or because the guest has not
          reached the required SEV state, GenericError

    > **Example::**
    >
    > ```QMP
    > -> { "execute" : "query-sev-attestation-report",
    >                  "arguments": { "mnonce": "aaaaaaa" } }
    > <- { "return" : { "data": "aaaaaaaabbbddddd"} }
    > ```

*Object* SgxEpcSection (Since: 7.0)
:   Information about intel SGX EPC section

    Members:
    :   - **node** (`int`) – the numa node
        - **size** (`int`) – the size of EPC section

*Object* SgxInfo (Since: 6.2)
:   Information about intel Safe Guard eXtension (SGX) support

    Members:
    :   - **sgx** (`boolean`) – true if SGX is supported
        - **sgx1** (`boolean`) – true if SGX1 is supported
        - **sgx2** (`boolean`) – true if SGX2 is supported
        - **flc** (`boolean`) – true if FLC is supported
        - **sections** (`[`[`SgxEpcSection`](qemu-qmp-ref.md#object-QMP-misc-i386.SgxEpcSection "QMP:misc-i386.SgxEpcSection")`]`) – The EPC sections information (Since: 7.0)

*Command* query-sgx (Since: 6.2)
:   Return information about configured SGX capabilities of guest

    Return:
    :   [`SgxInfo`](qemu-qmp-ref.md#object-QMP-misc-i386.SgxInfo "QMP:misc-i386.SgxInfo")

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "query-sgx" }
    > <- { "return": { "sgx": true, "sgx1" : true, "sgx2" : true,
    >                  "flc": true,
    >                  "sections": [{"node": 0, "size": 67108864},
    >                  {"node": 1, "size": 29360128}]} }
    > ```

*Command* query-sgx-capabilities (Since: 6.2)
:   Return information about SGX capabilities of host

    Return:
    :   [`SgxInfo`](qemu-qmp-ref.md#object-QMP-misc-i386.SgxInfo "QMP:misc-i386.SgxInfo")

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "query-sgx-capabilities" }
    > <- { "return": { "sgx": true, "sgx1" : true, "sgx2" : true,
    >                  "flc": true,
    >                  "section" : [{"node": 0, "size": 67108864},
    >                  {"node": 1, "size": 29360128}]} }
    > ```

*Enum* EvtchnPortType (Since: 8.0)
:   An enumeration of Xen event channel port types.

    Values:
    :   - **closed** – The port is unused.
        - **unbound** – The port is allocated and ready to be bound.
        - **interdomain** – The port is connected as an interdomain interrupt.
        - **pirq** – The port is bound to a physical IRQ (PIRQ).
        - **virq** – The port is bound to a virtual IRQ (VIRQ).
        - **ipi** – The post is an inter-processor interrupt (IPI).

*Object* EvtchnInfo (Since: 8.0)
:   Information about a Xen event channel port

    Members:
    :   - **port** (`int`) – the port number
        - **vcpu** (`int`) – target vCPU for this port
        - **type** ([`EvtchnPortType`](qemu-qmp-ref.md#enum-QMP-misc-i386.EvtchnPortType "QMP:misc-i386.EvtchnPortType")) – the port type
        - **remote-domain** (`string`) – remote domain for interdomain ports
        - **target** (`int`) – remote port ID, or virq/pirq number
        - **pending** (`boolean`) – port is currently active pending delivery
        - **masked** (`boolean`) – port is masked

*Command* xen-event-list (Since: 8.0)
:   Query the Xen event channels opened by the guest.

    Return:
    :   `[`[`EvtchnInfo`](qemu-qmp-ref.md#object-QMP-misc-i386.EvtchnInfo "QMP:misc-i386.EvtchnInfo")`]` – list of open event channel ports.

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "xen-event-list" }
    > <- { "return": [
    >         {
    >             "pending": false,
    >             "port": 1,
    >             "vcpu": 1,
    >             "remote-domain": "qemu",
    >             "masked": false,
    >             "type": "interdomain",
    >             "target": 1
    >         },
    >         {
    >             "pending": false,
    >             "port": 2,
    >             "vcpu": 0,
    >             "remote-domain": "",
    >             "masked": false,
    >             "type": "virq",
    >             "target": 0
    >         }
    >      ]
    >    }
    > ```

*Command* xen-event-inject (Since: 8.0)
:   Inject a Xen event channel port (interrupt) to the guest.

    Arguments:
    :   - **port** (`int`) – The port number

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "xen-event-inject", "arguments": { "port": 1 } }
    > <- { "return": { } }
    > ```

## [Audio](qemu-qmp-ref.md#id38)

*Object* AudiodevPerDirectionOptions (Since: 4.0)
:   General audio backend options that are used for both playback and
    recording.

    Members:
    :   - **mixing-engine** (`boolean`, *optional*) – use QEMU’s mixing engine to mix all streams inside
          QEMU and convert audio formats when not supported by the
          backend. When set to off, fixed-settings must be also off
          (default on, since 4.2)
        - **fixed-settings** (`boolean`, *optional*) – use fixed settings for host input/output. When
          off, frequency, channels and format must not be specified
          (default true)
        - **frequency** (`int`, *optional*) – frequency to use when using fixed settings (default
          44100)
        - **channels** (`int`, *optional*) – number of channels when using fixed settings (default 2)
        - **voices** (`int`, *optional*) – number of voices to use (default 1)
        - **format** ([`AudioFormat`](qemu-qmp-ref.md#enum-QMP-audio.AudioFormat "QMP:audio.AudioFormat"), *optional*) – sample format to use when using fixed settings (default
          s16)
        - **buffer-length** (`int`, *optional*) – the buffer length in microseconds

*Object* AudiodevGenericOptions (Since: 4.0)
:   Generic driver-specific options.

    Members:
    :   - **in** ([`AudiodevPerDirectionOptions`](qemu-qmp-ref.md#object-QMP-audio.AudiodevPerDirectionOptions "QMP:audio.AudiodevPerDirectionOptions"), *optional*) – options of the capture stream
        - **out** ([`AudiodevPerDirectionOptions`](qemu-qmp-ref.md#object-QMP-audio.AudiodevPerDirectionOptions "QMP:audio.AudiodevPerDirectionOptions"), *optional*) – options of the playback stream

*Object* AudiodevDBusOptions (Since: 10.0)
:   Options of the D-Bus audio backend.

    Members:
    :   - **in** ([`AudiodevPerDirectionOptions`](qemu-qmp-ref.md#object-QMP-audio.AudiodevPerDirectionOptions "QMP:audio.AudiodevPerDirectionOptions"), *optional*) – options of the capture stream
        - **out** ([`AudiodevPerDirectionOptions`](qemu-qmp-ref.md#object-QMP-audio.AudiodevPerDirectionOptions "QMP:audio.AudiodevPerDirectionOptions"), *optional*) – options of the playback stream
        - **nsamples** (`int`, *optional*) – set the number of samples per read/write calls
          (default to 480, 10ms at 48kHz).

*Object* AudiodevAlsaPerDirectionOptions (Since: 4.0)
:   Options of the ALSA backend that are used for both playback and
    recording.

    Members:
    :   - **dev** (`string`, *optional*) – the name of the ALSA device to use (default ‘default’)
        - **period-length** (`int`, *optional*) – the period length in microseconds
        - **try-poll** (`boolean`, *optional*) – attempt to use poll mode, falling back to non-polling
          access on failure (default false)
        - The members of [`AudiodevPerDirectionOptions`](qemu-qmp-ref.md#object-QMP-audio.AudiodevPerDirectionOptions "QMP:audio.AudiodevPerDirectionOptions").

*Object* AudiodevAlsaOptions (Since: 4.0)
:   Options of the ALSA audio backend.

    Members:
    :   - **in** ([`AudiodevAlsaPerDirectionOptions`](qemu-qmp-ref.md#object-QMP-audio.AudiodevAlsaPerDirectionOptions "QMP:audio.AudiodevAlsaPerDirectionOptions"), *optional*) – options of the capture stream
        - **out** ([`AudiodevAlsaPerDirectionOptions`](qemu-qmp-ref.md#object-QMP-audio.AudiodevAlsaPerDirectionOptions "QMP:audio.AudiodevAlsaPerDirectionOptions"), *optional*) – options of the playback stream
        - **threshold** (`int`, *optional*) – set the threshold (in microseconds) when playback starts

*Object* AudiodevSndioOptions (Since: 7.2)
:   Options of the sndio audio backend.

    Members:
    :   - **in** ([`AudiodevPerDirectionOptions`](qemu-qmp-ref.md#object-QMP-audio.AudiodevPerDirectionOptions "QMP:audio.AudiodevPerDirectionOptions"), *optional*) – options of the capture stream
        - **out** ([`AudiodevPerDirectionOptions`](qemu-qmp-ref.md#object-QMP-audio.AudiodevPerDirectionOptions "QMP:audio.AudiodevPerDirectionOptions"), *optional*) – options of the playback stream
        - **dev** (`string`, *optional*) – the name of the sndio device to use (default ‘default’)
        - **latency** (`int`, *optional*) – play buffer size (in microseconds)

*Object* AudiodevCoreaudioPerDirectionOptions (Since: 4.0)
:   Options of the Core Audio backend that are used for both playback
    and recording.

    Members:
    :   - **buffer-count** (`int`, *optional*) – number of buffers
        - The members of [`AudiodevPerDirectionOptions`](qemu-qmp-ref.md#object-QMP-audio.AudiodevPerDirectionOptions "QMP:audio.AudiodevPerDirectionOptions").

*Object* AudiodevCoreaudioOptions (Since: 4.0)
:   Options of the coreaudio audio backend.

    Members:
    :   - **in** ([`AudiodevCoreaudioPerDirectionOptions`](qemu-qmp-ref.md#object-QMP-audio.AudiodevCoreaudioPerDirectionOptions "QMP:audio.AudiodevCoreaudioPerDirectionOptions"), *optional*) – options of the capture stream
        - **out** ([`AudiodevCoreaudioPerDirectionOptions`](qemu-qmp-ref.md#object-QMP-audio.AudiodevCoreaudioPerDirectionOptions "QMP:audio.AudiodevCoreaudioPerDirectionOptions"), *optional*) – options of the playback stream

*Object* AudiodevDsoundOptions (Since: 4.0)
:   Options of the DirectSound audio backend.

    Members:
    :   - **in** ([`AudiodevPerDirectionOptions`](qemu-qmp-ref.md#object-QMP-audio.AudiodevPerDirectionOptions "QMP:audio.AudiodevPerDirectionOptions"), *optional*) – options of the capture stream
        - **out** ([`AudiodevPerDirectionOptions`](qemu-qmp-ref.md#object-QMP-audio.AudiodevPerDirectionOptions "QMP:audio.AudiodevPerDirectionOptions"), *optional*) – options of the playback stream
        - **latency** (`int`, *optional*) – add extra latency to playback in microseconds (default
          10000)

*Object* AudiodevJackPerDirectionOptions (Since: 5.1)
:   Options of the JACK backend that are used for both playback and
    recording.

    Members:
    :   - **server-name** (`string`, *optional*) – select from among several possible concurrent server
          instances (default: environment variable $JACK_DEFAULT_SERVER if
          set, else “default”)
        - **client-name** (`string`, *optional*) – the client name to use. The server will modify this
          name to create a unique variant, if needed unless `exact-name` is
          true (default: the guest’s name)
        - **connect-ports** (`string`, *optional*) – if set, a regular expression of JACK client port
          name(s) to monitor for and automatically connect to
        - **start-server** (`boolean`, *optional*) – start a jack server process if one is not already
          present (default: false)
        - **exact-name** (`boolean`, *optional*) – use the exact name requested otherwise JACK
          automatically generates a unique one, if needed (default: false)
        - The members of [`AudiodevPerDirectionOptions`](qemu-qmp-ref.md#object-QMP-audio.AudiodevPerDirectionOptions "QMP:audio.AudiodevPerDirectionOptions").

*Object* AudiodevJackOptions (Since: 5.1)
:   Options of the JACK audio backend.

    Members:
    :   - **in** ([`AudiodevJackPerDirectionOptions`](qemu-qmp-ref.md#object-QMP-audio.AudiodevJackPerDirectionOptions "QMP:audio.AudiodevJackPerDirectionOptions"), *optional*) – options of the capture stream
        - **out** ([`AudiodevJackPerDirectionOptions`](qemu-qmp-ref.md#object-QMP-audio.AudiodevJackPerDirectionOptions "QMP:audio.AudiodevJackPerDirectionOptions"), *optional*) – options of the playback stream

*Object* AudiodevOssPerDirectionOptions (Since: 4.0)
:   Options of the OSS backend that are used for both playback and
    recording.

    Members:
    :   - **dev** (`string`, *optional*) – file name of the OSS device (default ‘/dev/dsp’)
        - **buffer-count** (`int`, *optional*) – number of buffers
        - **try-poll** (`boolean`, *optional*) – attempt to use poll mode, falling back to non-polling
          access on failure (default true)
        - The members of [`AudiodevPerDirectionOptions`](qemu-qmp-ref.md#object-QMP-audio.AudiodevPerDirectionOptions "QMP:audio.AudiodevPerDirectionOptions").

*Object* AudiodevOssOptions (Since: 4.0)
:   Options of the OSS audio backend.

    Members:
    :   - **in** ([`AudiodevOssPerDirectionOptions`](qemu-qmp-ref.md#object-QMP-audio.AudiodevOssPerDirectionOptions "QMP:audio.AudiodevOssPerDirectionOptions"), *optional*) – options of the capture stream
        - **out** ([`AudiodevOssPerDirectionOptions`](qemu-qmp-ref.md#object-QMP-audio.AudiodevOssPerDirectionOptions "QMP:audio.AudiodevOssPerDirectionOptions"), *optional*) – options of the playback stream
        - **try-mmap** (`boolean`, *optional*) – try using memory-mapped access, falling back to
          non-memory-mapped access on failure (default true)
        - **exclusive** (`boolean`, *optional*) – open device in exclusive mode (vmix won’t work) (default
          false)
        - **dsp-policy** (`int`, *optional*) – set the timing policy of the device (between 0 and 10,
          where smaller number means smaller latency but higher CPU usage)
          or -1 to use fragment mode (option ignored on some platforms)
          (default 5)

*Object* AudiodevPaPerDirectionOptions (Since: 4.0)
:   Options of the Pulseaudio backend that are used for both playback
    and recording.

    Members:
    :   - **name** (`string`, *optional*) – name of the sink/source to use
        - **stream-name** (`string`, *optional*) – name of the PulseAudio stream created by QEMU. Can be
          used to identify the stream in PulseAudio when you create
          multiple PulseAudio devices or run multiple QEMU instances
          (default: audiodev’s id, since 4.2)
        - **latency** (`int`, *optional*) – latency you want PulseAudio to achieve in microseconds
          (default 15000)
        - The members of [`AudiodevPerDirectionOptions`](qemu-qmp-ref.md#object-QMP-audio.AudiodevPerDirectionOptions "QMP:audio.AudiodevPerDirectionOptions").

*Object* AudiodevPaOptions (Since: 4.0)
:   Options of the PulseAudio audio backend.

    Members:
    :   - **in** ([`AudiodevPaPerDirectionOptions`](qemu-qmp-ref.md#object-QMP-audio.AudiodevPaPerDirectionOptions "QMP:audio.AudiodevPaPerDirectionOptions"), *optional*) – options of the capture stream
        - **out** ([`AudiodevPaPerDirectionOptions`](qemu-qmp-ref.md#object-QMP-audio.AudiodevPaPerDirectionOptions "QMP:audio.AudiodevPaPerDirectionOptions"), *optional*) – options of the playback stream
        - **server** (`string`, *optional*) – PulseAudio server address (default: let PulseAudio choose)

*Object* AudiodevPipewirePerDirectionOptions (Since: 8.1)
:   Options of the PipeWire backend that are used for both playback and
    recording.

    Members:
    :   - **name** (`string`, *optional*) – name of the sink/source to use
        - **stream-name** (`string`, *optional*) – name of the PipeWire stream created by QEMU. Can be
          used to identify the stream in PipeWire when you create multiple
          PipeWire devices or run multiple QEMU instances (default:
          audiodev’s id)
        - **latency** (`int`, *optional*) – latency you want PipeWire to achieve in microseconds
          (default 46000)
        - The members of [`AudiodevPerDirectionOptions`](qemu-qmp-ref.md#object-QMP-audio.AudiodevPerDirectionOptions "QMP:audio.AudiodevPerDirectionOptions").

*Object* AudiodevPipewireOptions (Since: 8.1)
:   Options of the PipeWire audio backend.

    Members:
    :   - **in** ([`AudiodevPipewirePerDirectionOptions`](qemu-qmp-ref.md#object-QMP-audio.AudiodevPipewirePerDirectionOptions "QMP:audio.AudiodevPipewirePerDirectionOptions"), *optional*) – options of the capture stream
        - **out** ([`AudiodevPipewirePerDirectionOptions`](qemu-qmp-ref.md#object-QMP-audio.AudiodevPipewirePerDirectionOptions "QMP:audio.AudiodevPipewirePerDirectionOptions"), *optional*) – options of the playback stream

*Object* AudiodevSdlPerDirectionOptions (Since: 6.0)
:   Options of the SDL audio backend that are used for both playback and
    recording.

    Members:
    :   - **buffer-count** (`int`, *optional*) – number of buffers (default 4)
        - The members of [`AudiodevPerDirectionOptions`](qemu-qmp-ref.md#object-QMP-audio.AudiodevPerDirectionOptions "QMP:audio.AudiodevPerDirectionOptions").

*Object* AudiodevSdlOptions (Since: 6.0)
:   Options of the SDL audio backend.

    Members:
    :   - **in** ([`AudiodevSdlPerDirectionOptions`](qemu-qmp-ref.md#object-QMP-audio.AudiodevSdlPerDirectionOptions "QMP:audio.AudiodevSdlPerDirectionOptions"), *optional*) – options of the recording stream
        - **out** ([`AudiodevSdlPerDirectionOptions`](qemu-qmp-ref.md#object-QMP-audio.AudiodevSdlPerDirectionOptions "QMP:audio.AudiodevSdlPerDirectionOptions"), *optional*) – options of the playback stream

*Object* AudiodevWavOptions (Since: 4.0)
:   Options of the wav audio backend.

    Members:
    :   - **in** ([`AudiodevPerDirectionOptions`](qemu-qmp-ref.md#object-QMP-audio.AudiodevPerDirectionOptions "QMP:audio.AudiodevPerDirectionOptions"), *optional*) – options of the capture stream
        - **out** ([`AudiodevPerDirectionOptions`](qemu-qmp-ref.md#object-QMP-audio.AudiodevPerDirectionOptions "QMP:audio.AudiodevPerDirectionOptions"), *optional*) – options of the playback stream
        - **path** (`string`, *optional*) – name of the wav file to record (default ‘qemu.wav’)

*Enum* AudioFormat (Since: 4.0)
:   An enumeration of possible audio formats.

    Values:
    :   - **u8** – unsigned 8 bit integer
        - **s8** – signed 8 bit integer
        - **u16** – unsigned 16 bit integer
        - **s16** – signed 16 bit integer
        - **u32** – unsigned 32 bit integer
        - **s32** – signed 32 bit integer
        - **f32** – single precision floating-point (since 5.0)

*Enum* AudiodevDriver (Since: 4.0)
:   An enumeration of possible audio backend drivers.

    Values:
    :   - **jack** – JACK audio backend (since 5.1)
        - **none** – Not documented
        - **alsa** – Not documented
        - **coreaudio** – Not documented
        - **dbus** – Not documented
        - **dsound** – Not documented
        - **oss** – Not documented
        - **pa** – Not documented
        - **pipewire** – Not documented
        - **sdl** – Not documented
        - **sndio** – Not documented
        - **spice** – Not documented
        - **wav** – Not documented

*Object* Audiodev (Since: 4.0)
:   Options of an audio backend.

    Members:
    :   - **id** (`string`) – identifier of the backend
        - **driver** ([`AudiodevDriver`](qemu-qmp-ref.md#enum-QMP-audio.AudiodevDriver "QMP:audio.AudiodevDriver")) – the backend driver to use
        - **timer-period** (`int`, *optional*) – timer period (in microseconds, 0: use lowest
          possible)
        - When `driver` is `none`: The members of [`AudiodevGenericOptions`](qemu-qmp-ref.md#object-QMP-audio.AudiodevGenericOptions "QMP:audio.AudiodevGenericOptions").
        - When `driver` is `alsa`: The members of [`AudiodevAlsaOptions`](qemu-qmp-ref.md#object-QMP-audio.AudiodevAlsaOptions "QMP:audio.AudiodevAlsaOptions").
        - When `driver` is `coreaudio`: The members of [`AudiodevCoreaudioOptions`](qemu-qmp-ref.md#object-QMP-audio.AudiodevCoreaudioOptions "QMP:audio.AudiodevCoreaudioOptions").
        - When `driver` is `dbus`: The members of [`AudiodevDBusOptions`](qemu-qmp-ref.md#object-QMP-audio.AudiodevDBusOptions "QMP:audio.AudiodevDBusOptions").
        - When `driver` is `dsound`: The members of [`AudiodevDsoundOptions`](qemu-qmp-ref.md#object-QMP-audio.AudiodevDsoundOptions "QMP:audio.AudiodevDsoundOptions").
        - When `driver` is `jack`: The members of [`AudiodevJackOptions`](qemu-qmp-ref.md#object-QMP-audio.AudiodevJackOptions "QMP:audio.AudiodevJackOptions").
        - When `driver` is `oss`: The members of [`AudiodevOssOptions`](qemu-qmp-ref.md#object-QMP-audio.AudiodevOssOptions "QMP:audio.AudiodevOssOptions").
        - When `driver` is `pa`: The members of [`AudiodevPaOptions`](qemu-qmp-ref.md#object-QMP-audio.AudiodevPaOptions "QMP:audio.AudiodevPaOptions").
        - When `driver` is `pipewire`: The members of [`AudiodevPipewireOptions`](qemu-qmp-ref.md#object-QMP-audio.AudiodevPipewireOptions "QMP:audio.AudiodevPipewireOptions").
        - When `driver` is `sdl`: The members of [`AudiodevSdlOptions`](qemu-qmp-ref.md#object-QMP-audio.AudiodevSdlOptions "QMP:audio.AudiodevSdlOptions").
        - When `driver` is `sndio`: The members of [`AudiodevSndioOptions`](qemu-qmp-ref.md#object-QMP-audio.AudiodevSndioOptions "QMP:audio.AudiodevSndioOptions").
        - When `driver` is `spice`: The members of [`AudiodevGenericOptions`](qemu-qmp-ref.md#object-QMP-audio.AudiodevGenericOptions "QMP:audio.AudiodevGenericOptions").
        - When `driver` is `wav`: The members of [`AudiodevWavOptions`](qemu-qmp-ref.md#object-QMP-audio.AudiodevWavOptions "QMP:audio.AudiodevWavOptions").

*Command* query-audiodevs (Since: 8.0)
:   Return information about audiodev configuration

    Return:
    :   `[`[`Audiodev`](qemu-qmp-ref.md#object-QMP-audio.Audiodev "QMP:audio.Audiodev")`]`

## [ACPI](qemu-qmp-ref.md#id39)

*Object* AcpiTableOptions (Since: 1.5)
:   Specify an ACPI table on the command line to load.

    At most one of `file` and `data` can be specified. The list of files
    specified by any one of them is loaded and concatenated in order.
    If both are omitted, `data` is implied.

    Other fields / optargs can be used to override fields of the generic
    ACPI table header; refer to the ACPI specification 5.0, section
    5.2.6 System Description Table Header. If a header field is not
    overridden, then the corresponding value from the concatenated blob
    is used (in case of `file`), or it is filled in with a hard-coded
    value (in case of `data`).

    String fields are copied into the matching ACPI member from lowest
    address upwards, and silently truncated / NUL-padded to length.

    Members:
    :   - **sig** (`string`, *optional*) – table signature / identifier (4 bytes)
        - **rev** (`int`, *optional*) – table revision number (dependent on signature, 1 byte)
        - **oem_id** (`string`, *optional*) – OEM identifier (6 bytes)
        - **oem_table_id** (`string`, *optional*) – OEM table identifier (8 bytes)
        - **oem_rev** (`int`, *optional*) – OEM-supplied revision number (4 bytes)
        - **asl_compiler_id** (`string`, *optional*) – identifier of the utility that created the table
          (4 bytes)
        - **asl_compiler_rev** (`int`, *optional*) – revision number of the utility that created the
          table (4 bytes)
        - **file** (`string`, *optional*) – colon (:) separated list of pathnames to load and concatenate
          as table data. The resultant binary blob is expected to have an
          ACPI table header. At least one file is required. This field
          excludes `data`.
        - **data** (`string`, *optional*) – colon (:) separated list of pathnames to load and concatenate
          as table data. The resultant binary blob must not have an ACPI
          table header. At least one file is required. This field
          excludes `file`.

*Enum* ACPISlotType
:   Values:
    :   - **DIMM** – memory slot
        - **CPU** – logical CPU slot (since 2.7)

*Object* ACPIOSTInfo (Since: 2.1)
:   OSPM Status Indication for a device. For description of possible
    values of `source` and `status` fields see “_OST (OSPM Status
    Indication)” chapter of ACPI5.0 spec.

    Members:
    :   - **device** (`string`, *optional*) – device ID associated with slot
        - **slot** (`string`) – slot ID, unique per slot of a given `slot-type`
        - **slot-type** ([`ACPISlotType`](qemu-qmp-ref.md#enum-QMP-acpi.ACPISlotType "QMP:acpi.ACPISlotType")) – type of the slot
        - **source** (`int`) – an integer containing the source event
        - **status** (`int`) – an integer containing the status code

*Command* query-acpi-ospm-status (Since: 2.1)
:   Return a list of [`ACPIOSTInfo`](qemu-qmp-ref.md#object-QMP-acpi.ACPIOSTInfo "QMP:acpi.ACPIOSTInfo") for devices that support status
    reporting via ACPI _OST method.

    Return:
    :   `[`[`ACPIOSTInfo`](qemu-qmp-ref.md#object-QMP-acpi.ACPIOSTInfo "QMP:acpi.ACPIOSTInfo")`]`

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "query-acpi-ospm-status" }
    > <- { "return": [ { "device": "d1", "slot": "0", "slot-type": "DIMM", "source": 1, "status": 0},
    >                  { "slot": "1", "slot-type": "DIMM", "source": 0, "status": 0},
    >                  { "slot": "2", "slot-type": "DIMM", "source": 0, "status": 0},
    >                  { "slot": "3", "slot-type": "DIMM", "source": 0, "status": 0}
    >    ]}
    > ```

*Event* ACPI_DEVICE_OST (Since: 2.1)
:   Emitted when guest executes ACPI _OST method.

    Members:
    :   - **info** ([`ACPIOSTInfo`](qemu-qmp-ref.md#object-QMP-acpi.ACPIOSTInfo "QMP:acpi.ACPIOSTInfo")) – OSPM Status Indication

    > **Example::**
    >
    > ```QMP
    > <- { "event": "ACPI_DEVICE_OST",
    >      "data": { "info": { "device": "d1", "slot": "0",
    >                          "slot-type": "DIMM", "source": 1, "status": 0 } },
    >      "timestamp": { "seconds": 1265044230, "microseconds": 450486 } }
    > ```

== GHESv2 CPER Error Injection

Defined since ACPI Specification 6.1, section 18.3.2.8 Generic
Hardware Error Source version 2. See:

<https://uefi.org/sites/default/files/resources/ACPI_6_1.pdf>

*Command* inject-ghes-v2-error (Since: 10.2)
:   This command is unstable/experimental.

    Inject an error with additional ACPI 6.1 GHESv2 error information

    Arguments:
    :   - **cper** (`string`) – contains a base64 encoded string with raw data for a single
          CPER record with Generic Error Status Block, Generic Error Data
          Entry and generic error data payload, as described at
          <https://uefi.org/specs/UEFI/2.10/Apx_N_Common_Platform_Error_Record.html#format>

    Features:
    :   - **unstable** – This command is experimental.

## [PCI](qemu-qmp-ref.md#id40)

*Object* PciMemoryRange (Since: 0.14)
:   A PCI device memory region

    Members:
    :   - **base** (`int`) – the starting address (guest physical)
        - **limit** (`int`) – the ending address (guest physical)

*Object* PciMemoryRegion (Since: 0.14)
:   Information about a PCI device I/O region.

    Members:
    :   - **bar** (`int`) – the index of the Base Address Register for this region
        - **type** (`string`) –

          - ‘io’ if the region is a PIO region
          - ’memory’ if the region is a MMIO region
        - **address** (`int`) – memory address
        - **size** (`int`) – memory size
        - **prefetch** (`boolean`, *optional*) – if `type` is ‘memory’, true if the memory is prefetchable
        - **mem_type_64** (`boolean`, *optional*) – if `type` is ‘memory’, true if the BAR is 64-bit

*Object* PciBusInfo (Since: 2.4)
:   Information about a bus of a PCI Bridge device

    Members:
    :   - **number** (`int`) – primary bus interface number. This should be the number of
          the bus the device resides on.
        - **secondary** (`int`) – secondary bus interface number. This is the number of
          the main bus for the bridge
        - **subordinate** (`int`) – This is the highest number bus that resides below the
          bridge.
        - **io_range** ([`PciMemoryRange`](qemu-qmp-ref.md#object-QMP-pci.PciMemoryRange "QMP:pci.PciMemoryRange")) – The PIO range for all devices on this bridge
        - **memory_range** ([`PciMemoryRange`](qemu-qmp-ref.md#object-QMP-pci.PciMemoryRange "QMP:pci.PciMemoryRange")) – The MMIO range for all devices on this bridge
        - **prefetchable_range** ([`PciMemoryRange`](qemu-qmp-ref.md#object-QMP-pci.PciMemoryRange "QMP:pci.PciMemoryRange")) – The range of prefetchable MMIO for all devices
          on this bridge

*Object* PciBridgeInfo (Since: 0.14)
:   Information about a PCI Bridge device

    Members:
    :   - **bus** ([`PciBusInfo`](qemu-qmp-ref.md#object-QMP-pci.PciBusInfo "QMP:pci.PciBusInfo")) – information about the bus the device resides on
        - **devices** (`[`[`PciDeviceInfo`](qemu-qmp-ref.md#object-QMP-pci.PciDeviceInfo "QMP:pci.PciDeviceInfo")`]`, *optional*) – a list of [`PciDeviceInfo`](qemu-qmp-ref.md#object-QMP-pci.PciDeviceInfo "QMP:pci.PciDeviceInfo") for each device on this bridge

*Object* PciDeviceClass (Since: 2.4)
:   Information about the Class of a PCI device

    Members:
    :   - **desc** (`string`, *optional*) – a string description of the device’s class (not stable, and
          should only be treated as informational)
        - **class** (`int`) – the class code of the device

*Object* PciDeviceId (Since: 2.4)
:   Information about the Id of a PCI device

    Members:
    :   - **device** (`int`) – the PCI device id
        - **vendor** (`int`) – the PCI vendor id
        - **subsystem** (`int`, *optional*) – the PCI subsystem id (since 3.1)
        - **subsystem-vendor** (`int`, *optional*) – the PCI subsystem vendor id (since 3.1)

*Object* PciDeviceInfo (Since: 0.14)
:   Information about a PCI device

    Members:
    :   - **bus** (`int`) – the bus number of the device
        - **slot** (`int`) – the slot the device is located in
        - **function** (`int`) – the function of the slot used by the device
        - **class_info** ([`PciDeviceClass`](qemu-qmp-ref.md#object-QMP-pci.PciDeviceClass "QMP:pci.PciDeviceClass")) – the class of the device
        - **id** ([`PciDeviceId`](qemu-qmp-ref.md#object-QMP-pci.PciDeviceId "QMP:pci.PciDeviceId")) – the PCI device id
        - **irq** (`int`, *optional*) – if an IRQ is assigned to the device, the IRQ number
        - **irq_pin** (`int`) – the IRQ pin, zero means no IRQ (since 5.1)
        - **qdev_id** (`string`) – the device name of the PCI device
        - **pci_bridge** ([`PciBridgeInfo`](qemu-qmp-ref.md#object-QMP-pci.PciBridgeInfo "QMP:pci.PciBridgeInfo"), *optional*) – if the device is a PCI bridge, the bridge information
        - **regions** (`[`[`PciMemoryRegion`](qemu-qmp-ref.md#object-QMP-pci.PciMemoryRegion "QMP:pci.PciMemoryRegion")`]`) – a list of the PCI I/O regions associated with the device

*Object* PciInfo (Since: 0.14)
:   Information about a PCI bus

    Members:
    :   - **bus** (`int`) – the bus index
        - **devices** (`[`[`PciDeviceInfo`](qemu-qmp-ref.md#object-QMP-pci.PciDeviceInfo "QMP:pci.PciDeviceInfo")`]`) – a list of devices on this bus

*Command* query-pci (Since: 0.14)
:   Return information about the PCI bus topology of the guest.

    Return:
    :   `[`[`PciInfo`](qemu-qmp-ref.md#object-QMP-pci.PciInfo "QMP:pci.PciInfo")`]` – a list of info for each PCI bus. Each bus is
        represented by a json-object, which has a key with a json-array
        of all PCI devices attached to it. Each device is represented
        by a json-object.

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "query-pci" }
    > <- { "return": [
    >          {
    >             "bus": 0,
    >             "devices": [
    >                {
    >                   "bus": 0,
    >                   "qdev_id": "",
    >                   "slot": 0,
    >                   "class_info": {
    >                      "class": 1536,
    >                      "desc": "Host bridge"
    >                   },
    >                   "id": {
    >                      "device": 32902,
    >                      "vendor": 4663
    >                   },
    >                   "function": 0,
    >                   "regions": [
    >                   ]
    >                },
    >                {
    >                   "bus": 0,
    >                   "qdev_id": "",
    >                   "slot": 1,
    >                   "class_info": {
    >                      "class": 1537,
    >                      "desc": "ISA bridge"
    >                   },
    >                   "id": {
    >                      "device": 32902,
    >                      "vendor": 28672
    >                   },
    >                   "function": 0,
    >                   "regions": [
    >                   ]
    >                },
    >                {
    >                   "bus": 0,
    >                   "qdev_id": "",
    >                   "slot": 1,
    >                   "class_info": {
    >                      "class": 257,
    >                      "desc": "IDE controller"
    >                   },
    >                   "id": {
    >                      "device": 32902,
    >                      "vendor": 28688
    >                   },
    >                   "function": 1,
    >                   "regions": [
    >                      {
    >                         "bar": 4,
    >                         "size": 16,
    >                         "address": 49152,
    >                         "type": "io"
    >                      }
    >                   ]
    >                },
    >                {
    >                   "bus": 0,
    >                   "qdev_id": "",
    >                   "slot": 2,
    >                   "class_info": {
    >                      "class": 768,
    >                      "desc": "VGA controller"
    >                   },
    >                   "id": {
    >                      "device": 4115,
    >                      "vendor": 184
    >                   },
    >                   "function": 0,
    >                   "regions": [
    >                      {
    >                         "prefetch": true,
    >                         "mem_type_64": false,
    >                         "bar": 0,
    >                         "size": 33554432,
    >                         "address": 4026531840,
    >                         "type": "memory"
    >                      },
    >                      {
    >                         "prefetch": false,
    >                         "mem_type_64": false,
    >                         "bar": 1,
    >                         "size": 4096,
    >                         "address": 4060086272,
    >                         "type": "memory"
    >                      },
    >                      {
    >                         "prefetch": false,
    >                         "mem_type_64": false,
    >                         "bar": 6,
    >                         "size": 65536,
    >                         "address": -1,
    >                         "type": "memory"
    >                      }
    >                   ]
    >                },
    >                {
    >                   "bus": 0,
    >                   "qdev_id": "",
    >                   "irq": 11,
    >                   "slot": 4,
    >                   "class_info": {
    >                      "class": 1280,
    >                      "desc": "RAM controller"
    >                   },
    >                   "id": {
    >                      "device": 6900,
    >                      "vendor": 4098
    >                   },
    >                   "function": 0,
    >                   "regions": [
    >                      {
    >                         "bar": 0,
    >                         "size": 32,
    >                         "address": 49280,
    >                         "type": "io"
    >                      }
    >                   ]
    >                }
    >             ]
    >          }
    >       ]
    >    }
    > ```

    This example has been shortened as the real response is too long.

## [Statistics](qemu-qmp-ref.md#id41)

*Enum* StatsType (Since: 7.1)
:   Enumeration of statistics types

    Values:
    :   - **cumulative** – stat is cumulative; value can only increase.
        - **instant** – stat is instantaneous; value can increase or decrease.
        - **peak** – stat is the peak value; value can only increase.
        - **linear-histogram** – stat is a linear histogram.
        - **log2-histogram** – stat is a logarithmic histogram, with one bucket
          for each power of two.

*Enum* StatsUnit (Since: 7.1)
:   Enumeration of unit of measurement for statistics

    Values:
    :   - **bytes** – stat reported in bytes.
        - **seconds** – stat reported in seconds.
        - **cycles** – stat reported in clock cycles.
        - **boolean** – stat is a boolean value.

*Enum* StatsProvider (Since: 7.1)
:   Enumeration of statistics providers.

    Values:
    :   - **kvm** – since 7.1
        - **cryptodev** – since 8.0

*Enum* StatsTarget (Since: 7.1)
:   The kinds of objects on which one can request statistics.

    Values:
    :   - **vm** – statistics that apply to the entire virtual machine or the
          entire QEMU process.
        - **vcpu** – statistics that apply to a single virtual CPU.
        - **cryptodev** – statistics that apply to a crypto device (since 8.0)

*Object* StatsRequest (Since: 7.1)
:   Indicates a set of statistics that should be returned by
    [`query-stats`](qemu-qmp-ref.md#command-QMP-stats.query-stats "QMP:stats.query-stats").

    Members:
    :   - **provider** ([`StatsProvider`](qemu-qmp-ref.md#enum-QMP-stats.StatsProvider "QMP:stats.StatsProvider")) – provider for which to return statistics.
        - **names** (`[``string``]`, *optional*) – statistics to be returned (all if omitted).

*Object* StatsVCPUFilter (Since: 7.1)
:   Members:
    :   - **vcpus** (`[``string``]`, *optional*) – list of QOM paths for the desired vCPU objects.

*Object* StatsFilter (Since: 7.1)
:   The arguments to the [`query-stats`](qemu-qmp-ref.md#command-QMP-stats.query-stats "QMP:stats.query-stats") command; specifies a target for
    which to request statistics and optionally the required subset of
    information for that target.

    Members:
    :   - **target** ([`StatsTarget`](qemu-qmp-ref.md#enum-QMP-stats.StatsTarget "QMP:stats.StatsTarget")) – the kind of objects to query. Note that each possible
          target may enable additional filtering options
        - **providers** (`[`[`StatsRequest`](qemu-qmp-ref.md#object-QMP-stats.StatsRequest "QMP:stats.StatsRequest")`]`, *optional*) – which providers to request statistics from, and
          optionally which named values to return within each provider
        - When `target` is `vcpu`: The members of [`StatsVCPUFilter`](qemu-qmp-ref.md#object-QMP-stats.StatsVCPUFilter "QMP:stats.StatsVCPUFilter").

*Alternate* StatsValue (Since: 7.1)
:   Alternatives:
    :   - **scalar** (`int`) – single unsigned 64-bit integers.
        - **boolean** (`boolean`) – single boolean value.
        - **list** (`[``int``]`) – list of unsigned 64-bit integers (used for histograms).

*Object* Stats (Since: 7.1)
:   Members:
    :   - **name** (`string`) – name of stat.
        - **value** ([`StatsValue`](qemu-qmp-ref.md#alternate-QMP-stats.StatsValue "QMP:stats.StatsValue")) – stat value.

*Object* StatsResult (Since: 7.1)
:   Members:
    :   - **provider** ([`StatsProvider`](qemu-qmp-ref.md#enum-QMP-stats.StatsProvider "QMP:stats.StatsProvider")) – provider for this set of statistics.
        - **qom-path** (`string`, *optional*) – Path to the object for which the statistics are returned,
          if the object is exposed in the QOM tree
        - **stats** (`[`[`Stats`](qemu-qmp-ref.md#object-QMP-stats.Stats "QMP:stats.Stats")`]`) – list of statistics.

*Command* query-stats (Since: 7.1)
:   Return runtime-collected statistics for objects such as the VM or
    its vCPUs.

    The arguments are a [`StatsFilter`](qemu-qmp-ref.md#object-QMP-stats.StatsFilter "QMP:stats.StatsFilter") and specify the provider and
    objects to return statistics about.

    Arguments:
    :   - The members of [`StatsFilter`](qemu-qmp-ref.md#object-QMP-stats.StatsFilter "QMP:stats.StatsFilter").

    Return:
    :   `[`[`StatsResult`](qemu-qmp-ref.md#object-QMP-stats.StatsResult "QMP:stats.StatsResult")`]` – a list of statistics, one for each provider and object
        (e.g., for each vCPU).

*Object* StatsSchemaValue (Since: 7.1)
:   Schema for a single statistic.

    Members:
    :   - **name** (`string`) – name of the statistic; each element of the schema is uniquely
          identified by a target, a provider (both available in
          [`StatsSchema`](qemu-qmp-ref.md#object-QMP-stats.StatsSchema "QMP:stats.StatsSchema")) and the name.
        - **type** ([`StatsType`](qemu-qmp-ref.md#enum-QMP-stats.StatsType "QMP:stats.StatsType")) – kind of statistic.
        - **unit** ([`StatsUnit`](qemu-qmp-ref.md#enum-QMP-stats.StatsUnit "QMP:stats.StatsUnit"), *optional*) – basic unit of measure for the statistic; if missing, the
          statistic is a simple number or counter.
        - **base** (`int`, *optional*) – base for the multiple of `unit` in which the statistic is
          measured. Only present if `exponent` is non-zero; `base` and
          `exponent` together form a SI prefix (e.g., _nano-_ for
          `base=10` and `exponent=-9`) or IEC binary prefix (e.g.
          _kibi-_ for `base=2` and `exponent=10`)
        - **exponent** (`int`) – exponent for the multiple of `unit` in which the statistic
          is expressed, or 0 for the basic unit
        - **bucket-size** (`int`, *optional*) – Present when `type` is “linear-histogram”, contains the
          width of each bucket of the histogram.

*Object* StatsSchema (Since: 7.1)
:   Schema for all available statistics for a provider and target.

    Members:
    :   - **provider** ([`StatsProvider`](qemu-qmp-ref.md#enum-QMP-stats.StatsProvider "QMP:stats.StatsProvider")) – provider for this set of statistics.
        - **target** ([`StatsTarget`](qemu-qmp-ref.md#enum-QMP-stats.StatsTarget "QMP:stats.StatsTarget")) – the kind of object that can be queried through the
          provider.
        - **stats** (`[`[`StatsSchemaValue`](qemu-qmp-ref.md#object-QMP-stats.StatsSchemaValue "QMP:stats.StatsSchemaValue")`]`) – list of statistics.

*Command* query-stats-schemas (Since: 7.1)
:   Return the schema for all available runtime-collected statistics.

    Arguments:
    :   - **provider** ([`StatsProvider`](qemu-qmp-ref.md#enum-QMP-stats.StatsProvider "QMP:stats.StatsProvider"), *optional*) – a provider to restrict the query to.

    Return:
    :   `[`[`StatsSchema`](qemu-qmp-ref.md#object-QMP-stats.StatsSchema "QMP:stats.StatsSchema")`]`

    > **Note:**
    >
    > Runtime-collected statistics and their names fall outside
    > QEMU’s usual deprecation policies. QEMU will try to keep the set
    > of available data stable, together with their names, but will not
    > guarantee stability at all costs; the same is true of providers
    > that source statistics externally, e.g. from Linux. For example,
    > if the same value is being tracked with different names on
    > different architectures or by different providers, one of them
    > might be renamed. A statistic might go away if an algorithm is
    > changed or some code is removed; changing a default might cause
    > previously useful statistics to always report 0. Such changes,
    > however, are expected to be rare.

## [Virtio devices](qemu-qmp-ref.md#id42)

*Object* VirtioInfo (Since: 7.2)
:   Basic information about a given VirtIODevice

    Members:
    :   - **path** (`string`) – The VirtIODevice’s canonical QOM path
        - **name** (`string`) – Name of the VirtIODevice

*Command* x-query-virtio (Since: 7.2)
:   This command is unstable/experimental.

    Return a list of all realized VirtIODevices

    Features:
    :   - **unstable** – This command is meant for debugging.

    Return:
    :   `[`[`VirtioInfo`](qemu-qmp-ref.md#object-QMP-virtio.VirtioInfo "QMP:virtio.VirtioInfo")`]` – List of gathered VirtIODevices

    > **Example::**
    >
    > ```QMP
    > -> { "execute": "x-query-virtio" }
    > <- { "return": [
    >          {
    >              "name": "virtio-input",
    >              "path": "/machine/peripheral-anon/device[4]/virtio-backend"
    >          },
    >          {
    >              "name": "virtio-crypto",
    >              "path": "/machine/peripheral/crypto0/virtio-backend"
    >          },
    >          {
    >              "name": "virtio-scsi",
    >              "path": "/machine/peripheral-anon/device[2]/virtio-backend"
    >          },
    >          {
    >              "name": "virtio-net",
    >              "path": "/machine/peripheral-anon/device[1]/virtio-backend"
    >          },
    >          {
    >              "name": "virtio-serial",
    >              "path": "/machine/peripheral-anon/device[0]/virtio-backend"
    >          }
    >      ]
    >    }
    > ```

*Object* VhostStatus (Since: 7.2)
:   Information about a vhost device. This information will only be
    displayed if the vhost device is active.

    Members:
    :   - **n-mem-sections** (`int`) – vhost_dev n_mem_sections
        - **n-tmp-sections** (`int`) – vhost_dev n_tmp_sections
        - **nvqs** (`int`) – vhost_dev nvqs (number of virtqueues being used)
        - **vq-index** (`int`) – vhost_dev vq_index
        - **features** ([`VirtioDeviceFeatures`](qemu-qmp-ref.md#object-QMP-virtio.VirtioDeviceFeatures "QMP:virtio.VirtioDeviceFeatures")) – vhost_dev features
        - **acked-features** ([`VirtioDeviceFeatures`](qemu-qmp-ref.md#object-QMP-virtio.VirtioDeviceFeatures "QMP:virtio.VirtioDeviceFeatures")) – vhost_dev acked_features
        - **protocol-features** ([`VhostDeviceProtocols`](qemu-qmp-ref.md#object-QMP-virtio.VhostDeviceProtocols "QMP:virtio.VhostDeviceProtocols")) – vhost_dev protocol_features
        - **max-queues** (`int`) – vhost_dev max_queues
        - **backend-cap** (`int`) – vhost_dev backend_cap
        - **log-enabled** (`boolean`) – vhost_dev log_enabled flag
        - **log-size** (`int`) – vhost_dev log_size

*Object* VirtioStatus (Since: 7.2)
:   Full status of the virtio device with most VirtIODevice members.
    Also includes the full status of the corresponding vhost device if
    the vhost device is active.

    Members:
    :   - **name** (`string`) – VirtIODevice name
        - **device-id** (`int`) – VirtIODevice ID
        - **vhost-started** (`boolean`) – VirtIODevice vhost_started flag
        - **guest-features** ([`VirtioDeviceFeatures`](qemu-qmp-ref.md#object-QMP-virtio.VirtioDeviceFeatures "QMP:virtio.VirtioDeviceFeatures")) – VirtIODevice guest_features
        - **host-features** ([`VirtioDeviceFeatures`](qemu-qmp-ref.md#object-QMP-virtio.VirtioDeviceFeatures "QMP:virtio.VirtioDeviceFeatures")) – VirtIODevice host_features
        - **backend-features** ([`VirtioDeviceFeatures`](qemu-qmp-ref.md#object-QMP-virtio.VirtioDeviceFeatures "QMP:virtio.VirtioDeviceFeatures")) – VirtIODevice backend_features
        - **device-endian** (`string`) – VirtIODevice device_endian
        - **num-vqs** (`int`) – VirtIODevice virtqueue count. This is the number of
          active virtqueues being used by the VirtIODevice.
        - **status** ([`VirtioDeviceStatus`](qemu-qmp-ref.md#object-QMP-virtio.VirtioDeviceStatus "QMP:virtio.VirtioDeviceStatus")) – VirtIODevice configuration status ([`VirtioDeviceStatus`](qemu-qmp-ref.md#object-QMP-virtio.VirtioDeviceStatus "QMP:virtio.VirtioDeviceStatus"))
        - **isr** (`int`) – VirtIODevice ISR
        - **queue-sel** (`int`) – VirtIODevice queue_sel
        - **vm-running** (`boolean`) – VirtIODevice vm_running flag
        - **broken** (`boolean`) – VirtIODevice broken flag
        - **disabled** (`boolean`) – VirtIODevice disabled flag
        - **use-started** (`boolean`) – VirtIODevice use_started flag
        - **started** (`boolean`) – VirtIODevice started flag
        - **start-on-kick** (`boolean`) – VirtIODevice start_on_kick flag
        - **disable-legacy-check** (`boolean`) – VirtIODevice disabled_legacy_check flag
        - **bus-name** (`string`) – VirtIODevice bus_name
        - **use-guest-notifier-mask** (`boolean`) – VirtIODevice use_guest_notifier_mask flag
        - **vhost-dev** ([`VhostStatus`](qemu-qmp-ref.md#object-QMP-virtio.VhostStatus "QMP:virtio.VhostStatus"), *optional*) – Corresponding vhost device info for a given
          VirtIODevice. Present if the given VirtIODevice has an active
          vhost device.

*Command* x-query-virtio-status (Since: 7.2)
:   This command is unstable/experimental.

    Poll for a comprehensive status of a given virtio device

    Arguments:
    :   - **path** (`string`) – Canonical QOM path of the VirtIODevice

    Features:
    :   - **unstable** – This command is meant for debugging.

    Return:
    :   [`VirtioStatus`](qemu-qmp-ref.md#object-QMP-virtio.VirtioStatus "QMP:virtio.VirtioStatus") – Status of the virtio device

    > **Example::**
    >
    > Poll for the status of virtio-crypto (no vhost-crypto active)
    >
    > ```QMP
    > -> { "execute": "x-query-virtio-status",
    >      "arguments": { "path": "/machine/peripheral/crypto0/virtio-backend" }
    >    }
    > <- { "return": {
    >          "device-endian": "little",
    >          "bus-name": "",
    >          "disable-legacy-check": false,
    >          "name": "virtio-crypto",
    >          "started": true,
    >          "device-id": 20,
    >          "backend-features": {
    >              "transports": [],
    >              "dev-features": []
    >          },
    >          "start-on-kick": false,
    >          "isr": 1,
    >          "broken": false,
    >          "status": {
    >              "statuses": [
    >                  "VIRTIO_CONFIG_S_ACKNOWLEDGE: Valid virtio device found",
    >                  "VIRTIO_CONFIG_S_DRIVER: Guest OS compatible with device",
    >                  "VIRTIO_CONFIG_S_FEATURES_OK: Feature negotiation complete",
    >                  "VIRTIO_CONFIG_S_DRIVER_OK: Driver setup and ready"
    >              ]
    >          },
    >          "num-vqs": 2,
    >          "guest-features": {
    >              "dev-features": [],
    >              "transports": [
    >                  "VIRTIO_RING_F_EVENT_IDX: Used & avail. event fields enabled",
    >                  "VIRTIO_RING_F_INDIRECT_DESC: Indirect descriptors supported",
    >                  "VIRTIO_F_VERSION_1: Device compliant for v1 spec (legacy)"
    >              ]
    >          },
    >          "host-features": {
    >              "unknown-dev-features": 1073741824,
    >              "unknown-dev-features2": 0,
    >              "dev-features": [],
    >              "transports": [
    >                  "VIRTIO_RING_F_EVENT_IDX: Used & avail. event fields enabled",
    >                  "VIRTIO_RING_F_INDIRECT_DESC: Indirect descriptors supported",
    >                  "VIRTIO_F_VERSION_1: Device compliant for v1 spec (legacy)",
    >                  "VIRTIO_F_ANY_LAYOUT: Device accepts arbitrary desc. layouts",
    >                  "VIRTIO_F_NOTIFY_ON_EMPTY: Notify when device runs out of avail. descs. on VQ"
    >              ]
    >          },
    >          "use-guest-notifier-mask": true,
    >          "vm-running": true,
    >          "queue-sel": 1,
    >          "disabled": false,
    >          "vhost-started": false,
    >          "use-started": true
    >      }
    >    }
    > ```

    > **Example::**
    >
    > Poll for the status of virtio-net (vhost-net is active)
    >
    > ```QMP
    > -> { "execute": "x-query-virtio-status",
    >      "arguments": { "path": "/machine/peripheral-anon/device[1]/virtio-backend" }
    >    }
    > <- { "return": {
    >          "device-endian": "little",
    >          "bus-name": "",
    >          "disabled-legacy-check": false,
    >          "name": "virtio-net",
    >          "started": true,
    >          "device-id": 1,
    >          "vhost-dev": {
    >              "n-tmp-sections": 4,
    >              "n-mem-sections": 4,
    >              "max-queues": 1,
    >              "backend-cap": 2,
    >              "log-size": 0,
    >              "backend-features": {
    >                  "dev-features": [],
    >                  "transports": []
    >              },
    >              "nvqs": 2,
    >              "protocol-features": {
    >                  "protocols": []
    >              },
    >              "vq-index": 0,
    >              "log-enabled": false,
    >              "acked-features": {
    >                  "dev-features": [
    >                      "VIRTIO_NET_F_MRG_RXBUF: Driver can merge receive buffers"
    >                  ],
    >                  "transports": [
    >                      "VIRTIO_RING_F_EVENT_IDX: Used & avail. event fields enabled",
    >                      "VIRTIO_RING_F_INDIRECT_DESC: Indirect descriptors supported",
    >                      "VIRTIO_F_VERSION_1: Device compliant for v1 spec (legacy)"
    >                  ]
    >              },
    >              "features": {
    >                  "dev-features": [
    >                      "VHOST_F_LOG_ALL: Logging write descriptors supported",
    >                      "VIRTIO_NET_F_MRG_RXBUF: Driver can merge receive buffers"
    >                  ],
    >                  "transports": [
    >                      "VIRTIO_RING_F_EVENT_IDX: Used & avail. event fields enabled",
    >                      "VIRTIO_RING_F_INDIRECT_DESC: Indirect descriptors supported",
    >                      "VIRTIO_F_IOMMU_PLATFORM: Device can be used on IOMMU platform",
    >                      "VIRTIO_F_VERSION_1: Device compliant for v1 spec (legacy)",
    >                      "VIRTIO_F_ANY_LAYOUT: Device accepts arbitrary desc. layouts",
    >                      "VIRTIO_F_NOTIFY_ON_EMPTY: Notify when device runs out of avail. descs. on VQ"
    >                  ]
    >              }
    >          },
    >          "backend-features": {
    >              "dev-features": [
    >                  "VHOST_USER_F_PROTOCOL_FEATURES: Vhost-user protocol features negotiation supported",
    >                  "VIRTIO_NET_F_GSO: Handling GSO-type packets supported",
    >                  "VIRTIO_NET_F_CTRL_MAC_ADDR: MAC address set through control channel",
    >                  "VIRTIO_NET_F_GUEST_ANNOUNCE: Driver sending gratuitous packets supported",
    >                  "VIRTIO_NET_F_CTRL_RX_EXTRA: Extra RX mode control supported",
    >                  "VIRTIO_NET_F_CTRL_VLAN: Control channel VLAN filtering supported",
    >                  "VIRTIO_NET_F_CTRL_RX: Control channel RX mode supported",
    >                  "VIRTIO_NET_F_CTRL_VQ: Control channel available",
    >                  "VIRTIO_NET_F_STATUS: Configuration status field available",
    >                  "VIRTIO_NET_F_MRG_RXBUF: Driver can merge receive buffers",
    >                  "VIRTIO_NET_F_HOST_UFO: Device can receive UFO",
    >                  "VIRTIO_NET_F_HOST_ECN: Device can receive TSO with ECN",
    >                  "VIRTIO_NET_F_HOST_TSO6: Device can receive TSOv6",
    >                  "VIRTIO_NET_F_HOST_TSO4: Device can receive TSOv4",
    >                  "VIRTIO_NET_F_GUEST_UFO: Driver can receive UFO",
    >                  "VIRTIO_NET_F_GUEST_ECN: Driver can receive TSO with ECN",
    >                  "VIRTIO_NET_F_GUEST_TSO6: Driver can receive TSOv6",
    >                  "VIRTIO_NET_F_GUEST_TSO4: Driver can receive TSOv4",
    >                  "VIRTIO_NET_F_MAC: Device has given MAC address",
    >                  "VIRTIO_NET_F_CTRL_GUEST_OFFLOADS: Control channel offloading reconfig. supported",
    >                  "VIRTIO_NET_F_GUEST_CSUM: Driver handling packets with partial checksum supported",
    >                  "VIRTIO_NET_F_CSUM: Device handling packets with partial checksum supported"
    >              ],
    >              "transports": [
    >                  "VIRTIO_RING_F_EVENT_IDX: Used & avail. event fields enabled",
    >                  "VIRTIO_RING_F_INDIRECT_DESC: Indirect descriptors supported",
    >                  "VIRTIO_F_VERSION_1: Device compliant for v1 spec (legacy)",
    >                  "VIRTIO_F_ANY_LAYOUT: Device accepts arbitrary desc. layouts",
    >                  "VIRTIO_F_NOTIFY_ON_EMPTY: Notify when device runs out of avail. descs. on VQ"
    >              ]
    >          },
    >          "start-on-kick": false,
    >          "isr": 1,
    >          "broken": false,
    >          "status": {
    >              "statuses": [
    >                  "VIRTIO_CONFIG_S_ACKNOWLEDGE: Valid virtio device found",
    >                  "VIRTIO_CONFIG_S_DRIVER: Guest OS compatible with device",
    >                  "VIRTIO_CONFIG_S_FEATURES_OK: Feature negotiation complete",
    >                  "VIRTIO_CONFIG_S_DRIVER_OK: Driver setup and ready"
    >              ]
    >          },
    >          "num-vqs": 3,
    >          "guest-features": {
    >              "dev-features": [
    >                  "VIRTIO_NET_F_CTRL_MAC_ADDR: MAC address set through control channel",
    >                  "VIRTIO_NET_F_GUEST_ANNOUNCE: Driver sending gratuitous packets supported",
    >                  "VIRTIO_NET_F_CTRL_VLAN: Control channel VLAN filtering supported",
    >                  "VIRTIO_NET_F_CTRL_RX: Control channel RX mode supported",
    >                  "VIRTIO_NET_F_CTRL_VQ: Control channel available",
    >                  "VIRTIO_NET_F_STATUS: Configuration status field available",
    >                  "VIRTIO_NET_F_MRG_RXBUF: Driver can merge receive buffers",
    >                  "VIRTIO_NET_F_HOST_UFO: Device can receive UFO",
    >                  "VIRTIO_NET_F_HOST_ECN: Device can receive TSO with ECN",
    >                  "VIRTIO_NET_F_HOST_TSO6: Device can receive TSOv6",
    >                  "VIRTIO_NET_F_HOST_TSO4: Device can receive TSOv4",
    >                  "VIRTIO_NET_F_GUEST_UFO: Driver can receive UFO",
    >                  "VIRTIO_NET_F_GUEST_ECN: Driver can receive TSO with ECN",
    >                  "VIRTIO_NET_F_GUEST_TSO6: Driver can receive TSOv6",
    >                  "VIRTIO_NET_F_GUEST_TSO4: Driver can receive TSOv4",
    >                  "VIRTIO_NET_F_MAC: Device has given MAC address",
    >                  "VIRTIO_NET_F_CTRL_GUEST_OFFLOADS: Control channel offloading reconfig. supported",
    >                  "VIRTIO_NET_F_GUEST_CSUM: Driver handling packets with partial checksum supported",
    >                  "VIRTIO_NET_F_CSUM: Device handling packets with partial checksum supported"
    >              ],
    >              "transports": [
    >                  "VIRTIO_RING_F_EVENT_IDX: Used & avail. event fields enabled",
    >                  "VIRTIO_RING_F_INDIRECT_DESC: Indirect descriptors supported",
    >                  "VIRTIO_F_VERSION_1: Device compliant for v1 spec (legacy)"
    >             ]
    >          },
    >          "host-features": {
    >              "dev-features": [
    >                  "VHOST_USER_F_PROTOCOL_FEATURES: Vhost-user protocol features negotiation supported",
    >                  "VIRTIO_NET_F_GSO: Handling GSO-type packets supported",
    >                  "VIRTIO_NET_F_CTRL_MAC_ADDR: MAC address set through control channel",
    >                  "VIRTIO_NET_F_GUEST_ANNOUNCE: Driver sending gratuitous packets supported",
    >                  "VIRTIO_NET_F_CTRL_RX_EXTRA: Extra RX mode control supported",
    >                  "VIRTIO_NET_F_CTRL_VLAN: Control channel VLAN filtering supported",
    >                  "VIRTIO_NET_F_CTRL_RX: Control channel RX mode supported",
    >                  "VIRTIO_NET_F_CTRL_VQ: Control channel available",
    >                  "VIRTIO_NET_F_STATUS: Configuration status field available",
    >                  "VIRTIO_NET_F_MRG_RXBUF: Driver can merge receive buffers",
    >                  "VIRTIO_NET_F_HOST_UFO: Device can receive UFO",
    >                  "VIRTIO_NET_F_HOST_ECN: Device can receive TSO with ECN",
    >                  "VIRTIO_NET_F_HOST_TSO6: Device can receive TSOv6",
    >                  "VIRTIO_NET_F_HOST_TSO4: Device can receive TSOv4",
    >                  "VIRTIO_NET_F_GUEST_UFO: Driver can receive UFO",
    >                  "VIRTIO_NET_F_GUEST_ECN: Driver can receive TSO with ECN",
    >                  "VIRTIO_NET_F_GUEST_TSO6: Driver can receive TSOv6",
    >                  "VIRTIO_NET_F_GUEST_TSO4: Driver can receive TSOv4",
    >                  "VIRTIO_NET_F_MAC: Device has given MAC address",
    >                  "VIRTIO_NET_F_CTRL_GUEST_OFFLOADS: Control channel offloading reconfig. supported",
    >                  "VIRTIO_NET_F_GUEST_CSUM: Driver handling packets with partial checksum supported",
    >                  "VIRTIO_NET_F_CSUM: Device handling packets with partial checksum supported"
    >              ],
    >              "transports": [
    >                  "VIRTIO_RING_F_EVENT_IDX: Used & avail. event fields enabled",
    >                  "VIRTIO_RING_F_INDIRECT_DESC: Indirect descriptors supported",
    >                  "VIRTIO_F_VERSION_1: Device compliant for v1 spec (legacy)",
    >                  "VIRTIO_F_ANY_LAYOUT: Device accepts arbitrary desc. layouts",
    >                  "VIRTIO_F_NOTIFY_ON_EMPTY: Notify when device runs out of avail. descs. on VQ"
    >             ]
    >          },
    >          "use-guest-notifier-mask": true,
    >          "vm-running": true,
    >          "queue-sel": 2,
    >          "disabled": false,
    >          "vhost-started": true,
    >          "use-started": true
    >      }
    >    }
    > ```

*Object* VirtioDeviceStatus (Since: 7.2)
:   A structure defined to list the configuration statuses of a virtio
    device

    Members:
    :   - **statuses** (`[``string``]`) – List of decoded configuration statuses of the virtio
          device
        - **unknown-statuses** (`int`, *optional*) – Virtio device statuses bitmap that have not been
          decoded

*Object* VhostDeviceProtocols (Since: 7.2)
:   A structure defined to list the vhost user protocol features of a
    Vhost User device

    Members:
    :   - **protocols** (`[``string``]`) – List of decoded vhost user protocol features of a vhost
          user device
        - **unknown-protocols** (`int`, *optional*) – Vhost user device protocol features bitmap that
          have not been decoded

*Object* VirtioDeviceFeatures (Since: 7.2)
:   The common fields that apply to most Virtio devices. Some devices
    may not have their own device-specific features (e.g. virtio-rng).

    Members:
    :   - **transports** (`[``string``]`) – List of transport features of the virtio device
        - **dev-features** (`[``string``]`, *optional*) – List of device-specific features (if the device has
          unique features)
        - **unknown-dev-features** (`int`, *optional*) – Virtio device features bitmap that have not
          been decoded (bits 0-63)
        - **unknown-dev-features2** (`int`, *optional*) – Virtio device features bitmap that have not
          been decoded (bits 64-127) (since 10.2)

*Object* VirtQueueStatus (Since: 7.2)
:   Information of a VirtIODevice VirtQueue, including most members of
    the VirtQueue data structure.

    Members:
    :   - **name** (`string`) – Name of the VirtIODevice that uses this VirtQueue
        - **queue-index** (`int`) – VirtQueue queue_index
        - **inuse** (`int`) – VirtQueue inuse
        - **vring-num** (`int`) – VirtQueue vring.num
        - **vring-num-default** (`int`) – VirtQueue vring.num_default
        - **vring-align** (`int`) – VirtQueue vring.align
        - **vring-desc** (`int`) – VirtQueue vring.desc (descriptor area)
        - **vring-avail** (`int`) – VirtQueue vring.avail (driver area)
        - **vring-used** (`int`) – VirtQueue vring.used (device area)
        - **last-avail-idx** (`int`, *optional*) – VirtQueue last_avail_idx or return of vhost_dev
          vhost_get_vring_base (if vhost active)
        - **shadow-avail-idx** (`int`, *optional*) – VirtQueue shadow_avail_idx
        - **used-idx** (`int`) – VirtQueue used_idx
        - **signalled-used** (`int`) – VirtQueue signalled_used
        - **signalled-used-valid** (`boolean`) – VirtQueue signalled_used_valid flag

*Command* x-query-virtio-queue-status (Since: 7.2)
:   This command is unstable/experimental.

    Return the status of a given VirtIODevice’s VirtQueue

    Arguments:
    :   - **path** (`string`) – VirtIODevice canonical QOM path
        - **queue** (`int`) – VirtQueue index to examine

    Features:
    :   - **unstable** – This command is meant for debugging.

    Return:
    :   [`VirtQueueStatus`](qemu-qmp-ref.md#object-QMP-virtio.VirtQueueStatus "QMP:virtio.VirtQueueStatus") – Status of the queue

    > **Note:**
    >
    > last_avail_idx will not be displayed in the case where the
    > selected VirtIODevice has a running vhost device and the
    > VirtIODevice VirtQueue index (queue) does not exist for the
    > corresponding vhost device vhost_virtqueue. Also,
    > shadow_avail_idx will not be displayed in the case where the
    > selected VirtIODevice has a running vhost device.

    > **Example::**
    >
    > Get [`VirtQueueStatus`](qemu-qmp-ref.md#object-QMP-virtio.VirtQueueStatus "QMP:virtio.VirtQueueStatus") for virtio-vsock (vhost-vsock running)
    >
    > ```QMP
    > -> { "execute": "x-query-virtio-queue-status",
    >      "arguments": { "path": "/machine/peripheral/vsock0/virtio-backend",
    >                     "queue": 1 }
    >    }
    > <- { "return": {
    >          "signalled-used": 0,
    >          "inuse": 0,
    >          "name": "vhost-vsock",
    >          "vring-align": 4096,
    >          "vring-desc": 5217370112,
    >          "signalled-used-valid": false,
    >          "vring-num-default": 128,
    >          "vring-avail": 5217372160,
    >          "queue-index": 1,
    >          "last-avail-idx": 0,
    >          "vring-used": 5217372480,
    >          "used-idx": 0,
    >          "vring-num": 128
    >      }
    >    }
    > ```

    > **Example::**
    >
    > Get [`VirtQueueStatus`](qemu-qmp-ref.md#object-QMP-virtio.VirtQueueStatus "QMP:virtio.VirtQueueStatus") for virtio-serial (no vhost)
    >
    > ```QMP
    > -> { "execute": "x-query-virtio-queue-status",
    >      "arguments": { "path": "/machine/peripheral-anon/device[0]/virtio-backend",
    >                     "queue": 20 }
    >    }
    > <- { "return": {
    >          "signalled-used": 0,
    >          "inuse": 0,
    >          "name": "virtio-serial",
    >          "vring-align": 4096,
    >          "vring-desc": 5182074880,
    >          "signalled-used-valid": false,
    >          "vring-num-default": 128,
    >          "vring-avail": 5182076928,
    >          "queue-index": 20,
    >          "last-avail-idx": 0,
    >          "vring-used": 5182077248,
    >          "used-idx": 0,
    >          "shadow-avail-idx": 0,
    >          "vring-num": 128
    >      }
    >    }
    > ```

*Object* VirtVhostQueueStatus (Since: 7.2)
:   Information of a vhost device’s vhost_virtqueue, including most
    members of the vhost_dev vhost_virtqueue data structure.

    Members:
    :   - **name** (`string`) – Name of the VirtIODevice that uses this vhost_virtqueue
        - **kick** (`int`) – vhost_virtqueue kick
        - **call** (`int`) – vhost_virtqueue call
        - **num** (`int`) – vhost_virtqueue num
        - **desc-phys** (`int`) – vhost_virtqueue desc_phys (descriptor area physical
          address)
        - **desc-size** (`int`) – vhost_virtqueue desc_size
        - **avail-phys** (`int`) – vhost_virtqueue avail_phys (driver area physical
          address)
        - **avail-size** (`int`) – vhost_virtqueue avail_size
        - **used-phys** (`int`) – vhost_virtqueue used_phys (device area physical address)
        - **used-size** (`int`) – vhost_virtqueue used_size

*Command* x-query-virtio-vhost-queue-status (Since: 7.2)
:   This command is unstable/experimental.

    Return information of a given vhost device’s vhost_virtqueue

    Arguments:
    :   - **path** (`string`) – VirtIODevice canonical QOM path
        - **queue** (`int`) – vhost_virtqueue index to examine

    Features:
    :   - **unstable** – This command is meant for debugging.

    Return:
    :   [`VirtVhostQueueStatus`](qemu-qmp-ref.md#object-QMP-virtio.VirtVhostQueueStatus "QMP:virtio.VirtVhostQueueStatus") – Status of the vhost_virtqueue

    > **Example: Get vhost_virtqueue status for vhost-crypto:**
    >
    > ```QMP
    >  -> { "execute": "x-query-virtio-vhost-queue-status",
    >       "arguments": { "path": "/machine/peripheral/crypto0/virtio-backend",
    >                      "queue": 0 }
    >     }
    >  <- { "return": {
    >           "avail-phys": 5216124928,
    >           "name": "virtio-crypto",
    >           "used-phys": 5216127040,
    >           "avail-size": 2054,
    >           "desc-size": 16384,
    >           "used-size": 8198,
    >           "num": 1024,
    >           "call": 0,
    >           "desc-phys": 5216108544,
    >           "kick": 0
    >       }
    >     }
    > ```

    > **Example: Get vhost_virtqueue status for vhost-vsock:**
    >
    > ```QMP
    >  -> { "execute": "x-query-virtio-vhost-queue-status",
    >       "arguments": { "path": "/machine/peripheral/vsock0/virtio-backend",
    >                      "queue": 0 }
    >     }
    >  <- { "return": {
    >           "avail-phys": 5182261248,
    >           "name": "vhost-vsock",
    >           "used-phys": 5182261568,
    >           "avail-size": 262,
    >           "desc-size": 2048,
    >           "used-size": 1030,
    >           "num": 128,
    >           "call": 0,
    >           "desc-phys": 5182259200,
    >           "kick": 0
    >       }
    >     }
    > ```

*Object* VirtioRingDesc (Since: 7.2)
:   Information regarding the vring descriptor area

    Members:
    :   - **addr** (`int`) – Guest physical address of the descriptor area
        - **len** (`int`) – Length of the descriptor area
        - **flags** (`[``string``]`) – List of descriptor flags

*Object* VirtioRingAvail (Since: 7.2)
:   Information regarding the avail vring (a.k.a. driver area)

    Members:
    :   - **flags** (`int`) – VRingAvail flags
        - **idx** (`int`) – VRingAvail index
        - **ring** (`int`) – VRingAvail ring[] entry at provided index

*Object* VirtioRingUsed (Since: 7.2)
:   Information regarding the used vring (a.k.a. device area)

    Members:
    :   - **flags** (`int`) – VRingUsed flags
        - **idx** (`int`) – VRingUsed index

*Object* VirtioQueueElement (Since: 7.2)
:   Information regarding a VirtQueue’s VirtQueueElement including
    descriptor, driver, and device areas

    Members:
    :   - **name** (`string`) – Name of the VirtIODevice that uses this VirtQueue
        - **index** (`int`) – Index of the element in the queue
        - **descs** (`[`[`VirtioRingDesc`](qemu-qmp-ref.md#object-QMP-virtio.VirtioRingDesc "QMP:virtio.VirtioRingDesc")`]`) – List of descriptors ([`VirtioRingDesc`](qemu-qmp-ref.md#object-QMP-virtio.VirtioRingDesc "QMP:virtio.VirtioRingDesc"))
        - **avail** ([`VirtioRingAvail`](qemu-qmp-ref.md#object-QMP-virtio.VirtioRingAvail "QMP:virtio.VirtioRingAvail")) – VRingAvail info
        - **used** ([`VirtioRingUsed`](qemu-qmp-ref.md#object-QMP-virtio.VirtioRingUsed "QMP:virtio.VirtioRingUsed")) – VRingUsed info

*Command* x-query-virtio-queue-element (Since: 7.2)
:   This command is unstable/experimental.

    Return the information about a VirtQueue’s VirtQueueElement

    Arguments:
    :   - **path** (`string`) – VirtIODevice canonical QOM path
        - **queue** (`int`) – VirtQueue index to examine
        - **index** (`int`, *optional*) – Index of the element in the queue (default: head of the
          queue)

    Return:
    :   [`VirtioQueueElement`](qemu-qmp-ref.md#object-QMP-virtio.VirtioQueueElement "QMP:virtio.VirtioQueueElement")

    Features:
    :   - **unstable** – This command is meant for debugging.

    > **Example: Introspect on virtio-net’s VirtQueue 0 at index 5:**
    >
    > ```QMP
    >  -> { "execute": "x-query-virtio-queue-element",
    >       "arguments": { "path": "/machine/peripheral-anon/device[1]/virtio-backend",
    >                      "queue": 0,
    >                      "index": 5 }
    >     }
    >  <- { "return": {
    >           "index": 5,
    >           "name": "virtio-net",
    >           "descs": [
    >               {
    >                   "flags": ["write"],
    >                   "len": 1536,
    >                   "addr": 5257305600
    >               }
    >           ],
    >           "avail": {
    >               "idx": 256,
    >               "flags": 0,
    >               "ring": 5
    >           },
    >           "used": {
    >               "idx": 13,
    >               "flags": 0
    >           }
    >       }
    >     }
    > ```

    > **Example: Introspect on virtio-crypto’s VirtQueue 1 at head:**
    >
    > ```QMP
    >  -> { "execute": "x-query-virtio-queue-element",
    >       "arguments": { "path": "/machine/peripheral/crypto0/virtio-backend",
    >                      "queue": 1 }
    >     }
    >  <- { "return": {
    >           "index": 0,
    >           "name": "virtio-crypto",
    >           "descs": [
    >               {
    >                   "flags": [],
    >                   "len": 0,
    >                   "addr": 8080268923184214134
    >               }
    >           ],
    >           "avail": {
    >               "idx": 280,
    >               "flags": 0,
    >               "ring": 0
    >           },
    >           "used": {
    >               "idx": 280,
    >               "flags": 0
    >           }
    >       }
    >     }
    > ```

    > **Example: Introspect on virtio-scsi’s VirtQueue 2 at head:**
    >
    > ```QMP
    >  -> { "execute": "x-query-virtio-queue-element",
    >       "arguments": { "path": "/machine/peripheral-anon/device[2]/virtio-backend",
    >                      "queue": 2 }
    >     }
    >  <- { "return": {
    >           "index": 19,
    >           "name": "virtio-scsi",
    >           "descs": [
    >               {
    >                   "flags": ["used", "indirect", "write"],
    >                   "len": 4099327944,
    >                   "addr": 12055409292258155293
    >               }
    >           ],
    >           "avail": {
    >               "idx": 1147,
    >               "flags": 0,
    >               "ring": 19
    >           },
    >           "used": {
    >               "idx": 280,
    >               "flags": 0
    >           }
    >       }
    >     }
    > ```

*Object* IOThreadVirtQueueMapping (Since: 9.0)
:   Describes the subset of virtqueues assigned to an IOThread.

    Members:
    :   - **iothread** (`string`) – the id of IOThread object
        - **vqs** (`[``int``]`, *optional*) – an optional array of virtqueue indices that will be handled by
          this IOThread. When absent, virtqueues are assigned round-robin
          across all IOThreadVirtQueueMappings provided. Either all
          IOThreadVirtQueueMappings must have `vqs` or none of them must
          have it.

*Object* VirtIOGPUOutput (Since: 10.1)
:   Describes configuration of a VirtIO GPU output. If both `xres` and
    `yres` are set, they take precedence over root virtio-gpu resolution
    configuration and enable the corresponding output. If none of `xres`
    and `yres` are set, root virtio-gpu resolution configuration takes
    precedence and only the first output is enabled. Only setting one
    of `xres` or `yres` is an error.

    Members:
    :   - **name** (`string`) – the name of the output
        - **xres** (`int`, *optional*) – horizontal resolution of the output in pixels (since 11.0)
        - **yres** (`int`, *optional*) – vertical resolution of the output in pixels (since 11.0)

*Object* DummyVirtioForceArrays (Since: 9.0)
:   Not used by QMP; hack to let us use IOThreadVirtQueueMappingList and
    VirtIOGPUOutputList internally

    Members:
    :   - **unused-iothread-vq-mapping** (`[`[`IOThreadVirtQueueMapping`](qemu-qmp-ref.md#object-QMP-virtio.IOThreadVirtQueueMapping "QMP:virtio.IOThreadVirtQueueMapping")`]`) – Not documented
        - **unused-virtio-gpu-output** (`[`[`VirtIOGPUOutput`](qemu-qmp-ref.md#object-QMP-virtio.VirtIOGPUOutput "QMP:virtio.VirtIOGPUOutput")`]`) – Not documented

*Enum* GranuleMode (Since: 9.0)
:   Values:
    :   - **4k** – granule page size of 4KiB
        - **8k** – granule page size of 8KiB
        - **16k** – granule page size of 16KiB
        - **64k** – granule page size of 64KiB
        - **host** – granule matches the host page size

*Enum* VMAppleVirtioBlkVariant (Since: 9.2)
:   Values:
    :   - **unspecified** – The default, not a valid setting.
        - **root** – Block device holding the root volume
        - **aux** – Block device holding auxiliary data required for boot

## [VFIO devices](qemu-qmp-ref.md#id43)

*Enum* QapiVfioMigrationState (Since: 9.1)
:   An enumeration of the VFIO device migration states. In addition to
    the regular states, there are prepare states (with ‘prepare’ suffix)
    which indicate that the device is just about to transition to the
    corresponding state. Note that seeing a prepare state for state X
    doesn’t guarantee that the next state will be X, as the state
    transition can fail and the device may transition to a different
    state instead.

    Values:
    :   - **stop** – The device is stopped.
        - **running** – The device is running.
        - **stop-copy** – The device is stopped and its internal state is
          available for reading.
        - **resuming** – The device is stopped and its internal state is available
          for writing.
        - **running-p2p** – The device is running in the P2P quiescent state.
        - **pre-copy** – The device is running, tracking its internal state and
          its internal state is available for reading.
        - **pre-copy-p2p** – The device is running in the P2P quiescent state,
          tracking its internal state and its internal state is available
          for reading.
        - **pre-copy-p2p-prepare** – The device is just about to move to
          pre-copy-p2p state. (since 11.0)

*Event* VFIO_MIGRATION (Since: 9.1)
:   This event is emitted when a VFIO device migration state is changed.

    Members:
    :   - **device-id** (`string`) – The device’s id, if it has one.
        - **qom-path** (`string`) – The device’s QOM path.
        - **device-state** ([`QapiVfioMigrationState`](qemu-qmp-ref.md#enum-QMP-vfio.QapiVfioMigrationState "QMP:vfio.QapiVfioMigrationState")) – The new changed device migration state.

    > **Example::**
    >
    > ```QMP
    > <- { "timestamp": { "seconds": 1713771323, "microseconds": 212268 },
    >      "event": "VFIO_MIGRATION",
    >      "data": {
    >          "device-id": "vfio_dev1",
    >          "qom-path": "/machine/peripheral/vfio_dev1",
    >          "device-state": "stop" } }
    > ```

## [Cryptography devices](qemu-qmp-ref.md#id44)

*Enum* QCryptodevBackendAlgoType (Since: 8.0)
:   The supported algorithm types of a crypto device.

    Values:
    :   - **sym** – symmetric encryption
        - **asym** – asymmetric encryption

*Enum* QCryptodevBackendServiceType (Since: 8.0)
:   The supported service types of a crypto device.

    Values:
    :   - **cipher** – Symmetric Key Cipher service
        - **hash** – Hash service
        - **mac** – Message Authentication Codes service
        - **aead** – Authenticated Encryption with Associated Data service
        - **akcipher** – Asymmetric Key Cipher service

*Enum* QCryptodevBackendType (Since: 8.0)
:   The crypto device backend type

    Values:
    :   - **builtin** – the QEMU builtin support
        - **vhost-user** – vhost-user
        - **lkcf** – Linux kernel cryptographic framework

*Object* QCryptodevBackendClient (Since: 8.0)
:   Information about a queue of crypto device.

    Members:
    :   - **queue** (`int`) – the queue index of the crypto device
        - **type** ([`QCryptodevBackendType`](qemu-qmp-ref.md#enum-QMP-cryptodev.QCryptodevBackendType "QMP:cryptodev.QCryptodevBackendType")) – the type of the crypto device

*Object* QCryptodevInfo (Since: 8.0)
:   Information about a crypto device.

    Members:
    :   - **id** (`string`) – the id of the crypto device
        - **service** (`[`[`QCryptodevBackendServiceType`](qemu-qmp-ref.md#enum-QMP-cryptodev.QCryptodevBackendServiceType "QMP:cryptodev.QCryptodevBackendServiceType")`]`) – supported service types of a crypto device
        - **client** (`[`[`QCryptodevBackendClient`](qemu-qmp-ref.md#object-QMP-cryptodev.QCryptodevBackendClient "QMP:cryptodev.QCryptodevBackendClient")`]`) – the additional information of the crypto device

*Command* query-cryptodev (Since: 8.0)
:   Return information about current crypto devices.

    Return:
    :   `[`[`QCryptodevInfo`](qemu-qmp-ref.md#object-QMP-cryptodev.QCryptodevInfo "QMP:cryptodev.QCryptodevInfo")`]`

## [CXL devices](qemu-qmp-ref.md#id45)

*Enum* CxlEventLog (Since: 8.1)
:   CXL has a number of separate event logs for different types of
    events. Each such event log is handled and signaled independently.

    Values:
    :   - **informational** – Information Event Log
        - **warning** – Warning Event Log
        - **failure** – Failure Event Log
        - **fatal** – Fatal Event Log

*Object* CXLCommonEventBase (Since: 8.1)
:   Common event base for a CXL Event (CXL r3.2 8.2.10.2.1
    Table 8-55 Common Event Record Format).

    Members:
    :   - **path** (`string`) – CXL type 3 device canonical QOM path
        - **log** ([`CxlEventLog`](qemu-qmp-ref.md#enum-QMP-cxl.CxlEventLog "QMP:cxl.CxlEventLog")) – event log to add the event to
        - **flags** (`int`) – Event Record Flags. See CXL r3.2 Table 8-55 Common Event
          Record Format, Event Record Flags for subfield definitions.
        - **maint-op-class** (`int`, *optional*) – Maintenance operation class the device requests to
          initiate.
        - **maint-op-subclass** (`int`, *optional*) – Maintenance operation subclass the device
          requests to initiate.
        - **ld-id** (`int`, *optional*) – Logical Device (LD) ID of LD from where the event
          originated.
        - **head-id** (`int`, *optional*) – ID of the device head from where the event originated.

*Object* CXLGeneralMediaEvent (Since: 8.1)
:   Event record for a General Media Event (CXL r3.2 8.2.10.2.1.1).

    Members:
    :   - **dpa** (`int`) – Device Physical Address (relative to `path` device). Note
          lower bits include some flags. See CXL r3.2 Table 8-57 General
          Media Event Record, Physical Address.
        - **descriptor** (`int`) – Memory Event Descriptor with additional memory event
          information. See CXL r3.2 Table 8-57 General Media Event
          Record, Memory Event Descriptor for bit definitions.
        - **type** (`int`) – Type of memory event that occurred. See CXL r3.2 Table 8-57
          General Media Event Record, Memory Event Type for possible
          values.
        - **transaction-type** (`int`) – Type of first transaction that caused the event
          to occur. See CXL r3-2 Table 8-57 General Media Event Record,
          Transaction Type for possible values.
        - **channel** (`int`, *optional*) – The channel of the memory event location. A channel is an
          interface that can be independently accessed for a transaction.
        - **rank** (`int`, *optional*) – The rank of the memory event location. A rank is a set of
          memory devices on a channel that together execute a transaction.
        - **device** (`int`, *optional*) – Bitmask that represents all devices in the rank associated
          with the memory event location.
        - **component-id** (`string`, *optional*) – Device specific component identifier for the event.
          May describe a field replaceable sub-component of the device.
        - **is-comp-id-pldm** (`boolean`, *optional*) – This flag specifies whether the device-specific
          component identifier format follows PLDM.
        - **cme-ev-flags** (`int`, *optional*) – Advanced programmable corrected memory error
          threshold event flags.
        - **cme-count** (`int`, *optional*) – Corrected memory error count at event.
        - **sub-type** (`int`) – Memory event sub-type.
        - The members of [`CXLCommonEventBase`](qemu-qmp-ref.md#object-QMP-cxl.CXLCommonEventBase "QMP:cxl.CXLCommonEventBase").

*Command* cxl-inject-general-media-event (Since: 8.1)
:   Inject an event record for a General Media Event (CXL r3.2
    8.2.10.2.1.1). This event type is reported via one of the event
    logs specified via the log parameter.

    Arguments:
    :   - The members of [`CXLGeneralMediaEvent`](qemu-qmp-ref.md#object-QMP-cxl.CXLGeneralMediaEvent "QMP:cxl.CXLGeneralMediaEvent").

*Object* CXLDRAMEvent (Since: 8.1)
:   Event record for a DRAM Event (CXL r3.2 8.2.10.2.1.2).

    Members:
    :   - **dpa** (`int`) – Device Physical Address (relative to `path` device). Note
          lower bits include some flags. See CXL r3.2 Table 8-58 DRAM
          Event Record, Physical Address.
        - **descriptor** (`int`) – Memory Event Descriptor with additional memory event
          information. See CXL r3.2 Table 8-58 DRAM Event Record, Memory
          Event Descriptor for bit definitions.
        - **type** (`int`) – Type of memory event that occurred. See CXL r3.2 Table 8-58
          DRAM Event Record, Memory Event Type for possible values.
        - **transaction-type** (`int`) – Type of first transaction that caused the event
          to occur. See CXL r3.2 Table 8-58 DRAM Event Record,
          Transaction Type for possible values.
        - **channel** (`int`, *optional*) – The channel of the memory event location. A channel is an
          interface that can be independently accessed for a transaction.
        - **rank** (`int`, *optional*) – The rank of the memory event location. A rank is a set of
          memory devices on a channel that together execute a transaction.
        - **nibble-mask** (`int`, *optional*) – Identifies one or more nibbles that the error affects
        - **bank-group** (`int`, *optional*) – Bank group of the memory event location, incorporating
          a number of banks.
        - **bank** (`int`, *optional*) – Bank of the memory event location. A single bank is accessed
          per read or write of the memory.
        - **row** (`int`, *optional*) – Row address within the DRAM.
        - **column** (`int`, *optional*) – Column address within the DRAM.
        - **correction-mask** (`[``int``]`, *optional*) – Bits within each nibble. Used in order of bits
          set in the nibble-mask. Up to 4 nibbles may be covered.
        - **component-id** (`string`, *optional*) – Device specific component identifier for the event.
          May describe a field replaceable sub-component of the device.
        - **is-comp-id-pldm** (`boolean`, *optional*) – This flag specifies whether the device-specific
          component identifier format follows PLDM.
        - **sub-channel** (`int`, *optional*) – The sub-channel of the memory event location.
        - **cme-ev-flags** (`int`, *optional*) – Advanced programmable corrected memory error
          threshold event flags.
        - **cvme-count** (`int`, *optional*) – Corrected volatile memory error count at event.
        - **sub-type** (`int`) – Memory event sub-type.
        - The members of [`CXLCommonEventBase`](qemu-qmp-ref.md#object-QMP-cxl.CXLCommonEventBase "QMP:cxl.CXLCommonEventBase").

*Command* cxl-inject-dram-event (Since: 8.1)
:   Inject an event record for a DRAM Event (CXL r3.2 8.2.10.2.1.2).
    This event type is reported via one of the event logs
    specified via the log parameter.

    Arguments:
    :   - The members of [`CXLDRAMEvent`](qemu-qmp-ref.md#object-QMP-cxl.CXLDRAMEvent "QMP:cxl.CXLDRAMEvent").

*Object* CXLMemModuleEvent (Since: 8.1)
:   Event record for a Memory Module Event (CXL r3.2 8.2.10.2.1.3).

    Members:
    :   - **type** (`int`) – Device Event Type. See CXL r3.2 Table 8-59 Memory Module
          Event Record for bit definitions for bit definiions.
        - **health-status** (`int`) – Overall health summary bitmap. See CXL r3.2 Table
          8-148 Get Health Info Output Payload, Health Status for bit
          definitions.
        - **media-status** (`int`) – Overall media health summary. See CXL r3.2 Table
          8-148 Get Health Info Output Payload, Media Status for bit
          definitions.
        - **additional-status** (`int`) – See CXL r3.2 Table 8-148 Get Health Info Output
          Payload, Additional Status for subfield definitions.
        - **life-used** (`int`) – Percentage (0-100) of factory expected life span.
        - **temperature** (`int`) – Device temperature in degrees Celsius.
        - **dirty-shutdown-count** (`int`) – Number of times the device has been unable to
          determine whether data loss may have occurred.
        - **corrected-volatile-error-count** (`int`) – Total number of correctable errors
          in volatile memory.
        - **corrected-persistent-error-count** (`int`) – Total number of correctable
          errors in persistent memory
        - **component-id** (`string`, *optional*) – Device specific component identifier for the event.
          May describe a field replaceable sub-component of the device.
        - **is-comp-id-pldm** (`boolean`, *optional*) – This flag specifies whether the device-specific
          component identifier format follows PLDM.
        - **sub-type** (`int`) – Device event sub-type.
        - The members of [`CXLCommonEventBase`](qemu-qmp-ref.md#object-QMP-cxl.CXLCommonEventBase "QMP:cxl.CXLCommonEventBase").

*Command* cxl-inject-memory-module-event (Since: 8.1)
:   Inject an event record for a Memory Module Event (CXL r3.2
    8.2.10.2.1.3). This event includes a copy of the Device Health info
    at the time of the event.

    Arguments:
    :   - The members of [`CXLMemModuleEvent`](qemu-qmp-ref.md#object-QMP-cxl.CXLMemModuleEvent "QMP:cxl.CXLMemModuleEvent").

*Command* cxl-inject-poison (Since: 8.1)
:   Poison records indicate that a CXL memory device knows that a
    particular memory region may be corrupted. This may be because of
    locally detected errors (e.g. ECC failure) or poisoned writes
    received from other components in the system. This injection
    mechanism enables testing of the OS handling of poison records which
    may be queried via the CXL mailbox.

    Arguments:
    :   - **path** (`string`) – CXL type 3 device canonical QOM path
        - **start** (`int`) – Start address; must be 64 byte aligned.
        - **length** (`int`) – Length of poison to inject; must be a multiple of 64 bytes.

*Enum* CxlUncorErrorType (Since: 8.0)
:   Type of uncorrectable CXL error to inject. These errors are
    reported via an AER uncorrectable internal error with additional
    information logged at the CXL device.

    Values:
    :   - **cache-data-parity** – Data error such as data parity or data ECC error
          CXL.cache
        - **cache-address-parity** – Address parity or other errors associated
          with the address field on CXL.cache
        - **cache-be-parity** – Byte enable parity or other byte enable errors on
          CXL.cache
        - **cache-data-ecc** – ECC error on CXL.cache
        - **mem-data-parity** – Data error such as data parity or data ECC error
          on CXL.mem
        - **mem-address-parity** – Address parity or other errors associated with
          the address field on CXL.mem
        - **mem-be-parity** – Byte enable parity or other byte enable errors on
          CXL.mem.
        - **mem-data-ecc** – Data ECC error on CXL.mem.
        - **reinit-threshold** – REINIT threshold hit.
        - **rsvd-encoding** – Received unrecognized encoding.
        - **poison-received** – Received poison from the peer.
        - **receiver-overflow** – Buffer overflows (first 3 bits of header log
          indicate which)
        - **internal** – Component specific error
        - **cxl-ide-tx** – Integrity and data encryption tx error.
        - **cxl-ide-rx** – Integrity and data encryption rx error.

*Object* CXLUncorErrorRecord (Since: 8.0)
:   Record of a single error including header log.

    Members:
    :   - **type** ([`CxlUncorErrorType`](qemu-qmp-ref.md#enum-QMP-cxl.CxlUncorErrorType "QMP:cxl.CxlUncorErrorType")) – Type of error
        - **header** (`[``int``]`) – 16 DWORD of header.

*Command* cxl-inject-uncorrectable-errors (Since: 8.0)
:   Command to allow injection of multiple errors in one go. This
    allows testing of multiple header log handling in the OS.

    Arguments:
    :   - **path** (`string`) – CXL Type 3 device canonical QOM path
        - **errors** (`[`[`CXLUncorErrorRecord`](qemu-qmp-ref.md#object-QMP-cxl.CXLUncorErrorRecord "QMP:cxl.CXLUncorErrorRecord")`]`) – Errors to inject

*Enum* CxlCorErrorType (Since: 8.0)
:   Type of CXL correctable error to inject

    Values:
    :   - **cache-data-ecc** – Data ECC error on CXL.cache
        - **mem-data-ecc** – Data ECC error on CXL.mem
        - **crc-threshold** – Component specific and applicable to 68 byte Flit
          mode only.
        - **retry-threshold** – Retry threshold hit in the Local Retry State
          Machine, 68B Flits only.
        - **cache-poison-received** – Received poison from a peer on CXL.cache.
        - **mem-poison-received** – Received poison from a peer on CXL.mem
        - **physical** – Received error indication from the physical layer.

*Command* cxl-inject-correctable-error (Since: 8.0)
:   Command to inject a single correctable error. Multiple error
    injection of this error type is not interesting as there is no
    associated header log. These errors are reported via AER as a
    correctable internal error, with additional detail available from
    the CXL device.

    Arguments:
    :   - **path** (`string`) – CXL Type 3 device canonical QOM path
        - **type** ([`CxlCorErrorType`](qemu-qmp-ref.md#enum-QMP-cxl.CxlCorErrorType "QMP:cxl.CxlCorErrorType")) – Type of error.

*Object* CxlDynamicCapacityExtent (Since: 9.1)
:   A single dynamic capacity extent. This is a contiguous allocation
    of memory by Device Physical Address within a single Dynamic
    Capacity Region on a CXL Type 3 Device.

    Members:
    :   - **offset** (`int`) – The offset (in bytes) to the start of the region where the
          extent belongs to.
        - **len** (`int`) – The length of the extent in bytes.

*Enum* CxlExtentSelectionPolicy (Since: 9.1)
:   The policy to use for selecting which extents comprise the added
    capacity, as defined in Compute Express Link (CXL) Specification,
    Revision 3.1, Table 7-70.

    Values:
    :   - **free** – Device is responsible for allocating the requested memory
          capacity and is free to do this using any combination of
          supported extents.
        - **contiguous** – Device is responsible for allocating the requested
          memory capacity but must do so as a single contiguous
          extent.
        - **prescriptive** – The precise set of extents to be allocated is
          specified by the command. Thus allocation is being managed
          by the issuer of the allocation command, not the device.
        - **enable-shared-access** – Capacity has already been allocated to a
          different host using free, contiguous or prescriptive policy
          with a known tag. This policy then instructs the device to make
          the capacity with the specified tag available to an additional
          host. Capacity is implicit as it matches that already
          associated with the tag. Note that the extent list (and hence
          Device Physical Addresses) used are per host, so a device may
          use different representations on each host. The ordering of the
          extents provided to each host is indicated to the host using per
          extent sequence numbers generated by the device. Has a similar
          meaning for temporal sharing, but in that case there may be only
          one host involved.

*Command* cxl-add-dynamic-capacity (Since: 9.1)
:   This command is unstable/experimental.

    Initiate adding dynamic capacity extents to a host. This simulates
    operations defined in Compute Express Link (CXL) Specification,
    Revision 3.1, Section 7.6.7.6.5. Note that, currently, establishing
    success or failure of the full Add Dynamic Capacity flow requires
    out of band communication with the OS of the CXL host.

    Arguments:
    :   - **path** (`string`) – path to the CXL Dynamic Capacity Device in the QOM tree.
        - **host-id** (`int`) – The “Host ID” field as defined in Compute Express Link
          (CXL) Specification, Revision 3.1, Table 7-70.
        - **selection-policy** ([`CxlExtentSelectionPolicy`](qemu-qmp-ref.md#enum-QMP-cxl.CxlExtentSelectionPolicy "QMP:cxl.CxlExtentSelectionPolicy")) – The “Selection Policy” bits as defined in
          Compute Express Link (CXL) Specification, Revision 3.1,
          Table 7-70. It specifies the policy to use for selecting
          which extents comprise the added capacity.
        - **region** (`int`) – The “Region Number” field as defined in Compute Express
          Link (CXL) Specification, Revision 3.1, Table 7-70. Valid
          range is from 0-7.
        - **tag** (`string`, *optional*) – The “Tag” field as defined in Compute Express Link (CXL)
          Specification, Revision 3.1, Table 7-70.
        - **extents** (`[`[`CxlDynamicCapacityExtent`](qemu-qmp-ref.md#object-QMP-cxl.CxlDynamicCapacityExtent "QMP:cxl.CxlDynamicCapacityExtent")`]`) – The “Extent List” field as defined in Compute Express Link
          (CXL) Specification, Revision 3.1, Table 7-70.

    Features:
    :   - **unstable** – For now this command is subject to change.

*Enum* CxlExtentRemovalPolicy (Since: 9.1)
:   The policy to use for selecting which extents comprise the released
    capacity, defined in the “Flags” field in Compute Express Link (CXL)
    Specification, Revision 3.1, Table 7-71.

    Values:
    :   - **tag-based** – Extents are selected by the device based on tag, with
          no requirement for contiguous extents.
        - **prescriptive** – Extent list of capacity to release is included in
          the request payload.

*Command* cxl-release-dynamic-capacity (Since: 9.1)
:   This command is unstable/experimental.

    Initiate release of dynamic capacity extents from a host. This
    simulates operations defined in Compute Express Link (CXL)
    Specification, Revision 3.1, Section 7.6.7.6.6. Note that,
    currently, success or failure of the full Release Dynamic Capacity
    flow requires out of band communication with the OS of the CXL host.

    Arguments:
    :   - **path** (`string`) – path to the CXL Dynamic Capacity Device in the QOM tree.
        - **host-id** (`int`) – The “Host ID” field as defined in Compute Express Link
          (CXL) Specification, Revision 3.1, Table 7-71.
        - **removal-policy** ([`CxlExtentRemovalPolicy`](qemu-qmp-ref.md#enum-QMP-cxl.CxlExtentRemovalPolicy "QMP:cxl.CxlExtentRemovalPolicy")) – Bit[3:0] of the “Flags” field as defined in
          Compute Express Link (CXL) Specification, Revision 3.1,
          Table 7-71.
        - **forced-removal** (`boolean`, *optional*) – Bit[4] of the “Flags” field in Compute Express
          Link (CXL) Specification, Revision 3.1, Table 7-71. When set,
          the device does not wait for a Release Dynamic Capacity command
          from the host. Instead, the host immediately looses access to
          the released capacity.
        - **sanitize-on-release** (`boolean`, *optional*) – Bit[5] of the “Flags” field in Compute Express
          Link (CXL) Specification, Revision 3.1, Table 7-71. When set,
          the device should sanitize all released capacity as a result of
          this request. This ensures that all user data and metadata is
          made permanently unavailable by whatever means is appropriate
          for the media type. Note that changing encryption keys is not
          sufficient.
        - **region** (`int`) – The “Region Number” field as defined in Compute Express
          Link Specification, Revision 3.1, Table 7-71. Valid range
          is from 0-7.
        - **tag** (`string`, *optional*) – The “Tag” field as defined in Compute Express Link (CXL)
          Specification, Revision 3.1, Table 7-71.
        - **extents** (`[`[`CxlDynamicCapacityExtent`](qemu-qmp-ref.md#object-QMP-cxl.CxlDynamicCapacityExtent "QMP:cxl.CxlDynamicCapacityExtent")`]`) – The “Extent List” field as defined in Compute Express
          Link (CXL) Specification, Revision 3.1, Table 7-71.

    Features:
    :   - **unstable** – For now this command is subject to change.

## [UEFI Variable Store](qemu-qmp-ref.md#id46)

The QEMU efi variable store implementation (hw/uefi/) uses this to
store non-volatile variables in json format on disk.

This is an existing format already supported by (at least) two other
projects, specifically <https://gitlab.com/kraxel/virt-firmware> and
<https://github.com/awslabs/python-uefivars>.

*Object* UefiVariable (Since: 10.0)
:   UEFI Variable. Check the UEFI specification for more detailed
    information on the fields.

    Members:
    :   - **guid** (`string`) – variable namespace GUID
        - **name** (`string`) – variable name, in UTF-8 encoding.
        - **attr** (`int`) – variable attributes.
        - **data** (`string`) – variable value, encoded as hex string.
        - **time** (`string`, *optional*) – variable modification time. EFI_TIME struct, encoded as hex
          string. Used only for authenticated variables, where the
          EFI_VARIABLE_TIME_BASED_AUTHENTICATED_WRITE_ACCESS attribute bit
          is set.
        - **digest** (`string`, *optional*) – variable certificate digest. Used to verify the signature
          of updates for authenticated variables. UEFI has two kinds of
          authenticated variables. The secure boot variables (‘PK’,
          ‘KEK’, ‘db’ and ‘dbx’) have hard coded signature checking rules.
          For other authenticated variables the firmware stores a digest
          of the signing certificate at variable creation time, and any
          updates must be signed with the same certificate.

*Object* UefiVarStore (Since: 10.0)
:   Members:
    :   - **version** (`int`) – currently always 2
        - **variables** (`[`[`UefiVariable`](qemu-qmp-ref.md#object-QMP-uefi.UefiVariable "QMP:uefi.UefiVariable")`]`) – list of UEFI variables
