---
collection: kernel
version: "6.8"
title: "Register Table Processing"
source_url: https://www.kernel.org/doc/html/v6.8/gpu/xe/xe_rtp.html
fetched_at: 2026-08-21T03:41:26+00:00
---
# Register Table Processing

Internal infrastructure to define how registers should be updated based on
rules and actions. This can be used to define tables with multiple entries
(one per register) that will be walked over at some point in time to apply
the values to the registers that have matching rules.

## Internal API

struct xe_rtp_action
:   action to take for any matching rule

**Definition**:

```
struct xe_rtp_action {
    struct xe_reg           reg;
    u32 clr_bits;
    u32 set_bits;
#define XE_RTP_NOCHECK          .read_mask = 0;
    u32 read_mask;
#define XE_RTP_ACTION_FLAG_ENGINE_BASE          BIT(0);
    u8 flags;
};
```

**Members**

`reg`
:   Register

`clr_bits`
:   bits to clear when updating register. It's always a
    superset of bits being modified

`set_bits`
:   bits to set when updating register

`read_mask`
:   mask for bits to consider when reading value back

`flags`
:   flags to apply on rule evaluation or action

**Description**

This struct records what action should be taken in a register that has a
matching rule. Example of actions: set/clear bits.

XE_RTP_RULE_PLATFORM

`XE_RTP_RULE_PLATFORM (plat_)`

> Create rule matching platform

**Parameters**

`plat_`
:   platform to match

**Description**

