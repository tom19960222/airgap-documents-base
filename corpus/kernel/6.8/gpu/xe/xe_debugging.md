---
collection: kernel
version: "6.8"
title: "Debugging"
source_url: https://www.kernel.org/doc/html/v6.8/gpu/xe/xe_debugging.html
fetched_at: 2026-08-21T03:41:24+00:00
---
# Debugging

**Xe ASSERTs**

While Xe driver aims to be simpler than legacy i915 driver it is still
complex enough that some changes introduced while adding new functionality
could break the existing code.

Adding `drm_WARN` or `drm_err` to catch unwanted programming usage could lead
to undesired increased driver footprint and may impact production driver
performance as this additional code will be always present.

To allow annotate functions with additional detailed debug checks to assert
that all prerequisites are satisfied, without worrying about footprint or
performance penalty on production builds where all potential misuses
introduced during code integration were already fixed, we introduce family
of Xe assert macros that try to follow classic assert() utility:

> - [`xe_assert()`](xe_debugging.md#c.xe_assert "xe_assert")
> - [`xe_tile_assert()`](xe_debugging.md#c.xe_tile_assert "xe_tile_assert")
> - [`xe_gt_assert()`](xe_debugging.md#c.xe_gt_assert "xe_gt_assert")

These macros are implemented on top of `drm_WARN`, but unlikely to the origin,
warning is triggered when provided condition is false. Additionally all above
assert macros cannot be used in expressions or as a condition, since
underlying code will be compiled out on non-debug builds.

Note that these macros are not intended for use to cover known gaps in the
implementation; for such cases use regular `drm_WARN` or `drm_err` and provide
valid safe fallback.

Also in cases where performance or footprint is not an issue, developers
should continue to use the regular `drm_WARN` or `drm_err` to ensure that bug
reports from production builds will contain meaningful diagnostics data.

Below code shows how asserts could help in debug to catch unplanned use:

```
static void one_igfx(struct xe_device *xe)
{
        xe_assert(xe, xe->info.is_dgfx == false);
        xe_assert(xe, xe->info.tile_count == 1);
}

static void two_dgfx(struct xe_device *xe)
{
        xe_assert(xe, xe->info.is_dgfx);
        xe_assert(xe, xe->info.tile_count == 2);
}

void foo(struct xe_device *xe)
{
        if (xe->info.dgfx)
                return two_dgfx(xe);
        return one_igfx(xe);
}

void bar(struct xe_device *xe)
{
        if (drm_WARN_ON(xe->drm, xe->info.tile_count > 2))
                return;

        if (xe->info.tile_count == 2)
                return two_dgfx(xe);
        return one_igfx(xe);
}
```

xe_assert

`xe_assert (xe, condition)`

> warn if condition is false when debugging.

**Parameters**

`xe`
:   the `struct xe_device` pointer to which `condition` applies

`condition`
:   condition to check

**Description**

[`xe_assert()`](xe_debugging.md#c.xe_assert "xe_assert") uses `drm_WARN` to emit a warning and print additional information
that could be read from the `xe` pointer if provided `condition` is false.

Contrary to `drm_WARN`, [`xe_assert()`](xe_debugging.md#c.xe_assert "xe_assert") is effective only on debug builds
(`CONFIG_DRM_XE_DEBUG` must be enabled) and cannot be used in expressions
or as a condition.

See [Xe ASSERTs](xe_debugging.md#xe-asserts) for general usage guidelines.

xe_tile_assert

`xe_tile_assert (tile, condition)`

> warn if condition is false when debugging.

**Parameters**

`tile`
:   the `struct xe_tile` pointer to which `condition` applies

`condition`
:   condition to check

**Description**

[`xe_tile_assert()`](xe_debugging.md#c.xe_tile_assert "xe_tile_assert") uses `drm_WARN` to emit a warning and print additional
information that could be read from the `tile` pointer if provided `condition`
is false.

Contrary to `drm_WARN`, [`xe_tile_assert()`](xe_debugging.md#c.xe_tile_assert "xe_tile_assert") is effective only on debug builds
(`CONFIG_DRM_XE_DEBUG` must be enabled) and cannot be used in expressions
or as a condition.

See [Xe ASSERTs](xe_debugging.md#xe-asserts) for general usage guidelines.

xe_gt_assert

`xe_gt_assert (gt, condition)`

> warn if condition is false when debugging.

**Parameters**

`gt`
:   the `struct xe_gt` pointer to which `condition` applies

`condition`
:   condition to check

**Description**

[`xe_gt_assert()`](xe_debugging.md#c.xe_gt_assert "xe_gt_assert") uses `drm_WARN` to emit a warning and print additional
information that could be safetely read from the `gt` pointer if provided
`condition` is false.

Contrary to `drm_WARN`, [`xe_gt_assert()`](xe_debugging.md#c.xe_gt_assert "xe_gt_assert") is effective only on debug builds
(`CONFIG_DRM_XE_DEBUG` must be enabled) and cannot be used in expressions
or as a condition.

See [Xe ASSERTs](xe_debugging.md#xe-asserts) for general usage guidelines.
