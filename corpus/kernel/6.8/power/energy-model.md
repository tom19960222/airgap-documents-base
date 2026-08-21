---
collection: kernel
version: "6.8"
title: "Energy Model of devices"
source_url: https://www.kernel.org/doc/html/v6.8/power/energy-model.html
fetched_at: 2026-08-21T03:39:40+00:00
---
English

- [Chinese (Simplified)](../translations/zh_CN/power/energy-model.md)

# Energy Model of devices

## 1. Overview

The Energy Model (EM) framework serves as an interface between drivers knowing
the power consumed by devices at various performance levels, and the kernel
subsystems willing to use that information to make energy-aware decisions.

The source of the information about the power consumed by devices can vary greatly
from one platform to another. These power costs can be estimated using
devicetree data in some cases. In others, the firmware will know better.
Alternatively, userspace might be best positioned. And so on. In order to avoid
each and every client subsystem to re-implement support for each and every
possible source of information on its own, the EM framework intervenes as an
abstraction layer which standardizes the format of power cost tables in the
kernel, hence enabling to avoid redundant work.

The power values might be expressed in micro-Watts or in an 'abstract scale'.
Multiple subsystems might use the EM and it is up to the system integrator to
check that the requirements for the power value scale types are met. An example
can be found in the Energy-Aware Scheduler documentation
[Energy Aware Scheduling](../scheduler/sched-energy.md). For some subsystems like thermal or
powercap power values expressed in an 'abstract scale' might cause issues.
These subsystems are more interested in estimation of power used in the past,
thus the real micro-Watts might be needed. An example of these requirements can
be found in the Intelligent Power Allocation in
[Power allocator governor tunables](../driver-api/thermal/power_allocator.md).
Kernel subsystems might implement automatic detection to check whether EM
registered devices have inconsistent scale (based on EM internal flag).
Important thing to keep in mind is that when the power values are expressed in
an 'abstract scale' deriving real energy in micro-Joules would not be possible.

The figure below depicts an example of drivers (Arm-specific here, but the
approach is applicable to any architecture) providing power costs to the EM
framework, and interested clients reading the data from it:

```
+---------------+  +-----------------+  +---------------+
| Thermal (IPA) |  | Scheduler (EAS) |  |     Other     |
+---------------+  +-----------------+  +---------------+
        |                   | em_cpu_energy()   |
        |                   | em_cpu_get()      |
        +---------+         |         +---------+
                  |         |         |
                  v         v         v
                 +---------------------+
                 |    Energy Model     |
                 |     Framework       |
                 +---------------------+
                    ^       ^       ^
                    |       |       | em_dev_register_perf_domain()
         +----------+       |       +---------+
         |                  |                 |
 +---------------+  +---------------+  +--------------+
 |  cpufreq-dt   |  |   arm_scmi    |  |    Other     |
 +---------------+  +---------------+  +--------------+
         ^                  ^                 ^
         |                  |                 |
 +--------------+   +---------------+  +--------------+
 | Device Tree  |   |   Firmware    |  |      ?       |
 +--------------+   +---------------+  +--------------+
```

In case of CPU devices the EM framework manages power cost tables per
'performance domain' in the system. A performance domain is a group of CPUs
whose performance is scaled together. Performance domains generally have a
1-to-1 mapping with CPUFreq policies. All CPUs in a performance domain are
required to have the same micro-architecture. CPUs in different performance
domains can have different micro-architectures.

## 2. Core APIs

### 2.1 Config options

CONFIG_ENERGY_MODEL must be enabled to use the EM framework.

### 2.2 Registration of performance domains

#### Registration of 'advanced' EM

The 'advanced' EM gets its name due to the fact that the driver is allowed
to provide more precised power model. It's not limited to some implemented math
formula in the framework (like it is in 'simple' EM case). It can better reflect
the real power measurements performed for each performance state. Thus, this
registration method should be preferred in case considering EM static power
(leakage) is important.

Drivers are expected to register performance domains into the EM framework by
calling the following API:

```
int em_dev_register_perf_domain(struct device *dev, unsigned int nr_states,
              struct em_data_callback *cb, cpumask_t *cpus, bool microwatts);
```

Drivers must provide a callback function returning <frequency, power> tuples
for each performance state. The callback function provided by the driver is free
to fetch data from any relevant location (DT, firmware, ...), and by any mean
deemed necessary. Only for CPU devices, drivers must specify the CPUs of the
performance domains using cpumask. For other devices than CPUs the last
argument must be set to NULL.
The last argument 'microwatts' is important to set with correct value. Kernel
subsystems which use EM might rely on this flag to check if all EM devices use
the same scale. If there are different scales, these subsystems might decide
to return warning/error, stop working or panic.
See Section 3. for an example of driver implementing this
callback, or Section 2.4 for further documentation on this API

#### Registration of EM using DT

