---
collection: qemu
version: "11.1.0"
title: "D-Bus VNC"
source_url: https://www.qemu.org/docs/master/interop/dbus-vnc.html
fetched_at: 2026-08-21T03:22:07+00:00
---
# D-Bus VNC

The `qemu-vnc` standalone VNC server exposes a D-Bus interface for management
and monitoring of VNC connections.

The service is available on the bus under the well-known name `org.qemu.vnc`.
Objects are exported under `/org/qemu/Vnc1/`.

## org.qemu.Vnc1.Server interface

*interface* org.qemu.Vnc1.Server
:   This interface is implemented on `/org/qemu/Vnc1/Server`.
    It provides management and monitoring of the VNC server.

    *method* SetPassword(*s password*) → ()
    :   Arguments:
        :   - **password** (*s*) – The new VNC password.

        Change the VNC password. Existing clients are unaffected.

    *method* ExpirePassword(*s time*) → ()
    :   Arguments:
        :   - **time** (*s*) – Expiry specification.

        Set password expiry. Values: `"now"`, `"never"`,
        `"+N"` (seconds from now), `"N"` (absolute epoch seconds).

    *method* ReloadCertificates() → ()
    :   Reload TLS certificates from disk.

    *method* AddClient(*h socket*, *b skipauth*) → ()
    :   Arguments:
        :   - **socket** (*h*) – file descriptor of a connected socket.
            - **skipauth** (*b*) – whether to skip VNC authentication.

        Add a VNC client from an already-connected socket.

    *signal* ClientConnected(*o client*)
    :   Arguments:
        :   - **client** (*o*) – Object path of the new client.

        Emitted when a VNC client TCP connection is established
        (before authentication).

    *signal* ClientInitialized(*o client*)
    :   Arguments:
        :   - **client** (*o*) – Object path of the client.

        Emitted when a VNC client has completed authentication
        and is active.

    *signal* ClientDisconnected(*o client*)
    :   Arguments:
        :   - **client** (*o*) – Object path of the client.

        Emitted when a VNC client disconnects.

    *signal* Leaving(*s reason*)
    :   Arguments:
        :   - **reason** (*s*) –

              A human-readable reason for shutting down (e.g.

              ”D-Bus peer org.qemu vanished”).

        Emitted when the VNC server is shutting down cleanly.
        Clients should expect the connection to close shortly after.

    *property* Name:s
    :   Access:
        :   read-only

        Emits Changed:
        :   yes

        The VM name.

    *property* Auth:s
    :   Access:
        :   read-only

        Emits Changed:
        :   yes

        Primary authentication method (none, vnc, vencrypt, sasl, etc.).

    *property* VencryptSubAuth:s
    :   Access:
        :   read-only

        Emits Changed:
        :   yes

        VEncrypt sub-authentication method, if applicable.
        Empty string otherwise.

    *property* Clients:ao
    :   Access:
        :   read-only

        Emits Changed:
        :   yes

        Object paths of connected VNC clients.

    *property* Listeners:aa{sv}
    :   Access:
        :   read-only

        Emits Changed:
        :   yes

        List of listening sockets. Each entry is a dictionary with keys:
        `Host` (s), `Service` (s), `Family` (s),
        `WebSocket` (b), `Auth` (s), `VencryptSubAuth` (s).

## org.qemu.Vnc1.Client interface

*interface* org.qemu.Vnc1.Client
:   This interface is implemented on `/org/qemu/Vnc1/Client_$id`.
    It exposes information about a connected VNC client.

    *signal* ShutdownRequest()
    :   Emitted when the VNC client requests a guest shutdown.

    *signal* ResetRequest()
    :   Emitted when the VNC client requests a guest reset.

    *property* Host:s
    :   Access:
        :   read-only

        Emits Changed:
        :   yes

        Client IP address.

    *property* Service:s
    :   Access:
        :   read-only

        Emits Changed:
        :   yes

        Client port or service name. This may depend on the host system’s
        service database so symbolic names should not be relied on.

    *property* Family:s
    :   Access:
        :   read-only

        Emits Changed:
        :   yes

        Address family (ipv4, ipv6, unix).

    *property* WebSocket:b
    :   Access:
        :   read-only

        Emits Changed:
        :   yes

        Whether this is a WebSocket connection.

    *property* X509Dname:s
    :   Access:
        :   read-only

        Emits Changed:
        :   yes

        X.509 distinguished name (empty if not applicable).

    *property* SaslUsername:s
    :   Access:
        :   read-only

        Emits Changed:
        :   yes

        SASL username (empty if not applicable).
