---
collection: kernel
version: "6.8"
title: "Voltage and current regulator API"
source_url: https://www.kernel.org/doc/html/v6.8/driver-api/regulator.html
fetched_at: 2026-08-21T03:30:38+00:00
---
# Voltage and current regulator API

Author
:   Liam Girdwood

Author
:   Mark Brown

## Introduction

This framework is designed to provide a standard kernel interface to
control voltage and current regulators.

The intention is to allow systems to dynamically control regulator power
output in order to save power and prolong battery life. This applies to
both voltage regulators (where voltage output is controllable) and
current sinks (where current limit is controllable).

Note that additional (and currently more complete) documentation is
available in the Linux kernel source under
`Documentation/power/regulator`.

### Glossary

The regulator API uses a number of terms which may not be familiar:

Regulator

> Electronic device that supplies power to other devices. Most regulators
> can enable and disable their output and some can also control their
> output voltage or current.

Consumer

> Electronic device which consumes power provided by a regulator. These
> may either be static, requiring only a fixed supply, or dynamic,
> requiring active management of the regulator at runtime.

Power Domain

> The electronic circuit supplied by a given regulator, including the
> regulator and all consumer devices. The configuration of the regulator
> is shared between all the components in the circuit.

Power Management Integrated Circuit (PMIC)

> An IC which contains numerous regulators and often also other
> subsystems. In an embedded system the primary PMIC is often equivalent
> to a combination of the PSU and southbridge in a desktop system.

## Consumer driver interface

