---
collection: qemu
version: "11.1.0"
title: "QEMU UI subsystem"
source_url: https://www.qemu.org/docs/master/devel/ui.html
fetched_at: 2026-08-21T03:25:59+00:00
---
# QEMU UI subsystem

## QEMU Clipboard

**Introduction**

The header `ui/clipboard.h` declares the qemu clipboard interface.

All qemu elements which want use the clipboard can register as
clipboard peer. Subsequently they can set the clipboard content
and get notifications for clipboard updates.

Typical users are user interfaces (gtk), remote access protocols
(vnc) and devices talking to the guest (vdagent).

Even though the design allows different data types only plain text
is supported for now.

enum QemuClipboardType

**Constants**

`QEMU_CLIPBOARD_TYPE_TEXT`
:   text/plain; charset=utf-8

`QEMU_CLIPBOARD_TYPE__COUNT`
:   type count.

enum QemuClipboardSelection

**Constants**

`QEMU_CLIPBOARD_SELECTION_CLIPBOARD`
:   clipboard (explitcit cut+paste).

`QEMU_CLIPBOARD_SELECTION_PRIMARY`
:   primary selection (select + middle mouse button).

`QEMU_CLIPBOARD_SELECTION_SECONDARY`
:   secondary selection (dunno).

`QEMU_CLIPBOARD_SELECTION__COUNT`
:   selection count.

struct QemuClipboardPeer

**Definition**:

```
struct QemuClipboardPeer {
    const char *name;
    Notifier notifier;
    void (*request)(QemuClipboardInfo *info, QemuClipboardType type);
};
```

**Members**

`name`
:   peer name.

`notifier`
:   notifier for clipboard updates.

`request`
:   callback for clipboard data requests.

**Description**

Clipboard peer description.

enum QemuClipboardNotifyType

**Constants**

`QEMU_CLIPBOARD_UPDATE_INFO`
:   clipboard info update

`QEMU_CLIPBOARD_RESET_SERIAL`
:   reset clipboard serial

**Description**

Clipboard notify type.

struct QemuClipboardNotify

**Definition**:

```
struct QemuClipboardNotify {
    QemuClipboardNotifyType type;
    union {
        QemuClipboardInfo *info;
    };
};
```

**Members**

`type`
:   the type of event.

`{unnamed_union}`
:   anonymous

`info`
:   a QemuClipboardInfo event.

**Description**

Clipboard notify data.

struct QemuClipboardContent

**Definition**:

```
struct QemuClipboardContent {
    bool available;
    bool requested;
    uint32_t size;
    void *data;
};
```

**Members**

`available`
:   whether the data is available

`requested`
:   whether the data was requested

`size`
:   the size of the **data**

`data`
:   the clipboard data

**Description**

Clipboard content.

struct QemuClipboardInfo

**Definition**:

```
struct QemuClipboardInfo {
    uint32_t refcount;
    QemuClipboardPeer *owner;
    int selection;
    bool has_serial;
    uint32_t serial;
    QemuClipboardContent types[QEMU_CLIPBOARD_TYPE__COUNT];
};
```

**Members**

`refcount`
:   reference counter.

`owner`
:   clipboard owner.

`selection`
:   clipboard selection.

`has_serial`
:   whether **serial** is available.

`serial`
:   the grab serial counter.

`types`
:   clipboard data array (one entry per type).

**Description**

Clipboard content data and metadata.

