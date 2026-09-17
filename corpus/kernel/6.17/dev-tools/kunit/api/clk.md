---
collection: kernel
version: "6.17"
title: "Clk API"
source_url: https://www.kernel.org/doc/html/v6.17/dev-tools/kunit/api/clk.html
fetched_at: 2026-09-16T16:27:30+00:00
---
# Clk API

The KUnit clk API is used to test clk providers and clk consumers.

int clk_prepare_enable_kunit(struct [kunit](test.md#c.kunit "kunit") \*test, struct [clk](clk.md#c.clk_prepare_enable_kunit "clk") \*clk)
:   Test managed `clk_prepare_enable()`

**Parameters**

`struct kunit *test`
:   The test context

`struct clk *clk`
:   clk to prepare and enable

**Return**

0 on success, or negative errno on failure.

struct clk \*clk_get_kunit(struct [kunit](test.md#c.kunit "kunit") \*test, struct [device](../../../driver-api/infrastructure.md#c.device "device") \*dev, const char \*con_id)
:   Test managed [`clk_get()`](../../../core-api/kernel-api.md#c.clk_get "clk_get")

**Parameters**

`struct kunit *test`
:   The test context

`struct device *dev`
:   device for clock “consumer”

`const char *con_id`
:   clock consumer ID

**Description**

Just like [`clk_get()`](../../../core-api/kernel-api.md#c.clk_get "clk_get"), except the clk is managed by the test case and is
automatically put with [`clk_put()`](../../../core-api/kernel-api.md#c.clk_put "clk_put") after the test case concludes.

**Return**

new clk consumer or ERR_PTR on failure.

struct clk \*of_clk_get_kunit(struct [kunit](test.md#c.kunit "kunit") \*test, struct device_node \*np, int index)
:   Test managed `of_clk_get()`

**Parameters**

`struct kunit *test`
:   The test context

`struct device_node *np`
:   device_node for clock “consumer”

`int index`
:   index in ‘clocks’ property of **np**

**Description**

Just like `of_clk_get()`, except the clk is managed by the test case and is
automatically put with [`clk_put()`](../../../core-api/kernel-api.md#c.clk_put "clk_put") after the test case concludes.

**Return**

new clk consumer or ERR_PTR on failure.

struct clk \*clk_hw_get_clk_kunit(struct [kunit](test.md#c.kunit "kunit") \*test, struct clk_hw \*hw, const char \*con_id)
:   Test managed `clk_hw_get_clk()`

**Parameters**

`struct kunit *test`
:   The test context

`struct clk_hw *hw`
:   clk_hw associated with the clk being consumed

`const char *con_id`
:   connection ID string on device

**Description**

Just like `clk_hw_get_clk()`, except the clk is managed by the test case and
is automatically put with [`clk_put()`](../../../core-api/kernel-api.md#c.clk_put "clk_put") after the test case concludes.

**Return**

new clk consumer or ERR_PTR on failure.

struct clk \*clk_hw_get_clk_prepared_enabled_kunit(struct [kunit](test.md#c.kunit "kunit") \*test, struct clk_hw \*hw, const char \*con_id)
:   Test managed `clk_hw_get_clk()` + `clk_prepare_enable()`

**Parameters**

`struct kunit *test`
:   The test context

`struct clk_hw *hw`
:   clk_hw associated with the clk being consumed

`const char *con_id`
:   connection ID string on device

**Description**

Just like

```c
struct clk *clk = clk_hw_get_clk(...);
clk_prepare_enable(clk);
```

except the clk is managed by the test case and is automatically disabled and
unprepared with `clk_disable_unprepare()` and put with [`clk_put()`](../../../core-api/kernel-api.md#c.clk_put "clk_put") after the
test case concludes.

**Return**

new clk consumer that is prepared and enabled or ERR_PTR on failure.

int clk_hw_register_kunit(struct [kunit](test.md#c.kunit "kunit") \*test, struct [device](../../../driver-api/infrastructure.md#c.device "device") \*dev, struct clk_hw \*hw)
:   Test managed `clk_hw_register()`

**Parameters**

`struct kunit *test`
:   The test context

`struct device *dev`
:   device that is registering this clock

`struct clk_hw *hw`
:   link to hardware-specific clock data

**Description**

Just like `clk_hw_register()`, except the clk registration is managed by the
test case and is automatically unregistered after the test case concludes.

**Return**

0 on success or a negative errno value on failure.

int of_clk_hw_register_kunit(struct [kunit](test.md#c.kunit "kunit") \*test, struct device_node \*node, struct clk_hw \*hw)
:   Test managed `of_clk_hw_register()`

**Parameters**

`struct kunit *test`
:   The test context

`struct device_node *node`
:   device_node of device that is registering this clock

`struct clk_hw *hw`
:   link to hardware-specific clock data

**Description**

Just like `of_clk_hw_register()`, except the clk registration is managed by
the test case and is automatically unregistered after the test case
concludes.

**Return**

0 on success or a negative errno value on failure.

int of_clk_add_hw_provider_kunit(struct [kunit](test.md#c.kunit "kunit") \*test, struct device_node \*np, struct clk_hw \*(\*get)(struct of_phandle_args \*clkspec, void \*data), void \*data)
:   Test managed `of_clk_add_hw_provider()`

**Parameters**

`struct kunit *test`
:   The test context

`struct device_node *np`
:   Device node pointer associated with clock provider

`struct clk_hw *(*get)(struct of_phandle_args *clkspec, void *data)`
:   Callback for decoding clk_hw

`void *data`
:   Context pointer for **get** callback.

**Description**

Just like `of_clk_add_hw_provider()`, except the clk_hw provider is managed by
the test case and is automatically unregistered after the test case
concludes.

**Return**

0 on success or a negative errno value on failure.
