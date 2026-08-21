---
collection: kernel
version: "6.8"
title: "HW consumer"
source_url: https://www.kernel.org/doc/html/v6.8/driver-api/iio/hw-consumer.html
fetched_at: 2026-08-21T03:31:42+00:00
---
# HW consumer

An IIO device can be directly connected to another device in hardware. In this
case the buffers between IIO provider and IIO consumer are handled by hardware.
The Industrial I/O HW consumer offers a way to bond these IIO devices without
software buffer for data. The implementation can be found under
`drivers/iio/buffer/hw-consumer.c`

- struct iio_hw_consumer — Hardware consumer structure
- [`iio_hw_consumer_alloc()`](hw-consumer.md#c.iio_hw_consumer_alloc "iio_hw_consumer_alloc") — Allocate IIO hardware consumer
- [`iio_hw_consumer_free()`](hw-consumer.md#c.iio_hw_consumer_free "iio_hw_consumer_free") — Free IIO hardware consumer
- [`iio_hw_consumer_enable()`](hw-consumer.md#c.iio_hw_consumer_enable "iio_hw_consumer_enable") — Enable IIO hardware consumer
- [`iio_hw_consumer_disable()`](hw-consumer.md#c.iio_hw_consumer_disable "iio_hw_consumer_disable") — Disable IIO hardware consumer

## HW consumer setup

As standard IIO device the implementation is based on IIO provider/consumer.
A typical IIO HW consumer setup looks like this:

```
static struct iio_hw_consumer *hwc;

static const struct iio_info adc_info = {
        .read_raw = adc_read_raw,
};

static int adc_read_raw(struct iio_dev *indio_dev,
                        struct iio_chan_spec const *chan, int *val,
                        int *val2, long mask)
{
        ret = iio_hw_consumer_enable(hwc);

        /* Acquire data */

        ret = iio_hw_consumer_disable(hwc);
}

static int adc_probe(struct platform_device *pdev)
{
        hwc = devm_iio_hw_consumer_alloc(&iio->dev);
}
```

## More details

struct iio_hw_consumer \*iio_hw_consumer_alloc(struct [device](../infrastructure.md#c.device "device") \*dev)
:   Allocate IIO hardware consumer

**Parameters**

`struct device *dev`
:   Pointer to consumer device.

**Description**

Returns a valid iio_hw_consumer on success or a [`ERR_PTR()`](../../core-api/kernel-api.md#c.ERR_PTR "ERR_PTR") on failure.

void iio_hw_consumer_free(struct iio_hw_consumer \*hwc)
:   Free IIO hardware consumer

**Parameters**

`struct iio_hw_consumer *hwc`
:   hw consumer to free.

struct iio_hw_consumer \*devm_iio_hw_consumer_alloc(struct [device](../infrastructure.md#c.device "device") \*dev)
:   Resource-managed [`iio_hw_consumer_alloc()`](hw-consumer.md#c.iio_hw_consumer_alloc "iio_hw_consumer_alloc")

**Parameters**

`struct device *dev`
:   Pointer to consumer device.

**Description**

Managed iio_hw_consumer_alloc. iio_hw_consumer allocated with this function
is automatically freed on driver detach.

returns pointer to allocated iio_hw_consumer on success, NULL on failure.

int iio_hw_consumer_enable(struct iio_hw_consumer \*hwc)
:   Enable IIO hardware consumer

**Parameters**

`struct iio_hw_consumer *hwc`
:   iio_hw_consumer to enable.

**Description**

Returns 0 on success.

void iio_hw_consumer_disable(struct iio_hw_consumer \*hwc)
:   Disable IIO hardware consumer

**Parameters**

`struct iio_hw_consumer *hwc`
:   iio_hw_consumer to disable.
