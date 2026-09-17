---
collection: kernel
version: "6.17"
title: "Device Tree (OF) API"
source_url: https://www.kernel.org/doc/html/v6.17/dev-tools/kunit/api/of.html
fetched_at: 2026-09-16T16:26:54+00:00
---
# Device Tree (OF) API

The KUnit device tree API is used to test device tree (of_\*) dependent code.

int __of_overlay_apply_kunit(struct [kunit](test.md#c.kunit "kunit") \*test, u8 \*overlay_begin, const u8 \*overlay_end)
:   Test managed [`of_overlay_fdt_apply()`](../../../devicetree/kernel-api.md#c.of_overlay_fdt_apply "of_overlay_fdt_apply") variant

**Parameters**

`struct kunit *test`
:   test context

`u8 *overlay_begin`
:   start address of overlay to apply

`const u8 *overlay_end`
:   end address of overlay to apply

**Description**

This is mostly internal API. See [`of_overlay_apply_kunit()`](of.md#c.of_overlay_apply_kunit "of_overlay_apply_kunit") for the wrapper
that makes this easier to use.

Similar to [`of_overlay_fdt_apply()`](../../../devicetree/kernel-api.md#c.of_overlay_fdt_apply "of_overlay_fdt_apply"), except the overlay is managed by the test
case and is automatically removed with [`of_overlay_remove()`](../../../devicetree/kernel-api.md#c.of_overlay_remove "of_overlay_remove") after the test
case concludes.

**Return**

0 on success, negative errno on failure

of_overlay_apply_kunit

`of_overlay_apply_kunit (test, overlay_name)`

> Test managed [`of_overlay_fdt_apply()`](../../../devicetree/kernel-api.md#c.of_overlay_fdt_apply "of_overlay_fdt_apply") for built-in overlays

**Parameters**

`test`
:   test context

`overlay_name`
:   name of overlay to apply

**Description**

This macro is used to apply a device tree overlay built with the
cmd_dt_S_dtbo rule in scripts/Makefile.lib that has been compiled into the
kernel image or KUnit test module. The overlay is automatically removed when
the test is finished.

Unit tests that need device tree nodes should compile an overlay file with
**overlay_name**.dtbo.o in their Makefile along with their unit test and then
load the overlay during their test. The **overlay_name** matches the filename
of the overlay without the dtbo filename extension. If CONFIG_OF_OVERLAY is
not enabled, the **test** will be skipped.

In the Makefile

```
obj-$(CONFIG_OF_OVERLAY_KUNIT_TEST) += overlay_test.o kunit_overlay_test.dtbo.o
```

In the test

```c
static void of_overlay_kunit_of_overlay_apply(struct kunit *test)
{
        struct device_node *np;

        KUNIT_ASSERT_EQ(test, 0,
                        of_overlay_apply_kunit(test, kunit_overlay_test));

        np = of_find_node_by_name(NULL, "test-kunit");
        KUNIT_EXPECT_NOT_ERR_OR_NULL(test, np);
        of_node_put(np);
}
```

**Return**

0 on success, negative errno on failure.

void of_root_kunit_skip(struct [kunit](test.md#c.kunit "kunit") \*test)
:   Skip test if the root node isn’t populated

**Parameters**

`struct kunit *test`
:   test to skip if the root node isn’t populated

int of_overlay_fdt_apply_kunit(struct [kunit](test.md#c.kunit "kunit") \*test, void \*overlay_fdt, u32 overlay_fdt_size, int \*ovcs_id)
:   Test managed [`of_overlay_fdt_apply()`](../../../devicetree/kernel-api.md#c.of_overlay_fdt_apply "of_overlay_fdt_apply")

**Parameters**

`struct kunit *test`
:   test context

`void *overlay_fdt`
:   device tree overlay to apply

`u32 overlay_fdt_size`
:   size in bytes of **overlay_fdt**

`int *ovcs_id`
:   identifier of overlay, used to remove the overlay

**Description**

Just like [`of_overlay_fdt_apply()`](../../../devicetree/kernel-api.md#c.of_overlay_fdt_apply "of_overlay_fdt_apply"), except the overlay is managed by the test
case and is automatically removed with [`of_overlay_remove()`](../../../devicetree/kernel-api.md#c.of_overlay_remove "of_overlay_remove") after the test
case concludes.

**Return**

0 on success, negative errno on failure

void of_node_put_kunit(struct [kunit](test.md#c.kunit "kunit") \*test, struct device_node \*node)
:   Test managed [`of_node_put()`](../../../devicetree/kernel-api.md#c.of_node_put "of_node_put")

**Parameters**

`struct kunit *test`
:   test context

`struct device_node *node`
:   node to pass to [`of_node_put()`](../../../devicetree/kernel-api.md#c.of_node_put "of_node_put")

**Description**

Just like [`of_node_put()`](../../../devicetree/kernel-api.md#c.of_node_put "of_node_put"), except the node is managed by the test case and is
automatically put with [`of_node_put()`](../../../devicetree/kernel-api.md#c.of_node_put "of_node_put") after the test case concludes.
