---
collection: qemu
version: "11.1.0"
title: "QEMU Storage Daemon QMP Reference Manual"
source_url: https://www.qemu.org/docs/master/interop/qemu-storage-daemon-qmp-ref.html
fetched_at: 2026-08-21T03:22:24+00:00
---
# QEMU Storage Daemon QMP Reference Manual

- [Introduction](qemu-storage-daemon-qmp-ref.md#introduction)
- [Common data types](qemu-storage-daemon-qmp-ref.md#common-data-types)
- [Socket data types](qemu-storage-daemon-qmp-ref.md#socket-data-types)
- [Cryptography](qemu-storage-daemon-qmp-ref.md#cryptography)
- [Background jobs](qemu-storage-daemon-qmp-ref.md#background-jobs)
- [Block devices](qemu-storage-daemon-qmp-ref.md#block-devices)

  - [Block core (VM unrelated)](qemu-storage-daemon-qmp-ref.md#block-core-vm-unrelated)
  - [Block device exports](qemu-storage-daemon-qmp-ref.md#block-device-exports)
- [Character devices](qemu-storage-daemon-qmp-ref.md#character-devices)
- [User authorization](qemu-storage-daemon-qmp-ref.md#user-authorization)
- [Transactions](qemu-storage-daemon-qmp-ref.md#transactions)
- [QMP monitor control](qemu-storage-daemon-qmp-ref.md#qmp-monitor-control)
- [QMP introspection](qemu-storage-daemon-qmp-ref.md#qmp-introspection)
- [QEMU Object Model (QOM)](qemu-storage-daemon-qmp-ref.md#qemu-object-model-qom)

## [Introduction](qemu-storage-daemon-qmp-ref.md#id1)

This manual describes the commands and events supported by the QEMU
storage daemon QMP.

For locating a particular item, please see the [QSD Index](../qapi-qsd-index.md).

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

## [Common data types](qemu-storage-daemon-qmp-ref.md#id2)

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

## [Socket data types](qemu-storage-daemon-qmp-ref.md#id3)

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
        - The members of [`InetSocketAddressBase`](qemu-storage-daemon-qmp-ref.md#object-QSD-sockets.InetSocketAddressBase "QSD:sockets.InetSocketAddressBase").

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
    :   - **data** ([`InetSocketAddress`](qemu-storage-daemon-qmp-ref.md#object-QSD-sockets.InetSocketAddress "QSD:sockets.InetSocketAddress")) – internet domain socket address

*Object* UnixSocketAddressWrapper (Since: 1.3)
:   Members:
    :   - **data** ([`UnixSocketAddress`](qemu-storage-daemon-qmp-ref.md#object-QSD-sockets.UnixSocketAddress "QSD:sockets.UnixSocketAddress")) – UNIX domain socket address

*Object* VsockSocketAddressWrapper (Since: 2.8)
:   Members:
    :   - **data** ([`VsockSocketAddress`](qemu-storage-daemon-qmp-ref.md#object-QSD-sockets.VsockSocketAddress "QSD:sockets.VsockSocketAddress")) – VSOCK domain socket address

*Object* FdSocketAddressWrapper (Since: 1.3)
:   Members:
    :   - **data** ([`FdSocketAddress`](qemu-storage-daemon-qmp-ref.md#object-QSD-sockets.FdSocketAddress "QSD:sockets.FdSocketAddress")) – file descriptor name or number

*Object* SocketAddressLegacy (Since: 1.3)
:   Captures the address of a socket, which could also be a named file
    descriptor

    Members:
    :   - **type** ([`SocketAddressType`](qemu-storage-daemon-qmp-ref.md#enum-QSD-sockets.SocketAddressType "QSD:sockets.SocketAddressType")) – Transport type
        - When `type` is `inet`: The members of [`InetSocketAddressWrapper`](qemu-storage-daemon-qmp-ref.md#object-QSD-sockets.InetSocketAddressWrapper "QSD:sockets.InetSocketAddressWrapper").
        - When `type` is `unix`: The members of [`UnixSocketAddressWrapper`](qemu-storage-daemon-qmp-ref.md#object-QSD-sockets.UnixSocketAddressWrapper "QSD:sockets.UnixSocketAddressWrapper").
        - When `type` is `vsock`: The members of [`VsockSocketAddressWrapper`](qemu-storage-daemon-qmp-ref.md#object-QSD-sockets.VsockSocketAddressWrapper "QSD:sockets.VsockSocketAddressWrapper").
        - When `type` is `fd`: The members of [`FdSocketAddressWrapper`](qemu-storage-daemon-qmp-ref.md#object-QSD-sockets.FdSocketAddressWrapper "QSD:sockets.FdSocketAddressWrapper").

*Enum* SocketAddressType (Since: 2.9)
:   Available [`SocketAddress`](qemu-storage-daemon-qmp-ref.md#object-QSD-sockets.SocketAddress "QSD:sockets.SocketAddress") types

    Values:
    :   - **inet** – Internet address
        - **unix** – Unix domain socket
        - **vsock** – VMCI address
        - **fd** – Socket file descriptor

*Object* SocketAddress (Since: 2.9)
:   Captures the address of a socket, which could also be a socket file
    descriptor

    Members:
    :   - **type** ([`SocketAddressType`](qemu-storage-daemon-qmp-ref.md#enum-QSD-sockets.SocketAddressType "QSD:sockets.SocketAddressType")) – Transport type
        - When `type` is `inet`: The members of [`InetSocketAddress`](qemu-storage-daemon-qmp-ref.md#object-QSD-sockets.InetSocketAddress "QSD:sockets.InetSocketAddress").
        - When `type` is `unix`: The members of [`UnixSocketAddress`](qemu-storage-daemon-qmp-ref.md#object-QSD-sockets.UnixSocketAddress "QSD:sockets.UnixSocketAddress").
        - When `type` is `vsock`: The members of [`VsockSocketAddress`](qemu-storage-daemon-qmp-ref.md#object-QSD-sockets.VsockSocketAddress "QSD:sockets.VsockSocketAddress").
        - When `type` is `fd`: The members of [`FdSocketAddress`](qemu-storage-daemon-qmp-ref.md#object-QSD-sockets.FdSocketAddress "QSD:sockets.FdSocketAddress").

## [Cryptography](qemu-storage-daemon-qmp-ref.md#id4)

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
    :   - **format** ([`QCryptoBlockFormat`](qemu-storage-daemon-qmp-ref.md#enum-QSD-crypto.QCryptoBlockFormat "QSD:crypto.QCryptoBlockFormat")) – the encryption format

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
    :   - **cipher-alg** ([`QCryptoCipherAlgo`](qemu-storage-daemon-qmp-ref.md#enum-QSD-crypto.QCryptoCipherAlgo "QSD:crypto.QCryptoCipherAlgo"), *optional*) – the cipher algorithm for data encryption. Currently
          defaults to ‘aes-256’.
        - **cipher-mode** ([`QCryptoCipherMode`](qemu-storage-daemon-qmp-ref.md#enum-QSD-crypto.QCryptoCipherMode "QSD:crypto.QCryptoCipherMode"), *optional*) – the cipher mode for data encryption. Currently
          defaults to ‘xts’
        - **ivgen-alg** ([`QCryptoIVGenAlgo`](qemu-storage-daemon-qmp-ref.md#enum-QSD-crypto.QCryptoIVGenAlgo "QSD:crypto.QCryptoIVGenAlgo"), *optional*) – the initialization vector generator. Currently defaults
          to ‘plain64’
        - **ivgen-hash-alg** ([`QCryptoHashAlgo`](qemu-storage-daemon-qmp-ref.md#enum-QSD-crypto.QCryptoHashAlgo "QSD:crypto.QCryptoHashAlgo"), *optional*) – the initialization vector generator hash.
          Currently defaults to ‘sha256’
        - **hash-alg** ([`QCryptoHashAlgo`](qemu-storage-daemon-qmp-ref.md#enum-QSD-crypto.QCryptoHashAlgo "QSD:crypto.QCryptoHashAlgo"), *optional*) – the master key hash algorithm. Currently defaults to
          ‘sha256’
        - **iter-time** (`int`, *optional*) – number of milliseconds to spend in PBKDF passphrase
          processing. Currently defaults to 2000. (since 2.8)
        - The members of [`QCryptoBlockOptionsLUKS`](qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.QCryptoBlockOptionsLUKS "QSD:crypto.QCryptoBlockOptionsLUKS").

*Object* QCryptoBlockOpenOptions (Since: 2.6)
:   The options that are available for all encryption formats when
    opening an existing volume

    Members:
    :   - The members of [`QCryptoBlockOptionsBase`](qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.QCryptoBlockOptionsBase "QSD:crypto.QCryptoBlockOptionsBase").
        - When `format` is `qcow`: The members of [`QCryptoBlockOptionsQCow`](qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.QCryptoBlockOptionsQCow "QSD:crypto.QCryptoBlockOptionsQCow").
        - When `format` is `luks`: The members of [`QCryptoBlockOptionsLUKS`](qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.QCryptoBlockOptionsLUKS "QSD:crypto.QCryptoBlockOptionsLUKS").

*Object* QCryptoBlockCreateOptions (Since: 2.6)
:   The options that are available for all encryption formats when
    initializing a new volume

    Members:
    :   - The members of [`QCryptoBlockOptionsBase`](qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.QCryptoBlockOptionsBase "QSD:crypto.QCryptoBlockOptionsBase").
        - When `format` is `qcow`: The members of [`QCryptoBlockOptionsQCow`](qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.QCryptoBlockOptionsQCow "QSD:crypto.QCryptoBlockOptionsQCow").
        - When `format` is `luks`: The members of [`QCryptoBlockCreateOptionsLUKS`](qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.QCryptoBlockCreateOptionsLUKS "QSD:crypto.QCryptoBlockCreateOptionsLUKS").

*Object* QCryptoBlockInfoBase (Since: 2.7)
:   The common information that applies to all full disk encryption
    formats

    Members:
    :   - **format** ([`QCryptoBlockFormat`](qemu-storage-daemon-qmp-ref.md#enum-QSD-crypto.QCryptoBlockFormat "QSD:crypto.QCryptoBlockFormat")) – the encryption format

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
    :   - **cipher-alg** ([`QCryptoCipherAlgo`](qemu-storage-daemon-qmp-ref.md#enum-QSD-crypto.QCryptoCipherAlgo "QSD:crypto.QCryptoCipherAlgo")) – the cipher algorithm for data encryption
        - **cipher-mode** ([`QCryptoCipherMode`](qemu-storage-daemon-qmp-ref.md#enum-QSD-crypto.QCryptoCipherMode "QSD:crypto.QCryptoCipherMode")) – the cipher mode for data encryption
        - **ivgen-alg** ([`QCryptoIVGenAlgo`](qemu-storage-daemon-qmp-ref.md#enum-QSD-crypto.QCryptoIVGenAlgo "QSD:crypto.QCryptoIVGenAlgo")) – the initialization vector generator
        - **ivgen-hash-alg** ([`QCryptoHashAlgo`](qemu-storage-daemon-qmp-ref.md#enum-QSD-crypto.QCryptoHashAlgo "QSD:crypto.QCryptoHashAlgo"), *optional*) – the initialization vector generator hash
        - **hash-alg** ([`QCryptoHashAlgo`](qemu-storage-daemon-qmp-ref.md#enum-QSD-crypto.QCryptoHashAlgo "QSD:crypto.QCryptoHashAlgo")) – the master key hash algorithm
        - **detached-header** (`boolean`) – whether the LUKS header is detached (Since 9.0)
        - **payload-offset** (`int`) – offset to the payload data in bytes
        - **master-key-iters** (`int`) – number of PBKDF2 iterations for key material
        - **uuid** (`string`) – unique identifier for the volume
        - **slots** (`[`[`QCryptoBlockInfoLUKSSlot`](qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.QCryptoBlockInfoLUKSSlot "QSD:crypto.QCryptoBlockInfoLUKSSlot")`]`) – information about each key slot

*Object* QCryptoBlockInfo (Since: 2.7)
:   Information about the block encryption options

    Members:
    :   - The members of [`QCryptoBlockInfoBase`](qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.QCryptoBlockInfoBase "QSD:crypto.QCryptoBlockInfoBase").
        - When `format` is `luks`: The members of [`QCryptoBlockInfoLUKS`](qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.QCryptoBlockInfoLUKS "QSD:crypto.QCryptoBlockInfoLUKS").

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
    :   - **state** ([`QCryptoBlockLUKSKeyslotState`](qemu-storage-daemon-qmp-ref.md#enum-QSD-crypto.QCryptoBlockLUKSKeyslotState "QSD:crypto.QCryptoBlockLUKSKeyslotState")) – the desired state of the keyslots
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
    :   - The members of [`QCryptoBlockOptionsBase`](qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.QCryptoBlockOptionsBase "QSD:crypto.QCryptoBlockOptionsBase").
        - When `format` is `luks`: The members of [`QCryptoBlockAmendOptionsLUKS`](qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.QCryptoBlockAmendOptionsLUKS "QSD:crypto.QCryptoBlockAmendOptionsLUKS").

*Object* SecretCommonProperties (Since: 2.6)
:   Properties for objects of classes derived from secret-common.

    Members:
    :   - **format** ([`QCryptoSecretFormat`](qemu-storage-daemon-qmp-ref.md#enum-QSD-crypto.QCryptoSecretFormat "QSD:crypto.QCryptoSecretFormat"), *optional*) – the data format that the secret is provided in
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
        - The members of [`SecretCommonProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.SecretCommonProperties "QSD:crypto.SecretCommonProperties").

*Object* SecretKeyringProperties (Since: 5.1)
:   *Availability*: `CONFIG_SECRET_KEYRING`

    Properties for secret_keyring objects.

    Members:
    :   - **serial** (`int`) – serial number that identifies a key to get from the kernel
        - The members of [`SecretCommonProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.SecretCommonProperties "QSD:crypto.SecretCommonProperties").

*Object* TlsCredsProperties (Since: 2.5)
:   Properties for objects of classes derived from tls-creds.

    Members:
    :   - **verify-peer** (`boolean`, *optional*) – if true the peer credentials will be verified once the
          handshake is completed. This is a no-op for anonymous
          credentials. (default: true)
        - **dir** (`string`, *optional*) – the path of the directory that contains the credential files
        - **endpoint** ([`QCryptoTLSCredsEndpoint`](qemu-storage-daemon-qmp-ref.md#enum-QSD-crypto.QCryptoTLSCredsEndpoint "QSD:crypto.QCryptoTLSCredsEndpoint"), *optional*) – whether the QEMU network backend that uses the
          credentials will be acting as a client or as a server
          (default: client)
        - **priority** (`string`, *optional*) – a gnutls priority string as described at
          <https://gnutls.org/manual/html_node/Priority-Strings.html>

*Object* TlsCredsAnonProperties (Since: 2.5)
:   Properties for tls-creds-anon objects.

    Members:
    :   - The members of [`TlsCredsProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.TlsCredsProperties "QSD:crypto.TlsCredsProperties").

*Object* TlsCredsPskProperties (Since: 3.0)
:   Properties for tls-creds-psk objects.

    Members:
    :   - **username** (`string`, *optional*) – the username which will be sent to the server. For
          clients only. If absent, “qemu” is sent and the property will
          read back as an empty string.
        - The members of [`TlsCredsProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.TlsCredsProperties "QSD:crypto.TlsCredsProperties").

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
        - The members of [`TlsCredsProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.TlsCredsProperties "QSD:crypto.TlsCredsProperties").

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
    :   - **hash-alg** ([`QCryptoHashAlgo`](qemu-storage-daemon-qmp-ref.md#enum-QSD-crypto.QCryptoHashAlgo "QSD:crypto.QCryptoHashAlgo")) – [`QCryptoHashAlgo`](qemu-storage-daemon-qmp-ref.md#enum-QSD-crypto.QCryptoHashAlgo "QSD:crypto.QCryptoHashAlgo")
        - **padding-alg** ([`QCryptoRSAPaddingAlgo`](qemu-storage-daemon-qmp-ref.md#enum-QSD-crypto.QCryptoRSAPaddingAlgo "QSD:crypto.QCryptoRSAPaddingAlgo")) – [`QCryptoRSAPaddingAlgo`](qemu-storage-daemon-qmp-ref.md#enum-QSD-crypto.QCryptoRSAPaddingAlgo "QSD:crypto.QCryptoRSAPaddingAlgo")

*Object* QCryptoAkCipherOptions (Since: 7.1)
:   The options that are available for all asymmetric key algorithms
    when creating a new QCryptoAkCipher.

    Members:
    :   - **alg** ([`QCryptoAkCipherAlgo`](qemu-storage-daemon-qmp-ref.md#enum-QSD-crypto.QCryptoAkCipherAlgo "QSD:crypto.QCryptoAkCipherAlgo")) – encryption cipher algorithm
        - When `alg` is `rsa`: The members of [`QCryptoAkCipherOptionsRSA`](qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.QCryptoAkCipherOptionsRSA "QSD:crypto.QCryptoAkCipherOptionsRSA").

## [Background jobs](qemu-storage-daemon-qmp-ref.md#id5)

*Enum* JobType (Since: 1.7)
:   Type of a background job.

    Values:
    :   - **commit** – block commit job type, see [`block-commit`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.block-commit "QSD:block-core.block-commit")
        - **stream** – block stream job type, see [`block-stream`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.block-stream "QSD:block-core.block-stream")
        - **mirror** – drive mirror job type, see [`drive-mirror`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.drive-mirror "QSD:block-core.drive-mirror")
        - **backup** – drive backup job type, see [`drive-backup`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.drive-backup "QSD:block-core.drive-backup")
        - **create** – image creation job type, see [`blockdev-create`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.blockdev-create "QSD:block-core.blockdev-create") (since 3.0)
        - **amend** – image options amend job type, see [`x-blockdev-amend`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.x-blockdev-amend "QSD:block-core.x-blockdev-amend")
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
          require manual intervention via [`job-finalize`](qemu-storage-daemon-qmp-ref.md#command-QSD-job.job-finalize "QSD:job.job-finalize") if auto-finalize
          was set to false. These pending changes may still fail.
        - **aborting** – The job is in the process of being aborted, and will
          finish with an error. The job will afterwards report that it is
          `concluded`. This status may not be visible to the management
          process.
        - **concluded** – The job has finished all work. If auto-dismiss was set
          to false, the job will remain in this state until it is
          dismissed via [`job-dismiss`](qemu-storage-daemon-qmp-ref.md#command-QSD-job.job-dismiss "QSD:job.job-dismiss").
        - **null** – The job is in the process of being dismantled. This state
          should not ever be visible externally.

*Enum* JobVerb (Since: 2.12)
:   Represents command verbs that can be applied to a job.

    Values:
    :   - **cancel** – see [`job-cancel`](qemu-storage-daemon-qmp-ref.md#command-QSD-job.job-cancel "QSD:job.job-cancel")
        - **pause** – see [`job-pause`](qemu-storage-daemon-qmp-ref.md#command-QSD-job.job-pause "QSD:job.job-pause")
        - **resume** – see [`job-resume`](qemu-storage-daemon-qmp-ref.md#command-QSD-job.job-resume "QSD:job.job-resume")
        - **set-speed** – see [`block-job-set-speed`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.block-job-set-speed "QSD:block-core.block-job-set-speed")
        - **complete** – see [`job-complete`](qemu-storage-daemon-qmp-ref.md#command-QSD-job.job-complete "QSD:job.job-complete")
        - **dismiss** – see [`job-dismiss`](qemu-storage-daemon-qmp-ref.md#command-QSD-job.job-dismiss "QSD:job.job-dismiss")
        - **finalize** – see [`job-finalize`](qemu-storage-daemon-qmp-ref.md#command-QSD-job.job-finalize "QSD:job.job-finalize")
        - **change** – see [`block-job-change`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.block-job-change "QSD:block-core.block-job-change") (since 8.2)

*Event* JOB_STATUS_CHANGE (Since: 3.0)
:   Emitted when a job transitions to a different status.

    Members:
    :   - **id** (`string`) – The job identifier
        - **status** ([`JobStatus`](qemu-storage-daemon-qmp-ref.md#enum-QSD-job.JobStatus "QSD:job.JobStatus")) – The new job status

*Command* job-pause (Since: 3.0)
:   Pause an active job.

    This command returns immediately after marking the active job for
    pausing. Pausing an already paused job is an error.

    The job will pause as soon as possible, which means transitioning
    into the PAUSED state if it was RUNNING, or into STANDBY if it was
    READY. The corresponding [`JOB_STATUS_CHANGE`](qemu-storage-daemon-qmp-ref.md#event-QSD-job.JOB_STATUS_CHANGE "QSD:job.JOB_STATUS_CHANGE") event will be emitted.

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
    [`JOB_STATUS_CHANGE`](qemu-storage-daemon-qmp-ref.md#event-QSD-job.JOB_STATUS_CHANGE "QSD:job.JOB_STATUS_CHANGE") event. Usually, the status will change to
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
    mirroring includes [`drive-mirror`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.drive-mirror "QSD:block-core.drive-mirror"), [`blockdev-mirror`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.blockdev-mirror "QSD:block-core.blockdev-mirror") and
    [`block-commit`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.block-commit "QSD:block-core.block-commit") job (only in case of “active commit”, when the node
    being committed is used by the guest). The ability to complete is
    signaled with a [`BLOCK_JOB_READY`](qemu-storage-daemon-qmp-ref.md#event-QSD-block-core.BLOCK_JOB_READY "QSD:block-core.BLOCK_JOB_READY") event.

    This command completes an active background block operation
    synchronously. The ordering of this command’s return with the
    [`BLOCK_JOB_COMPLETED`](qemu-storage-daemon-qmp-ref.md#event-QSD-block-core.BLOCK_JOB_COMPLETED "QSD:block-core.BLOCK_JOB_COMPLETED") event is not defined. Note that if an I/O
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
    jobs that have `auto-dismiss` option, which are [`drive-backup`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.drive-backup "QSD:block-core.drive-backup"),
    [`blockdev-backup`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.blockdev-backup "QSD:block-core.blockdev-backup"), [`drive-mirror`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.drive-mirror "QSD:block-core.drive-mirror"), [`blockdev-mirror`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.blockdev-mirror "QSD:block-core.blockdev-mirror"), [`block-commit`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.block-commit "QSD:block-core.block-commit")
    and [`block-stream`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.block-stream "QSD:block-core.block-stream"). `auto-dismiss` is enabled by default for these
    jobs.

    This command will refuse to operate on any job that has not yet
    reached its terminal state, CONCLUDED. For jobs that make use of
    the JOB_READY event, [`job-cancel`](qemu-storage-daemon-qmp-ref.md#command-QSD-job.job-cancel "QSD:job.job-cancel") or [`job-complete`](qemu-storage-daemon-qmp-ref.md#command-QSD-job.job-complete "QSD:job.job-complete") will still need
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
        - **type** ([`JobType`](qemu-storage-daemon-qmp-ref.md#enum-QSD-job.JobType "QSD:job.JobType")) – The kind of job that is being performed
        - **status** ([`JobStatus`](qemu-storage-daemon-qmp-ref.md#enum-QSD-job.JobStatus "QSD:job.JobStatus")) – Current job state/status
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
    :   `[`[`JobInfo`](qemu-storage-daemon-qmp-ref.md#object-QSD-job.JobInfo "QSD:job.JobInfo")`]` – a list with info for each active job

## [Block devices](qemu-storage-daemon-qmp-ref.md#id6)

### [Block core (VM unrelated)](qemu-storage-daemon-qmp-ref.md#id7)

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
    :   - **format** ([`BlockdevQcow2EncryptionFormat`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockdevQcow2EncryptionFormat "QSD:block-core.BlockdevQcow2EncryptionFormat")) – The encryption format

*Object* ImageInfoSpecificQCow2Encryption (Since: 2.10)
:   Members:
    :   - The members of [`ImageInfoSpecificQCow2EncryptionBase`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.ImageInfoSpecificQCow2EncryptionBase "QSD:block-core.ImageInfoSpecificQCow2EncryptionBase").
        - When `format` is `luks`: The members of [`QCryptoBlockInfoLUKS`](qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.QCryptoBlockInfoLUKS "QSD:crypto.QCryptoBlockInfoLUKS").

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
        - **encrypt** ([`ImageInfoSpecificQCow2Encryption`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.ImageInfoSpecificQCow2Encryption "QSD:block-core.ImageInfoSpecificQCow2Encryption"), *optional*) – details about encryption parameters; only set if image is
          encrypted (since 2.10)
        - **bitmaps** (`[`[`Qcow2BitmapInfo`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.Qcow2BitmapInfo "QSD:block-core.Qcow2BitmapInfo")`]`, *optional*) – A list of qcow2 bitmap details (since 4.0)
        - **compression-type** ([`Qcow2CompressionType`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.Qcow2CompressionType "QSD:block-core.Qcow2CompressionType")) – the image cluster compression method (since 5.1)

*Object* ImageInfoSpecificVmdk (Since: 1.7)
:   Members:
    :   - **create-type** (`string`) – The create type of VMDK image
        - **cid** (`int`) – Content id of image
        - **parent-cid** (`int`) – Parent VMDK image’s cid
        - **extents** (`[`[`VmdkExtentInfo`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.VmdkExtentInfo "QSD:block-core.VmdkExtentInfo")`]`) – List of extent files

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
    :   - **encryption-format** ([`RbdImageEncryptionFormat`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.RbdImageEncryptionFormat "QSD:block-core.RbdImageEncryptionFormat"), *optional*) – Image encryption format. If encryption is
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
    :   - **data** ([`ImageInfoSpecificQCow2`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.ImageInfoSpecificQCow2 "QSD:block-core.ImageInfoSpecificQCow2")) – image information specific to QCOW2

*Object* ImageInfoSpecificVmdkWrapper (Since: 6.1)
:   Members:
    :   - **data** ([`ImageInfoSpecificVmdk`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.ImageInfoSpecificVmdk "QSD:block-core.ImageInfoSpecificVmdk")) – image information specific to VMDK

*Object* ImageInfoSpecificLUKSWrapper (Since: 2.7)
:   Members:
    :   - **data** ([`QCryptoBlockInfoLUKS`](qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.QCryptoBlockInfoLUKS "QSD:crypto.QCryptoBlockInfoLUKS")) – image information specific to LUKS

*Object* ImageInfoSpecificRbdWrapper (Since: 6.1)
:   Members:
    :   - **data** ([`ImageInfoSpecificRbd`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.ImageInfoSpecificRbd "QSD:block-core.ImageInfoSpecificRbd")) – image information specific to RBD

*Object* ImageInfoSpecificFileWrapper (Since: 8.0)
:   Members:
    :   - **data** ([`ImageInfoSpecificFile`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.ImageInfoSpecificFile "QSD:block-core.ImageInfoSpecificFile")) – image information specific to files

*Object* ImageInfoSpecific (Since: 1.7)
:   A discriminated record of image format specific information
    structures.

    Members:
    :   - **type** ([`ImageInfoSpecificKind`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.ImageInfoSpecificKind "QSD:block-core.ImageInfoSpecificKind")) – block driver name
        - When `type` is `qcow2`: The members of [`ImageInfoSpecificQCow2Wrapper`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.ImageInfoSpecificQCow2Wrapper "QSD:block-core.ImageInfoSpecificQCow2Wrapper").
        - When `type` is `vmdk`: The members of [`ImageInfoSpecificVmdkWrapper`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.ImageInfoSpecificVmdkWrapper "QSD:block-core.ImageInfoSpecificVmdkWrapper").
        - When `type` is `luks`: The members of [`ImageInfoSpecificLUKSWrapper`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.ImageInfoSpecificLUKSWrapper "QSD:block-core.ImageInfoSpecificLUKSWrapper").
        - When `type` is `rbd`: The members of [`ImageInfoSpecificRbdWrapper`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.ImageInfoSpecificRbdWrapper "QSD:block-core.ImageInfoSpecificRbdWrapper").
        - When `type` is `file`: The members of [`ImageInfoSpecificFileWrapper`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.ImageInfoSpecificFileWrapper "QSD:block-core.ImageInfoSpecificFileWrapper").

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
        - **snapshots** (`[`[`SnapshotInfo`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.SnapshotInfo "QSD:block-core.SnapshotInfo")`]`, *optional*) – list of VM snapshots
        - **limits** ([`BlockLimitsInfo`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockLimitsInfo "QSD:block-core.BlockLimitsInfo"), *optional*) – block limits that are used for I/O on the node (Since 10.2)
        - **format-specific** ([`ImageInfoSpecific`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.ImageInfoSpecific "QSD:block-core.ImageInfoSpecific"), *optional*) – structure supplying additional format-specific
          information (since 1.7)

*Object* ImageInfo (Since: 1.3)
:   Information about a QEMU image file, and potentially its backing
    image

    Members:
    :   - **backing-image** ([`ImageInfo`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.ImageInfo "QSD:block-core.ImageInfo"), *optional*) – info of the backing image
        - The members of [`BlockNodeInfo`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockNodeInfo "QSD:block-core.BlockNodeInfo").

*Object* BlockChildInfo (Since: 8.0)
:   Information about all nodes in the block graph starting at some
    node, annotated with information about that node in relation to its
    parent.

    Members:
    :   - **name** (`string`) – Child name of the root node in the [`BlockGraphInfo`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockGraphInfo "QSD:block-core.BlockGraphInfo") struct,
          in its role as the child of some undescribed parent node
        - **info** ([`BlockGraphInfo`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockGraphInfo "QSD:block-core.BlockGraphInfo")) – Block graph information starting at this node

*Object* BlockGraphInfo (Since: 8.0)
:   Information about all nodes in a block (sub)graph in the form of
    [`BlockNodeInfo`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockNodeInfo "QSD:block-core.BlockNodeInfo") data. The base [`BlockNodeInfo`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockNodeInfo "QSD:block-core.BlockNodeInfo") struct contains the
    information for the (sub)graph’s root node.

    Members:
    :   - **children** (`[`[`BlockChildInfo`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockChildInfo "QSD:block-core.BlockChildInfo")`]`) – Array of links to this node’s child nodes’ information
        - The members of [`BlockNodeInfo`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockNodeInfo "QSD:block-core.BlockNodeInfo").

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
        - **children** (`[`[`BlockdevChild`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevChild "QSD:block-core.BlockdevChild")`]`) – Information about child block nodes. (since: 10.1)
        - **active** (`boolean`) – true if the backend is active; typical cases for inactive
          backends are on the migration source instance after migration
          completes and on the destination before it completes.
          (since: 10.0)
        - **encrypted** (`boolean`) – true if the backing device is encrypted
        - **detect_zeroes** ([`BlockdevDetectZeroesOptions`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockdevDetectZeroesOptions "QSD:block-core.BlockdevDetectZeroesOptions")) – detect and optimize zero writes (Since 2.1)
        - **bps** (`int`) – total throughput limit in bytes per second is specified
        - **bps_rd** (`int`) – read throughput limit in bytes per second is specified
        - **bps_wr** (`int`) – write throughput limit in bytes per second is specified
        - **iops** (`int`) – total I/O operations per second is specified
        - **iops_rd** (`int`) – read I/O operations per second is specified
        - **iops_wr** (`int`) – write I/O operations per second is specified
        - **image** ([`ImageInfo`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.ImageInfo "QSD:block-core.ImageInfo")) – the info of image used (since: 1.6)
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
        - **cache** ([`BlockdevCacheInfo`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevCacheInfo "QSD:block-core.BlockdevCacheInfo")) – the cache mode used for the block device (since: 2.3)
        - **write_threshold** (`int`) – configured write threshold for the device. 0 if
          disabled. (Since 2.3)
        - **dirty-bitmaps** (`[`[`BlockDirtyInfo`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockDirtyInfo "QSD:block-core.BlockDirtyInfo")`]`, *optional*) – dirty bitmaps information (only present if node has
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
          it, use [`block-dirty-bitmap-remove`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.block-dirty-bitmap-remove "QSD:block-core.block-dirty-bitmap-remove"). (Since 4.0)

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
        - **flags** (`[`[`Qcow2BitmapInfoFlags`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.Qcow2BitmapInfoFlags "QSD:block-core.Qcow2BitmapInfoFlags")`]`) – flags of the bitmap

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
        - **io-status** ([`BlockDeviceIoStatus`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockDeviceIoStatus "QSD:block-core.BlockDeviceIoStatus"), *optional*) – [`BlockDeviceIoStatus`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockDeviceIoStatus "QSD:block-core.BlockDeviceIoStatus"). Only present if the device
          supports it and the VM is configured to stop on errors
          (supported device models: virtio-blk, IDE, SCSI except
          scsi-generic)
        - **inserted** ([`BlockDeviceInfo`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockDeviceInfo "QSD:block-core.BlockDeviceInfo"), *optional*) – [`BlockDeviceInfo`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockDeviceInfo "QSD:block-core.BlockDeviceInfo") describing the device if media is
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
:   Get a list of [`BlockInfo`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockInfo "QSD:block-core.BlockInfo") for all virtual block devices.

    Arguments:
    :   - **flat** (`boolean`, *optional*) – Omit nested data about the backing image, i.e. [`BlockInfo`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockInfo "QSD:block-core.BlockInfo")
          member ‘inserted.image.backing-image’ will be absent.
          Default is false. (Since 11.0)

    Return:
    :   `[`[`BlockInfo`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockInfo "QSD:block-core.BlockInfo")`]` – a list describing each virtual block device. Filter nodes
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
        - **timed_stats** (`[`[`BlockDeviceTimedStats`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockDeviceTimedStats "QSD:block-core.BlockDeviceTimedStats")`]`) – Statistics specific to the set of previously defined
          intervals of time (Since 2.5)
        - **rd_latency_histogram** ([`BlockLatencyHistogramInfo`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockLatencyHistogramInfo "QSD:block-core.BlockLatencyHistogramInfo"), *optional*) – [`BlockLatencyHistogramInfo`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockLatencyHistogramInfo "QSD:block-core.BlockLatencyHistogramInfo"). (Since 4.0)
        - **wr_latency_histogram** ([`BlockLatencyHistogramInfo`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockLatencyHistogramInfo "QSD:block-core.BlockLatencyHistogramInfo"), *optional*) – [`BlockLatencyHistogramInfo`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockLatencyHistogramInfo "QSD:block-core.BlockLatencyHistogramInfo"). (Since 4.0)
        - **zone_append_latency_histogram** ([`BlockLatencyHistogramInfo`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockLatencyHistogramInfo "QSD:block-core.BlockLatencyHistogramInfo"), *optional*) – [`BlockLatencyHistogramInfo`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockLatencyHistogramInfo "QSD:block-core.BlockLatencyHistogramInfo").
          (since 8.1)
        - **flush_latency_histogram** ([`BlockLatencyHistogramInfo`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockLatencyHistogramInfo "QSD:block-core.BlockLatencyHistogramInfo"), *optional*) – [`BlockLatencyHistogramInfo`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockLatencyHistogramInfo "QSD:block-core.BlockLatencyHistogramInfo"). (Since 4.0)

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
    :   - **driver** ([`BlockdevDriver`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockdevDriver "QSD:block-core.BlockdevDriver")) – block driver name
        - When `driver` is `file`: The members of [`BlockStatsSpecificFile`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockStatsSpecificFile "QSD:block-core.BlockStatsSpecificFile").
        - When `driver` is `host_device`: The members of [`BlockStatsSpecificFile`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockStatsSpecificFile "QSD:block-core.BlockStatsSpecificFile").
        - When `driver` is `nvme`: The members of [`BlockStatsSpecificNvme`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockStatsSpecificNvme "QSD:block-core.BlockStatsSpecificNvme").

*Object* BlockStats (Since: 0.14)
:   Statistics of a virtual block device or a block backing device.

    Members:
    :   - **device** (`string`, *optional*) – If the stats are for a virtual block device, the name
          corresponding to the virtual block device.
        - **node-name** (`string`, *optional*) – The node name of the device. (Since 2.3)
        - **qdev** (`string`, *optional*) – The qdev ID, or if no ID is assigned, the QOM path of the
          block device. (since 3.0)
        - **stats** ([`BlockDeviceStats`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockDeviceStats "QSD:block-core.BlockDeviceStats")) – A [`BlockDeviceStats`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockDeviceStats "QSD:block-core.BlockDeviceStats") for the device.
        - **driver-specific** ([`BlockStatsSpecific`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockStatsSpecific "QSD:block-core.BlockStatsSpecific"), *optional*) – Optional driver-specific stats. (Since 4.2)
        - **parent** ([`BlockStats`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockStats "QSD:block-core.BlockStats"), *optional*) – This describes the file block device if it has one.
          Contains recursively the statistics of the underlying protocol
          (e.g. the host file for a qcow2 image). If there is no
          underlying protocol, this field is omitted
        - **backing** ([`BlockStats`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockStats "QSD:block-core.BlockStats"), *optional*) – This describes the backing block device if it has one.
          (Since 2.0)

*Command* query-blockstats (Since: 0.14)
:   Query the [`BlockStats`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockStats "QSD:block-core.BlockStats") for all virtual block devices.

    Arguments:
    :   - **query-nodes** (`boolean`, *optional*) – If true, the command will query all the block nodes
          that have a node name, in a list which will include “parent”
          information, but not “backing”. If false or omitted, the
          behavior is as before - query all the device backends,
          recursively including their “parent” and “backing”. Filter
          nodes that were created implicitly are skipped over in this
          mode. (Since 2.3)

    Return:
    :   `[`[`BlockStats`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockStats "QSD:block-core.BlockStats")`]` – A list of statistics for each virtual block device.

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
        - **ignore** – ignore the error, only report a QMP event ([`BLOCK_IO_ERROR`](qemu-storage-daemon-qmp-ref.md#event-QSD-block-core.BLOCK_IO_ERROR "QSD:block-core.BLOCK_IO_ERROR")
          or [`BLOCK_JOB_ERROR`](qemu-storage-daemon-qmp-ref.md#event-QSD-block-core.BLOCK_JOB_ERROR "QSD:block-core.BLOCK_JOB_ERROR")). The backup, mirror and commit block jobs
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
          completion is determined by the [`BitmapSyncMode`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BitmapSyncMode "QSD:block-core.BitmapSyncMode"). (since: 4.2)

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
    :   - **type** ([`JobType`](qemu-storage-daemon-qmp-ref.md#enum-QSD-job.JobType "QSD:job.JobType")) – the job type (‘stream’ for image streaming)
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
        - **io-status** ([`BlockDeviceIoStatus`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockDeviceIoStatus "QSD:block-core.BlockDeviceIoStatus")) – the status of the job (since 1.3)
        - **ready** (`boolean`) – true if the job may be completed (since 2.2)
        - **status** ([`JobStatus`](qemu-storage-daemon-qmp-ref.md#enum-QSD-job.JobStatus "QSD:job.JobStatus")) – Current job state/status (since 2.12)
        - **auto-finalize** (`boolean`) – Job will finalize itself when PENDING, moving to the
          CONCLUDED state. (since 2.12)
        - **auto-dismiss** (`boolean`) – Job will dismiss itself when CONCLUDED, and
          disappear. (since 2.12)
        - **error** (`string`, *optional*) – Error information if the job did not complete successfully.
          Not set if the job completed successfully. (since 2.12.1)
        - When `type` is `mirror`: The members of [`BlockJobInfoMirror`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockJobInfoMirror "QSD:block-core.BlockJobInfoMirror").

*Command* query-block-jobs (Since: 1.1)
:   Return information about long-running block device operations.

    Return:
    :   `[`[`BlockJobInfo`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockJobInfo "QSD:block-core.BlockJobInfo")`]` – a list of job info for each active block job

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
        - **mode** ([`NewImageMode`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.NewImageMode "QSD:block-core.NewImageMode"), *optional*) – whether and how QEMU should create a new image, default is
          ‘absolute-paths’.

*Object* BlockdevSnapshot (Since: 2.5)
:   Members:
    :   - **node** (`string`) – device or node name that will have a snapshot taken.
        - **overlay** (`string`) – reference to the existing block device that will become
          the overlay of `node`, as part of taking the snapshot. It must
          not have a current backing file (this can be achieved by passing
          “backing”: null to [`blockdev-add`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.blockdev-add "QSD:block-core.blockdev-add")).

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
        - **sync** ([`MirrorSyncMode`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.MirrorSyncMode "QSD:block-core.MirrorSyncMode")) – what parts of the disk image should be copied to the
          destination (all the disk, only the sectors allocated in the
          topmost image, from a dirty bitmap, or only new I/O).
        - **speed** (`int`, *optional*) – the maximum speed, in bytes per second. The default is 0,
          for unlimited.
        - **bitmap** (`string`, *optional*) – The name of a dirty bitmap to use. Must be present if sync
          is “bitmap” or “incremental”. Can be present if sync is “full”
          or “top”. Must not be present otherwise.
          (Since 2.4 ([`drive-backup`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.drive-backup "QSD:block-core.drive-backup")), 3.1 ([`blockdev-backup`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.blockdev-backup "QSD:block-core.blockdev-backup")))
        - **bitmap-mode** ([`BitmapSyncMode`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BitmapSyncMode "QSD:block-core.BitmapSyncMode"), *optional*) – Specifies the type of data the bitmap should contain
          after the operation concludes. Must be present if a bitmap was
          provided, must **not** be present otherwise. (Since 4.2)
        - **compress** (`boolean`, *optional*) – true to compress data, if the target format supports it.
          (default: false) (since 2.8)
        - **on-source-error** ([`BlockdevOnError`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockdevOnError "QSD:block-core.BlockdevOnError"), *optional*) – the action to take on an error on the source,
          default ‘report’. ‘stop’ and ‘enospc’ can only be used if the
          block device supports io-status (see [`BlockInfo`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockInfo "QSD:block-core.BlockInfo")).
        - **on-target-error** ([`BlockdevOnError`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockdevOnError "QSD:block-core.BlockdevOnError"), *optional*) – the action to take on an error on the target,
          default ‘report’ (no limitations, since this applies to a
          different block device than `device`).
        - **on-cbw-error** ([`OnCbwError`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.OnCbwError "QSD:block-core.OnCbwError"), *optional*) – policy defining behavior on I/O errors in
          copy-before-write jobs; defaults to break-guest-write.
          (Since 10.1)
        - **auto-finalize** (`boolean`, *optional*) – When false, this job will wait in a PENDING state
          after it has finished its work, waiting for [`job-finalize`](qemu-storage-daemon-qmp-ref.md#command-QSD-job.job-finalize "QSD:job.job-finalize")
          before making any block graph changes. When true, this job will
          automatically perform its abort or commit actions. Defaults to
          true. (Since 2.12)
        - **auto-dismiss** (`boolean`, *optional*) – When false, this job will wait in a CONCLUDED state
          after it has completely ceased all work, and awaits
          [`job-dismiss`](qemu-storage-daemon-qmp-ref.md#command-QSD-job.job-dismiss "QSD:job.job-dismiss"). When true, this job will automatically disappear
          without user intervention. Defaults to true. (Since 2.12)
        - **filter-node-name** (`string`, *optional*) – the node name that should be assigned to the
          filter driver that the backup job inserts into the graph above
          node specified by `drive`. If this option is not given, a node
          name is autogenerated. (Since: 4.2)
        - **discard-source** (`boolean`, *optional*) – Discard blocks on source which have already been
          copied to the target. (Since 9.1)
        - **x-perf** ([`BackupPerf`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BackupPerf "QSD:block-core.BackupPerf"), *optional*) – Performance options. (Since 6.0)

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
        - **mode** ([`NewImageMode`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.NewImageMode "QSD:block-core.NewImageMode"), *optional*) – whether and how QEMU should create a new image, default is
          ‘absolute-paths’.
        - The members of [`BackupCommon`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BackupCommon "QSD:block-core.BackupCommon").

*Object* BlockdevBackup (Since: 2.3)
:   Members:
    :   - **target** (`string`) – the device name or node-name of the backup target node.
        - The members of [`BackupCommon`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BackupCommon "QSD:block-core.BackupCommon").

*Command* blockdev-snapshot-sync (Since: 0.14)
:   Takes a synchronous snapshot of a block device.

    Arguments:
    :   - The members of [`BlockdevSnapshotSync`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevSnapshotSync "QSD:block-core.BlockdevSnapshotSync").

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
    :   - The members of [`BlockdevSnapshot`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevSnapshot "QSD:block-core.BlockdevSnapshot").

    Features:
    :   - **allow-write-only-overlay** – If present, the check whether this
          operation is safe was relaxed so that it can be used to change
          backing file of a destination of a [`blockdev-mirror`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.blockdev-mirror "QSD:block-core.blockdev-mirror").
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
    itself. The user needs to complete the job with the [`job-complete`](qemu-storage-daemon-qmp-ref.md#command-QSD-job.job-complete "QSD:job.job-complete")
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
        - **on-error** ([`BlockdevOnError`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockdevOnError "QSD:block-core.BlockdevOnError"), *optional*) – the action to take on an error. ‘ignore’ means that the
          request should be retried. (default: report; since: 5.0)
        - **filter-node-name** (`string`, *optional*) – the node name that should be assigned to the
          filter driver that the commit job inserts into the graph above
          `top`. If this option is not given, a node name is
          autogenerated. (Since: 2.9)
        - **auto-finalize** (`boolean`, *optional*) – When false, this job will wait in a PENDING state
          after it has finished its work, waiting for [`job-finalize`](qemu-storage-daemon-qmp-ref.md#command-QSD-job.job-finalize "QSD:job.job-finalize")
          before making any block graph changes. When true, this job will
          automatically perform its abort or commit actions. Defaults to
          true. (Since 3.1)
        - **auto-dismiss** (`boolean`, *optional*) – When false, this job will wait in a CONCLUDED state
          after it has completely ceased all work, and awaits
          [`job-dismiss`](qemu-storage-daemon-qmp-ref.md#command-QSD-job.job-dismiss "QSD:job.job-dismiss"). When true, this job will automatically disappear
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
    The status of ongoing [`drive-backup`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.drive-backup "QSD:block-core.drive-backup") operations can be checked with
    [`query-block-jobs`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.query-block-jobs "QSD:block-core.query-block-jobs") where the [`BlockJobInfo`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockJobInfo "QSD:block-core.BlockJobInfo").type field has the value
    ‘backup’. The operation can be stopped before it has completed
    using the [`job-cancel`](qemu-storage-daemon-qmp-ref.md#command-QSD-job.job-cancel "QSD:job.job-cancel") or [`block-job-cancel`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.block-job-cancel "QSD:block-core.block-job-cancel") command.

    Arguments:
    :   - The members of [`DriveBackup`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.DriveBackup "QSD:block-core.DriveBackup").

    Features:
    :   - **deprecated** – This command is deprecated. Use [`blockdev-backup`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.blockdev-backup "QSD:block-core.blockdev-backup")
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
    The status of ongoing [`blockdev-backup`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.blockdev-backup "QSD:block-core.blockdev-backup") operations can be checked
    with [`query-block-jobs`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.query-block-jobs "QSD:block-core.query-block-jobs") where the [`BlockJobInfo`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockJobInfo "QSD:block-core.BlockJobInfo").type field has the
    value ‘backup’. The operation can be stopped before it has
    completed using the [`job-cancel`](qemu-storage-daemon-qmp-ref.md#command-QSD-job.job-cancel "QSD:job.job-cancel") or [`block-job-cancel`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.block-job-cancel "QSD:block-core.block-job-cancel") command.

    Arguments:
    :   - The members of [`BlockdevBackup`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevBackup "QSD:block-core.BlockdevBackup").

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
    :   `[`[`BlockDeviceInfo`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockDeviceInfo "QSD:block-core.BlockDeviceInfo")`]`

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
          [`x-debug-query-block-graph`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.x-debug-query-block-graph "QSD:block-core.x-debug-query-block-graph") and does not relate to any other
          identifiers in QEMU.
        - **type** ([`XDbgBlockGraphNodeType`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.XDbgBlockGraphNodeType "QSD:block-core.XDbgBlockGraphNodeType")) – Type of graph node. Can be one of block-backend, block-job
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
:   Block Graph edge description for [`x-debug-query-block-graph`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.x-debug-query-block-graph "QSD:block-core.x-debug-query-block-graph").

    Members:
    :   - **parent** (`int`) – parent id
        - **child** (`int`) – child id
        - **name** (`string`) – name of the relation (examples are ‘file’ and ‘backing’)
        - **perm** (`[`[`BlockPermission`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockPermission "QSD:block-core.BlockPermission")`]`) – granted permissions for the parent operating on the child
        - **shared-perm** (`[`[`BlockPermission`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockPermission "QSD:block-core.BlockPermission")`]`) – permissions that can still be granted to other users
          of the child while it is still attached to this parent

*Object* XDbgBlockGraph (Since: 4.0)
:   Block Graph - list of nodes and list of edges.

    Members:
    :   - **nodes** (`[`[`XDbgBlockGraphNode`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.XDbgBlockGraphNode "QSD:block-core.XDbgBlockGraphNode")`]`) – Not documented
        - **edges** (`[`[`XDbgBlockGraphEdge`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.XDbgBlockGraphEdge "QSD:block-core.XDbgBlockGraphEdge")`]`) – Not documented

*Command* x-debug-query-block-graph (Since: 4.0)
:   This command is unstable/experimental.

    Get the block graph.

    Return:
    :   [`XDbgBlockGraph`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.XDbgBlockGraph "QSD:block-core.XDbgBlockGraph")

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
    :   - The members of [`DriveMirror`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.DriveMirror "QSD:block-core.DriveMirror").

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
        - **mode** ([`NewImageMode`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.NewImageMode "QSD:block-core.NewImageMode"), *optional*) – whether and how QEMU should create a new image, default is
          ‘absolute-paths’.
        - **speed** (`int`, *optional*) – the maximum speed, in bytes per second
        - **sync** ([`MirrorSyncMode`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.MirrorSyncMode "QSD:block-core.MirrorSyncMode")) – what parts of the disk image should be copied to the
          destination (all the disk, only the sectors allocated in the
          topmost image, or only new I/O).
        - **granularity** (`int`, *optional*) – granularity of the dirty bitmap, default is 64K if the
          image format doesn’t have clusters, 4K if the clusters are
          smaller than that, else the cluster size. Must be a power of 2
          between 512 and 64M (since 1.4).
        - **buf-size** (`int`, *optional*) – maximum amount of data in flight from source to target
          (since 1.4).
        - **on-source-error** ([`BlockdevOnError`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockdevOnError "QSD:block-core.BlockdevOnError"), *optional*) – the action to take on an error on the source,
          default ‘report’. ‘stop’ and ‘enospc’ can only be used if the
          block device supports io-status (see [`BlockInfo`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockInfo "QSD:block-core.BlockInfo")).
        - **on-target-error** ([`BlockdevOnError`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockdevOnError "QSD:block-core.BlockdevOnError"), *optional*) – the action to take on an error on the target,
          default ‘report’ (no limitations, since this applies to a
          different block device than `device`).
        - **unmap** (`boolean`, *optional*) – Whether to try to unmap target sectors where source has only
          zero. If true, and target unallocated sectors will read as
          zero, target image sectors will be unmapped; otherwise, zeroes
          will be written. Both will result in identical contents.
          Default is true. (Since 2.4)
        - **copy-mode** ([`MirrorCopyMode`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.MirrorCopyMode "QSD:block-core.MirrorCopyMode"), *optional*) – when to copy data to the destination; defaults to
          ‘background’ (Since: 3.0)
        - **auto-finalize** (`boolean`, *optional*) – When false, this job will wait in a PENDING state
          after it has finished its work, waiting for [`job-finalize`](qemu-storage-daemon-qmp-ref.md#command-QSD-job.job-finalize "QSD:job.job-finalize")
          before making any block graph changes. When true, this job will
          automatically perform its abort or commit actions. Defaults to
          true. (Since 3.1)
        - **auto-dismiss** (`boolean`, *optional*) – When false, this job will wait in a CONCLUDED state
          after it has completely ceased all work, and awaits
          [`job-dismiss`](qemu-storage-daemon-qmp-ref.md#command-QSD-job.job-dismiss "QSD:job.job-dismiss"). When true, this job will automatically disappear
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
          [`block-dirty-bitmap-add`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.block-dirty-bitmap-add "QSD:block-core.block-dirty-bitmap-add")
        - **persistent** (`boolean`, *optional*) – the bitmap is persistent, i.e. it will be saved to the
          corresponding block device image file on its close. For now
          only Qcow2 disks support persistent bitmaps. Default is false
          for [`block-dirty-bitmap-add`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.block-dirty-bitmap-add "QSD:block-core.block-dirty-bitmap-add"). This fails if the node is
          read-only or inactive, since such a bitmap could never be
          stored. (Since: 2.10)
        - **disabled** (`boolean`, *optional*) – the bitmap is created in the disabled state, which means
          that it will not track drive changes. The bitmap may be enabled
          with [`block-dirty-bitmap-enable`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.block-dirty-bitmap-enable "QSD:block-core.block-dirty-bitmap-enable"). Default is false.
          (Since: 4.0)

*Alternate* BlockDirtyBitmapOrStr (Since: 4.1)
:   Alternatives:
    :   - **local** (`string`) – name of the bitmap, attached to the same node as target
          bitmap.
        - **external** ([`BlockDirtyBitmap`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockDirtyBitmap "QSD:block-core.BlockDirtyBitmap")) – bitmap with specified node

*Object* BlockDirtyBitmapMerge (Since: 4.0)
:   Members:
    :   - **node** (`string`) – name of device/node which the `target` bitmap is tracking
        - **target** (`string`) – name of the destination dirty bitmap
        - **bitmaps** (`[`[`BlockDirtyBitmapOrStr`](qemu-storage-daemon-qmp-ref.md#alternate-QSD-block-core.BlockDirtyBitmapOrStr "QSD:block-core.BlockDirtyBitmapOrStr")`]`) – name(s) of the source dirty bitmap(s) at `node` and/or
          fully specified [`BlockDirtyBitmap`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockDirtyBitmap "QSD:block-core.BlockDirtyBitmap") elements. The latter are
          supported since 4.1.

*Command* block-dirty-bitmap-add (Since: 2.4)
:   Create a dirty bitmap with a name on the node, and start tracking
    the writes.

    Arguments:
    :   - The members of [`BlockDirtyBitmapAdd`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockDirtyBitmapAdd "QSD:block-core.BlockDirtyBitmapAdd").

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
    with [`block-dirty-bitmap-add`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.block-dirty-bitmap-add "QSD:block-core.block-dirty-bitmap-add"). If the bitmap is persistent, remove
    it from its storage too.

    Arguments:
    :   - The members of [`BlockDirtyBitmap`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockDirtyBitmap "QSD:block-core.BlockDirtyBitmap").

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
    :   - The members of [`BlockDirtyBitmap`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockDirtyBitmap "QSD:block-core.BlockDirtyBitmap").

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
    :   - The members of [`BlockDirtyBitmap`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockDirtyBitmap "QSD:block-core.BlockDirtyBitmap").

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
    :   - The members of [`BlockDirtyBitmap`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockDirtyBitmap "QSD:block-core.BlockDirtyBitmap").

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
    :   - The members of [`BlockDirtyBitmapMerge`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockDirtyBitmapMerge "QSD:block-core.BlockDirtyBitmapMerge").

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
    :   - The members of [`BlockDirtyBitmap`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockDirtyBitmap "QSD:block-core.BlockDirtyBitmap").

    Features:
    :   - **unstable** – This command is meant for debugging.

    Return:
    :   [`BlockDirtyBitmapSha256`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockDirtyBitmapSha256 "QSD:block-core.BlockDirtyBitmapSha256")

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
        - **sync** ([`MirrorSyncMode`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.MirrorSyncMode "QSD:block-core.MirrorSyncMode")) – what parts of the disk image should be copied to the
          destination (all the disk, only the sectors allocated in the
          topmost image, or only new I/O).
        - **granularity** (`int`, *optional*) – granularity of the dirty bitmap, default is 64K if the
          image format doesn’t have clusters, 4K if the clusters are
          smaller than that, else the cluster size. Must be a power of 2
          between 512 and 64M
        - **buf-size** (`int`, *optional*) – maximum amount of data in flight from source to target
        - **on-source-error** ([`BlockdevOnError`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockdevOnError "QSD:block-core.BlockdevOnError"), *optional*) – the action to take on an error on the source,
          default ‘report’. ‘stop’ and ‘enospc’ can only be used if the
          block device supports io-status (see [`BlockInfo`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockInfo "QSD:block-core.BlockInfo")).
        - **on-target-error** ([`BlockdevOnError`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockdevOnError "QSD:block-core.BlockdevOnError"), *optional*) – the action to take on an error on the target,
          default ‘report’ (no limitations, since this applies to a
          different block device than `device`).
        - **filter-node-name** (`string`, *optional*) – the node name that should be assigned to the
          filter driver that the mirror job inserts into the graph above
          `device`. If this option is not given, a node name is
          autogenerated. (Since: 2.9)
        - **copy-mode** ([`MirrorCopyMode`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.MirrorCopyMode "QSD:block-core.MirrorCopyMode"), *optional*) – when to copy data to the destination; defaults to
          ‘background’ (Since: 3.0)
        - **auto-finalize** (`boolean`, *optional*) – When false, this job will wait in a PENDING state
          after it has finished its work, waiting for [`job-finalize`](qemu-storage-daemon-qmp-ref.md#command-QSD-job.job-finalize "QSD:job.job-finalize")
          before making any block graph changes. When true, this job will
          automatically perform its abort or commit actions. Defaults to
          true. (Since 3.1)
        - **auto-dismiss** (`boolean`, *optional*) – When false, this job will wait in a CONCLUDED state
          after it has completely ceased all work, and awaits
          [`job-dismiss`](qemu-storage-daemon-qmp-ref.md#command-QSD-job.job-dismiss "QSD:job.job-dismiss"). When true, this job will automatically disappear
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
    :   - **limits** ([`ThrottleLimits`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.ThrottleLimits "QSD:block-core.ThrottleLimits"), *optional*) – limits to apply for this throttle group
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
    streaming operations can be checked with [`query-block-jobs`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.query-block-jobs "QSD:block-core.query-block-jobs"). The
    operation can be stopped before it has completed using the
    [`job-cancel`](qemu-storage-daemon-qmp-ref.md#command-QSD-job.job-cancel "QSD:job.job-cancel") or [`block-job-cancel`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.block-job-cancel "QSD:block-core.block-job-cancel") command.

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
    backing file and the [`BLOCK_JOB_COMPLETED`](qemu-storage-daemon-qmp-ref.md#event-QSD-block-core.BLOCK_JOB_COMPLETED "QSD:block-core.BLOCK_JOB_COMPLETED") event is emitted.

    In case `device` is a filter node, [`block-stream`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.block-stream "QSD:block-core.block-stream") modifies the first
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
        - **on-error** ([`BlockdevOnError`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockdevOnError "QSD:block-core.BlockdevOnError"), *optional*) – the action to take on an error (default report). ‘stop’
          and ‘enospc’ can only be used if the block device supports
          io-status (see [`BlockInfo`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockInfo "QSD:block-core.BlockInfo")). (Since 1.3)
        - **filter-node-name** (`string`, *optional*) – the node name that should be assigned to the
          filter driver that the stream job inserts into the graph above
          `device`. If this option is not given, a node name is
          autogenerated. (Since: 6.0)
        - **auto-finalize** (`boolean`, *optional*) – When false, this job will wait in a PENDING state
          after it has finished its work, waiting for [`job-finalize`](qemu-storage-daemon-qmp-ref.md#command-QSD-job.job-finalize "QSD:job.job-finalize")
          before making any block graph changes. When true, this job will
          automatically perform its abort or commit actions. Defaults to
          true. (Since 3.1)
        - **auto-dismiss** (`boolean`, *optional*) – When false, this job will wait in a CONCLUDED state
          after it has completely ceased all work, and awaits
          [`job-dismiss`](qemu-storage-daemon-qmp-ref.md#command-QSD-job.job-dismiss "QSD:job.job-dismiss"). When true, this job will automatically disappear
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
    [`BLOCK_JOB_CANCELLED`](qemu-storage-daemon-qmp-ref.md#event-QSD-block-core.BLOCK_JOB_CANCELLED "QSD:block-core.BLOCK_JOB_CANCELLED") event. Before that happens the job is still
    visible when enumerated using [`query-block-jobs`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.query-block-jobs "QSD:block-core.query-block-jobs").

    Note that if you issue [`block-job-cancel`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.block-job-cancel "QSD:block-core.block-job-cancel") after [`drive-mirror`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.drive-mirror "QSD:block-core.drive-mirror") has
    indicated (via the event [`BLOCK_JOB_READY`](qemu-storage-daemon-qmp-ref.md#event-QSD-block-core.BLOCK_JOB_READY "QSD:block-core.BLOCK_JOB_READY")) that the source and
    destination are synchronized, then the event triggered by this
    command changes to [`BLOCK_JOB_COMPLETED`](qemu-storage-daemon-qmp-ref.md#event-QSD-block-core.BLOCK_JOB_COMPLETED "QSD:block-core.BLOCK_JOB_COMPLETED"), to indicate that the
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
          [`BLOCK_JOB_READY`](qemu-storage-daemon-qmp-ref.md#event-QSD-block-core.BLOCK_JOB_READY "QSD:block-core.BLOCK_JOB_READY"), abandon the job immediately (even if it is
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
    READY. The corresponding [`JOB_STATUS_CHANGE`](qemu-storage-daemon-qmp-ref.md#event-QSD-job.JOB_STATUS_CHANGE "QSD:job.JOB_STATUS_CHANGE") event will be emitted.

    Cancelling a paused job automatically resumes it.

    Arguments:
    :   - **device** (`string`) – The job identifier. This used to be a device name (hence
          the name of the parameter), but since QEMU 2.7 it can have other
          values.

    Features:
    :   - **deprecated** – This command is deprecated. Use [`job-pause`](qemu-storage-daemon-qmp-ref.md#command-QSD-job.job-pause "QSD:job.job-pause")
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
    :   - **deprecated** – This command is deprecated. Use [`job-resume`](qemu-storage-daemon-qmp-ref.md#command-QSD-job.job-resume "QSD:job.job-resume")
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
    mirroring includes [`drive-mirror`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.drive-mirror "QSD:block-core.drive-mirror"), [`blockdev-mirror`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.blockdev-mirror "QSD:block-core.blockdev-mirror") and
    [`block-commit`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.block-commit "QSD:block-core.block-commit") job (only in case of “active commit”, when the node
    being committed is used by the guest). The ability to complete is
    signaled with a [`BLOCK_JOB_READY`](qemu-storage-daemon-qmp-ref.md#event-QSD-block-core.BLOCK_JOB_READY "QSD:block-core.BLOCK_JOB_READY") event.

    This command completes an active background block operation
    synchronously. The ordering of this command’s return with the
    [`BLOCK_JOB_COMPLETED`](qemu-storage-daemon-qmp-ref.md#event-QSD-block-core.BLOCK_JOB_COMPLETED "QSD:block-core.BLOCK_JOB_COMPLETED") event is not defined. Note that if an I/O
    error occurs during the processing of this command: 1) the command
    itself will fail; 2) the error will be processed according to the
    rerror/werror arguments that were specified when starting the
    operation.

    Arguments:
    :   - **device** (`string`) – The job identifier. This used to be a device name (hence
          the name of the parameter), but since QEMU 2.7 it can have other
          values.

    Features:
    :   - **deprecated** – This command is deprecated. Use [`job-complete`](qemu-storage-daemon-qmp-ref.md#command-QSD-job.job-complete "QSD:job.job-complete")
          instead.

    Errors:
    :   - If no background operation is active on this device,
          DeviceNotActive

*Command* block-job-dismiss (Since: 2.12)
:   This command is deprecated.

    Deletes a job that is in the CONCLUDED state. This command only
    needs to be run explicitly for jobs that don’t have automatic
    dismiss enabled. In turn, automatic dismiss may be enabled only for
    jobs that have `auto-dismiss` option, which are [`drive-backup`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.drive-backup "QSD:block-core.drive-backup"),
    [`blockdev-backup`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.blockdev-backup "QSD:block-core.blockdev-backup"), [`drive-mirror`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.drive-mirror "QSD:block-core.drive-mirror"), [`blockdev-mirror`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.blockdev-mirror "QSD:block-core.blockdev-mirror"), [`block-commit`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.block-commit "QSD:block-core.block-commit")
    and [`block-stream`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.block-stream "QSD:block-core.block-stream"). `auto-dismiss` is enabled by default for these
    jobs.

    This command will refuse to operate on any job that has not yet
    reached its terminal state, CONCLUDED. For jobs that make use of
    the [`BLOCK_JOB_READY`](qemu-storage-daemon-qmp-ref.md#event-QSD-block-core.BLOCK_JOB_READY "QSD:block-core.BLOCK_JOB_READY") event, [`job-cancel`](qemu-storage-daemon-qmp-ref.md#command-QSD-job.job-cancel "QSD:job.job-cancel"), [`block-job-cancel`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.block-job-cancel "QSD:block-core.block-job-cancel") or
    [`job-complete`](qemu-storage-daemon-qmp-ref.md#command-QSD-job.job-complete "QSD:job.job-complete") will still need to be used as appropriate.

    Arguments:
    :   - **id** (`string`) – The job identifier.

    Features:
    :   - **deprecated** – This command is deprecated. Use [`job-dismiss`](qemu-storage-daemon-qmp-ref.md#command-QSD-job.job-dismiss "QSD:job.job-dismiss")
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
    :   - **deprecated** – This command is deprecated. Use [`job-finalize`](qemu-storage-daemon-qmp-ref.md#command-QSD-job.job-finalize "QSD:job.job-finalize")
          instead.

*Object* BlockJobChangeOptionsMirror (Since: 8.2)
:   Members:
    :   - **copy-mode** ([`MirrorCopyMode`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.MirrorCopyMode "QSD:block-core.MirrorCopyMode")) – Switch to this copy mode. Currently, only the switch
          from ‘background’ to ‘write-blocking’ is implemented.

*Object* BlockJobChangeOptions (Since: 8.2)
:   Block job options that can be changed after job creation.

    Members:
    :   - **id** (`string`) – The job identifier
        - **type** ([`JobType`](qemu-storage-daemon-qmp-ref.md#enum-QSD-job.JobType "QSD:job.JobType")) – The job type
        - When `type` is `mirror`: The members of [`BlockJobChangeOptionsMirror`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockJobChangeOptionsMirror "QSD:block-core.BlockJobChangeOptionsMirror").

*Command* block-job-change (Since: 8.2)
:   Change the block job’s options.

    Arguments:
    :   - The members of [`BlockJobChangeOptions`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockJobChangeOptions "QSD:block-core.BlockJobChangeOptions").

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
          requires also that [`BlockdevDiscardOptions`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockdevDiscardOptions "QSD:block-core.BlockdevDiscardOptions") is set to unmap for
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
        - **aio** ([`BlockdevAioOptions`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockdevAioOptions "QSD:block-core.BlockdevAioOptions"), *optional*) – AIO backend (default: threads) (since: 2.8)
        - **aio-max-batch** (`int`, *optional*) – maximum number of requests to batch together into a
          single submission in the AIO backend. The smallest value
          between this and the aio-max-batch value of the IOThread object
          is chosen. 0 means that the AIO backend will handle it
          automatically. (default: 0, since 6.2)
        - **locking** ([`OnOffAuto`](qemu-storage-daemon-qmp-ref.md#enum-QSD-common.OnOffAuto "QSD:common.OnOffAuto"), *optional*) – whether to enable file locking. If set to ‘auto’, only
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
    :   - **file** ([`BlockdevRef`](qemu-storage-daemon-qmp-ref.md#alternate-QSD-block-core.BlockdevRef "QSD:block-core.BlockdevRef")) – reference to or definition of the data source block device

*Object* BlockdevOptionsLUKS (Since: 2.9)
:   Driver specific block device options for LUKS.

    Members:
    :   - **key-secret** (`string`, *optional*) – the ID of a QCryptoSecret object providing the
          decryption key. Mandatory except when doing a metadata-only
          probe of the image. (since 2.6)
        - **header** ([`BlockdevRef`](qemu-storage-daemon-qmp-ref.md#alternate-QSD-block-core.BlockdevRef "QSD:block-core.BlockdevRef"), *optional*) – block device holding a detached LUKS header. (since 9.0)
        - The members of [`BlockdevOptionsGenericFormat`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsGenericFormat "QSD:block-core.BlockdevOptionsGenericFormat").

*Object* BlockdevOptionsGenericCOWFormat (Since: 2.9)
:   Driver specific block device options for image format that have no
    option besides their data source and an optional backing file.

    Members:
    :   - **backing** ([`BlockdevRefOrNull`](qemu-storage-daemon-qmp-ref.md#alternate-QSD-block-core.BlockdevRefOrNull "QSD:block-core.BlockdevRefOrNull"), *optional*) – reference to or definition of the backing file block
          device, null disables the backing file entirely. Defaults to
          the backing file stored the image file.
        - The members of [`BlockdevOptionsGenericFormat`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsGenericFormat "QSD:block-core.BlockdevOptionsGenericFormat").

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
    :   - **template** ([`Qcow2OverlapCheckMode`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.Qcow2OverlapCheckMode "QSD:block-core.Qcow2OverlapCheckMode"), *optional*) – Specifies a template mode which can be adjusted using the
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
    :   - **flags** ([`Qcow2OverlapCheckFlags`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.Qcow2OverlapCheckFlags "QSD:block-core.Qcow2OverlapCheckFlags")) – set of flags for separate specification of each metadata
          structure type
        - **mode** ([`Qcow2OverlapCheckMode`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.Qcow2OverlapCheckMode "QSD:block-core.Qcow2OverlapCheckMode")) – named mode which chooses a specific set of flags

*Enum* BlockdevQcowEncryptionFormat (Since: 2.10)
:   Values:
    :   - **aes** – AES-CBC with plain64 initialization vectors

*Object* BlockdevQcowEncryption (Since: 2.10)
:   Members:
    :   - **format** ([`BlockdevQcowEncryptionFormat`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockdevQcowEncryptionFormat "QSD:block-core.BlockdevQcowEncryptionFormat")) – encryption format
        - When `format` is `aes`: The members of [`QCryptoBlockOptionsQCow`](qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.QCryptoBlockOptionsQCow "QSD:crypto.QCryptoBlockOptionsQCow").

*Object* BlockdevOptionsQcow (Since: 2.10)
:   Driver specific block device options for qcow.

    Members:
    :   - **encrypt** ([`BlockdevQcowEncryption`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevQcowEncryption "QSD:block-core.BlockdevQcowEncryption"), *optional*) – Image decryption options. Mandatory for encrypted images,
          except when doing a metadata-only probe of the image.
        - The members of [`BlockdevOptionsGenericCOWFormat`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsGenericCOWFormat "QSD:block-core.BlockdevOptionsGenericCOWFormat").

*Enum* BlockdevQcow2EncryptionFormat (Since: 2.10)
:   Values:
    :   - **aes** – AES-CBC with plain64 initialization vectors
        - **luks** – Not documented

*Object* BlockdevQcow2Encryption (Since: 2.10)
:   Members:
    :   - **format** ([`BlockdevQcow2EncryptionFormat`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockdevQcow2EncryptionFormat "QSD:block-core.BlockdevQcow2EncryptionFormat")) – encryption format
        - When `format` is `aes`: The members of [`QCryptoBlockOptionsQCow`](qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.QCryptoBlockOptionsQCow "QSD:crypto.QCryptoBlockOptionsQCow").
        - When `format` is `luks`: The members of [`QCryptoBlockOptionsLUKS`](qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.QCryptoBlockOptionsLUKS "QSD:crypto.QCryptoBlockOptionsLUKS").

*Object* BlockdevOptionsPreallocate (Since: 6.0)
:   Filter driver intended to be inserted between format and protocol
    node and do preallocation in protocol node on write.

    Members:
    :   - **prealloc-align** (`int`, *optional*) – on preallocation, align file length to this number,
          default 1048576 (1M)
        - **prealloc-size** (`int`, *optional*) – how much to preallocate, default 134217728 (128M)
        - The members of [`BlockdevOptionsGenericFormat`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsGenericFormat "QSD:block-core.BlockdevOptionsGenericFormat").

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
        - **overlap-check** ([`Qcow2OverlapChecks`](qemu-storage-daemon-qmp-ref.md#alternate-QSD-block-core.Qcow2OverlapChecks "QSD:block-core.Qcow2OverlapChecks"), *optional*) – which overlap checks to perform for writes to the
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
        - **encrypt** ([`BlockdevQcow2Encryption`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevQcow2Encryption "QSD:block-core.BlockdevQcow2Encryption"), *optional*) – Image decryption options. Mandatory for encrypted images,
          except when doing a metadata-only probe of the image.
          (since 2.10)
        - **data-file** ([`BlockdevRef`](qemu-storage-daemon-qmp-ref.md#alternate-QSD-block-core.BlockdevRef "QSD:block-core.BlockdevRef"), *optional*) – reference to or definition of the external data file.
          This may only be specified for images that require an external
          data file. If it is not specified for such an image, the data
          file name is loaded from the image file. (since 4.0)
        - The members of [`BlockdevOptionsGenericCOWFormat`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsGenericCOWFormat "QSD:block-core.BlockdevOptionsGenericCOWFormat").

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
    :   - **type** ([`SshHostKeyCheckHashType`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.SshHostKeyCheckHashType "QSD:block-core.SshHostKeyCheckHashType")) – The hash algorithm used for the hash
        - **hash** (`string`) – The expected hash value

*Object* SshHostKeyCheck (Since: 2.12)
:   Members:
    :   - **mode** ([`SshHostKeyCheckMode`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.SshHostKeyCheckMode "QSD:block-core.SshHostKeyCheckMode")) – How to check the host key
        - When `mode` is `hash`: The members of [`SshHostKeyHash`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.SshHostKeyHash "QSD:block-core.SshHostKeyHash").

*Object* BlockdevOptionsSsh (Since: 2.9)
:   Members:
    :   - **server** ([`InetSocketAddress`](qemu-storage-daemon-qmp-ref.md#object-QSD-sockets.InetSocketAddress "QSD:sockets.InetSocketAddress")) – host address
        - **path** (`string`) – path to the image on the host
        - **user** (`string`, *optional*) – user as which to connect, defaults to current local user name
        - **host-key-check** ([`SshHostKeyCheck`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.SshHostKeyCheck "QSD:block-core.SshHostKeyCheck"), *optional*) – Defines how and what to check the host key against
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
    :   - **event** ([`BlkdebugEvent`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlkdebugEvent "QSD:block-core.BlkdebugEvent")) – trigger event
        - **state** (`int`, *optional*) – the state identifier blkdebug needs to be in to actually
          trigger the event; defaults to “any”
        - **iotype** ([`BlkdebugIOType`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlkdebugIOType "QSD:block-core.BlkdebugIOType"), *optional*) – the type of I/O operations on which this error should be
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
    :   - **event** ([`BlkdebugEvent`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlkdebugEvent "QSD:block-core.BlkdebugEvent")) – trigger event
        - **state** (`int`, *optional*) – the current state identifier blkdebug needs to be in;
          defaults to “any”
        - **new_state** (`int`) – the state identifier blkdebug is supposed to assume if
          this event is triggered

*Object* BlockdevOptionsBlkdebug (Since: 2.9)
:   Driver specific block device options for blkdebug.

    Members:
    :   - **image** ([`BlockdevRef`](qemu-storage-daemon-qmp-ref.md#alternate-QSD-block-core.BlockdevRef "QSD:block-core.BlockdevRef")) – underlying raw block device (or image file)
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
        - **inject-error** (`[`[`BlkdebugInjectErrorOptions`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlkdebugInjectErrorOptions "QSD:block-core.BlkdebugInjectErrorOptions")`]`, *optional*) – array of error injection descriptions
        - **set-state** (`[`[`BlkdebugSetStateOptions`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlkdebugSetStateOptions "QSD:block-core.BlkdebugSetStateOptions")`]`, *optional*) – array of state-change descriptions
        - **take-child-perms** (`[`[`BlockPermission`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockPermission "QSD:block-core.BlockPermission")`]`, *optional*) – Permissions to take on `image` in addition to what
          is necessary anyway (which depends on how the blkdebug node is
          used). Defaults to none. (since 5.0)
        - **unshare-child-perms** (`[`[`BlockPermission`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockPermission "QSD:block-core.BlockPermission")`]`, *optional*) – Permissions not to share on `image` in addition
          to what cannot be shared anyway (which depends on how the
          blkdebug node is used). Defaults to none. (since 5.0)

*Object* BlockdevOptionsBlklogwrites (Since: 3.0)
:   Driver specific block device options for blklogwrites.

    Members:
    :   - **file** ([`BlockdevRef`](qemu-storage-daemon-qmp-ref.md#alternate-QSD-block-core.BlockdevRef "QSD:block-core.BlockdevRef")) – block device
        - **log** ([`BlockdevRef`](qemu-storage-daemon-qmp-ref.md#alternate-QSD-block-core.BlockdevRef "QSD:block-core.BlockdevRef")) – block device used to log writes to `file`
        - **log-sector-size** (`int`, *optional*) – sector size used in logging writes to `file`,
          determines granularity of offsets and sizes of writes
          (default: 512)
        - **log-append** (`boolean`, *optional*) – append to an existing log (default: false)
        - **log-super-update-interval** (`int`, *optional*) – interval of write requests after which
          the log super block is updated to disk (default: 4096)

*Object* BlockdevOptionsBlkverify (Since: 2.9)
:   Driver specific block device options for blkverify.

    Members:
    :   - **test** ([`BlockdevRef`](qemu-storage-daemon-qmp-ref.md#alternate-QSD-block-core.BlockdevRef "QSD:block-core.BlockdevRef")) – block device to be tested
        - **raw** ([`BlockdevRef`](qemu-storage-daemon-qmp-ref.md#alternate-QSD-block-core.BlockdevRef "QSD:block-core.BlockdevRef")) – raw image used for verification

*Object* BlockdevOptionsBlkreplay (Since: 4.2)
:   Driver specific block device options for blkreplay.

    Members:
    :   - **image** ([`BlockdevRef`](qemu-storage-daemon-qmp-ref.md#alternate-QSD-block-core.BlockdevRef "QSD:block-core.BlockdevRef")) – disk image which should be controlled with blkreplay

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
        - **children** (`[`[`BlockdevRef`](qemu-storage-daemon-qmp-ref.md#alternate-QSD-block-core.BlockdevRef "QSD:block-core.BlockdevRef")`]`) – the children block devices to use
        - **vote-threshold** (`int`) – the vote limit under which a read will fail
        - **rewrite-corrupted** (`boolean`, *optional*) – rewrite corrupted data when quorum is reached
          (Since 2.1)
        - **read-pattern** ([`QuorumReadPattern`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.QuorumReadPattern "QSD:block-core.QuorumReadPattern"), *optional*) – choose read pattern and set to quorum by default
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
    :   - **transport** ([`IscsiTransport`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.IscsiTransport "QSD:block-core.IscsiTransport")) – The iscsi transport type
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
        - **header-digest** ([`IscsiHeaderDigest`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.IscsiHeaderDigest "QSD:block-core.IscsiHeaderDigest"), *optional*) – The desired header digest. Defaults to none-crc32c.
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
    :   - **cipher-alg** ([`QCryptoCipherAlgo`](qemu-storage-daemon-qmp-ref.md#enum-QSD-crypto.QCryptoCipherAlgo "QSD:crypto.QCryptoCipherAlgo"), *optional*) – The encryption algorithm
        - The members of [`RbdEncryptionOptionsLUKSBase`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.RbdEncryptionOptionsLUKSBase "QSD:block-core.RbdEncryptionOptionsLUKSBase").

*Object* RbdEncryptionOptionsLUKS (Since: 6.1)
:   Members:
    :   - The members of [`RbdEncryptionOptionsLUKSBase`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.RbdEncryptionOptionsLUKSBase "QSD:block-core.RbdEncryptionOptionsLUKSBase").

*Object* RbdEncryptionOptionsLUKS2 (Since: 6.1)
:   Members:
    :   - The members of [`RbdEncryptionOptionsLUKSBase`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.RbdEncryptionOptionsLUKSBase "QSD:block-core.RbdEncryptionOptionsLUKSBase").

*Object* RbdEncryptionOptionsLUKSAny (Since: 8.0)
:   Members:
    :   - The members of [`RbdEncryptionOptionsLUKSBase`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.RbdEncryptionOptionsLUKSBase "QSD:block-core.RbdEncryptionOptionsLUKSBase").

*Object* RbdEncryptionCreateOptionsLUKS (Since: 6.1)
:   Members:
    :   - The members of [`RbdEncryptionCreateOptionsLUKSBase`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.RbdEncryptionCreateOptionsLUKSBase "QSD:block-core.RbdEncryptionCreateOptionsLUKSBase").

*Object* RbdEncryptionCreateOptionsLUKS2 (Since: 6.1)
:   Members:
    :   - The members of [`RbdEncryptionCreateOptionsLUKSBase`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.RbdEncryptionCreateOptionsLUKSBase "QSD:block-core.RbdEncryptionCreateOptionsLUKSBase").

*Object* RbdEncryptionOptions (Since: 6.1)
:   Members:
    :   - **format** ([`RbdImageEncryptionFormat`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.RbdImageEncryptionFormat "QSD:block-core.RbdImageEncryptionFormat")) – Encryption format.
        - **parent** ([`RbdEncryptionOptions`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.RbdEncryptionOptions "QSD:block-core.RbdEncryptionOptions"), *optional*) – Parent image encryption options (for cloned images). Can
          be left unspecified if this cloned image is encrypted using the
          same format and secret as its parent image (i.e. not explicitly
          formatted) or if its parent image is not encrypted. (Since 8.0)
        - When `format` is `luks`: The members of [`RbdEncryptionOptionsLUKS`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.RbdEncryptionOptionsLUKS "QSD:block-core.RbdEncryptionOptionsLUKS").
        - When `format` is `luks2`: The members of [`RbdEncryptionOptionsLUKS2`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.RbdEncryptionOptionsLUKS2 "QSD:block-core.RbdEncryptionOptionsLUKS2").
        - When `format` is `luks-any`: The members of [`RbdEncryptionOptionsLUKSAny`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.RbdEncryptionOptionsLUKSAny "QSD:block-core.RbdEncryptionOptionsLUKSAny").

*Object* RbdEncryptionCreateOptions (Since: 6.1)
:   Members:
    :   - **format** ([`RbdImageEncryptionFormat`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.RbdImageEncryptionFormat "QSD:block-core.RbdImageEncryptionFormat")) – Encryption format.
        - When `format` is `luks`: The members of [`RbdEncryptionCreateOptionsLUKS`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.RbdEncryptionCreateOptionsLUKS "QSD:block-core.RbdEncryptionCreateOptionsLUKS").
        - When `format` is `luks2`: The members of [`RbdEncryptionCreateOptionsLUKS2`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.RbdEncryptionCreateOptionsLUKS2 "QSD:block-core.RbdEncryptionCreateOptionsLUKS2").

*Object* BlockdevOptionsRbd (Since: 2.9)
:   Members:
    :   - **pool** (`string`) – Ceph pool name.
        - **namespace** (`string`, *optional*) – Rados namespace name in the Ceph pool. (Since 5.0)
        - **image** (`string`) – Image name in the Ceph pool.
        - **conf** (`string`, *optional*) – path to Ceph configuration file. Values in the configuration
          file will be overridden by options specified via QAPI.
        - **snapshot** (`string`, *optional*) – Ceph snapshot name.
        - **encrypt** ([`RbdEncryptionOptions`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.RbdEncryptionOptions "QSD:block-core.RbdEncryptionOptions"), *optional*) – Image encryption options. (Since 6.1)
        - **user** (`string`, *optional*) – Ceph id name.
        - **auth-client-required** (`[`[`RbdAuthMode`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.RbdAuthMode "QSD:block-core.RbdAuthMode")`]`, *optional*) – Acceptable authentication modes. This maps
          to Ceph configuration option “auth_client_required”.
          (Since 3.0)
        - **key-secret** (`string`, *optional*) – ID of a QCryptoSecret object providing a key for cephx
          authentication. This maps to Ceph configuration option “key”.
          (Since 3.0)
        - **server** (`[`[`InetSocketAddressBase`](qemu-storage-daemon-qmp-ref.md#object-QSD-sockets.InetSocketAddressBase "QSD:sockets.InetSocketAddressBase")`]`, *optional*) – Monitor host address and port. This maps to the “mon_host”
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
    :   - **mode** ([`ReplicationMode`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.ReplicationMode "QSD:block-core.ReplicationMode")) – the replication mode
        - **top-id** (`string`, *optional*) – In secondary mode, node name or device ID of the root node
          who owns the replication node chain. Must not be given in
          primary mode.
        - The members of [`BlockdevOptionsGenericFormat`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsGenericFormat "QSD:block-core.BlockdevOptionsGenericFormat").

*Enum* NFSTransport (Since: 2.9)
:   An enumeration of NFS transport types

    Values:
    :   - **inet** – TCP transport

*Object* NFSServer (Since: 2.9)
:   Captures the address of the socket

    Members:
    :   - **type** ([`NFSTransport`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.NFSTransport "QSD:block-core.NFSTransport")) – transport type used for NFS (only TCP supported)
        - **host** (`string`) – host address for NFS server

*Object* BlockdevOptionsNfs (Since: 2.9)
:   Driver specific block device option for NFS

    Members:
    :   - **server** ([`NFSServer`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.NFSServer "QSD:block-core.NFSServer")) – host address
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
        - The members of [`BlockdevOptionsCurlBase`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsCurlBase "QSD:block-core.BlockdevOptionsCurlBase").

*Object* BlockdevOptionsCurlHttps (Since: 2.9)
:   Driver specific block device options for HTTPS connections over the
    curl backend. URLs must start with “[https://](qemu-storage-daemon-qmp-ref.md)”.

    Members:
    :   - **sslverify** (`boolean`, *optional*) – Whether to verify the SSL certificate’s validity
          (defaults to true)
        - The members of [`BlockdevOptionsCurlHttp`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsCurlHttp "QSD:block-core.BlockdevOptionsCurlHttp").

*Object* BlockdevOptionsCurlFtp (Since: 2.9)
:   Driver specific block device options for FTP connections over the
    curl backend. URLs must start with “<ftp://>”.

    Members:
    :   - The members of [`BlockdevOptionsCurlBase`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsCurlBase "QSD:block-core.BlockdevOptionsCurlBase").

*Object* BlockdevOptionsCurlFtps (Since: 2.9)
:   Driver specific block device options for FTPS connections over the
    curl backend. URLs must start with “ftps://”.

    Members:
    :   - **sslverify** (`boolean`, *optional*) – Whether to verify the SSL certificate’s validity
          (defaults to true)
        - The members of [`BlockdevOptionsCurlBase`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsCurlBase "QSD:block-core.BlockdevOptionsCurlBase").

*Object* BlockdevOptionsNbd (Since: 2.9)
:   Driver specific block device options for NBD.

    Members:
    :   - **server** ([`SocketAddress`](qemu-storage-daemon-qmp-ref.md#object-QSD-sockets.SocketAddress "QSD:sockets.SocketAddress")) – NBD server address
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
        - The members of [`BlockdevOptionsGenericFormat`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsGenericFormat "QSD:block-core.BlockdevOptionsGenericFormat").

*Object* BlockdevOptionsThrottle (Since: 2.11)
:   Driver specific block device options for the throttle driver

    Members:
    :   - **throttle-group** (`string`) – the name of the throttle-group object to use. It
          must already exist.
        - **file** ([`BlockdevRef`](qemu-storage-daemon-qmp-ref.md#alternate-QSD-block-core.BlockdevRef "QSD:block-core.BlockdevRef")) – reference to or definition of the data source block device

*Object* BlockdevOptionsCor (Since: 6.0)
:   Driver specific block device options for the copy-on-read driver.

    Members:
    :   - **bottom** (`string`, *optional*) – The name of a non-filter node (allocation-bearing layer)
          that limits the COR operations in the backing chain (inclusive),
          so that no data below this node will be copied by this filter.
          If option is absent, the limit is not applied, so that data from
          all backing layers may be copied.
        - The members of [`BlockdevOptionsGenericFormat`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsGenericFormat "QSD:block-core.BlockdevOptionsGenericFormat").

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
    :   - **target** ([`BlockdevRef`](qemu-storage-daemon-qmp-ref.md#alternate-QSD-block-core.BlockdevRef "QSD:block-core.BlockdevRef")) – The target for copy-before-write operations.
        - **bitmap** ([`BlockDirtyBitmap`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockDirtyBitmap "QSD:block-core.BlockDirtyBitmap"), *optional*) – If specified, copy-before-write filter will do
          copy-before-write operations only for dirty regions of the
          bitmap. Bitmap size must be equal to length of file and target
          child of the filter. Note also, that bitmap is used only to
          initialize internal bitmap of the process, so further
          modifications (or removing) of specified bitmap doesn’t
          influence the filter. (Since 7.0)
        - **on-cbw-error** ([`OnCbwError`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.OnCbwError "QSD:block-core.OnCbwError"), *optional*) – Behavior on failure of copy-before-write operation.
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
        - The members of [`BlockdevOptionsGenericFormat`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsGenericFormat "QSD:block-core.BlockdevOptionsGenericFormat").

*Object* BlockdevOptions (Since: 2.9)
:   Options for creating a block device. Many options are available for
    all block devices, independent of the block driver:

    Members:
    :   - **driver** ([`BlockdevDriver`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockdevDriver "QSD:block-core.BlockdevDriver")) – block driver name
        - **node-name** (`string`, *optional*) – the node name of the new node. This option is required
          on the top level of [`blockdev-add`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.blockdev-add "QSD:block-core.blockdev-add"). Valid node names start with
          an alphabetic character and may contain only alphanumeric
          characters, ‘-’, ‘.’ and ‘_’. Their maximum length is 31
          characters. (Since 2.0)
        - **discard** ([`BlockdevDiscardOptions`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockdevDiscardOptions "QSD:block-core.BlockdevDiscardOptions"), *optional*) – discard-related options (default: ignore)
        - **cache** ([`BlockdevCacheOptions`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevCacheOptions "QSD:block-core.BlockdevCacheOptions"), *optional*) – cache-related options
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
        - **detect-zeroes** ([`BlockdevDetectZeroesOptions`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockdevDetectZeroesOptions "QSD:block-core.BlockdevDetectZeroesOptions"), *optional*) – detect and optimize zero writes (Since 2.1)
          (default: off)
        - **force-share** (`boolean`, *optional*) – force share all permission on added nodes. Requires
          read-only=true. (Since 2.10)
        - When `driver` is `blkdebug`: The members of [`BlockdevOptionsBlkdebug`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsBlkdebug "QSD:block-core.BlockdevOptionsBlkdebug").
        - When `driver` is `blklogwrites`: The members of [`BlockdevOptionsBlklogwrites`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsBlklogwrites "QSD:block-core.BlockdevOptionsBlklogwrites").
        - When `driver` is `blkverify`: The members of [`BlockdevOptionsBlkverify`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsBlkverify "QSD:block-core.BlockdevOptionsBlkverify").
        - When `driver` is `blkreplay`: The members of [`BlockdevOptionsBlkreplay`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsBlkreplay "QSD:block-core.BlockdevOptionsBlkreplay").
        - When `driver` is `bochs`: The members of [`BlockdevOptionsGenericFormat`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsGenericFormat "QSD:block-core.BlockdevOptionsGenericFormat").
        - When `driver` is `cloop`: The members of [`BlockdevOptionsGenericFormat`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsGenericFormat "QSD:block-core.BlockdevOptionsGenericFormat").
        - When `driver` is `compress`: The members of [`BlockdevOptionsGenericFormat`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsGenericFormat "QSD:block-core.BlockdevOptionsGenericFormat").
        - When `driver` is `copy-before-write`: The members of [`BlockdevOptionsCbw`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsCbw "QSD:block-core.BlockdevOptionsCbw").
        - When `driver` is `copy-on-read`: The members of [`BlockdevOptionsCor`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsCor "QSD:block-core.BlockdevOptionsCor").
        - When `driver` is `dmg`: The members of [`BlockdevOptionsGenericFormat`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsGenericFormat "QSD:block-core.BlockdevOptionsGenericFormat").
        - When `driver` is `file`: The members of [`BlockdevOptionsFile`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsFile "QSD:block-core.BlockdevOptionsFile").
        - When `driver` is `ftp`: The members of [`BlockdevOptionsCurlFtp`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsCurlFtp "QSD:block-core.BlockdevOptionsCurlFtp").
        - When `driver` is `ftps`: The members of [`BlockdevOptionsCurlFtps`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsCurlFtps "QSD:block-core.BlockdevOptionsCurlFtps").
        - When `driver` is `host_cdrom`: The members of [`BlockdevOptionsFile`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsFile "QSD:block-core.BlockdevOptionsFile").
        - When `driver` is `host_device`: The members of [`BlockdevOptionsFile`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsFile "QSD:block-core.BlockdevOptionsFile").
        - When `driver` is `http`: The members of [`BlockdevOptionsCurlHttp`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsCurlHttp "QSD:block-core.BlockdevOptionsCurlHttp").
        - When `driver` is `https`: The members of [`BlockdevOptionsCurlHttps`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsCurlHttps "QSD:block-core.BlockdevOptionsCurlHttps").
        - When `driver` is `io_uring`: The members of [`BlockdevOptionsIoUring`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsIoUring "QSD:block-core.BlockdevOptionsIoUring").
        - When `driver` is `iscsi`: The members of [`BlockdevOptionsIscsi`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsIscsi "QSD:block-core.BlockdevOptionsIscsi").
        - When `driver` is `luks`: The members of [`BlockdevOptionsLUKS`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsLUKS "QSD:block-core.BlockdevOptionsLUKS").
        - When `driver` is `nbd`: The members of [`BlockdevOptionsNbd`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsNbd "QSD:block-core.BlockdevOptionsNbd").
        - When `driver` is `nfs`: The members of [`BlockdevOptionsNfs`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsNfs "QSD:block-core.BlockdevOptionsNfs").
        - When `driver` is `null-aio`: The members of [`BlockdevOptionsNull`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsNull "QSD:block-core.BlockdevOptionsNull").
        - When `driver` is `null-co`: The members of [`BlockdevOptionsNull`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsNull "QSD:block-core.BlockdevOptionsNull").
        - When `driver` is `nvme`: The members of [`BlockdevOptionsNVMe`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsNVMe "QSD:block-core.BlockdevOptionsNVMe").
        - When `driver` is `nvme-io_uring`: The members of [`BlockdevOptionsNvmeIoUring`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsNvmeIoUring "QSD:block-core.BlockdevOptionsNvmeIoUring").
        - When `driver` is `parallels`: The members of [`BlockdevOptionsGenericFormat`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsGenericFormat "QSD:block-core.BlockdevOptionsGenericFormat").
        - When `driver` is `preallocate`: The members of [`BlockdevOptionsPreallocate`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsPreallocate "QSD:block-core.BlockdevOptionsPreallocate").
        - When `driver` is `qcow2`: The members of [`BlockdevOptionsQcow2`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsQcow2 "QSD:block-core.BlockdevOptionsQcow2").
        - When `driver` is `qcow`: The members of [`BlockdevOptionsQcow`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsQcow "QSD:block-core.BlockdevOptionsQcow").
        - When `driver` is `qed`: The members of [`BlockdevOptionsGenericCOWFormat`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsGenericCOWFormat "QSD:block-core.BlockdevOptionsGenericCOWFormat").
        - When `driver` is `quorum`: The members of [`BlockdevOptionsQuorum`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsQuorum "QSD:block-core.BlockdevOptionsQuorum").
        - When `driver` is `raw`: The members of [`BlockdevOptionsRaw`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsRaw "QSD:block-core.BlockdevOptionsRaw").
        - When `driver` is `rbd`: The members of [`BlockdevOptionsRbd`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsRbd "QSD:block-core.BlockdevOptionsRbd").
        - When `driver` is `replication`: The members of [`BlockdevOptionsReplication`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsReplication "QSD:block-core.BlockdevOptionsReplication").
        - When `driver` is `snapshot-access`: The members of [`BlockdevOptionsGenericFormat`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsGenericFormat "QSD:block-core.BlockdevOptionsGenericFormat").
        - When `driver` is `ssh`: The members of [`BlockdevOptionsSsh`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsSsh "QSD:block-core.BlockdevOptionsSsh").
        - When `driver` is `throttle`: The members of [`BlockdevOptionsThrottle`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsThrottle "QSD:block-core.BlockdevOptionsThrottle").
        - When `driver` is `vdi`: The members of [`BlockdevOptionsGenericFormat`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsGenericFormat "QSD:block-core.BlockdevOptionsGenericFormat").
        - When `driver` is `vhdx`: The members of [`BlockdevOptionsGenericFormat`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsGenericFormat "QSD:block-core.BlockdevOptionsGenericFormat").
        - When `driver` is `virtio-blk-vfio-pci`: The members of [`BlockdevOptionsVirtioBlkVfioPci`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsVirtioBlkVfioPci "QSD:block-core.BlockdevOptionsVirtioBlkVfioPci").
        - When `driver` is `virtio-blk-vhost-user`: The members of [`BlockdevOptionsVirtioBlkVhostUser`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsVirtioBlkVhostUser "QSD:block-core.BlockdevOptionsVirtioBlkVhostUser").
        - When `driver` is `virtio-blk-vhost-vdpa`: The members of [`BlockdevOptionsVirtioBlkVhostVdpa`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsVirtioBlkVhostVdpa "QSD:block-core.BlockdevOptionsVirtioBlkVhostVdpa").
        - When `driver` is `vmdk`: The members of [`BlockdevOptionsGenericCOWFormat`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsGenericCOWFormat "QSD:block-core.BlockdevOptionsGenericCOWFormat").
        - When `driver` is `vpc`: The members of [`BlockdevOptionsGenericFormat`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsGenericFormat "QSD:block-core.BlockdevOptionsGenericFormat").
        - When `driver` is `vvfat`: The members of [`BlockdevOptionsVVFAT`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsVVFAT "QSD:block-core.BlockdevOptionsVVFAT").

*Alternate* BlockdevRef (Since: 2.9)
:   Reference to a block device.

    Alternatives:
    :   - **definition** ([`BlockdevOptions`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptions "QSD:block-core.BlockdevOptions")) – defines a new block device inline
        - **reference** (`string`) – references the ID of an existing block device

*Alternate* BlockdevRefOrNull (Since: 2.9)
:   Reference to a block device.

    Alternatives:
    :   - **definition** ([`BlockdevOptions`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptions "QSD:block-core.BlockdevOptions")) – defines a new block device inline
        - **reference** (`string`) – references the ID of an existing block device. An empty
          string means that no block device should be referenced.
          Deprecated; use null instead.
        - **null** (`null`) – No block device should be referenced (since 2.10)

*Command* blockdev-add (Since: 2.9)
:   Creates a new block device.

    Arguments:
    :   - The members of [`BlockdevOptions`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptions "QSD:block-core.BlockdevOptions").

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
    [`BlockdevOptions`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptions "QSD:block-core.BlockdevOptions")) must be specified and is used to select the block
    device to be reopened. Other `node-name` options must be either
    omitted or set to the current name of the appropriate node. This
    command won’t change any node name and any attempt to do it will
    result in an error.

    In the case of options that refer to child nodes, the behavior of
    this command depends on the value:

    > 1. A set of options ([`BlockdevOptions`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptions "QSD:block-core.BlockdevOptions")): the child is reopened with
    >    the specified set of options.
    > 2. A reference to the current child: the child is reopened using
    >    its existing set of options.
    > 3. A reference to a different node: the current child is replaced
    >    with the specified one.
    > 4. null: the current child (if any) is detached.

    Options (1) and (2) are supported in all cases. Option (3) is
    supported for `file` and `backing`, and option (4) for `backing` only.

    Unlike with [`blockdev-add`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.blockdev-add "QSD:block-core.blockdev-add"), the `backing` option must always be
    present unless the node being reopened does not have a backing file
    and its image does not have a default backing file name as part of
    its metadata.

    Arguments:
    :   - **options** (`[`[`BlockdevOptions`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptions "QSD:block-core.BlockdevOptions")`]`) – Not documented

*Command* blockdev-del (Since: 2.9)
:   Deletes a block device that has been added using [`blockdev-add`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.blockdev-add "QSD:block-core.blockdev-add").
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
        - **preallocation** ([`PreallocMode`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.PreallocMode "QSD:block-core.PreallocMode"), *optional*) – Preallocation mode for the new image (default: off;
          allowed values: off, falloc (if CONFIG_POSIX_FALLOCATE), full
          (if CONFIG_POSIX))
        - **nocow** (`boolean`, *optional*) – Turn off copy-on-write (valid only on btrfs; default: off)
        - **extent-size-hint** (`int`, *optional*) – Extent size hint to add to the image file; 0 for
          not adding an extent size hint (default: 1 MB, since 5.1)

*Object* BlockdevCreateOptionsLUKS (Since: 2.12)
:   Driver specific image creation options for LUKS.

    Members:
    :   - **file** ([`BlockdevRef`](qemu-storage-daemon-qmp-ref.md#alternate-QSD-block-core.BlockdevRef "QSD:block-core.BlockdevRef"), *optional*) – Node to create the image format on, mandatory except when
          ‘preallocation’ is not requested
        - **header** ([`BlockdevRef`](qemu-storage-daemon-qmp-ref.md#alternate-QSD-block-core.BlockdevRef "QSD:block-core.BlockdevRef"), *optional*) – Block device holding a detached LUKS header. (since 9.0)
        - **size** (`int`) – Size of the virtual disk in bytes
        - **preallocation** ([`PreallocMode`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.PreallocMode "QSD:block-core.PreallocMode"), *optional*) – Preallocation mode for the new image (since: 4.2)
          (default: off; allowed values: off, metadata, falloc, full)
        - The members of [`QCryptoBlockCreateOptionsLUKS`](qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.QCryptoBlockCreateOptionsLUKS "QSD:crypto.QCryptoBlockCreateOptionsLUKS").

*Object* BlockdevCreateOptionsNfs (Since: 2.12)
:   Driver specific image creation options for NFS.

    Members:
    :   - **location** ([`BlockdevOptionsNfs`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsNfs "QSD:block-core.BlockdevOptionsNfs")) – Where to store the new image file
        - **size** (`int`) – Size of the virtual disk in bytes

*Object* BlockdevCreateOptionsParallels (Since: 2.12)
:   Driver specific image creation options for parallels.

    Members:
    :   - **file** ([`BlockdevRef`](qemu-storage-daemon-qmp-ref.md#alternate-QSD-block-core.BlockdevRef "QSD:block-core.BlockdevRef")) – Node to create the image format on
        - **size** (`int`) – Size of the virtual disk in bytes
        - **cluster-size** (`int`, *optional*) – Cluster size in bytes (default: 1 MB)

*Object* BlockdevCreateOptionsQcow (Since: 2.12)
:   Driver specific image creation options for qcow.

    Members:
    :   - **file** ([`BlockdevRef`](qemu-storage-daemon-qmp-ref.md#alternate-QSD-block-core.BlockdevRef "QSD:block-core.BlockdevRef")) – Node to create the image format on
        - **size** (`int`) – Size of the virtual disk in bytes
        - **backing-file** (`string`, *optional*) – File name of the backing file if a backing file
          should be used
        - **encrypt** ([`QCryptoBlockCreateOptions`](qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.QCryptoBlockCreateOptions "QSD:crypto.QCryptoBlockCreateOptions"), *optional*) – Encryption options if the image should be encrypted

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
    :   - **file** ([`BlockdevRef`](qemu-storage-daemon-qmp-ref.md#alternate-QSD-block-core.BlockdevRef "QSD:block-core.BlockdevRef")) – Node to create the image format on
        - **data-file** ([`BlockdevRef`](qemu-storage-daemon-qmp-ref.md#alternate-QSD-block-core.BlockdevRef "QSD:block-core.BlockdevRef"), *optional*) – Node to use as an external data file in which all guest
          data is stored so that only metadata remains in the qcow2 file
          (since: 4.0)
        - **data-file-raw** (`boolean`, *optional*) – True if the external data file must stay valid as a
          standalone (read-only) raw image without looking at qcow2
          metadata (default: false; since: 4.0)
        - **extended-l2** (`boolean`, *optional*) – True to make the image have extended L2 entries
          (default: false; since 5.2)
        - **size** (`int`) – Size of the virtual disk in bytes
        - **version** ([`BlockdevQcow2Version`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockdevQcow2Version "QSD:block-core.BlockdevQcow2Version"), *optional*) – Compatibility level (default: v3)
        - **backing-file** (`string`, *optional*) – File name of the backing file if a backing file
          should be used
        - **backing-fmt** ([`BlockdevDriver`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockdevDriver "QSD:block-core.BlockdevDriver"), *optional*) – Name of the block driver to use for the backing file
        - **encrypt** ([`QCryptoBlockCreateOptions`](qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.QCryptoBlockCreateOptions "QSD:crypto.QCryptoBlockCreateOptions"), *optional*) – Encryption options if the image should be encrypted
        - **cluster-size** (`int`, *optional*) – qcow2 cluster size in bytes (default: 65536)
        - **preallocation** ([`PreallocMode`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.PreallocMode "QSD:block-core.PreallocMode"), *optional*) – Preallocation mode for the new image (default: off;
          allowed values: off, falloc, full, metadata)
        - **lazy-refcounts** (`boolean`, *optional*) – True if refcounts may be updated lazily
          (default: off)
        - **refcount-bits** (`int`, *optional*) – Width of reference counts in bits (default: 16)
        - **compression-type** ([`Qcow2CompressionType`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.Qcow2CompressionType "QSD:block-core.Qcow2CompressionType"), *optional*) – The image cluster compression method
          (default: zlib, since 5.1)

*Object* BlockdevCreateOptionsQed (Since: 2.12)
:   Driver specific image creation options for qed.

    Members:
    :   - **file** ([`BlockdevRef`](qemu-storage-daemon-qmp-ref.md#alternate-QSD-block-core.BlockdevRef "QSD:block-core.BlockdevRef")) – Node to create the image format on
        - **size** (`int`) – Size of the virtual disk in bytes
        - **backing-file** (`string`, *optional*) – File name of the backing file if a backing file
          should be used
        - **backing-fmt** ([`BlockdevDriver`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockdevDriver "QSD:block-core.BlockdevDriver"), *optional*) – Name of the block driver to use for the backing file
        - **cluster-size** (`int`, *optional*) – Cluster size in bytes (default: 65536)
        - **table-size** (`int`, *optional*) – L1/L2 table size (in clusters)

*Object* BlockdevCreateOptionsRbd (Since: 2.12)
:   Driver specific image creation options for rbd/Ceph.

    Members:
    :   - **location** ([`BlockdevOptionsRbd`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsRbd "QSD:block-core.BlockdevOptionsRbd")) – Where to store the new image file. This location cannot
          point to a snapshot.
        - **size** (`int`) – Size of the virtual disk in bytes
        - **cluster-size** (`int`, *optional*) – RBD object size
        - **encrypt** ([`RbdEncryptionCreateOptions`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.RbdEncryptionCreateOptions "QSD:block-core.RbdEncryptionCreateOptions"), *optional*) – Image encryption options. (Since 6.1)

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
    :   - **file** ([`BlockdevRef`](qemu-storage-daemon-qmp-ref.md#alternate-QSD-block-core.BlockdevRef "QSD:block-core.BlockdevRef")) – Where to store the new image file. This refers to the image
          file for monolithcSparse and streamOptimized format, or the
          descriptor file for other formats.
        - **size** (`int`) – Size of the virtual disk in bytes
        - **extents** (`[`[`BlockdevRef`](qemu-storage-daemon-qmp-ref.md#alternate-QSD-block-core.BlockdevRef "QSD:block-core.BlockdevRef")`]`, *optional*) – Where to store the data extents. Required for
          monolithcFlat, twoGbMaxExtentSparse and twoGbMaxExtentFlat
          formats. For monolithicFlat, only one entry is required; for
          twoGbMaxExtent\* formats, the number of entries required is
          calculated as extent_number = virtual_size / 2GB. Providing
          more extents than will be used is an error.
        - **subformat** ([`BlockdevVmdkSubformat`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockdevVmdkSubformat "QSD:block-core.BlockdevVmdkSubformat"), *optional*) – The subformat of the VMDK image. Default:
          “monolithicSparse”.
        - **backing-file** (`string`, *optional*) – The path of backing file. Default: no backing file
          is used.
        - **adapter-type** ([`BlockdevVmdkAdapterType`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockdevVmdkAdapterType "QSD:block-core.BlockdevVmdkAdapterType"), *optional*) – The adapter type used to fill in the descriptor.
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
    :   - **location** ([`BlockdevOptionsSsh`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevOptionsSsh "QSD:block-core.BlockdevOptionsSsh")) – Where to store the new image file
        - **size** (`int`) – Size of the virtual disk in bytes

*Object* BlockdevCreateOptionsVdi (Since: 2.12)
:   Driver specific image creation options for VDI.

    Members:
    :   - **file** ([`BlockdevRef`](qemu-storage-daemon-qmp-ref.md#alternate-QSD-block-core.BlockdevRef "QSD:block-core.BlockdevRef")) – Node to create the image format on
        - **size** (`int`) – Size of the virtual disk in bytes
        - **preallocation** ([`PreallocMode`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.PreallocMode "QSD:block-core.PreallocMode"), *optional*) – Preallocation mode for the new image (default: off;
          allowed values: off, metadata)

*Enum* BlockdevVhdxSubformat (Since: 2.12)
:   Values:
    :   - **dynamic** – Growing image file
        - **fixed** – Preallocated fixed-size image file

*Object* BlockdevCreateOptionsVhdx (Since: 2.12)
:   Driver specific image creation options for vhdx.

    Members:
    :   - **file** ([`BlockdevRef`](qemu-storage-daemon-qmp-ref.md#alternate-QSD-block-core.BlockdevRef "QSD:block-core.BlockdevRef")) – Node to create the image format on
        - **size** (`int`) – Size of the virtual disk in bytes
        - **log-size** (`int`, *optional*) – Log size in bytes, must be a multiple of 1 MB (default: 1
          MB)
        - **block-size** (`int`, *optional*) – Block size in bytes, must be a multiple of 1 MB and not
          larger than 256 MB (default: automatically choose a block size
          depending on the image size)
        - **subformat** ([`BlockdevVhdxSubformat`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockdevVhdxSubformat "QSD:block-core.BlockdevVhdxSubformat"), *optional*) – vhdx subformat (default: dynamic)
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
    :   - **file** ([`BlockdevRef`](qemu-storage-daemon-qmp-ref.md#alternate-QSD-block-core.BlockdevRef "QSD:block-core.BlockdevRef")) – Node to create the image format on
        - **size** (`int`) – Size of the virtual disk in bytes
        - **subformat** ([`BlockdevVpcSubformat`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockdevVpcSubformat "QSD:block-core.BlockdevVpcSubformat"), *optional*) – vhdx subformat (default: dynamic)
        - **force-size** (`boolean`, *optional*) – Force use of the exact byte size instead of rounding to
          the next size that can be represented in CHS geometry
          (default: false)

*Object* BlockdevCreateOptions (Since: 2.12)
:   Options for creating an image format on a given node.

    Members:
    :   - **driver** ([`BlockdevDriver`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockdevDriver "QSD:block-core.BlockdevDriver")) – block driver to create the image format
        - When `driver` is `file`: The members of [`BlockdevCreateOptionsFile`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevCreateOptionsFile "QSD:block-core.BlockdevCreateOptionsFile").
        - When `driver` is `luks`: The members of [`BlockdevCreateOptionsLUKS`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevCreateOptionsLUKS "QSD:block-core.BlockdevCreateOptionsLUKS").
        - When `driver` is `nfs`: The members of [`BlockdevCreateOptionsNfs`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevCreateOptionsNfs "QSD:block-core.BlockdevCreateOptionsNfs").
        - When `driver` is `parallels`: The members of [`BlockdevCreateOptionsParallels`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevCreateOptionsParallels "QSD:block-core.BlockdevCreateOptionsParallels").
        - When `driver` is `qcow`: The members of [`BlockdevCreateOptionsQcow`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevCreateOptionsQcow "QSD:block-core.BlockdevCreateOptionsQcow").
        - When `driver` is `qcow2`: The members of [`BlockdevCreateOptionsQcow2`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevCreateOptionsQcow2 "QSD:block-core.BlockdevCreateOptionsQcow2").
        - When `driver` is `qed`: The members of [`BlockdevCreateOptionsQed`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevCreateOptionsQed "QSD:block-core.BlockdevCreateOptionsQed").
        - When `driver` is `rbd`: The members of [`BlockdevCreateOptionsRbd`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevCreateOptionsRbd "QSD:block-core.BlockdevCreateOptionsRbd").
        - When `driver` is `ssh`: The members of [`BlockdevCreateOptionsSsh`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevCreateOptionsSsh "QSD:block-core.BlockdevCreateOptionsSsh").
        - When `driver` is `vdi`: The members of [`BlockdevCreateOptionsVdi`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevCreateOptionsVdi "QSD:block-core.BlockdevCreateOptionsVdi").
        - When `driver` is `vhdx`: The members of [`BlockdevCreateOptionsVhdx`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevCreateOptionsVhdx "QSD:block-core.BlockdevCreateOptionsVhdx").
        - When `driver` is `vmdk`: The members of [`BlockdevCreateOptionsVmdk`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevCreateOptionsVmdk "QSD:block-core.BlockdevCreateOptionsVmdk").
        - When `driver` is `vpc`: The members of [`BlockdevCreateOptionsVpc`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevCreateOptionsVpc "QSD:block-core.BlockdevCreateOptionsVpc").

*Command* blockdev-create (Since: 3.0)
:   Starts a job to create an image format on a given node. The job is
    automatically finalized, but a manual [`job-dismiss`](qemu-storage-daemon-qmp-ref.md#command-QSD-job.job-dismiss "QSD:job.job-dismiss") is required.

    Arguments:
    :   - **job-id** (`string`) – Identifier for the newly created job.
        - **options** ([`BlockdevCreateOptions`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevCreateOptions "QSD:block-core.BlockdevCreateOptions")) – Options for the image creation.

*Object* BlockdevAmendOptionsLUKS (Since: 5.1)
:   Driver specific image amend options for LUKS.

    Members:
    :   - The members of [`QCryptoBlockAmendOptionsLUKS`](qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.QCryptoBlockAmendOptionsLUKS "QSD:crypto.QCryptoBlockAmendOptionsLUKS").

*Object* BlockdevAmendOptionsQcow2 (Since: 5.1)
:   Driver specific image amend options for qcow2. For now, only
    encryption options can be amended

    Members:
    :   - **encrypt** ([`QCryptoBlockAmendOptions`](qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.QCryptoBlockAmendOptions "QSD:crypto.QCryptoBlockAmendOptions"), *optional*) – Encryption options to be amended

*Object* BlockdevAmendOptions (Since: 5.1)
:   Options for amending an image format

    Members:
    :   - **driver** ([`BlockdevDriver`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockdevDriver "QSD:block-core.BlockdevDriver")) – Block driver of the node to amend.
        - When `driver` is `luks`: The members of [`BlockdevAmendOptionsLUKS`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevAmendOptionsLUKS "QSD:block-core.BlockdevAmendOptionsLUKS").
        - When `driver` is `qcow2`: The members of [`BlockdevAmendOptionsQcow2`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevAmendOptionsQcow2 "QSD:block-core.BlockdevAmendOptionsQcow2").

*Command* x-blockdev-amend (Since: 5.1)
:   This command is unstable/experimental.

    Starts a job to amend format specific options of an existing open
    block device. The job is automatically finalized, but a manual
    [`job-dismiss`](qemu-storage-daemon-qmp-ref.md#command-QSD-job.job-dismiss "QSD:job.job-dismiss") is required.

    Arguments:
    :   - **job-id** (`string`) – Identifier for the newly created job.
        - **node-name** (`string`) – Name of the block node to work on
        - **options** ([`BlockdevAmendOptions`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevAmendOptions "QSD:block-core.BlockdevAmendOptions")) – Options (driver specific)
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
          [`BLOCK_IMAGE_CORRUPTED`](qemu-storage-daemon-qmp-ref.md#event-QSD-block-core.BLOCK_IMAGE_CORRUPTED "QSD:block-core.BLOCK_IMAGE_CORRUPTED") event was fatal)

    > **Note:**
    >
    > If action is “stop”, a [`STOP`](qemu-qmp-ref.md#event-QMP-run-state.STOP "QMP:run-state.STOP") event will eventually follow
    > the [`BLOCK_IO_ERROR`](qemu-storage-daemon-qmp-ref.md#event-QSD-block-core.BLOCK_IO_ERROR "QSD:block-core.BLOCK_IO_ERROR") event.

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
        - **operation** ([`IoOperationType`](qemu-storage-daemon-qmp-ref.md#enum-QSD-common.IoOperationType "QSD:common.IoOperationType")) – I/O operation
        - **action** ([`BlockErrorAction`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockErrorAction "QSD:block-core.BlockErrorAction")) – action that has been taken
        - **nospace** (`boolean`, *optional*) – true if I/O error was caused due to a no-space condition.
          This key is only present if query-block’s io-status is present,
          please see [`query-block`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.query-block "QSD:block-core.query-block") documentation for more information
          (since: 2.2)
        - **reason** (`string`) – human readable string describing the error cause. (This
          field is a debugging aid for humans, it should not be parsed by
          applications) (since: 2.2)

    > **Note:**
    >
    > If action is “stop”, a [`STOP`](qemu-qmp-ref.md#event-QMP-run-state.STOP "QMP:run-state.STOP") event will eventually follow
    > the [`BLOCK_IO_ERROR`](qemu-storage-daemon-qmp-ref.md#event-QSD-block-core.BLOCK_IO_ERROR "QSD:block-core.BLOCK_IO_ERROR") event.

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
    :   - **type** ([`JobType`](qemu-storage-daemon-qmp-ref.md#enum-QSD-job.JobType "QSD:job.JobType")) – job type
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
    :   - **type** ([`JobType`](qemu-storage-daemon-qmp-ref.md#enum-QSD-job.JobType "QSD:job.JobType")) – job type
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
        - **operation** ([`IoOperationType`](qemu-storage-daemon-qmp-ref.md#enum-QSD-common.IoOperationType "QSD:common.IoOperationType")) – I/O operation
        - **action** ([`BlockErrorAction`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.BlockErrorAction "QSD:block-core.BlockErrorAction")) – action that has been taken

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
    :   - **type** ([`JobType`](qemu-storage-daemon-qmp-ref.md#enum-QSD-job.JobType "QSD:job.JobType")) – job type
        - **device** (`string`) – The job identifier. Originally the device name but other
          values are allowed since QEMU 2.7
        - **len** (`int`) – maximum progress value
        - **offset** (`int`) – current progress value. On success this is equal to len.
          On failure this is less than len
        - **speed** (`int`) – rate limit, bytes per second

    > **Note:**
    >
    > The “ready to complete” status is always reset by a
    > [`BLOCK_JOB_ERROR`](qemu-storage-daemon-qmp-ref.md#event-QSD-block-core.BLOCK_JOB_ERROR "QSD:block-core.BLOCK_JOB_ERROR") event.

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
    finalize graph changes via [`job-finalize`](qemu-storage-daemon-qmp-ref.md#command-QSD-job.job-finalize "QSD:job.job-finalize"). If this job is part of a
    transaction, it will not emit this event until the transaction has
    converged first.

    Members:
    :   - **type** ([`JobType`](qemu-storage-daemon-qmp-ref.md#enum-QSD-job.JobType "QSD:job.JobType")) – job type
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
    re-registered with another [`block-set-write-threshold`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.block-set-write-threshold "QSD:block-core.block-set-write-threshold") command.

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
        - **iothread** ([`StrOrNull`](qemu-storage-daemon-qmp-ref.md#alternate-QSD-common.StrOrNull "QSD:common.StrOrNull")) – the name of the IOThread object or null for the main loop
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
    :   - **type** ([`QuorumOpType`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-core.QuorumOpType "QSD:block-core.QuorumOpType")) – quorum operation type (Since 2.6)
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
    :   - The members of [`BlockdevSnapshotInternal`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevSnapshotInternal "QSD:block-core.BlockdevSnapshotInternal").

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
    [`SnapshotInfo`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.SnapshotInfo "QSD:block-core.SnapshotInfo") for the successfully deleted snapshot.

    Arguments:
    :   - **device** (`string`) – the device name or node-name of a root node to delete the
          snapshot from
        - **id** (`string`, *optional*) – optional the snapshot’s ID to be deleted
        - **name** (`string`, *optional*) – optional the snapshot’s name to be deleted

    Return:
    :   [`SnapshotInfo`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.SnapshotInfo "QSD:block-core.SnapshotInfo")

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
    :   - **unused-block-graph-info** (`[`[`BlockGraphInfo`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockGraphInfo "QSD:block-core.BlockGraphInfo")`]`) – Not documented

### [Block device exports](qemu-storage-daemon-qmp-ref.md#id8)

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
:   Keep this type consistent with the [`NbdServerOptionsLegacy`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-export.NbdServerOptionsLegacy "QSD:block-export.NbdServerOptionsLegacy") type.
    The only intended difference is using [`SocketAddress`](qemu-storage-daemon-qmp-ref.md#object-QSD-sockets.SocketAddress "QSD:sockets.SocketAddress") instead of
    [`SocketAddressLegacy`](qemu-storage-daemon-qmp-ref.md#object-QSD-sockets.SocketAddressLegacy "QSD:sockets.SocketAddressLegacy").

    Members:
    :   - **addr** ([`SocketAddress`](qemu-storage-daemon-qmp-ref.md#object-QSD-sockets.SocketAddress "QSD:sockets.SocketAddress")) – Address on which to listen (since 4.2).
        - The members of [`NbdServerOptionsBase`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-export.NbdServerOptionsBase "QSD:block-export.NbdServerOptionsBase").

*Object* NbdServerOptionsLegacy
:   Keep this type consistent with the [`NbdServerOptions`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-export.NbdServerOptions "QSD:block-export.NbdServerOptions") type. The
    only intended difference is using [`SocketAddressLegacy`](qemu-storage-daemon-qmp-ref.md#object-QSD-sockets.SocketAddressLegacy "QSD:sockets.SocketAddressLegacy") instead of
    [`SocketAddress`](qemu-storage-daemon-qmp-ref.md#object-QSD-sockets.SocketAddress "QSD:sockets.SocketAddress").

    Members:
    :   - **addr** ([`SocketAddressLegacy`](qemu-storage-daemon-qmp-ref.md#object-QSD-sockets.SocketAddressLegacy "QSD:sockets.SocketAddressLegacy")) – Address on which to listen (since 1.3).
        - The members of [`NbdServerOptionsBase`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-export.NbdServerOptionsBase "QSD:block-export.NbdServerOptionsBase").

*Command* nbd-server-start (Since: 1.3)
:   Start an NBD server listening on the given host and port. Block
    devices can then be exported using [`nbd-server-add`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-export.nbd-server-add "QSD:block-export.nbd-server-add"). The NBD server
    will present them as named exports; for example, another QEMU
    instance could refer to them as “nbd:HOST:PORT:exportname=NAME”.

    Arguments:
    :   - The members of [`NbdServerOptionsLegacy`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-export.NbdServerOptionsLegacy "QSD:block-export.NbdServerOptionsLegacy").

    Errors:
    :   - if the server is already running

*Object* BlockExportOptionsNbdBase (Since: 5.0)
:   An NBD block export (common options shared between [`nbd-server-add`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-export.nbd-server-add "QSD:block-export.nbd-server-add")
    and the NBD branch of [`block-export-add`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-export.block-export-add "QSD:block-export.block-export-add")).

    Members:
    :   - **name** (`string`, *optional*) – Export name. If unspecified, the `device` parameter is used
          as the export name. (Since 2.12)
        - **description** (`string`, *optional*) – Free-form description of the export, up to 4096 bytes.
          (Since 5.0)

*Object* BlockExportOptionsNbd (Since: 5.2)
:   An NBD block export (distinct options used in the NBD branch of
    [`block-export-add`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-export.block-export-add "QSD:block-export.block-export-add")).

    Members:
    :   - **bitmaps** (`[`[`BlockDirtyBitmapOrStr`](qemu-storage-daemon-qmp-ref.md#alternate-QSD-block-core.BlockDirtyBitmapOrStr "QSD:block-core.BlockDirtyBitmapOrStr")`]`, *optional*) – Also export each of the named dirty bitmaps reachable from
          `device`, so the NBD client can use NBD_OPT_SET_META_CONTEXT with
          the metadata context name “qemu:dirty-bitmap:BITMAP” to inspect
          each bitmap. Since 7.1 bitmap may be specified by node/name
          pair.
        - **allocation-depth** (`boolean`, *optional*) – Also export the allocation depth map for `device`,
          so the NBD client can use NBD_OPT_SET_META_CONTEXT with the
          metadata context name “qemu:allocation-depth” to inspect
          allocation details. (since 5.2)
        - The members of [`BlockExportOptionsNbdBase`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-export.BlockExportOptionsNbdBase "QSD:block-export.BlockExportOptionsNbdBase").

*Object* BlockExportOptionsVhostUserBlk (Since: 5.2)
:   A vhost-user-blk block export.

    Members:
    :   - **addr** ([`SocketAddress`](qemu-storage-daemon-qmp-ref.md#object-QSD-sockets.SocketAddress "QSD:sockets.SocketAddress")) – The vhost-user socket on which to listen. Both ‘unix’ and
          ‘fd’ [`SocketAddress`](qemu-storage-daemon-qmp-ref.md#object-QSD-sockets.SocketAddress "QSD:sockets.SocketAddress") types are supported. Passed fds must be
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
        - **allow-other** ([`FuseExportAllowOther`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-export.FuseExportAllowOther "QSD:block-export.FuseExportAllowOther"), *optional*) – If this is off, only QEMU’s user is allowed access to
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
:   An NBD block export, per legacy [`nbd-server-add`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-export.nbd-server-add "QSD:block-export.nbd-server-add") command.

    Members:
    :   - **device** (`string`) – The device name or node name of the node to be exported
        - **writable** (`boolean`, *optional*) – Whether clients should be able to write to the device via
          the NBD connection (default false).
        - **bitmap** (`string`, *optional*) – Also export a single dirty bitmap reachable from `device`,
          so the NBD client can use NBD_OPT_SET_META_CONTEXT with the
          metadata context name “qemu:dirty-bitmap:BITMAP” to inspect the
          bitmap (since 4.0).
        - The members of [`BlockExportOptionsNbdBase`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-export.BlockExportOptionsNbdBase "QSD:block-export.BlockExportOptionsNbdBase").

*Command* nbd-server-add (Since: 1.3)
:   This command is deprecated.

    Export a block node to QEMU’s embedded NBD server.

    The export name will be used as the id for the resulting block
    export.

    Arguments:
    :   - The members of [`NbdServerAddOptions`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-export.NbdServerAddOptions "QSD:block-export.NbdServerAddOptions").

    Features:
    :   - **deprecated** – This command is deprecated. Use [`block-export-add`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-export.block-export-add "QSD:block-export.block-export-add")
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
        - **mode** ([`BlockExportRemoveMode`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-export.BlockExportRemoveMode "QSD:block-export.BlockExportRemoveMode"), *optional*) – Mode of command operation. See [`BlockExportRemoveMode`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-export.BlockExportRemoveMode "QSD:block-export.BlockExportRemoveMode")
          description. Default is ‘safe’.

    Features:
    :   - **deprecated** – This command is deprecated. Use [`block-export-del`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-export.block-export-del "QSD:block-export.block-export-del")
          instead.

    Errors:
    :   - if the server is not running
        - if export is not found
        - if mode is ‘safe’ and there are existing connections

*Command* nbd-server-stop (Since: 1.3)
:   Stop QEMU’s embedded NBD server, and unregister all devices
    previously added via [`nbd-server-add`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-export.nbd-server-add "QSD:block-export.nbd-server-add").

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
    :   - **type** ([`BlockExportType`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-export.BlockExportType "QSD:block-export.BlockExportType")) – Block export type
        - **id** (`string`) – A unique identifier for the block export (across all export
          types)
        - **node-name** (`string`) – The node name of the block node to be exported
          (since: 5.2)
        - **writable** (`boolean`, *optional*) – True if clients should be able to write to the export
          (default false)
        - **writethrough** (`boolean`, *optional*) – If true, caches are flushed after every write request
          to the export before completion is signalled. (since: 5.2;
          default: false)
        - **iothread** ([`BlockExportIothreads`](qemu-storage-daemon-qmp-ref.md#alternate-QSD-block-export.BlockExportIothreads "QSD:block-export.BlockExportIothreads"), *optional*) – The name(s) of one or more iothread object(s) where the
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
        - When `type` is `nbd`: The members of [`BlockExportOptionsNbd`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-export.BlockExportOptionsNbd "QSD:block-export.BlockExportOptionsNbd").
        - When `type` is `vhost-user-blk`: The members of [`BlockExportOptionsVhostUserBlk`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-export.BlockExportOptionsVhostUserBlk "QSD:block-export.BlockExportOptionsVhostUserBlk").
        - When `type` is `fuse`: The members of [`BlockExportOptionsFuse`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-export.BlockExportOptionsFuse "QSD:block-export.BlockExportOptionsFuse").
        - When `type` is `vduse-blk`: The members of [`BlockExportOptionsVduseBlk`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-export.BlockExportOptionsVduseBlk "QSD:block-export.BlockExportOptionsVduseBlk").

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
    :   - The members of [`BlockExportOptions`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-export.BlockExportOptions "QSD:block-export.BlockExportOptions").

*Command* block-export-del (Since: 5.2)
:   Request to remove a block export. This drops the user’s reference
    to the export, but the export may still stay around after this
    command returns until the shutdown of the export has completed.

    Arguments:
    :   - **id** (`string`) – Block export id.
        - **mode** ([`BlockExportRemoveMode`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-export.BlockExportRemoveMode "QSD:block-export.BlockExportRemoveMode"), *optional*) – Mode of command operation. See [`BlockExportRemoveMode`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-export.BlockExportRemoveMode "QSD:block-export.BlockExportRemoveMode")
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
        - **type** ([`BlockExportType`](qemu-storage-daemon-qmp-ref.md#enum-QSD-block-export.BlockExportType "QSD:block-export.BlockExportType")) – The block export type
        - **node-name** (`string`) – The node name of the block node that is exported
        - **shutting-down** (`boolean`) – True if the export is shutting down (e.g. after a
          [`block-export-del`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-export.block-export-del "QSD:block-export.block-export-del") command, but before the shutdown has
          completed)

*Command* query-block-exports (Since: 5.2)
:   Return:
    :   `[`[`BlockExportInfo`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-export.BlockExportInfo "QSD:block-export.BlockExportInfo")`]` – A list describing all block exports

## [Character devices](qemu-storage-daemon-qmp-ref.md#id9)

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
    :   `[`[`ChardevInfo`](qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevInfo "QSD:char.ChardevInfo")`]`

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
    :   `[`[`ChardevBackendInfo`](qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevBackendInfo "QSD:char.ChardevBackendInfo")`]`

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
        - **format** ([`DataFormat`](qemu-storage-daemon-qmp-ref.md#enum-QSD-char.DataFormat "QSD:char.DataFormat"), *optional*) –

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
        - **format** ([`DataFormat`](qemu-storage-daemon-qmp-ref.md#enum-QSD-char.DataFormat "QSD:char.DataFormat"), *optional*) –

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
        - The members of [`ChardevCommon`](qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevCommon "QSD:char.ChardevCommon").

*Object* ChardevHostdev (Since: 1.4)
:   Configuration info for device and pipe chardevs.

    Members:
    :   - **device** (`string`) – The name of the special file for the device, i.e.
          /dev/ttyS0 on Unix or COM1: on Windows
        - The members of [`ChardevCommon`](qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevCommon "QSD:char.ChardevCommon").

*Object* ChardevSocket (Since: 1.4)
:   Configuration info for (stream) socket chardevs.

    Members:
    :   - **addr** ([`SocketAddressLegacy`](qemu-storage-daemon-qmp-ref.md#object-QSD-sockets.SocketAddressLegacy "QSD:sockets.SocketAddressLegacy")) – socket address to listen on (server=true) or connect to
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
        - The members of [`ChardevCommon`](qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevCommon "QSD:char.ChardevCommon").

*Object* ChardevUdp (Since: 1.5)
:   Configuration info for datagram socket chardevs.

    Members:
    :   - **remote** ([`SocketAddressLegacy`](qemu-storage-daemon-qmp-ref.md#object-QSD-sockets.SocketAddressLegacy "QSD:sockets.SocketAddressLegacy")) – remote address
        - **local** ([`SocketAddressLegacy`](qemu-storage-daemon-qmp-ref.md#object-QSD-sockets.SocketAddressLegacy "QSD:sockets.SocketAddressLegacy"), *optional*) – local address
        - The members of [`ChardevCommon`](qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevCommon "QSD:char.ChardevCommon").

*Object* ChardevMux (Since: 1.5)
:   Configuration info for mux chardevs.

    Members:
    :   - **chardev** (`string`) – name of the base chardev.
        - The members of [`ChardevCommon`](qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevCommon "QSD:char.ChardevCommon").

*Object* ChardevHub (Since: 10.0)
:   Configuration info for hub chardevs.

    Members:
    :   - **chardevs** (`[``string``]`) – IDs to be added to this hub (maximum 4 devices).
        - The members of [`ChardevCommon`](qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevCommon "QSD:char.ChardevCommon").

*Object* ChardevStdio (Since: 1.5)
:   Configuration info for stdio chardevs.

    Members:
    :   - **signal** (`boolean`, *optional*) – Allow signals (such as SIGINT triggered by ^C) be delivered
          to QEMU. Default: true.
        - The members of [`ChardevCommon`](qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevCommon "QSD:char.ChardevCommon").

*Object* ChardevSpiceChannel (Since: 1.5)
:   *Availability*: `CONFIG_SPICE`

    Configuration info for spice vm channel chardevs.

    Members:
    :   - **type** (`string`) – kind of channel (for example vdagent).
        - The members of [`ChardevCommon`](qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevCommon "QSD:char.ChardevCommon").

*Object* ChardevSpicePort (Since: 1.5)
:   *Availability*: `CONFIG_SPICE`

    Configuration info for spice port chardevs.

    Members:
    :   - **fqdn** (`string`) – name of the channel (see docs/spice-port-fqdn.txt)
        - The members of [`ChardevCommon`](qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevCommon "QSD:char.ChardevCommon").

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
        - **encoding** ([`ChardevVCEncoding`](qemu-storage-daemon-qmp-ref.md#enum-QSD-char.ChardevVCEncoding "QSD:char.ChardevVCEncoding"), *optional*) – character encoding the guest is expected to use
          (since 11.1)
        - The members of [`ChardevCommon`](qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevCommon "QSD:char.ChardevCommon").

*Object* ChardevVC (Since: 1.5)
:   Configuration info for virtual console chardevs.

    Members:
    :   - **width** (`int`, *optional*) – console width, in pixels
        - **height** (`int`, *optional*) – console height, in pixels
        - **cols** (`int`, *optional*) – console width, in chars
        - **rows** (`int`, *optional*) – console height, in chars
        - **encoding** ([`ChardevVCEncoding`](qemu-storage-daemon-qmp-ref.md#enum-QSD-char.ChardevVCEncoding "QSD:char.ChardevVCEncoding"), *optional*) – character encoding the guest is expected to use
          (since 11.1)
        - The members of [`ChardevCommon`](qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevCommon "QSD:char.ChardevCommon").

    > **Note:**
    >
    > The options are only effective when the VNC or SDL
    > graphical display backend is active. They are ignored with the
    > GTK, Spice, VNC and D-Bus display backends.

*Object* ChardevRingbuf (Since: 1.5)
:   Configuration info for ring buffer chardevs.

    Members:
    :   - **size** (`int`, *optional*) – ring buffer size, must be power of two, default is 65536
        - The members of [`ChardevCommon`](qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevCommon "QSD:char.ChardevCommon").

*Object* ChardevQemuVDAgent (Since: 6.1)
:   *Availability*: `CONFIG_SPICE_PROTOCOL`

    Configuration info for QEMU vdagent implementation.

    Members:
    :   - **mouse** (`boolean`, *optional*) – enable/disable mouse, default is enabled.
        - **clipboard** (`boolean`, *optional*) – enable/disable clipboard, default is disabled.
        - The members of [`ChardevCommon`](qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevCommon "QSD:char.ChardevCommon").

*Object* ChardevPty (Since: 9.2)
:   Configuration info for pty implementation.

    Members:
    :   - **path** (`string`, *optional*) – optional path to create a symbolic link that points to the
          allocated PTY
        - The members of [`ChardevCommon`](qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevCommon "QSD:char.ChardevCommon").

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
    :   - **data** ([`ChardevFile`](qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevFile "QSD:char.ChardevFile")) – Configuration info for file chardevs

*Object* ChardevHostdevWrapper (Since: 1.4)
:   Members:
    :   - **data** ([`ChardevHostdev`](qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevHostdev "QSD:char.ChardevHostdev")) – Configuration info for device and pipe chardevs

*Object* ChardevSocketWrapper (Since: 1.4)
:   Members:
    :   - **data** ([`ChardevSocket`](qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevSocket "QSD:char.ChardevSocket")) – Configuration info for (stream) socket chardevs

*Object* ChardevUdpWrapper (Since: 1.5)
:   Members:
    :   - **data** ([`ChardevUdp`](qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevUdp "QSD:char.ChardevUdp")) – Configuration info for datagram socket chardevs

*Object* ChardevCommonWrapper (Since: 2.6)
:   Members:
    :   - **data** ([`ChardevCommon`](qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevCommon "QSD:char.ChardevCommon")) – Configuration shared across all chardev backends

*Object* ChardevMuxWrapper (Since: 1.5)
:   Members:
    :   - **data** ([`ChardevMux`](qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevMux "QSD:char.ChardevMux")) – Configuration info for mux chardevs

*Object* ChardevHubWrapper (Since: 10.0)
:   Members:
    :   - **data** ([`ChardevHub`](qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevHub "QSD:char.ChardevHub")) – Configuration info for hub chardevs

*Object* ChardevStdioWrapper (Since: 1.5)
:   Members:
    :   - **data** ([`ChardevStdio`](qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevStdio "QSD:char.ChardevStdio")) – Configuration info for stdio chardevs

*Object* ChardevSpiceChannelWrapper (Since: 1.5)
:   *Availability*: `CONFIG_SPICE`

    Members:
    :   - **data** ([`ChardevSpiceChannel`](qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevSpiceChannel "QSD:char.ChardevSpiceChannel")) – Configuration info for spice vm channel chardevs

*Object* ChardevSpicePortWrapper (Since: 1.5)
:   *Availability*: `CONFIG_SPICE`

    Members:
    :   - **data** ([`ChardevSpicePort`](qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevSpicePort "QSD:char.ChardevSpicePort")) – Configuration info for spice port chardevs

*Object* ChardevQemuVDAgentWrapper (Since: 6.1)
:   *Availability*: `CONFIG_SPICE_PROTOCOL`

    Members:
    :   - **data** ([`ChardevQemuVDAgent`](qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevQemuVDAgent "QSD:char.ChardevQemuVDAgent")) – Configuration info for QEMU vdagent implementation

*Object* ChardevDBusWrapper (Since: 7.0)
:   *Availability*: `CONFIG_DBUS_DISPLAY`

    Members:
    :   - **data** ([`ChardevDBus`](qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevDBus "QSD:char.ChardevDBus")) – Configuration info for DBus chardevs

*Object* ChardevVCWrapper (Since: 1.5)
:   Members:
    :   - **data** ([`ChardevVC`](qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevVC "QSD:char.ChardevVC")) – Configuration info for virtual console chardevs

*Object* ChardevRingbufWrapper (Since: 1.5)
:   Members:
    :   - **data** ([`ChardevRingbuf`](qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevRingbuf "QSD:char.ChardevRingbuf")) – Configuration info for ring buffer chardevs

*Object* ChardevPtyWrapper (Since: 9.2)
:   Members:
    :   - **data** ([`ChardevPty`](qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevPty "QSD:char.ChardevPty")) – Configuration info for pty chardevs

*Object* ChardevBackend (Since: 1.4)
:   Configuration info for the new chardev backend.

    Members:
    :   - **type** ([`ChardevBackendKind`](qemu-storage-daemon-qmp-ref.md#enum-QSD-char.ChardevBackendKind "QSD:char.ChardevBackendKind")) – backend type
        - When `type` is `file`: The members of [`ChardevFileWrapper`](qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevFileWrapper "QSD:char.ChardevFileWrapper").
        - When `type` is `serial`: The members of [`ChardevHostdevWrapper`](qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevHostdevWrapper "QSD:char.ChardevHostdevWrapper").
        - When `type` is `parallel`: The members of [`ChardevHostdevWrapper`](qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevHostdevWrapper "QSD:char.ChardevHostdevWrapper").
        - When `type` is `pipe`: The members of [`ChardevHostdevWrapper`](qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevHostdevWrapper "QSD:char.ChardevHostdevWrapper").
        - When `type` is `socket`: The members of [`ChardevSocketWrapper`](qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevSocketWrapper "QSD:char.ChardevSocketWrapper").
        - When `type` is `udp`: The members of [`ChardevUdpWrapper`](qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevUdpWrapper "QSD:char.ChardevUdpWrapper").
        - When `type` is `pty`: The members of [`ChardevPtyWrapper`](qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevPtyWrapper "QSD:char.ChardevPtyWrapper").
        - When `type` is `null`: The members of [`ChardevCommonWrapper`](qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevCommonWrapper "QSD:char.ChardevCommonWrapper").
        - When `type` is `mux`: The members of [`ChardevMuxWrapper`](qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevMuxWrapper "QSD:char.ChardevMuxWrapper").
        - When `type` is `hub`: The members of [`ChardevHubWrapper`](qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevHubWrapper "QSD:char.ChardevHubWrapper").
        - When `type` is `msmouse`: The members of [`ChardevCommonWrapper`](qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevCommonWrapper "QSD:char.ChardevCommonWrapper").
        - When `type` is `wctablet`: The members of [`ChardevCommonWrapper`](qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevCommonWrapper "QSD:char.ChardevCommonWrapper").
        - When `type` is `braille`: The members of [`ChardevCommonWrapper`](qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevCommonWrapper "QSD:char.ChardevCommonWrapper").
        - When `type` is `testdev`: The members of [`ChardevCommonWrapper`](qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevCommonWrapper "QSD:char.ChardevCommonWrapper").
        - When `type` is `stdio`: The members of [`ChardevStdioWrapper`](qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevStdioWrapper "QSD:char.ChardevStdioWrapper").
        - When `type` is `console`: The members of [`ChardevCommonWrapper`](qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevCommonWrapper "QSD:char.ChardevCommonWrapper").
        - When `type` is `spicevmc`: The members of [`ChardevSpiceChannelWrapper`](qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevSpiceChannelWrapper "QSD:char.ChardevSpiceChannelWrapper").
        - When `type` is `spiceport`: The members of [`ChardevSpicePortWrapper`](qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevSpicePortWrapper "QSD:char.ChardevSpicePortWrapper").
        - When `type` is `qemu-vdagent`: The members of [`ChardevQemuVDAgentWrapper`](qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevQemuVDAgentWrapper "QSD:char.ChardevQemuVDAgentWrapper").
        - When `type` is `dbus`: The members of [`ChardevDBusWrapper`](qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevDBusWrapper "QSD:char.ChardevDBusWrapper").
        - When `type` is `vc`: The members of [`ChardevVCWrapper`](qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevVCWrapper "QSD:char.ChardevVCWrapper").
        - When `type` is `ringbuf`: The members of [`ChardevRingbufWrapper`](qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevRingbufWrapper "QSD:char.ChardevRingbufWrapper").
        - When `type` is `memory`: The members of [`ChardevRingbufWrapper`](qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevRingbufWrapper "QSD:char.ChardevRingbufWrapper").

*Object* ChardevReturn (Since: 1.4)
:   Return info about the chardev backend just created.

    Members:
    :   - **pty** (`string`, *optional*) – name of the slave pseudoterminal device, present if and only
          if a chardev of type ‘pty’ was created

*Command* chardev-add (Since: 1.4)
:   Add a character device backend

    Arguments:
    :   - **id** (`string`) – the chardev’s ID, must be unique
        - **backend** ([`ChardevBackend`](qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevBackend "QSD:char.ChardevBackend")) – backend type and parameters

    Return:
    :   [`ChardevReturn`](qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevReturn "QSD:char.ChardevReturn")

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
        - **backend** ([`ChardevBackend`](qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevBackend "QSD:char.ChardevBackend")) – new backend type and parameters

    Return:
    :   [`ChardevReturn`](qemu-storage-daemon-qmp-ref.md#object-QSD-char.ChardevReturn "QSD:char.ChardevReturn")

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

## [User authorization](qemu-storage-daemon-qmp-ref.md#id10)

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
        - **policy** ([`QAuthZListPolicy`](qemu-storage-daemon-qmp-ref.md#enum-QSD-authz.QAuthZListPolicy "QSD:authz.QAuthZListPolicy")) – the result to return if `match` evaluates to true
        - **format** ([`QAuthZListFormat`](qemu-storage-daemon-qmp-ref.md#enum-QSD-authz.QAuthZListFormat "QSD:authz.QAuthZListFormat"), *optional*) – the format of the `match` rule (default ‘exact’)

*Object* AuthZListProperties (Since: 4.0)
:   Properties for authz-list objects.

    Members:
    :   - **policy** ([`QAuthZListPolicy`](qemu-storage-daemon-qmp-ref.md#enum-QSD-authz.QAuthZListPolicy "QSD:authz.QAuthZListPolicy"), *optional*) – Default policy to apply when no rule matches (default:
          deny)
        - **rules** (`[`[`QAuthZListRule`](qemu-storage-daemon-qmp-ref.md#object-QSD-authz.QAuthZListRule "QSD:authz.QAuthZListRule")`]`, *optional*) – Authorization rules based on matching user

*Object* AuthZListFileProperties (Since: 4.0)
:   Properties for authz-listfile objects.

    Members:
    :   - **filename** (`string`) – File name to load the configuration from. The file must
          contain valid JSON for [`AuthZListProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-authz.AuthZListProperties "QSD:authz.AuthZListProperties").
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

## [Transactions](qemu-storage-daemon-qmp-ref.md#id11)

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
    :   - **deprecated** – Member [`drive-backup`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.drive-backup "QSD:block-core.drive-backup") is deprecated. Use member
          [`blockdev-backup`](qemu-storage-daemon-qmp-ref.md#command-QSD-block-core.blockdev-backup "QSD:block-core.blockdev-backup") instead.

*Object* AbortWrapper (Since: 1.6)
:   Members:
    :   - **data** ([`Abort`](qemu-storage-daemon-qmp-ref.md#object-QSD-transaction.Abort "QSD:transaction.Abort")) – Not documented

*Object* BlockDirtyBitmapAddWrapper (Since: 2.5)
:   Members:
    :   - **data** ([`BlockDirtyBitmapAdd`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockDirtyBitmapAdd "QSD:block-core.BlockDirtyBitmapAdd")) – Not documented

*Object* BlockDirtyBitmapWrapper (Since: 2.5)
:   Members:
    :   - **data** ([`BlockDirtyBitmap`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockDirtyBitmap "QSD:block-core.BlockDirtyBitmap")) – Not documented

*Object* BlockDirtyBitmapMergeWrapper (Since: 4.0)
:   Members:
    :   - **data** ([`BlockDirtyBitmapMerge`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockDirtyBitmapMerge "QSD:block-core.BlockDirtyBitmapMerge")) – Not documented

*Object* BlockdevBackupWrapper (Since: 2.3)
:   Members:
    :   - **data** ([`BlockdevBackup`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevBackup "QSD:block-core.BlockdevBackup")) – Not documented

*Object* BlockdevSnapshotWrapper (Since: 2.5)
:   Members:
    :   - **data** ([`BlockdevSnapshot`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevSnapshot "QSD:block-core.BlockdevSnapshot")) – Not documented

*Object* BlockdevSnapshotInternalWrapper (Since: 1.7)
:   Members:
    :   - **data** ([`BlockdevSnapshotInternal`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevSnapshotInternal "QSD:block-core.BlockdevSnapshotInternal")) – Not documented

*Object* BlockdevSnapshotSyncWrapper (Since: 1.1)
:   Members:
    :   - **data** ([`BlockdevSnapshotSync`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.BlockdevSnapshotSync "QSD:block-core.BlockdevSnapshotSync")) – Not documented

*Object* DriveBackupWrapper (Since: 1.6)
:   Members:
    :   - **data** ([`DriveBackup`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.DriveBackup "QSD:block-core.DriveBackup")) – Not documented

*Object* TransactionAction (Since: 1.1)
:   A discriminated record of operations that can be performed with
    [`transaction`](qemu-storage-daemon-qmp-ref.md#command-QSD-transaction.transaction "QSD:transaction.transaction").

    Members:
    :   - **type** ([`TransactionActionKind`](qemu-storage-daemon-qmp-ref.md#enum-QSD-transaction.TransactionActionKind "QSD:transaction.TransactionActionKind")) – the operation to be performed
        - When `type` is `abort`: The members of [`AbortWrapper`](qemu-storage-daemon-qmp-ref.md#object-QSD-transaction.AbortWrapper "QSD:transaction.AbortWrapper").
        - When `type` is `block-dirty-bitmap-add`: The members of [`BlockDirtyBitmapAddWrapper`](qemu-storage-daemon-qmp-ref.md#object-QSD-transaction.BlockDirtyBitmapAddWrapper "QSD:transaction.BlockDirtyBitmapAddWrapper").
        - When `type` is `block-dirty-bitmap-remove`: The members of [`BlockDirtyBitmapWrapper`](qemu-storage-daemon-qmp-ref.md#object-QSD-transaction.BlockDirtyBitmapWrapper "QSD:transaction.BlockDirtyBitmapWrapper").
        - When `type` is `block-dirty-bitmap-clear`: The members of [`BlockDirtyBitmapWrapper`](qemu-storage-daemon-qmp-ref.md#object-QSD-transaction.BlockDirtyBitmapWrapper "QSD:transaction.BlockDirtyBitmapWrapper").
        - When `type` is `block-dirty-bitmap-enable`: The members of [`BlockDirtyBitmapWrapper`](qemu-storage-daemon-qmp-ref.md#object-QSD-transaction.BlockDirtyBitmapWrapper "QSD:transaction.BlockDirtyBitmapWrapper").
        - When `type` is `block-dirty-bitmap-disable`: The members of [`BlockDirtyBitmapWrapper`](qemu-storage-daemon-qmp-ref.md#object-QSD-transaction.BlockDirtyBitmapWrapper "QSD:transaction.BlockDirtyBitmapWrapper").
        - When `type` is `block-dirty-bitmap-merge`: The members of [`BlockDirtyBitmapMergeWrapper`](qemu-storage-daemon-qmp-ref.md#object-QSD-transaction.BlockDirtyBitmapMergeWrapper "QSD:transaction.BlockDirtyBitmapMergeWrapper").
        - When `type` is `blockdev-backup`: The members of [`BlockdevBackupWrapper`](qemu-storage-daemon-qmp-ref.md#object-QSD-transaction.BlockdevBackupWrapper "QSD:transaction.BlockdevBackupWrapper").
        - When `type` is `blockdev-snapshot`: The members of [`BlockdevSnapshotWrapper`](qemu-storage-daemon-qmp-ref.md#object-QSD-transaction.BlockdevSnapshotWrapper "QSD:transaction.BlockdevSnapshotWrapper").
        - When `type` is `blockdev-snapshot-internal-sync`: The members of [`BlockdevSnapshotInternalWrapper`](qemu-storage-daemon-qmp-ref.md#object-QSD-transaction.BlockdevSnapshotInternalWrapper "QSD:transaction.BlockdevSnapshotInternalWrapper").
        - When `type` is `blockdev-snapshot-sync`: The members of [`BlockdevSnapshotSyncWrapper`](qemu-storage-daemon-qmp-ref.md#object-QSD-transaction.BlockdevSnapshotSyncWrapper "QSD:transaction.BlockdevSnapshotSyncWrapper").
        - When `type` is `drive-backup`: The members of [`DriveBackupWrapper`](qemu-storage-daemon-qmp-ref.md#object-QSD-transaction.DriveBackupWrapper "QSD:transaction.DriveBackupWrapper").

*Object* TransactionProperties (Since: 2.5)
:   Optional arguments to modify the behavior of a Transaction.

    Members:
    :   - **completion-mode** ([`ActionCompletionMode`](qemu-storage-daemon-qmp-ref.md#enum-QSD-transaction.ActionCompletionMode "QSD:transaction.ActionCompletionMode"), *optional*) – Controls how jobs launched asynchronously by
          Actions will complete or fail as a group. See
          [`ActionCompletionMode`](qemu-storage-daemon-qmp-ref.md#enum-QSD-transaction.ActionCompletionMode "QSD:transaction.ActionCompletionMode") for details.

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
    :   - **actions** (`[`[`TransactionAction`](qemu-storage-daemon-qmp-ref.md#object-QSD-transaction.TransactionAction "QSD:transaction.TransactionAction")`]`) – List of [`TransactionAction`](qemu-storage-daemon-qmp-ref.md#object-QSD-transaction.TransactionAction "QSD:transaction.TransactionAction"); information needed for the
          respective operations.
        - **properties** ([`TransactionProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-transaction.TransactionProperties "QSD:transaction.TransactionProperties"), *optional*) – structure of additional options to control the
          execution of the transaction. See [`TransactionProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-transaction.TransactionProperties "QSD:transaction.TransactionProperties") for
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

## [QMP monitor control](qemu-storage-daemon-qmp-ref.md#id12)

*Command* qmp_capabilities (Since: 0.13)
:   Enable QMP capabilities.

    Arguments:
    :   - **enable** (`[`[`QMPCapability`](qemu-storage-daemon-qmp-ref.md#enum-QSD-control.QMPCapability "QSD:control.QMPCapability")`]`, *optional*) – An optional list of [`QMPCapability`](qemu-storage-daemon-qmp-ref.md#enum-QSD-control.QMPCapability "QSD:control.QMPCapability") values to enable. The
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
    :   - **qemu** ([`VersionTriple`](qemu-storage-daemon-qmp-ref.md#object-QSD-control.VersionTriple "QSD:control.VersionTriple")) – The version of QEMU. By current convention, a micro version
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
    :   [`VersionInfo`](qemu-storage-daemon-qmp-ref.md#object-QSD-control.VersionInfo "QSD:control.VersionInfo") – An object describing the current version of QEMU.

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
    :   `[`[`CommandInfo`](qemu-storage-daemon-qmp-ref.md#object-QSD-control.CommandInfo "QSD:control.CommandInfo")`]` – A list of all supported commands

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
        - **mode** ([`MonitorMode`](qemu-storage-daemon-qmp-ref.md#enum-QSD-control.MonitorMode "QSD:control.MonitorMode"), *optional*) – Selects the monitor mode (default: readline in the system
          emulator, control in qemu-storage-daemon)
        - **pretty** (`boolean`, *optional*) – Enables pretty printing (QMP only)
        - **chardev** (`string`) – Name of a character device to expose the monitor on

## [QMP introspection](qemu-storage-daemon-qmp-ref.md#id13)

*Command* query-qmp-schema (Since: 2.5)
:   Command [`query-qmp-schema`](qemu-storage-daemon-qmp-ref.md#command-QSD-introspect.query-qmp-schema "QSD:introspect.query-qmp-schema") exposes the QMP wire ABI as an array of
    [`SchemaInfo`](qemu-storage-daemon-qmp-ref.md#object-QSD-introspect.SchemaInfo "QSD:introspect.SchemaInfo"). This lets QMP clients figure out what commands and
    events are available in this QEMU, and their parameters and results.

    However, the [`SchemaInfo`](qemu-storage-daemon-qmp-ref.md#object-QSD-introspect.SchemaInfo "QSD:introspect.SchemaInfo") can’t reflect all the rules and
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
    :   `[`[`SchemaInfo`](qemu-storage-daemon-qmp-ref.md#object-QSD-introspect.SchemaInfo "QSD:introspect.SchemaInfo")`]` –

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
:   This is a [`SchemaInfo`](qemu-storage-daemon-qmp-ref.md#object-QSD-introspect.SchemaInfo "QSD:introspect.SchemaInfo")’s meta type, i.e. the kind of entity it
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
    :   - **name** (`string`) – the entity’s name, inherited from `base`. The [`SchemaInfo`](qemu-storage-daemon-qmp-ref.md#object-QSD-introspect.SchemaInfo "QSD:introspect.SchemaInfo") is
          always referenced by this name. Commands and events have the
          name defined in the QAPI schema. Unlike command and event
          names, type names are not part of the wire ABI. Consequently,
          type names are meaningless strings here, although they are still
          guaranteed unique regardless of `meta-type`.
        - **meta-type** ([`SchemaMetaType`](qemu-storage-daemon-qmp-ref.md#enum-QSD-introspect.SchemaMetaType "QSD:introspect.SchemaMetaType")) – the entity’s meta type, inherited from `base`.
        - **features** (`[``string``]`, *optional*) – names of features associated with the entity, in no
          particular order. (since 4.1 for object types, 4.2 for
          commands, 5.0 for the rest)
        - When `meta-type` is `builtin`: The members of [`SchemaInfoBuiltin`](qemu-storage-daemon-qmp-ref.md#object-QSD-introspect.SchemaInfoBuiltin "QSD:introspect.SchemaInfoBuiltin").
        - When `meta-type` is `enum`: The members of [`SchemaInfoEnum`](qemu-storage-daemon-qmp-ref.md#object-QSD-introspect.SchemaInfoEnum "QSD:introspect.SchemaInfoEnum").
        - When `meta-type` is `array`: The members of [`SchemaInfoArray`](qemu-storage-daemon-qmp-ref.md#object-QSD-introspect.SchemaInfoArray "QSD:introspect.SchemaInfoArray").
        - When `meta-type` is `object`: The members of [`SchemaInfoObject`](qemu-storage-daemon-qmp-ref.md#object-QSD-introspect.SchemaInfoObject "QSD:introspect.SchemaInfoObject").
        - When `meta-type` is `alternate`: The members of [`SchemaInfoAlternate`](qemu-storage-daemon-qmp-ref.md#object-QSD-introspect.SchemaInfoAlternate "QSD:introspect.SchemaInfoAlternate").
        - When `meta-type` is `command`: The members of [`SchemaInfoCommand`](qemu-storage-daemon-qmp-ref.md#object-QSD-introspect.SchemaInfoCommand "QSD:introspect.SchemaInfoCommand").
        - When `meta-type` is `event`: The members of [`SchemaInfoEvent`](qemu-storage-daemon-qmp-ref.md#object-QSD-introspect.SchemaInfoEvent "QSD:introspect.SchemaInfoEvent").

*Object* SchemaInfoBuiltin (Since: 2.5)
:   Additional [`SchemaInfo`](qemu-storage-daemon-qmp-ref.md#object-QSD-introspect.SchemaInfo "QSD:introspect.SchemaInfo") members for meta-type ‘builtin’.

    Members:
    :   - **json-type** ([`JSONType`](qemu-storage-daemon-qmp-ref.md#enum-QSD-introspect.JSONType "QSD:introspect.JSONType")) – the JSON type used for this type on the wire.

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
:   Additional [`SchemaInfo`](qemu-storage-daemon-qmp-ref.md#object-QSD-introspect.SchemaInfo "QSD:introspect.SchemaInfo") members for meta-type ‘enum’.

    Members:
    :   - **members** (`[`[`SchemaInfoEnumMember`](qemu-storage-daemon-qmp-ref.md#object-QSD-introspect.SchemaInfoEnumMember "QSD:introspect.SchemaInfoEnumMember")`]`) – the enum type’s members, in no particular order.
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
:   Additional [`SchemaInfo`](qemu-storage-daemon-qmp-ref.md#object-QSD-introspect.SchemaInfo "QSD:introspect.SchemaInfo") members for meta-type ‘array’.

    Members:
    :   - **element-type** (`string`) – the array type’s element type.

    Values of this type are JSON array on the wire.

*Object* SchemaInfoObject (Since: 2.5)
:   Additional [`SchemaInfo`](qemu-storage-daemon-qmp-ref.md#object-QSD-introspect.SchemaInfo "QSD:introspect.SchemaInfo") members for meta-type ‘object’.

    Members:
    :   - **members** (`[`[`SchemaInfoObjectMember`](qemu-storage-daemon-qmp-ref.md#object-QSD-introspect.SchemaInfoObjectMember "QSD:introspect.SchemaInfoObjectMember")`]`) – the object type’s (non-variant) members, in no particular
          order.
        - **tag** (`string`, *optional*) – the name of the member serving as type tag. An element of
          `members` with this name must exist.
        - **variants** (`[`[`SchemaInfoObjectVariant`](qemu-storage-daemon-qmp-ref.md#object-QSD-introspect.SchemaInfoObjectVariant "QSD:introspect.SchemaInfoObjectVariant")`]`, *optional*) – variant members, i.e. additional members that depend on
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
:   Additional [`SchemaInfo`](qemu-storage-daemon-qmp-ref.md#object-QSD-introspect.SchemaInfo "QSD:introspect.SchemaInfo") members for meta-type ‘alternate’.

    Members:
    :   - **members** (`[`[`SchemaInfoAlternateMember`](qemu-storage-daemon-qmp-ref.md#object-QSD-introspect.SchemaInfoAlternateMember "QSD:introspect.SchemaInfoAlternateMember")`]`) – the alternate type’s members, in no particular order. The
          members’ wire encoding is distinct, see
          [How to use the QAPI code generator](../devel/qapi-code-gen.md) section Alternate types.

    On the wire, this can be any of the members.

*Object* SchemaInfoAlternateMember (Since: 2.5)
:   An alternate member.

    Members:
    :   - **type** (`string`) – the name of the member’s type.

*Object* SchemaInfoCommand (Since: 2.5)
:   Additional [`SchemaInfo`](qemu-storage-daemon-qmp-ref.md#object-QSD-introspect.SchemaInfo "QSD:introspect.SchemaInfo") members for meta-type ‘command’.

    Members:
    :   - **arg-type** (`string`) – the name of the object type that provides the command’s
          parameters.
        - **ret-type** (`string`) – the name of the command’s result type.
        - **allow-oob** (`boolean`, *optional*) – whether the command allows out-of-band execution,
          defaults to false (Since: 2.12)

*Object* SchemaInfoEvent (Since: 2.5)
:   Additional [`SchemaInfo`](qemu-storage-daemon-qmp-ref.md#object-QSD-introspect.SchemaInfo "QSD:introspect.SchemaInfo") members for meta-type ‘event’.

    Members:
    :   - **arg-type** (`string`) – the name of the object type that provides the event’s
          parameters.

## [QEMU Object Model (QOM)](qemu-storage-daemon-qmp-ref.md#id14)

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
          [`ObjectPropertyInfo`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.ObjectPropertyInfo "QSD:qom.ObjectPropertyInfo").
        - **value** (`value`, *optional*) – the value of the property. Absent when the property cannot
          be read.

*Object* ObjectPropertiesValues (Since: 10.1)
:   Members:
    :   - **properties** (`[`[`ObjectPropertyValue`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.ObjectPropertyValue "QSD:qom.ObjectPropertyValue")`]`) – a list of properties.

*Command* qom-list (Since: 1.2)
:   List properties of a object given a path in the object model.

    Arguments:
    :   - **path** (`string`) – the path within the object model. See [`qom-get`](qemu-storage-daemon-qmp-ref.md#command-QSD-qom.qom-get "QSD:qom.qom-get") for a
          description of this parameter.

    Return:
    :   `[`[`ObjectPropertyInfo`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.ObjectPropertyInfo "QSD:qom.ObjectPropertyInfo")`]` – a list that describe the properties of the object.

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
          in [`qom-get`](qemu-storage-daemon-qmp-ref.md#command-QSD-qom.qom-get "QSD:qom.qom-get").

    Errors:
    :   - If any path is not valid or is ambiguous

    Return:
    :   `[`[`ObjectPropertiesValues`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.ObjectPropertiesValues "QSD:qom.ObjectPropertiesValues")`]` – A list where each element is the result for the
        corresponding element of `paths`.

*Command* qom-set (Since: 1.2)
:   Set a property value.

    Arguments:
    :   - **path** (`string`) – see [`qom-get`](qemu-storage-daemon-qmp-ref.md#command-QSD-qom.qom-get "QSD:qom.qom-get") for a description of this parameter
        - **property** (`string`) – the property name to set
        - **value** (`value`) – a value who’s type is appropriate for the property type.
          See [`qom-get`](qemu-storage-daemon-qmp-ref.md#command-QSD-qom.qom-get "QSD:qom.qom-get") for a description of type mapping.

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
:   This structure describes a search result from [`qom-list-types`](qemu-storage-daemon-qmp-ref.md#command-QSD-qom.qom-list-types "QSD:qom.qom-list-types")

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
    :   `[`[`ObjectTypeInfo`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.ObjectTypeInfo "QSD:qom.ObjectTypeInfo")`]` – a list of types, or an empty list if no results are found

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
    :   `[`[`ObjectPropertyInfo`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.ObjectPropertyInfo "QSD:qom.ObjectPropertyInfo")`]` – a list describing object properties

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
        - The members of [`CryptodevBackendProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.CryptodevBackendProperties "QSD:qom.CryptodevBackendProperties").

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
        - **queue** ([`NetFilterDirection`](qemu-storage-daemon-qmp-ref.md#enum-QSD-common.NetFilterDirection "QSD:common.NetFilterDirection"), *optional*) – indicates which queue(s) to filter (default: all)
        - **status** (`string`, *optional*) – indicates whether the filter is enabled (“on”) or disabled
          (“off”) (default: “on”)
        - **position** (`string`, *optional*) – specifies where the filter should be inserted in the
          filter list. “head” means the filter is inserted at the head of
          the filter list, before any existing filters. “tail” means the
          filter is inserted at the tail of the filter list, behind any
          existing filters (default). “id=<id>” means the filter is
          inserted before or behind the filter specified by <id>,
          depending on the `insert` property. (default: “tail”)
        - **insert** ([`NetfilterInsert`](qemu-storage-daemon-qmp-ref.md#enum-QSD-qom.NetfilterInsert "QSD:qom.NetfilterInsert"), *optional*) – where to insert the filter relative to the filter given in
          `position`. Ignored if `position` is “head” or “tail”.
          (default: behind)

*Object* FilterBufferProperties (Since: 2.5)
:   Properties for filter-buffer objects.

    Members:
    :   - **interval** (`int`) – a non-zero interval in microseconds. All packets
          arriving in the given interval are delayed until the end of the
          interval.
        - The members of [`NetfilterProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.NetfilterProperties "QSD:qom.NetfilterProperties").

*Object* FilterDumpProperties (Since: 2.5)
:   Properties for filter-dump objects.

    Members:
    :   - **file** (`string`) – the filename where the dumped packets should be stored
        - **maxlen** (`int`, *optional*) – maximum number of bytes in a packet that are stored
          (default: 65536)
        - The members of [`NetfilterProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.NetfilterProperties "QSD:qom.NetfilterProperties").

*Object* FilterMirrorProperties (Since: 2.6)
:   Properties for filter-mirror objects.

    Members:
    :   - **outdev** (`string`) – the name of a character device backend to which all
          incoming packets are mirrored
        - **vnet_hdr_support** (`boolean`, *optional*) – if true, vnet header support is enabled
          (default: false)
        - The members of [`NetfilterProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.NetfilterProperties "QSD:qom.NetfilterProperties").

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
        - The members of [`NetfilterProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.NetfilterProperties "QSD:qom.NetfilterProperties").

*Object* FilterRewriterProperties (Since: 2.8)
:   Properties for filter-rewriter objects.

    Members:
    :   - **vnet_hdr_support** (`boolean`, *optional*) – if true, vnet header support is enabled
          (default: false)
        - The members of [`NetfilterProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.NetfilterProperties "QSD:qom.NetfilterProperties").

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
        - **grab-toggle** ([`GrabToggleKeys`](qemu-storage-daemon-qmp-ref.md#enum-QSD-common.GrabToggleKeys "QSD:common.GrabToggleKeys"), *optional*) – the key or key combination that toggles device grab
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
        - The members of [`EventLoopBaseProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.EventLoopBaseProperties "QSD:qom.EventLoopBaseProperties").

    The `aio-max-batch` option is available since 6.1.

*Object* MainLoopProperties (Since: 7.1)
:   Properties for the main-loop object.

    Members:
    :   - The members of [`EventLoopBaseProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.EventLoopBaseProperties "QSD:qom.EventLoopBaseProperties").

*Object* MemoryBackendProperties (Since: 2.1)
:   Properties for objects of classes derived from memory-backend.

    Members:
    :   - **merge** (`boolean`, *optional*) – if true, mark the memory as mergeable (default depends on
          the machine type)
        - **dump** (`boolean`, *optional*) – if true, include the memory in core dumps (default depends on
          the machine type)
        - **host-nodes** (`[``int``]`, *optional*) – the list of NUMA host nodes to bind the memory to
        - **policy** ([`HostMemPolicy`](qemu-storage-daemon-qmp-ref.md#enum-QSD-common.HostMemPolicy "QSD:common.HostMemPolicy"), *optional*) – the NUMA policy (default: ‘default’)
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
        - **rom** ([`OnOffAuto`](qemu-storage-daemon-qmp-ref.md#enum-QSD-common.OnOffAuto "QSD:common.OnOffAuto"), *optional*) – whether to create Read Only Memory (ROM) that cannot be
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
        - The members of [`MemoryBackendProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.MemoryBackendProperties "QSD:qom.MemoryBackendProperties").

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
        - The members of [`MemoryBackendProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.MemoryBackendProperties "QSD:qom.MemoryBackendProperties").

*Object* MemoryBackendShmProperties (Since: 9.1)
:   *Availability*: `CONFIG_POSIX`

    Properties for memory-backend-shm objects.

    This memory backend supports only shared memory, which is the
    default.

    Members:
    :   - The members of [`MemoryBackendProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.MemoryBackendProperties "QSD:qom.MemoryBackendProperties").

*Object* MemoryBackendEpcProperties (Since: 6.2)
:   *Availability*: `CONFIG_LINUX`

    Properties for memory-backend-epc objects.

    The `merge` boolean option is false by default with epc

    The `dump` boolean option is false by default with epc

    Members:
    :   - The members of [`MemoryBackendProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.MemoryBackendProperties "QSD:qom.MemoryBackendProperties").

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
    :   - **socket** ([`SocketAddress`](qemu-storage-daemon-qmp-ref.md#object-QSD-sockets.SocketAddress "QSD:sockets.SocketAddress")) – socket to be used by the libvfio-user library
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
        - The members of [`RngProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.RngProperties "QSD:qom.RngProperties").

*Object* RngRandomProperties (Since: 1.3)
:   *Availability*: `CONFIG_POSIX`

    Properties for rng-random objects.

    Members:
    :   - **filename** (`string`, *optional*) – the filename of the device on the host to obtain entropy
          from (default: “/dev/urandom”)
        - The members of [`RngProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.RngProperties "QSD:qom.RngProperties").

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
        - **legacy-vm-type** ([`OnOffAuto`](qemu-storage-daemon-qmp-ref.md#enum-QSD-common.OnOffAuto "QSD:common.OnOffAuto"), *optional*) – Use legacy KVM_SEV_INIT KVM interface for creating
          the VM. The newer KVM_SEV_INIT2 interface, from Linux >= 6.10,
          syncs additional vCPU state when initializing the VMSA
          structures, which will result in a different guest measurement.
          Set this to ‘on’ to force compatibility with older QEMU or kernel
          versions that rely on legacy KVM_SEV_INIT behavior. ‘auto’ will
          behave identically to ‘on’, but will automatically switch to
          using KVM_SEV_INIT2 if the user specifies any additional options
          that require it. If set to ‘off’, QEMU will require
          KVM_SEV_INIT2 unconditionally. (default: off) (since 9.1)
        - The members of [`SevCommonProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.SevCommonProperties "QSD:qom.SevCommonProperties").

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
        - The members of [`SevCommonProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.SevCommonProperties "QSD:qom.SevCommonProperties").

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
        - **quote-generation-socket** ([`SocketAddress`](qemu-storage-daemon-qmp-ref.md#object-QSD-sockets.SocketAddress "QSD:sockets.SocketAddress"), *optional*) – socket address for Quote Generation
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
        - The members of [`MonitorProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.MonitorProperties "QSD:qom.MonitorProperties").

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
        - **close-action** ([`MonitorQMPCloseAction`](qemu-storage-daemon-qmp-ref.md#enum-QSD-qom.MonitorQMPCloseAction "QSD:qom.MonitorQMPCloseAction"), *optional*) – action to take when the character device backend is
          closed (default: none)
        - The members of [`MonitorProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.MonitorProperties "QSD:qom.MonitorProperties").

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
    :   - **qom-type** ([`ObjectType`](qemu-storage-daemon-qmp-ref.md#enum-QSD-qom.ObjectType "QSD:qom.ObjectType")) – the class name for the object to be created
        - **id** (`string`) – the name of the new object
        - When `qom-type` is `acpi-generic-initiator`: The members of [`AcpiGenericInitiatorProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.AcpiGenericInitiatorProperties "QSD:qom.AcpiGenericInitiatorProperties").
        - When `qom-type` is `acpi-generic-port`: The members of [`AcpiGenericPortProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.AcpiGenericPortProperties "QSD:qom.AcpiGenericPortProperties").
        - When `qom-type` is `authz-list`: The members of [`AuthZListProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-authz.AuthZListProperties "QSD:authz.AuthZListProperties").
        - When `qom-type` is `authz-listfile`: The members of [`AuthZListFileProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-authz.AuthZListFileProperties "QSD:authz.AuthZListFileProperties").
        - When `qom-type` is `authz-pam`: The members of [`AuthZPAMProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-authz.AuthZPAMProperties "QSD:authz.AuthZPAMProperties").
        - When `qom-type` is `authz-simple`: The members of [`AuthZSimpleProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-authz.AuthZSimpleProperties "QSD:authz.AuthZSimpleProperties").
        - When `qom-type` is `can-host-socketcan`: The members of [`CanHostSocketcanProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.CanHostSocketcanProperties "QSD:qom.CanHostSocketcanProperties").
        - When `qom-type` is `colo-compare`: The members of [`ColoCompareProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.ColoCompareProperties "QSD:qom.ColoCompareProperties").
        - When `qom-type` is `cryptodev-backend`: The members of [`CryptodevBackendProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.CryptodevBackendProperties "QSD:qom.CryptodevBackendProperties").
        - When `qom-type` is `cryptodev-backend-builtin`: The members of [`CryptodevBackendProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.CryptodevBackendProperties "QSD:qom.CryptodevBackendProperties").
        - When `qom-type` is `cryptodev-backend-lkcf`: The members of [`CryptodevBackendProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.CryptodevBackendProperties "QSD:qom.CryptodevBackendProperties").
        - When `qom-type` is `cryptodev-vhost-user`: The members of [`CryptodevVhostUserProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.CryptodevVhostUserProperties "QSD:qom.CryptodevVhostUserProperties").
        - When `qom-type` is `dbus-vmstate`: The members of [`DBusVMStateProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.DBusVMStateProperties "QSD:qom.DBusVMStateProperties").
        - When `qom-type` is `filter-buffer`: The members of [`FilterBufferProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.FilterBufferProperties "QSD:qom.FilterBufferProperties").
        - When `qom-type` is `filter-dump`: The members of [`FilterDumpProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.FilterDumpProperties "QSD:qom.FilterDumpProperties").
        - When `qom-type` is `filter-mirror`: The members of [`FilterMirrorProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.FilterMirrorProperties "QSD:qom.FilterMirrorProperties").
        - When `qom-type` is `filter-redirector`: The members of [`FilterRedirectorProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.FilterRedirectorProperties "QSD:qom.FilterRedirectorProperties").
        - When `qom-type` is `filter-replay`: The members of [`NetfilterProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.NetfilterProperties "QSD:qom.NetfilterProperties").
        - When `qom-type` is `filter-rewriter`: The members of [`FilterRewriterProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.FilterRewriterProperties "QSD:qom.FilterRewriterProperties").
        - When `qom-type` is `igvm-cfg`: The members of [`IgvmCfgProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.IgvmCfgProperties "QSD:qom.IgvmCfgProperties").
        - When `qom-type` is `input-barrier`: The members of [`InputBarrierProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.InputBarrierProperties "QSD:qom.InputBarrierProperties").
        - When `qom-type` is `input-linux`: The members of [`InputLinuxProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.InputLinuxProperties "QSD:qom.InputLinuxProperties").
        - When `qom-type` is `iommufd`: The members of [`IOMMUFDProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.IOMMUFDProperties "QSD:qom.IOMMUFDProperties").
        - When `qom-type` is `iothread`: The members of [`IothreadProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.IothreadProperties "QSD:qom.IothreadProperties").
        - When `qom-type` is `main-loop`: The members of [`MainLoopProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.MainLoopProperties "QSD:qom.MainLoopProperties").
        - When `qom-type` is `memory-backend-epc`: The members of [`MemoryBackendEpcProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.MemoryBackendEpcProperties "QSD:qom.MemoryBackendEpcProperties").
        - When `qom-type` is `memory-backend-file`: The members of [`MemoryBackendFileProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.MemoryBackendFileProperties "QSD:qom.MemoryBackendFileProperties").
        - When `qom-type` is `memory-backend-memfd`: The members of [`MemoryBackendMemfdProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.MemoryBackendMemfdProperties "QSD:qom.MemoryBackendMemfdProperties").
        - When `qom-type` is `memory-backend-ram`: The members of [`MemoryBackendProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.MemoryBackendProperties "QSD:qom.MemoryBackendProperties").
        - When `qom-type` is `memory-backend-shm`: The members of [`MemoryBackendShmProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.MemoryBackendShmProperties "QSD:qom.MemoryBackendShmProperties").
        - When `qom-type` is `monitor-hmp`: The members of [`MonitorHMPProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.MonitorHMPProperties "QSD:qom.MonitorHMPProperties").
        - When `qom-type` is `monitor-qmp`: The members of [`MonitorQMPProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.MonitorQMPProperties "QSD:qom.MonitorQMPProperties").
        - When `qom-type` is `pr-manager-helper`: The members of [`PrManagerHelperProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.PrManagerHelperProperties "QSD:qom.PrManagerHelperProperties").
        - When `qom-type` is `qtest`: The members of [`QtestProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.QtestProperties "QSD:qom.QtestProperties").
        - When `qom-type` is `rng-builtin`: The members of [`RngProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.RngProperties "QSD:qom.RngProperties").
        - When `qom-type` is `rng-egd`: The members of [`RngEgdProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.RngEgdProperties "QSD:qom.RngEgdProperties").
        - When `qom-type` is `rng-random`: The members of [`RngRandomProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.RngRandomProperties "QSD:qom.RngRandomProperties").
        - When `qom-type` is `secret`: The members of [`SecretProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.SecretProperties "QSD:crypto.SecretProperties").
        - When `qom-type` is `secret_keyring`: The members of [`SecretKeyringProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.SecretKeyringProperties "QSD:crypto.SecretKeyringProperties").
        - When `qom-type` is `sev-guest`: The members of [`SevGuestProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.SevGuestProperties "QSD:qom.SevGuestProperties").
        - When `qom-type` is `sev-snp-guest`: The members of [`SevSnpGuestProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.SevSnpGuestProperties "QSD:qom.SevSnpGuestProperties").
        - When `qom-type` is `tdx-guest`: The members of [`TdxGuestProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.TdxGuestProperties "QSD:qom.TdxGuestProperties").
        - When `qom-type` is `thread-context`: The members of [`ThreadContextProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.ThreadContextProperties "QSD:qom.ThreadContextProperties").
        - When `qom-type` is `throttle-group`: The members of [`ThrottleGroupProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-block-core.ThrottleGroupProperties "QSD:block-core.ThrottleGroupProperties").
        - When `qom-type` is `tls-creds-anon`: The members of [`TlsCredsAnonProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.TlsCredsAnonProperties "QSD:crypto.TlsCredsAnonProperties").
        - When `qom-type` is `tls-creds-psk`: The members of [`TlsCredsPskProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.TlsCredsPskProperties "QSD:crypto.TlsCredsPskProperties").
        - When `qom-type` is `tls-creds-x509`: The members of [`TlsCredsX509Properties`](qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.TlsCredsX509Properties "QSD:crypto.TlsCredsX509Properties").
        - When `qom-type` is `tls-cipher-suites`: The members of [`TlsCredsProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-crypto.TlsCredsProperties "QSD:crypto.TlsCredsProperties").
        - When `qom-type` is `x-remote-object`: The members of [`RemoteObjectProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.RemoteObjectProperties "QSD:qom.RemoteObjectProperties").
        - When `qom-type` is `x-vfio-user-server`: The members of [`VfioUserServerProperties`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.VfioUserServerProperties "QSD:qom.VfioUserServerProperties").

*Command* object-add (Since: 2.0)
:   Create a QOM object.

    Arguments:
    :   - The members of [`ObjectOptions`](qemu-storage-daemon-qmp-ref.md#object-QSD-qom.ObjectOptions "QSD:qom.ObjectOptions").

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