The EM can also be registered using OPP framework and information in DT
"operating-points-v2". Each OPP entry in DT can be extended with a property
"opp-microwatt" containing micro-Watts power value. This OPP DT property
allows a platform to register EM power values which are reflecting total power
(static + dynamic). These power values might be coming directly from
experiments and measurements.

#### Registration of 'artificial' EM

There is an option to provide a custom callback for drivers missing detailed
knowledge about power value for each performance state. The callback
.get_cost() is optional and provides the 'cost' values used by the EAS.
This is useful for platforms that only provide information on relative
efficiency between CPU types, where one could use the information to
create an abstract power model. But even an abstract power model can
sometimes be hard to fit in, given the input power value size restrictions.
The .get_cost() allows to provide the 'cost' values which reflect the
efficiency of the CPUs. This would allow to provide EAS information which
has different relation than what would be forced by the EM internal
formulas calculating 'cost' values. To register an EM for such platform, the
driver must set the flag 'microwatts' to 0, provide .get_power() callback
and provide .get_cost() callback. The EM framework would handle such platform
properly during registration. A flag EM_PERF_DOMAIN_ARTIFICIAL is set for such
platform. Special care should be taken by other frameworks which are using EM
to test and treat this flag properly.

#### Registration of 'simple' EM

The 'simple' EM is registered using the framework helper function
cpufreq_register_em_with_opp(). It implements a power model which is tight to
math formula:

```
Power = C * V^2 * f
```

The EM which is registered using this method might not reflect correctly the
physics of a real device, e.g. when static power (leakage) is important.

### 2.3 Accessing performance domains

