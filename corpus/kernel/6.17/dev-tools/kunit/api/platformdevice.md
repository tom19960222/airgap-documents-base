---
collection: kernel
version: "6.17"
title: "Platform Device API"
source_url: https://www.kernel.org/doc/html/v6.17/dev-tools/kunit/api/platformdevice.html
fetched_at: 2026-09-16T16:29:01+00:00
---
# Platform Device API

The KUnit platform device API is used to test platform devices.

struct platform_device \*kunit_platform_device_alloc(struct [kunit](test.md#c.kunit "kunit") \*test, const char \*name, int id)
:   Allocate a KUnit test managed platform device

**Parameters**

`struct kunit *test`
:   test context

`const char *name`
:   device name of platform device to alloc

`int id`
:   identifier of platform device to alloc.

**Description**

Allocate a test managed platform device. The device is put when the test completes.

**Return**

Allocated platform device on success, NULL on failure.

int kunit_platform_device_add(struct [kunit](test.md#c.kunit "kunit") \*test, struct platform_device \*pdev)
:   Register a KUnit test managed platform device

**Parameters**

`struct kunit *test`
:   test context

`struct platform_device *pdev`
:   platform device to add

**Description**

Register a test managed platform device. The device is unregistered when the
test completes.

**Return**

0 on success, negative errno on failure.

int kunit_platform_device_prepare_wait_for_probe(struct [kunit](test.md#c.kunit "kunit") \*test, struct platform_device \*pdev, struct completion \*x)
:   Prepare a completion variable to wait for a platform device to probe

**Parameters**

`struct kunit *test`
:   test context

`struct platform_device *pdev`
:   platform device to prepare to wait for probe of

`struct completion *x`
:   completion variable completed when **dev** has probed

**Description**

Prepare a completion variable **x** to wait for **pdev** to probe. Waiting on the
completion forces a preemption, allowing the platform driver to probe.

Example

```c
static int kunit_platform_driver_probe(struct platform_device *pdev)
{
        return 0;
}

static void kunit_platform_driver_test(struct kunit *test)
{
        struct platform_device *pdev;
        struct platform_driver *pdrv;
        DECLARE_COMPLETION_ONSTACK(comp);

        pdev = kunit_platform_device_alloc(test, "kunit-platform", -1);
        KUNIT_ASSERT_NOT_ERR_OR_NULL(test, pdev);
        KUNIT_ASSERT_EQ(test, 0, kunit_platform_device_add(test, pdev));

        pdrv = kunit_kzalloc(test, sizeof(*pdrv), GFP_KERNEL);
        KUNIT_ASSERT_NOT_ERR_OR_NULL(test, pdrv);

        pdrv->probe = kunit_platform_driver_probe;
        pdrv->driver.name = "kunit-platform";
        pdrv->driver.owner = THIS_MODULE;

        KUNIT_ASSERT_EQ(test, 0, kunit_platform_device_prepare_wait_for_probe(test, pdev, &comp));
        KUNIT_ASSERT_EQ(test, 0, kunit_platform_driver_register(test, pdrv));

        KUNIT_EXPECT_NE(test, 0, wait_for_completion_timeout(&comp, 3 * HZ));
}
```

**Return**

0 on success, negative errno on failure.

int kunit_platform_driver_register(struct [kunit](test.md#c.kunit "kunit") \*test, struct platform_driver \*drv)
:   Register a KUnit test managed platform driver

**Parameters**

`struct kunit *test`
:   test context

`struct platform_driver *drv`
:   platform driver to register

**Description**

Register a test managed platform driver. This allows callers to embed the
**drv** in a container structure and use `container_of()` in the probe function
to pass information to KUnit tests.

Example

```c
struct kunit_test_context {
        struct platform_driver pdrv;
        const char *data;
};

static inline struct kunit_test_context *
to_test_context(struct platform_device *pdev)
{
        return container_of(to_platform_driver(pdev->dev.driver),
                            struct kunit_test_context,
                            pdrv);
}

static int kunit_platform_driver_probe(struct platform_device *pdev)
{
        struct kunit_test_context *ctx;

        ctx = to_test_context(pdev);
        ctx->data = "test data";

        return 0;
}

static void kunit_platform_driver_test(struct kunit *test)
{
        struct kunit_test_context *ctx;

        ctx = kunit_kzalloc(test, sizeof(*ctx), GFP_KERNEL);
        KUNIT_ASSERT_NOT_ERR_OR_NULL(test, ctx);

        ctx->pdrv.probe = kunit_platform_driver_probe;
        ctx->pdrv.driver.name = "kunit-platform";
        ctx->pdrv.driver.owner = THIS_MODULE;

        KUNIT_EXPECT_EQ(test, 0, kunit_platform_driver_register(test, &ctx->pdrv));
        <... wait for driver to probe ...>
        KUNIT_EXPECT_STREQ(test, ctx->data, "test data");
}
```

**Return**

0 on success, negative errno on failure.