void qemu_clipboard_peer_register([QemuClipboardPeer](ui.md#c.QemuClipboardPeer "QemuClipboardPeer") \*peer)

**Parameters**

`QemuClipboardPeer *peer`
:   peer information.

**Description**

Register clipboard peer. Registering is needed for both active
(set+grab clipboard) and passive (watch clipboard for updates)
interaction with the qemu clipboard.

void qemu_clipboard_peer_unregister([QemuClipboardPeer](ui.md#c.QemuClipboardPeer "QemuClipboardPeer") \*peer)

**Parameters**

`QemuClipboardPeer *peer`
:   peer information.

**Description**

Unregister clipboard peer.

bool qemu_clipboard_peer_owns([QemuClipboardPeer](ui.md#c.QemuClipboardPeer "QemuClipboardPeer") \*peer, [QemuClipboardSelection](ui.md#c.QemuClipboardSelection "QemuClipboardSelection") selection)

**Parameters**

`QemuClipboardPeer *peer`
:   peer information.

`QemuClipboardSelection selection`
:   clipboard selection.

**Description**

Return TRUE if the peer owns the clipboard.

void qemu_clipboard_peer_release([QemuClipboardPeer](ui.md#c.QemuClipboardPeer "QemuClipboardPeer") \*peer, [QemuClipboardSelection](ui.md#c.QemuClipboardSelection "QemuClipboardSelection") selection)

**Parameters**

`QemuClipboardPeer *peer`
:   peer information.

`QemuClipboardSelection selection`
:   clipboard selection.

**Description**

If the peer owns the clipboard, release it.

[QemuClipboardInfo](ui.md#c.QemuClipboardInfo "QemuClipboardInfo") \*qemu_clipboard_info([QemuClipboardSelection](ui.md#c.QemuClipboardSelection "QemuClipboardSelection") selection)

**Parameters**

`QemuClipboardSelection selection`
:   clipboard selection.

**Description**

Return the current clipboard data & owner information.

bool qemu_clipboard_check_serial([QemuClipboardInfo](ui.md#c.QemuClipboardInfo "QemuClipboardInfo") \*info, bool client)

**Parameters**

`QemuClipboardInfo *info`
:   clipboard info.

`bool client`
:   whether to check from the client context and priority.

**Description**

Return TRUE if the **info** has a higher serial than the current clipboard.

[QemuClipboardInfo](ui.md#c.QemuClipboardInfo "QemuClipboardInfo") \*qemu_clipboard_info_new([QemuClipboardPeer](ui.md#c.QemuClipboardPeer "QemuClipboardPeer") \*owner, [QemuClipboardSelection](ui.md#c.QemuClipboardSelection "QemuClipboardSelection") selection)

**Parameters**

`QemuClipboardPeer *owner`
:   clipboard owner.

`QemuClipboardSelection selection`
:   clipboard selection.

**Description**

Allocate a new QemuClipboardInfo and initialize it with the given
**owner** and **selection**.

QemuClipboardInfo is a reference-counted struct. The new struct is
returned with a reference already taken (i.e. reference count is
one).

[QemuClipboardInfo](ui.md#c.QemuClipboardInfo "QemuClipboardInfo") \*qemu_clipboard_info_ref([QemuClipboardInfo](ui.md#c.QemuClipboardInfo "QemuClipboardInfo") \*info)

**Parameters**

`QemuClipboardInfo *info`
:   clipboard info.

**Description**

Increase **info** reference count.

void qemu_clipboard_info_unref([QemuClipboardInfo](ui.md#c.QemuClipboardInfo "QemuClipboardInfo") \*info)

**Parameters**

`QemuClipboardInfo *info`
:   clipboard info.

**Description**

Decrease **info** reference count. When the count goes down to zero
free the **info** struct itself and all clipboard data.

void qemu_clipboard_update([QemuClipboardInfo](ui.md#c.QemuClipboardInfo "QemuClipboardInfo") \*info)

**Parameters**

`QemuClipboardInfo *info`
:   clipboard info.

**Description**

Update the qemu clipboard. Notify all registered peers (including
the clipboard owner) that the qemu clipboard has been updated.

This is used for both new completely clipboard content and for
clipboard data updates in response to qemu_clipboard_request()
calls.

void qemu_clipboard_reset_serial(void)

**Parameters**

`void`
:   no arguments

**Description**

Reset the clipboard serial.

void qemu_clipboard_request([QemuClipboardInfo](ui.md#c.QemuClipboardInfo "QemuClipboardInfo") \*info, [QemuClipboardType](ui.md#c.QemuClipboardType "QemuClipboardType") type)

**Parameters**

`QemuClipboardInfo *info`
:   clipboard info.

`QemuClipboardType type`
:   clipboard data type.

**Description**

Request clipboard content. Typically the clipboard owner only
advertises the available data types and provides the actual data
only on request.

void qemu_clipboard_set_data([QemuClipboardPeer](ui.md#c.QemuClipboardPeer "QemuClipboardPeer") \*peer, [QemuClipboardInfo](ui.md#c.QemuClipboardInfo "QemuClipboardInfo") \*info, [QemuClipboardType](ui.md#c.QemuClipboardType "QemuClipboardType") type, uint32_t size, const void \*data, bool update)

**Parameters**

`QemuClipboardPeer *peer`
:   clipboard peer.

`QemuClipboardInfo *info`
:   clipboard info.

`QemuClipboardType type`
:   clipboard data type.

`uint32_t size`
:   data size.

`const void *data`
:   data blob.

`bool update`
:   notify peers about the update.

**Description**

Set clipboard content for the given **type**. This function will make
a copy of the content data and store that.
