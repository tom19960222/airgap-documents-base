---
collection: qemu
version: "11.1.0"
title: "D-Bus display"
source_url: https://www.qemu.org/docs/master/interop/dbus-display.html
fetched_at: 2026-08-21T03:22:06+00:00
---
# D-Bus display

QEMU can export the VM display through D-Bus (when started with `-display
dbus`), to allow out-of-process UIs, remote protocol servers or other
interactive display usages.

Various specialized D-Bus interfaces are available on different object paths
under `/org/qemu/Display1/`, depending on the VM configuration.

QEMU also implements the standard interfaces, such as
[org.freedesktop.DBus.Introspectable](https://dbus.freedesktop.org/doc/dbus-specification.html#standard-interfaces).

## org.qemu.Display1.VM interface

*interface* org.qemu.Display1.VM
:   This interface is implemented on `/org/qemu/Display1/VM`.

    *property* Name:s
    :   Access:
        :   read-only

        Emits Changed:
        :   yes

        The name of the VM.

    *property* UUID:s
    :   Access:
        :   read-only

        Emits Changed:
        :   yes

        The UUID of the VM.

    *property* ConsoleIDs:au
    :   Access:
        :   read-only

        Emits Changed:
        :   yes

        The list of consoles available on `/org/qemu/Display1/Console_$id`.

    *property* Interfaces:as
    :   Access:
        :   read-only

        Emits Changed:
        :   yes

        This property lists extra interfaces provided by the
        /org/qemu/Display1/VM object, and can be used to detect
        the capabilities with which they are communicating.

        Unlike the standard D-Bus Introspectable interface, querying this
        property does not require parsing XML.

        (earlier version of the display interface do not provide this property)

## org.qemu.Display1.Console interface

*interface* org.qemu.Display1.Console
:   This interface is implemented on `/org/qemu/Display1/Console_$id`. You
    may discover available consoles through introspection or with the
    [`org.qemu.Display1.VM.ConsoleIDs`](dbus-display.md#org.qemu.Display1.VM.ConsoleIDs) property.

    A console is attached to a video device head. It may be “Graphic” or
    “Text” (see [`Type`](dbus-display.md#org.qemu.Display1.Console.Type) and other properties).

    Interactions with a console may be done with
    [`org.qemu.Display1.Keyboard`](dbus-display.md#org.qemu.Display1.Keyboard),
    [`org.qemu.Display1.Mouse`](dbus-display.md#org.qemu.Display1.Mouse) and
    [`org.qemu.Display1.MultiTouch`](dbus-display.md#org.qemu.Display1.MultiTouch) interfaces when available.

    *method* RegisterListener(*ay listener*, *h listener*) → ()
    :   Arguments:
        :   - **listener** (*h*) – a Unix socket FD, for peer-to-peer D-Bus communication.
            - **listener** – a Unix socket FD, for peer-to-peer D-Bus communication.

        Register a console listener, which will receive display updates, until
        it is disconnected.

        Multiple listeners may be registered simultaneously.

        The listener is expected to implement the
        [`org.qemu.Display1.Listener`](dbus-display.md#org.qemu.Display1.Listener) interface.

    *method* SetUIInfo(*q width_mm*, *q height_mm*, *i xoff*, *i yoff*, *u width*, *u height*) → ()
    :   Arguments:
        :   - **width_mm** (*q*) – the physical display width in millimeters.
            - **height_mm** (*q*) – the physical display height in millimeters.
            - **xoff** (*i*) – horizontal offset, in pixels.
            - **yoff** (*i*) – vertical offset, in pixels.
            - **width** (*u*) – console width, in pixels.
            - **height** (*u*) – console height, in pixels.

        Modify the dimensions and display settings.

    *property* Label:s
    :   Access:
        :   read-only

        Emits Changed:
        :   yes

        A user-friendly name for the console (for ex: “VGA”).

    *property* Head:u
    :   Access:
        :   read-only

        Emits Changed:
        :   yes

        Graphical device head number.

    *property* Type:s
    :   Access:
        :   read-only

        Emits Changed:
        :   yes

        Console type (“Graphic” or “Text”).

    *property* Width:u
    :   Access:
        :   read-only

        Emits Changed:
        :   yes

        Console width, in pixels.

    *property* Height:u
    :   Access:
        :   read-only

        Emits Changed:
        :   yes

        Console height, in pixels.

    *property* DeviceAddress:s
    :   Access:
        :   read-only

        Emits Changed:
        :   yes

        The device address (ex: “pci/0000/02.0”).

    *property* Interfaces:as
    :   Access:
        :   read-only

        Emits Changed:
        :   yes

        This property lists extra interfaces provided by the
        `/org/qemu/Display1/Console_$id` object, and can be used to detect the
        capabilities with which they are communicating.

        Unlike the standard D-Bus Introspectable interface, querying this
        property does not require parsing XML.

        (earlier version of the display interface do not provide this property)

## org.qemu.Display1.Keyboard interface

*interface* org.qemu.Display1.Keyboard
:   This interface is optionally implemented on
    `/org/qemu/Display1/Console_$id` (see
    [`Console`](dbus-display.md#org.qemu.Display1.Console)).

    *method* Press(*u keycode*) → ()
    :   Arguments:
        :   - **keycode** (*u*) – QEMU key number (xtkbd + special re-encoding of high bit)

        Send a key press event.

    *method* Release(*u keycode*) → ()
    :   Arguments:
        :   - **keycode** (*u*) – QEMU key number (xtkbd + special re-encoding of high bit)

        Send a key release event.

    *property* Modifiers:u
    :   Access:
        :   read-only

        Emits Changed:
        :   yes

        The active keyboard modifiers:

        ```
        Scroll = 1 << 0
        Num    = 1 << 1
        Caps   = 1 << 2
        ```

## org.qemu.Display1.Mouse interface

*interface* org.qemu.Display1.Mouse
:   This interface is optionally implemented on
    `/org/qemu/Display1/Console_$id` (see
    [`Console`](dbus-display.md#org.qemu.Display1.Console) documentation).

    **Button values**:

    ```
    Left       = 0
    Middle     = 1
    Right      = 2
    Wheel-up   = 3
    Wheel-down = 4
    Side       = 5
    Extra      = 6
    ```

    *method* Press(*u button*) → ()
    :   Arguments:
        :   - **button** (*u*) – [button value](dbus-display.md#dbus-button-values).

        Send a mouse button press event.

    *method* Release(*u button*) → ()
    :   Arguments:
        :   - **button** (*u*) – [button value](dbus-display.md#dbus-button-values).

        Send a mouse button release event.

    *method* SetAbsPosition(*u x*, *u y*) → ()
    :   Arguments:
        :   - **x** (*u*) – X position, in pixels.
            - **y** (*u*) – Y position, in pixels.

        Set the mouse pointer position.

        Returns an error if not [`IsAbsolute`](dbus-display.md#org.qemu.Display1.Mouse.IsAbsolute).

    *method* RelMotion(*i dx*, *i dy*) → ()
    :   Arguments:
        :   - **dx** (*i*) – X-delta, in pixels.
            - **dy** (*i*) – Y-delta, in pixels.

        Move the mouse pointer position, relative to the current position.

        Returns an error if [`IsAbsolute`](dbus-display.md#org.qemu.Display1.Mouse.IsAbsolute).

    *property* IsAbsolute:b
    :   Access:
        :   read-only

        Emits Changed:
        :   yes

        Whether the mouse is using absolute movements.

## org.qemu.Display1.MultiTouch interface

*interface* org.qemu.Display1.MultiTouch
:   This interface in implemented on `/org/qemu/Display1/Console_$id` (see
    [`Console`](dbus-display.md#org.qemu.Display1.Console) documentation).

    **Kind values**:

    ```
    Begin       = 0
    Update      = 1
    End         = 2
    Cancel      = 3
    ```

    *method* SendEvent(*u kind*, *t num_slot*, *d x*, *d y*) → ()
    :   Arguments:
        :   - **kind** (*u*) – The touch event kind
            - **num_slot** (*t*) – The slot number.
            - **x** (*d*) – The x coordinates.
            - **y** (*d*) – The y coordinates.

        Send a touch gesture event.

    *property* MaxSlots:i
    :   Access:
        :   read-only

        Emits Changed:
        :   yes

        The maximum number of slots.

## org.qemu.Display1.Listener interface

*interface* org.qemu.Display1.Listener
:   This client-side interface must be available on
    `/org/qemu/Display1/Listener` when registering the peer-to-peer
    connection with [`Register`](dbus-display.md#org.qemu.Display1.Chardev.Register).

    *method* Scanout(*u width*, *u height*, *u stride*, *u pixman_format*, *ay data*) → ()
    :   Arguments:
        :   - **width** (*u*) – display width, in pixels.
            - **height** (*u*) – display height, in pixels.
            - **stride** (*u*) – data stride, in bytes.
            - **pixman_format** (*u*) – image format (ex: `PIXMAN_X8R8G8B8`).
            - **data** (*ay*) – image data.

        Resize and update the display content.

        The data to transfer for the display update may be large. The preferred
        scanout method is [`ScanoutDMABUF`](dbus-display.md#org.qemu.Display1.Listener.ScanoutDMABUF), used whenever possible.

    *method* Update(*i x*, *i y*, *i width*, *i height*, *u stride*, *u pixman_format*, *ay data*) → ()
    :   Arguments:
        :   - **x** (*i*) – X update position, in pixels.
            - **y** (*i*) – Y update position, in pixels.
            - **width** (*i*) – update width, in pixels.
            - **height** (*i*) – update height, in pixels.
            - **stride** (*u*) – data stride, in bytes.
            - **pixman_format** (*u*) – image format (ex: `PIXMAN_X8R8G8B8`).
            - **data** (*ay*) – display image data.

        Update the display content.

        This method is only called after a [`Scanout`](dbus-display.md#org.qemu.Display1.Listener.Scanout) call.

    *method* ScanoutDMABUF(*h dmabuf*, *u width*, *u height*, *u stride*, *u fourcc*, *t modifier*, *b y0_top*) → ()
    :   Arguments:
        :   - **dmabuf** (*h*) – the DMABUF file descriptor.
            - **width** (*u*) – display width, in pixels.
            - **height** (*u*) – display height, in pixels.
            - **stride** (*u*) – stride, in bytes.
            - **fourcc** (*u*) – DMABUF fourcc.
            - **modifier** (*t*) – DMABUF modifier.
            - **y0_top** (*b*) – whether Y position 0 is the top or not.

        Resize and update the display content with a DMABUF.

    *method* UpdateDMABUF(*i x*, *i y*, *i width*, *i height*) → ()
    :   Arguments:
        :   - **x** (*i*) – the X update position, in pixels.
            - **y** (*i*) – the Y update position, in pixels.
            - **width** (*i*) – the update width, in pixels.
            - **height** (*i*) – the update height, in pixels.

        Update the display content with the current DMABUF and the given region.

    *method* Disable() → ()
    :   Disable the display (turn it off).

    *method* MouseSet(*i x*, *i y*, *i on*) → ()
    :   Arguments:
        :   - **x** (*i*) – X mouse position, in pixels.
            - **y** (*i*) – Y mouse position, in pixels.
            - **on** (*i*) – whether the mouse is visible or not.

        Set the mouse position and visibility.

    *method* CursorDefine(*i width*, *i height*, *i hot_x*, *i hot_y*, *ay data*) → ()
    :   Arguments:
        :   - **width** (*i*) – cursor width, in pixels.
            - **height** (*i*) – cursor height, in pixels.
            - **hot_x** (*i*) – hot-spot X position, in pixels.
            - **hot_y** (*i*) – hot-spot Y position, in pixels.
            - **data** (*ay*) – the cursor data.

        Set the mouse cursor shape and hot-spot. The “data” must be ARGB, 32-bit
        per pixel.

    *property* Interfaces:as
    :   Access:
        :   read-only

        Emits Changed:
        :   yes

        This property lists extra interfaces provided by the
        /org/qemu/Display1/Listener object, and can be used to detect
        the capabilities with which they are communicating.

        Unlike the standard D-Bus Introspectable interface, querying this
        property does not require parsing XML.

        (earlier version of the display interface do not provide this property)

## org.qemu.Display1.Listener.Unix.Map interface

*interface* org.qemu.Display1.Listener.Unix.Map
:   This optional client-side interface can complement
    org.qemu.Display1.Listener on `/org/qemu/Display1/Listener` for
    Unix-specific shared memory scanouts.

    *method* ScanoutMap(*h handle*, *u offset*, *u width*, *u height*, *u stride*, *u pixman_format*) → ()
    :   Arguments:
        :   - **handle** (*h*) – the shared map FD.
            - **offset** (*u*) – mapping offset, in bytes.
            - **width** (*u*) – display width, in pixels.
            - **height** (*u*) – display height, in pixels.
            - **stride** (*u*) – stride, in bytes.
            - **pixman_format** (*u*) – image format (ex: `PIXMAN_X8R8G8B8`).

        Resize and update the display content with a shared map.

    *method* UpdateMap(*i x*, *i y*, *i width*, *i height*) → ()
    :   Arguments:
        :   - **x** (*i*) – the X update position, in pixels.
            - **y** (*i*) – the Y update position, in pixels.
            - **width** (*i*) – the update width, in pixels.
            - **height** (*i*) – the update height, in pixels.

        Update the display content with the current shared map and the given region.

## org.qemu.Display1.Listener.Win32.Map interface

*interface* org.qemu.Display1.Listener.Win32.Map
:   This optional client-side interface can complement
    org.qemu.Display1.Listener on `/org/qemu/Display1/Listener` for Windows
    specific shared memory scanouts.

    *method* ScanoutMap(*t handle*, *u offset*, *u width*, *u height*, *u stride*, *u pixman_format*) → ()
    :   Arguments:
        :   - **handle** (*t*) – the shared file mapping handle value (not a file handle)
            - **offset** (*u*) – mapping offset.
            - **width** (*u*) – display width, in pixels.
            - **height** (*u*) – display height, in pixels.
            - **stride** (*u*) – stride, in bytes.
            - **pixman_format** (*u*) – image format (ex: `PIXMAN_X8R8G8B8`).

        Resize and update the display content with a shared file mapping object.

    *method* UpdateMap(*i x*, *i y*, *i width*, *i height*) → ()
    :   Arguments:
        :   - **x** (*i*) – the X update position, in pixels.
            - **y** (*i*) – the Y update position, in pixels.
            - **width** (*i*) – the update width, in pixels.
            - **height** (*i*) – the update height, in pixels.

        Update the display content with the current shared map and the given region.

## org.qemu.Display1.Listener.Win32.D3d11 interface

*interface* org.qemu.Display1.Listener.Win32.D3d11
:   This optional client-side interface can complement
    org.qemu.Display1.Listener on `/org/qemu/Display1/Listener` for Windows
    specific Direct3D texture sharing of the scanouts.

    *method* ScanoutTexture2d(*t handle*, *u texture_width*, *u texture_height*, *b y0_top*, *u x*, *u y*, *u width*, *u height*) → ()
    :   Arguments:
        :   - **handle** (*t*) – the NT handle for the shared texture (to be opened back with ID3D11Device1::OpenSharedResource1).
            - **texture_width** (*u*) – texture width, in pixels.
            - **texture_height** (*u*) – texture height, in pixels.
            - **y0_top** (*b*) – whether Y position 0 is the top or not.
            - **x** (*u*) – the X scanout position, in pixels.
            - **y** (*u*) – the Y scanout position, in pixels.
            - **width** (*u*) – the scanout width, in pixels.
            - **height** (*u*) – the scanout height, in pixels.

        Resize and update the display content with a Direct3D 11 2D texture.
        You must acquire and release the associated KeyedMutex 0 during rendering.

    *method* UpdateTexture2d(*i x*, *i y*, *i width*, *i height*) → ()
    :   Arguments:
        :   - **x** (*i*) – the X update position, in pixels.
            - **y** (*i*) – the Y update position, in pixels.
            - **width** (*i*) – the update width, in pixels.
            - **height** (*i*) – the update height, in pixels.

        Update the display content with the current Direct3D 2D texture and the given region.
        You must acquire and release the associated KeyedMutex 0 during rendering.

## org.qemu.Display1.Listener.Unix.ScanoutDMABUF2 interface

*interface* org.qemu.Display1.Listener.Unix.ScanoutDMABUF2
:   This optional client-side interface can complement
    org.qemu.Display1.Listener on `/org/qemu/Display1/Listener` for
    Unix-specific DMABUF scanout setup which support multi plane.

    *method* ScanoutDMABUF2(*ah dmabuf*, *u x*, *u y*, *u width*, *u height*, *au offset*, *au stride*, *u num_planes*, *u fourcc*, *u backing_width*, *u backing_height*, *t modifier*, *b y0_top*) → ()
    :   Arguments:
        :   - **dmabuf** (*ah*) – DMABUF file descriptor of each plane.
            - **x** (*u*) – display x offset, in pixels
            - **y** (*u*) – display y offset, in pixels
            - **width** (*u*) – display width, in pixels.
            - **height** (*u*) – display height, in pixels.
            - **offset** (*au*) – offset of each plane, in bytes.
            - **stride** (*au*) – stride of each plane, in bytes.
            - **num_planes** (*u*) – plane number.
            - **fourcc** (*u*) – DMABUF fourcc.
            - **backing_width** (*u*) – backing framebuffer width, in pixels
            - **backing_height** (*u*) – backing framebuffer height, in pixels
            - **modifier** (*t*) – DMABUF modifier.
            - **y0_top** (*b*) – whether Y position 0 is the top or not.

        Resize and update the display content with DMABUF.

## org.qemu.Display1.Clipboard interface

*interface* org.qemu.Display1.Clipboard
:   This interface must be implemented by both the client and the server on
    `/org/qemu/Display1/Clipboard` to support clipboard sharing between
    the client and the guest.

    Once [`Register`](dbus-display.md#org.qemu.Display1.Chardev.Register)’ed, method calls may be sent and received in both
    directions. Unregistered callers will get error replies.

    **Selection values**:

    ```
    Clipboard   = 0
    Primary     = 1
    Secondary   = 2
    ```

    **Serial counter**

    To solve potential clipboard races, clipboard grabs have an associated
    serial counter. It is set to 0 on registration, and incremented by 1 for
    each grab. The peer with the highest serial is the clipboard grab owner.

    When a grab with a lower serial is received, it should be discarded.

    When a grab is attempted with the same serial number as the current grab,
    the one coming from the client should have higher priority, and the client
    should gain clipboard grab ownership.

    *method* Register() → ()
    :   Register a clipboard session and reinitialize the serial counter.

        The client must register itself, and is granted an exclusive
        access for handling the clipboard.

        The server can reinitialize the session as well (to reset the counter).

    *method* Unregister() → ()
    :   Unregister the clipboard session.

    *method* Grab(*u selection*, *u serial*, *as mimes*) → ()
    :   Arguments:
        :   - **selection** (*u*) – a [selection value](dbus-display.md#dbus-clipboard-selection).
            - **serial** (*u*) – the current grab [serial](dbus-display.md#dbus-clipboard-serial).
            - **mimes** (*as*) – the list of available content MIME types.

        Grab the clipboard, claiming current clipboard content.

    *method* Release(*u selection*) → ()
    :   Arguments:
        :   - **selection** (*u*) – a [selection value](dbus-display.md#dbus-clipboard-selection).

        Release the clipboard (does nothing if not the current owner).

    *method* Request(*u selection*, *as mimes*) → (*s reply_mime*, *ay data*)
    :   Arguments:
        :   - **selection** (*u*) – a [selection value](dbus-display.md#dbus-clipboard-selection)
            - **mimes** (*as*) – requested MIME types (by order of preference).

        Returns:
        :   - **reply_mime** (*s*) – the returned data MIME type.
            - **data** (*ay*) – the clipboard data.

        Request the clipboard content.

        Return an error if the clipboard is empty, or the requested MIME types
        are unavailable.

    *property* Interfaces:as
    :   Access:
        :   read-only

        Emits Changed:
        :   yes

        This property lists extra interfaces provided by the
        /org/qemu/Display1/Clipboard object, and can be used to detect
        the capabilities with which they are communicating.

        Unlike the standard D-Bus Introspectable interface, querying this
        property does not require parsing XML.

        (earlier version of the display interface do not provide this property)

## org.qemu.Display1.Audio interface

*interface* org.qemu.Display1.Audio
:   Audio backend may be available on `/org/qemu/Display1/Audio`.

    *method* RegisterOutListener(*ay listener*, *h listener*) → ()
    :   Arguments:
        :   - **listener** (*h*) – a Unix socket FD, for peer-to-peer D-Bus communication.
            - **listener** – a Unix socket FD, for peer-to-peer D-Bus communication.

        Register an audio backend playback handler.

        Multiple listeners may be registered simultaneously.

        The listener is expected to implement the
        [`org.qemu.Display1.AudioOutListener`](dbus-display.md#org.qemu.Display1.AudioOutListener) interface.

    *method* RegisterInListener(*ay listener*, *h listener*) → ()
    :   Arguments:
        :   - **listener** (*h*) – a Unix socket FD, for peer-to-peer D-Bus communication.
            - **listener** – a Unix socket FD, for peer-to-peer D-Bus communication.

        Register an audio backend record handler.

        Multiple listeners may be registered simultaneously.

        The listener is expected to implement the
        [`org.qemu.Display1.AudioInListener`](dbus-display.md#org.qemu.Display1.AudioInListener) interface.

    *property* NSamples:u
    :   Access:
        :   read-only

        Emits Changed:
        :   yes

        The number of samples per read/write frames. (for example the default is
        480, or 10ms at 48kHz)

        (earlier version of the display interface do not provide this property)

    *property* Interfaces:as
    :   Access:
        :   read-only

        Emits Changed:
        :   yes

        This property lists extra interfaces provided by the
        /org/qemu/Display1/Audio object, and can be used to detect
        the capabilities with which they are communicating.

        Unlike the standard D-Bus Introspectable interface, querying this
        property does not require parsing XML.

        (earlier version of the display interface do not provide this property)

## org.qemu.Display1.AudioOutListener interface

*interface* org.qemu.Display1.AudioOutListener
:   This client-side interface must be available on
    `/org/qemu/Display1/AudioOutListener` when registering the peer-to-peer
    connection with [`RegisterOutListener`](dbus-display.md#org.qemu.Display1.Audio.RegisterOutListener).

    *method* Init(*t id*, *y bits*, *b is_signed*, *b is_float*, *u freq*, *y nchannels*, *u bytes_per_frame*, *u bytes_per_second*, *b be*) → ()
    :   Arguments:
        :   - **id** (*t*) – the stream ID.
            - **bits** (*y*) – PCM bits per sample.
            - **is_signed** (*b*) – whether the PCM data is signed.
            - **is_float** (*b*) – PCM floating point format.
            - **freq** (*u*) – the PCM frequency in Hz.
            - **nchannels** (*y*) – the number of channels.
            - **bytes_per_frame** (*u*) – the bytes per frame.
            - **bytes_per_second** (*u*) – the bytes per second.
            - **be** (*b*) – whether using big-endian format.

        Initializes a PCM playback stream.

    *method* Fini(*t id*) → ()
    :   Arguments:
        :   - **id** (*t*) – the stream ID.

        Finish & close a playback stream.

    *method* SetEnabled(*t id*, *b enabled*) → ()
    :   Arguments:
        :   - **id** (*t*) – the stream ID.
            - **enabled** (*b*)

        Resume or suspend the playback stream.

    *method* SetVolume(*t id*, *b mute*, *ay volume*) → ()
    :   Arguments:
        :   - **id** (*t*) – the stream ID.
            - **mute** (*b*) – whether the stream is muted.
            - **volume** (*ay*) – the volume per-channel.

        Set the stream volume and mute state (volume without unit, 0-255).

    *method* Write(*t id*, *ay data*) → ()
    :   Arguments:
        :   - **id** (*t*) – the stream ID.
            - **data** (*ay*) – the PCM data.

        PCM stream to play.

    *property* Interfaces:as
    :   Access:
        :   read-only

        Emits Changed:
        :   yes

        This property lists extra interfaces provided by the
        /org/qemu/Display1/AudioOutListener object, and can be used to detect
        the capabilities with which they are communicating.

        Unlike the standard D-Bus Introspectable interface, querying this
        property does not require parsing XML.

        (earlier version of the display interface do not provide this property)

## org.qemu.Display1.AudioInListener interface

*interface* org.qemu.Display1.AudioInListener
:   This client-side interface must be available on
    `/org/qemu/Display1/AudioInListener` when registering the peer-to-peer
    connection with [`RegisterInListener`](dbus-display.md#org.qemu.Display1.Audio.RegisterInListener).

    *method* Init(*t id*, *y bits*, *b is_signed*, *b is_float*, *u freq*, *y nchannels*, *u bytes_per_frame*, *u bytes_per_second*, *b be*) → ()
    :   Arguments:
        :   - **id** (*t*) – the stream ID.
            - **bits** (*y*) – PCM bits per sample.
            - **is_signed** (*b*) – whether the PCM data is signed.
            - **is_float** (*b*) – PCM floating point format.
            - **freq** (*u*) – the PCM frequency in Hz.
            - **nchannels** (*y*) – the number of channels.
            - **bytes_per_frame** (*u*) – the bytes per frame.
            - **bytes_per_second** (*u*) – the bytes per second.
            - **be** (*b*) – whether using big-endian format.

        Initializes a PCM record stream.

    *method* Fini(*t id*) → ()
    :   Arguments:
        :   - **id** (*t*) – the stream ID.

        Finish & close a record stream.

    *method* SetEnabled(*t id*, *b enabled*) → ()
    :   Arguments:
        :   - **id** (*t*) – the stream ID.
            - **enabled** (*b*)

        Resume or suspend the record stream.

    *method* SetVolume(*t id*, *b mute*, *ay volume*) → ()
    :   Arguments:
        :   - **id** (*t*) – the stream ID.
            - **mute** (*b*) – whether the stream is muted.
            - **volume** (*ay*) – the volume per-channel.

        Set the stream volume and mute state (volume without unit, 0-255).

    *method* Read(*t id*, *t size*) → (*ay data*)
    :   Arguments:
        :   - **id** (*t*) – the stream ID.
            - **size** (*t*) – the amount to read, in bytes.

        Returns:
        :   - **data** (*ay*) – the recorded data (which may be less than requested).

        Read “size” bytes from the record stream.

    *property* Interfaces:as
    :   Access:
        :   read-only

        Emits Changed:
        :   yes

        This property lists extra interfaces provided by the
        /org/qemu/Display1/AudioInListener object, and can be used to detect
        the capabilities with which they are communicating.

        Unlike the standard D-Bus Introspectable interface, querying this
        property does not require parsing XML.

        (earlier version of the display interface do not provide this property)

## org.qemu.Display1.Chardev interface

*interface* org.qemu.Display1.Chardev
:   Character devices may be available on `/org/qemu/Display1/Chardev_$id`.

    They may be used for different kind of streams, which are identified via
    their FQDN [`Name`](dbus-vnc.md#org.qemu.Vnc1.Server.Name).

    Here are some known reserved kind names (the `org.qemu` prefix is
    reserved by QEMU):

    org.qemu.console.serial.0
    :   A serial console stream.

    org.qemu.monitor.hmp.0
    :   A QEMU HMP human monitor.

    org.qemu.monitor.qmp.0
    :   A QEMU QMP monitor.

    org.qemu.usbredir
    :   A usbredir stream.

    *method* Register(*ay listener*, *h stream*) → ()
    :   Arguments:
        :   - **listener** (*ay*)
            - **stream** (*h*) – a Unix FD to redirect the stream to.

        Register a file-descriptor for the stream handling.

        The current handler, if any, will be replaced.

    *method* SendBreak() → ()
    :   Send a break event to the character device.

    *property* Name:s
    :   Access:
        :   read-only

        Emits Changed:
        :   yes

        The FQDN name to identify the kind of stream. See [reserved
        names](dbus-display.md#dbus-chardev-fqdn).

    *property* FEOpened:b
    :   Access:
        :   read-only

        Emits Changed:
        :   yes

        Whether the front-end side is opened.

    *property* Echo:b
    :   Access:
        :   read-only

        Emits Changed:
        :   yes

        Whether the input should be echo’ed (for serial streams).

    *property* Owner:s
    :   Access:
        :   read-only

        Emits Changed:
        :   yes

        The D-Bus unique name of the registered handler.

    *property* Interfaces:as
    :   Access:
        :   read-only

        Emits Changed:
        :   yes

        This property lists extra interfaces provided by the
        `/org/qemu/Display1/Chardev_$i` object, and can be used to detect
        the capabilities with which they are communicating.

        Unlike the standard D-Bus Introspectable interface, querying this
        property does not require parsing XML.

        (earlier version of the display interface do not provide this property)

## org.qemu.Display1.Chardev.VCEncoding interface

*interface* org.qemu.Display1.Chardev.VCEncoding
:   Provides encoding information for virtual console chardevs.

    This interface is present on chardev objects that are virtual
    consoles, and exposes the character encoding used by the guest.

    *property* Encoding:s
    :   Access:
        :   read-only

        Emits Changed:
        :   yes

        The character encoding used by the virtual console
        (matching `ChardevVCEncoding`): `cp437` or `utf8`.
