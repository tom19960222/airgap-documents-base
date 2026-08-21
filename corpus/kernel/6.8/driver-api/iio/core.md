---
collection: kernel
version: "6.8"
title: "Core elements"
source_url: https://www.kernel.org/doc/html/v6.8/driver-api/iio/core.html
fetched_at: 2026-08-21T03:31:40+00:00
---
# Core elements

The Industrial I/O core offers both a unified framework for writing drivers for
many different types of embedded sensors and a standard interface to user space
applications manipulating sensors. The implementation can be found under
`drivers/iio/industrialio-*`

## Industrial I/O Devices

- [`struct iio_dev`](core.md#c.iio_dev "iio_dev") - industrial I/O device
- [`iio_device_alloc()`](core.md#c.iio_device_alloc "iio_device_alloc") - allocate an [`iio_dev`](core.md#c.iio_dev "iio_dev") from a driver
- [`iio_device_free()`](core.md#c.iio_device_free "iio_device_free") - free an [`iio_dev`](core.md#c.iio_dev "iio_dev") from a driver
- [`iio_device_register()`](core.md#c.iio_device_register "iio_device_register") - register a device with the IIO subsystem
- [`iio_device_unregister()`](core.md#c.iio_device_unregister "iio_device_unregister") - unregister a device from the IIO
  subsystem

An IIO device usually corresponds to a single hardware sensor and it
provides all the information needed by a driver handling a device.
Let's first have a look at the functionality embedded in an IIO device
then we will show how a device driver makes use of an IIO device.

There are two ways for a user space application to interact with an IIO driver.

1. `/sys/bus/iio/iio:deviceX/`, this represents a hardware sensor
   and groups together the data channels of the same chip.
2. `/dev/iio:deviceX`, character device node interface used for
   buffered data transfer and for events information retrieval.

A typical IIO driver will register itself as an [I2C](../i2c.md) or
[SPI](../spi.md) driver and will create two routines, probe and remove.

At probe:

1. Call [`iio_device_alloc()`](core.md#c.iio_device_alloc "iio_device_alloc"), which allocates memory for an IIO device.
2. Initialize IIO device fields with driver specific information (e.g.
   device name, device channels).
3. Call [`iio_device_register()`](core.md#c.iio_device_register "iio_device_register"), this registers the device with the
   IIO core. After this call the device is ready to accept requests from user
   space applications.

At remove, we free the resources allocated in probe in reverse order:

1. [`iio_device_unregister()`](core.md#c.iio_device_unregister "iio_device_unregister"), unregister the device from the IIO core.
2. [`iio_device_free()`](core.md#c.iio_device_free "iio_device_free"), free the memory allocated for the IIO device.

### IIO device sysfs interface

Attributes are sysfs files used to expose chip info and also allowing
applications to set various configuration parameters. For device with
index X, attributes can be found under /sys/bus/iio/iio:deviceX/ directory.
Common attributes are:

- `name`, description of the physical chip.
- `dev`, shows the major:minor pair associated with
  `/dev/iio:deviceX` node.
- `sampling_frequency_available`, available discrete set of sampling
  frequency values for device.
- Available standard attributes for IIO devices are described in the
  `Documentation/ABI/testing/sysfs-bus-iio` file in the Linux kernel
  sources.

### IIO device channels

[`struct iio_chan_spec`](core.md#c.iio_chan_spec "iio_chan_spec") - specification of a single channel

An IIO device channel is a representation of a data channel. An IIO device can
have one or multiple channels. For example:

- a thermometer sensor has one channel representing the temperature measurement.
- a light sensor with two channels indicating the measurements in the visible
  and infrared spectrum.
- an accelerometer can have up to 3 channels representing acceleration on X, Y
  and Z axes.

An IIO channel is described by the [`struct iio_chan_spec`](core.md#c.iio_chan_spec "iio_chan_spec").
A thermometer driver for the temperature sensor in the example above would
have to describe its channel as follows:

```
static const struct iio_chan_spec temp_channel[] = {
     {
         .type = IIO_TEMP,
         .info_mask_separate = BIT(IIO_CHAN_INFO_PROCESSED),
     },
};
```

Channel sysfs attributes exposed to userspace are specified in the form of
bitmasks. Depending on their shared info, attributes can be set in one of the
following masks:

- **info_mask_separate**, attributes will be specific to
  this channel
- **info_mask_shared_by_type**, attributes are shared by all channels of the
  same type
- **info_mask_shared_by_dir**, attributes are shared by all channels of the same
  direction
- **info_mask_shared_by_all**, attributes are shared by all channels

When there are multiple data channels per channel type we have two ways to
distinguish between them:

- set **.modified** field of [`iio_chan_spec`](core.md#c.iio_chan_spec "iio_chan_spec") to 1. Modifiers are
  specified using **.channel2** field of the same [`iio_chan_spec`](core.md#c.iio_chan_spec "iio_chan_spec")
  structure and are used to indicate a physically unique characteristic of the
  channel such as its direction or spectral response. For example, a light
  sensor can have two channels, one for infrared light and one for both
  infrared and visible light.
- set **.indexed** field of [`iio_chan_spec`](core.md#c.iio_chan_spec "iio_chan_spec") to 1. In this case the
  channel is simply another instance with an index specified by the **.channel**
  field.

Here is how we can make use of the channel's modifiers:

```
static const struct iio_chan_spec light_channels[] = {
        {
                .type = IIO_INTENSITY,
                .modified = 1,
                .channel2 = IIO_MOD_LIGHT_IR,
                .info_mask_separate = BIT(IIO_CHAN_INFO_RAW),
                .info_mask_shared = BIT(IIO_CHAN_INFO_SAMP_FREQ),
        },
        {
                .type = IIO_INTENSITY,
                .modified = 1,
                .channel2 = IIO_MOD_LIGHT_BOTH,
                .info_mask_separate = BIT(IIO_CHAN_INFO_RAW),
                .info_mask_shared = BIT(IIO_CHAN_INFO_SAMP_FREQ),
        },
        {
                .type = IIO_LIGHT,
                .info_mask_separate = BIT(IIO_CHAN_INFO_PROCESSED),
                .info_mask_shared = BIT(IIO_CHAN_INFO_SAMP_FREQ),
        },
   }
```

This channel's definition will generate two separate sysfs files for raw data
retrieval:

- `/sys/bus/iio/iio:deviceX/in_intensity_ir_raw`
- `/sys/bus/iio/iio:deviceX/in_intensity_both_raw`

one file for processed data:

- `/sys/bus/iio/iio:deviceX/in_illuminance_input`

and one shared sysfs file for sampling frequency:

- `/sys/bus/iio/iio:deviceX/sampling_frequency`.

Here is how we can make use of the channel's indexing:

```
static const struct iio_chan_spec light_channels[] = {
        {
                .type = IIO_VOLTAGE,
                .indexed = 1,
                .channel = 0,
                .info_mask_separate = BIT(IIO_CHAN_INFO_RAW),
        },
        {
                .type = IIO_VOLTAGE,
                .indexed = 1,
                .channel = 1,
                .info_mask_separate = BIT(IIO_CHAN_INFO_RAW),
        },
}
```

This will generate two separate attributes files for raw data retrieval:

- `/sys/bus/iio/devices/iio:deviceX/in_voltage0_raw`, representing
  voltage measurement for channel 0.
- `/sys/bus/iio/devices/iio:deviceX/in_voltage1_raw`, representing
  voltage measurement for channel 1.

### More details

struct iio_chan_spec_ext_info
:   Extended channel info attribute

**Definition**:

```
struct iio_chan_spec_ext_info {
    const char *name;
    enum iio_shared_by shared;
    ssize_t (*read)(struct iio_dev *, uintptr_t private, struct iio_chan_spec const *, char *buf);
    ssize_t (*write)(struct iio_dev *, uintptr_t private,struct iio_chan_spec const *, const char *buf, size_t len);
    uintptr_t private;
};
```

**Members**

`name`
:   Info attribute name

`shared`
:   Whether this attribute is shared between all channels.

`read`
:   Read callback for this info attribute, may be NULL.

`write`
:   Write callback for this info attribute, may be NULL.

`private`
:   Data private to the driver.

struct iio_enum
:   Enum channel info attribute

**Definition**:

```
struct iio_enum {
    const char * const *items;
    unsigned int num_items;
    int (*set)(struct iio_dev *, const struct iio_chan_spec *, unsigned int);
    int (*get)(struct iio_dev *, const struct iio_chan_spec *);
};
```

**Members**

`items`
:   An array of strings.

`num_items`
:   Length of the item array.

`set`
:   Set callback function, may be NULL.

`get`
:   Get callback function, may be NULL.

**Description**

The iio_enum struct can be used to implement enum style channel attributes.
Enum style attributes are those which have a set of strings which map to
unsigned integer values. The IIO enum helper code takes care of mapping
between value and string as well as generating a "_available" file which
contains a list of all available items. The set callback will be called when
the attribute is updated. The last parameter is the index to the newly
activated item. The get callback will be used to query the currently active
item and is supposed to return the index for it.

IIO_ENUM

`IIO_ENUM (_name, _shared, _e)`

> Initialize enum extended channel attribute

**Parameters**

`_name`
:   Attribute name

`_shared`
:   Whether the attribute is shared between all channels

`_e`
:   Pointer to an iio_enum struct

**Description**

This should usually be used together with [`IIO_ENUM_AVAILABLE()`](core.md#c.IIO_ENUM_AVAILABLE "IIO_ENUM_AVAILABLE")

IIO_ENUM_AVAILABLE

`IIO_ENUM_AVAILABLE (_name, _shared, _e)`

> Initialize enum available extended channel attribute

**Parameters**

`_name`
:   Attribute name ("_available" will be appended to the name)

`_shared`
:   Whether the attribute is shared between all channels

`_e`
:   Pointer to an iio_enum struct

**Description**

Creates a read only attribute which lists all the available enum items in a
space separated list. This should usually be used together with [`IIO_ENUM()`](core.md#c.IIO_ENUM "IIO_ENUM")

struct iio_mount_matrix
:   iio mounting matrix

**Definition**:

```
struct iio_mount_matrix {
    const char *rotation[9];
};
```

**Members**

`rotation`
:   3 dimensional space rotation matrix defining sensor alignment with
    main hardware

IIO_MOUNT_MATRIX

`IIO_MOUNT_MATRIX (_shared, _get)`

> Initialize mount matrix extended channel attribute

**Parameters**

`_shared`
:   Whether the attribute is shared between all channels

`_get`
:   Pointer to an iio_get_mount_matrix_t accessor

struct iio_event_spec
:   specification for a channel event

**Definition**:

```
struct iio_event_spec {
    enum iio_event_type type;
    enum iio_event_direction dir;
    unsigned long mask_separate;
    unsigned long mask_shared_by_type;
    unsigned long mask_shared_by_dir;
    unsigned long mask_shared_by_all;
};
```

**Members**

`type`
:   Type of the event

`dir`
:   Direction of the event

`mask_separate`
:   Bit mask of enum iio_event_info values. Attributes
    set in this mask will be registered per channel.

`mask_shared_by_type`
:   Bit mask of enum iio_event_info values. Attributes
    set in this mask will be shared by channel type.

`mask_shared_by_dir`
:   Bit mask of enum iio_event_info values. Attributes
    set in this mask will be shared by channel type and
    direction.

`mask_shared_by_all`
:   Bit mask of enum iio_event_info values. Attributes
    set in this mask will be shared by all channels.

struct iio_chan_spec
:   specification of a single channel

**Definition**:

```
struct iio_chan_spec {
    enum iio_chan_type      type;
    int channel;
    int channel2;
    unsigned long           address;
    int scan_index;
    struct {
        char sign;
        u8 realbits;
        u8 storagebits;
        u8 shift;
        u8 repeat;
        enum iio_endian endianness;
    } scan_type;
    long info_mask_separate;
    long info_mask_separate_available;
    long info_mask_shared_by_type;
    long info_mask_shared_by_type_available;
    long info_mask_shared_by_dir;
    long info_mask_shared_by_dir_available;
    long info_mask_shared_by_all;
    long info_mask_shared_by_all_available;
    const struct iio_event_spec *event_spec;
    unsigned int            num_event_specs;
    const struct iio_chan_spec_ext_info *ext_info;
    const char              *extend_name;
    const char              *datasheet_name;
    unsigned modified:1;
    unsigned indexed:1;
    unsigned output:1;
    unsigned differential:1;
};
```

**Members**

`type`
:   What type of measurement is the channel making.

`channel`
:   What number do we wish to assign the channel.

`channel2`
:   If there is a second number for a differential
    channel then this is it. If modified is set then the
    value here specifies the modifier.

`address`
:   Driver specific identifier.

`scan_index`
:   Monotonic index to give ordering in scans when read
    from a buffer.

`scan_type`
:   struct describing the scan type

`scan_type.sign`
:   's' or 'u' to specify signed or unsigned

`scan_type.realbits`
:   Number of valid bits of data

`scan_type.storagebits`
:   Realbits + padding

`scan_type.shift`
:   Shift right by this before masking out
    realbits.

`scan_type.repeat`
:   Number of times real/storage bits repeats.
    When the repeat element is more than 1, then
    the type element in sysfs will show a repeat
    value. Otherwise, the number of repetitions
    is omitted.

`scan_type.endianness`
:   little or big endian

`info_mask_separate`
:   What information is to be exported that is specific to
    this channel.

`info_mask_separate_available`
:   What availability information is to be
    exported that is specific to this channel.

`info_mask_shared_by_type`
:   What information is to be exported that is shared
    by all channels of the same type.

`info_mask_shared_by_type_available`
:   What availability information is to be
    exported that is shared by all channels of the same
    type.

`info_mask_shared_by_dir`
:   What information is to be exported that is shared
    by all channels of the same direction.

`info_mask_shared_by_dir_available`
:   What availability information is to be
    exported that is shared by all channels of the same
    direction.

`info_mask_shared_by_all`
:   What information is to be exported that is shared
    by all channels.

`info_mask_shared_by_all_available`
:   What availability information is to be
    exported that is shared by all channels.

`event_spec`
:   Array of events which should be registered for this
    channel.

`num_event_specs`
:   Size of the event_spec array.

`ext_info`
:   Array of extended info attributes for this channel.
    The array is NULL terminated, the last element should
    have its name field set to NULL.

`extend_name`
:   Allows labeling of channel attributes with an
    informative name. Note this has no effect codes etc,
    unlike modifiers.
    This field is deprecated in favour of providing
    iio_info->read_label() to override the label, which
    unlike **extend_name** does not affect sysfs filenames.

`datasheet_name`
:   A name used in in-kernel mapping of channels. It should
    correspond to the first name that the channel is referred
    to by in the datasheet (e.g. IND), or the nearest
    possible compound name (e.g. IND-INC).

`modified`
:   Does a modifier apply to this channel. What these are
    depends on the channel type. Modifier is set in
    channel2. Examples are IIO_MOD_X for axial sensors about
    the 'x' axis.

`indexed`
:   Specify the channel has a numerical index. If not,
    the channel index number will be suppressed for sysfs
    attributes but not for event codes.

`output`
:   Channel is output.

`differential`
:   Channel is differential.

bool iio_channel_has_info(const struct [iio_chan_spec](core.md#c.iio_chan_spec "iio_chan_spec") \*chan, enum iio_chan_info_enum type)
:   Checks whether a channel supports a info attribute

**Parameters**

`const struct iio_chan_spec *chan`
:   The channel to be queried

`enum iio_chan_info_enum type`
:   Type of the info attribute to be checked

**Description**

Returns true if the channels supports reporting values for the given info
attribute type, false otherwise.

bool iio_channel_has_available(const struct [iio_chan_spec](core.md#c.iio_chan_spec "iio_chan_spec") \*chan, enum iio_chan_info_enum type)
:   Checks if a channel has an available attribute

**Parameters**

`const struct iio_chan_spec *chan`
:   The channel to be queried

`enum iio_chan_info_enum type`
:   Type of the available attribute to be checked

**Description**

Returns true if the channel supports reporting available values for the
given attribute type, false otherwise.

struct iio_info
:   constant information about device

**Definition**:

```
struct iio_info {
    const struct attribute_group    *event_attrs;
    const struct attribute_group    *attrs;
    int (*read_raw)(struct iio_dev *indio_dev,struct iio_chan_spec const *chan,int *val,int *val2, long mask);
    int (*read_raw_multi)(struct iio_dev *indio_dev,struct iio_chan_spec const *chan,int max_len,int *vals,int *val_len, long mask);
    int (*read_avail)(struct iio_dev *indio_dev,struct iio_chan_spec const *chan,const int **vals,int *type,int *length, long mask);
    int (*write_raw)(struct iio_dev *indio_dev,struct iio_chan_spec const *chan,int val,int val2, long mask);
    int (*read_label)(struct iio_dev *indio_dev,struct iio_chan_spec const *chan, char *label);
    int (*write_raw_get_fmt)(struct iio_dev *indio_dev,struct iio_chan_spec const *chan, long mask);
    int (*read_event_config)(struct iio_dev *indio_dev,const struct iio_chan_spec *chan,enum iio_event_type type, enum iio_event_direction dir);
    int (*write_event_config)(struct iio_dev *indio_dev,const struct iio_chan_spec *chan,enum iio_event_type type,enum iio_event_direction dir, int state);
    int (*read_event_value)(struct iio_dev *indio_dev,const struct iio_chan_spec *chan,enum iio_event_type type,enum iio_event_direction dir, enum iio_event_info info, int *val, int *val2);
    int (*write_event_value)(struct iio_dev *indio_dev,const struct iio_chan_spec *chan,enum iio_event_type type,enum iio_event_direction dir, enum iio_event_info info, int val, int val2);
    int (*read_event_label)(struct iio_dev *indio_dev,struct iio_chan_spec const *chan,enum iio_event_type type,enum iio_event_direction dir, char *label);
    int (*validate_trigger)(struct iio_dev *indio_dev, struct iio_trigger *trig);
    int (*update_scan_mode)(struct iio_dev *indio_dev, const unsigned long *scan_mask);
    int (*debugfs_reg_access)(struct iio_dev *indio_dev,unsigned reg, unsigned writeval, unsigned *readval);
    int (*fwnode_xlate)(struct iio_dev *indio_dev, const struct fwnode_reference_args *iiospec);
    int (*hwfifo_set_watermark)(struct iio_dev *indio_dev, unsigned val);
    int (*hwfifo_flush_to_buffer)(struct iio_dev *indio_dev, unsigned count);
};
```

**Members**

`event_attrs`
:   event control attributes

`attrs`
:   general purpose device attributes

`read_raw`
:   function to request a value from the device.
    mask specifies which value. Note 0 means a reading of
    the channel in question. Return value will specify the
    type of value returned by the device. val and val2 will
    contain the elements making up the returned value.

`read_raw_multi`
:   function to return values from the device.
    mask specifies which value. Note 0 means a reading of
    the channel in question. Return value will specify the
    type of value returned by the device. vals pointer
    contain the elements making up the returned value.
    max_len specifies maximum number of elements
    vals pointer can contain. val_len is used to return
    length of valid elements in vals.

`read_avail`
:   function to return the available values from the device.
    mask specifies which value. Note 0 means the available
    values for the channel in question. Return value
    specifies if a IIO_AVAIL_LIST or a IIO_AVAIL_RANGE is
    returned in vals. The type of the vals are returned in
    type and the number of vals is returned in length. For
    ranges, there are always three vals returned; min, step
    and max. For lists, all possible values are enumerated.

`write_raw`
:   function to write a value to the device.
    Parameters are the same as for read_raw.

`read_label`
:   function to request label name for a specified label,
    for better channel identification.

`write_raw_get_fmt`
:   callback function to query the expected
    format/precision. If not set by the driver, write_raw
    returns IIO_VAL_INT_PLUS_MICRO.

`read_event_config`
:   find out if the event is enabled.

`write_event_config`
:   set if the event is enabled.

`read_event_value`
:   read a configuration value associated with the event.

`write_event_value`
:   write a configuration value for the event.

`read_event_label`
:   function to request label name for a specified label,
    for better event identification.

`validate_trigger`
:   function to validate the trigger when the
    current trigger gets changed.

`update_scan_mode`
:   function to configure device and scan buffer when
    channels have changed

`debugfs_reg_access`
:   function to read or write register value of device

`fwnode_xlate`
:   fwnode based function pointer to obtain channel specifier index.

`hwfifo_set_watermark`
:   function pointer to set the current hardware
    fifo watermark level; see hwfifo_\* entries in
    Documentation/ABI/testing/sysfs-bus-iio for details on
    how the hardware fifo operates

`hwfifo_flush_to_buffer`
:   function pointer to flush the samples stored
    in the hardware fifo to the device buffer. The driver
    should not flush more than count samples. The function
    must return the number of samples flushed, 0 if no
    samples were flushed or a negative integer if no samples
    were flushed and there was an error.

struct iio_buffer_setup_ops
:   buffer setup related callbacks

**Definition**:

```
struct iio_buffer_setup_ops {
    int (*preenable)(struct iio_dev *);
    int (*postenable)(struct iio_dev *);
    int (*predisable)(struct iio_dev *);
    int (*postdisable)(struct iio_dev *);
    bool (*validate_scan_mask)(struct iio_dev *indio_dev, const unsigned long *scan_mask);
};
```

**Members**

`preenable`
:   [DRIVER] function to run prior to marking buffer enabled

`postenable`
:   [DRIVER] function to run after marking buffer enabled

`predisable`
:   [DRIVER] function to run prior to marking buffer
    disabled

`postdisable`
:   [DRIVER] function to run after marking buffer disabled

`validate_scan_mask`
:   [DRIVER] function callback to check whether a given
    scan mask is valid for the device.

struct iio_dev
:   industrial I/O device

**Definition**:

```
struct iio_dev {
    int modes;
    struct device                   dev;
    struct iio_buffer               *buffer;
    int scan_bytes;
    const unsigned long             *available_scan_masks;
    unsigned masklength;
    const unsigned long             *active_scan_mask;
    bool scan_timestamp;
    struct iio_trigger              *trig;
    struct iio_poll_func            *pollfunc;
    struct iio_poll_func            *pollfunc_event;
    struct iio_chan_spec const      *channels;
    int num_channels;
    const char                      *name;
    const char                      *label;
    const struct iio_info           *info;
    const struct iio_buffer_setup_ops       *setup_ops;
    void *priv;
};
```

**Members**

`modes`
:   [DRIVER] bitmask listing all the operating modes
    supported by the IIO device. This list should be
    initialized before registering the IIO device. It can
    also be filed up by the IIO core, as a result of
    enabling particular features in the driver
    (see iio_triggered_event_setup()).

`dev`
:   [DRIVER] device structure, should be assigned a parent
    and owner

`buffer`
:   [DRIVER] any buffer present

`scan_bytes`
:   [INTERN] num bytes captured to be fed to buffer demux

`available_scan_masks`
:   [DRIVER] optional array of allowed bitmasks. Sort the
    array in order of preference, the most preferred
    masks first.

`masklength`
:   [INTERN] the length of the mask established from
    channels

`active_scan_mask`
:   [INTERN] union of all scan masks requested by buffers

`scan_timestamp`
:   [INTERN] set if any buffers have requested timestamp

`trig`
:   [INTERN] current device trigger (buffer modes)

`pollfunc`
:   [DRIVER] function run on trigger being received

`pollfunc_event`
:   [DRIVER] function run on events trigger being received

`channels`
:   [DRIVER] channel specification structure table

`num_channels`
:   [DRIVER] number of channels specified in **channels**.

`name`
:   [DRIVER] name of the device.

`label`
:   [DRIVER] unique name to identify which device this is

`info`
:   [DRIVER] callbacks and constant info from driver

`setup_ops`
:   [DRIVER] callbacks to call before and after buffer
    enable/disable

`priv`
:   [DRIVER] reference to driver's private information
    **MUST** be accessed **ONLY** via iio_priv() helper

iio_device_register

`iio_device_register (indio_dev)`

> register a device with the IIO subsystem

**Parameters**

`indio_dev`
:   Device structure filled by the device driver

devm_iio_device_register

`devm_iio_device_register (dev, indio_dev)`

> Resource-managed [`iio_device_register()`](core.md#c.iio_device_register "iio_device_register")

**Parameters**

`dev`
:   Device to allocate iio_dev for

`indio_dev`
:   Device structure filled by the device driver

**Description**

Managed iio_device_register. The IIO device registered with this
function is automatically unregistered on driver detach. This function
calls [`iio_device_register()`](core.md#c.iio_device_register "iio_device_register") internally. Refer to that function for more
information.

**Return**

0 on success, negative error number on failure.

void iio_device_put(struct [iio_dev](core.md#c.iio_dev "iio_dev") \*indio_dev)
:   reference counted deallocation of [`struct device`](../infrastructure.md#c.device "device")

**Parameters**

`struct iio_dev *indio_dev`
:   IIO device structure containing the device

struct [iio_dev](core.md#c.iio_dev "iio_dev") \*dev_to_iio_dev(struct [device](../infrastructure.md#c.device "device") \*dev)
:   Get IIO device struct from a device struct

**Parameters**

`struct device *dev`
:   The device embedded in the IIO device

**Note**

The device must be a IIO device, otherwise the result is undefined.

struct [iio_dev](core.md#c.iio_dev "iio_dev") \*iio_device_get(struct [iio_dev](core.md#c.iio_dev "iio_dev") \*indio_dev)
:   increment reference count for the device

**Parameters**

`struct iio_dev *indio_dev`
:   IIO device structure

**Return**

The passed IIO device

void iio_device_set_parent(struct [iio_dev](core.md#c.iio_dev "iio_dev") \*indio_dev, struct [device](../infrastructure.md#c.device "device") \*parent)
:   assign parent device to the IIO device object

**Parameters**

`struct iio_dev *indio_dev`
:   IIO device structure

`struct device *parent`
:   reference to parent device object

**Description**

This utility must be called between IIO device allocation
(via [`devm_iio_device_alloc()`](core.md#c.devm_iio_device_alloc "devm_iio_device_alloc")) & IIO device registration
(via [`iio_device_register()`](core.md#c.iio_device_register "iio_device_register") and [`devm_iio_device_register()`](core.md#c.devm_iio_device_register "devm_iio_device_register"))).
By default, the device allocation will also assign a parent device to
the IIO device object. In cases where [`devm_iio_device_alloc()`](core.md#c.devm_iio_device_alloc "devm_iio_device_alloc") is used,
sometimes the parent device must be different than the device used to
manage the allocation.
In that case, this helper should be used to change the parent, hence the
requirement to call this between allocation & registration.

void iio_device_set_drvdata(struct [iio_dev](core.md#c.iio_dev "iio_dev") \*indio_dev, void \*data)
:   Set device driver data

**Parameters**

`struct iio_dev *indio_dev`
:   IIO device structure

`void *data`
:   Driver specific data

**Description**

Allows to attach an arbitrary pointer to an IIO device, which can later be
retrieved by [`iio_device_get_drvdata()`](core.md#c.iio_device_get_drvdata "iio_device_get_drvdata").

void \*iio_device_get_drvdata(const struct [iio_dev](core.md#c.iio_dev "iio_dev") \*indio_dev)
:   Get device driver data

**Parameters**

`const struct iio_dev *indio_dev`
:   IIO device structure

**Description**

Returns the data previously set with [`iio_device_set_drvdata()`](core.md#c.iio_device_set_drvdata "iio_device_set_drvdata")

struct dentry \*iio_get_debugfs_dentry(struct [iio_dev](core.md#c.iio_dev "iio_dev") \*indio_dev)
:   helper function to get the debugfs_dentry

**Parameters**

`struct iio_dev *indio_dev`
:   IIO device structure for device

IIO_DEGREE_TO_RAD

`IIO_DEGREE_TO_RAD (deg)`

> Convert degree to rad

**Parameters**

`deg`
:   A value in degree

**Description**

Returns the given value converted from degree to rad

IIO_RAD_TO_DEGREE

`IIO_RAD_TO_DEGREE (rad)`

> Convert rad to degree

**Parameters**

`rad`
:   A value in rad

**Description**

Returns the given value converted from rad to degree

IIO_G_TO_M_S_2

`IIO_G_TO_M_S_2 (g)`

> Convert g to meter / second\*\*2

**Parameters**

`g`
:   A value in g

**Description**

Returns the given value converted from g to meter / second\*\*2

IIO_M_S_2_TO_G

`IIO_M_S_2_TO_G (ms2)`

> Convert meter / second\*\*2 to g

**Parameters**

`ms2`
:   A value in meter / second\*\*2

**Description**

Returns the given value converted from meter / second\*\*2 to g

int iio_device_id(struct [iio_dev](core.md#c.iio_dev "iio_dev") \*indio_dev)
:   query the unique ID for the device

**Parameters**

`struct iio_dev *indio_dev`
:   Device structure whose ID is being queried

**Description**

The IIO device ID is a unique index used for example for the naming
of the character device /dev/iio:device[ID].

**Return**

Unique ID for the device.

bool iio_buffer_enabled(struct [iio_dev](core.md#c.iio_dev "iio_dev") \*indio_dev)
:   helper function to test if the buffer is enabled

**Parameters**

`struct iio_dev *indio_dev`
:   IIO device structure for device

**Return**

True, if the buffer is enabled.

int iio_device_set_clock(struct [iio_dev](core.md#c.iio_dev "iio_dev") \*indio_dev, clockid_t clock_id)
:   Set current timestamping clock for the device

**Parameters**

`struct iio_dev *indio_dev`
:   IIO device structure containing the device

`clockid_t clock_id`
:   timestamping clock POSIX identifier to set.

**Return**

0 on success, or a negative error code.

clockid_t iio_device_get_clock(const struct [iio_dev](core.md#c.iio_dev "iio_dev") \*indio_dev)
:   Retrieve current timestamping clock for the device

**Parameters**

`const struct iio_dev *indio_dev`
:   IIO device structure containing the device

**Return**

Clock ID of the current timestamping clock for the device.

s64 iio_get_time_ns(const struct [iio_dev](core.md#c.iio_dev "iio_dev") \*indio_dev)
:   utility function to get a time stamp for events etc

**Parameters**

`const struct iio_dev *indio_dev`
:   device

**Return**

Timestamp of the event in nanoseconds.

int iio_read_mount_matrix(struct [device](../infrastructure.md#c.device "device") \*dev, struct [iio_mount_matrix](core.md#c.iio_mount_matrix "iio_mount_matrix") \*matrix)
:   retrieve iio device mounting matrix from device "mount-matrix" property

**Parameters**

`struct device *dev`
:   device the mounting matrix property is assigned to

`struct iio_mount_matrix *matrix`
:   where to store retrieved matrix

**Description**

If device is assigned no mounting matrix property, a default 3x3 identity
matrix will be filled in.

**Return**

0 if success, or a negative error code on failure.

ssize_t iio_format_value(char \*buf, unsigned int type, int size, int \*vals)
:   Formats a IIO value into its string representation

**Parameters**

`char *buf`
:   The buffer to which the formatted value gets written
    which is assumed to be big enough (i.e. PAGE_SIZE).

`unsigned int type`
:   One of the IIO_VAL_\* constants. This decides how the val
    and val2 parameters are formatted.

`int size`
:   Number of IIO value entries contained in vals

`int *vals`
:   Pointer to the values, exact meaning depends on the
    type parameter.

**Return**

0 by default, a negative number on failure or the total number of characters
written for a type that belongs to the IIO_VAL_\* constant.

int iio_str_to_fixpoint(const char \*str, int fract_mult, int \*integer, int \*fract)
:   Parse a fixed-point number from a string

**Parameters**

`const char *str`
:   The string to parse

`int fract_mult`
:   Multiplier for the first decimal place, should be a power of 10

`int *integer`
:   The integer part of the number

`int *fract`
:   The fractional part of the number

**Return**

0 on success, or a negative error code if the string could not be parsed.

struct [iio_dev](core.md#c.iio_dev "iio_dev") \*iio_device_alloc(struct [device](../infrastructure.md#c.device "device") \*parent, int sizeof_priv)
:   allocate an iio_dev from a driver

**Parameters**

`struct device *parent`
:   Parent device.

`int sizeof_priv`
:   Space to allocate for private structure.

**Return**

Pointer to allocated iio_dev on success, NULL on failure.

void iio_device_free(struct [iio_dev](core.md#c.iio_dev "iio_dev") \*dev)
:   free an iio_dev from a driver

**Parameters**

`struct iio_dev *dev`
:   the iio_dev associated with the device

struct [iio_dev](core.md#c.iio_dev "iio_dev") \*devm_iio_device_alloc(struct [device](../infrastructure.md#c.device "device") \*parent, int sizeof_priv)
:   Resource-managed [`iio_device_alloc()`](core.md#c.iio_device_alloc "iio_device_alloc")

**Parameters**

`struct device *parent`
:   Device to allocate iio_dev for, and parent for this IIO device

`int sizeof_priv`
:   Space to allocate for private structure.

**Description**

Managed iio_device_alloc. iio_dev allocated with this function is
automatically freed on driver detach.

**Return**

Pointer to allocated iio_dev on success, NULL on failure.

void iio_device_unregister(struct [iio_dev](core.md#c.iio_dev "iio_dev") \*indio_dev)
:   unregister a device from the IIO subsystem

**Parameters**

`struct iio_dev *indio_dev`
:   Device structure representing the device.

int iio_device_claim_direct_mode(struct [iio_dev](core.md#c.iio_dev "iio_dev") \*indio_dev)
:   Keep device in direct mode

**Parameters**

`struct iio_dev *indio_dev`
:   the iio_dev associated with the device

**Description**

If the device is in direct mode it is guaranteed to stay
that way until [`iio_device_release_direct_mode()`](core.md#c.iio_device_release_direct_mode "iio_device_release_direct_mode") is called.

Use with [`iio_device_release_direct_mode()`](core.md#c.iio_device_release_direct_mode "iio_device_release_direct_mode")

**Return**

0 on success, -EBUSY on failure.

void iio_device_release_direct_mode(struct [iio_dev](core.md#c.iio_dev "iio_dev") \*indio_dev)
:   releases claim on direct mode

**Parameters**

`struct iio_dev *indio_dev`
:   the iio_dev associated with the device

**Description**

Release the claim. Device is no longer guaranteed to stay
in direct mode.

Use with [`iio_device_claim_direct_mode()`](core.md#c.iio_device_claim_direct_mode "iio_device_claim_direct_mode")

int iio_device_claim_buffer_mode(struct [iio_dev](core.md#c.iio_dev "iio_dev") \*indio_dev)
:   Keep device in buffer mode

**Parameters**

`struct iio_dev *indio_dev`
:   the iio_dev associated with the device

**Description**

If the device is in buffer mode it is guaranteed to stay
that way until [`iio_device_release_buffer_mode()`](core.md#c.iio_device_release_buffer_mode "iio_device_release_buffer_mode") is called.

Use with [`iio_device_release_buffer_mode()`](core.md#c.iio_device_release_buffer_mode "iio_device_release_buffer_mode").

**Return**

0 on success, -EBUSY on failure.

void iio_device_release_buffer_mode(struct [iio_dev](core.md#c.iio_dev "iio_dev") \*indio_dev)
:   releases claim on buffer mode

**Parameters**

`struct iio_dev *indio_dev`
:   the iio_dev associated with the device

**Description**

Release the claim. Device is no longer guaranteed to stay
in buffer mode.

Use with [`iio_device_claim_buffer_mode()`](core.md#c.iio_device_claim_buffer_mode "iio_device_claim_buffer_mode").

int iio_device_get_current_mode(struct [iio_dev](core.md#c.iio_dev "iio_dev") \*indio_dev)
:   helper function providing read-only access to the opaque **currentmode** variable

**Parameters**

`struct iio_dev *indio_dev`
:   IIO device structure for device
