---
collection: kernel
version: "6.8"
title: "Hardware workarounds"
source_url: https://www.kernel.org/doc/html/v6.8/gpu/xe/xe_wa.html
fetched_at: 2026-08-21T03:41:27+00:00
---
# Hardware workarounds

Hardware workarounds are register programming documented to be executed in
the driver that fall outside of the normal programming sequences for a
platform. There are some basic categories of workarounds, depending on
how/when they are applied:

- LRC workarounds: workarounds that touch registers that are
  saved/restored to/from the HW context image. The list is emitted (via Load
  Register Immediate commands) once when initializing the device and saved in
  the default context. That default context is then used on every context
  creation to have a "primed golden context", i.e. a context image that
  already contains the changes needed to all the registers.
- Engine workarounds: the list of these WAs is applied whenever the specific
  engine is reset. It's also possible that a set of engine classes share a
  common power domain and they are reset together. This happens on some
  platforms with render and compute engines. In this case (at least) one of
  them need to keeep the workaround programming: the approach taken in the
  driver is to tie those workarounds to the first compute/render engine that
  is registered. When executing with GuC submission, engine resets are
  outside of kernel driver control, hence the list of registers involved in
  written once, on engine initialization, and then passed to GuC, that
  saves/restores their values before/after the reset takes place. See
  `drivers/gpu/drm/xe/xe_guc_ads.c` for reference.
- GT workarounds: the list of these WAs is applied whenever these registers
  revert to their default values: on GPU reset, suspend/resume [1](xe_wa.md#id2), etc.
- Register whitelist: some workarounds need to be implemented in userspace,
  but need to touch privileged registers. The whitelist in the kernel
  instructs the hardware to allow the access to happen. From the kernel side,
  this is just a special case of a MMIO workaround (as we write the list of
  these to/be-whitelisted registers to some special HW registers).
- Workaround batchbuffers: buffers that get executed automatically by the
  hardware on every HW context restore. These buffers are created and
  programmed in the default context so the hardware always go through those
  programming sequences when switching contexts. The support for workaround
  batchbuffers is enabled these hardware mechanisms:

  1. INDIRECT_CTX: A batchbuffer and an offset are provided in the default
     context, pointing the hardware to jump to that location when that offset
     is reached in the context restore. Workaround batchbuffer in the driver
     currently uses this mechanism for all platforms.
  2. BB_PER_CTX_PTR: A batchbuffer is provided in the default context,
     pointing the hardware to a buffer to continue executing after the
     engine registers are restored in a context restore sequence. This is
     currently not used in the driver.
- Other/OOB: There are WAs that, due to their nature, cannot be applied from
  a central place. Those are peppered around the rest of the code, as needed.
  Workarounds related to the display IP are the main example.

[1](xe_wa.md#id1)
:   Technically, some registers are powercontext saved & restored, so they
    survive a suspend/resume. In practice, writing them again is not too
    costly and simplifies things, so it's the approach taken in the driver.

> **Note:**
>
> Hardware workarounds in xe work the same way as in i915, with the
> difference of how they are maintained in the code. In xe it uses the
> xe_rtp infrastructure so the workarounds can be kept in tables, following
> a more declarative approach rather than procedural.

## Internal API

void xe_wa_process_oob(struct xe_gt \*gt)
:   process OOB workaround table

**Parameters**

`struct xe_gt *gt`
:   GT instance to process workarounds for

**Description**

Process OOB workaround table for this platform, marking in **gt** the
workarounds that are active.

void xe_wa_process_gt(struct xe_gt \*gt)
:   process GT workaround table

**Parameters**

`struct xe_gt *gt`
:   GT instance to process workarounds for

**Description**

Process GT workaround table for this platform, saving in **gt** all the
workarounds that need to be applied at the GT level.

void xe_wa_process_engine(struct xe_hw_engine \*hwe)
:   process engine workaround table

**Parameters**

`struct xe_hw_engine *hwe`
:   engine instance to process workarounds for

**Description**

Process engine workaround table for this platform, saving in **hwe** all the
workarounds that need to be applied at the engine level that match this
engine.

void xe_wa_process_lrc(struct xe_hw_engine \*hwe)
:   process context workaround table

**Parameters**

`struct xe_hw_engine *hwe`
:   engine instance to process workarounds for

**Description**

Process context workaround table for this platform, saving in **hwe** all the
workarounds that need to be applied on context restore. These are workarounds
touching registers that are part of the HW context image.

int xe_wa_init(struct xe_gt \*gt)
:   initialize gt with workaround bookkeeping

**Parameters**

`struct xe_gt *gt`
:   GT instance to initialize

**Description**

Returns 0 for success, negative error code otherwise.
