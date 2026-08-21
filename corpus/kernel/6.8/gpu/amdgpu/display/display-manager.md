---
collection: kernel
version: "6.8"
title: "AMDgpu Display Manager"
source_url: https://www.kernel.org/doc/html/v6.8/gpu/amdgpu/display/display-manager.html
fetched_at: 2026-08-21T03:38:19+00:00
---
# [AMDgpu Display Manager](display-manager.md#id1)

Table of Contents

- [AMDgpu Display Manager](display-manager.md#amdgpu-display-manager)

  - [Lifecycle](display-manager.md#lifecycle)
  - [Interrupts](display-manager.md#interrupts)
  - [Atomic Implementation](display-manager.md#atomic-implementation)
  - [Color Management Properties](display-manager.md#color-management-properties)

    - [DC Color Capabilities between DCN generations](display-manager.md#dc-color-capabilities-between-dcn-generations)
  - [Blend Mode Properties](display-manager.md#blend-mode-properties)

    - [Blend configuration flow](display-manager.md#blend-configuration-flow)

The AMDgpu display manager, **amdgpu_dm** (or even simpler,
**dm**) sits between DRM and DC. It acts as a liaison, converting DRM
requests into DC requests, and DC responses into DRM responses.

The root control structure is [`struct amdgpu_display_manager`](display-manager.md#c.amdgpu_display_manager "amdgpu_display_manager").

struct dm_compressor_info
:   Buffer info used by frame buffer compression

**Definition**:

```
struct dm_compressor_info {
    void *cpu_addr;
    struct amdgpu_bo *bo_ptr;
    uint64_t gpu_addr;
};
```

**Members**

`cpu_addr`
:   MMIO cpu addr

`bo_ptr`
:   Pointer to the buffer object

`gpu_addr`
:   MMIO gpu addr

struct dmub_hpd_work
:   Handle time consuming work in low priority outbox IRQ

**Definition**:

```
struct dmub_hpd_work {
    struct work_struct handle_hpd_work;
    struct dmub_notification *dmub_notify;
    struct amdgpu_device *adev;
};
```

**Members**

`handle_hpd_work`
:   Work to be executed in a separate thread to handle hpd_low_irq

`dmub_notify`
:   notification for callback function

`adev`
:   amdgpu_device pointer

struct vblank_control_work
:   Work data for vblank control

**Definition**:

```
struct vblank_control_work {
    struct work_struct work;
    struct amdgpu_display_manager *dm;
    struct amdgpu_crtc *acrtc;
    struct dc_stream_state *stream;
    bool enable;
};
```

**Members**

`work`
:   Kernel work data for the work event

`dm`
:   amdgpu display manager device

`acrtc`
:   amdgpu CRTC instance for which the event has occurred

`stream`
:   DC stream for which the event has occurred

`enable`
:   true if enabling vblank

struct amdgpu_dm_backlight_caps
:   Information about backlight

**Definition**:

```
struct amdgpu_dm_backlight_caps {
    union dpcd_sink_ext_caps *ext_caps;
    u32 aux_min_input_signal;
    u32 aux_max_input_signal;
    int min_input_signal;
    int max_input_signal;
    bool caps_valid;
    bool aux_support;
};
```

**Members**

`ext_caps`
:   Keep the data struct with all the information about the
    display support for HDR.

`aux_min_input_signal`
:   Min brightness value supported by the display

`aux_max_input_signal`
:   Max brightness value supported by the display
    in nits.

`min_input_signal`
:   minimum possible input in range 0-255.

`max_input_signal`
:   maximum possible input in range 0-255.

`caps_valid`
:   true if these values are from the ACPI interface.

`aux_support`
:   Describes if the display supports AUX backlight.

**Description**

Describe the backlight support for ACPI or eDP AUX.

struct dal_allocation
:   Tracks mapped FB memory for SMU communication

**Definition**:

```
struct dal_allocation {
    struct list_head list;
    struct amdgpu_bo *bo;
    void *cpu_ptr;
    u64 gpu_addr;
};
```

**Members**

`list`
:   list of dal allocations

`bo`
:   GPU buffer object

`cpu_ptr`
:   CPU virtual address of the GPU buffer object

`gpu_addr`
:   GPU virtual address of the GPU buffer object

struct hpd_rx_irq_offload_work_queue
:   Work queue to handle hpd_rx_irq offload work

**Definition**:

```
struct hpd_rx_irq_offload_work_queue {
    struct workqueue_struct *wq;
    spinlock_t offload_lock;
    bool is_handling_link_loss;
    bool is_handling_mst_msg_rdy_event;
    struct amdgpu_dm_connector *aconnector;
};
```

**Members**

`wq`
:   workqueue structure to queue offload work.

`offload_lock`
:   To protect fields of offload work queue.

`is_handling_link_loss`
:   Used to prevent inserting link loss event when
    we're handling link loss

`is_handling_mst_msg_rdy_event`
:   Used to prevent inserting mst message
    ready event when we're already handling mst message ready event

`aconnector`
:   The aconnector that this work queue is attached to

struct hpd_rx_irq_offload_work
:   hpd_rx_irq offload work structure

**Definition**:

```
struct hpd_rx_irq_offload_work {
    struct work_struct work;
    union hpd_irq_data data;
    struct hpd_rx_irq_offload_work_queue *offload_wq;
};
```

**Members**

`work`
:   offload work

`data`
:   reference irq data which is used while handling offload work

`offload_wq`
:   offload work queue that this work is queued to

struct amdgpu_display_manager
:   Central amdgpu display manager device

**Definition**:

```
struct amdgpu_display_manager {
    struct dc *dc;
    struct dmub_srv *dmub_srv;
    struct dmub_notification *dmub_notify;
    dmub_notify_interrupt_callback_t dmub_callback[AMDGPU_DMUB_NOTIFICATION_MAX];
    bool dmub_thread_offload[AMDGPU_DMUB_NOTIFICATION_MAX];
    struct dmub_srv_fb_info *dmub_fb_info;
    const struct firmware *dmub_fw;
    struct amdgpu_bo *dmub_bo;
    u64 dmub_bo_gpu_addr;
    void *dmub_bo_cpu_addr;
    uint32_t dmcub_fw_version;
    struct cgs_device *cgs_device;
    struct amdgpu_device *adev;
    struct drm_device *ddev;
    u16 display_indexes_num;
    struct drm_private_obj atomic_obj;
    struct mutex dc_lock;
    struct mutex audio_lock;
    struct drm_audio_component *audio_component;
    bool audio_registered;
    struct list_head irq_handler_list_low_tab[DAL_IRQ_SOURCES_NUMBER];
    struct list_head irq_handler_list_high_tab[DAL_IRQ_SOURCES_NUMBER];
    struct common_irq_params pflip_params[DC_IRQ_SOURCE_PFLIP_LAST - DC_IRQ_SOURCE_PFLIP_FIRST + 1];
    struct common_irq_params vblank_params[DC_IRQ_SOURCE_VBLANK6 - DC_IRQ_SOURCE_VBLANK1 + 1];
    struct common_irq_params vline0_params[DC_IRQ_SOURCE_DC6_VLINE0 - DC_IRQ_SOURCE_DC1_VLINE0 + 1];
    struct common_irq_params vupdate_params[DC_IRQ_SOURCE_VUPDATE6 - DC_IRQ_SOURCE_VUPDATE1 + 1];
    struct common_irq_params dmub_trace_params[1];
    struct common_irq_params dmub_outbox_params[1];
    spinlock_t irq_handler_list_table_lock;
    struct backlight_device *backlight_dev[AMDGPU_DM_MAX_NUM_EDP];
    const struct dc_link *backlight_link[AMDGPU_DM_MAX_NUM_EDP];
    uint8_t num_of_edps;
    struct amdgpu_dm_backlight_caps backlight_caps[AMDGPU_DM_MAX_NUM_EDP];
    struct mod_freesync *freesync_module;
    struct hdcp_workqueue *hdcp_workqueue;
    struct workqueue_struct *vblank_control_workqueue;
    struct drm_atomic_state *cached_state;
    struct dc_state *cached_dc_state;
    struct dm_compressor_info compressor;
    const struct firmware *fw_dmcu;
    uint32_t dmcu_fw_version;
    const struct gpu_info_soc_bounding_box_v1_0 *soc_bounding_box;
    uint32_t active_vblank_irq_count;
#if defined(CONFIG_DRM_AMD_SECURE_DISPLAY);
    struct secure_display_context *secure_display_ctxs;
#endif;
    struct hpd_rx_irq_offload_work_queue *hpd_rx_offload_wq;
    struct amdgpu_encoder mst_encoders[AMDGPU_DM_MAX_CRTC];
    bool force_timing_sync;
    bool disable_hpd_irq;
    bool dmcub_trace_event_en;
    struct list_head da_list;
    struct completion dmub_aux_transfer_done;
    struct workqueue_struct *delayed_hpd_wq;
    u32 brightness[AMDGPU_DM_MAX_NUM_EDP];
    u32 actual_brightness[AMDGPU_DM_MAX_NUM_EDP];
    bool aux_hpd_discon_quirk;
    struct mutex dpia_aux_lock;
};
```

**Members**

`dc`
:   Display Core control structure

`dmub_srv`
:   DMUB service, used for controlling the DMUB on hardware
    that supports it. The pointer to the dmub_srv will be
    NULL on hardware that does not support it.

`dmub_notify`
:   Notification from DMUB.

`dmub_callback`
:   Callback functions to handle notification from DMUB.

`dmub_thread_offload`
:   Flag to indicate if callback is offload.

`dmub_fb_info`
:   Framebuffer regions for the DMUB.

`dmub_fw`
:   DMUB firmware, required on hardware that has DMUB support.

`dmub_bo`
:   Buffer object for the DMUB.

`dmub_bo_gpu_addr`
:   GPU virtual address for the DMUB buffer object.

`dmub_bo_cpu_addr`
:   CPU address for the DMUB buffer object.

`dmcub_fw_version`
:   DMCUB firmware version.

`cgs_device`
:   The Common Graphics Services device. It provides an interface for
    accessing registers.

`adev`
:   AMDGPU base driver structure

`ddev`
:   DRM base driver structure

`display_indexes_num`
:   Max number of display streams supported

`atomic_obj`
:   In combination with `dm_atomic_state` it helps manage
    global atomic state that doesn't map cleanly into existing
    drm resources, like `dc_context`.

`dc_lock`
:   Guards access to DC functions that can issue register write
    sequences.

`audio_lock`
:   Guards access to audio instance changes.

`audio_component`
:   Used to notify ELD changes to sound driver.

`audio_registered`
:   True if the audio component has been registered
    successfully, false otherwise.

`irq_handler_list_low_tab`
:   Low priority IRQ handler table.

    It is a n\*m table consisting of n IRQ sources, and m handlers per IRQ
    source. Low priority IRQ handlers are deferred to a workqueue to be
    processed. Hence, they can sleep.

    Note that handlers are called in the same order as they were
    registered (FIFO).

`irq_handler_list_high_tab`
:   High priority IRQ handler table.

    It is a n\*m table, same as `irq_handler_list_low_tab`. However,
    handlers in this table are not deferred and are called immediately.

`pflip_params`
:   Page flip IRQ parameters, passed to registered handlers when
    triggered.

`vblank_params`
:   Vertical blanking IRQ parameters, passed to registered handlers when
    triggered.

`vline0_params`
:   OTG vertical interrupt0 IRQ parameters, passed to registered
    handlers when triggered.

`vupdate_params`
:   Vertical update IRQ parameters, passed to registered handlers when
    triggered.

`dmub_trace_params`
:   DMUB trace event IRQ parameters, passed to registered handlers when
    triggered.

`dmub_outbox_params`
:   DMUB Outbox parameters

`irq_handler_list_table_lock`
:   Synchronizes access to IRQ tables

`backlight_dev`
:   Backlight control device

`backlight_link`
:   Link on which to control backlight

`num_of_edps`
:   number of backlight eDPs

`backlight_caps`
:   Capabilities of the backlight device

`freesync_module`
:   Module handling freesync calculations

`hdcp_workqueue`
:   AMDGPU content protection queue

`vblank_control_workqueue`
:   Deferred work for vblank control events.

`cached_state`
:   Caches device atomic state for suspend/resume

`cached_dc_state`
:   Cached state of content streams

`compressor`
:   Frame buffer compression buffer. See [`struct dm_compressor_info`](display-manager.md#c.dm_compressor_info "dm_compressor_info")

`fw_dmcu`
:   Reference to DMCU firmware

`dmcu_fw_version`
:   Version of the DMCU firmware

`soc_bounding_box`
:   gpu_info FW provided soc bounding box struct or 0 if not
    available in FW

`active_vblank_irq_count`
:   number of currently active vblank irqs

`secure_display_ctxs`
:   Store the ROI information and the work_struct to command dmub and psp for
    all crtcs.

`hpd_rx_offload_wq`
:   Work queue to offload works of hpd_rx_irq

`mst_encoders`
:   fake encoders used for DP MST.

`force_timing_sync`
:   set via debugfs. When set, indicates that all connected
    displays will be forced to synchronize.

`disable_hpd_irq`
:   disables all HPD and HPD RX interrupt handling in the
    driver when true

`dmcub_trace_event_en`
:   enable dmcub trace events

`da_list`
:   DAL fb memory allocation list, for communication with SMU.

`dmub_aux_transfer_done`
:   struct completion used to indicate when DMUB
    transfers are done

`delayed_hpd_wq`
:   work queue used to delay DMUB HPD work

`brightness`
:   cached backlight values.

`actual_brightness`
:   last successfully applied backlight values.

`aux_hpd_discon_quirk`
:   quirk for hpd discon while aux is on-going.
    occurred on certain intel platform

`dpia_aux_lock`
:   Guards access to DPIA AUX

struct amdgpu_hdmi_vsdb_info
:   Keep track of the VSDB info

**Definition**:

```
struct amdgpu_hdmi_vsdb_info {
    unsigned int amd_vsdb_version;
    bool freesync_supported;
    unsigned int min_refresh_rate_hz;
    unsigned int max_refresh_rate_hz;
    bool replay_mode;
};
```

**Members**

`amd_vsdb_version`
:   Vendor Specific Data Block Version, should be
    used to determine which Vendor Specific InfoFrame (VSIF) to send.

`freesync_supported`
:   FreeSync Supported.

`min_refresh_rate_hz`
:   FreeSync Minimum Refresh Rate in Hz.

`max_refresh_rate_hz`
:   FreeSync Maximum Refresh Rate in Hz

`replay_mode`
:   Replay supported

**Description**

AMDGPU supports FreeSync over HDMI by using the VSDB section, and this
struct is useful to keep track of the display-specific information about
FreeSync.

## [Lifecycle](display-manager.md#id2)

DM (and consequently DC) is registered in the amdgpu base driver as a IP
block. When CONFIG_DRM_AMD_DC is enabled, the DM device IP block is added to
the base driver's device list to be initialized and torn down accordingly.

The functions to do so are provided as hooks in [`struct amd_ip_funcs`](../driver-core.md#c.amd_ip_funcs "amd_ip_funcs").

int dm_hw_init(void \*handle)
:   Initialize DC device

**Parameters**

`void *handle`
:   The base driver device containing the amdgpu_dm device.

**Description**

Initialize the [`struct amdgpu_display_manager`](display-manager.md#c.amdgpu_display_manager "amdgpu_display_manager") device. This involves calling
the initializers of each DM component, then populating the struct with them.

Although the function implies hardware initialization, both hardware and
software are initialized here. Splitting them out to their relevant init
hooks is a future TODO item.

Some notable things that are initialized here:

- Display Core, both software and hardware
- DC modules that we need (freesync and color management)
- DRM software states
- Interrupt sources and handlers
- Vblank support
- Debug FS entries, if enabled

int dm_hw_fini(void \*handle)
:   Teardown DC device

**Parameters**

`void *handle`
:   The base driver device containing the amdgpu_dm device.

**Description**

Teardown components within [`struct amdgpu_display_manager`](display-manager.md#c.amdgpu_display_manager "amdgpu_display_manager") that require
cleanup. This involves cleaning up the DRM device, DC, and any modules that
were loaded. Also flush IRQ workqueues and disable them.

## [Interrupts](display-manager.md#id3)

DM provides another layer of IRQ management on top of what the base driver
already provides. This is something that could be cleaned up, and is a
future TODO item.

The base driver provides IRQ source registration with DRM, handler
registration into the base driver's IRQ table, and a handler callback
[`amdgpu_irq_handler()`](../driver-core.md#c.amdgpu_irq_handler "amdgpu_irq_handler"), with which DRM calls on interrupts. This generic
handler looks up the IRQ table, and calls the respective
`amdgpu_irq_src_funcs.process` hookups.

What DM provides on top are two IRQ tables specifically for top-half and
bottom-half IRQ handling, with the bottom-half implementing workqueues:

- [`amdgpu_display_manager.irq_handler_list_high_tab`](display-manager.md#c.amdgpu_display_manager "amdgpu_display_manager")
- [`amdgpu_display_manager.irq_handler_list_low_tab`](display-manager.md#c.amdgpu_display_manager "amdgpu_display_manager")

They override the base driver's IRQ table, and the effect can be seen
in the hooks that DM provides for `amdgpu_irq_src_funcs.process`. They
are all set to the DM generic handler [`amdgpu_dm_irq_handler()`](display-manager.md#c.amdgpu_dm_irq_handler "amdgpu_dm_irq_handler"), which looks up
DM's IRQ tables. However, in order for base driver to recognize this hook, DM
still needs to register the IRQ with the base driver. See
dce110_register_irq_handlers() and dcn10_register_irq_handlers().

To expose DC's hardware interrupt toggle to the base driver, DM implements
`amdgpu_irq_src_funcs.set` hooks. Base driver calls it through
[`amdgpu_irq_update()`](../driver-core.md#c.amdgpu_irq_update "amdgpu_irq_update") to enable or disable the interrupt.

struct amdgpu_dm_irq_handler_data
:   Data for DM interrupt handlers.

**Definition**:

```
struct amdgpu_dm_irq_handler_data {
    struct list_head list;
    interrupt_handler handler;
    void *handler_arg;
    struct amdgpu_display_manager *dm;
    enum dc_irq_source irq_source;
    struct work_struct work;
};
```

**Members**

`list`
:   Linked list entry referencing the next/previous handler

`handler`
:   Handler function

`handler_arg`
:   Argument passed to the handler when triggered

`dm`
:   DM which this handler belongs to

`irq_source`
:   DC interrupt source that this handler is registered for

`work`
:   work struct

void dm_irq_work_func(struct work_struct \*work)
:   Handle an IRQ outside of the interrupt handler proper.

**Parameters**

`struct work_struct *work`
:   work struct

void unregister_all_irq_handlers(struct amdgpu_device \*adev)
:   Cleans up handlers from the DM IRQ table

**Parameters**

`struct amdgpu_device *adev`
:   The base driver device containing the DM device

**Description**

Go through low and high context IRQ tables and deallocate handlers.

void \*amdgpu_dm_irq_register_interrupt(struct amdgpu_device \*adev, struct dc_interrupt_params \*int_params, void (\*ih)(void\*), void \*handler_args)
:   Register a handler within DM.

**Parameters**

`struct amdgpu_device *adev`
:   The base driver device containing the DM device.

`struct dc_interrupt_params *int_params`
:   Interrupt parameters containing the source, and handler context

`void (*ih)(void *)`
:   Function pointer to the interrupt handler to register

`void *handler_args`
:   Arguments passed to the handler when the interrupt occurs

**Description**

Register an interrupt handler for the given IRQ source, under the given
context. The context can either be high or low. High context handlers are
executed directly within ISR context, while low context is executed within a
workqueue, thereby allowing operations that sleep.

Registered handlers are called in a FIFO manner, i.e. the most recently
registered handler will be called first.

**Return**

Handler data [`struct amdgpu_dm_irq_handler_data`](display-manager.md#c.amdgpu_dm_irq_handler_data "amdgpu_dm_irq_handler_data") containing the IRQ
:   source, handler function, and args

void amdgpu_dm_irq_unregister_interrupt(struct amdgpu_device \*adev, enum dc_irq_source irq_source, void \*ih)
:   Remove a handler from the DM IRQ table

**Parameters**

`struct amdgpu_device *adev`
:   The base driver device containing the DM device

`enum dc_irq_source irq_source`
:   IRQ source to remove the given handler from

`void *ih`
:   Function pointer to the interrupt handler to unregister

**Description**

Go through both low and high context IRQ tables, and find the given handler
for the given irq source. If found, remove it. Otherwise, do nothing.

int amdgpu_dm_irq_init(struct amdgpu_device \*adev)
:   Initialize DM IRQ management

**Parameters**

`struct amdgpu_device *adev`
:   The base driver device containing the DM device

**Description**

Initialize DM's high and low context IRQ tables.

The N by M table contains N IRQ sources, with M
[`struct amdgpu_dm_irq_handler_data`](display-manager.md#c.amdgpu_dm_irq_handler_data "amdgpu_dm_irq_handler_data") hooked together in a linked list. The
list_heads are initialized here. When an interrupt n is triggered, all m
handlers are called in sequence, FIFO according to registration order.

The low context table requires special steps to initialize, since handlers
will be deferred to a workqueue. See `struct irq_list_head`.

void amdgpu_dm_irq_fini(struct amdgpu_device \*adev)
:   Tear down DM IRQ management

**Parameters**

`struct amdgpu_device *adev`
:   The base driver device containing the DM device

**Description**

Flush all work within the low context IRQ table.

int amdgpu_dm_irq_handler(struct amdgpu_device \*adev, struct amdgpu_irq_src \*source, struct amdgpu_iv_entry \*entry)
:   Generic DM IRQ handler

**Parameters**

`struct amdgpu_device *adev`
:   amdgpu base driver device containing the DM device

`struct amdgpu_irq_src *source`
:   Unused

`struct amdgpu_iv_entry *entry`
:   Data about the triggered interrupt

**Description**

Calls all registered high irq work immediately, and schedules work for low
irq. The DM IRQ table is used to find the corresponding handlers.

void amdgpu_dm_hpd_init(struct amdgpu_device \*adev)
:   hpd setup callback.

**Parameters**

`struct amdgpu_device *adev`
:   amdgpu_device pointer

**Description**

Setup the hpd pins used by the card (evergreen+).
Enable the pin, set the polarity, and enable the hpd interrupts.

void amdgpu_dm_hpd_fini(struct amdgpu_device \*adev)
:   hpd tear down callback.

**Parameters**

`struct amdgpu_device *adev`
:   amdgpu_device pointer

**Description**

Tear down the hpd pins used by the card (evergreen+).
Disable the hpd interrupts.

void dm_pflip_high_irq(void \*interrupt_params)
:   Handle pageflip interrupt

**Parameters**

`void *interrupt_params`
:   ignored

**Description**

Handles the pageflip interrupt by notifying all interested parties
that the pageflip has been completed.

void dm_crtc_high_irq(void \*interrupt_params)
:   Handles CRTC interrupt

**Parameters**

`void *interrupt_params`
:   used for determining the CRTC instance

**Description**

Handles the CRTC/VSYNC interrupt by notfying DRM's VBLANK
event handler.

## [Atomic Implementation](display-manager.md#id4)

*WIP*

void amdgpu_dm_atomic_commit_tail(struct [drm_atomic_state](../../drm-kms.md#c.drm_atomic_state "drm_atomic_state") \*state)
:   AMDgpu DM's commit tail implementation.

**Parameters**

`struct drm_atomic_state *state`
:   The atomic state to commit

**Description**

This will tell DC to commit the constructed DC state from atomic_check,
programming the hardware. Any failures here implies a hardware failure, since
atomic check should have filtered anything non-kosher.

int amdgpu_dm_atomic_check(struct [drm_device](../../drm-internals.md#c.drm_device "drm_device") \*dev, struct [drm_atomic_state](../../drm-kms.md#c.drm_atomic_state "drm_atomic_state") \*state)
:   Atomic check implementation for AMDgpu DM.

**Parameters**

`struct drm_device *dev`
:   The DRM device

`struct drm_atomic_state *state`
:   The atomic state to commit

**Description**

Validate that the given atomic state is programmable by DC into hardware.
This involves constructing a `struct dc_state` reflecting the new hardware
state we wish to commit, then querying DC to see if it is programmable. It's
important not to modify the existing DC state. Otherwise, atomic_check
may unexpectedly commit hardware changes.

When validating the DC state, it's important that the right locks are
acquired. For full updates case which removes/adds/updates streams on one
CRTC while flipping on another CRTC, acquiring global lock will guarantee
that any such full update commit will wait for completion of any outstanding
flip using DRMs synchronization events.

Note that DM adds the affected connectors for all CRTCs in state, when that
might not seem necessary. This is because DC stream creation requires the
DC sink, which is tied to the DRM connector state. Cleaning this up should
be possible but non-trivial - a possible TODO item.

**Return**

-Error code if validation failed.

## [Color Management Properties](display-manager.md#id5)

The DC interface to HW gives us the following color management blocks
per pipe (surface):

- Input gamma LUT (de-normalized)
- Input CSC (normalized)
- Surface degamma LUT (normalized)
- Surface CSC (normalized)
- Surface regamma LUT (normalized)
- Output CSC (normalized)

But these aren't a direct mapping to DRM color properties. The current DRM
interface exposes CRTC degamma, CRTC CTM and CRTC regamma while our hardware
is essentially giving:

Plane CTM -> Plane degamma -> Plane CTM -> Plane regamma -> Plane CTM

The input gamma LUT block isn't really applicable here since it operates
on the actual input data itself rather than the HW fp representation. The
input and output CSC blocks are technically available to use as part of
the DC interface but are typically used internally by DC for conversions
between color spaces. These could be blended together with user
adjustments in the future but for now these should remain untouched.

The pipe blending also happens after these blocks so we don't actually
support any CRTC props with correct blending with multiple planes - but we
can still support CRTC color management properties in DM in most single
plane cases correctly with clever management of the DC interface in DM.

As per DRM documentation, blocks should be in hardware bypass when their
respective property is set to NULL. A linear DGM/RGM LUT should also
considered as putting the respective block into bypass mode.

This means that the following
configuration is assumed to be the default:

Plane DGM Bypass -> Plane CTM Bypass -> Plane RGM Bypass -> ...
CRTC DGM Bypass -> CRTC CTM Bypass -> CRTC RGM Bypass

void amdgpu_dm_init_color_mod(void)
:   Initialize the color module.

**Parameters**

`void`
:   no arguments

**Description**

We're not using the full color module, only certain components.
Only call setup functions for components that we need.

const struct drm_color_lut \*__extract_blob_lut(const struct [drm_property_blob](../../drm-kms.md#c.drm_property_blob "drm_property_blob") \*blob, uint32_t \*size)
:   Extracts the DRM lut and lut size from a blob.

**Parameters**

`const struct drm_property_blob *blob`
:   DRM color mgmt property blob

`uint32_t *size`
:   lut size

**Return**

DRM LUT or NULL

bool __is_lut_linear(const struct drm_color_lut \*lut, uint32_t size)
:   check if the given lut is a linear mapping of values

**Parameters**

`const struct drm_color_lut *lut`
:   given lut to check values

`uint32_t size`
:   lut size

**Description**

It is considered linear if the lut represents:
f(a) = (0xFF00/MAX_COLOR_LUT_ENTRIES-1)a; for integer a in [0,
MAX_COLOR_LUT_ENTRIES)

**Return**

True if the given lut is a linear mapping of values, i.e. it acts like a
bypass LUT. Otherwise, false.

void __drm_lut_to_dc_gamma(const struct drm_color_lut \*lut, struct dc_gamma \*gamma, bool is_legacy)
:   convert the drm_color_lut to dc_gamma.

**Parameters**

`const struct drm_color_lut *lut`
:   DRM lookup table for color conversion

`struct dc_gamma *gamma`
:   DC gamma to set entries

`bool is_legacy`
:   legacy or atomic gamma

**Description**

The conversion depends on the size of the lut - whether or not it's legacy.

void __drm_ctm_to_dc_matrix(const struct drm_color_ctm \*ctm, struct fixed31_32 \*matrix)
:   converts a DRM CTM to a DC CSC float matrix

**Parameters**

`const struct drm_color_ctm *ctm`
:   DRM color transformation matrix

`struct fixed31_32 *matrix`
:   DC CSC float matrix

**Description**

The matrix needs to be a 3x4 (12 entry) matrix.

void __drm_ctm_3x4_to_dc_matrix(const struct drm_color_ctm_3x4 \*ctm, struct fixed31_32 \*matrix)
:   converts a DRM CTM 3x4 to a DC CSC float matrix

**Parameters**

`const struct drm_color_ctm_3x4 *ctm`
:   DRM color transformation matrix with 3x4 dimensions

`struct fixed31_32 *matrix`
:   DC CSC float matrix

**Description**

The matrix needs to be a 3x4 (12 entry) matrix.

int __set_legacy_tf(struct dc_transfer_func \*func, const struct drm_color_lut \*lut, uint32_t lut_size, bool has_rom)
:   Calculates the legacy transfer function

**Parameters**

`struct dc_transfer_func *func`
:   transfer function

`const struct drm_color_lut *lut`
:   lookup table that defines the color space

`uint32_t lut_size`
:   size of respective lut

`bool has_rom`
:   if ROM can be used for hardcoded curve

**Description**

Only for sRGB input space

**Return**

0 in case of success, -ENOMEM if fails

int __set_output_tf(struct dc_transfer_func \*func, const struct drm_color_lut \*lut, uint32_t lut_size, bool has_rom)
:   calculates the output transfer function based on expected input space.

**Parameters**

`struct dc_transfer_func *func`
:   transfer function

`const struct drm_color_lut *lut`
:   lookup table that defines the color space

`uint32_t lut_size`
:   size of respective lut

`bool has_rom`
:   if ROM can be used for hardcoded curve

**Return**

0 in case of success. -ENOMEM if fails.

int __set_input_tf(struct [dc_color_caps](display-manager.md#c.dc_color_caps "dc_color_caps") \*caps, struct dc_transfer_func \*func, const struct drm_color_lut \*lut, uint32_t lut_size)
:   calculates the input transfer function based on expected input space.

**Parameters**

`struct dc_color_caps *caps`
:   dc color capabilities

`struct dc_transfer_func *func`
:   transfer function

`const struct drm_color_lut *lut`
:   lookup table that defines the color space

`uint32_t lut_size`
:   size of respective lut.

**Return**

0 in case of success. -ENOMEM if fails.

int amdgpu_dm_verify_lut3d_size(struct amdgpu_device \*adev, struct [drm_plane_state](../../drm-kms.md#c.drm_plane_state "drm_plane_state") \*plane_state)
:   verifies if 3D LUT is supported and if user shaper and 3D LUTs match the hw supported size

**Parameters**

`struct amdgpu_device *adev`
:   amdgpu device

`struct drm_plane_state *plane_state`
:   the DRM plane state

**Description**

Verifies if pre-blending (DPP) 3D LUT is supported by the HW (DCN 2.0 or
newer) and if the user shaper and 3D LUTs match the supported size.

**Return**

0 on success. -EINVAL if lut size are invalid.

int amdgpu_dm_verify_lut_sizes(const struct [drm_crtc_state](../../drm-kms.md#c.drm_crtc_state "drm_crtc_state") \*crtc_state)
:   verifies if DRM luts match the hw supported sizes

**Parameters**

`const struct drm_crtc_state *crtc_state`
:   the DRM CRTC state

**Description**

Verifies that the Degamma and Gamma LUTs attached to the `crtc_state`
are of the expected size.

**Return**

0 on success. -EINVAL if any lut sizes are invalid.

int amdgpu_dm_update_crtc_color_mgmt(struct dm_crtc_state \*crtc)
:   Maps DRM color management to DC stream.

**Parameters**

`struct dm_crtc_state *crtc`
:   amdgpu_dm crtc state

**Description**

With no plane level color management properties we're free to use any
of the HW blocks as long as the CRTC CTM always comes before the
CRTC RGM and after the CRTC DGM.

- The CRTC RGM block will be placed in the RGM LUT block if it is non-linear.
- The CRTC DGM block will be placed in the DGM LUT block if it is non-linear.
- The CRTC CTM will be placed in the gamut remap block if it is non-linear.

The RGM block is typically more fully featured and accurate across
all ASICs - DCE can't support a custom non-linear CRTC DGM.

For supporting both plane level color management and CRTC level color
management at once we have to either restrict the usage of CRTC properties
or blend adjustments together.

**Return**

0 on success. Error code if setup fails.

int amdgpu_dm_update_plane_color_mgmt(struct dm_crtc_state \*crtc, struct [drm_plane_state](../../drm-kms.md#c.drm_plane_state "drm_plane_state") \*plane_state, struct [dc_plane_state](display-manager.md#c.amdgpu_dm_update_plane_color_mgmt "dc_plane_state") \*dc_plane_state)
:   Maps DRM color management to DC plane.

**Parameters**

`struct dm_crtc_state *crtc`
:   amdgpu_dm crtc state

`struct drm_plane_state *plane_state`
:   DRM plane state

`struct dc_plane_state *dc_plane_state`
:   target DC surface

**Description**

Update the underlying dc_stream_state's input transfer function (ITF) in
preparation for hardware commit. The transfer function used depends on
the preparation done on the stream for color management.

**Return**

0 on success. -ENOMEM if mem allocation fails.

### [DC Color Capabilities between DCN generations](display-manager.md#id6)

DRM/KMS framework defines three CRTC color correction properties: degamma,
color transformation matrix (CTM) and gamma, and two properties for degamma and
gamma LUT sizes. AMD DC programs some of the color correction features
pre-blending but DRM/KMS has not per-plane color correction properties.

In general, the DRM CRTC color properties are programmed to DC, as follows:
CRTC gamma after blending, and CRTC degamma pre-blending. Although CTM is
programmed after blending, it is mapped to DPP hw blocks (pre-blending). Other
color caps available in the hw is not currently exposed by DRM interface and
are bypassed.

**Color management caps (DPP and MPC)**

Modules/color calculates various color operations which are translated to
abstracted HW. DCE 5-12 had almost no important changes, but starting with
DCN1, every new generation comes with fairly major differences in color
pipeline. Therefore, we abstract color pipe capabilities so modules/DM can
decide mapping to HW block based on logical capabilities.

struct rom_curve_caps
:   predefined transfer function caps for degamma and regamma

**Definition**:

```
struct rom_curve_caps {
    uint16_t srgb : 1;
    uint16_t bt2020 : 1;
    uint16_t gamma2_2 : 1;
    uint16_t pq : 1;
    uint16_t hlg : 1;
};
```

**Members**

`srgb`
:   RGB color space transfer func

`bt2020`
:   BT.2020 transfer func

`gamma2_2`
:   standard gamma

`pq`
:   perceptual quantizer transfer function

`hlg`
:   hybrid log–gamma transfer function

struct dpp_color_caps
:   color pipeline capabilities for display pipe and plane blocks

**Definition**:

```
struct dpp_color_caps {
    uint16_t dcn_arch : 1;
    uint16_t input_lut_shared : 1;
    uint16_t icsc : 1;
    uint16_t dgam_ram : 1;
    uint16_t post_csc : 1;
    uint16_t gamma_corr : 1;
    uint16_t hw_3d_lut : 1;
    uint16_t ogam_ram : 1;
    uint16_t ocsc : 1;
    uint16_t dgam_rom_for_yuv : 1;
    struct rom_curve_caps dgam_rom_caps;
    struct rom_curve_caps ogam_rom_caps;
};
```

**Members**

`dcn_arch`
:   all DCE generations treated the same

`input_lut_shared`
:   shared with DGAM. Input LUT is different than most LUTs,
    just plain 256-entry lookup

`icsc`
:   input color space conversion

`dgam_ram`
:   programmable degamma LUT

`post_csc`
:   post color space conversion, before gamut remap

`gamma_corr`
:   degamma correction

`hw_3d_lut`
:   3D LUT support. It implies a shaper LUT before. It may be shared
    with MPC by setting mpc:shared_3d_lut flag

`ogam_ram`
:   programmable out/blend gamma LUT

`ocsc`
:   output color space conversion

`dgam_rom_for_yuv`
:   pre-defined degamma LUT for YUV planes

`dgam_rom_caps`
:   pre-definied curve caps for degamma 1D LUT

`ogam_rom_caps`
:   pre-definied curve caps for regamma 1D LUT

**Note**

hdr_mult and gamut remap (CTM) are always available in DPP (in that order)

struct mpc_color_caps
:   color pipeline capabilities for multiple pipe and plane combined blocks

**Definition**:

```
struct mpc_color_caps {
    uint16_t gamut_remap : 1;
    uint16_t ogam_ram : 1;
    uint16_t ocsc : 1;
    uint16_t num_3dluts : 3;
    uint16_t shared_3d_lut:1;
    struct rom_curve_caps ogam_rom_caps;
};
```

**Members**

`gamut_remap`
:   color transformation matrix

`ogam_ram`
:   programmable out gamma LUT

`ocsc`
:   output color space conversion matrix

`num_3dluts`
:   MPC 3D LUT; always assumes a preceding shaper LUT

`shared_3d_lut`
:   shared 3D LUT flag. Can be either DPP or MPC, but single
    instance

`ogam_rom_caps`
:   pre-definied curve caps for regamma 1D LUT

struct dc_color_caps
:   color pipes capabilities for DPP and MPC hw blocks

**Definition**:

```
struct dc_color_caps {
    struct dpp_color_caps dpp;
    struct mpc_color_caps mpc;
};
```

**Members**

`dpp`
:   color pipes caps for DPP

`mpc`
:   color pipes caps for MPC

enum pipe_split_policy
:   Pipe split strategy supported by DCN

**Constants**

`MPC_SPLIT_DYNAMIC`
:   DC will automatically decide how to split the
    pipe in order to bring the best trade-off between performance and
    power consumption. This is the recommended option.

`MPC_SPLIT_AVOID`
:   Avoid pipe split, which means that DC will not
    try any sort of split optimization.

`MPC_SPLIT_AVOID_MULT_DISP`
:   With this option, DC will only try to
    optimize the pipe utilization when using a single display; if the
    user connects to a second display, DC will avoid pipe split.

**Description**

This enum is used to define the pipe split policy supported by DCN. By
default, DC favors MPC_SPLIT_DYNAMIC.

struct dc_validation_set
:   Struct to store surface/stream associations for validation

**Definition**:

```
struct dc_validation_set {
    struct dc_stream_state *stream;
    struct dc_plane_state *plane_states[MAX_SURFACES];
    uint8_t plane_count;
};
```

**Members**

`stream`
:   Stream state properties

`plane_states`
:   Surface state

`plane_count`
:   Total of active planes

The color pipeline has undergone major changes between DCN hardware
generations. What's possible to do before and after blending depends on
hardware capabilities, as illustrated below by the DCN 2.0 and DCN 3.0 families
schemas.

**DCN 2.0 family color caps and mapping**

![../../../_images/dcn2_cm_drm_current.svg](../../../_images/dcn2_cm_drm_current.svg)

**DCN 3.0 family color caps and mapping**

![../../../_images/dcn3_cm_drm_current.svg](../../../_images/dcn3_cm_drm_current.svg)

## [Blend Mode Properties](display-manager.md#id7)

Pixel blend mode is a DRM plane composition property of [`drm_plane`](../../drm-kms.md#c.drm_plane "drm_plane") used to
describes how pixels from a foreground plane (fg) are composited with the
background plane (bg). Here, we present main concepts of DRM blend mode to help
to understand how this property is mapped to AMD DC interface. See more about
this DRM property and the alpha blending equations in [DRM Plane
Composition Properties](../../drm-kms.md#plane-composition-properties).

Basically, a blend mode sets the alpha blending equation for plane
composition that fits the mode in which the alpha channel affects the state of
pixel color values and, therefore, the resulted pixel color. For
example, consider the following elements of the alpha blending equation:

- *fg.rgb*: Each of the RGB component values from the foreground's pixel.
- *fg.alpha*: Alpha component value from the foreground's pixel.
- *bg.rgb*: Each of the RGB component values from the background.
- *plane_alpha*: Plane alpha value set by the **plane "alpha" property**, see
  more in [DRM Plane Composition Properties](../../drm-kms.md#plane-composition-properties).

in the basic alpha blending equation:

```
out.rgb = alpha * fg.rgb + (1 - alpha) * bg.rgb
```

the alpha channel value of each pixel in a plane is ignored and only the plane
alpha affects the resulted pixel color values.

DRM has three blend mode to define the blend formula in the plane composition:

- **None**: Blend formula that ignores the pixel alpha.
- **Pre-multiplied**: Blend formula that assumes the pixel color values in a
  plane was already pre-multiplied by its own alpha channel before storage.
- **Coverage**: Blend formula that assumes the pixel color values were not
  pre-multiplied with the alpha channel values.

and pre-multiplied is the default pixel blend mode, that means, when no blend
mode property is created or defined, DRM considers the plane's pixels has
pre-multiplied color values. On IGT GPU tools, the kms_plane_alpha_blend test
provides a set of subtests to verify plane alpha and blend mode properties.

The DRM blend mode and its elements are then mapped by AMDGPU display manager
(DM) to program the blending configuration of the Multiple Pipe/Plane Combined
(MPC), as follows:

Multiple Pipe/Plane Combined (MPC) is a component in the hardware pipeline
that performs blending of multiple planes, using global and per-pixel alpha.
It also performs post-blending color correction operations according to the
hardware capabilities, such as color transformation matrix and gamma 1D and
3D LUT.

struct mpcc_blnd_cfg
:   MPCC blending configuration

**Definition**:

```
struct mpcc_blnd_cfg {
    struct tg_color black_color;
    enum mpcc_alpha_blend_mode alpha_mode;
    bool pre_multiplied_alpha;
    int global_gain;
    int global_alpha;
    bool overlap_only;
    int bottom_gain_mode;
    int background_color_bpc;
    int top_gain;
    int bottom_inside_gain;
    int bottom_outside_gain;
};
```

**Members**

`black_color`
:   background color

`alpha_mode`
:   alpha blend mode (MPCC_ALPHA_BLND_MODE)

`pre_multiplied_alpha`
:   whether pixel color values were pre-multiplied by the
    alpha channel (MPCC_ALPHA_MULTIPLIED_MODE)

`global_gain`
:   used when blend mode considers both pixel alpha and plane
    alpha value and assumes the global alpha value.

`global_alpha`
:   plane alpha value

`overlap_only`
:   whether overlapping of different planes is allowed

`bottom_gain_mode`
:   blend mode for bottom gain setting

`background_color_bpc`
:   background color for bpc

`top_gain`
:   top gain setting

`bottom_inside_gain`
:   blend mode for bottom inside

`bottom_outside_gain`
:   blend mode for bottom outside

Therefore, the blending configuration for a single MPCC instance on the MPC
tree is defined by [`mpcc_blnd_cfg`](display-manager.md#c.mpcc_blnd_cfg "mpcc_blnd_cfg"), where
`pre_multiplied_alpha` is the alpha pre-multiplied mode flag used to
set `MPCC_ALPHA_MULTIPLIED_MODE`. It controls whether alpha is
multiplied (true/false), being only true for DRM pre-multiplied blend mode.
[`mpcc_alpha_blend_mode`](display-manager.md#c.mpcc_alpha_blend_mode "mpcc_alpha_blend_mode") defines the alpha blend mode regarding pixel
alpha and plane alpha values. It sets one of the three modes for
`MPCC_ALPHA_BLND_MODE`, as described below.

enum mpcc_alpha_blend_mode
:   define the alpha blend mode regarding pixel alpha and plane alpha values

**Constants**

`MPCC_ALPHA_BLEND_MODE_PER_PIXEL_ALPHA`
:   per pixel alpha using DPP
    alpha value

`MPCC_ALPHA_BLEND_MODE_PER_PIXEL_ALPHA_COMBINED_GLOBAL_GAIN`
:   per
    pixel alpha using DPP alpha value multiplied by a global gain (plane
    alpha)

`MPCC_ALPHA_BLEND_MODE_GLOBAL_ALPHA`
:   global alpha value, ignores
    pixel alpha and consider only plane alpha

DM then maps the elements of [`enum mpcc_alpha_blend_mode`](display-manager.md#c.mpcc_alpha_blend_mode "mpcc_alpha_blend_mode") to those in the DRM
blend formula, as follows:

- *MPC pixel alpha* matches *DRM fg.alpha* as the alpha component value
  from the plane's pixel
- *MPC global alpha* matches *DRM plane_alpha* when the pixel alpha should
  be ignored and, therefore, pixel values are not pre-multiplied
- *MPC global gain* assumes *MPC global alpha* value when both *DRM
  fg.alpha* and *DRM plane_alpha* participate in the blend equation

In short, *fg.alpha* is ignored by selecting
`MPCC_ALPHA_BLEND_MODE_GLOBAL_ALPHA`. On the other hand, (plane_alpha \*
fg.alpha) component becomes available by selecting
`MPCC_ALPHA_BLEND_MODE_PER_PIXEL_ALPHA_COMBINED_GLOBAL_GAIN`. And the
`MPCC_ALPHA_MULTIPLIED_MODE` defines if the pixel color values are
pre-multiplied by alpha or not.

### [Blend configuration flow](display-manager.md#id8)

The alpha blending equation is configured from DRM to DC interface by the
following path:

1. When updating a [`drm_plane_state`](../../drm-kms.md#c.drm_plane_state "drm_plane_state"), DM calls
   `amdgpu_dm_plane_fill_blending_from_plane_state()` that maps
   [`drm_plane_state`](../../drm-kms.md#c.drm_plane_state "drm_plane_state") attributes to
   `dc_plane_info` struct to be handled in the
   OS-agnostic component (DC).
2. On DC interface, [`struct mpcc_blnd_cfg`](display-manager.md#c.mpcc_blnd_cfg "mpcc_blnd_cfg") programs the
   MPCC blend configuration considering the `dc_plane_info` input from DPP.