There are two API functions which provide the access to the energy model:
[`em_cpu_get()`](energy-model.md#c.em_cpu_get "em_cpu_get") which takes CPU id as an argument and [`em_pd_get()`](energy-model.md#c.em_pd_get "em_pd_get") with device
pointer as an argument. It depends on the subsystem which interface it is
going to use, but in case of CPU devices both functions return the same
performance domain.

Subsystems interested in the energy model of a CPU can retrieve it using the
[`em_cpu_get()`](energy-model.md#c.em_cpu_get "em_cpu_get") API. The energy model tables are allocated once upon creation of
the performance domains, and kept in memory untouched.

The energy consumed by a performance domain can be estimated using the
[`em_cpu_energy()`](energy-model.md#c.em_cpu_energy "em_cpu_energy") API. The estimation is performed assuming that the schedutil
CPUfreq governor is in use in case of CPU device. Currently this calculation is
not provided for other type of devices.

More details about the above APIs can be found in `<linux/energy_model.h>`
or in Section 2.4

### 2.4 Description details of this API

struct em_perf_state
:   Performance state of a performance domain

**Definition**:

```
struct em_perf_state {
    unsigned long frequency;
    unsigned long power;
    unsigned long cost;
    unsigned long flags;
};
```

**Members**

`frequency`
:   The frequency in KHz, for consistency with CPUFreq

`power`
:   The power consumed at this level (by 1 CPU or by a registered
    device). It can be a total power: static and dynamic.

`cost`
:   The cost coefficient associated with this level, used during
    energy calculation. Equal to: power \* max_frequency / frequency

`flags`
:   see "em_perf_state flags" description below.

struct em_perf_domain
:   Performance domain

**Definition**:

```
struct em_perf_domain {
    struct em_perf_state *table;
    int nr_perf_states;
    unsigned long flags;
    unsigned long cpus[];
};
```

**Members**

`table`
:   List of performance states, in ascending order

`nr_perf_states`
:   Number of performance states

`flags`
:   See "em_perf_domain flags"

`cpus`
:   Cpumask covering the CPUs of the domain. It's here
    for performance reasons to avoid potential cache
    misses during energy calculations in the scheduler
    and simplifies allocating/freeing that memory region.

**Description**

In case of CPU device, a "performance domain" represents a group of CPUs
whose performance is scaled together. All CPUs of a performance domain
must have the same micro-architecture. Performance domains often have
a 1-to-1 mapping with CPUFreq policies. In case of other devices the **cpus**
field is unused.

struct [em_perf_state](energy-model.md#c.em_perf_state "em_perf_state") \*em_pd_get_efficient_state(struct [em_perf_domain](energy-model.md#c.em_perf_domain "em_perf_domain") \*pd, unsigned long freq)
:   Get an efficient performance state from the EM

**Parameters**

`struct em_perf_domain *pd`
:   Performance domain for which we want an efficient frequency

`unsigned long freq`
:   Frequency to map with the EM

**Description**

It is called from the scheduler code quite frequently and as a consequence
doesn't implement any check.

**Return**

An efficient performance state, high enough to meet **freq**
requirement.

unsigned long em_cpu_energy(struct [em_perf_domain](energy-model.md#c.em_perf_domain "em_perf_domain") \*pd, unsigned long max_util, unsigned long sum_util, unsigned long allowed_cpu_cap)
:   Estimates the energy consumed by the CPUs of a performance domain

**Parameters**

`struct em_perf_domain *pd`
:   performance domain for which energy has to be estimated

`unsigned long max_util`
:   highest utilization among CPUs of the domain

`unsigned long sum_util`
:   sum of the utilization of all CPUs in the domain

`unsigned long allowed_cpu_cap`
:   maximum allowed CPU capacity for the **pd**, which
    might reflect reduced frequency (due to thermal)

**Description**

This function must be used only for CPU devices. There is no validation,
i.e. if the EM is a CPU type and has cpumask allocated. It is called from
the scheduler code quite frequently and that is why there is not checks.

**Return**

the sum of the energy consumed by the CPUs of the domain assuming
a capacity state satisfying the max utilization of the domain.

int em_pd_nr_perf_states(struct [em_perf_domain](energy-model.md#c.em_perf_domain "em_perf_domain") \*pd)
:   Get the number of performance states of a perf. domain

**Parameters**

`struct em_perf_domain *pd`
:   performance domain for which this must be done

**Return**

the number of performance states in the performance domain table

struct [em_perf_domain](energy-model.md#c.em_perf_domain "em_perf_domain") \*em_pd_get(struct [device](../driver-api/infrastructure.md#c.device "device") \*dev)
:   Return the performance domain for a device

**Parameters**

`struct device *dev`
:   Device to find the performance domain for

**Description**

Returns the performance domain to which **dev** belongs, or NULL if it doesn't
exist.

struct [em_perf_domain](energy-model.md#c.em_perf_domain "em_perf_domain") \*em_cpu_get(int cpu)
:   Return the performance domain for a CPU

**Parameters**

`int cpu`
:   CPU to find the performance domain for

**Description**

Returns the performance domain to which **cpu** belongs, or NULL if it doesn't
exist.

int em_dev_register_perf_domain(struct [device](../driver-api/infrastructure.md#c.device "device") \*dev, unsigned int nr_states, struct em_data_callback \*cb, cpumask_t \*cpus, bool microwatts)
:   Register the Energy Model (EM) for a device

**Parameters**

`struct device *dev`
:   Device for which the EM is to register

`unsigned int nr_states`
:   Number of performance states to register

`struct em_data_callback *cb`
:   Callback functions providing the data of the Energy Model

`cpumask_t *cpus`
:   Pointer to cpumask_t, which in case of a CPU device is
    obligatory. It can be taken from i.e. 'policy->cpus'. For other
    type of devices this should be set to NULL.

`bool microwatts`
:   Flag indicating that the power values are in micro-Watts or
    in some other scale. It must be set properly.

**Description**

Create Energy Model tables for a performance domain using the callbacks
defined in cb.

The **microwatts** is important to set with correct value. Some kernel
sub-systems might rely on this flag and check if all devices in the EM are
using the same scale.

If multiple clients register the same performance domain, all but the first
registration will be ignored.

Return 0 on success

void em_dev_unregister_perf_domain(struct [device](../driver-api/infrastructure.md#c.device "device") \*dev)
:   Unregister Energy Model (EM) for a device

**Parameters**

`struct device *dev`
:   Device for which the EM is registered

**Description**

Unregister the EM for the specified **dev** (but not a CPU device).

## 3. Example driver

The CPUFreq framework supports dedicated callback for registering
the EM for a given CPU(s) 'policy' object: cpufreq_driver::register_em().
That callback has to be implemented properly for a given driver,
because the framework would call it at the right time during setup.
This section provides a simple example of a CPUFreq driver registering a
performance domain in the Energy Model framework using the (fake) 'foo'
protocol. The driver implements an est_power() function to be provided to the
EM framework:

```
-> drivers/cpufreq/foo_cpufreq.c

01    static int est_power(struct device *dev, unsigned long *mW,
02                    unsigned long *KHz)
03    {
04            long freq, power;
05
06            /* Use the 'foo' protocol to ceil the frequency */
07            freq = foo_get_freq_ceil(dev, *KHz);
08            if (freq < 0);
09                    return freq;
10
11            /* Estimate the power cost for the dev at the relevant freq. */
12            power = foo_estimate_power(dev, freq);
13            if (power < 0);
14                    return power;
15
16            /* Return the values to the EM framework */
17            *mW = power;
18            *KHz = freq;
19
20            return 0;
21    }
22
23    static void foo_cpufreq_register_em(struct cpufreq_policy *policy)
24    {
25            struct em_data_callback em_cb = EM_DATA_CB(est_power);
26            struct device *cpu_dev;
27            int nr_opp;
28
29            cpu_dev = get_cpu_device(cpumask_first(policy->cpus));
30
31            /* Find the number of OPPs for this policy */
32            nr_opp = foo_get_nr_opp(policy);
33
34            /* And register the new performance domain */
35            em_dev_register_perf_domain(cpu_dev, nr_opp, &em_cb, policy->cpus,
36                                        true);
37    }
38
39    static struct cpufreq_driver foo_cpufreq_driver = {
40            .register_em = foo_cpufreq_register_em,
41    };
```