Refer to [`XE_RTP_RULES()`](xe_rtp.md#c.XE_RTP_RULES "XE_RTP_RULES") for expected usage.

XE_RTP_RULE_SUBPLATFORM

`XE_RTP_RULE_SUBPLATFORM (plat_, sub_)`

> Create rule matching platform and sub-platform

**Parameters**

`plat_`
:   platform to match

`sub_`
:   sub-platform to match

**Description**

Refer to [`XE_RTP_RULES()`](xe_rtp.md#c.XE_RTP_RULES "XE_RTP_RULES") for expected usage.

XE_RTP_RULE_GRAPHICS_STEP

`XE_RTP_RULE_GRAPHICS_STEP (start_, end_)`

> Create rule matching graphics stepping

**Parameters**

`start_`
:   First stepping matching the rule

`end_`
:   First stepping that does not match the rule

**Description**

Note that the range matching this rule is [ **start_**, **end_** ), i.e. inclusive
on the left, exclusive on the right.

Refer to [`XE_RTP_RULES()`](xe_rtp.md#c.XE_RTP_RULES "XE_RTP_RULES") for expected usage.

XE_RTP_RULE_MEDIA_STEP

`XE_RTP_RULE_MEDIA_STEP (start_, end_)`

> Create rule matching media stepping

**Parameters**

`start_`
:   First stepping matching the rule

`end_`
:   First stepping that does not match the rule

**Description**

Note that the range matching this rule is [ **start_**, **end_** ), i.e. inclusive
on the left, exclusive on the right.

Refer to [`XE_RTP_RULES()`](xe_rtp.md#c.XE_RTP_RULES "XE_RTP_RULES") for expected usage.

XE_RTP_RULE_ENGINE_CLASS

`XE_RTP_RULE_ENGINE_CLASS (cls_)`

> Create rule matching an engine class

**Parameters**

`cls_`
:   Engine class to match

**Description**

Refer to [`XE_RTP_RULES()`](xe_rtp.md#c.XE_RTP_RULES "XE_RTP_RULES") for expected usage.

XE_RTP_RULE_FUNC

`XE_RTP_RULE_FUNC (func__)`

> Create rule using callback function for match

**Parameters**

`func__`
:   Function to call to decide if rule matches

**Description**

This allows more complex checks to be performed. The `XE_RTP`
infrastructure will simply call the function **func_** passed to decide if this
rule matches the device.

Refer to [`XE_RTP_RULES()`](xe_rtp.md#c.XE_RTP_RULES "XE_RTP_RULES") for expected usage.

XE_RTP_RULE_GRAPHICS_VERSION

`XE_RTP_RULE_GRAPHICS_VERSION (ver__)`

> Create rule matching graphics version

**Parameters**

`ver__`
:   Graphics IP version to match

**Description**

Refer to [`XE_RTP_RULES()`](xe_rtp.md#c.XE_RTP_RULES "XE_RTP_RULES") for expected usage.

XE_RTP_RULE_GRAPHICS_VERSION_RANGE

`XE_RTP_RULE_GRAPHICS_VERSION_RANGE (ver_start__, ver_end__)`

> Create rule matching a range of graphics version

**Parameters**

`ver_start__`
:   First graphics IP version to match

`ver_end__`
:   Last graphics IP version to match

**Description**

Note that the range matching this rule is [ **ver_start__**, **ver_end__** ], i.e.
inclusive on boths sides

Refer to [`XE_RTP_RULES()`](xe_rtp.md#c.XE_RTP_RULES "XE_RTP_RULES") for expected usage.

XE_RTP_RULE_MEDIA_VERSION

`XE_RTP_RULE_MEDIA_VERSION (ver__)`

> Create rule matching media version

**Parameters**

`ver__`
:   Graphics IP version to match

**Description**

Refer to [`XE_RTP_RULES()`](xe_rtp.md#c.XE_RTP_RULES "XE_RTP_RULES") for expected usage.

XE_RTP_RULE_MEDIA_VERSION_RANGE

`XE_RTP_RULE_MEDIA_VERSION_RANGE (ver_start__, ver_end__)`

> Create rule matching a range of media version

**Parameters**

`ver_start__`
:   First media IP version to match

`ver_end__`
:   Last media IP version to match

**Description**

Note that the range matching this rule is [ **ver_start__**, **ver_end__** ], i.e.
inclusive on boths sides

Refer to [`XE_RTP_RULES()`](xe_rtp.md#c.XE_RTP_RULES "XE_RTP_RULES") for expected usage.

XE_RTP_RULE_IS_INTEGRATED

`XE_RTP_RULE_IS_INTEGRATED ()`

> Create a rule matching integrated graphics devices

**Parameters**

**Description**

Refer to [`XE_RTP_RULES()`](xe_rtp.md#c.XE_RTP_RULES "XE_RTP_RULES") for expected usage.

XE_RTP_RULE_IS_DISCRETE

`XE_RTP_RULE_IS_DISCRETE ()`

> Create a rule matching discrete graphics devices

**Parameters**

**Description**

Refer to [`XE_RTP_RULES()`](xe_rtp.md#c.XE_RTP_RULES "XE_RTP_RULES") for expected usage.

XE_RTP_ACTION_WR

`XE_RTP_ACTION_WR (reg_, val_, ...)`

> Helper to write a value to the register, overriding all the bits

**Parameters**

`reg_`
:   Register

`val_`
:   Value to set

`...`
:   Additional fields to override in the [`struct xe_rtp_action`](xe_rtp.md#c.xe_rtp_action "xe_rtp_action") entry

**Description**

The correspondent notation in bspec is:

> REGNAME = VALUE

XE_RTP_ACTION_SET

`XE_RTP_ACTION_SET (reg_, val_, ...)`

> Set bits from **val_** in the register.

**Parameters**

`reg_`
:   Register

`val_`
:   Bits to set in the register

`...`
:   Additional fields to override in the [`struct xe_rtp_action`](xe_rtp.md#c.xe_rtp_action "xe_rtp_action") entry

**Description**

For masked registers this translates to a single write, while for other
registers it's a RMW. The correspondent bspec notation is (example for bits 2
and 5, but could be any):

> REGNAME[2] = 1
> REGNAME[5] = 1

XE_RTP_ACTION_CLR

`XE_RTP_ACTION_CLR (reg_, val_, ...)`

> Clear bits from **val_** in the register.

**Parameters**

`reg_`
:   Register

`val_`
:   Bits to clear in the register

`...`
:   Additional fields to override in the [`struct xe_rtp_action`](xe_rtp.md#c.xe_rtp_action "xe_rtp_action") entry

**Description**

For masked registers this translates to a single write, while for other
registers it's a RMW. The correspondent bspec notation is (example for bits 2
and 5, but could be any):

> REGNAME[2] = 0
> REGNAME[5] = 0

XE_RTP_ACTION_FIELD_SET

`XE_RTP_ACTION_FIELD_SET (reg_, mask_bits_, val_, ...)`

> Set a bit range

**Parameters**

`reg_`
:   Register

`mask_bits_`
:   Mask of bits to be changed in the register, forming a field

`val_`
:   Value to set in the field denoted by **mask_bits_**

`...`
:   Additional fields to override in the [`struct xe_rtp_action`](xe_rtp.md#c.xe_rtp_action "xe_rtp_action") entry

**Description**

For masked registers this translates to a single write, while for other
registers it's a RMW. The correspondent bspec notation is:

> REGNAME[<end>:<start>] = VALUE

XE_RTP_ACTION_WHITELIST

`XE_RTP_ACTION_WHITELIST (reg_, val_, ...)`

> Add register to userspace whitelist

**Parameters**

`reg_`
:   Register

`val_`
:   Whitelist-specific flags to set

`...`
:   Additional fields to override in the [`struct xe_rtp_action`](xe_rtp.md#c.xe_rtp_action "xe_rtp_action") entry

**Description**

Add a register to the whitelist, allowing userspace to modify the ster with
regular user privileges.

XE_RTP_NAME

`XE_RTP_NAME (s_)`

> Helper to set the name in xe_rtp_entry

**Parameters**

`s_`
:   Name describing this rule, often a HW-specific number

**Description**

TODO: maybe move this behind a debug config?

XE_RTP_ENTRY_FLAG

`XE_RTP_ENTRY_FLAG (...)`

> Helper to add multiple flags to a struct xe_rtp_entry_sr

**Parameters**

`...`
:   Entry flags, without the `XE_RTP_ENTRY_FLAG_` prefix

**Description**

Helper to automatically add a `XE_RTP_ENTRY_FLAG_` prefix to the flags
when defining struct xe_rtp_entry entries. Example:

```c
const struct xe_rtp_entry_sr wa_entries[] = {
        ...
        { XE_RTP_NAME("test-entry"),
          ...
          XE_RTP_ENTRY_FLAG(FOREACH_ENGINE),
          ...
        },
        ...
};
```

XE_RTP_ACTION_FLAG

`XE_RTP_ACTION_FLAG (...)`

> Helper to add multiple flags to a [`struct xe_rtp_action`](xe_rtp.md#c.xe_rtp_action "xe_rtp_action")

**Parameters**

`...`
:   Action flags, without the `XE_RTP_ACTION_FLAG_` prefix

**Description**

Helper to automatically add a `XE_RTP_ACTION_FLAG_` prefix to the flags
when defining [`struct xe_rtp_action`](xe_rtp.md#c.xe_rtp_action "xe_rtp_action") entries. Example:

```c
const struct xe_rtp_entry_sr wa_entries[] = {
        ...
        { XE_RTP_NAME("test-entry"),
          ...
          XE_RTP_ACTION_SET(..., XE_RTP_ACTION_FLAG(FOREACH_ENGINE)),
          ...
        },
        ...
};
```

XE_RTP_RULES

`XE_RTP_RULES (...)`

> Helper to set multiple rules to a struct xe_rtp_entry_sr entry

**Parameters**

`...`
:   Rules

**Description**

At least one rule is needed and up to 4 are supported. Multiple rules are
AND'ed together, i.e. all the rules must evaluate to true for the entry to
be processed. See XE_RTP_MATCH_\* for the possible match rules. Example:

```c
const struct xe_rtp_entry_sr wa_entries[] = {
        ...
        { XE_RTP_NAME("test-entry"),
          XE_RTP_RULES(SUBPLATFORM(DG2, G10), GRAPHICS_STEP(A0, B0)),
          ...
        },
        ...
};
```

XE_RTP_ACTIONS

`XE_RTP_ACTIONS (...)`

> Helper to set multiple actions to a struct xe_rtp_entry_sr

**Parameters**

`...`
:   Actions to be taken

**Description**

At least one action is needed and up to 4 are supported. See XE_RTP_ACTION_\*
for the possible actions. Example:

```c
const struct xe_rtp_entry_sr wa_entries[] = {
        ...
        { XE_RTP_NAME("test-entry"),
          XE_RTP_RULES(...),
          XE_RTP_ACTIONS(SET(..), SET(...), CLR(...)),
          ...
        },
        ...
};
```

bool xe_rtp_match_even_instance(const struct xe_gt \*gt, const struct xe_hw_engine \*hwe)
:   Match if engine instance is even

**Parameters**

`const struct xe_gt *gt`
:   GT structure

`const struct xe_hw_engine *hwe`
:   Engine instance

**Return**

true if engine instance is even, false otherwise

void xe_rtp_process_ctx_enable_active_tracking(struct xe_rtp_process_ctx \*ctx, unsigned long \*active_entries, size_t n_entries)
:   Enable tracking of active entries

**Parameters**

`struct xe_rtp_process_ctx *ctx`
:   The context for processing the table

`unsigned long *active_entries`
:   bitmap to store the active entries

`size_t n_entries`
:   number of entries to be processed

**Description**

Set additional metadata to track what entries are considered "active", i.e.
their rules match the condition. Bits are never cleared: entries with
matching rules set the corresponding bit in the bitmap.

void xe_rtp_process_to_sr(struct xe_rtp_process_ctx \*ctx, const struct xe_rtp_entry_sr \*entries, struct xe_reg_sr \*sr)
:   Process all rtp **entries**, adding the matching ones to the save-restore argument.

**Parameters**

`struct xe_rtp_process_ctx *ctx`
:   The context for processing the table, with one of device, gt or hwe

`const struct xe_rtp_entry_sr *entries`
:   Table with RTP definitions

`struct xe_reg_sr *sr`
:   Save-restore struct where matching rules execute the action. This can be
    viewed as the "coalesced view" of multiple the tables. The bits for each
    register set are expected not to collide with previously added entries

**Description**

Walk the table pointed by **entries** (with an empty sentinel) and add all
entries with matching rules to **sr**. If **hwe** is not NULL, its mmio_base is
used to calculate the right register offset

void xe_rtp_process(struct xe_rtp_process_ctx \*ctx, const struct xe_rtp_entry \*entries)
:   Process all rtp **entries**, without running any action

**Parameters**

`struct xe_rtp_process_ctx *ctx`
:   The context for processing the table, with one of device, gt or hwe

`const struct xe_rtp_entry *entries`
:   Table with RTP definitions

**Description**

Walk the table pointed by **entries** (with an empty sentinel), executing the
rules. A few differences from [`xe_rtp_process_to_sr()`](xe_rtp.md#c.xe_rtp_process_to_sr "xe_rtp_process_to_sr"):

1. There is no action associated with each entry since this uses
   struct xe_rtp_entry. Its main use is for marking active workarounds via
   [`xe_rtp_process_ctx_enable_active_tracking()`](xe_rtp.md#c.xe_rtp_process_ctx_enable_active_tracking "xe_rtp_process_ctx_enable_active_tracking").
2. There is support for OR operations by having entries with no name.
