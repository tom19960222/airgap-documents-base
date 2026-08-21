---
collection: kernel
version: "6.8"
title: "Device Frequency Scaling"
source_url: https://www.kernel.org/doc/html/v6.8/driver-api/devfreq.html
fetched_at: 2026-08-21T03:30:46+00:00
---
# Device Frequency Scaling

## Introduction

This framework provides a standard kernel interface for Dynamic Voltage and
Frequency Switching on arbitrary devices.

It exposes controls for adjusting frequency through sysfs files which are
similar to the cpufreq subsystem.

Devices for which current usage can be measured can have their frequency
automatically adjusted by governors.

## API

Device drivers need to initialize a `devfreq_profile` and call the
[`devfreq_add_device()`](devfreq.md#c.devfreq_add_device "devfreq_add_device") function to create a [`devfreq`](devfreq.md#c.devfreq "devfreq") instance.

struct devfreq_dev_status
:   Data given from devfreq user device to governors. Represents the performance statistics.

**Definition**:

```
struct devfreq_dev_status {
    unsigned long total_time;
    unsigned long busy_time;
    unsigned long current_frequency;
    void *private_data;
};
```

**Members**

`total_time`
:   The total time represented by this instance of
    devfreq_dev_status

`busy_time`
:   The time that the device was working among the
    total_time.

`current_frequency`
:   The operating frequency.

`private_data`
:   An entry not specified by the devfreq framework.
    A device and a specific governor may have their
    own protocol with private_data. However, because
    this is governor-specific, a governor using this
    will be only compatible with devices aware of it.

struct devfreq_dev_profile
:   Devfreq's user device profile

**Definition**:

```
struct devfreq_dev_profile {
    unsigned long initial_freq;
    unsigned int polling_ms;
    enum devfreq_timer timer;
    int (*target)(struct device *dev, unsigned long *freq, u32 flags);
    int (*get_dev_status)(struct device *dev, struct devfreq_dev_status *stat);
    int (*get_cur_freq)(struct device *dev, unsigned long *freq);
    void (*exit)(struct device *dev);
    unsigned long *freq_table;
    unsigned int max_state;
    bool is_cooling_device;
};
```

**Members**

`initial_freq`
:   The operating frequency when [`devfreq_add_device()`](devfreq.md#c.devfreq_add_device "devfreq_add_device") is
    called.

`polling_ms`
:   The polling interval in ms. 0 disables polling.

`timer`
:   Timer type is either deferrable or delayed timer.

`target`
:   The device should set its operating frequency at
    freq or lowest-upper-than-freq value. If freq is
    higher than any operable frequency, set maximum.
    Before returning, target function should set
    freq at the current frequency.
    The "flags" parameter's possible values are
    explained above with "DEVFREQ_FLAG_\*" macros.

`get_dev_status`
:   The device should provide the current performance
    status to devfreq. Governors are recommended not to
    use this directly. Instead, governors are recommended
    to use devfreq_update_stats() along with
    devfreq.last_status.

`get_cur_freq`
:   The device should provide the current frequency
    at which it is operating.

`exit`
:   An optional callback that is called when devfreq
    is removing the devfreq object due to error or
    from [`devfreq_remove_device()`](devfreq.md#c.devfreq_remove_device "devfreq_remove_device") call. If the user
    has registered devfreq->nb at a notifier-head,
    this is the time to unregister it.

`freq_table`
:   Optional list of frequencies to support statistics
    and freq_table must be generated in ascending order.

`max_state`
:   The size of freq_table.

`is_cooling_device`
:   A self-explanatory boolean giving the device a
    cooling effect property.

struct devfreq_stats
:   Statistics of devfreq device behavior

**Definition**:

```
struct devfreq_stats {
    unsigned int total_trans;
    unsigned int *trans_table;
    u64 *time_in_state;
    u64 last_update;
};
```

**Members**

`total_trans`
:   Number of devfreq transitions.

`trans_table`
:   Statistics of devfreq transitions.

`time_in_state`
:   Statistics of devfreq states.

`last_update`
:   The last time stats were updated.

struct devfreq
:   Device devfreq structure

**Definition**:

```
struct devfreq {
    struct list_head node;
    struct mutex lock;
    struct device dev;
    struct devfreq_dev_profile *profile;
    const struct devfreq_governor *governor;
    struct opp_table *opp_table;
    struct notifier_block nb;
    struct delayed_work work;
    unsigned long *freq_table;
    unsigned int max_state;
    unsigned long previous_freq;
    struct devfreq_dev_status last_status;
    void *data;
    void *governor_data;
    struct dev_pm_qos_request user_min_freq_req;
    struct dev_pm_qos_request user_max_freq_req;
    unsigned long scaling_min_freq;
    unsigned long scaling_max_freq;
    bool stop_polling;
    unsigned long suspend_freq;
    unsigned long resume_freq;
    atomic_t suspend_count;
    struct devfreq_stats stats;
    struct srcu_notifier_head transition_notifier_list;
    struct thermal_cooling_device *cdev;
    struct notifier_block nb_min;
    struct notifier_block nb_max;
};
```

**Members**

`node`
:   list node - contains the devices with devfreq that have been
    registered.

`lock`
:   a mutex to protect accessing devfreq.

`dev`
:   device registered by devfreq class. dev.parent is the device
    using devfreq.

`profile`
:   device-specific devfreq profile

`governor`
:   method how to choose frequency based on the usage.

`opp_table`
:   Reference to OPP table of dev.parent, if one exists.

`nb`
:   notifier block used to notify devfreq object that it should
    reevaluate operable frequencies. Devfreq users may use
    devfreq.nb to the corresponding register notifier call chain.

`work`
:   delayed work for load monitoring.

`freq_table`
:   current frequency table used by the devfreq driver.

`max_state`
:   count of entry present in the frequency table.

`previous_freq`
:   previously configured frequency value.

`last_status`
:   devfreq user device info, performance statistics

`data`
:   devfreq driver pass to governors, governor should not change it.

`governor_data`
:   private data for governors, devfreq core doesn't touch it.

`user_min_freq_req`
:   PM QoS minimum frequency request from user (via sysfs)

`user_max_freq_req`
:   PM QoS maximum frequency request from user (via sysfs)

`scaling_min_freq`
:   Limit minimum frequency requested by OPP interface

`scaling_max_freq`
:   Limit maximum frequency requested by OPP interface

`stop_polling`
:   devfreq polling status of a device.

`suspend_freq`
:   frequency of a device set during suspend phase.

`resume_freq`
:   frequency of a device set in resume phase.

`suspend_count`
:   suspend requests counter for a device.

`stats`
:   Statistics of devfreq device behavior

`transition_notifier_list`
:   list head of DEVFREQ_TRANSITION_NOTIFIER notifier

`cdev`
:   Cooling device pointer if the devfreq has cooling property

`nb_min`
:   Notifier block for DEV_PM_QOS_MIN_FREQUENCY

`nb_max`
:   Notifier block for DEV_PM_QOS_MAX_FREQUENCY

**Description**

This structure stores the devfreq information for a given device.

Note that when a governor accesses entries in [`struct devfreq`](devfreq.md#c.devfreq "devfreq") in its
functions except for the context of callbacks defined in struct
devfreq_governor, the governor should protect its access with the
struct mutex lock in [`struct devfreq`](devfreq.md#c.devfreq "devfreq"). A governor may use this mutex
to protect its own private data in `void *data` as well.

struct devfreq_simple_ondemand_data
:   `void *data` fed to [`struct devfreq`](devfreq.md#c.devfreq "devfreq") and devfreq_add_device

**Definition**:

```
struct devfreq_simple_ondemand_data {
    unsigned int upthreshold;
    unsigned int downdifferential;
};
```

**Members**

`upthreshold`
:   If the load is over this value, the frequency jumps.
    Specify 0 to use the default. Valid value = 0 to 100.

`downdifferential`
:   If the load is under upthreshold - downdifferential,
    the governor may consider slowing the frequency down.
    Specify 0 to use the default. Valid value = 0 to 100.
    downdifferential < upthreshold must hold.

**Description**

If the fed devfreq_simple_ondemand_data pointer is NULL to the governor,
the governor uses the default values.

struct devfreq_passive_data
:   `void *data` fed to [`struct devfreq`](devfreq.md#c.devfreq "devfreq") and devfreq_add_device

**Definition**:

```
struct devfreq_passive_data {
    struct devfreq *parent;
    int (*get_target_freq)(struct devfreq *this, unsigned long *freq);
    enum devfreq_parent_dev_type parent_type;
    struct devfreq *this;
    struct notifier_block nb;
    struct list_head cpu_data_list;
};
```

**Members**

`parent`
:   the devfreq instance of parent device.

`get_target_freq`
:   Optional callback, Returns desired operating frequency
    for the device using passive governor. That is called
    when passive governor should decide the next frequency
    by using the new frequency of parent devfreq device
    using governors except for passive governor.
    If the devfreq device has the specific method to decide
    the next frequency, should use this callback.

`parent_type`
:   the parent type of the device.

`this`
:   the devfreq instance of own device.

`nb`
:   the notifier block for DEVFREQ_TRANSITION_NOTIFIER or
    CPUFREQ_TRANSITION_NOTIFIER list.

`cpu_data_list`
:   the list of cpu frequency data for all cpufreq_policy.

**Description**

The devfreq_passive_data have to set the devfreq instance of parent
device with governors except for the passive governor. But, don't need to
initialize the 'this' and 'nb' field because the devfreq core will handle
them.

struct devfreq_event_dev
:   the devfreq-event device

**Definition**:

```
struct devfreq_event_dev {
    struct list_head node;
    struct device dev;
    struct mutex lock;
    u32 enable_count;
    const struct devfreq_event_desc *desc;
};
```

**Members**

`node`
:   Contain the devfreq-event device that have been registered.

`dev`
:   the device registered by devfreq-event class. dev.parent is
    the device using devfreq-event.

`lock`
:   a mutex to protect accessing devfreq-event.

`enable_count`
:   the number of enable function have been called.

`desc`
:   the description for devfreq-event device.

**Description**

This structure contains devfreq-event device information.

struct devfreq_event_data
:   the devfreq-event data

**Definition**:

```
struct devfreq_event_data {
    unsigned long load_count;
    unsigned long total_count;
};
```

**Members**

`load_count`
:   load count of devfreq-event device for the given period.

`total_count`
:   total count of devfreq-event device for the given period.
    each count may represent a clock cycle, a time unit
    (ns/us/...), or anything the device driver wants.
    Generally, utilization is load_count / total_count.

**Description**

This structure contains the data of devfreq-event device for polling period.

struct devfreq_event_ops
:   the operations of devfreq-event device

**Definition**:

```
struct devfreq_event_ops {
    int (*enable)(struct devfreq_event_dev *edev);
    int (*disable)(struct devfreq_event_dev *edev);
    int (*reset)(struct devfreq_event_dev *edev);
    int (*set_event)(struct devfreq_event_dev *edev);
    int (*get_event)(struct devfreq_event_dev *edev, struct devfreq_event_data *edata);
};
```

**Members**

`enable`
:   Enable the devfreq-event device.

`disable`
:   Disable the devfreq-event device.

`reset`
:   Reset all setting of the devfreq-event device.

`set_event`
:   Set the specific event type for the devfreq-event device.

`get_event`
:   Get the result of the devfreq-event devie with specific
    event type.

**Description**

This structure contains devfreq-event device operations which can be
implemented by devfreq-event device drivers.

struct devfreq_event_desc
:   the descriptor of devfreq-event device

**Definition**:

```
struct devfreq_event_desc {
    const char *name;
    u32 event_type;
    void *driver_data;
    const struct devfreq_event_ops *ops;
};
```

**Members**

`name`
:   the name of devfreq-event device.

`event_type`
:   the type of the event determined and used by driver

`driver_data`
:   the private data for devfreq-event driver.

`ops`
:   the operation to control devfreq-event device.

**Description**

Each devfreq-event device is described with a this structure.
This structure contains the various data for devfreq-event device.
The event_type describes what is going to be counted in the register.
It might choose to count e.g. read requests, write data in bytes, etc.
The full supported list of types is present in specyfic header in:
include/dt-bindings/pmu/.

void devfreq_get_freq_range(struct [devfreq](devfreq.md#c.devfreq_get_freq_range "devfreq") \*devfreq, unsigned long \*min_freq, unsigned long \*max_freq)
:   Get the current freq range

**Parameters**

`struct devfreq *devfreq`
:   the devfreq instance

`unsigned long *min_freq`
:   the min frequency

`unsigned long *max_freq`
:   the max frequency

**Description**

This takes into consideration all constraints.

int devfreq_update_status(struct [devfreq](devfreq.md#c.devfreq_update_status "devfreq") \*devfreq, unsigned long freq)
:   Update statistics of devfreq behavior

**Parameters**

`struct devfreq *devfreq`
:   the devfreq instance

`unsigned long freq`
:   the update target frequency

int devfreq_update_target(struct [devfreq](devfreq.md#c.devfreq_update_target "devfreq") \*devfreq, unsigned long freq)
:   Reevaluate the device and configure frequency on the final stage.

**Parameters**

`struct devfreq *devfreq`
:   the devfreq instance.

`unsigned long freq`
:   the new frequency of parent device. This argument
    is only used for devfreq device using passive governor.

**Note**

Lock devfreq->lock before calling devfreq_update_target. This function
:   should be only used by both [`update_devfreq()`](devfreq.md#c.update_devfreq "update_devfreq") and devfreq governors.

int update_devfreq(struct [devfreq](devfreq.md#c.update_devfreq "devfreq") \*devfreq)
:   Reevaluate the device and configure frequency.

**Parameters**

`struct devfreq *devfreq`
:   the devfreq instance.

**Note**

Lock devfreq->lock before calling update_devfreq
:   This function is exported for governors.

void devfreq_monitor_start(struct [devfreq](devfreq.md#c.devfreq_monitor_start "devfreq") \*devfreq)
:   Start load monitoring of devfreq instance

**Parameters**

`struct devfreq *devfreq`
:   the devfreq instance.

**Description**

Helper function for starting devfreq device load monitoring. By default,
deferrable timer is used for load monitoring. But the users can change this
behavior using the "timer" type in devfreq_dev_profile. This function will be
called by devfreq governor in response to the DEVFREQ_GOV_START event
generated while adding a device to the devfreq framework.

void devfreq_monitor_stop(struct [devfreq](devfreq.md#c.devfreq_monitor_stop "devfreq") \*devfreq)
:   Stop load monitoring of a devfreq instance

**Parameters**

`struct devfreq *devfreq`
:   the devfreq instance.

**Description**

Helper function to stop devfreq device load monitoring. Function
to be called from governor in response to DEVFREQ_GOV_STOP
event when device is removed from devfreq framework.

void devfreq_monitor_suspend(struct [devfreq](devfreq.md#c.devfreq_monitor_suspend "devfreq") \*devfreq)
:   Suspend load monitoring of a devfreq instance

**Parameters**

`struct devfreq *devfreq`
:   the devfreq instance.

**Description**

Helper function to suspend devfreq device load monitoring. Function
to be called from governor in response to DEVFREQ_GOV_SUSPEND
event or when polling interval is set to zero.

**Note**

Though this function is same as [`devfreq_monitor_stop()`](devfreq.md#c.devfreq_monitor_stop "devfreq_monitor_stop"),
intentionally kept separate to provide hooks for collecting
transition statistics.

void devfreq_monitor_resume(struct [devfreq](devfreq.md#c.devfreq_monitor_resume "devfreq") \*devfreq)
:   Resume load monitoring of a devfreq instance

**Parameters**

`struct devfreq *devfreq`
:   the devfreq instance.

**Description**

Helper function to resume devfreq device load monitoring. Function
to be called from governor in response to DEVFREQ_GOV_RESUME
event or when polling interval is set to non-zero.

void devfreq_update_interval(struct [devfreq](devfreq.md#c.devfreq_update_interval "devfreq") \*devfreq, unsigned int \*delay)
:   Update device devfreq monitoring interval

**Parameters**

`struct devfreq *devfreq`
:   the devfreq instance.

`unsigned int *delay`
:   new polling interval to be set.

**Description**

Helper function to set new load monitoring polling interval. Function
to be called from governor in response to DEVFREQ_GOV_UPDATE_INTERVAL event.

struct [devfreq](devfreq.md#c.devfreq "devfreq") \*devfreq_add_device(struct [device](infrastructure.md#c.device "device") \*dev, struct [devfreq_dev_profile](devfreq.md#c.devfreq_dev_profile "devfreq_dev_profile") \*profile, const char \*governor_name, void \*data)
:   Add devfreq feature to the device

**Parameters**

`struct device *dev`
:   the device to add devfreq feature.

`struct devfreq_dev_profile *profile`
:   device-specific profile to run devfreq.

`const char *governor_name`
:   name of the policy to choose frequency.

`void *data`
:   devfreq driver pass to governors, governor should not change it.

int devfreq_remove_device(struct [devfreq](devfreq.md#c.devfreq_remove_device "devfreq") \*devfreq)
:   Remove devfreq feature from a device.

**Parameters**

`struct devfreq *devfreq`
:   the devfreq instance to be removed

**Description**

The opposite of [`devfreq_add_device()`](devfreq.md#c.devfreq_add_device "devfreq_add_device").

struct [devfreq](devfreq.md#c.devfreq "devfreq") \*devm_devfreq_add_device(struct [device](infrastructure.md#c.device "device") \*dev, struct [devfreq_dev_profile](devfreq.md#c.devfreq_dev_profile "devfreq_dev_profile") \*profile, const char \*governor_name, void \*data)
:   Resource-managed [`devfreq_add_device()`](devfreq.md#c.devfreq_add_device "devfreq_add_device")

**Parameters**

`struct device *dev`
:   the device to add devfreq feature.

`struct devfreq_dev_profile *profile`
:   device-specific profile to run devfreq.

`const char *governor_name`
:   name of the policy to choose frequency.

`void *data`
:   devfreq driver pass to governors, governor should not change it.

**Description**

This function manages automatically the memory of devfreq device using device
resource management and simplify the free operation for memory of devfreq
device.

void devm_devfreq_remove_device(struct [device](infrastructure.md#c.device "device") \*dev, struct [devfreq](devfreq.md#c.devm_devfreq_remove_device "devfreq") \*devfreq)
:   Resource-managed [`devfreq_remove_device()`](devfreq.md#c.devfreq_remove_device "devfreq_remove_device")

**Parameters**

`struct device *dev`
:   the device from which to remove devfreq feature.

`struct devfreq *devfreq`
:   the devfreq instance to be removed

int devfreq_suspend_device(struct [devfreq](devfreq.md#c.devfreq_suspend_device "devfreq") \*devfreq)
:   Suspend devfreq of a device.

**Parameters**

`struct devfreq *devfreq`
:   the devfreq instance to be suspended

**Description**

This function is intended to be called by the pm callbacks
(e.g., runtime_suspend, suspend) of the device driver that
holds the devfreq.

int devfreq_resume_device(struct [devfreq](devfreq.md#c.devfreq_resume_device "devfreq") \*devfreq)
:   Resume devfreq of a device.

**Parameters**

`struct devfreq *devfreq`
:   the devfreq instance to be resumed

**Description**

This function is intended to be called by the pm callbacks
(e.g., runtime_resume, resume) of the device driver that
holds the devfreq.

int devfreq_add_governor(struct devfreq_governor \*governor)
:   Add devfreq governor

**Parameters**

`struct devfreq_governor *governor`
:   the devfreq governor to be added

int devm_devfreq_add_governor(struct [device](infrastructure.md#c.device "device") \*dev, struct devfreq_governor \*governor)
:   Add devfreq governor

**Parameters**

`struct device *dev`
:   device which adds devfreq governor

`struct devfreq_governor *governor`
:   the devfreq governor to be added

**Description**

This is a resource-managed variant of [`devfreq_add_governor()`](devfreq.md#c.devfreq_add_governor "devfreq_add_governor").

int devfreq_remove_governor(struct devfreq_governor \*governor)
:   Remove devfreq feature from a device.

**Parameters**

`struct devfreq_governor *governor`
:   the devfreq governor to be removed

struct dev_pm_opp \*devfreq_recommended_opp(struct [device](infrastructure.md#c.device "device") \*dev, unsigned long \*freq, u32 flags)
:   Helper function to get proper OPP for the freq value given to target callback.

**Parameters**

`struct device *dev`
:   The devfreq user device. (parent of devfreq)

`unsigned long *freq`
:   The frequency given to target function

`u32 flags`
:   Flags handed from devfreq framework.

**Description**

The callers are required to call dev_pm_opp_put() for the returned OPP after
use.

int devfreq_register_opp_notifier(struct [device](infrastructure.md#c.device "device") \*dev, struct [devfreq](devfreq.md#c.devfreq_register_opp_notifier "devfreq") \*devfreq)
:   Helper function to get devfreq notified for any changes in the OPP availability changes

**Parameters**

`struct device *dev`
:   The devfreq user device. (parent of devfreq)

`struct devfreq *devfreq`
:   The devfreq object.

int devfreq_unregister_opp_notifier(struct [device](infrastructure.md#c.device "device") \*dev, struct [devfreq](devfreq.md#c.devfreq_unregister_opp_notifier "devfreq") \*devfreq)
:   Helper function to stop getting devfreq notified for any changes in the OPP availability changes anymore.

**Parameters**

`struct device *dev`
:   The devfreq user device. (parent of devfreq)

`struct devfreq *devfreq`
:   The devfreq object.

**Description**

At exit() callback of devfreq_dev_profile, this must be included if
devfreq_recommended_opp is used.

int devm_devfreq_register_opp_notifier(struct [device](infrastructure.md#c.device "device") \*dev, struct [devfreq](devfreq.md#c.devm_devfreq_register_opp_notifier "devfreq") \*devfreq)
:   Resource-managed [`devfreq_register_opp_notifier()`](devfreq.md#c.devfreq_register_opp_notifier "devfreq_register_opp_notifier")

**Parameters**

`struct device *dev`
:   The devfreq user device. (parent of devfreq)

`struct devfreq *devfreq`
:   The devfreq object.

void devm_devfreq_unregister_opp_notifier(struct [device](infrastructure.md#c.device "device") \*dev, struct [devfreq](devfreq.md#c.devm_devfreq_unregister_opp_notifier "devfreq") \*devfreq)
:   Resource-managed [`devfreq_unregister_opp_notifier()`](devfreq.md#c.devfreq_unregister_opp_notifier "devfreq_unregister_opp_notifier")

**Parameters**

`struct device *dev`
:   The devfreq user device. (parent of devfreq)

`struct devfreq *devfreq`
:   The devfreq object.

int devfreq_register_notifier(struct [devfreq](devfreq.md#c.devfreq_register_notifier "devfreq") \*devfreq, struct notifier_block \*nb, unsigned int list)
:   Register a driver with devfreq

**Parameters**

`struct devfreq *devfreq`
:   The devfreq object.

`struct notifier_block *nb`
:   The notifier block to register.

`unsigned int list`
:   DEVFREQ_TRANSITION_NOTIFIER.

int devm_devfreq_register_notifier(struct [device](infrastructure.md#c.device "device") \*dev, struct [devfreq](devfreq.md#c.devm_devfreq_register_notifier "devfreq") \*devfreq, struct notifier_block \*nb, unsigned int list)

**Parameters**

`struct device *dev`
:   The devfreq user device. (parent of devfreq)

`struct devfreq *devfreq`
:   The devfreq object.

`struct notifier_block *nb`
:   The notifier block to be unregistered.

`unsigned int list`
:   DEVFREQ_TRANSITION_NOTIFIER.

**Description**

> - Resource-managed [`devfreq_register_notifier()`](devfreq.md#c.devfreq_register_notifier "devfreq_register_notifier")

void devm_devfreq_unregister_notifier(struct [device](infrastructure.md#c.device "device") \*dev, struct [devfreq](devfreq.md#c.devm_devfreq_unregister_notifier "devfreq") \*devfreq, struct notifier_block \*nb, unsigned int list)

**Parameters**

`struct device *dev`
:   The devfreq user device. (parent of devfreq)

`struct devfreq *devfreq`
:   The devfreq object.

`struct notifier_block *nb`
:   The notifier block to be unregistered.

`unsigned int list`
:   DEVFREQ_TRANSITION_NOTIFIER.

**Description**

> - Resource-managed devfreq_unregister_notifier()

int devfreq_event_enable_edev(struct [devfreq_event_dev](devfreq.md#c.devfreq_event_dev "devfreq_event_dev") \*edev)
:   Enable the devfreq-event dev and increase the enable_count of devfreq-event dev.

**Parameters**

`struct devfreq_event_dev *edev`
:   the devfreq-event device

**Description**

Note that this function increase the enable_count and enable the
devfreq-event device. The devfreq-event device should be enabled before
using it by devfreq device.

int devfreq_event_disable_edev(struct [devfreq_event_dev](devfreq.md#c.devfreq_event_dev "devfreq_event_dev") \*edev)
:   Disable the devfreq-event dev and decrease the enable_count of the devfreq-event dev.

**Parameters**

`struct devfreq_event_dev *edev`
:   the devfreq-event device

**Description**

Note that this function decrease the enable_count and disable the
devfreq-event device. After the devfreq-event device is disabled,
devfreq device can't use the devfreq-event device for get/set/reset
operations.

bool devfreq_event_is_enabled(struct [devfreq_event_dev](devfreq.md#c.devfreq_event_dev "devfreq_event_dev") \*edev)
:   Check whether devfreq-event dev is enabled or not.

**Parameters**

`struct devfreq_event_dev *edev`
:   the devfreq-event device

**Description**

Note that this function check whether devfreq-event dev is enabled or not.
If return true, the devfreq-event dev is enabeld. If return false, the
devfreq-event dev is disabled.

int devfreq_event_set_event(struct [devfreq_event_dev](devfreq.md#c.devfreq_event_dev "devfreq_event_dev") \*edev)
:   Set event to devfreq-event dev to start.

**Parameters**

`struct devfreq_event_dev *edev`
:   the devfreq-event device

**Description**

Note that this function set the event to the devfreq-event device to start
for getting the event data which could be various event type.

int devfreq_event_get_event(struct [devfreq_event_dev](devfreq.md#c.devfreq_event_dev "devfreq_event_dev") \*edev, struct [devfreq_event_data](devfreq.md#c.devfreq_event_data "devfreq_event_data") \*edata)
:   Get {load|total}_count from devfreq-event dev.

**Parameters**

`struct devfreq_event_dev *edev`
:   the devfreq-event device

`struct devfreq_event_data *edata`
:   the calculated data of devfreq-event device

**Description**

Note that this function get the calculated event data from devfreq-event dev
after stoping the progress of whole sequence of devfreq-event dev.

int devfreq_event_reset_event(struct [devfreq_event_dev](devfreq.md#c.devfreq_event_dev "devfreq_event_dev") \*edev)
:   Reset all opeations of devfreq-event dev.

**Parameters**

`struct devfreq_event_dev *edev`
:   the devfreq-event device

**Description**

Note that this function stop all operations of devfreq-event dev and reset
the current event data to make the devfreq-event device into initial state.

struct [devfreq_event_dev](devfreq.md#c.devfreq_event_dev "devfreq_event_dev") \*devfreq_event_get_edev_by_phandle(struct [device](infrastructure.md#c.device "device") \*dev, const char \*phandle_name, int index)
:   Get the devfreq-event dev from devicetree.

**Parameters**

`struct device *dev`
:   the pointer to the given device

`const char *phandle_name`
:   name of property holding a phandle value

`int index`
:   the index into list of devfreq-event device

**Description**

Note that this function return the pointer of devfreq-event device.

int devfreq_event_get_edev_count(struct [device](infrastructure.md#c.device "device") \*dev, const char \*phandle_name)
:   Get the count of devfreq-event dev

**Parameters**

`struct device *dev`
:   the pointer to the given device

`const char *phandle_name`
:   name of property holding a phandle value

**Description**

Note that this function return the count of devfreq-event devices.

struct [devfreq_event_dev](devfreq.md#c.devfreq_event_dev "devfreq_event_dev") \*devfreq_event_add_edev(struct [device](infrastructure.md#c.device "device") \*dev, struct [devfreq_event_desc](devfreq.md#c.devfreq_event_desc "devfreq_event_desc") \*desc)
:   Add new devfreq-event device.

**Parameters**

`struct device *dev`
:   the device owning the devfreq-event device being created

`struct devfreq_event_desc *desc`
:   the devfreq-event device's descriptor which include essential
    data for devfreq-event device.

**Description**

Note that this function add new devfreq-event device to devfreq-event class
list and register the device of the devfreq-event device.

int devfreq_event_remove_edev(struct [devfreq_event_dev](devfreq.md#c.devfreq_event_dev "devfreq_event_dev") \*edev)
:   Remove the devfreq-event device registered.

**Parameters**

`struct devfreq_event_dev *edev`
:   the devfreq-event device

**Description**

Note that this function removes the registered devfreq-event device.

struct [devfreq_event_dev](devfreq.md#c.devfreq_event_dev "devfreq_event_dev") \*devm_devfreq_event_add_edev(struct [device](infrastructure.md#c.device "device") \*dev, struct [devfreq_event_desc](devfreq.md#c.devfreq_event_desc "devfreq_event_desc") \*desc)
:   Resource-managed [`devfreq_event_add_edev()`](devfreq.md#c.devfreq_event_add_edev "devfreq_event_add_edev")

**Parameters**

`struct device *dev`
:   the device owning the devfreq-event device being created

`struct devfreq_event_desc *desc`
:   the devfreq-event device's descriptor which include essential
    data for devfreq-event device.

**Description**

Note that this function manages automatically the memory of devfreq-event
device using device resource management and simplify the free operation
for memory of devfreq-event device.

void devm_devfreq_event_remove_edev(struct [device](infrastructure.md#c.device "device") \*dev, struct [devfreq_event_dev](devfreq.md#c.devfreq_event_dev "devfreq_event_dev") \*edev)
:   Resource-managed [`devfreq_event_remove_edev()`](devfreq.md#c.devfreq_event_remove_edev "devfreq_event_remove_edev")

**Parameters**

`struct device *dev`
:   the device owning the devfreq-event device being created

`struct devfreq_event_dev *edev`
:   the devfreq-event device

**Description**

Note that this function manages automatically the memory of devfreq-event
device using device resource management.