This offers a similar API to the kernel clock framework. Consumer
drivers use [get](regulator.md#API-regulator-get) and
[put](regulator.md#API-regulator-put) operations to acquire and release
regulators. Functions are provided to [enable](regulator.md#API-regulator-enable)
and [disable](regulator.md#API-regulator-disable) the regulator and to get and
set the runtime parameters of the regulator.

When requesting regulators consumers use symbolic names for their
supplies, such as "Vcc", which are mapped into actual regulator devices
by the machine interface.

A stub version of this API is provided when the regulator framework is
not in use in order to minimise the need to use ifdefs.

### Enabling and disabling

The regulator API provides reference counted enabling and disabling of
regulators. Consumer devices use the [`regulator_enable()`](regulator.md#c.regulator_enable "regulator_enable") and
[`regulator_disable()`](regulator.md#c.regulator_disable "regulator_disable") functions to enable and disable
regulators. Calls to the two functions must be balanced.

Note that since multiple consumers may be using a regulator and machine
constraints may not allow the regulator to be disabled there is no
guarantee that calling [`regulator_disable()`](regulator.md#c.regulator_disable "regulator_disable") will actually
cause the supply provided by the regulator to be disabled. Consumer
drivers should assume that the regulator may be enabled at all times.

### Configuration

Some consumer devices may need to be able to dynamically configure their
supplies. For example, MMC drivers may need to select the correct
operating voltage for their cards. This may be done while the regulator
is enabled or disabled.

The [`regulator_set_voltage()`](regulator.md#c.regulator_set_voltage "regulator_set_voltage") and
[`regulator_set_current_limit()`](regulator.md#c.regulator_set_current_limit "regulator_set_current_limit") functions provide the primary
interface for this. Both take ranges of voltages and currents, supporting
drivers that do not require a specific value (eg, CPU frequency scaling
normally permits the CPU to use a wider range of supply voltages at lower
frequencies but does not require that the supply voltage be lowered). Where
an exact value is required both minimum and maximum values should be
identical.

### Callbacks

Callbacks may also be registered for events such as regulation failures.

## Regulator driver interface

Drivers for regulator chips register the regulators with the regulator
core, providing operations structures to the core. A notifier interface
allows error conditions to be reported to the core.

Registration should be triggered by explicit setup done by the platform,
supplying a [`struct regulator_init_data`](regulator.md#c.regulator_init_data "regulator_init_data") for the regulator
containing constraint and supply information.

## Machine interface

This interface provides a way to define how regulators are connected to
consumers on a given system and what the valid operating parameters are
for the system.

### Supplies

Regulator supplies are specified using struct
[`regulator_consumer_supply`](regulator.md#c.regulator_consumer_supply "regulator_consumer_supply"). This is done at driver registration
time as part of the machine constraints.

### Constraints

As well as defining the connections the machine interface also provides
constraints defining the operations that clients are allowed to perform
and the parameters that may be set. This is required since generally
regulator devices will offer more flexibility than it is safe to use on
a given system, for example supporting higher supply voltages than the
consumers are rated for.

This is done at driver registration time` by providing a
[`struct regulation_constraints`](regulator.md#c.regulation_constraints "regulation_constraints").

The constraints may also specify an initial configuration for the
regulator in the constraints, which is particularly useful for use with
static consumers.

## API reference

Due to limitations of the kernel documentation framework and the
existing layout of the source code the entire regulator API is
documented here.

struct pre_voltage_change_data
:   Data sent with PRE_VOLTAGE_CHANGE event

**Definition**:

```
struct pre_voltage_change_data {
    unsigned long old_uV;
    unsigned long min_uV;
    unsigned long max_uV;
};
```

**Members**

`old_uV`
:   Current voltage before change.

`min_uV`
:   Min voltage we'll change to.

`max_uV`
:   Max voltage we'll change to.

struct regulator_bulk_data
:   Data used for bulk regulator operations.

**Definition**:

```
struct regulator_bulk_data {
    const char *supply;
    int init_load_uA;
    struct regulator *consumer;
};
```

**Members**

`supply`
:   The name of the supply. Initialised by the user before
    using the bulk regulator APIs.

`init_load_uA`
:   After getting the regulator, [`regulator_set_load()`](regulator.md#c.regulator_set_load "regulator_set_load") will be
    called with this load. Initialised by the user before
    using the bulk regulator APIs.

`consumer`
:   The regulator consumer for the supply. This will be managed
    by the bulk API.

**Description**

The regulator APIs provide a series of regulator_bulk_() API calls as
a convenience to consumers which require multiple supplies. This
structure is used to manage data for these calls.

struct regulator_state
:   regulator state during low power system states

**Definition**:

```
struct regulator_state {
    int uV;
    int min_uV;
    int max_uV;
    unsigned int mode;
    int enabled;
    bool changeable;
};
```

**Members**

`uV`
:   Default operating voltage during suspend, it can be adjusted
    among <min_uV, max_uV>.

`min_uV`
:   Minimum suspend voltage may be set.

`max_uV`
:   Maximum suspend voltage may be set.

`mode`
:   Operating mode during suspend.

`enabled`
:   operations during suspend.
    - DO_NOTHING_IN_SUSPEND
    - DISABLE_IN_SUSPEND
    - ENABLE_IN_SUSPEND

`changeable`
:   Is this state can be switched between enabled/disabled,

**Description**

This describes a regulators state during a system wide low power
state. One of enabled or disabled must be set for the
configuration to be applied.

struct regulation_constraints
:   regulator operating constraints.

**Definition**:

```
struct regulation_constraints {
    const char *name;
    int min_uV;
    int max_uV;
    int uV_offset;
    int min_uA;
    int max_uA;
    int ilim_uA;
    int system_load;
    u32 *max_spread;
    int max_uV_step;
    unsigned int valid_modes_mask;
    unsigned int valid_ops_mask;
    int input_uV;
    struct regulator_state state_disk;
    struct regulator_state state_mem;
    struct regulator_state state_standby;
    struct notification_limit over_curr_limits;
    struct notification_limit over_voltage_limits;
    struct notification_limit under_voltage_limits;
    struct notification_limit temp_limits;
    suspend_state_t initial_state;
    unsigned int initial_mode;
    unsigned int ramp_delay;
    unsigned int settling_time;
    unsigned int settling_time_up;
    unsigned int settling_time_down;
    unsigned int enable_time;
    unsigned int uv_less_critical_window_ms;
    unsigned int active_discharge;
    unsigned always_on:1;
    unsigned boot_on:1;
    unsigned apply_uV:1;
    unsigned ramp_disable:1;
    unsigned soft_start:1;
    unsigned pull_down:1;
    unsigned system_critical:1;
    unsigned over_current_protection:1;
    unsigned over_current_detection:1;
    unsigned over_voltage_detection:1;
    unsigned under_voltage_detection:1;
    unsigned over_temp_detection:1;
};
```

**Members**

`name`
:   Descriptive name for the constraints, used for display purposes.

`min_uV`
:   Smallest voltage consumers may set.

`max_uV`
:   Largest voltage consumers may set.

`uV_offset`
:   Offset applied to voltages from consumer to compensate for
    voltage drops.

`min_uA`
:   Smallest current consumers may set.

`max_uA`
:   Largest current consumers may set.

`ilim_uA`
:   Maximum input current.

`system_load`
:   Load that isn't captured by any consumer requests.

`max_spread`
:   Max possible spread between coupled regulators

`max_uV_step`
:   Max possible step change in voltage

`valid_modes_mask`
:   Mask of modes which may be configured by consumers.

`valid_ops_mask`
:   Operations which may be performed by consumers.

`input_uV`
:   Input voltage for regulator when supplied by another regulator.

`state_disk`
:   State for regulator when system is suspended in disk mode.

`state_mem`
:   State for regulator when system is suspended in mem mode.

`state_standby`
:   State for regulator when system is suspended in standby
    mode.

`over_curr_limits`
:   Limits for acting on over current.

`over_voltage_limits`
:   Limits for acting on over voltage.

`under_voltage_limits`
:   Limits for acting on under voltage.

`temp_limits`
:   Limits for acting on over temperature.

`initial_state`
:   Suspend state to set by default.

`initial_mode`
:   Mode to set at startup.

`ramp_delay`
:   Time to settle down after voltage change (unit: uV/us)

`settling_time`
:   Time to settle down after voltage change when voltage
    change is non-linear (unit: microseconds).

`settling_time_up`
:   Time to settle down after voltage increase when voltage
    change is non-linear (unit: microseconds).

`settling_time_down`
:   Time to settle down after voltage decrease when
    voltage change is non-linear (unit: microseconds).

`enable_time`
:   Turn-on time of the rails (unit: microseconds)

`uv_less_critical_window_ms`
:   Specifies the time window (in milliseconds)
    following a critical under-voltage (UV) event
    during which less critical actions can be
    safely carried out by the system (for example
    logging). After this time window more critical
    actions should be done (for example prevent
    HW damage).

`active_discharge`
:   Enable/disable active discharge. The enum
    regulator_active_discharge values are used for
    initialisation.

`always_on`
:   Set if the regulator should never be disabled.

`boot_on`
:   Set if the regulator is enabled when the system is initially
    started. If the regulator is not enabled by the hardware or
    bootloader then it will be enabled when the constraints are
    applied.

`apply_uV`
:   Apply the voltage constraint when initialising.

`ramp_disable`
:   Disable ramp delay when initialising or when setting voltage.

`soft_start`
:   Enable soft start so that voltage ramps slowly.

`pull_down`
:   Enable pull down when regulator is disabled.

`system_critical`
:   Set if the regulator is critical to system stability or
    functionality.

`over_current_protection`
:   Auto disable on over current event.

`over_current_detection`
:   Configure over current limits.

`over_voltage_detection`
:   Configure over voltage limits.

`under_voltage_detection`
:   Configure under voltage limits.

`over_temp_detection`
:   Configure over temperature limits.

**Description**

This struct describes regulator and board/machine specific constraints.

struct regulator_consumer_supply
:   supply -> device mapping

**Definition**:

```
struct regulator_consumer_supply {
    const char *dev_name;
    const char *supply;
};
```

**Members**

`dev_name`
:   Result of [`dev_name()`](infrastructure.md#c.dev_name "dev_name") for the consumer.

`supply`
:   Name for the supply.

**Description**

This maps a supply name to a device. Use of dev_name allows support for
buses which make [`struct device`](infrastructure.md#c.device "device") available late such as I2C.

struct regulator_init_data
:   regulator platform initialisation data.

**Definition**:

```
struct regulator_init_data {
    const char *supply_regulator;
    struct regulation_constraints constraints;
    int num_consumer_supplies;
    struct regulator_consumer_supply *consumer_supplies;
    int (*regulator_init)(void *driver_data);
    void *driver_data;
};
```

**Members**

`supply_regulator`
:   Parent regulator. Specified using the regulator name
    as it appears in the name field in sysfs, which can
    be explicitly set using the constraints field 'name'.

`constraints`
:   Constraints. These must be specified for the regulator to
    be usable.

`num_consumer_supplies`
:   Number of consumer device supplies.

`consumer_supplies`
:   Consumer device supply configuration.

`regulator_init`
:   Callback invoked when the regulator has been registered.

`driver_data`
:   Data passed to regulator_init.

**Description**

Initialisation constraints, our supply and consumers supplies.

struct regulator_ops
:   regulator operations.

**Definition**:

```
struct regulator_ops {
    int (*list_voltage) (struct regulator_dev *, unsigned selector);
    int (*set_voltage) (struct regulator_dev *, int min_uV, int max_uV, unsigned *selector);
    int (*map_voltage)(struct regulator_dev *, int min_uV, int max_uV);
    int (*set_voltage_sel) (struct regulator_dev *, unsigned selector);
    int (*get_voltage) (struct regulator_dev *);
    int (*get_voltage_sel) (struct regulator_dev *);
    int (*set_current_limit) (struct regulator_dev *, int min_uA, int max_uA);
    int (*get_current_limit) (struct regulator_dev *);
    int (*set_input_current_limit) (struct regulator_dev *, int lim_uA);
    int (*set_over_current_protection)(struct regulator_dev *, int lim_uA, int severity, bool enable);
    int (*set_over_voltage_protection)(struct regulator_dev *, int lim_uV, int severity, bool enable);
    int (*set_under_voltage_protection)(struct regulator_dev *, int lim_uV, int severity, bool enable);
    int (*set_thermal_protection)(struct regulator_dev *, int lim, int severity, bool enable);
    int (*set_active_discharge)(struct regulator_dev *, bool enable);
    int (*enable) (struct regulator_dev *);
    int (*disable) (struct regulator_dev *);
    int (*is_enabled) (struct regulator_dev *);
    int (*set_mode) (struct regulator_dev *, unsigned int mode);
    unsigned int (*get_mode) (struct regulator_dev *);
    int (*get_error_flags)(struct regulator_dev *, unsigned int *flags);
    int (*enable_time) (struct regulator_dev *);
    int (*set_ramp_delay) (struct regulator_dev *, int ramp_delay);
    int (*set_voltage_time) (struct regulator_dev *, int old_uV, int new_uV);
    int (*set_voltage_time_sel) (struct regulator_dev *,unsigned int old_selector, unsigned int new_selector);
    int (*set_soft_start) (struct regulator_dev *);
    int (*get_status)(struct regulator_dev *);
    unsigned int (*get_optimum_mode) (struct regulator_dev *, int input_uV, int output_uV, int load_uA);
    int (*set_load)(struct regulator_dev *, int load_uA);
    int (*set_bypass)(struct regulator_dev *dev, bool enable);
    int (*get_bypass)(struct regulator_dev *dev, bool *enable);
    int (*set_suspend_voltage) (struct regulator_dev *, int uV);
    int (*set_suspend_enable) (struct regulator_dev *);
    int (*set_suspend_disable) (struct regulator_dev *);
    int (*set_suspend_mode) (struct regulator_dev *, unsigned int mode);
    int (*resume)(struct regulator_dev *rdev);
    int (*set_pull_down) (struct regulator_dev *);
};
```

**Members**

`list_voltage`
:   Return one of the supported voltages, in microvolts; zero
    if the selector indicates a voltage that is unusable on this system;
    or negative errno. Selectors range from zero to one less than
    regulator_desc.n_voltages. Voltages may be reported in any order.

`set_voltage`
:   Set the voltage for the regulator within the range specified.
    The driver should select the voltage closest to min_uV.

`map_voltage`
:   Convert a voltage into a selector

`set_voltage_sel`
:   Set the voltage for the regulator using the specified
    selector.

`get_voltage`
:   Return the currently configured voltage for the regulator;
    return -ENOTRECOVERABLE if regulator can't be read at
    bootup and hasn't been set yet.

`get_voltage_sel`
:   Return the currently configured voltage selector for the
    regulator; return -ENOTRECOVERABLE if regulator can't
    be read at bootup and hasn't been set yet.

`set_current_limit`
:   Configure a limit for a current-limited regulator.
    The driver should select the current closest to max_uA.

`get_current_limit`
:   Get the configured limit for a current-limited regulator.

`set_input_current_limit`
:   Configure an input limit.

`set_over_current_protection`
:   Support enabling of and setting limits for over
    current situation detection. Detection can be configured for three
    levels of severity.

    - REGULATOR_SEVERITY_PROT should automatically shut down the regulator(s).
    - REGULATOR_SEVERITY_ERR should indicate that over-current situation is
      :   caused by an unrecoverable error but HW does not perform
          automatic shut down.
    - REGULATOR_SEVERITY_WARN should indicate situation where hardware is
      :   still believed to not be damaged but that a board sepcific
          recovery action is needed. If lim_uA is 0 the limit should not
          be changed but the detection should just be enabled/disabled as
          is requested.

`set_over_voltage_protection`
:   Support enabling of and setting limits for over
    voltage situation detection. Detection can be configured for same
    severities as over current protection. Units of uV.

`set_under_voltage_protection`
:   Support enabling of and setting limits for
    under voltage situation detection. Detection can be configured for same
    severities as over current protection. Units of uV.

`set_thermal_protection`
:   Support enabling of and setting limits for over
    temperature situation detection.Detection can be configured for same
    severities as over current protection. Units of degree Kelvin.

`set_active_discharge`
:   Set active discharge enable/disable of regulators.

`enable`
:   Configure the regulator as enabled.

`disable`
:   Configure the regulator as disabled.

`is_enabled`
:   Return 1 if the regulator is enabled, 0 if not.
    May also return negative errno.

`set_mode`
:   Set the configured operating mode for the regulator.

`get_mode`
:   Get the configured operating mode for the regulator.

`get_error_flags`
:   Get the current error(s) for the regulator.

`enable_time`
:   Time taken for the regulator voltage output voltage to
    stabilise after being enabled, in microseconds.

`set_ramp_delay`
:   Set the ramp delay for the regulator. The driver should
    select ramp delay equal to or less than(closest) ramp_delay.

`set_voltage_time`
:   Time taken for the regulator voltage output voltage
    to stabilise after being set to a new value, in microseconds.
    The function receives the from and to voltage as input, it
    should return the worst case.

`set_voltage_time_sel`
:   Time taken for the regulator voltage output voltage
    to stabilise after being set to a new value, in microseconds.
    The function receives the from and to voltage selector as
    input, it should return the worst case.

`set_soft_start`
:   Enable soft start for the regulator.

`get_status`
:   Return actual (not as-configured) status of regulator, as a
    REGULATOR_STATUS value (or negative errno)

`get_optimum_mode`
:   Get the most efficient operating mode for the regulator
    when running with the specified parameters.

`set_load`
:   Set the load for the regulator.

`set_bypass`
:   Set the regulator in bypass mode.

`get_bypass`
:   Get the regulator bypass mode state.

`set_suspend_voltage`
:   Set the voltage for the regulator when the system
    is suspended.

`set_suspend_enable`
:   Mark the regulator as enabled when the system is
    suspended.

`set_suspend_disable`
:   Mark the regulator as disabled when the system is
    suspended.

`set_suspend_mode`
:   Set the operating mode for the regulator when the
    system is suspended.

`resume`
:   Resume operation of suspended regulator.

`set_pull_down`
:   Configure the regulator to pull down when the regulator
    is disabled.

**Description**

This struct describes regulator operations which can be implemented by
regulator chip drivers.

struct regulator_desc
:   Static regulator descriptor

**Definition**:

```
struct regulator_desc {
    const char *name;
    const char *supply_name;
    const char *of_match;
    bool of_match_full_name;
    const char *regulators_node;
    int (*of_parse_cb)(struct device_node *,const struct regulator_desc *, struct regulator_config *);
    int id;
    unsigned int continuous_voltage_range:1;
    unsigned n_voltages;
    unsigned int n_current_limits;
    const struct regulator_ops *ops;
    int irq;
    enum regulator_type type;
    struct module *owner;
    unsigned int min_uV;
    unsigned int uV_step;
    unsigned int linear_min_sel;
    int fixed_uV;
    unsigned int ramp_delay;
    int min_dropout_uV;
    const struct linear_range *linear_ranges;
    const unsigned int *linear_range_selectors_bitfield;
    int n_linear_ranges;
    const unsigned int *volt_table;
    const unsigned int *curr_table;
    unsigned int vsel_range_reg;
    unsigned int vsel_range_mask;
    unsigned int vsel_reg;
    unsigned int vsel_mask;
    unsigned int vsel_step;
    unsigned int csel_reg;
    unsigned int csel_mask;
    unsigned int apply_reg;
    unsigned int apply_bit;
    unsigned int enable_reg;
    unsigned int enable_mask;
    unsigned int enable_val;
    unsigned int disable_val;
    bool enable_is_inverted;
    unsigned int bypass_reg;
    unsigned int bypass_mask;
    unsigned int bypass_val_on;
    unsigned int bypass_val_off;
    unsigned int active_discharge_on;
    unsigned int active_discharge_off;
    unsigned int active_discharge_mask;
    unsigned int active_discharge_reg;
    unsigned int soft_start_reg;
    unsigned int soft_start_mask;
    unsigned int soft_start_val_on;
    unsigned int pull_down_reg;
    unsigned int pull_down_mask;
    unsigned int pull_down_val_on;
    unsigned int ramp_reg;
    unsigned int ramp_mask;
    const unsigned int *ramp_delay_table;
    unsigned int n_ramp_values;
    unsigned int enable_time;
    unsigned int off_on_delay;
    unsigned int poll_enabled_time;
    unsigned int (*of_map_mode)(unsigned int mode);
};
```

**Members**

`name`
:   Identifying name for the regulator.

`supply_name`
:   Identifying the regulator supply

`of_match`
:   Name used to identify regulator in DT.

`of_match_full_name`
:   A flag to indicate that the of_match string, if
    present, should be matched against the node full_name.

`regulators_node`
:   Name of node containing regulator definitions in DT.

`of_parse_cb`
:   Optional callback called only if of_match is present.
    Will be called for each regulator parsed from DT, during
    init_data parsing.
    The regulator_config passed as argument to the callback will
    be a copy of config passed to regulator_register, valid only
    for this particular call. Callback may freely change the
    config but it cannot store it for later usage.
    Callback should return 0 on success or negative ERRNO
    indicating failure.

`id`
:   Numerical identifier for the regulator.

`continuous_voltage_range`
:   Indicates if the regulator can set any
    voltage within constrains range.

`n_voltages`
:   Number of selectors available for ops.list_voltage().

`n_current_limits`
:   Number of selectors available for current limits

`ops`
:   Regulator operations table.

`irq`
:   Interrupt number for the regulator.

`type`
:   Indicates if the regulator is a voltage or current regulator.

`owner`
:   Module providing the regulator, used for refcounting.

`min_uV`
:   Voltage given by the lowest selector (if linear mapping)

`uV_step`
:   Voltage increase with each selector (if linear mapping)

`linear_min_sel`
:   Minimal selector for starting linear mapping

`fixed_uV`
:   Fixed voltage of rails.

`ramp_delay`
:   Time to settle down after voltage change (unit: uV/us)

`min_dropout_uV`
:   The minimum dropout voltage this regulator can handle

`linear_ranges`
:   A constant table of possible voltage ranges.

`linear_range_selectors_bitfield`
:   A constant table of voltage range
    selectors as bitfield values. If
    pickable ranges are used each range
    must have corresponding selector here.

`n_linear_ranges`
:   Number of entries in the **linear_ranges** (and in
    linear_range_selectors_bitfield if used) table(s).

`volt_table`
:   Voltage mapping table (if table based mapping)

`curr_table`
:   Current limit mapping table (if table based mapping)

`vsel_range_reg`
:   Register for range selector when using pickable ranges
    and `regulator_map_*_voltage_*_pickable` functions.

`vsel_range_mask`
:   Mask for register bitfield used for range selector

`vsel_reg`
:   Register for selector when using `regulator_map_*_voltage_*`

`vsel_mask`
:   Mask for register bitfield used for selector

`vsel_step`
:   Specify the resolution of selector stepping when setting
    voltage. If 0, then no stepping is done (requested selector is
    set directly), if >0 then the regulator API will ramp the
    voltage up/down gradually each time increasing/decreasing the
    selector by the specified step value.

`csel_reg`
:   Register for current limit selector using regmap set_current_limit

`csel_mask`
:   Mask for register bitfield used for current limit selector

`apply_reg`
:   Register for initiate voltage change on the output when
    using regulator_set_voltage_sel_regmap

`apply_bit`
:   Register bitfield used for initiate voltage change on the
    output when using regulator_set_voltage_sel_regmap

`enable_reg`
:   Register for control when using regmap enable/disable ops

`enable_mask`
:   Mask for control when using regmap enable/disable ops

`enable_val`
:   Enabling value for control when using regmap enable/disable ops

`disable_val`
:   Disabling value for control when using regmap enable/disable ops

`enable_is_inverted`
:   A flag to indicate set enable_mask bits to disable
    when using regulator_enable_regmap and friends APIs.

`bypass_reg`
:   Register for control when using regmap set_bypass

`bypass_mask`
:   Mask for control when using regmap set_bypass

`bypass_val_on`
:   Enabling value for control when using regmap set_bypass

`bypass_val_off`
:   Disabling value for control when using regmap set_bypass

`active_discharge_on`
:   Disabling value for control when using regmap
    set_active_discharge

`active_discharge_off`
:   Enabling value for control when using regmap
    set_active_discharge

`active_discharge_mask`
:   Mask for control when using regmap
    set_active_discharge

`active_discharge_reg`
:   Register for control when using regmap
    set_active_discharge

`soft_start_reg`
:   Register for control when using regmap set_soft_start

`soft_start_mask`
:   Mask for control when using regmap set_soft_start

`soft_start_val_on`
:   Enabling value for control when using regmap
    set_soft_start

`pull_down_reg`
:   Register for control when using regmap set_pull_down

`pull_down_mask`
:   Mask for control when using regmap set_pull_down

`pull_down_val_on`
:   Enabling value for control when using regmap
    set_pull_down

`ramp_reg`
:   Register for controlling the regulator ramp-rate.

`ramp_mask`
:   Bitmask for the ramp-rate control register.

`ramp_delay_table`
:   Table for mapping the regulator ramp-rate values. Values
    should be given in units of V/S (uV/uS). See the
    regulator_set_ramp_delay_regmap().

`n_ramp_values`
:   number of elements at **ramp_delay_table**.

`enable_time`
:   Time taken for initial enable of regulator (in uS).

`off_on_delay`
:   guard time (in uS), before re-enabling a regulator

`poll_enabled_time`
:   The polling interval (in uS) to use while checking that
    the regulator was actually enabled. Max upto enable_time.

`of_map_mode`
:   Maps a hardware mode defined in a DeviceTree to a standard mode

**Description**

Each regulator registered with the core is described with a
structure of this type and a [`struct regulator_config`](regulator.md#c.regulator_config "regulator_config"). This
structure contains the non-varying parts of the regulator
description.

struct regulator_config
:   Dynamic regulator descriptor

**Definition**:

```
struct regulator_config {
    struct device *dev;
    const struct regulator_init_data *init_data;
    void *driver_data;
    struct device_node *of_node;
    struct regmap *regmap;
    struct gpio_desc *ena_gpiod;
};
```

**Members**

`dev`
:   [`struct device`](infrastructure.md#c.device "device") for the regulator

`init_data`
:   platform provided init data, passed through by driver

`driver_data`
:   private regulator data

`of_node`
:   OpenFirmware node to parse for device tree bindings (may be
    NULL).

`regmap`
:   regmap to use for core regmap helpers if dev_get_regmap() is
    insufficient.

`ena_gpiod`
:   GPIO controlling regulator enable.

**Description**

Each regulator registered with the core is described with a
structure of this type and a [`struct regulator_desc`](regulator.md#c.regulator_desc "regulator_desc"). This structure
contains the runtime variable parts of the regulator description.

struct regulator_err_state
:   regulator error/notification status

**Definition**:

```
struct regulator_err_state {
    struct regulator_dev *rdev;
    unsigned long notifs;
    unsigned long errors;
    int possible_errs;
};
```

**Members**

`rdev`
:   Regulator which status the struct indicates.

`notifs`
:   Events which have occurred on the regulator.

`errors`
:   Errors which are active on the regulator.

`possible_errs`
:   Errors which can be signaled (by given IRQ).

struct regulator_irq_data
:   regulator error/notification status data

**Definition**:

```
struct regulator_irq_data {
    struct regulator_err_state *states;
    int num_states;
    void *data;
    long opaque;
};
```

**Members**

`states`
:   Status structs for each of the associated regulators.

`num_states`
:   Amount of associated regulators.

`data`
:   Driver data pointer given at regulator_irq_desc.

`opaque`
:   Value storage for IC driver. Core does not update this. ICs
    may want to store status register value here at map_event and
    compare contents at 'renable' callback to see if new problems
    have been added to status. If that is the case it may be
    desirable to return REGULATOR_ERROR_CLEARED and not
    REGULATOR_ERROR_ON to allow IRQ fire again and to generate
    notifications also for the new issues.

**Description**

This structure is passed to 'map_event' and 'renable' callbacks for
reporting regulator status to core.

struct regulator_irq_desc
:   notification sender for IRQ based events.

**Definition**:

```
struct regulator_irq_desc {
    const char *name;
    int fatal_cnt;
    int reread_ms;
    int irq_off_ms;
    bool skip_off;
    bool high_prio;
    void *data;
    int (*die)(struct regulator_irq_data *rid);
    int (*map_event)(int irq, struct regulator_irq_data *rid, unsigned long *dev_mask);
    int (*renable)(struct regulator_irq_data *rid);
};
```

**Members**

`name`
:   The visible name for the IRQ

`fatal_cnt`
:   If this IRQ is used to signal HW damaging condition it may be
    best to shut-down regulator(s) or reboot the SOC if error
    handling is repeatedly failing. If fatal_cnt is given the IRQ
    handling is aborted if it fails for fatal_cnt times and die()
    callback (if populated) is called. If die() is not populated
    poweroff for the system is attempted in order to prevent any
    further damage.

`reread_ms`
:   The time which is waited before attempting to re-read status
    at the worker if IC reading fails. Immediate re-read is done
    if time is not specified.

`irq_off_ms`
:   The time which IRQ is kept disabled before re-evaluating the
    status for devices which keep IRQ disabled for duration of the
    error. If this is not given the IRQ is left enabled and renable
    is not called.

`skip_off`
:   If set to true the IRQ handler will attempt to check if any of
    the associated regulators are enabled prior to taking other
    actions. If no regulators are enabled and this is set to true
    a spurious IRQ is assumed and IRQ_NONE is returned.

`high_prio`
:   Boolean to indicate that high priority WQ should be used.

`data`
:   Driver private data pointer which will be passed as such to
    the renable, map_event and die callbacks in regulator_irq_data.

`die`
:   Protection callback. If IC status reading or recovery actions
    fail fatal_cnt times this callback is called or system is
    powered off. This callback should implement a final protection
    attempt like disabling the regulator. If protection succeeded
    die() may return 0. If anything else is returned the core
    assumes final protection failed and attempts to perform a
    poweroff as a last resort.

`map_event`
:   Driver callback to map IRQ status into regulator devices with
    events / errors. NOTE: callback MUST initialize both the
    errors and notifs for all rdevs which it signals having
    active events as core does not clean the map data.
    REGULATOR_FAILED_RETRY can be returned to indicate that the
    status reading from IC failed. If this is repeated for
    fatal_cnt times the core will call die() callback or power-off
    the system as a last resort to protect the HW.

`renable`
:   Optional callback to check status (if HW supports that) before
    re-enabling IRQ. If implemented this should clear the error
    flags so that errors fetched by [`regulator_get_error_flags()`](regulator.md#c.regulator_get_error_flags "regulator_get_error_flags")
    are updated. If callback is not implemented then errors are
    assumed to be cleared and IRQ is re-enabled.
    REGULATOR_FAILED_RETRY can be returned to
    indicate that the status reading from IC failed. If this is
    repeated for 'fatal_cnt' times the core will call die()
    callback or if die() is not populated then attempt to power-off
    the system as a last resort to protect the HW.
    Returning zero indicates that the problem in HW has been solved
    and IRQ will be re-enabled. Returning REGULATOR_ERROR_ON
    indicates the error condition is still active and keeps IRQ
    disabled. Please note that returning REGULATOR_ERROR_ON does
    not retrigger evaluating what events are active or resending
    notifications. If this is needed you probably want to return
    zero and allow IRQ to retrigger causing events to be
    re-evaluated and re-sent.

**Description**

This structure is used for registering regulator IRQ notification helper.

struct regulator \*regulator_get(struct [device](infrastructure.md#c.device "device") \*dev, const char \*id)
:   lookup and obtain a reference to a regulator.

**Parameters**

`struct device *dev`
:   device for regulator "consumer"

`const char *id`
:   Supply name or regulator ID.

**Description**

Returns a struct regulator corresponding to the regulator producer,
or [`IS_ERR()`](../core-api/kernel-api.md#c.IS_ERR "IS_ERR") condition containing errno.

Use of supply names configured via set_consumer_device_supply() is
strongly encouraged. It is recommended that the supply name used
should match the name used for the supply and/or the relevant
device pins in the datasheet.

struct regulator \*regulator_get_exclusive(struct [device](infrastructure.md#c.device "device") \*dev, const char \*id)
:   obtain exclusive access to a regulator.

**Parameters**

`struct device *dev`
:   device for regulator "consumer"

`const char *id`
:   Supply name or regulator ID.

**Description**

Returns a struct regulator corresponding to the regulator producer,
or [`IS_ERR()`](../core-api/kernel-api.md#c.IS_ERR "IS_ERR") condition containing errno. Other consumers will be
unable to obtain this regulator while this reference is held and the
use count for the regulator will be initialised to reflect the current
state of the regulator.

This is intended for use by consumers which cannot tolerate shared
use of the regulator such as those which need to force the
regulator off for correct operation of the hardware they are
controlling.

Use of supply names configured via set_consumer_device_supply() is
strongly encouraged. It is recommended that the supply name used
should match the name used for the supply and/or the relevant
device pins in the datasheet.

struct regulator \*regulator_get_optional(struct [device](infrastructure.md#c.device "device") \*dev, const char \*id)
:   obtain optional access to a regulator.

**Parameters**

`struct device *dev`
:   device for regulator "consumer"

`const char *id`
:   Supply name or regulator ID.

**Description**

Returns a struct regulator corresponding to the regulator producer,
or [`IS_ERR()`](../core-api/kernel-api.md#c.IS_ERR "IS_ERR") condition containing errno.

This is intended for use by consumers for devices which can have
some supplies unconnected in normal use, such as some MMC devices.
It can allow the regulator core to provide stub supplies for other
supplies requested using normal [`regulator_get()`](regulator.md#c.regulator_get "regulator_get") calls without
disrupting the operation of drivers that can handle absent
supplies.

Use of supply names configured via set_consumer_device_supply() is
strongly encouraged. It is recommended that the supply name used
should match the name used for the supply and/or the relevant
device pins in the datasheet.

void regulator_put(struct [regulator](regulator.md#c.regulator_put "regulator") \*regulator)
:   "free" the regulator source

**Parameters**

`struct regulator *regulator`
:   regulator source

**Note**

drivers must ensure that all regulator_enable calls made on this
regulator source are balanced by regulator_disable calls prior to calling
this function.

int regulator_register_supply_alias(struct [device](infrastructure.md#c.device "device") \*dev, const char \*id, struct [device](infrastructure.md#c.device "device") \*alias_dev, const char \*alias_id)
:   Provide device alias for supply lookup

**Parameters**

`struct device *dev`
:   device that will be given as the regulator "consumer"

`const char *id`
:   Supply name or regulator ID

`struct device *alias_dev`
:   device that should be used to lookup the supply

`const char *alias_id`
:   Supply name or regulator ID that should be used to lookup the
    supply

**Description**

All lookups for id on dev will instead be conducted for alias_id on
alias_dev.

void regulator_unregister_supply_alias(struct [device](infrastructure.md#c.device "device") \*dev, const char \*id)
:   Remove device alias

**Parameters**

`struct device *dev`
:   device that will be given as the regulator "consumer"

`const char *id`
:   Supply name or regulator ID

**Description**

Remove a lookup alias if one exists for id on dev.

int regulator_bulk_register_supply_alias(struct [device](infrastructure.md#c.device "device") \*dev, const char \*const \*id, struct [device](infrastructure.md#c.device "device") \*alias_dev, const char \*const \*alias_id, int num_id)
:   register multiple aliases

**Parameters**

`struct device *dev`
:   device that will be given as the regulator "consumer"

`const char *const *id`
:   List of supply names or regulator IDs

`struct device *alias_dev`
:   device that should be used to lookup the supply

`const char *const *alias_id`
:   List of supply names or regulator IDs that should be used to
    lookup the supply

`int num_id`
:   Number of aliases to register

**Description**

**return** 0 on success, an errno on failure.

This helper function allows drivers to register several supply
aliases in one operation. If any of the aliases cannot be
registered any aliases that were registered will be removed
before returning to the caller.

void regulator_bulk_unregister_supply_alias(struct [device](infrastructure.md#c.device "device") \*dev, const char \*const \*id, int num_id)
:   unregister multiple aliases

**Parameters**

`struct device *dev`
:   device that will be given as the regulator "consumer"

`const char *const *id`
:   List of supply names or regulator IDs

`int num_id`
:   Number of aliases to unregister

**Description**

This helper function allows drivers to unregister several supply
aliases in one operation.

int regulator_enable(struct [regulator](regulator.md#c.regulator_enable "regulator") \*regulator)
:   enable regulator output

**Parameters**

`struct regulator *regulator`
:   regulator source

**Description**

Request that the regulator be enabled with the regulator output at
the predefined voltage or current value. Calls to [`regulator_enable()`](regulator.md#c.regulator_enable "regulator_enable")
must be balanced with calls to [`regulator_disable()`](regulator.md#c.regulator_disable "regulator_disable").

**NOTE**

the output value can be set by other drivers, boot loader or may be
hardwired in the regulator.

int regulator_disable(struct [regulator](regulator.md#c.regulator_disable "regulator") \*regulator)
:   disable regulator output

**Parameters**

`struct regulator *regulator`
:   regulator source

**Description**

Disable the regulator output voltage or current. Calls to
[`regulator_enable()`](regulator.md#c.regulator_enable "regulator_enable") must be balanced with calls to
[`regulator_disable()`](regulator.md#c.regulator_disable "regulator_disable").

**NOTE**

this will only disable the regulator output if no other consumer
devices have it enabled, the regulator device supports disabling and
machine constraints permit this operation.

int regulator_force_disable(struct [regulator](regulator.md#c.regulator_force_disable "regulator") \*regulator)
:   force disable regulator output

**Parameters**

`struct regulator *regulator`
:   regulator source

**Description**

Forcibly disable the regulator output voltage or current.

**NOTE**

this *will* disable the regulator output even if other consumer
devices have it enabled. This should be used for situations when device
damage will likely occur if the regulator is not disabled (e.g. over temp).

int regulator_disable_deferred(struct [regulator](regulator.md#c.regulator_disable_deferred "regulator") \*regulator, int ms)
:   disable regulator output with delay

**Parameters**

`struct regulator *regulator`
:   regulator source

`int ms`
:   milliseconds until the regulator is disabled

**Description**

Execute [`regulator_disable()`](regulator.md#c.regulator_disable "regulator_disable") on the regulator after a delay. This
is intended for use with devices that require some time to quiesce.

**NOTE**

this will only disable the regulator output if no other consumer
devices have it enabled, the regulator device supports disabling and
machine constraints permit this operation.

int regulator_is_enabled(struct [regulator](regulator.md#c.regulator_is_enabled "regulator") \*regulator)
:   is the regulator output enabled

**Parameters**

`struct regulator *regulator`
:   regulator source

**Description**

Returns positive if the regulator driver backing the source/client
has requested that the device be enabled, zero if it hasn't, else a
negative errno code.

Note that the device backing this regulator handle can have multiple
users, so it might be enabled even if [`regulator_enable()`](regulator.md#c.regulator_enable "regulator_enable") was never
called for this particular source.

int regulator_count_voltages(struct [regulator](regulator.md#c.regulator_count_voltages "regulator") \*regulator)
:   count [`regulator_list_voltage()`](regulator.md#c.regulator_list_voltage "regulator_list_voltage") selectors

**Parameters**

`struct regulator *regulator`
:   regulator source

**Description**

Returns number of selectors, or negative errno. Selectors are
numbered starting at zero, and typically correspond to bitfields
in hardware registers.

int regulator_list_voltage(struct [regulator](regulator.md#c.regulator_list_voltage "regulator") \*regulator, unsigned selector)
:   enumerate supported voltages

**Parameters**

`struct regulator *regulator`
:   regulator source

`unsigned selector`
:   identify voltage to list

**Context**

can sleep

**Description**

Returns a voltage that can be passed to **[`regulator_set_voltage()`](regulator.md#c.regulator_set_voltage "regulator_set_voltage")**,
zero if this selector code can't be used on this system, or a
negative errno.

int regulator_get_hardware_vsel_register(struct [regulator](regulator.md#c.regulator_get_hardware_vsel_register "regulator") \*regulator, unsigned \*vsel_reg, unsigned \*vsel_mask)
:   get the HW voltage selector register

**Parameters**

`struct regulator *regulator`
:   regulator source

`unsigned *vsel_reg`
:   voltage selector register, output parameter

`unsigned *vsel_mask`
:   mask for voltage selector bitfield, output parameter

**Description**

Returns the hardware register offset and bitmask used for setting the
regulator voltage. This might be useful when configuring voltage-scaling
hardware or firmware that can make I2C requests behind the kernel's back,
for example.

On success, the output parameters **vsel_reg** and **vsel_mask** are filled in
and 0 is returned, otherwise a negative errno is returned.

int regulator_list_hardware_vsel(struct [regulator](regulator.md#c.regulator_list_hardware_vsel "regulator") \*regulator, unsigned selector)
:   get the HW-specific register value for a selector

**Parameters**

`struct regulator *regulator`
:   regulator source

`unsigned selector`
:   identify voltage to list

**Description**

Converts the selector to a hardware-specific voltage selector that can be
directly written to the regulator registers. The address of the voltage
register can be determined by calling **regulator_get_hardware_vsel_register**.

On error a negative errno is returned.

unsigned int regulator_get_linear_step(struct [regulator](regulator.md#c.regulator_get_linear_step "regulator") \*regulator)
:   return the voltage step size between VSEL values

**Parameters**

`struct regulator *regulator`
:   regulator source

**Description**

Returns the voltage step size between VSEL values for linear
regulators, or return 0 if the regulator isn't a linear regulator.

int regulator_is_supported_voltage(struct [regulator](regulator.md#c.regulator_is_supported_voltage "regulator") \*regulator, int min_uV, int max_uV)
:   check if a voltage range can be supported

**Parameters**

`struct regulator *regulator`
:   Regulator to check.

`int min_uV`
:   Minimum required voltage in uV.

`int max_uV`
:   Maximum required voltage in uV.

**Description**

Returns a boolean.

int regulator_set_voltage(struct [regulator](regulator.md#c.regulator_set_voltage "regulator") \*regulator, int min_uV, int max_uV)
:   set regulator output voltage

**Parameters**

`struct regulator *regulator`
:   regulator source

`int min_uV`
:   Minimum required voltage in uV

`int max_uV`
:   Maximum acceptable voltage in uV

**Description**

Sets a voltage regulator to the desired output voltage. This can be set
during any regulator state. IOW, regulator can be disabled or enabled.

If the regulator is enabled then the voltage will change to the new value
immediately otherwise if the regulator is disabled the regulator will
output at the new voltage when enabled.

**NOTE**

If the regulator is shared between several devices then the lowest
request voltage that meets the system constraints will be used.
Regulator system constraints must be set for this regulator before
calling this function otherwise this call will fail.

int regulator_set_voltage_time(struct [regulator](regulator.md#c.regulator_set_voltage_time "regulator") \*regulator, int old_uV, int new_uV)
:   get raise/fall time

**Parameters**

`struct regulator *regulator`
:   regulator source

`int old_uV`
:   starting voltage in microvolts

`int new_uV`
:   target voltage in microvolts

**Description**

Provided with the starting and ending voltage, this function attempts to
calculate the time in microseconds required to rise or fall to this new
voltage.

int regulator_set_voltage_time_sel(struct regulator_dev \*rdev, unsigned int old_selector, unsigned int new_selector)
:   get raise/fall time

**Parameters**

`struct regulator_dev *rdev`
:   regulator source device

`unsigned int old_selector`
:   selector for starting voltage

`unsigned int new_selector`
:   selector for target voltage

**Description**

Provided with the starting and target voltage selectors, this function
returns time in microseconds required to rise or fall to this new voltage

Drivers providing ramp_delay in regulation_constraints can use this as their
set_voltage_time_sel() operation.

int regulator_sync_voltage(struct [regulator](regulator.md#c.regulator_sync_voltage "regulator") \*regulator)
:   re-apply last regulator output voltage

**Parameters**

`struct regulator *regulator`
:   regulator source

**Description**

Re-apply the last configured voltage. This is intended to be used
where some external control source the consumer is cooperating with
has caused the configured voltage to change.

int regulator_get_voltage(struct [regulator](regulator.md#c.regulator_get_voltage "regulator") \*regulator)
:   get regulator output voltage

**Parameters**

`struct regulator *regulator`
:   regulator source

**Description**

This returns the current regulator voltage in uV.

**NOTE**

If the regulator is disabled it will return the voltage value. This
function should not be used to determine regulator state.

int regulator_set_current_limit(struct [regulator](regulator.md#c.regulator_set_current_limit "regulator") \*regulator, int min_uA, int max_uA)
:   set regulator output current limit

**Parameters**

`struct regulator *regulator`
:   regulator source

`int min_uA`
:   Minimum supported current in uA

`int max_uA`
:   Maximum supported current in uA

**Description**

Sets current sink to the desired output current. This can be set during
any regulator state. IOW, regulator can be disabled or enabled.

If the regulator is enabled then the current will change to the new value
immediately otherwise if the regulator is disabled the regulator will
output at the new current when enabled.

**NOTE**

Regulator system constraints must be set for this regulator before
calling this function otherwise this call will fail.

int regulator_get_current_limit(struct [regulator](regulator.md#c.regulator_get_current_limit "regulator") \*regulator)
:   get regulator output current

**Parameters**

`struct regulator *regulator`
:   regulator source

**Description**

This returns the current supplied by the specified current sink in uA.

**NOTE**

If the regulator is disabled it will return the current value. This
function should not be used to determine regulator state.

int regulator_set_mode(struct [regulator](regulator.md#c.regulator_set_mode "regulator") \*regulator, unsigned int mode)
:   set regulator operating mode

**Parameters**

`struct regulator *regulator`
:   regulator source

`unsigned int mode`
:   operating mode - one of the REGULATOR_MODE constants

**Description**

Set regulator operating mode to increase regulator efficiency or improve
regulation performance.

**NOTE**

Regulator system constraints must be set for this regulator before
calling this function otherwise this call will fail.

unsigned int regulator_get_mode(struct [regulator](regulator.md#c.regulator_get_mode "regulator") \*regulator)
:   get regulator operating mode

**Parameters**

`struct regulator *regulator`
:   regulator source

**Description**

Get the current regulator operating mode.

int regulator_get_error_flags(struct [regulator](regulator.md#c.regulator_get_error_flags "regulator") \*regulator, unsigned int \*flags)
:   get regulator error information

**Parameters**

`struct regulator *regulator`
:   regulator source

`unsigned int *flags`
:   pointer to store error flags

**Description**

Get the current regulator error information.

int regulator_set_load(struct [regulator](regulator.md#c.regulator_set_load "regulator") \*regulator, int uA_load)
:   set regulator load

**Parameters**

`struct regulator *regulator`
:   regulator source

`int uA_load`
:   load current

**Description**

Notifies the regulator core of a new device load. This is then used by
DRMS (if enabled by constraints) to set the most efficient regulator
operating mode for the new regulator loading.

Consumer devices notify their supply regulator of the maximum power
they will require (can be taken from device datasheet in the power
consumption tables) when they change operational status and hence power
state. Examples of operational state changes that can affect power
consumption are :-

> o Device is opened / closed.
> o Device I/O is about to begin or has just finished.
> o Device is idling in between work.

This information is also exported via sysfs to userspace.

DRMS will sum the total requested load on the regulator and change
to the most efficient operating mode if platform constraints allow.

If a regulator is an always-on regulator then an individual consumer's
load will still be removed if that consumer is fully disabled.

On error a negative errno is returned.

**NOTE**

when a regulator consumer requests to have a regulator
disabled then any load that consumer requested no longer counts
toward the total requested load. If the regulator is re-enabled
then the previously requested load will start counting again.

int regulator_allow_bypass(struct [regulator](regulator.md#c.regulator_allow_bypass "regulator") \*regulator, bool enable)
:   allow the regulator to go into bypass mode

**Parameters**

`struct regulator *regulator`
:   Regulator to configure

`bool enable`
:   enable or disable bypass mode

**Description**

Allow the regulator to go into bypass mode if all other consumers
for the regulator also enable bypass mode and the machine
constraints allow this. Bypass mode means that the regulator is
simply passing the input directly to the output with no regulation.

int regulator_register_notifier(struct [regulator](regulator.md#c.regulator_register_notifier "regulator") \*regulator, struct notifier_block \*nb)
:   register regulator event notifier

**Parameters**

`struct regulator *regulator`
:   regulator source

`struct notifier_block *nb`
:   notifier block

**Description**

Register notifier block to receive regulator events.

int regulator_unregister_notifier(struct [regulator](regulator.md#c.regulator_unregister_notifier "regulator") \*regulator, struct notifier_block \*nb)
:   unregister regulator event notifier

**Parameters**

`struct regulator *regulator`
:   regulator source

`struct notifier_block *nb`
:   notifier block

**Description**

Unregister regulator event notifier block.

int regulator_bulk_get(struct [device](infrastructure.md#c.device "device") \*dev, int num_consumers, struct [regulator_bulk_data](regulator.md#c.regulator_bulk_data "regulator_bulk_data") \*consumers)
:   get multiple regulator consumers

**Parameters**

`struct device *dev`
:   Device to supply

`int num_consumers`
:   Number of consumers to register

`struct regulator_bulk_data *consumers`
:   Configuration of consumers; clients are stored here.

**Description**

**return** 0 on success, an errno on failure.

This helper function allows drivers to get several regulator
consumers in one operation. If any of the regulators cannot be
acquired then any regulators that were allocated will be freed
before returning to the caller.

int regulator_bulk_enable(int num_consumers, struct [regulator_bulk_data](regulator.md#c.regulator_bulk_data "regulator_bulk_data") \*consumers)
:   enable multiple regulator consumers

**Parameters**

`int num_consumers`
:   Number of consumers

`struct regulator_bulk_data *consumers`
:   Consumer data; clients are stored here.
    **return** 0 on success, an errno on failure

**Description**

This convenience API allows consumers to enable multiple regulator
clients in a single API call. If any consumers cannot be enabled
then any others that were enabled will be disabled again prior to
return.

int regulator_bulk_disable(int num_consumers, struct [regulator_bulk_data](regulator.md#c.regulator_bulk_data "regulator_bulk_data") \*consumers)
:   disable multiple regulator consumers

**Parameters**

`int num_consumers`
:   Number of consumers

`struct regulator_bulk_data *consumers`
:   Consumer data; clients are stored here.
    **return** 0 on success, an errno on failure

**Description**

This convenience API allows consumers to disable multiple regulator
clients in a single API call. If any consumers cannot be disabled
then any others that were disabled will be enabled again prior to
return.

int regulator_bulk_force_disable(int num_consumers, struct [regulator_bulk_data](regulator.md#c.regulator_bulk_data "regulator_bulk_data") \*consumers)
:   force disable multiple regulator consumers

**Parameters**

`int num_consumers`
:   Number of consumers

`struct regulator_bulk_data *consumers`
:   Consumer data; clients are stored here.
    **return** 0 on success, an errno on failure

**Description**

This convenience API allows consumers to forcibly disable multiple regulator
clients in a single API call.

**NOTE**

This should be used for situations when device damage will
likely occur if the regulators are not disabled (e.g. over temp).
Although regulator_force_disable function call for some consumers can
return error numbers, the function is called for all consumers.

void regulator_bulk_free(int num_consumers, struct [regulator_bulk_data](regulator.md#c.regulator_bulk_data "regulator_bulk_data") \*consumers)
:   free multiple regulator consumers

**Parameters**

`int num_consumers`
:   Number of consumers

`struct regulator_bulk_data *consumers`
:   Consumer data; clients are stored here.

**Description**

This convenience API allows consumers to free multiple regulator
clients in a single API call.

int regulator_notifier_call_chain(struct regulator_dev \*rdev, unsigned long event, void \*data)
:   call regulator event notifier

**Parameters**

`struct regulator_dev *rdev`
:   regulator source

`unsigned long event`
:   notifier block

`void *data`
:   callback-specific data.

**Description**

Called by regulator drivers to notify clients a regulator event has
occurred.

int regulator_mode_to_status(unsigned int mode)
:   convert a regulator mode into a status

**Parameters**

`unsigned int mode`
:   Mode to convert

**Description**

Convert a regulator mode into a status.

struct regulator_dev \*regulator_register(struct [device](infrastructure.md#c.device "device") \*dev, const struct [regulator_desc](regulator.md#c.regulator_register "regulator_desc") \*regulator_desc, const struct [regulator_config](regulator.md#c.regulator_config "regulator_config") \*cfg)
:   register regulator

**Parameters**

`struct device *dev`
:   the device that drive the regulator

`const struct regulator_desc *regulator_desc`
:   regulator to register

`const struct regulator_config *cfg`
:   runtime configuration for regulator

**Description**

Called by regulator drivers to register a regulator.
Returns a valid pointer to struct regulator_dev on success
or an [`ERR_PTR()`](../core-api/kernel-api.md#c.ERR_PTR "ERR_PTR") on error.

void regulator_unregister(struct regulator_dev \*rdev)
:   unregister regulator

**Parameters**

`struct regulator_dev *rdev`
:   regulator to unregister

**Description**

Called by regulator drivers to unregister a regulator.

void regulator_has_full_constraints(void)
:   the system has fully specified constraints

**Parameters**

`void`
:   no arguments

**Description**

Calling this function will cause the regulator API to disable all
regulators which have a zero use count and don't have an always_on
constraint in a late_initcall.

The intention is that this will become the default behaviour in a
future kernel release so users are encouraged to use this facility
now.

void \*rdev_get_drvdata(struct regulator_dev \*rdev)
:   get rdev regulator driver data

**Parameters**

`struct regulator_dev *rdev`
:   regulator

**Description**

Get rdev regulator driver private data. This call can be used in the
regulator driver context.

void \*regulator_get_drvdata(struct [regulator](regulator.md#c.regulator_get_drvdata "regulator") \*regulator)
:   get regulator driver data

**Parameters**

`struct regulator *regulator`
:   regulator

**Description**

Get regulator driver private data. This call can be used in the consumer
driver context when non API regulator specific functions need to be called.

void regulator_set_drvdata(struct [regulator](regulator.md#c.regulator_set_drvdata "regulator") \*regulator, void \*data)
:   set regulator driver data

**Parameters**

`struct regulator *regulator`
:   regulator

`void *data`
:   data

int rdev_get_id(struct regulator_dev \*rdev)
:   get regulator ID

**Parameters**

`struct regulator_dev *rdev`
:   regulator
