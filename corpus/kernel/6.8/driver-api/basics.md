---
collection: kernel
version: "6.8"
title: "Driver Basics"
source_url: https://www.kernel.org/doc/html/v6.8/driver-api/basics.html
fetched_at: 2026-08-21T03:30:26+00:00
---
# Driver Basics

## Driver Entry and Exit points

module_init

`module_init (x)`

> driver initialization entry point

**Parameters**

`x`
:   function to be run at kernel boot time or module insertion

**Description**

[`module_init()`](basics.md#c.module_init "module_init") will either be called during do_initcalls() (if
builtin) or at module insertion time (if a module). There can only
be one per module.

module_exit

`module_exit (x)`

> driver exit entry point

**Parameters**

`x`
:   function to be run when driver is removed

**Description**

[`module_exit()`](basics.md#c.module_exit "module_exit") will wrap the driver clean-up code
with cleanup_module() when used with rmmod when
the driver is a module. If the driver is statically
compiled into the kernel, [`module_exit()`](basics.md#c.module_exit "module_exit") has no effect.
There can only be one per module.

struct klp_modinfo
:   ELF information preserved from the livepatch module

**Definition**:

```
struct klp_modinfo {
    Elf_Ehdr hdr;
    Elf_Shdr *sechdrs;
    char *secstrings;
    unsigned int symndx;
};
```

**Members**

`hdr`
:   ELF header

`sechdrs`
:   Section header table

`secstrings`
:   String table for the section headers

`symndx`
:   The symbol table section index

bool try_module_get(struct [module](basics.md#c.try_module_get "module") \*module)
:   take module refcount unless module is being removed

**Parameters**

`struct module *module`
:   the module we should check for

**Description**

Only try to get a module reference count if the module is not being removed.
This call will fail if the module is in the process of being removed.

Care must also be taken to ensure the module exists and is alive prior to
usage of this call. This can be gauranteed through two means:

1. Direct protection: you know an earlier caller must have increased the
   module reference through __module_get(). This can typically be achieved
   by having another entity other than the module itself increment the
   module reference count.
2. Implied protection: there is an implied protection against module
   removal. An example of this is the implied protection used by kernfs /
   sysfs. The sysfs store / read file operations are guaranteed to exist
   through the use of kernfs's active reference (see kernfs_active()) and a
   sysfs / kernfs file removal cannot happen unless the same file is not
   active. Therefore, if a sysfs file is being read or written to the module
   which created it must still exist. It is therefore safe to use
   [`try_module_get()`](basics.md#c.try_module_get "try_module_get") on module sysfs store / read ops.

One of the real values to [`try_module_get()`](basics.md#c.try_module_get "try_module_get") is the module_is_live() check
which ensures that the caller of [`try_module_get()`](basics.md#c.try_module_get "try_module_get") can yield to userspace
module removal requests and gracefully fail if the module is on its way out.

Returns true if the reference count was successfully incremented.

void module_put(struct [module](basics.md#c.module_put "module") \*module)
:   release a reference count to a module

**Parameters**

`struct module *module`
:   the module we should release a reference count for

**Description**

If you successfully bump a reference count to a module with [`try_module_get()`](basics.md#c.try_module_get "try_module_get"),
when you are finished you must call [`module_put()`](basics.md#c.module_put "module_put") to release that reference
count.

## Driver device table

struct usb_device_id
:   identifies USB devices for probing and hotplugging

**Definition**:

```
struct usb_device_id {
    __u16 match_flags;
    __u16 idVendor;
    __u16 idProduct;
    __u16 bcdDevice_lo;
    __u16 bcdDevice_hi;
    __u8 bDeviceClass;
    __u8 bDeviceSubClass;
    __u8 bDeviceProtocol;
    __u8 bInterfaceClass;
    __u8 bInterfaceSubClass;
    __u8 bInterfaceProtocol;
    __u8 bInterfaceNumber;
    kernel_ulong_t driver_info ;
};
```

**Members**

`match_flags`
:   Bit mask controlling which of the other fields are used to
    match against new devices. Any field except for driver_info may be
    used, although some only make sense in conjunction with other fields.
    This is usually set by a USB_DEVICE_\*() macro, which sets all
    other fields in this structure except for driver_info.

`idVendor`
:   USB vendor ID for a device; numbers are assigned
    by the USB forum to its members.

`idProduct`
:   Vendor-assigned product ID.

`bcdDevice_lo`
:   Low end of range of vendor-assigned product version numbers.
    This is also used to identify individual product versions, for
    a range consisting of a single device.

`bcdDevice_hi`
:   High end of version number range. The range of product
    versions is inclusive.

`bDeviceClass`
:   Class of device; numbers are assigned
    by the USB forum. Products may choose to implement classes,
    or be vendor-specific. Device classes specify behavior of all
    the interfaces on a device.

`bDeviceSubClass`
:   Subclass of device; associated with bDeviceClass.

`bDeviceProtocol`
:   Protocol of device; associated with bDeviceClass.

`bInterfaceClass`
:   Class of interface; numbers are assigned
    by the USB forum. Products may choose to implement classes,
    or be vendor-specific. Interface classes specify behavior only
    of a given interface; other interfaces may support other classes.

`bInterfaceSubClass`
:   Subclass of interface; associated with bInterfaceClass.

`bInterfaceProtocol`
:   Protocol of interface; associated with bInterfaceClass.

`bInterfaceNumber`
:   Number of interface; composite devices may use
    fixed interface numbers to differentiate between vendor-specific
    interfaces.

`driver_info`
:   Holds information used by the driver. Usually it holds
    a pointer to a descriptor understood by the driver, or perhaps
    device flags.

**Description**

In most cases, drivers will create a table of device IDs by using
[`USB_DEVICE()`](usb/usb.md#c.USB_DEVICE "USB_DEVICE"), or similar macros designed for that purpose.
They will then export it to userspace using MODULE_DEVICE_TABLE(),
and provide it to the USB core through their usb_driver structure.

See the [`usb_match_id()`](usb/usb.md#c.usb_match_id "usb_match_id") function for information about how matches are
performed. Briefly, you will normally use one of several macros to help
construct these entries. Each entry you provide will either identify
one or more specific products, or will identify a class of products
which have agreed to behave the same. You should put the more specific
matches towards the beginning of your table, so that driver_info can
record quirks of specific products.

ACPI_DEVICE_CLASS

`ACPI_DEVICE_CLASS (_cls, _msk)`

> macro used to describe an ACPI device with the PCI-defined class-code information

**Parameters**

`_cls`
:   the class, subclass, prog-if triple for this device

`_msk`
:   the class mask for this device

**Description**

This macro is used to create a struct acpi_device_id that matches a
specific PCI class. The .id and .driver_data fields will be left
initialized with the default value.

struct mdio_device_id
:   identifies PHY devices on an MDIO/MII bus

**Definition**:

```
struct mdio_device_id {
    __u32 phy_id;
    __u32 phy_id_mask;
};
```

**Members**

`phy_id`
:   The result of
    (mdio_read(`MII_PHYSID1`) << 16 | mdio_read(`MII_PHYSID2`)) & **phy_id_mask**
    for this PHY type

`phy_id_mask`
:   Defines the significant bits of **phy_id**. A value of 0
    is used to terminate an array of [`struct mdio_device_id`](basics.md#c.mdio_device_id "mdio_device_id").

struct amba_id
:   identifies a device on an AMBA bus

**Definition**:

```
struct amba_id {
    unsigned int            id;
    unsigned int            mask;
    void *data;
};
```

**Members**

`id`
:   The significant bits if the hardware device ID

`mask`
:   Bitmask specifying which bits of the id field are significant when
    matching. A driver binds to a device when ((hardware device ID) & mask)
    == id.

`data`
:   Private data used by the driver.

struct mips_cdmm_device_id
:   identifies devices in MIPS CDMM bus

**Definition**:

```
struct mips_cdmm_device_id {
    __u8 type;
};
```

**Members**

`type`
:   Device type identifier.

struct mei_cl_device_id
:   MEI client device identifier

**Definition**:

```
struct mei_cl_device_id {
    char name[MEI_CL_NAME_SIZE];
    uuid_le uuid;
    __u8 version;
    kernel_ulong_t driver_info;
};
```

**Members**

`name`
:   helper name

`uuid`
:   client uuid

`version`
:   client protocol version

`driver_info`
:   information used by the driver.

**Description**

identifies mei client device by uuid and name

struct rio_device_id
:   RIO device identifier

**Definition**:

```
struct rio_device_id {
    __u16 did, vid;
    __u16 asm_did, asm_vid;
};
```

**Members**

`did`
:   RapidIO device ID

`vid`
:   RapidIO vendor ID

`asm_did`
:   RapidIO assembly device ID

`asm_vid`
:   RapidIO assembly vendor ID

**Description**

Identifies a RapidIO device based on both the device/vendor IDs and
the assembly device/vendor IDs.

struct fsl_mc_device_id
:   MC object device identifier

**Definition**:

```
struct fsl_mc_device_id {
    __u16 vendor;
    const char obj_type[16];
};
```

**Members**

`vendor`
:   vendor ID

`obj_type`
:   MC object type

**Description**

Type of entries in the "device Id" table for MC object devices supported by
a MC object device driver. The last entry of the table has vendor set to 0x0

struct tb_service_id
:   Thunderbolt service identifiers

**Definition**:

```
struct tb_service_id {
    __u32 match_flags;
    char protocol_key[8 + 1];
    __u32 protocol_id;
    __u32 protocol_version;
    __u32 protocol_revision;
    kernel_ulong_t driver_data;
};
```

**Members**

`match_flags`
:   Flags used to match the structure

`protocol_key`
:   Protocol key the service supports

`protocol_id`
:   Protocol id the service supports

`protocol_version`
:   Version of the protocol

`protocol_revision`
:   Revision of the protocol software

`driver_data`
:   Driver specific data

**Description**

Thunderbolt XDomain services are exposed as devices where each device
carries the protocol information the service supports. Thunderbolt
XDomain service drivers match against that information.

struct typec_device_id
:   USB Type-C alternate mode identifiers

**Definition**:

```
struct typec_device_id {
    __u16 svid;
    __u8 mode;
    kernel_ulong_t driver_data;
};
```

**Members**

`svid`
:   Standard or Vendor ID

`mode`
:   Mode index

`driver_data`
:   Driver specific data

struct tee_client_device_id
:   tee based device identifier

**Definition**:

```
struct tee_client_device_id {
    uuid_t uuid;
};
```

**Members**

`uuid`
:   For TEE based client devices we use the device uuid as
    the identifier.

struct wmi_device_id
:   WMI device identifier

**Definition**:

```
struct wmi_device_id {
    const char guid_string[UUID_STRING_LEN+1];
    const void *context;
};
```

**Members**

`guid_string`
:   36 char string of the form fa50ff2b-f2e8-45de-83fa-65417f2f49ba

`context`
:   pointer to driver specific data

struct mhi_device_id
:   MHI device identification

**Definition**:

```
struct mhi_device_id {
    const char chan[MHI_NAME_SIZE];
    kernel_ulong_t driver_data;
};
```

**Members**

`chan`
:   MHI channel name

`driver_data`
:   driver data;

struct dfl_device_id
:   dfl device identifier

**Definition**:

```
struct dfl_device_id {
    __u16 type;
    __u16 feature_id;
    kernel_ulong_t driver_data;
};
```

**Members**

`type`
:   DFL FIU type of the device. See enum dfl_id_type.

`feature_id`
:   feature identifier local to its DFL FIU type.

`driver_data`
:   driver specific data.

struct ishtp_device_id
:   ISHTP device identifier

**Definition**:

```
struct ishtp_device_id {
    guid_t guid;
    kernel_ulong_t driver_data;
};
```

**Members**

`guid`
:   GUID of the device.

`driver_data`
:   pointer to driver specific data

struct cdx_device_id
:   CDX device identifier

**Definition**:

```
struct cdx_device_id {
    __u16 vendor;
    __u16 device;
    __u16 subvendor;
    __u16 subdevice;
    __u32 class;
    __u32 class_mask;
    __u32 override_only;
};
```

**Members**

`vendor`
:   Vendor ID

`device`
:   Device ID

`subvendor`
:   Subsystem vendor ID (or CDX_ANY_ID)

`subdevice`
:   Subsystem device ID (or CDX_ANY_ID)

`class`
:   Device class
    Most drivers do not need to specify class/class_mask
    as vendor/device is normally sufficient.

`class_mask`
:   Limit which sub-fields of the class field are compared.

`override_only`
:   Match only when dev->driver_override is this driver.

**Description**

Type of entries in the "device Id" table for CDX devices supported by
a CDX device driver.

## Delaying and scheduling routines

struct prev_cputime
:   snapshot of system and user cputime

**Definition**:

```
struct prev_cputime {
#ifndef CONFIG_VIRT_CPU_ACCOUNTING_NATIVE;
    u64 utime;
    u64 stime;
    raw_spinlock_t lock;
#endif;
};
```

**Members**

`utime`
:   time spent in user mode

`stime`
:   time spent in system mode

`lock`
:   protects the above two fields

**Description**

Stores previous user/system time values such that we can guarantee
monotonicity.

int set_cpus_allowed_ptr(struct task_struct \*p, const struct cpumask \*new_mask)
:   set CPU affinity mask of a task

**Parameters**

`struct task_struct *p`
:   the task

`const struct cpumask *new_mask`
:   CPU affinity mask

**Return**

zero if successful, or a negative error code

int task_nice(const struct task_struct \*p)
:   return the nice value of a given task.

**Parameters**

`const struct task_struct *p`
:   the task in question.

**Return**

The nice value [ -20 ... 0 ... 19 ].

bool is_idle_task(const struct task_struct \*p)
:   is the specified task an idle task?

**Parameters**

`const struct task_struct *p`
:   the task in question.

**Return**

1 if **p** is an idle task. 0 otherwise.

int wake_up_process(struct task_struct \*p)
:   Wake up a specific process

**Parameters**

`struct task_struct *p`
:   The process to be woken up.

**Description**

Attempt to wake up the nominated process and move it to the set of runnable
processes.

This function executes a full memory barrier before accessing the task state.

**Return**

1 if the process was woken up, 0 if it was already running.

void preempt_notifier_register(struct preempt_notifier \*notifier)
:   tell me when current is being preempted & rescheduled

**Parameters**

`struct preempt_notifier *notifier`
:   notifier struct to register

void preempt_notifier_unregister(struct preempt_notifier \*notifier)
:   no longer interested in preemption notifications

**Parameters**

`struct preempt_notifier *notifier`
:   notifier struct to unregister

**Description**

This is *not* safe to call from within a preemption notifier.

__visible void notrace preempt_schedule_notrace(void)
:   preempt_schedule called by tracing

**Parameters**

`void`
:   no arguments

**Description**

The tracing infrastructure uses preempt_enable_notrace to prevent
recursion and tracing preempt enabling caused by the tracing
infrastructure itself. But as tracing can happen in areas coming
from userspace or just about to enter userspace, a preempt enable
can occur before user_exit() is called. This will cause the scheduler
to be called when the system is still in usermode.

To prevent this, the preempt_enable_notrace will use this function
instead of preempt_schedule() to exit user context if needed before
calling the scheduler.

void yield(void)
:   yield the current processor to other threads.

**Parameters**

`void`
:   no arguments

**Description**

Do not ever use this function, there's a 99% chance you're doing it wrong.

The scheduler is at all times free to pick the calling task as the most
eligible task to run, if removing the [`yield()`](basics.md#c.yield "yield") call from your code breaks
it, it's already broken.

Typical broken usage is:

while (!event)
:   [`yield()`](basics.md#c.yield "yield");

where one assumes that [`yield()`](basics.md#c.yield "yield") will let 'the other' process run that will
make event true. If the current task is a SCHED_FIFO task that will never
happen. Never use [`yield()`](basics.md#c.yield "yield") as a progress guarantee!!

If you want to use [`yield()`](basics.md#c.yield "yield") to wait for something, use [`wait_event()`](basics.md#c.wait_event "wait_event").
If you want to use [`yield()`](basics.md#c.yield "yield") to be 'nice' for others, use cond_resched().
If you still want to use [`yield()`](basics.md#c.yield "yield"), do not!

int yield_to(struct task_struct \*p, bool preempt)
:   yield the current processor to another thread in your thread group, or accelerate that thread toward the processor it's on.

**Parameters**

`struct task_struct *p`
:   target task

`bool preempt`
:   whether task preemption is allowed or not

**Description**

It's the caller's job to ensure that the target task struct
can't go away on us before we can do any checks.

**Return**

> true (>0) if we indeed boosted the target task.
> false (0) if we failed to boost the target.
> -ESRCH if there's no task to yield to.

int cpupri_find_fitness(struct cpupri \*cp, struct task_struct \*p, struct cpumask \*lowest_mask, bool (\*fitness_fn)(struct task_struct \*p, int cpu))
:   find the best (lowest-pri) CPU in the system

**Parameters**

`struct cpupri *cp`
:   The cpupri context

`struct task_struct *p`
:   The task

`struct cpumask *lowest_mask`
:   A mask to fill in with selected CPUs (or NULL)

`bool (*fitness_fn)(struct task_struct *p, int cpu)`
:   A pointer to a function to do custom checks whether the CPU
    fits a specific criteria so that we only return those CPUs.

**Note**

This function returns the recommended CPUs as calculated during the
current invocation. By the time the call returns, the CPUs may have in
fact changed priorities any number of times. While not ideal, it is not
an issue of correctness since the normal rebalancer logic will correct
any discrepancies created by racing against the uncertainty of the current
priority configuration.

**Return**

(int)bool - CPUs were found

void cpupri_set(struct cpupri \*cp, int cpu, int newpri)
:   update the CPU priority setting

**Parameters**

`struct cpupri *cp`
:   The cpupri context

`int cpu`
:   The target CPU

`int newpri`
:   The priority (INVALID,NORMAL,RT1-RT99,HIGHER) to assign to this CPU

**Note**

Assumes cpu_rq(cpu)->lock is locked

**Return**

(void)

int cpupri_init(struct cpupri \*cp)
:   initialize the cpupri structure

**Parameters**

`struct cpupri *cp`
:   The cpupri context

**Return**

-ENOMEM on memory allocation failure.

void cpupri_cleanup(struct cpupri \*cp)
:   clean up the cpupri structure

**Parameters**

`struct cpupri *cp`
:   The cpupri context

void update_tg_load_avg(struct [cfs_rq](basics.md#c.update_tg_load_avg "cfs_rq") \*cfs_rq)
:   update the tg's load avg

**Parameters**

`struct cfs_rq *cfs_rq`
:   the cfs_rq whose avg changed

**Description**

This function 'ensures': tg->load_avg := Sum tg->cfs_rq[]->avg.load.
However, because tg->load_avg is a global value there are performance
considerations.

In order to avoid having to look at the other cfs_rq's, we use a
differential update where we store the last value we propagated. This in
turn allows skipping updates if the differential is 'small'.

Updating tg's load_avg is necessary before update_cfs_share().

int update_cfs_rq_load_avg(u64 now, struct [cfs_rq](basics.md#c.update_cfs_rq_load_avg "cfs_rq") \*cfs_rq)
:   update the cfs_rq's load/util averages

**Parameters**

`u64 now`
:   current time, as per cfs_rq_clock_pelt()

`struct cfs_rq *cfs_rq`
:   cfs_rq to update

**Description**

The cfs_rq avg is the direct sum of all its entities (blocked and runnable)
avg. The immediate corollary is that all (fair) tasks must be attached.

cfs_rq->avg is used for task_h_load() and update_cfs_share() for example.

Since both these conditions indicate a changed cfs_rq->avg.load we should
call [`update_tg_load_avg()`](basics.md#c.update_tg_load_avg "update_tg_load_avg") when this function returns true.

**Return**

true if the load decayed or we removed load.

void attach_entity_load_avg(struct [cfs_rq](basics.md#c.attach_entity_load_avg "cfs_rq") \*cfs_rq, struct sched_entity \*se)
:   attach this entity to its cfs_rq load avg

**Parameters**

`struct cfs_rq *cfs_rq`
:   cfs_rq to attach to

`struct sched_entity *se`
:   sched_entity to attach

**Description**

Must call [`update_cfs_rq_load_avg()`](basics.md#c.update_cfs_rq_load_avg "update_cfs_rq_load_avg") before this, since we rely on
cfs_rq->avg.last_update_time being current.

void detach_entity_load_avg(struct [cfs_rq](basics.md#c.detach_entity_load_avg "cfs_rq") \*cfs_rq, struct sched_entity \*se)
:   detach this entity from its cfs_rq load avg

**Parameters**

`struct cfs_rq *cfs_rq`
:   cfs_rq to detach from

`struct sched_entity *se`
:   sched_entity to detach

**Description**

Must call [`update_cfs_rq_load_avg()`](basics.md#c.update_cfs_rq_load_avg "update_cfs_rq_load_avg") before this, since we rely on
cfs_rq->avg.last_update_time being current.

unsigned long cpu_util(int cpu, struct task_struct \*p, int dst_cpu, int boost)
:   Estimates the amount of CPU capacity used by CFS tasks.

**Parameters**

`int cpu`
:   the CPU to get the utilization for

`struct task_struct *p`
:   task for which the CPU utilization should be predicted or NULL

`int dst_cpu`
:   CPU **p** migrates to, -1 if **p** moves from **cpu** or **p** == NULL

`int boost`
:   1 to enable boosting, otherwise 0

**Description**

The unit of the return value must be the same as the one of CPU capacity
so that CPU utilization can be compared with CPU capacity.

CPU utilization is the sum of running time of runnable tasks plus the
recent utilization of currently non-runnable tasks on that CPU.
It represents the amount of CPU capacity currently used by CFS tasks in
the range [0..max CPU capacity] with max CPU capacity being the CPU
capacity at f_max.

The estimated CPU utilization is defined as the maximum between CPU
utilization and sum of the estimated utilization of the currently
runnable tasks on that CPU. It preserves a utilization "snapshot" of
previously-executed tasks, which helps better deduce how busy a CPU will
be when a long-sleeping task wakes up. The contribution to CPU utilization
of such a task would be significantly decayed at this point of time.

Boosted CPU utilization is defined as max(CPU runnable, CPU utilization).
CPU contention for CFS tasks can be detected by CPU runnable > CPU
utilization. Boosting is implemented in [`cpu_util()`](basics.md#c.cpu_util "cpu_util") so that internal
users (e.g. EAS) can use it next to external users (e.g. schedutil),
latter via cpu_util_cfs_boost().

CPU utilization can be higher than the current CPU capacity
(f_curr/f_max \* max CPU capacity) or even the max CPU capacity because
of rounding errors as well as task migrations or wakeups of new tasks.
CPU utilization has to be capped to fit into the [0..max CPU capacity]
range. Otherwise a group of CPUs (CPU0 util = 121% + CPU1 util = 80%)
could be seen as over-utilized even though CPU1 has 20% of spare CPU
capacity. CPU utilization is allowed to overshoot current CPU capacity
though since this is useful for predicting the CPU capacity required
after task migrations (scheduler-driven DVFS).

**Return**

(Boosted) (estimated) utilization for the specified CPU.

bool sched_use_asym_prio(struct sched_domain \*sd, int cpu)
:   Check whether asym_packing priority must be used

**Parameters**

`struct sched_domain *sd`
:   The scheduling domain of the load balancing

`int cpu`
:   A CPU

**Description**

Always use CPU priority when balancing load between SMT siblings. When
balancing load between cores, it is not sufficient that **cpu** is idle. Only
use CPU priority if the whole core is idle.

**Return**

True if the priority of **cpu** must be followed. False otherwise.

bool sched_asym(struct lb_env \*env, struct sd_lb_stats \*sds, struct sg_lb_stats \*sgs, struct sched_group \*group)
:   Check if the destination CPU can do asym_packing load balance

**Parameters**

`struct lb_env *env`
:   The load balancing environment

`struct sd_lb_stats *sds`
:   Load-balancing data with statistics of the local group

`struct sg_lb_stats *sgs`
:   Load-balancing statistics of the candidate busiest group

`struct sched_group *group`
:   The candidate busiest group

**Description**

**env**::dst_cpu can do asym_packing if it has higher priority than the
preferred CPU of **group**.

SMT is a special case. If we are balancing load between cores, **env**::dst_cpu
can do asym_packing balance only if all its SMT siblings are idle. Also, it
can only do it if **group** is an SMT group and has exactly on busy CPU. Larger
imbalances in the number of CPUS are dealt with in [`find_busiest_group()`](basics.md#c.find_busiest_group "find_busiest_group").

If we are balancing load within an SMT core, or at PKG domain level, always
proceed.

**Return**

true if **env**::dst_cpu can do with asym_packing load balance. False
otherwise.

void update_sg_lb_stats(struct lb_env \*env, struct sd_lb_stats \*sds, struct sched_group \*group, struct sg_lb_stats \*sgs, int \*sg_status)
:   Update sched_group's statistics for load balancing.

**Parameters**

`struct lb_env *env`
:   The load balancing environment.

`struct sd_lb_stats *sds`
:   Load-balancing data with statistics of the local group.

`struct sched_group *group`
:   sched_group whose statistics are to be updated.

`struct sg_lb_stats *sgs`
:   variable to hold the statistics for this group.

`int *sg_status`
:   Holds flag indicating the status of the sched_group

bool update_sd_pick_busiest(struct lb_env \*env, struct sd_lb_stats \*sds, struct sched_group \*sg, struct sg_lb_stats \*sgs)
:   return 1 on busiest group

**Parameters**

`struct lb_env *env`
:   The load balancing environment.

`struct sd_lb_stats *sds`
:   sched_domain statistics

`struct sched_group *sg`
:   sched_group candidate to be checked for being the busiest

`struct sg_lb_stats *sgs`
:   sched_group statistics

**Description**

Determine if **sg** is a busier group than the previously selected
busiest group.

**Return**

`true` if **sg** is a busier group than the previously selected
busiest group. `false` otherwise.

int idle_cpu_without(int cpu, struct task_struct \*p)
:   would a given CPU be idle without p ?

**Parameters**

`int cpu`
:   the processor on which idleness is tested.

`struct task_struct *p`
:   task which should be ignored.

**Return**

1 if the CPU would be idle. 0 otherwise.

void update_sd_lb_stats(struct lb_env \*env, struct sd_lb_stats \*sds)
:   Update sched_domain's statistics for load balancing.

**Parameters**

`struct lb_env *env`
:   The load balancing environment.

`struct sd_lb_stats *sds`
:   variable to hold the statistics for this sched_domain.

void calculate_imbalance(struct lb_env \*env, struct sd_lb_stats \*sds)
:   Calculate the amount of imbalance present within the groups of a given sched_domain during load balance.

**Parameters**

`struct lb_env *env`
:   load balance environment

`struct sd_lb_stats *sds`
:   statistics of the sched_domain whose imbalance is to be calculated.

struct sched_group \*find_busiest_group(struct lb_env \*env)
:   Returns the busiest group within the sched_domain if there is an imbalance.

**Parameters**

`struct lb_env *env`
:   The load balancing environment.

**Description**

Also calculates the amount of runnable load which should be moved
to restore balance.

**Return**

- The busiest group if imbalance exists.

DECLARE_COMPLETION

`DECLARE_COMPLETION (work)`

> declare and initialize a completion structure

**Parameters**

`work`
:   identifier for the completion structure

**Description**

This macro declares and initializes a completion structure. Generally used
for static declarations. You should use the _ONSTACK variant for automatic
variables.

DECLARE_COMPLETION_ONSTACK

`DECLARE_COMPLETION_ONSTACK (work)`

> declare and initialize a completion structure

**Parameters**

`work`
:   identifier for the completion structure

**Description**

This macro declares and initializes a completion structure on the kernel
stack.

void init_completion(struct completion \*x)
:   Initialize a dynamically allocated completion

**Parameters**

`struct completion *x`
:   pointer to completion structure that is to be initialized

**Description**

This inline function will initialize a dynamically created completion
structure.

void reinit_completion(struct completion \*x)
:   reinitialize a completion structure

**Parameters**

`struct completion *x`
:   pointer to completion structure that is to be reinitialized

**Description**

This inline function should be used to reinitialize a completion structure so it can
be reused. This is especially important after complete_all() is used.

## Time and timer routines

u64 get_jiffies_64(void)
:   read the 64-bit non-atomic jiffies_64 value

**Parameters**

`void`
:   no arguments

**Description**

When BITS_PER_LONG < 64, this uses sequence number sampling using
jiffies_lock to protect the 64-bit read.

**Return**

current 64-bit jiffies value

time_after

`time_after (a, b)`

> returns true if the time a is after time b.

**Parameters**

`a`
:   first comparable as unsigned long

`b`
:   second comparable as unsigned long

**Description**

Do this with "<0" and ">=0" to only test the sign of the result. A
good compiler would generate better code (and a really good compiler
wouldn't care). Gcc is currently neither.

**Return**

`true` is time a is after time b, otherwise `false`.

time_before

`time_before (a, b)`

> returns true if the time a is before time b.

**Parameters**

`a`
:   first comparable as unsigned long

`b`
:   second comparable as unsigned long

**Return**

`true` is time a is before time b, otherwise `false`.

time_after_eq

`time_after_eq (a, b)`

> returns true if the time a is after or the same as time b.

**Parameters**

`a`
:   first comparable as unsigned long

`b`
:   second comparable as unsigned long

**Return**

`true` is time a is after or the same as time b, otherwise `false`.

time_before_eq

`time_before_eq (a, b)`

> returns true if the time a is before or the same as time b.

**Parameters**

`a`
:   first comparable as unsigned long

`b`
:   second comparable as unsigned long

**Return**

`true` is time a is before or the same as time b, otherwise `false`.

time_in_range

`time_in_range (a, b, c)`

> Calculate whether a is in the range of [b, c].

**Parameters**

`a`
:   time to test

`b`
:   beginning of the range

`c`
:   end of the range

**Return**

`true` is time a is in the range [b, c], otherwise `false`.

time_in_range_open

`time_in_range_open (a, b, c)`

> Calculate whether a is in the range of [b, c).

**Parameters**

`a`
:   time to test

`b`
:   beginning of the range

`c`
:   end of the range

**Return**

`true` is time a is in the range [b, c), otherwise `false`.

time_after64

`time_after64 (a, b)`

> returns true if the time a is after time b.

**Parameters**

`a`
:   first comparable as __u64

`b`
:   second comparable as __u64

**Description**

This must be used when utilizing jiffies_64 (i.e. return value of
[`get_jiffies_64()`](basics.md#c.get_jiffies_64 "get_jiffies_64")).

**Return**

`true` is time a is after time b, otherwise `false`.

time_before64

`time_before64 (a, b)`

> returns true if the time a is before time b.

**Parameters**

`a`
:   first comparable as __u64

`b`
:   second comparable as __u64

**Description**

This must be used when utilizing jiffies_64 (i.e. return value of
[`get_jiffies_64()`](basics.md#c.get_jiffies_64 "get_jiffies_64")).

**Return**

`true` is time a is before time b, otherwise `false`.

time_after_eq64

`time_after_eq64 (a, b)`

> returns true if the time a is after or the same as time b.

**Parameters**

`a`
:   first comparable as __u64

`b`
:   second comparable as __u64

**Description**

This must be used when utilizing jiffies_64 (i.e. return value of
[`get_jiffies_64()`](basics.md#c.get_jiffies_64 "get_jiffies_64")).

**Return**

`true` is time a is after or the same as time b, otherwise `false`.

time_before_eq64

`time_before_eq64 (a, b)`

> returns true if the time a is before or the same as time b.

**Parameters**

`a`
:   first comparable as __u64

`b`
:   second comparable as __u64

**Description**

This must be used when utilizing jiffies_64 (i.e. return value of
[`get_jiffies_64()`](basics.md#c.get_jiffies_64 "get_jiffies_64")).

**Return**

`true` is time a is before or the same as time b, otherwise `false`.

time_in_range64

`time_in_range64 (a, b, c)`

> Calculate whether a is in the range of [b, c].

**Parameters**

`a`
:   time to test

`b`
:   beginning of the range

`c`
:   end of the range

**Return**

`true` is time a is in the range [b, c], otherwise `false`.

time_is_before_jiffies

`time_is_before_jiffies (a)`

> return true if a is before jiffies

**Parameters**

`a`
:   time (unsigned long) to compare to jiffies

**Return**

`true` is time a is before jiffies, otherwise `false`.

time_is_before_jiffies64

`time_is_before_jiffies64 (a)`

> return true if a is before jiffies_64

**Parameters**

`a`
:   time (__u64) to compare to jiffies_64

**Return**

`true` is time a is before jiffies_64, otherwise `false`.

time_is_after_jiffies

`time_is_after_jiffies (a)`

> return true if a is after jiffies

**Parameters**

`a`
:   time (unsigned long) to compare to jiffies

**Return**

`true` is time a is after jiffies, otherwise `false`.

time_is_after_jiffies64

`time_is_after_jiffies64 (a)`

> return true if a is after jiffies_64

**Parameters**

`a`
:   time (__u64) to compare to jiffies_64

**Return**

`true` is time a is after jiffies_64, otherwise `false`.

time_is_before_eq_jiffies

`time_is_before_eq_jiffies (a)`

> return true if a is before or equal to jiffies

**Parameters**

`a`
:   time (unsigned long) to compare to jiffies

**Return**

`true` is time a is before or the same as jiffies, otherwise `false`.

time_is_before_eq_jiffies64

`time_is_before_eq_jiffies64 (a)`

> return true if a is before or equal to jiffies_64

**Parameters**

`a`
:   time (__u64) to compare to jiffies_64

**Return**

`true` is time a is before or the same jiffies_64, otherwise `false`.

time_is_after_eq_jiffies

`time_is_after_eq_jiffies (a)`

> return true if a is after or equal to jiffies

**Parameters**

`a`
:   time (unsigned long) to compare to jiffies

**Return**

`true` is time a is after or the same as jiffies, otherwise `false`.

time_is_after_eq_jiffies64

`time_is_after_eq_jiffies64 (a)`

> return true if a is after or equal to jiffies_64

**Parameters**

`a`
:   time (__u64) to compare to jiffies_64

**Return**

`true` is time a is after or the same as jiffies_64, otherwise `false`.

u64 jiffies_to_nsecs(const unsigned long j)
:   Convert jiffies to nanoseconds

**Parameters**

`const unsigned long j`
:   jiffies value

**Return**

nanoseconds value

unsigned long msecs_to_jiffies(const unsigned int m)
:   - convert milliseconds to jiffies

**Parameters**

`const unsigned int m`
:   time in milliseconds

**Description**

conversion is done as follows:

- negative values mean 'infinite timeout' (MAX_JIFFY_OFFSET)
- 'too large' values [that would result in larger than
  MAX_JIFFY_OFFSET values] mean 'infinite timeout' too.
- all other values are converted to jiffies by either multiplying
  the input value by a factor or dividing it with a factor and
  handling any 32-bit overflows.
  for the details see [`__msecs_to_jiffies()`](basics.md#c.__msecs_to_jiffies "__msecs_to_jiffies")

[`msecs_to_jiffies()`](basics.md#c.msecs_to_jiffies "msecs_to_jiffies") checks for the passed in value being a constant
via __builtin_constant_p() allowing gcc to eliminate most of the
code. [`__msecs_to_jiffies()`](basics.md#c.__msecs_to_jiffies "__msecs_to_jiffies") is called if the value passed does not
allow constant folding and the actual conversion must be done at
runtime.
The HZ range specific helpers _msecs_to_jiffies() are called both
directly here and from [`__msecs_to_jiffies()`](basics.md#c.__msecs_to_jiffies "__msecs_to_jiffies") in the case where
constant folding is not possible.

**Return**

jiffies value

unsigned long usecs_to_jiffies(const unsigned int u)
:   - convert microseconds to jiffies

**Parameters**

`const unsigned int u`
:   time in microseconds

**Description**

conversion is done as follows:

- 'too large' values [that would result in larger than
  MAX_JIFFY_OFFSET values] mean 'infinite timeout' too.
- all other values are converted to jiffies by either multiplying
  the input value by a factor or dividing it with a factor and
  handling any 32-bit overflows as for msecs_to_jiffies.

[`usecs_to_jiffies()`](basics.md#c.usecs_to_jiffies "usecs_to_jiffies") checks for the passed in value being a constant
via __builtin_constant_p() allowing gcc to eliminate most of the
code. [`__usecs_to_jiffies()`](basics.md#c.__usecs_to_jiffies "__usecs_to_jiffies") is called if the value passed does not
allow constant folding and the actual conversion must be done at
runtime.
The HZ range specific helpers _usecs_to_jiffies() are called both
directly here and from [`__msecs_to_jiffies()`](basics.md#c.__msecs_to_jiffies "__msecs_to_jiffies") in the case where
constant folding is not possible.

**Return**

jiffies value

unsigned int jiffies_to_msecs(const unsigned long j)
:   Convert jiffies to milliseconds

**Parameters**

`const unsigned long j`
:   jiffies value

**Description**

Avoid unnecessary multiplications/divisions in the
two most common HZ cases.

**Return**

milliseconds value

unsigned int jiffies_to_usecs(const unsigned long j)
:   Convert jiffies to microseconds

**Parameters**

`const unsigned long j`
:   jiffies value

**Return**

microseconds value

time64_t mktime64(const unsigned int year0, const unsigned int mon0, const unsigned int day, const unsigned int hour, const unsigned int min, const unsigned int sec)
:   Converts date to seconds.

**Parameters**

`const unsigned int year0`
:   year to convert

`const unsigned int mon0`
:   month to convert

`const unsigned int day`
:   day to convert

`const unsigned int hour`
:   hour to convert

`const unsigned int min`
:   minute to convert

`const unsigned int sec`
:   second to convert

**Description**

Converts Gregorian date to seconds since 1970-01-01 00:00:00.
Assumes input in normal date format, i.e. 1980-12-31 23:59:59
=> year=1980, mon=12, day=31, hour=23, min=59, sec=59.

[For the Julian calendar (which was used in Russia before 1917,
Britain & colonies before 1752, anywhere else before 1582,
and is still in use by some communities) leave out the
-year/100+year/400 terms, and add 10.]

This algorithm was first published by Gauss (I think).

A leap second can be indicated by calling this function with sec as
60 (allowable under ISO 8601). The leap second is treated the same
as the following second since they don't exist in UNIX time.

An encoding of midnight at the end of the day as 24:00:00 - ie. midnight
tomorrow - (allowable under ISO 8601) is supported.

**Return**

seconds since the epoch time for the given input date

void set_normalized_timespec64(struct timespec64 \*ts, time64_t sec, s64 nsec)
:   set timespec sec and nsec parts and normalize

**Parameters**

`struct timespec64 *ts`
:   pointer to timespec variable to be set

`time64_t sec`
:   seconds to set

`s64 nsec`
:   nanoseconds to set

**Description**

Set seconds and nanoseconds field of a timespec variable and
normalize to the timespec storage format

**Note**

The tv_nsec part is always in the range of 0 <= tv_nsec < NSEC_PER_SEC.
For negative values only the tv_sec field is negative !

struct timespec64 ns_to_timespec64(s64 nsec)
:   Convert nanoseconds to timespec64

**Parameters**

`s64 nsec`
:   the nanoseconds value to be converted

**Return**

the timespec64 representation of the nsec parameter.

unsigned long __msecs_to_jiffies(const unsigned int m)
:   - convert milliseconds to jiffies

**Parameters**

`const unsigned int m`
:   time in milliseconds

**Description**

conversion is done as follows:

- negative values mean 'infinite timeout' (MAX_JIFFY_OFFSET)
- 'too large' values [that would result in larger than
  MAX_JIFFY_OFFSET values] mean 'infinite timeout' too.
- all other values are converted to jiffies by either multiplying
  the input value by a factor or dividing it with a factor and
  handling any 32-bit overflows.
  for the details see [`__msecs_to_jiffies()`](basics.md#c.__msecs_to_jiffies "__msecs_to_jiffies")

[`__msecs_to_jiffies()`](basics.md#c.__msecs_to_jiffies "__msecs_to_jiffies") checks for the passed in value being a constant
via __builtin_constant_p() allowing gcc to eliminate most of the
code, [`__msecs_to_jiffies()`](basics.md#c.__msecs_to_jiffies "__msecs_to_jiffies") is called if the value passed does not
allow constant folding and the actual conversion must be done at
runtime.
The _msecs_to_jiffies helpers are the HZ dependent conversion
routines found in include/linux/jiffies.h

**Return**

jiffies value

unsigned long __usecs_to_jiffies(const unsigned int u)
:   - convert microseconds to jiffies

**Parameters**

`const unsigned int u`
:   time in milliseconds

**Return**

jiffies value

unsigned long timespec64_to_jiffies(const struct timespec64 \*value)
:   convert a timespec64 value to jiffies

**Parameters**

`const struct timespec64 *value`
:   pointer to `struct timespec64`

**Description**

The TICK_NSEC - 1 rounds up the value to the next resolution. Note
that a remainder subtract here would not do the right thing as the
resolution values don't fall on second boundaries. I.e. the line:
nsec -= nsec % TICK_NSEC; is NOT a correct resolution rounding.
Note that due to the small error in the multiplier here, this
rounding is incorrect for sufficiently large values of tv_nsec, but
well formed timespecs should have tv_nsec < NSEC_PER_SEC, so we're
OK.

Rather, we just shift the bits off the right.

The >> (NSEC_JIFFIE_SC - SEC_JIFFIE_SC) converts the scaled nsec
value to a scaled second value.

**Return**

jiffies value

void jiffies_to_timespec64(const unsigned long jiffies, struct timespec64 \*value)
:   convert jiffies value to `struct timespec64`

**Parameters**

`const unsigned long jiffies`
:   jiffies value

`struct timespec64 *value`
:   pointer to `struct timespec64`

clock_t jiffies_to_clock_t(unsigned long x)
:   Convert jiffies to clock_t

**Parameters**

`unsigned long x`
:   jiffies value

**Return**

jiffies converted to clock_t (CLOCKS_PER_SEC)

unsigned long clock_t_to_jiffies(unsigned long x)
:   Convert clock_t to jiffies

**Parameters**

`unsigned long x`
:   clock_t value

**Return**

clock_t value converted to jiffies

u64 jiffies_64_to_clock_t(u64 x)
:   Convert jiffies_64 to clock_t

**Parameters**

`u64 x`
:   jiffies_64 value

**Return**

jiffies_64 value converted to 64-bit "clock_t" (CLOCKS_PER_SEC)

u64 jiffies64_to_nsecs(u64 j)
:   Convert jiffies64 to nanoseconds

**Parameters**

`u64 j`
:   jiffies64 value

**Return**

nanoseconds value

u64 jiffies64_to_msecs(const u64 j)
:   Convert jiffies64 to milliseconds

**Parameters**

`const u64 j`
:   jiffies64 value

**Return**

milliseconds value

u64 nsecs_to_jiffies64(u64 n)
:   Convert nsecs in u64 to jiffies64

**Parameters**

`u64 n`
:   nsecs in u64

**Description**

Unlike {m,u}secs_to_jiffies, type of input is not unsigned int but u64.
And this doesn't return MAX_JIFFY_OFFSET since this function is designed
for scheduler, not for use in device drivers to calculate timeout value.

**note**

> NSEC_PER_SEC = 10^9 = (5^9 \* 2^9) = (1953125 \* 512)
> ULLONG_MAX ns = 18446744073.709551615 secs = about 584 years

**Return**

nsecs converted to jiffies64 value

unsigned long nsecs_to_jiffies(u64 n)
:   Convert nsecs in u64 to jiffies

**Parameters**

`u64 n`
:   nsecs in u64

**Description**

Unlike {m,u}secs_to_jiffies, type of input is not unsigned int but u64.
And this doesn't return MAX_JIFFY_OFFSET since this function is designed
for scheduler, not for use in device drivers to calculate timeout value.

**note**

> NSEC_PER_SEC = 10^9 = (5^9 \* 2^9) = (1953125 \* 512)
> ULLONG_MAX ns = 18446744073.709551615 secs = about 584 years

**Return**

nsecs converted to jiffies value

int get_timespec64(struct timespec64 \*ts, const struct __kernel_timespec __user \*uts)
:   get user's time value into kernel space

**Parameters**

`struct timespec64 *ts`
:   destination `struct timespec64`

`const struct __kernel_timespec __user *uts`
:   user's time value as `struct __kernel_timespec`

**Description**

Handles compat or 32-bit modes.

**Return**

`0` on success or negative errno on error

int put_timespec64(const struct timespec64 \*ts, struct __kernel_timespec __user \*uts)
:   convert timespec64 value to __kernel_timespec format and copy the latter to userspace

**Parameters**

`const struct timespec64 *ts`
:   input `struct timespec64`

`struct __kernel_timespec __user *uts`
:   user's `struct __kernel_timespec`

**Return**

`0` on success or negative errno on error

int get_old_timespec32(struct timespec64 \*ts, const void __user \*uts)
:   get user's old-format time value into kernel space

**Parameters**

`struct timespec64 *ts`
:   destination `struct timespec64`

`const void __user *uts`
:   user's old-format time value (`struct old_timespec32`)

**Description**

Handles X86_X32_ABI compatibility conversion.

**Return**

`0` on success or negative errno on error

int put_old_timespec32(const struct timespec64 \*ts, void __user \*uts)
:   convert timespec64 value to `struct old_timespec32` and copy the latter to userspace

**Parameters**

`const struct timespec64 *ts`
:   input `struct timespec64`

`void __user *uts`
:   user's `struct old_timespec32`

**Description**

Handles X86_X32_ABI compatibility conversion.

**Return**

`0` on success or negative errno on error

int get_itimerspec64(struct itimerspec64 \*it, const struct __kernel_itimerspec __user \*uit)
:   get user's `struct __kernel_itimerspec` into kernel space

**Parameters**

`struct itimerspec64 *it`
:   destination `struct itimerspec64`

`const struct __kernel_itimerspec __user *uit`
:   user's `struct __kernel_itimerspec`

**Return**

`0` on success or negative errno on error

int put_itimerspec64(const struct itimerspec64 \*it, struct __kernel_itimerspec __user \*uit)
:   convert `struct itimerspec64` to __kernel_itimerspec format and copy the latter to userspace

**Parameters**

`const struct itimerspec64 *it`
:   input `struct itimerspec64`

`struct __kernel_itimerspec __user *uit`
:   user's `struct __kernel_itimerspec`

**Return**

`0` on success or negative errno on error

int get_old_itimerspec32(struct itimerspec64 \*its, const struct old_itimerspec32 __user \*uits)
:   get user's `struct old_itimerspec32` into kernel space

**Parameters**

`struct itimerspec64 *its`
:   destination `struct itimerspec64`

`const struct old_itimerspec32 __user *uits`
:   user's `struct old_itimerspec32`

**Return**

`0` on success or negative errno on error

int put_old_itimerspec32(const struct itimerspec64 \*its, struct old_itimerspec32 __user \*uits)
:   convert `struct itimerspec64` to `struct old_itimerspec32` and copy the latter to userspace

**Parameters**

`const struct itimerspec64 *its`
:   input `struct itimerspec64`

`struct old_itimerspec32 __user *uits`
:   user's `struct old_itimerspec32`

**Return**

`0` on success or negative errno on error

unsigned long __round_jiffies(unsigned long j, int cpu)
:   function to round jiffies to a full second

**Parameters**

`unsigned long j`
:   the time in (absolute) jiffies that should be rounded

`int cpu`
:   the processor number on which the timeout will happen

**Description**

[`__round_jiffies()`](basics.md#c.__round_jiffies "__round_jiffies") rounds an absolute time in the future (in jiffies)
up or down to (approximately) full seconds. This is useful for timers
for which the exact time they fire does not matter too much, as long as
they fire approximately every X seconds.

By rounding these timers to whole seconds, all such timers will fire
at the same time, rather than at various times spread out. The goal
of this is to have the CPU wake up less, which saves power.

The exact rounding is skewed for each processor to avoid all
processors firing at the exact same time, which could lead
to lock contention or spurious cache line bouncing.

The return value is the rounded version of the **j** parameter.

unsigned long __round_jiffies_relative(unsigned long j, int cpu)
:   function to round jiffies to a full second

**Parameters**

`unsigned long j`
:   the time in (relative) jiffies that should be rounded

`int cpu`
:   the processor number on which the timeout will happen

**Description**

[`__round_jiffies_relative()`](basics.md#c.__round_jiffies_relative "__round_jiffies_relative") rounds a time delta in the future (in jiffies)
up or down to (approximately) full seconds. This is useful for timers
for which the exact time they fire does not matter too much, as long as
they fire approximately every X seconds.

By rounding these timers to whole seconds, all such timers will fire
at the same time, rather than at various times spread out. The goal
of this is to have the CPU wake up less, which saves power.

The exact rounding is skewed for each processor to avoid all
processors firing at the exact same time, which could lead
to lock contention or spurious cache line bouncing.

The return value is the rounded version of the **j** parameter.

unsigned long round_jiffies(unsigned long j)
:   function to round jiffies to a full second

**Parameters**

`unsigned long j`
:   the time in (absolute) jiffies that should be rounded

**Description**

[`round_jiffies()`](basics.md#c.round_jiffies "round_jiffies") rounds an absolute time in the future (in jiffies)
up or down to (approximately) full seconds. This is useful for timers
for which the exact time they fire does not matter too much, as long as
they fire approximately every X seconds.

By rounding these timers to whole seconds, all such timers will fire
at the same time, rather than at various times spread out. The goal
of this is to have the CPU wake up less, which saves power.

The return value is the rounded version of the **j** parameter.

unsigned long round_jiffies_relative(unsigned long j)
:   function to round jiffies to a full second

**Parameters**

`unsigned long j`
:   the time in (relative) jiffies that should be rounded

**Description**

[`round_jiffies_relative()`](basics.md#c.round_jiffies_relative "round_jiffies_relative") rounds a time delta in the future (in jiffies)
up or down to (approximately) full seconds. This is useful for timers
for which the exact time they fire does not matter too much, as long as
they fire approximately every X seconds.

By rounding these timers to whole seconds, all such timers will fire
at the same time, rather than at various times spread out. The goal
of this is to have the CPU wake up less, which saves power.

The return value is the rounded version of the **j** parameter.

unsigned long __round_jiffies_up(unsigned long j, int cpu)
:   function to round jiffies up to a full second

**Parameters**

`unsigned long j`
:   the time in (absolute) jiffies that should be rounded

`int cpu`
:   the processor number on which the timeout will happen

**Description**

This is the same as [`__round_jiffies()`](basics.md#c.__round_jiffies "__round_jiffies") except that it will never
round down. This is useful for timeouts for which the exact time
of firing does not matter too much, as long as they don't fire too
early.

unsigned long __round_jiffies_up_relative(unsigned long j, int cpu)
:   function to round jiffies up to a full second

**Parameters**

`unsigned long j`
:   the time in (relative) jiffies that should be rounded

`int cpu`
:   the processor number on which the timeout will happen

**Description**

This is the same as [`__round_jiffies_relative()`](basics.md#c.__round_jiffies_relative "__round_jiffies_relative") except that it will never
round down. This is useful for timeouts for which the exact time
of firing does not matter too much, as long as they don't fire too
early.

unsigned long round_jiffies_up(unsigned long j)
:   function to round jiffies up to a full second

**Parameters**

`unsigned long j`
:   the time in (absolute) jiffies that should be rounded

**Description**

This is the same as [`round_jiffies()`](basics.md#c.round_jiffies "round_jiffies") except that it will never
round down. This is useful for timeouts for which the exact time
of firing does not matter too much, as long as they don't fire too
early.

unsigned long round_jiffies_up_relative(unsigned long j)
:   function to round jiffies up to a full second

**Parameters**

`unsigned long j`
:   the time in (relative) jiffies that should be rounded

**Description**

This is the same as [`round_jiffies_relative()`](basics.md#c.round_jiffies_relative "round_jiffies_relative") except that it will never
round down. This is useful for timeouts for which the exact time
of firing does not matter too much, as long as they don't fire too
early.

void init_timer_key(struct timer_list \*timer, void (\*func)(struct timer_list\*), unsigned int flags, const char \*name, struct lock_class_key \*key)
:   initialize a timer

**Parameters**

`struct timer_list *timer`
:   the timer to be initialized

`void (*func)(struct timer_list *)`
:   timer callback function

`unsigned int flags`
:   timer flags

`const char *name`
:   name of the timer

`struct lock_class_key *key`
:   lockdep class key of the fake lock used for tracking timer
    sync lock dependencies

**Description**

[`init_timer_key()`](basics.md#c.init_timer_key "init_timer_key") must be done to a timer prior calling *any* of the
other timer functions.

int mod_timer_pending(struct timer_list \*timer, unsigned long expires)
:   Modify a pending timer's timeout

**Parameters**

`struct timer_list *timer`
:   The pending timer to be modified

`unsigned long expires`
:   New absolute timeout in jiffies

**Description**

[`mod_timer_pending()`](basics.md#c.mod_timer_pending "mod_timer_pending") is the same for pending timers as [`mod_timer()`](basics.md#c.mod_timer "mod_timer"), but
will not activate inactive timers.

If **timer->function** == NULL then the start operation is silently
discarded.

**Return**

- `0` - The timer was inactive and not modified or was in
  :   shutdown state and the operation was discarded
- `1` - The timer was active and requeued to expire at **expires**

int mod_timer(struct timer_list \*timer, unsigned long expires)
:   Modify a timer's timeout

**Parameters**

`struct timer_list *timer`
:   The timer to be modified

`unsigned long expires`
:   New absolute timeout in jiffies

**Description**

mod_timer(timer, expires) is equivalent to:

> del_timer(timer); timer->expires = expires; add_timer(timer);

[`mod_timer()`](basics.md#c.mod_timer "mod_timer") is more efficient than the above open coded sequence. In
case that the timer is inactive, the del_timer() part is a NOP. The
timer is in any case activated with the new expiry time **expires**.

Note that if there are multiple unserialized concurrent users of the
same timer, then [`mod_timer()`](basics.md#c.mod_timer "mod_timer") is the only safe way to modify the timeout,
since [`add_timer()`](basics.md#c.add_timer "add_timer") cannot modify an already running timer.

If **timer->function** == NULL then the start operation is silently
discarded. In this case the return value is 0 and meaningless.

**Return**

- `0` - The timer was inactive and started or was in shutdown
  :   state and the operation was discarded
- `1` - The timer was active and requeued to expire at **expires** or
  :   the timer was active and not modified because **expires** did
      not change the effective expiry time

int timer_reduce(struct timer_list \*timer, unsigned long expires)
:   Modify a timer's timeout if it would reduce the timeout

**Parameters**

`struct timer_list *timer`
:   The timer to be modified

`unsigned long expires`
:   New absolute timeout in jiffies

**Description**

[`timer_reduce()`](basics.md#c.timer_reduce "timer_reduce") is very similar to [`mod_timer()`](basics.md#c.mod_timer "mod_timer"), except that it will only
modify an enqueued timer if that would reduce the expiration time. If
**timer** is not enqueued it starts the timer.

If **timer->function** == NULL then the start operation is silently
discarded.

**Return**

- `0` - The timer was inactive and started or was in shutdown
  :   state and the operation was discarded
- `1` - The timer was active and requeued to expire at **expires** or
  :   the timer was active and not modified because **expires**
      did not change the effective expiry time such that the
      timer would expire earlier than already scheduled

void add_timer(struct timer_list \*timer)
:   Start a timer

**Parameters**

`struct timer_list *timer`
:   The timer to be started

**Description**

Start **timer** to expire at **timer->expires** in the future. **timer->expires**
is the absolute expiry time measured in 'jiffies'. When the timer expires
timer->function(timer) will be invoked from soft interrupt context.

The **timer->expires** and **timer->function** fields must be set prior
to calling this function.

If **timer->function** == NULL then the start operation is silently
discarded.

If **timer->expires** is already in the past **timer** will be queued to
expire at the next timer tick.

This can only operate on an inactive timer. Attempts to invoke this on
an active timer are rejected with a warning.

void add_timer_on(struct timer_list \*timer, int cpu)
:   Start a timer on a particular CPU

**Parameters**

`struct timer_list *timer`
:   The timer to be started

`int cpu`
:   The CPU to start it on

**Description**

Same as [`add_timer()`](basics.md#c.add_timer "add_timer") except that it starts the timer on the given CPU.

See [`add_timer()`](basics.md#c.add_timer "add_timer") for further details.

int timer_delete(struct timer_list \*timer)
:   Deactivate a timer

**Parameters**

`struct timer_list *timer`
:   The timer to be deactivated

**Description**

The function only deactivates a pending timer, but contrary to
[`timer_delete_sync()`](basics.md#c.timer_delete_sync "timer_delete_sync") it does not take into account whether the timer's
callback function is concurrently executed on a different CPU or not.
It neither prevents rearming of the timer. If **timer** can be rearmed
concurrently then the return value of this function is meaningless.

**Return**

- `0` - The timer was not pending
- `1` - The timer was pending and deactivated

int timer_shutdown(struct timer_list \*timer)
:   Deactivate a timer and prevent rearming

**Parameters**

`struct timer_list *timer`
:   The timer to be deactivated

**Description**

The function does not wait for an eventually running timer callback on a
different CPU but it prevents rearming of the timer. Any attempt to arm
**timer** after this function returns will be silently ignored.

This function is useful for teardown code and should only be used when
[`timer_shutdown_sync()`](basics.md#c.timer_shutdown_sync "timer_shutdown_sync") cannot be invoked due to locking or context constraints.

**Return**

- `0` - The timer was not pending
- `1` - The timer was pending

int try_to_del_timer_sync(struct timer_list \*timer)
:   Try to deactivate a timer

**Parameters**

`struct timer_list *timer`
:   Timer to deactivate

**Description**

This function tries to deactivate a timer. On success the timer is not
queued and the timer callback function is not running on any CPU.

This function does not guarantee that the timer cannot be rearmed right
after dropping the base lock. That needs to be prevented by the calling
code if necessary.

**Return**

- `0` - The timer was not pending
- `1` - The timer was pending and deactivated
- `-1` - The timer callback function is running on a different CPU

int timer_delete_sync(struct timer_list \*timer)
:   Deactivate a timer and wait for the handler to finish.

**Parameters**

`struct timer_list *timer`
:   The timer to be deactivated

**Description**

Synchronization rules: Callers must prevent restarting of the timer,
otherwise this function is meaningless. It must not be called from
interrupt contexts unless the timer is an irqsafe one. The caller must
not hold locks which would prevent completion of the timer's callback
function. The timer's handler must not call [`add_timer_on()`](basics.md#c.add_timer_on "add_timer_on"). Upon exit
the timer is not queued and the handler is not running on any CPU.

For !irqsafe timers, the caller must not hold locks that are held in
interrupt context. Even if the lock has nothing to do with the timer in
question. Here's why:

```
CPU0                             CPU1
----                             ----
                                 <SOFTIRQ>
                                   call_timer_fn();
                                   base->running_timer = mytimer;
spin_lock_irq(somelock);
                                 <IRQ>
                                    spin_lock(somelock);
timer_delete_sync(mytimer);
while (base->running_timer == mytimer);
```

Now [`timer_delete_sync()`](basics.md#c.timer_delete_sync "timer_delete_sync") will never return and never release somelock.
The interrupt on the other CPU is waiting to grab somelock but it has
interrupted the softirq that CPU0 is waiting to finish.

This function cannot guarantee that the timer is not rearmed again by
some concurrent or preempting code, right after it dropped the base
lock. If there is the possibility of a concurrent rearm then the return
value of the function is meaningless.

If such a guarantee is needed, e.g. for teardown situations then use
[`timer_shutdown_sync()`](basics.md#c.timer_shutdown_sync "timer_shutdown_sync") instead.

**Return**

- `0` - The timer was not pending
- `1` - The timer was pending and deactivated

int timer_shutdown_sync(struct timer_list \*timer)
:   Shutdown a timer and prevent rearming

**Parameters**

`struct timer_list *timer`
:   The timer to be shutdown

**Description**

When the function returns it is guaranteed that:
:   - **timer** is not queued
    - The callback function of **timer** is not running
    - **timer** cannot be enqueued again. Any attempt to rearm
      **timer** is silently ignored.

See [`timer_delete_sync()`](basics.md#c.timer_delete_sync "timer_delete_sync") for synchronization rules.

This function is useful for final teardown of an infrastructure where
the timer is subject to a circular dependency problem.

A common pattern for this is a timer and a workqueue where the timer can
schedule work and work can arm the timer. On shutdown the workqueue must
be destroyed and the timer must be prevented from rearming. Unless the
code has conditionals like 'if (mything->in_shutdown)' to prevent that
there is no way to get this correct with [`timer_delete_sync()`](basics.md#c.timer_delete_sync "timer_delete_sync").

[`timer_shutdown_sync()`](basics.md#c.timer_shutdown_sync "timer_shutdown_sync") is solving the problem. The correct ordering of
calls in this case is:

> timer_shutdown_sync(`mything->timer`);
> workqueue_destroy(`mything->workqueue`);

After this 'mything' can be safely freed.

This obviously implies that the timer is not required to be functional
for the rest of the shutdown operation.

**Return**

- `0` - The timer was not pending
- `1` - The timer was pending

signed long schedule_timeout(signed long timeout)
:   sleep until timeout

**Parameters**

`signed long timeout`
:   timeout value in jiffies

**Description**

Make the current task sleep until **timeout** jiffies have elapsed.
The function behavior depends on the current task state
(see also set_current_state() description):

`TASK_RUNNING` - the scheduler is called, but the task does not sleep
at all. That happens because sched_submit_work() does nothing for
tasks in `TASK_RUNNING` state.

`TASK_UNINTERRUPTIBLE` - at least **timeout** jiffies are guaranteed to
pass before the routine returns unless the current task is explicitly
woken up, (e.g. by [`wake_up_process()`](basics.md#c.wake_up_process "wake_up_process")).

`TASK_INTERRUPTIBLE` - the routine may return early if a signal is
delivered to the current task or the current task is explicitly woken
up.

The current task state is guaranteed to be `TASK_RUNNING` when this
routine returns.

Specifying a **timeout** value of `MAX_SCHEDULE_TIMEOUT` will schedule
the CPU away without a bound on the timeout. In this case the return
value will be `MAX_SCHEDULE_TIMEOUT`.

Returns 0 when the timer has expired otherwise the remaining time in
jiffies will be returned. In all cases the return value is guaranteed
to be non-negative.

void msleep(unsigned int msecs)
:   sleep safely even with waitqueue interruptions

**Parameters**

`unsigned int msecs`
:   Time in milliseconds to sleep for

unsigned long msleep_interruptible(unsigned int msecs)
:   sleep waiting for signals

**Parameters**

`unsigned int msecs`
:   Time in milliseconds to sleep for

void usleep_range_state(unsigned long min, unsigned long max, unsigned int state)
:   Sleep for an approximate time in a given state

**Parameters**

`unsigned long min`
:   Minimum time in usecs to sleep

`unsigned long max`
:   Maximum time in usecs to sleep

`unsigned int state`
:   State of the current task that will be while sleeping

**Description**

In non-atomic context where the exact wakeup time is flexible, use
[`usleep_range_state()`](basics.md#c.usleep_range_state "usleep_range_state") instead of udelay(). The sleep improves responsiveness
by avoiding the CPU-hogging busy-wait of udelay(), and the range reduces
power usage by allowing hrtimers to take advantage of an already-
scheduled interrupt instead of scheduling a new one just for this sleep.

## High-resolution timers

ktime_t ktime_set(const s64 secs, const unsigned long nsecs)
:   Set a ktime_t variable from a seconds/nanoseconds value

**Parameters**

`const s64 secs`
:   seconds to set

`const unsigned long nsecs`
:   nanoseconds to set

**Return**

The ktime_t representation of the value.

int ktime_compare(const ktime_t cmp1, const ktime_t cmp2)
:   Compares two ktime_t variables for less, greater or equal

**Parameters**

`const ktime_t cmp1`
:   comparable1

`const ktime_t cmp2`
:   comparable2

**Return**

...
:   cmp1 < cmp2: return <0
    cmp1 == cmp2: return 0
    cmp1 > cmp2: return >0

bool ktime_after(const ktime_t cmp1, const ktime_t cmp2)
:   Compare if a ktime_t value is bigger than another one.

**Parameters**

`const ktime_t cmp1`
:   comparable1

`const ktime_t cmp2`
:   comparable2

**Return**

true if cmp1 happened after cmp2.

bool ktime_before(const ktime_t cmp1, const ktime_t cmp2)
:   Compare if a ktime_t value is smaller than another one.

**Parameters**

`const ktime_t cmp1`
:   comparable1

`const ktime_t cmp2`
:   comparable2

**Return**

true if cmp1 happened before cmp2.

bool ktime_to_timespec64_cond(const ktime_t kt, struct timespec64 \*ts)
:   convert a ktime_t variable to timespec64 format only if the variable contains data

**Parameters**

`const ktime_t kt`
:   the ktime_t variable to convert

`struct timespec64 *ts`
:   the timespec variable to store the result in

**Return**

`true` if there was a successful conversion, `false` if kt was 0.

struct hrtimer_sleeper
:   simple sleeper structure

**Definition**:

```
struct hrtimer_sleeper {
    struct hrtimer timer;
    struct task_struct *task;
};
```

**Members**

`timer`
:   embedded timer structure

`task`
:   task to wake up

**Description**

task is set to NULL, when the timer expires.

struct hrtimer_clock_base
:   the timer base for a specific clock

**Definition**:

```
struct hrtimer_clock_base {
    struct hrtimer_cpu_base *cpu_base;
    unsigned int            index;
    clockid_t clockid;
    seqcount_raw_spinlock_t seq;
    struct hrtimer          *running;
    struct timerqueue_head  active;
    ktime_t (*get_time)(void);
    ktime_t offset;
};
```

**Members**

`cpu_base`
:   per cpu clock base

`index`
:   clock type index for per_cpu support when moving a
    timer to a base on another cpu.

`clockid`
:   clock id for per_cpu support

`seq`
:   seqcount around __run_hrtimer

`running`
:   pointer to the currently running hrtimer

`active`
:   red black tree root node for the active timers

`get_time`
:   function to retrieve the current time of the clock

`offset`
:   offset of this clock to the monotonic base

struct hrtimer_cpu_base
:   the per cpu clock bases

**Definition**:

```
struct hrtimer_cpu_base {
    raw_spinlock_t lock;
    unsigned int                    cpu;
    unsigned int                    active_bases;
    unsigned int                    clock_was_set_seq;
    unsigned int                    hres_active             : 1,in_hrtirq               : 1,hang_detected           : 1,softirq_activated       : 1, online                  : 1;
#ifdef CONFIG_HIGH_RES_TIMERS;
    unsigned int                    nr_events;
    unsigned short                  nr_retries;
    unsigned short                  nr_hangs;
    unsigned int                    max_hang_time;
#endif;
#ifdef CONFIG_PREEMPT_RT;
    spinlock_t softirq_expiry_lock;
    atomic_t timer_waiters;
#endif;
    ktime_t expires_next;
    struct hrtimer                  *next_timer;
    ktime_t softirq_expires_next;
    struct hrtimer                  *softirq_next_timer;
    struct hrtimer_clock_base       clock_base[HRTIMER_MAX_CLOCK_BASES];
};
```

**Members**

`lock`
:   lock protecting the base and associated clock bases
    and timers

`cpu`
:   cpu number

`active_bases`
:   Bitfield to mark bases with active timers

`clock_was_set_seq`
:   Sequence counter of clock was set events

`hres_active`
:   State of high resolution mode

`in_hrtirq`
:   hrtimer_interrupt() is currently executing

`hang_detected`
:   The last hrtimer interrupt detected a hang

`softirq_activated`
:   displays, if the softirq is raised - update of softirq
    related settings is not required then.

`online`
:   CPU is online from an hrtimers point of view

`nr_events`
:   Total number of hrtimer interrupt events

`nr_retries`
:   Total number of hrtimer interrupt retries

`nr_hangs`
:   Total number of hrtimer interrupt hangs

`max_hang_time`
:   Maximum time spent in hrtimer_interrupt

`softirq_expiry_lock`
:   Lock which is taken while softirq based hrtimer are
    expired

`timer_waiters`
:   A [`hrtimer_cancel()`](basics.md#c.hrtimer_cancel "hrtimer_cancel") invocation waits for the timer
    callback to finish.

`expires_next`
:   absolute time of the next event, is required for remote
    hrtimer enqueue; it is the total first expiry time (hard
    and soft hrtimer are taken into account)

`next_timer`
:   Pointer to the first expiring timer

`softirq_expires_next`
:   Time to check, if soft queues needs also to be expired

`softirq_next_timer`
:   Pointer to the first expiring softirq based timer

`clock_base`
:   array of clock bases for this cpu

**Note**

next_timer is just an optimization for __remove_hrtimer().
:   Do not dereference the pointer because it is not reliable on
    cross cpu removals.

void hrtimer_start(struct hrtimer \*timer, ktime_t tim, const enum hrtimer_mode mode)
:   (re)start an hrtimer

**Parameters**

`struct hrtimer *timer`
:   the timer to be added

`ktime_t tim`
:   expiry time

`const enum hrtimer_mode mode`
:   timer mode: absolute (HRTIMER_MODE_ABS) or
    relative (HRTIMER_MODE_REL), and pinned (HRTIMER_MODE_PINNED);
    softirq based mode is considered for debug purpose only!

ktime_t hrtimer_get_remaining(const struct hrtimer \*timer)
:   get remaining time for the timer

**Parameters**

`const struct hrtimer *timer`
:   the timer to read

bool hrtimer_is_queued(struct hrtimer \*timer)
:   check, whether the timer is on one of the queues

**Parameters**

`struct hrtimer *timer`
:   Timer to check

**Return**

True if the timer is queued, false otherwise

**Description**

The function can be used lockless, but it gives only a current snapshot.

u64 hrtimer_forward_now(struct hrtimer \*timer, ktime_t interval)
:   forward the timer expiry so it expires after now

**Parameters**

`struct hrtimer *timer`
:   hrtimer to forward

`ktime_t interval`
:   the interval to forward

**Description**

Forward the timer expiry so it will expire after the current time
of the hrtimer clock base. Returns the number of overruns.

Can be safely called from the callback function of **timer**. If
called from other contexts **timer** must neither be enqueued nor
running the callback and the caller needs to take care of
serialization.

**Note**

This only updates the timer expiry value and does not requeue
the timer.

u64 hrtimer_forward(struct hrtimer \*timer, ktime_t now, ktime_t interval)
:   forward the timer expiry

**Parameters**

`struct hrtimer *timer`
:   hrtimer to forward

`ktime_t now`
:   forward past this time

`ktime_t interval`
:   the interval to forward

**Description**

Forward the timer expiry so it will expire in the future.
Returns the number of overruns.

Can be safely called from the callback function of **timer**. If
called from other contexts **timer** must neither be enqueued nor
running the callback and the caller needs to take care of
serialization.

**Note**

This only updates the timer expiry value and does not requeue
the timer.

void hrtimer_start_range_ns(struct hrtimer \*timer, ktime_t tim, u64 delta_ns, const enum hrtimer_mode mode)
:   (re)start an hrtimer

**Parameters**

`struct hrtimer *timer`
:   the timer to be added

`ktime_t tim`
:   expiry time

`u64 delta_ns`
:   "slack" range for the timer

`const enum hrtimer_mode mode`
:   timer mode: absolute (HRTIMER_MODE_ABS) or
    relative (HRTIMER_MODE_REL), and pinned (HRTIMER_MODE_PINNED);
    softirq based mode is considered for debug purpose only!

int hrtimer_try_to_cancel(struct hrtimer \*timer)
:   try to deactivate a timer

**Parameters**

`struct hrtimer *timer`
:   hrtimer to stop

**Return**

> - 0 when the timer was not active
> - 1 when the timer was active
> - -1 when the timer is currently executing the callback function and
>   cannot be stopped

int hrtimer_cancel(struct hrtimer \*timer)
:   cancel a timer and wait for the handler to finish.

**Parameters**

`struct hrtimer *timer`
:   the timer to be cancelled

**Return**

> 0 when the timer was not active
> 1 when the timer was active

ktime_t __hrtimer_get_remaining(const struct hrtimer \*timer, bool adjust)
:   get remaining time for the timer

**Parameters**

`const struct hrtimer *timer`
:   the timer to read

`bool adjust`
:   adjust relative timers when CONFIG_TIME_LOW_RES=y

void hrtimer_init(struct hrtimer \*timer, clockid_t clock_id, enum hrtimer_mode mode)
:   initialize a timer to the given clock

**Parameters**

`struct hrtimer *timer`
:   the timer to be initialized

`clockid_t clock_id`
:   the clock to be used

`enum hrtimer_mode mode`
:   The modes which are relevant for initialization:
    HRTIMER_MODE_ABS, HRTIMER_MODE_REL, HRTIMER_MODE_ABS_SOFT,
    HRTIMER_MODE_REL_SOFT

    The PINNED variants of the above can be handed in,
    but the PINNED bit is ignored as pinning happens
    when the hrtimer is started

void hrtimer_sleeper_start_expires(struct [hrtimer_sleeper](basics.md#c.hrtimer_sleeper "hrtimer_sleeper") \*sl, enum hrtimer_mode mode)
:   Start a hrtimer sleeper timer

**Parameters**

`struct hrtimer_sleeper *sl`
:   sleeper to be started

`enum hrtimer_mode mode`
:   timer mode abs/rel

**Description**

Wrapper around hrtimer_start_expires() for hrtimer_sleeper based timers
to allow PREEMPT_RT to tweak the delivery mode (soft/hardirq context)

void hrtimer_init_sleeper(struct [hrtimer_sleeper](basics.md#c.hrtimer_sleeper "hrtimer_sleeper") \*sl, clockid_t clock_id, enum hrtimer_mode mode)
:   initialize sleeper to the given clock

**Parameters**

`struct hrtimer_sleeper *sl`
:   sleeper to be initialized

`clockid_t clock_id`
:   the clock to be used

`enum hrtimer_mode mode`
:   timer mode abs/rel

int schedule_hrtimeout_range_clock(ktime_t \*expires, u64 delta, const enum hrtimer_mode mode, clockid_t clock_id)
:   sleep until timeout

**Parameters**

`ktime_t *expires`
:   timeout value (ktime_t)

`u64 delta`
:   slack in expires timeout (ktime_t) for SCHED_OTHER tasks

`const enum hrtimer_mode mode`
:   timer mode

`clockid_t clock_id`
:   timer clock to be used

int schedule_hrtimeout_range(ktime_t \*expires, u64 delta, const enum hrtimer_mode mode)
:   sleep until timeout

**Parameters**

`ktime_t *expires`
:   timeout value (ktime_t)

`u64 delta`
:   slack in expires timeout (ktime_t) for SCHED_OTHER tasks

`const enum hrtimer_mode mode`
:   timer mode

**Description**

Make the current task sleep until the given expiry time has
elapsed. The routine will return immediately unless
the current task state has been set (see set_current_state()).

The **delta** argument gives the kernel the freedom to schedule the
actual wakeup to a time that is both power and performance friendly
for regular (non RT/DL) tasks.
The kernel give the normal best effort behavior for "**expires\*\*+\*\*delta**",
but may decide to fire the timer earlier, but no earlier than **expires**.

You can set the task state as follows -

`TASK_UNINTERRUPTIBLE` - at least **timeout** time is guaranteed to
pass before the routine returns unless the current task is explicitly
woken up, (e.g. by [`wake_up_process()`](basics.md#c.wake_up_process "wake_up_process")).

`TASK_INTERRUPTIBLE` - the routine may return early if a signal is
delivered to the current task or the current task is explicitly woken
up.

The current task state is guaranteed to be TASK_RUNNING when this
routine returns.

Returns 0 when the timer has expired. If the task was woken before the
timer expired by a signal (only possible in state TASK_INTERRUPTIBLE) or
by an explicit wakeup, it returns -EINTR.

int schedule_hrtimeout(ktime_t \*expires, const enum hrtimer_mode mode)
:   sleep until timeout

**Parameters**

`ktime_t *expires`
:   timeout value (ktime_t)

`const enum hrtimer_mode mode`
:   timer mode

**Description**

Make the current task sleep until the given expiry time has
elapsed. The routine will return immediately unless
the current task state has been set (see set_current_state()).

You can set the task state as follows -

`TASK_UNINTERRUPTIBLE` - at least **timeout** time is guaranteed to
pass before the routine returns unless the current task is explicitly
woken up, (e.g. by [`wake_up_process()`](basics.md#c.wake_up_process "wake_up_process")).

`TASK_INTERRUPTIBLE` - the routine may return early if a signal is
delivered to the current task or the current task is explicitly woken
up.

The current task state is guaranteed to be TASK_RUNNING when this
routine returns.

Returns 0 when the timer has expired. If the task was woken before the
timer expired by a signal (only possible in state TASK_INTERRUPTIBLE) or
by an explicit wakeup, it returns -EINTR.

## Wait queues and Wake events

int waitqueue_active(struct wait_queue_head \*wq_head)
:   - locklessly test for waiters on the queue

**Parameters**

`struct wait_queue_head *wq_head`
:   the waitqueue to test for waiters

**Description**

returns true if the wait list is not empty

Use either while holding wait_queue_head::lock or when used for wakeups
with an extra smp_mb() like:

```
CPU0 - waker                    CPU1 - waiter

                                for (;;) {
@cond = true;                     prepare_to_wait(&wq_head, &wait, state);
smp_mb();                         // smp_mb() from set_current_state()
if (waitqueue_active(wq_head))         if (@cond)
  wake_up(wq_head);                      break;
                                  schedule();
                                }
                                finish_wait(&wq_head, &wait);
```

Because without the explicit smp_mb() it's possible for the
[`waitqueue_active()`](basics.md#c.waitqueue_active "waitqueue_active") load to get hoisted over the **cond** store such that we'll
observe an empty wait list while the waiter might not observe **cond**.

Also note that this 'optimization' trades a spin_lock() for an smp_mb(),
which (when the lock is uncontended) are of roughly equal cost.

**NOTE**

this function is lockless and requires care, incorrect usage _will_
lead to sporadic and non-obvious failure.

bool wq_has_single_sleeper(struct wait_queue_head \*wq_head)
:   check if there is only one sleeper

**Parameters**

`struct wait_queue_head *wq_head`
:   wait queue head

**Description**

Returns true of wq_head has only one sleeper on the list.

Please refer to the comment for waitqueue_active.

bool wq_has_sleeper(struct wait_queue_head \*wq_head)
:   check if there are any waiting processes

**Parameters**

`struct wait_queue_head *wq_head`
:   wait queue head

**Description**

Returns true if wq_head has waiting processes

Please refer to the comment for waitqueue_active.

void wake_up_pollfree(struct wait_queue_head \*wq_head)
:   signal that a polled waitqueue is going away

**Parameters**

`struct wait_queue_head *wq_head`
:   the wait queue head

**Description**

In the very rare cases where a ->poll() implementation uses a waitqueue whose
lifetime is tied to a task rather than to the 'struct file' being polled,
this function must be called before the waitqueue is freed so that
non-blocking polls (e.g. epoll) are notified that the queue is going away.

The caller must also RCU-delay the freeing of the wait_queue_head, e.g. via
an explicit [`synchronize_rcu()`](../core-api/kernel-api.md#c.synchronize_rcu "synchronize_rcu") or [`call_rcu()`](../core-api/kernel-api.md#c.call_rcu "call_rcu"), or via SLAB_TYPESAFE_BY_RCU.

wait_event

`wait_event (wq_head, condition)`

> sleep until a condition gets true

**Parameters**

`wq_head`
:   the waitqueue to wait on

`condition`
:   a C expression for the event to wait for

**Description**

The process is put to sleep (TASK_UNINTERRUPTIBLE) until the
**condition** evaluates to true. The **condition** is checked each time
the waitqueue **wq_head** is woken up.

wake_up() has to be called after changing any variable that could
change the result of the wait condition.

wait_event_freezable

`wait_event_freezable (wq_head, condition)`

> sleep (or freeze) until a condition gets true

**Parameters**

`wq_head`
:   the waitqueue to wait on

`condition`
:   a C expression for the event to wait for

**Description**

The process is put to sleep (TASK_INTERRUPTIBLE -- so as not to contribute
to system load) until the **condition** evaluates to true. The
**condition** is checked each time the waitqueue **wq_head** is woken up.

wake_up() has to be called after changing any variable that could
change the result of the wait condition.

wait_event_timeout

`wait_event_timeout (wq_head, condition, timeout)`

> sleep until a condition gets true or a timeout elapses

**Parameters**

`wq_head`
:   the waitqueue to wait on

`condition`
:   a C expression for the event to wait for

`timeout`
:   timeout, in jiffies

**Description**

The process is put to sleep (TASK_UNINTERRUPTIBLE) until the
**condition** evaluates to true. The **condition** is checked each time
the waitqueue **wq_head** is woken up.

wake_up() has to be called after changing any variable that could
change the result of the wait condition.

**Return**

0 if the **condition** evaluated to `false` after the **timeout** elapsed,
1 if the **condition** evaluated to `true` after the **timeout** elapsed,
or the remaining jiffies (at least 1) if the **condition** evaluated
to `true` before the **timeout** elapsed.

wait_event_cmd

`wait_event_cmd (wq_head, condition, cmd1, cmd2)`

> sleep until a condition gets true

**Parameters**

`wq_head`
:   the waitqueue to wait on

`condition`
:   a C expression for the event to wait for

`cmd1`
:   the command will be executed before sleep

`cmd2`
:   the command will be executed after sleep

**Description**

The process is put to sleep (TASK_UNINTERRUPTIBLE) until the
**condition** evaluates to true. The **condition** is checked each time
the waitqueue **wq_head** is woken up.

wake_up() has to be called after changing any variable that could
change the result of the wait condition.

wait_event_interruptible

`wait_event_interruptible (wq_head, condition)`

> sleep until a condition gets true

**Parameters**

`wq_head`
:   the waitqueue to wait on

`condition`
:   a C expression for the event to wait for

**Description**

The process is put to sleep (TASK_INTERRUPTIBLE) until the
**condition** evaluates to true or a signal is received.
The **condition** is checked each time the waitqueue **wq_head** is woken up.

wake_up() has to be called after changing any variable that could
change the result of the wait condition.

The function will return -ERESTARTSYS if it was interrupted by a
signal and 0 if **condition** evaluated to true.

wait_event_interruptible_timeout

`wait_event_interruptible_timeout (wq_head, condition, timeout)`

> sleep until a condition gets true or a timeout elapses

**Parameters**

`wq_head`
:   the waitqueue to wait on

`condition`
:   a C expression for the event to wait for

`timeout`
:   timeout, in jiffies

**Description**

The process is put to sleep (TASK_INTERRUPTIBLE) until the
**condition** evaluates to true or a signal is received.
The **condition** is checked each time the waitqueue **wq_head** is woken up.

wake_up() has to be called after changing any variable that could
change the result of the wait condition.

**Return**

0 if the **condition** evaluated to `false` after the **timeout** elapsed,
1 if the **condition** evaluated to `true` after the **timeout** elapsed,
the remaining jiffies (at least 1) if the **condition** evaluated
to `true` before the **timeout** elapsed, or -`ERESTARTSYS` if it was
interrupted by a signal.

wait_event_hrtimeout

`wait_event_hrtimeout (wq_head, condition, timeout)`

> sleep until a condition gets true or a timeout elapses

**Parameters**

`wq_head`
:   the waitqueue to wait on

`condition`
:   a C expression for the event to wait for

`timeout`
:   timeout, as a ktime_t

**Description**

The process is put to sleep (TASK_UNINTERRUPTIBLE) until the
**condition** evaluates to true or a signal is received.
The **condition** is checked each time the waitqueue **wq_head** is woken up.

wake_up() has to be called after changing any variable that could
change the result of the wait condition.

The function returns 0 if **condition** became true, or -ETIME if the timeout
elapsed.

wait_event_interruptible_hrtimeout

`wait_event_interruptible_hrtimeout (wq, condition, timeout)`

> sleep until a condition gets true or a timeout elapses

**Parameters**

`wq`
:   the waitqueue to wait on

`condition`
:   a C expression for the event to wait for

`timeout`
:   timeout, as a ktime_t

**Description**

The process is put to sleep (TASK_INTERRUPTIBLE) until the
**condition** evaluates to true or a signal is received.
The **condition** is checked each time the waitqueue **wq** is woken up.

wake_up() has to be called after changing any variable that could
change the result of the wait condition.

The function returns 0 if **condition** became true, -ERESTARTSYS if it was
interrupted by a signal, or -ETIME if the timeout elapsed.

wait_event_idle

`wait_event_idle (wq_head, condition)`

> wait for a condition without contributing to system load

**Parameters**

`wq_head`
:   the waitqueue to wait on

`condition`
:   a C expression for the event to wait for

**Description**

The process is put to sleep (TASK_IDLE) until the
**condition** evaluates to true.
The **condition** is checked each time the waitqueue **wq_head** is woken up.

wake_up() has to be called after changing any variable that could
change the result of the wait condition.

wait_event_idle_exclusive

`wait_event_idle_exclusive (wq_head, condition)`

> wait for a condition with contributing to system load

**Parameters**

`wq_head`
:   the waitqueue to wait on

`condition`
:   a C expression for the event to wait for

**Description**

The process is put to sleep (TASK_IDLE) until the
**condition** evaluates to true.
The **condition** is checked each time the waitqueue **wq_head** is woken up.

The process is put on the wait queue with an WQ_FLAG_EXCLUSIVE flag
set thus if other processes wait on the same list, when this
process is woken further processes are not considered.

wake_up() has to be called after changing any variable that could
change the result of the wait condition.

wait_event_idle_timeout

`wait_event_idle_timeout (wq_head, condition, timeout)`

> sleep without load until a condition becomes true or a timeout elapses

**Parameters**

`wq_head`
:   the waitqueue to wait on

`condition`
:   a C expression for the event to wait for

`timeout`
:   timeout, in jiffies

**Description**

The process is put to sleep (TASK_IDLE) until the
**condition** evaluates to true. The **condition** is checked each time
the waitqueue **wq_head** is woken up.

wake_up() has to be called after changing any variable that could
change the result of the wait condition.

**Return**

0 if the **condition** evaluated to `false` after the **timeout** elapsed,
1 if the **condition** evaluated to `true` after the **timeout** elapsed,
or the remaining jiffies (at least 1) if the **condition** evaluated
to `true` before the **timeout** elapsed.

wait_event_idle_exclusive_timeout

`wait_event_idle_exclusive_timeout (wq_head, condition, timeout)`

> sleep without load until a condition becomes true or a timeout elapses

**Parameters**

`wq_head`
:   the waitqueue to wait on

`condition`
:   a C expression for the event to wait for

`timeout`
:   timeout, in jiffies

**Description**

The process is put to sleep (TASK_IDLE) until the
**condition** evaluates to true. The **condition** is checked each time
the waitqueue **wq_head** is woken up.

The process is put on the wait queue with an WQ_FLAG_EXCLUSIVE flag
set thus if other processes wait on the same list, when this
process is woken further processes are not considered.

wake_up() has to be called after changing any variable that could
change the result of the wait condition.

**Return**

0 if the **condition** evaluated to `false` after the **timeout** elapsed,
1 if the **condition** evaluated to `true` after the **timeout** elapsed,
or the remaining jiffies (at least 1) if the **condition** evaluated
to `true` before the **timeout** elapsed.

wait_event_interruptible_locked

`wait_event_interruptible_locked (wq, condition)`

> sleep until a condition gets true

**Parameters**

`wq`
:   the waitqueue to wait on

`condition`
:   a C expression for the event to wait for

**Description**

The process is put to sleep (TASK_INTERRUPTIBLE) until the
**condition** evaluates to true or a signal is received.
The **condition** is checked each time the waitqueue **wq** is woken up.

It must be called with wq.lock being held. This spinlock is
unlocked while sleeping but **condition** testing is done while lock
is held and when this macro exits the lock is held.

The lock is locked/unlocked using spin_lock()/spin_unlock()
functions which must match the way they are locked/unlocked outside
of this macro.

wake_up_locked() has to be called after changing any variable that could
change the result of the wait condition.

The function will return -ERESTARTSYS if it was interrupted by a
signal and 0 if **condition** evaluated to true.

wait_event_interruptible_locked_irq

`wait_event_interruptible_locked_irq (wq, condition)`

> sleep until a condition gets true

**Parameters**

`wq`
:   the waitqueue to wait on

`condition`
:   a C expression for the event to wait for

**Description**

The process is put to sleep (TASK_INTERRUPTIBLE) until the
**condition** evaluates to true or a signal is received.
The **condition** is checked each time the waitqueue **wq** is woken up.

It must be called with wq.lock being held. This spinlock is
unlocked while sleeping but **condition** testing is done while lock
is held and when this macro exits the lock is held.

The lock is locked/unlocked using spin_lock_irq()/spin_unlock_irq()
functions which must match the way they are locked/unlocked outside
of this macro.

wake_up_locked() has to be called after changing any variable that could
change the result of the wait condition.

The function will return -ERESTARTSYS if it was interrupted by a
signal and 0 if **condition** evaluated to true.

wait_event_interruptible_exclusive_locked

`wait_event_interruptible_exclusive_locked (wq, condition)`

> sleep exclusively until a condition gets true

**Parameters**

`wq`
:   the waitqueue to wait on

`condition`
:   a C expression for the event to wait for

**Description**

The process is put to sleep (TASK_INTERRUPTIBLE) until the
**condition** evaluates to true or a signal is received.
The **condition** is checked each time the waitqueue **wq** is woken up.

It must be called with wq.lock being held. This spinlock is
unlocked while sleeping but **condition** testing is done while lock
is held and when this macro exits the lock is held.

The lock is locked/unlocked using spin_lock()/spin_unlock()
functions which must match the way they are locked/unlocked outside
of this macro.

The process is put on the wait queue with an WQ_FLAG_EXCLUSIVE flag
set thus when other process waits process on the list if this
process is awaken further processes are not considered.

wake_up_locked() has to be called after changing any variable that could
change the result of the wait condition.

The function will return -ERESTARTSYS if it was interrupted by a
signal and 0 if **condition** evaluated to true.

wait_event_interruptible_exclusive_locked_irq

`wait_event_interruptible_exclusive_locked_irq (wq, condition)`

> sleep until a condition gets true

**Parameters**

`wq`
:   the waitqueue to wait on

`condition`
:   a C expression for the event to wait for

**Description**

The process is put to sleep (TASK_INTERRUPTIBLE) until the
**condition** evaluates to true or a signal is received.
The **condition** is checked each time the waitqueue **wq** is woken up.

It must be called with wq.lock being held. This spinlock is
unlocked while sleeping but **condition** testing is done while lock
is held and when this macro exits the lock is held.

The lock is locked/unlocked using spin_lock_irq()/spin_unlock_irq()
functions which must match the way they are locked/unlocked outside
of this macro.

The process is put on the wait queue with an WQ_FLAG_EXCLUSIVE flag
set thus when other process waits process on the list if this
process is awaken further processes are not considered.

wake_up_locked() has to be called after changing any variable that could
change the result of the wait condition.

The function will return -ERESTARTSYS if it was interrupted by a
signal and 0 if **condition** evaluated to true.

wait_event_killable

`wait_event_killable (wq_head, condition)`

> sleep until a condition gets true

**Parameters**

`wq_head`
:   the waitqueue to wait on

`condition`
:   a C expression for the event to wait for

**Description**

The process is put to sleep (TASK_KILLABLE) until the
**condition** evaluates to true or a signal is received.
The **condition** is checked each time the waitqueue **wq_head** is woken up.

wake_up() has to be called after changing any variable that could
change the result of the wait condition.

The function will return -ERESTARTSYS if it was interrupted by a
signal and 0 if **condition** evaluated to true.

wait_event_state

`wait_event_state (wq_head, condition, state)`

> sleep until a condition gets true

**Parameters**

`wq_head`
:   the waitqueue to wait on

`condition`
:   a C expression for the event to wait for

`state`
:   state to sleep in

**Description**

The process is put to sleep (**state**) until the **condition** evaluates to true
or a signal is received (when allowed by **state**). The **condition** is checked
each time the waitqueue **wq_head** is woken up.

wake_up() has to be called after changing any variable that could
change the result of the wait condition.

The function will return -ERESTARTSYS if it was interrupted by a signal
(when allowed by **state**) and 0 if **condition** evaluated to true.

wait_event_killable_timeout

`wait_event_killable_timeout (wq_head, condition, timeout)`

> sleep until a condition gets true or a timeout elapses

**Parameters**

`wq_head`
:   the waitqueue to wait on

`condition`
:   a C expression for the event to wait for

`timeout`
:   timeout, in jiffies

**Description**

The process is put to sleep (TASK_KILLABLE) until the
**condition** evaluates to true or a kill signal is received.
The **condition** is checked each time the waitqueue **wq_head** is woken up.

wake_up() has to be called after changing any variable that could
change the result of the wait condition.

Only kill signals interrupt this process.

**Return**

0 if the **condition** evaluated to `false` after the **timeout** elapsed,
1 if the **condition** evaluated to `true` after the **timeout** elapsed,
the remaining jiffies (at least 1) if the **condition** evaluated
to `true` before the **timeout** elapsed, or -`ERESTARTSYS` if it was
interrupted by a kill signal.

wait_event_lock_irq_cmd

`wait_event_lock_irq_cmd (wq_head, condition, lock, cmd)`

> sleep until a condition gets true. The condition is checked under the lock. This is expected to be called with the lock taken.

**Parameters**

`wq_head`
:   the waitqueue to wait on

`condition`
:   a C expression for the event to wait for

`lock`
:   a locked spinlock_t, which will be released before cmd
    and schedule() and reacquired afterwards.

`cmd`
:   a command which is invoked outside the critical section before
    sleep

**Description**

The process is put to sleep (TASK_UNINTERRUPTIBLE) until the
**condition** evaluates to true. The **condition** is checked each time
the waitqueue **wq_head** is woken up.

wake_up() has to be called after changing any variable that could
change the result of the wait condition.

This is supposed to be called while holding the lock. The lock is
dropped before invoking the cmd and going to sleep and is reacquired
afterwards.

wait_event_lock_irq

`wait_event_lock_irq (wq_head, condition, lock)`

> sleep until a condition gets true. The condition is checked under the lock. This is expected to be called with the lock taken.

**Parameters**

`wq_head`
:   the waitqueue to wait on

`condition`
:   a C expression for the event to wait for

`lock`
:   a locked spinlock_t, which will be released before schedule()
    and reacquired afterwards.

**Description**

The process is put to sleep (TASK_UNINTERRUPTIBLE) until the
**condition** evaluates to true. The **condition** is checked each time
the waitqueue **wq_head** is woken up.

wake_up() has to be called after changing any variable that could
change the result of the wait condition.

This is supposed to be called while holding the lock. The lock is
dropped before going to sleep and is reacquired afterwards.

wait_event_interruptible_lock_irq_cmd

`wait_event_interruptible_lock_irq_cmd (wq_head, condition, lock, cmd)`

> sleep until a condition gets true. The condition is checked under the lock. This is expected to be called with the lock taken.

**Parameters**

`wq_head`
:   the waitqueue to wait on

`condition`
:   a C expression for the event to wait for

`lock`
:   a locked spinlock_t, which will be released before cmd and
    schedule() and reacquired afterwards.

`cmd`
:   a command which is invoked outside the critical section before
    sleep

**Description**

The process is put to sleep (TASK_INTERRUPTIBLE) until the
**condition** evaluates to true or a signal is received. The **condition** is
checked each time the waitqueue **wq_head** is woken up.

wake_up() has to be called after changing any variable that could
change the result of the wait condition.

This is supposed to be called while holding the lock. The lock is
dropped before invoking the cmd and going to sleep and is reacquired
afterwards.

The macro will return -ERESTARTSYS if it was interrupted by a signal
and 0 if **condition** evaluated to true.

wait_event_interruptible_lock_irq

`wait_event_interruptible_lock_irq (wq_head, condition, lock)`

> sleep until a condition gets true. The condition is checked under the lock. This is expected to be called with the lock taken.

**Parameters**

`wq_head`
:   the waitqueue to wait on

`condition`
:   a C expression for the event to wait for

`lock`
:   a locked spinlock_t, which will be released before schedule()
    and reacquired afterwards.

**Description**

The process is put to sleep (TASK_INTERRUPTIBLE) until the
**condition** evaluates to true or signal is received. The **condition** is
checked each time the waitqueue **wq_head** is woken up.

wake_up() has to be called after changing any variable that could
change the result of the wait condition.

This is supposed to be called while holding the lock. The lock is
dropped before going to sleep and is reacquired afterwards.

The macro will return -ERESTARTSYS if it was interrupted by a signal
and 0 if **condition** evaluated to true.

wait_event_interruptible_lock_irq_timeout

`wait_event_interruptible_lock_irq_timeout (wq_head, condition, lock, timeout)`

> sleep until a condition gets true or a timeout elapses. The condition is checked under the lock. This is expected to be called with the lock taken.

**Parameters**

`wq_head`
:   the waitqueue to wait on

`condition`
:   a C expression for the event to wait for

`lock`
:   a locked spinlock_t, which will be released before schedule()
    and reacquired afterwards.

`timeout`
:   timeout, in jiffies

**Description**

The process is put to sleep (TASK_INTERRUPTIBLE) until the
**condition** evaluates to true or signal is received. The **condition** is
checked each time the waitqueue **wq_head** is woken up.

wake_up() has to be called after changing any variable that could
change the result of the wait condition.

This is supposed to be called while holding the lock. The lock is
dropped before going to sleep and is reacquired afterwards.

The function returns 0 if the **timeout** elapsed, -ERESTARTSYS if it
was interrupted by a signal, and the remaining jiffies otherwise
if the condition evaluated to true before the timeout elapsed.

int __wake_up(struct wait_queue_head \*wq_head, unsigned int mode, int nr_exclusive, void \*key)
:   wake up threads blocked on a waitqueue.

**Parameters**

`struct wait_queue_head *wq_head`
:   the waitqueue

`unsigned int mode`
:   which threads

`int nr_exclusive`
:   how many wake-one or wake-many threads to wake up

`void *key`
:   is directly passed to the wakeup function

**Description**

If this function wakes up a task, it executes a full memory barrier
before accessing the task state. Returns the number of exclusive
tasks that were awaken.

void __wake_up_sync_key(struct wait_queue_head \*wq_head, unsigned int mode, void \*key)
:   wake up threads blocked on a waitqueue.

**Parameters**

`struct wait_queue_head *wq_head`
:   the waitqueue

`unsigned int mode`
:   which threads

`void *key`
:   opaque value to be passed to wakeup targets

**Description**

The sync wakeup differs that the waker knows that it will schedule
away soon, so while the target thread will be woken up, it will not
be migrated to another CPU - ie. the two threads are 'synchronized'
with each other. This can prevent needless bouncing between CPUs.

On UP it can prevent extra preemption.

If this function wakes up a task, it executes a full memory barrier before
accessing the task state.

void __wake_up_locked_sync_key(struct wait_queue_head \*wq_head, unsigned int mode, void \*key)
:   wake up a thread blocked on a locked waitqueue.

**Parameters**

`struct wait_queue_head *wq_head`
:   the waitqueue

`unsigned int mode`
:   which threads

`void *key`
:   opaque value to be passed to wakeup targets

**Description**

The sync wakeup differs in that the waker knows that it will schedule
away soon, so while the target thread will be woken up, it will not
be migrated to another CPU - ie. the two threads are 'synchronized'
with each other. This can prevent needless bouncing between CPUs.

On UP it can prevent extra preemption.

If this function wakes up a task, it executes a full memory barrier before
accessing the task state.

void finish_wait(struct wait_queue_head \*wq_head, struct wait_queue_entry \*wq_entry)
:   clean up after waiting in a queue

**Parameters**

`struct wait_queue_head *wq_head`
:   waitqueue waited on

`struct wait_queue_entry *wq_entry`
:   wait descriptor

**Description**

Sets current thread back to running state and removes
the wait descriptor from the given waitqueue if still
queued.

## Internal Functions

int wait_task_stopped(struct wait_opts \*wo, int ptrace, struct task_struct \*p)
:   Wait for `TASK_STOPPED` or `TASK_TRACED`

**Parameters**

`struct wait_opts *wo`
:   wait options

`int ptrace`
:   is the wait for ptrace

`struct task_struct *p`
:   task to wait for

**Description**

Handle sys_wait4() work for `p` in state `TASK_STOPPED` or `TASK_TRACED`.

**Context**

read_lock(`tasklist_lock`), which is released if return value is
non-zero. Also, grabs and releases **p->sighand->siglock**.

**Return**

0 if wait condition didn't exist and search for other wait conditions
should continue. Non-zero return, -errno on failure and **p**'s pid on
success, implies that tasklist_lock is released and wait condition
search should terminate.

bool task_set_jobctl_pending(struct task_struct \*task, unsigned long mask)
:   set jobctl pending bits

**Parameters**

`struct task_struct *task`
:   target task

`unsigned long mask`
:   pending bits to set

**Description**

Clear **mask** from **task->jobctl**. **mask** must be subset of
`JOBCTL_PENDING_MASK` | `JOBCTL_STOP_CONSUME` | `JOBCTL_STOP_SIGMASK` |
`JOBCTL_TRAPPING`. If stop signo is being set, the existing signo is
cleared. If **task** is already being killed or exiting, this function
becomes noop.

**Context**

Must be called with **task->sighand->siglock** held.

**Return**

`true` if **mask** is set, `false` if made noop because **task** was dying.

void task_clear_jobctl_trapping(struct task_struct \*task)
:   clear jobctl trapping bit

**Parameters**

`struct task_struct *task`
:   target task

**Description**

If JOBCTL_TRAPPING is set, a ptracer is waiting for us to enter TRACED.
Clear it and wake up the ptracer. Note that we don't need any further
locking. **task->siglock** guarantees that **task->parent** points to the
ptracer.

**Context**

Must be called with **task->sighand->siglock** held.

void task_clear_jobctl_pending(struct task_struct \*task, unsigned long mask)
:   clear jobctl pending bits

**Parameters**

`struct task_struct *task`
:   target task

`unsigned long mask`
:   pending bits to clear

**Description**

Clear **mask** from **task->jobctl**. **mask** must be subset of
`JOBCTL_PENDING_MASK`. If `JOBCTL_STOP_PENDING` is being cleared, other
STOP bits are cleared together.

If clearing of **mask** leaves no stop or trap pending, this function calls
[`task_clear_jobctl_trapping()`](basics.md#c.task_clear_jobctl_trapping "task_clear_jobctl_trapping").

**Context**

Must be called with **task->sighand->siglock** held.

bool task_participate_group_stop(struct task_struct \*task)
:   participate in a group stop

**Parameters**

`struct task_struct *task`
:   task participating in a group stop

**Description**

**task** has `JOBCTL_STOP_PENDING` set and is participating in a group stop.
Group stop states are cleared and the group stop count is consumed if
`JOBCTL_STOP_CONSUME` was set. If the consumption completes the group
stop, the appropriate SIGNAL_\* flags are set.

**Context**

Must be called with **task->sighand->siglock** held.

**Return**

`true` if group stop completion should be notified to the parent, `false`
otherwise.

void ptrace_trap_notify(struct task_struct \*t)
:   schedule trap to notify ptracer

**Parameters**

`struct task_struct *t`
:   tracee wanting to notify tracer

**Description**

This function schedules sticky ptrace trap which is cleared on the next
TRAP_STOP to notify ptracer of an event. **t** must have been seized by
ptracer.

If **t** is running, STOP trap will be taken. If trapped for STOP and
ptracer is listening for events, tracee is woken up so that it can
re-trap for the new event. If trapped otherwise, STOP trap will be
eventually taken without returning to userland after the existing traps
are finished by PTRACE_CONT.

**Context**

Must be called with **task->sighand->siglock** held.

int force_sig_seccomp(int syscall, int reason, bool force_coredump)
:   signals the task to allow in-process syscall emulation

**Parameters**

`int syscall`
:   syscall number to send to userland

`int reason`
:   filter-supplied reason code to send to userland (via si_errno)

`bool force_coredump`
:   true to trigger a coredump

**Description**

Forces a SIGSYS with a code of SYS_SECCOMP and related sigsys info.

void do_notify_parent_cldstop(struct task_struct \*tsk, bool for_ptracer, int why)
:   notify parent of stopped/continued state change

**Parameters**

`struct task_struct *tsk`
:   task reporting the state change

`bool for_ptracer`
:   the notification is for ptracer

`int why`
:   CLD_{CONTINUED|STOPPED|TRAPPED} to report

**Description**

Notify **tsk**'s parent that the stopped/continued state has changed. If
**for_ptracer** is `false`, **tsk**'s group leader notifies to its real parent.
If `true`, **tsk** reports to **tsk->parent** which should be the ptracer.

**Context**

Must be called with tasklist_lock at least read locked.

bool do_signal_stop(int signr)
:   handle group stop for SIGSTOP and other stop signals

**Parameters**

`int signr`
:   signr causing group stop if initiating

**Description**

If `JOBCTL_STOP_PENDING` is not set yet, initiate group stop with **signr**
and participate in it. If already set, participate in the existing
group stop. If participated in a group stop (and thus slept), `true` is
returned with siglock released.

If ptraced, this function doesn't handle stop itself. Instead,
`JOBCTL_TRAP_STOP` is scheduled and `false` is returned with siglock
untouched. The caller must ensure that INTERRUPT trap handling takes
places afterwards.

**Context**

Must be called with **current->sighand->siglock** held, which is released
on `true` return.

**Return**

`false` if group stop is already cancelled or ptrace trap is scheduled.
`true` if participated in group stop.

void do_jobctl_trap(void)
:   take care of ptrace jobctl traps

**Parameters**

`void`
:   no arguments

**Description**

When PT_SEIZED, it's used for both group stop and explicit
SEIZE/INTERRUPT traps. Both generate PTRACE_EVENT_STOP trap with
accompanying siginfo. If stopped, lower eight bits of exit_code contain
the stop signal; otherwise, `SIGTRAP`.

When !PT_SEIZED, it's used only for group stop trap with stop signal
number as exit_code and no siginfo.

**Context**

Must be called with **current->sighand->siglock** held, which may be
released and re-acquired before returning with intervening sleep.

void do_freezer_trap(void)
:   handle the freezer jobctl trap

**Parameters**

`void`
:   no arguments

**Description**

Puts the task into frozen state, if only the task is not about to quit.
In this case it drops JOBCTL_TRAP_FREEZE.

**Context**

Must be called with **current->sighand->siglock** held,
which is always released before returning.

void signal_delivered(struct ksignal \*ksig, int stepping)
:   called after signal delivery to update blocked signals

**Parameters**

`struct ksignal *ksig`
:   kernel signal struct

`int stepping`
:   nonzero if debugger single-step or block-step in use

**Description**

This function should be called when a signal has successfully been
delivered. It updates the blocked signals accordingly (**ksig->ka.sa.sa_mask**
is always blocked), and the signal itself is blocked unless `SA_NODEFER`
is set in **ksig->ka.sa.sa_flags**. Tracing is notified.

long sys_restart_syscall(void)
:   restart a system call

**Parameters**

`void`
:   no arguments

void set_current_blocked(sigset_t \*newset)
:   change current->blocked mask

**Parameters**

`sigset_t *newset`
:   new mask

**Description**

It is wrong to change ->blocked directly, this helper should be used
to ensure the process can't miss a shared signal we are going to block.

long sys_rt_sigprocmask(int how, sigset_t __user \*nset, sigset_t __user \*oset, size_t sigsetsize)
:   change the list of currently blocked signals

**Parameters**

`int how`
:   whether to add, remove, or set signals

`sigset_t __user * nset`
:   stores pending signals

`sigset_t __user * oset`
:   previous value of signal mask if non-null

`size_t sigsetsize`
:   size of sigset_t type

long sys_rt_sigpending(sigset_t __user \*uset, size_t sigsetsize)
:   examine a pending signal that has been raised while blocked

**Parameters**

`sigset_t __user * uset`
:   stores pending signals

`size_t sigsetsize`
:   size of sigset_t type or larger

void copy_siginfo_to_external32(struct compat_siginfo \*to, const struct kernel_siginfo \*from)
:   copy a kernel siginfo into a compat user siginfo

**Parameters**

`struct compat_siginfo *to`
:   compat siginfo destination

`const struct kernel_siginfo *from`
:   kernel siginfo source

**Note**

This function does not work properly for the SIGCHLD on x32, but
fortunately it doesn't have to. The only valid callers for this function are
copy_siginfo_to_user32, which is overriden for x32 and the coredump code.
The latter does not care because SIGCHLD will never cause a coredump.

int do_sigtimedwait(const sigset_t \*which, kernel_siginfo_t \*info, const struct timespec64 \*ts)
:   wait for queued signals specified in **which**

**Parameters**

`const sigset_t *which`
:   queued signals to wait for

`kernel_siginfo_t *info`
:   if non-null, the signal's siginfo is returned here

`const struct timespec64 *ts`
:   upper bound on process time suspension

long sys_rt_sigtimedwait(const sigset_t __user \*uthese, siginfo_t __user \*uinfo, const struct __kernel_timespec __user \*uts, size_t sigsetsize)
:   synchronously wait for queued signals specified in **uthese**

**Parameters**

`const sigset_t __user * uthese`
:   queued signals to wait for

`siginfo_t __user * uinfo`
:   if non-null, the signal's siginfo is returned here

`const struct __kernel_timespec __user * uts`
:   upper bound on process time suspension

`size_t sigsetsize`
:   size of sigset_t type

long sys_kill(pid_t pid, int sig)
:   send a signal to a process

**Parameters**

`pid_t pid`
:   the PID of the process

`int sig`
:   signal to be sent

long sys_pidfd_send_signal(int pidfd, int sig, siginfo_t __user \*info, unsigned int flags)
:   Signal a process through a pidfd

**Parameters**

`int pidfd`
:   file descriptor of the process

`int sig`
:   signal to send

`siginfo_t __user * info`
:   signal info

`unsigned int flags`
:   future flags

**Description**

The syscall currently only signals via PIDTYPE_PID which covers
kill(<positive-pid>, <signal>. It does not signal threads or process
groups.
In order to extend the syscall to threads and process groups the **flags**
argument should be used. In essence, the **flags** argument will determine
what is signaled and not the file descriptor itself. Put in other words,
grouping is a property of the flags argument not a property of the file
descriptor.

**Return**

0 on success, negative errno on failure

long sys_tgkill(pid_t tgid, pid_t pid, int sig)
:   send signal to one specific thread

**Parameters**

`pid_t tgid`
:   the thread group ID of the thread

`pid_t pid`
:   the PID of the thread

`int sig`
:   signal to be sent

    This syscall also checks the **tgid** and returns -ESRCH even if the PID
    exists but it's not belonging to the target process anymore. This
    method solves the problem of threads exiting and PIDs getting reused.

long sys_tkill(pid_t pid, int sig)
:   send signal to one specific task

**Parameters**

`pid_t pid`
:   the PID of the task

`int sig`
:   signal to be sent

    Send a signal to only one task, even if it's a CLONE_THREAD task.

long sys_rt_sigqueueinfo(pid_t pid, int sig, siginfo_t __user \*uinfo)
:   send signal information to a signal

**Parameters**

`pid_t pid`
:   the PID of the thread

`int sig`
:   signal to be sent

`siginfo_t __user * uinfo`
:   signal info to be sent

long sys_sigpending(old_sigset_t __user \*uset)
:   examine pending signals

**Parameters**

`old_sigset_t __user * uset`
:   where mask of pending signal is returned

long sys_sigprocmask(int how, old_sigset_t __user \*nset, old_sigset_t __user \*oset)
:   examine and change blocked signals

**Parameters**

`int how`
:   whether to add, remove, or set signals

`old_sigset_t __user * nset`
:   signals to add or remove (if non-null)

`old_sigset_t __user * oset`
:   previous value of signal mask if non-null

**Description**

Some platforms have their own version with special arguments;
others support only sys_rt_sigprocmask.

long sys_rt_sigaction(int sig, const struct sigaction __user \*act, struct sigaction __user \*oact, size_t sigsetsize)
:   alter an action taken by a process

**Parameters**

`int sig`
:   signal to be sent

`const struct sigaction __user * act`
:   new sigaction

`struct sigaction __user * oact`
:   used to save the previous sigaction

`size_t sigsetsize`
:   size of sigset_t type

long sys_rt_sigsuspend(sigset_t __user \*unewset, size_t sigsetsize)
:   replace the signal mask for a value with the **unewset** value until a signal is received

**Parameters**

`sigset_t __user * unewset`
:   new signal mask value

`size_t sigsetsize`
:   size of sigset_t type

kthread_create

`kthread_create (threadfn, data, namefmt, arg...)`

> create a kthread on the current node

**Parameters**

`threadfn`
:   the function to run in the thread

`data`
:   data pointer for **threadfn()**

`namefmt`
:   printf-style format string for the thread name

`arg...`
:   arguments for **namefmt**.

**Description**

This macro will create a kthread on the current node, leaving it in
the stopped state. This is just a helper for [`kthread_create_on_node()`](basics.md#c.kthread_create_on_node "kthread_create_on_node");
see the documentation there for more details.

kthread_run

`kthread_run (threadfn, data, namefmt, ...)`

> create and wake a thread.

**Parameters**

`threadfn`
:   the function to run until signal_pending(current).

`data`
:   data ptr for **threadfn**.

`namefmt`
:   printf-style name for the thread.

`...`
:   variable arguments

**Description**

Convenient wrapper for [`kthread_create()`](basics.md#c.kthread_create "kthread_create") followed by
[`wake_up_process()`](basics.md#c.wake_up_process "wake_up_process"). Returns the kthread or ERR_PTR(-ENOMEM).

struct task_struct \*kthread_run_on_cpu(int (\*threadfn)(void \*data), void \*data, unsigned int cpu, const char \*namefmt)
:   create and wake a cpu bound thread.

**Parameters**

`int (*threadfn)(void *data)`
:   the function to run until signal_pending(current).

`void *data`
:   data ptr for **threadfn**.

`unsigned int cpu`
:   The cpu on which the thread should be bound,

`const char *namefmt`
:   printf-style name for the thread. Format is restricted
    to "name.\*``u``". Code fills in cpu number.

**Description**

Convenient wrapper for [`kthread_create_on_cpu()`](basics.md#c.kthread_create_on_cpu "kthread_create_on_cpu")
followed by [`wake_up_process()`](basics.md#c.wake_up_process "wake_up_process"). Returns the kthread or
ERR_PTR(-ENOMEM).

bool kthread_should_stop(void)
:   should this kthread return now?

**Parameters**

`void`
:   no arguments

**Description**

When someone calls [`kthread_stop()`](basics.md#c.kthread_stop "kthread_stop") on your kthread, it will be woken
and this will return true. You should then return, and your return
value will be passed through to [`kthread_stop()`](basics.md#c.kthread_stop "kthread_stop").

bool kthread_should_park(void)
:   should this kthread park now?

**Parameters**

`void`
:   no arguments

**Description**

When someone calls [`kthread_park()`](basics.md#c.kthread_park "kthread_park") on your kthread, it will be woken
and this will return true. You should then do the necessary
cleanup and call kthread_parkme()

Similar to [`kthread_should_stop()`](basics.md#c.kthread_should_stop "kthread_should_stop"), but this keeps the thread alive
and in a park position. [`kthread_unpark()`](basics.md#c.kthread_unpark "kthread_unpark") "restarts" the thread and
calls the thread function again.

bool kthread_freezable_should_stop(bool \*was_frozen)
:   should this freezable kthread return now?

**Parameters**

`bool *was_frozen`
:   optional out parameter, indicates whether `current` was frozen

**Description**

[`kthread_should_stop()`](basics.md#c.kthread_should_stop "kthread_should_stop") for freezable kthreads, which will enter
refrigerator if necessary. This function is safe from [`kthread_stop()`](basics.md#c.kthread_stop "kthread_stop") /
freezer deadlock and freezable kthreads should use this function instead
of calling try_to_freeze() directly.

void \*kthread_func(struct task_struct \*task)
:   return the function specified on kthread creation

**Parameters**

`struct task_struct *task`
:   kthread task in question

**Description**

Returns NULL if the task is not a kthread.

void \*kthread_data(struct task_struct \*task)
:   return data value specified on kthread creation

**Parameters**

`struct task_struct *task`
:   kthread task in question

**Description**

Return the data value specified when kthread **task** was created.
The caller is responsible for ensuring the validity of **task** when
calling this function.

void __noreturn kthread_complete_and_exit(struct completion \*comp, long code)
:   Exit the current kthread.

**Parameters**

`struct completion *comp`
:   Completion to complete

`long code`
:   The integer value to return to [`kthread_stop()`](basics.md#c.kthread_stop "kthread_stop").

**Description**

If present, complete **comp** and then return code to [`kthread_stop()`](basics.md#c.kthread_stop "kthread_stop").

A kernel thread whose module may be removed after the completion of
**comp** can use this function to exit safely.

Does not return.

struct task_struct \*kthread_create_on_node(int (\*threadfn)(void \*data), void \*data, int node, const char namefmt[], ...)
:   create a kthread.

**Parameters**

`int (*threadfn)(void *data)`
:   the function to run until signal_pending(current).

`void *data`
:   data ptr for **threadfn**.

`int node`
:   task and thread structures for the thread are allocated on this node

`const char namefmt[]`
:   printf-style name for the thread.

`...`
:   variable arguments

**Description**

This helper function creates and names a kernel
thread. The thread will be stopped: use [`wake_up_process()`](basics.md#c.wake_up_process "wake_up_process") to start
it. See also [`kthread_run()`](basics.md#c.kthread_run "kthread_run"). The new thread has SCHED_NORMAL policy and
is affine to all CPUs.

If thread is going to be bound on a particular cpu, give its node
in **node**, to get NUMA affinity for kthread stack, or else give NUMA_NO_NODE.
When woken, the thread will run **threadfn()** with **data** as its
argument. **threadfn()** can either return directly if it is a
standalone thread for which no one will call [`kthread_stop()`](basics.md#c.kthread_stop "kthread_stop"), or
return when '[`kthread_should_stop()`](basics.md#c.kthread_should_stop "kthread_should_stop")' is true (which means
[`kthread_stop()`](basics.md#c.kthread_stop "kthread_stop") has been called). The return value should be zero
or a negative error number; it will be passed to [`kthread_stop()`](basics.md#c.kthread_stop "kthread_stop").

Returns a task_struct or ERR_PTR(-ENOMEM) or ERR_PTR(-EINTR).

void kthread_bind(struct task_struct \*p, unsigned int cpu)
:   bind a just-created kthread to a cpu.

**Parameters**

`struct task_struct *p`
:   thread created by [`kthread_create()`](basics.md#c.kthread_create "kthread_create").

`unsigned int cpu`
:   cpu (might not be online, must be possible) for **k** to run on.

**Description**

This function is equivalent to set_cpus_allowed(),
except that **cpu** doesn't need to be online, and the thread must be
stopped (i.e., just returned from [`kthread_create()`](basics.md#c.kthread_create "kthread_create")).

struct task_struct \*kthread_create_on_cpu(int (\*threadfn)(void \*data), void \*data, unsigned int cpu, const char \*namefmt)
:   Create a cpu bound kthread

**Parameters**

`int (*threadfn)(void *data)`
:   the function to run until signal_pending(current).

`void *data`
:   data ptr for **threadfn**.

`unsigned int cpu`
:   The cpu on which the thread should be bound,

`const char *namefmt`
:   printf-style name for the thread. Format is restricted
    to "name.\*``u``". Code fills in cpu number.

**Description**

This helper function creates and names a kernel thread

void kthread_unpark(struct task_struct \*k)
:   unpark a thread created by [`kthread_create()`](basics.md#c.kthread_create "kthread_create").

**Parameters**

`struct task_struct *k`
:   thread created by [`kthread_create()`](basics.md#c.kthread_create "kthread_create").

**Description**

Sets [`kthread_should_park()`](basics.md#c.kthread_should_park "kthread_should_park") for **k** to return false, wakes it, and
waits for it to return. If the thread is marked percpu then its
bound to the cpu again.

int kthread_park(struct task_struct \*k)
:   park a thread created by [`kthread_create()`](basics.md#c.kthread_create "kthread_create").

**Parameters**

`struct task_struct *k`
:   thread created by [`kthread_create()`](basics.md#c.kthread_create "kthread_create").

**Description**

Sets [`kthread_should_park()`](basics.md#c.kthread_should_park "kthread_should_park") for **k** to return true, wakes it, and
waits for it to return. This can also be called after [`kthread_create()`](basics.md#c.kthread_create "kthread_create")
instead of calling [`wake_up_process()`](basics.md#c.wake_up_process "wake_up_process"): the thread will park without
calling threadfn().

Returns 0 if the thread is parked, -ENOSYS if the thread exited.
If called by the kthread itself just the park bit is set.

int kthread_stop(struct task_struct \*k)
:   stop a thread created by [`kthread_create()`](basics.md#c.kthread_create "kthread_create").

**Parameters**

`struct task_struct *k`
:   thread created by [`kthread_create()`](basics.md#c.kthread_create "kthread_create").

**Description**

Sets [`kthread_should_stop()`](basics.md#c.kthread_should_stop "kthread_should_stop") for **k** to return true, wakes it, and
waits for it to exit. This can also be called after [`kthread_create()`](basics.md#c.kthread_create "kthread_create")
instead of calling [`wake_up_process()`](basics.md#c.wake_up_process "wake_up_process"): the thread will exit without
calling threadfn().

If threadfn() may call kthread_exit() itself, the caller must ensure
task_struct can't go away.

Returns the result of threadfn(), or `-EINTR` if [`wake_up_process()`](basics.md#c.wake_up_process "wake_up_process")
was never called.

int kthread_stop_put(struct task_struct \*k)
:   stop a thread and put its task struct

**Parameters**

`struct task_struct *k`
:   thread created by [`kthread_create()`](basics.md#c.kthread_create "kthread_create").

**Description**

Stops a thread created by [`kthread_create()`](basics.md#c.kthread_create "kthread_create") and put its task_struct.
Only use when holding an extra task struct reference obtained by
calling get_task_struct().

int kthread_worker_fn(void \*worker_ptr)
:   kthread function to process kthread_worker

**Parameters**

`void *worker_ptr`
:   pointer to initialized kthread_worker

**Description**

This function implements the main cycle of kthread worker. It processes
work_list until it is stopped with [`kthread_stop()`](basics.md#c.kthread_stop "kthread_stop"). It sleeps when the queue
is empty.

The works are not allowed to keep any locks, disable preemption or interrupts
when they finish. There is defined a safe point for freezing when one work
finishes and before a new one is started.

Also the works must not be handled by more than one worker at the same time,
see also [`kthread_queue_work()`](basics.md#c.kthread_queue_work "kthread_queue_work").

struct kthread_worker \*kthread_create_worker(unsigned int flags, const char namefmt[], ...)
:   create a kthread worker

**Parameters**

`unsigned int flags`
:   flags modifying the default behavior of the worker

`const char namefmt[]`
:   printf-style name for the kthread worker (task).

`...`
:   variable arguments

**Description**

Returns a pointer to the allocated worker on success, ERR_PTR(-ENOMEM)
when the needed structures could not get allocated, and ERR_PTR(-EINTR)
when the caller was killed by a fatal signal.

struct kthread_worker \*kthread_create_worker_on_cpu(int cpu, unsigned int flags, const char namefmt[], ...)
:   create a kthread worker and bind it to a given CPU and the associated NUMA node.

**Parameters**

`int cpu`
:   CPU number

`unsigned int flags`
:   flags modifying the default behavior of the worker

`const char namefmt[]`
:   printf-style name for the kthread worker (task).

`...`
:   variable arguments

**Description**

Use a valid CPU number if you want to bind the kthread worker
to the given CPU and the associated NUMA node.

A good practice is to add the cpu number also into the worker name.
For example, use kthread_create_worker_on_cpu(cpu, "helper/`d`", cpu).

CPU hotplug:
The kthread worker API is simple and generic. It just provides a way
to create, use, and destroy workers.

It is up to the API user how to handle CPU hotplug. They have to decide
how to handle pending work items, prevent queuing new ones, and
restore the functionality when the CPU goes off and on. There are a
few catches:

> - CPU affinity gets lost when it is scheduled on an offline CPU.
> - The worker might not exist when the CPU was off when the user
>   created the workers.

Good practice is to implement two CPU hotplug callbacks and to
destroy/create the worker when the CPU goes down/up.

**Return**

The pointer to the allocated worker on success, ERR_PTR(-ENOMEM)
when the needed structures could not get allocated, and ERR_PTR(-EINTR)
when the caller was killed by a fatal signal.

bool kthread_queue_work(struct kthread_worker \*worker, struct kthread_work \*work)
:   queue a kthread_work

**Parameters**

`struct kthread_worker *worker`
:   target kthread_worker

`struct kthread_work *work`
:   kthread_work to queue

**Description**

Queue **work** to work processor **task** for async execution. **task**
must have been created with kthread_worker_create(). Returns `true`
if **work** was successfully queued, `false` if it was already pending.

Reinitialize the work if it needs to be used by another worker.
For example, when the worker was stopped and started again.

void kthread_delayed_work_timer_fn(struct timer_list \*t)
:   callback that queues the associated kthread delayed work when the timer expires.

**Parameters**

`struct timer_list *t`
:   pointer to the expired timer

**Description**

The format of the function is defined by struct timer_list.
It should have been called from irqsafe timer with irq already off.

bool kthread_queue_delayed_work(struct kthread_worker \*worker, struct kthread_delayed_work \*dwork, unsigned long delay)
:   queue the associated kthread work after a delay.

**Parameters**

`struct kthread_worker *worker`
:   target kthread_worker

`struct kthread_delayed_work *dwork`
:   kthread_delayed_work to queue

`unsigned long delay`
:   number of jiffies to wait before queuing

**Description**

If the work has not been pending it starts a timer that will queue
the work after the given **delay**. If **delay** is zero, it queues the
work immediately.

**Return**

`false` if the **work** has already been pending. It means that
either the timer was running or the work was queued. It returns `true`
otherwise.

void kthread_flush_work(struct kthread_work \*work)
:   flush a kthread_work

**Parameters**

`struct kthread_work *work`
:   work to flush

**Description**

If **work** is queued or executing, wait for it to finish execution.

bool kthread_mod_delayed_work(struct kthread_worker \*worker, struct kthread_delayed_work \*dwork, unsigned long delay)
:   modify delay of or queue a kthread delayed work

**Parameters**

`struct kthread_worker *worker`
:   kthread worker to use

`struct kthread_delayed_work *dwork`
:   kthread delayed work to queue

`unsigned long delay`
:   number of jiffies to wait before queuing

**Description**

If **dwork** is idle, equivalent to [`kthread_queue_delayed_work()`](basics.md#c.kthread_queue_delayed_work "kthread_queue_delayed_work"). Otherwise,
modify **dwork**'s timer so that it expires after **delay**. If **delay** is zero,
**work** is guaranteed to be queued immediately.

A special case is when the work is being canceled in parallel.
It might be caused either by the real [`kthread_cancel_delayed_work_sync()`](basics.md#c.kthread_cancel_delayed_work_sync "kthread_cancel_delayed_work_sync")
or yet another [`kthread_mod_delayed_work()`](basics.md#c.kthread_mod_delayed_work "kthread_mod_delayed_work") call. We let the other command
win and return `true` here. The return value can be used for reference
counting and the number of queued works stays the same. Anyway, the caller
is supposed to synchronize these operations a reasonable way.

This function is safe to call from any context including IRQ handler.
See __kthread_cancel_work() and [`kthread_delayed_work_timer_fn()`](basics.md#c.kthread_delayed_work_timer_fn "kthread_delayed_work_timer_fn")
for details.

**Return**

`false` if **dwork** was idle and queued, `true` otherwise.

bool kthread_cancel_work_sync(struct kthread_work \*work)
:   cancel a kthread work and wait for it to finish

**Parameters**

`struct kthread_work *work`
:   the kthread work to cancel

**Description**

Cancel **work** and wait for its execution to finish. This function
can be used even if the work re-queues itself. On return from this
function, **work** is guaranteed to be not pending or executing on any CPU.

kthread_cancel_work_sync(`delayed_work->work`) must not be used for
delayed_work's. Use [`kthread_cancel_delayed_work_sync()`](basics.md#c.kthread_cancel_delayed_work_sync "kthread_cancel_delayed_work_sync") instead.

The caller must ensure that the worker on which **work** was last
queued can't be destroyed before this function returns.

**Return**

`true` if **work** was pending, `false` otherwise.

bool kthread_cancel_delayed_work_sync(struct kthread_delayed_work \*dwork)
:   cancel a kthread delayed work and wait for it to finish.

**Parameters**

`struct kthread_delayed_work *dwork`
:   the kthread delayed work to cancel

**Description**

This is [`kthread_cancel_work_sync()`](basics.md#c.kthread_cancel_work_sync "kthread_cancel_work_sync") for delayed works.

**Return**

`true` if **dwork** was pending, `false` otherwise.

void kthread_flush_worker(struct kthread_worker \*worker)
:   flush all current works on a kthread_worker

**Parameters**

`struct kthread_worker *worker`
:   worker to flush

**Description**

Wait until all currently executing or pending works on **worker** are
finished.

void kthread_destroy_worker(struct kthread_worker \*worker)
:   destroy a kthread worker

**Parameters**

`struct kthread_worker *worker`
:   worker to be destroyed

**Description**

Flush and destroy **worker**. The simple flush is enough because the kthread
worker API is used only in trivial scenarios. There are no multi-step state
machines needed.

Note that this function is not responsible for handling delayed work, so
caller should be responsible for queuing or canceling all delayed work items
before invoke this function.

void kthread_use_mm(struct mm_struct \*mm)
:   make the calling kthread operate on an address space

**Parameters**

`struct mm_struct *mm`
:   address space to operate on

void kthread_unuse_mm(struct mm_struct \*mm)
:   reverse the effect of [`kthread_use_mm()`](basics.md#c.kthread_use_mm "kthread_use_mm")

**Parameters**

`struct mm_struct *mm`
:   address space to operate on

void kthread_associate_blkcg(struct cgroup_subsys_state \*css)
:   associate blkcg to current kthread

**Parameters**

`struct cgroup_subsys_state *css`
:   the cgroup info

**Description**

Current thread must be a kthread. The thread is running jobs on behalf of
other threads. In some cases, we expect the jobs attach cgroup info of
original threads instead of that of current thread. This function stores
original thread's cgroup info in current kthread context for later
retrieval.

## Reference counting

void refcount_set(refcount_t \*r, int n)
:   set a refcount's value

**Parameters**

`refcount_t *r`
:   the refcount

`int n`
:   value to which the refcount will be set

unsigned int refcount_read(const refcount_t \*r)
:   get a refcount's value

**Parameters**

`const refcount_t *r`
:   the refcount

**Return**

the refcount's value

bool refcount_add_not_zero(int i, refcount_t \*r)
:   add a value to a refcount unless it is 0

**Parameters**

`int i`
:   the value to add to the refcount

`refcount_t *r`
:   the refcount

**Description**

Will saturate at REFCOUNT_SATURATED and WARN.

Provides no memory ordering, it is assumed the caller has guaranteed the
object memory to be stable (RCU, etc.). It does provide a control dependency
and thereby orders future stores. See the comment on top.

Use of this function is not recommended for the normal reference counting
use case in which references are taken and released one at a time. In these
cases, [`refcount_inc()`](basics.md#c.refcount_inc "refcount_inc"), or one of its variants, should instead be used to
increment a reference count.

**Return**

false if the passed refcount is 0, true otherwise

void refcount_add(int i, refcount_t \*r)
:   add a value to a refcount

**Parameters**

`int i`
:   the value to add to the refcount

`refcount_t *r`
:   the refcount

**Description**

Similar to [`atomic_add()`](basics.md#c.atomic_add "atomic_add"), but will saturate at REFCOUNT_SATURATED and WARN.

Provides no memory ordering, it is assumed the caller has guaranteed the
object memory to be stable (RCU, etc.). It does provide a control dependency
and thereby orders future stores. See the comment on top.

Use of this function is not recommended for the normal reference counting
use case in which references are taken and released one at a time. In these
cases, [`refcount_inc()`](basics.md#c.refcount_inc "refcount_inc"), or one of its variants, should instead be used to
increment a reference count.

bool refcount_inc_not_zero(refcount_t \*r)
:   increment a refcount unless it is 0

**Parameters**

`refcount_t *r`
:   the refcount to increment

**Description**

Similar to [`atomic_inc_not_zero()`](basics.md#c.atomic_inc_not_zero "atomic_inc_not_zero"), but will saturate at REFCOUNT_SATURATED
and WARN.

Provides no memory ordering, it is assumed the caller has guaranteed the
object memory to be stable (RCU, etc.). It does provide a control dependency
and thereby orders future stores. See the comment on top.

**Return**

true if the increment was successful, false otherwise

void refcount_inc(refcount_t \*r)
:   increment a refcount

**Parameters**

`refcount_t *r`
:   the refcount to increment

**Description**

Similar to [`atomic_inc()`](basics.md#c.atomic_inc "atomic_inc"), but will saturate at REFCOUNT_SATURATED and WARN.

Provides no memory ordering, it is assumed the caller already has a
reference on the object.

Will WARN if the refcount is 0, as this represents a possible use-after-free
condition.

bool refcount_sub_and_test(int i, refcount_t \*r)
:   subtract from a refcount and test if it is 0

**Parameters**

`int i`
:   amount to subtract from the refcount

`refcount_t *r`
:   the refcount

**Description**

Similar to [`atomic_dec_and_test()`](basics.md#c.atomic_dec_and_test "atomic_dec_and_test"), but it will WARN, return false and
ultimately leak on underflow and will fail to decrement when saturated
at REFCOUNT_SATURATED.

Provides release memory ordering, such that prior loads and stores are done
before, and provides an acquire ordering on success such that free()
must come after.

Use of this function is not recommended for the normal reference counting
use case in which references are taken and released one at a time. In these
cases, [`refcount_dec()`](basics.md#c.refcount_dec "refcount_dec"), or one of its variants, should instead be used to
decrement a reference count.

**Return**

true if the resulting refcount is 0, false otherwise

bool refcount_dec_and_test(refcount_t \*r)
:   decrement a refcount and test if it is 0

**Parameters**

`refcount_t *r`
:   the refcount

**Description**

Similar to [`atomic_dec_and_test()`](basics.md#c.atomic_dec_and_test "atomic_dec_and_test"), it will WARN on underflow and fail to
decrement when saturated at REFCOUNT_SATURATED.

Provides release memory ordering, such that prior loads and stores are done
before, and provides an acquire ordering on success such that free()
must come after.

**Return**

true if the resulting refcount is 0, false otherwise

void refcount_dec(refcount_t \*r)
:   decrement a refcount

**Parameters**

`refcount_t *r`
:   the refcount

**Description**

Similar to [`atomic_dec()`](basics.md#c.atomic_dec "atomic_dec"), it will WARN on underflow and fail to decrement
when saturated at REFCOUNT_SATURATED.

Provides release memory ordering, such that prior loads and stores are done
before.

bool refcount_dec_if_one(refcount_t \*r)
:   decrement a refcount if it is 1

**Parameters**

`refcount_t *r`
:   the refcount

**Description**

No atomic_t counterpart, it attempts a 1 -> 0 transition and returns the
success thereof.

Like all decrement operations, it provides release memory order and provides
a control dependency.

It can be used like a try-delete operator; this explicit case is provided
and not cmpxchg in generic, because that would allow implementing unsafe
operations.

**Return**

true if the resulting refcount is 0, false otherwise

bool refcount_dec_not_one(refcount_t \*r)
:   decrement a refcount if it is not 1

**Parameters**

`refcount_t *r`
:   the refcount

**Description**

No atomic_t counterpart, it decrements unless the value is 1, in which case
it will return false.

Was often done like: atomic_add_unless(`var`, -1, 1)

**Return**

true if the decrement operation was successful, false otherwise

bool refcount_dec_and_mutex_lock(refcount_t \*r, struct mutex \*lock)
:   return holding mutex if able to decrement refcount to 0

**Parameters**

`refcount_t *r`
:   the refcount

`struct mutex *lock`
:   the mutex to be locked

**Description**

Similar to [`atomic_dec_and_mutex_lock()`](../kernel-hacking/locking.md#c.atomic_dec_and_mutex_lock "atomic_dec_and_mutex_lock"), it will WARN on underflow and fail
to decrement when saturated at REFCOUNT_SATURATED.

Provides release memory ordering, such that prior loads and stores are done
before, and provides a control dependency such that free() must come after.
See the comment on top.

**Return**

true and hold mutex if able to decrement refcount to 0, false
:   otherwise

bool refcount_dec_and_lock(refcount_t \*r, spinlock_t \*lock)
:   return holding spinlock if able to decrement refcount to 0

**Parameters**

`refcount_t *r`
:   the refcount

`spinlock_t *lock`
:   the spinlock to be locked

**Description**

Similar to atomic_dec_and_lock(), it will WARN on underflow and fail to
decrement when saturated at REFCOUNT_SATURATED.

Provides release memory ordering, such that prior loads and stores are done
before, and provides a control dependency such that free() must come after.
See the comment on top.

**Return**

true and hold spinlock if able to decrement refcount to 0, false
:   otherwise

bool refcount_dec_and_lock_irqsave(refcount_t \*r, spinlock_t \*lock, unsigned long \*flags)
:   return holding spinlock with disabled interrupts if able to decrement refcount to 0

**Parameters**

`refcount_t *r`
:   the refcount

`spinlock_t *lock`
:   the spinlock to be locked

`unsigned long *flags`
:   saved IRQ-flags if the is acquired

**Description**

Same as [`refcount_dec_and_lock()`](basics.md#c.refcount_dec_and_lock "refcount_dec_and_lock") above except that the spinlock is acquired
with disabled interrupts.

**Return**

true and hold spinlock if able to decrement refcount to 0, false
:   otherwise

## Atomics

int atomic_read(const atomic_t \*v)
:   atomic load with relaxed ordering

**Parameters**

`const atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically loads the value of **v** with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic_read()`](basics.md#c.raw_atomic_read "raw_atomic_read") there.

**Return**

The value loaded from **v**.

int atomic_read_acquire(const atomic_t \*v)
:   atomic load with acquire ordering

**Parameters**

`const atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically loads the value of **v** with acquire ordering.

Unsafe to use in noinstr code; use [`raw_atomic_read_acquire()`](basics.md#c.raw_atomic_read_acquire "raw_atomic_read_acquire") there.

**Return**

The value loaded from **v**.

void atomic_set(atomic_t \*v, int i)
:   atomic set with relaxed ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

`int i`
:   int value to assign

**Description**

Atomically sets **v** to **i** with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic_set()`](basics.md#c.raw_atomic_set "raw_atomic_set") there.

**Return**

Nothing.

void atomic_set_release(atomic_t \*v, int i)
:   atomic set with release ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

`int i`
:   int value to assign

**Description**

Atomically sets **v** to **i** with release ordering.

Unsafe to use in noinstr code; use [`raw_atomic_set_release()`](basics.md#c.raw_atomic_set_release "raw_atomic_set_release") there.

**Return**

Nothing.

void atomic_add(int i, atomic_t \*v)
:   atomic add with relaxed ordering

**Parameters**

`int i`
:   int value to add

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** + **i**) with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic_add()`](basics.md#c.raw_atomic_add "raw_atomic_add") there.

**Return**

Nothing.

int atomic_add_return(int i, atomic_t \*v)
:   atomic add with full ordering

**Parameters**

`int i`
:   int value to add

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** + **i**) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic_add_return()`](basics.md#c.raw_atomic_add_return "raw_atomic_add_return") there.

**Return**

The updated value of **v**.

int atomic_add_return_acquire(int i, atomic_t \*v)
:   atomic add with acquire ordering

**Parameters**

`int i`
:   int value to add

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** + **i**) with acquire ordering.

Unsafe to use in noinstr code; use [`raw_atomic_add_return_acquire()`](basics.md#c.raw_atomic_add_return_acquire "raw_atomic_add_return_acquire") there.

**Return**

The updated value of **v**.

int atomic_add_return_release(int i, atomic_t \*v)
:   atomic add with release ordering

**Parameters**

`int i`
:   int value to add

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** + **i**) with release ordering.

Unsafe to use in noinstr code; use [`raw_atomic_add_return_release()`](basics.md#c.raw_atomic_add_return_release "raw_atomic_add_return_release") there.

**Return**

The updated value of **v**.

int atomic_add_return_relaxed(int i, atomic_t \*v)
:   atomic add with relaxed ordering

**Parameters**

`int i`
:   int value to add

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** + **i**) with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic_add_return_relaxed()`](basics.md#c.raw_atomic_add_return_relaxed "raw_atomic_add_return_relaxed") there.

**Return**

The updated value of **v**.

int atomic_fetch_add(int i, atomic_t \*v)
:   atomic add with full ordering

**Parameters**

`int i`
:   int value to add

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** + **i**) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic_fetch_add()`](basics.md#c.raw_atomic_fetch_add "raw_atomic_fetch_add") there.

**Return**

The original value of **v**.

int atomic_fetch_add_acquire(int i, atomic_t \*v)
:   atomic add with acquire ordering

**Parameters**

`int i`
:   int value to add

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** + **i**) with acquire ordering.

Unsafe to use in noinstr code; use [`raw_atomic_fetch_add_acquire()`](basics.md#c.raw_atomic_fetch_add_acquire "raw_atomic_fetch_add_acquire") there.

**Return**

The original value of **v**.

int atomic_fetch_add_release(int i, atomic_t \*v)
:   atomic add with release ordering

**Parameters**

`int i`
:   int value to add

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** + **i**) with release ordering.

Unsafe to use in noinstr code; use [`raw_atomic_fetch_add_release()`](basics.md#c.raw_atomic_fetch_add_release "raw_atomic_fetch_add_release") there.

**Return**

The original value of **v**.

int atomic_fetch_add_relaxed(int i, atomic_t \*v)
:   atomic add with relaxed ordering

**Parameters**

`int i`
:   int value to add

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** + **i**) with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic_fetch_add_relaxed()`](basics.md#c.raw_atomic_fetch_add_relaxed "raw_atomic_fetch_add_relaxed") there.

**Return**

The original value of **v**.

void atomic_sub(int i, atomic_t \*v)
:   atomic subtract with relaxed ordering

**Parameters**

`int i`
:   int value to subtract

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** - **i**) with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic_sub()`](basics.md#c.raw_atomic_sub "raw_atomic_sub") there.

**Return**

Nothing.

int atomic_sub_return(int i, atomic_t \*v)
:   atomic subtract with full ordering

**Parameters**

`int i`
:   int value to subtract

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** - **i**) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic_sub_return()`](basics.md#c.raw_atomic_sub_return "raw_atomic_sub_return") there.

**Return**

The updated value of **v**.

int atomic_sub_return_acquire(int i, atomic_t \*v)
:   atomic subtract with acquire ordering

**Parameters**

`int i`
:   int value to subtract

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** - **i**) with acquire ordering.

Unsafe to use in noinstr code; use [`raw_atomic_sub_return_acquire()`](basics.md#c.raw_atomic_sub_return_acquire "raw_atomic_sub_return_acquire") there.

**Return**

The updated value of **v**.

int atomic_sub_return_release(int i, atomic_t \*v)
:   atomic subtract with release ordering

**Parameters**

`int i`
:   int value to subtract

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** - **i**) with release ordering.

Unsafe to use in noinstr code; use [`raw_atomic_sub_return_release()`](basics.md#c.raw_atomic_sub_return_release "raw_atomic_sub_return_release") there.

**Return**

The updated value of **v**.

int atomic_sub_return_relaxed(int i, atomic_t \*v)
:   atomic subtract with relaxed ordering

**Parameters**

`int i`
:   int value to subtract

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** - **i**) with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic_sub_return_relaxed()`](basics.md#c.raw_atomic_sub_return_relaxed "raw_atomic_sub_return_relaxed") there.

**Return**

The updated value of **v**.

int atomic_fetch_sub(int i, atomic_t \*v)
:   atomic subtract with full ordering

**Parameters**

`int i`
:   int value to subtract

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** - **i**) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic_fetch_sub()`](basics.md#c.raw_atomic_fetch_sub "raw_atomic_fetch_sub") there.

**Return**

The original value of **v**.

int atomic_fetch_sub_acquire(int i, atomic_t \*v)
:   atomic subtract with acquire ordering

**Parameters**

`int i`
:   int value to subtract

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** - **i**) with acquire ordering.

Unsafe to use in noinstr code; use [`raw_atomic_fetch_sub_acquire()`](basics.md#c.raw_atomic_fetch_sub_acquire "raw_atomic_fetch_sub_acquire") there.

**Return**

The original value of **v**.

int atomic_fetch_sub_release(int i, atomic_t \*v)
:   atomic subtract with release ordering

**Parameters**

`int i`
:   int value to subtract

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** - **i**) with release ordering.

Unsafe to use in noinstr code; use [`raw_atomic_fetch_sub_release()`](basics.md#c.raw_atomic_fetch_sub_release "raw_atomic_fetch_sub_release") there.

**Return**

The original value of **v**.

int atomic_fetch_sub_relaxed(int i, atomic_t \*v)
:   atomic subtract with relaxed ordering

**Parameters**

`int i`
:   int value to subtract

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** - **i**) with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic_fetch_sub_relaxed()`](basics.md#c.raw_atomic_fetch_sub_relaxed "raw_atomic_fetch_sub_relaxed") there.

**Return**

The original value of **v**.

void atomic_inc(atomic_t \*v)
:   atomic increment with relaxed ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** + 1) with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic_inc()`](basics.md#c.raw_atomic_inc "raw_atomic_inc") there.

**Return**

Nothing.

int atomic_inc_return(atomic_t \*v)
:   atomic increment with full ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** + 1) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic_inc_return()`](basics.md#c.raw_atomic_inc_return "raw_atomic_inc_return") there.

**Return**

The updated value of **v**.

int atomic_inc_return_acquire(atomic_t \*v)
:   atomic increment with acquire ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** + 1) with acquire ordering.

Unsafe to use in noinstr code; use [`raw_atomic_inc_return_acquire()`](basics.md#c.raw_atomic_inc_return_acquire "raw_atomic_inc_return_acquire") there.

**Return**

The updated value of **v**.

int atomic_inc_return_release(atomic_t \*v)
:   atomic increment with release ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** + 1) with release ordering.

Unsafe to use in noinstr code; use [`raw_atomic_inc_return_release()`](basics.md#c.raw_atomic_inc_return_release "raw_atomic_inc_return_release") there.

**Return**

The updated value of **v**.

int atomic_inc_return_relaxed(atomic_t \*v)
:   atomic increment with relaxed ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** + 1) with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic_inc_return_relaxed()`](basics.md#c.raw_atomic_inc_return_relaxed "raw_atomic_inc_return_relaxed") there.

**Return**

The updated value of **v**.

int atomic_fetch_inc(atomic_t \*v)
:   atomic increment with full ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** + 1) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic_fetch_inc()`](basics.md#c.raw_atomic_fetch_inc "raw_atomic_fetch_inc") there.

**Return**

The original value of **v**.

int atomic_fetch_inc_acquire(atomic_t \*v)
:   atomic increment with acquire ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** + 1) with acquire ordering.

Unsafe to use in noinstr code; use [`raw_atomic_fetch_inc_acquire()`](basics.md#c.raw_atomic_fetch_inc_acquire "raw_atomic_fetch_inc_acquire") there.

**Return**

The original value of **v**.

int atomic_fetch_inc_release(atomic_t \*v)
:   atomic increment with release ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** + 1) with release ordering.

Unsafe to use in noinstr code; use [`raw_atomic_fetch_inc_release()`](basics.md#c.raw_atomic_fetch_inc_release "raw_atomic_fetch_inc_release") there.

**Return**

The original value of **v**.

int atomic_fetch_inc_relaxed(atomic_t \*v)
:   atomic increment with relaxed ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** + 1) with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic_fetch_inc_relaxed()`](basics.md#c.raw_atomic_fetch_inc_relaxed "raw_atomic_fetch_inc_relaxed") there.

**Return**

The original value of **v**.

void atomic_dec(atomic_t \*v)
:   atomic decrement with relaxed ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** - 1) with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic_dec()`](basics.md#c.raw_atomic_dec "raw_atomic_dec") there.

**Return**

Nothing.

int atomic_dec_return(atomic_t \*v)
:   atomic decrement with full ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** - 1) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic_dec_return()`](basics.md#c.raw_atomic_dec_return "raw_atomic_dec_return") there.

**Return**

The updated value of **v**.

int atomic_dec_return_acquire(atomic_t \*v)
:   atomic decrement with acquire ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** - 1) with acquire ordering.

Unsafe to use in noinstr code; use [`raw_atomic_dec_return_acquire()`](basics.md#c.raw_atomic_dec_return_acquire "raw_atomic_dec_return_acquire") there.

**Return**

The updated value of **v**.

int atomic_dec_return_release(atomic_t \*v)
:   atomic decrement with release ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** - 1) with release ordering.

Unsafe to use in noinstr code; use [`raw_atomic_dec_return_release()`](basics.md#c.raw_atomic_dec_return_release "raw_atomic_dec_return_release") there.

**Return**

The updated value of **v**.

int atomic_dec_return_relaxed(atomic_t \*v)
:   atomic decrement with relaxed ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** - 1) with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic_dec_return_relaxed()`](basics.md#c.raw_atomic_dec_return_relaxed "raw_atomic_dec_return_relaxed") there.

**Return**

The updated value of **v**.

int atomic_fetch_dec(atomic_t \*v)
:   atomic decrement with full ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** - 1) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic_fetch_dec()`](basics.md#c.raw_atomic_fetch_dec "raw_atomic_fetch_dec") there.

**Return**

The original value of **v**.

int atomic_fetch_dec_acquire(atomic_t \*v)
:   atomic decrement with acquire ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** - 1) with acquire ordering.

Unsafe to use in noinstr code; use [`raw_atomic_fetch_dec_acquire()`](basics.md#c.raw_atomic_fetch_dec_acquire "raw_atomic_fetch_dec_acquire") there.

**Return**

The original value of **v**.

int atomic_fetch_dec_release(atomic_t \*v)
:   atomic decrement with release ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** - 1) with release ordering.

Unsafe to use in noinstr code; use [`raw_atomic_fetch_dec_release()`](basics.md#c.raw_atomic_fetch_dec_release "raw_atomic_fetch_dec_release") there.

**Return**

The original value of **v**.

int atomic_fetch_dec_relaxed(atomic_t \*v)
:   atomic decrement with relaxed ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** - 1) with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic_fetch_dec_relaxed()`](basics.md#c.raw_atomic_fetch_dec_relaxed "raw_atomic_fetch_dec_relaxed") there.

**Return**

The original value of **v**.

void atomic_and(int i, atomic_t \*v)
:   atomic bitwise AND with relaxed ordering

**Parameters**

`int i`
:   int value

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** & **i**) with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic_and()`](basics.md#c.raw_atomic_and "raw_atomic_and") there.

**Return**

Nothing.

int atomic_fetch_and(int i, atomic_t \*v)
:   atomic bitwise AND with full ordering

**Parameters**

`int i`
:   int value

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** & **i**) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic_fetch_and()`](basics.md#c.raw_atomic_fetch_and "raw_atomic_fetch_and") there.

**Return**

The original value of **v**.

int atomic_fetch_and_acquire(int i, atomic_t \*v)
:   atomic bitwise AND with acquire ordering

**Parameters**

`int i`
:   int value

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** & **i**) with acquire ordering.

Unsafe to use in noinstr code; use [`raw_atomic_fetch_and_acquire()`](basics.md#c.raw_atomic_fetch_and_acquire "raw_atomic_fetch_and_acquire") there.

**Return**

The original value of **v**.

int atomic_fetch_and_release(int i, atomic_t \*v)
:   atomic bitwise AND with release ordering

**Parameters**

`int i`
:   int value

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** & **i**) with release ordering.

Unsafe to use in noinstr code; use [`raw_atomic_fetch_and_release()`](basics.md#c.raw_atomic_fetch_and_release "raw_atomic_fetch_and_release") there.

**Return**

The original value of **v**.

int atomic_fetch_and_relaxed(int i, atomic_t \*v)
:   atomic bitwise AND with relaxed ordering

**Parameters**

`int i`
:   int value

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** & **i**) with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic_fetch_and_relaxed()`](basics.md#c.raw_atomic_fetch_and_relaxed "raw_atomic_fetch_and_relaxed") there.

**Return**

The original value of **v**.

void atomic_andnot(int i, atomic_t \*v)
:   atomic bitwise AND NOT with relaxed ordering

**Parameters**

`int i`
:   int value

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** & **~i**) with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic_andnot()`](basics.md#c.raw_atomic_andnot "raw_atomic_andnot") there.

**Return**

Nothing.

int atomic_fetch_andnot(int i, atomic_t \*v)
:   atomic bitwise AND NOT with full ordering

**Parameters**

`int i`
:   int value

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** & **~i**) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic_fetch_andnot()`](basics.md#c.raw_atomic_fetch_andnot "raw_atomic_fetch_andnot") there.

**Return**

The original value of **v**.

int atomic_fetch_andnot_acquire(int i, atomic_t \*v)
:   atomic bitwise AND NOT with acquire ordering

**Parameters**

`int i`
:   int value

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** & **~i**) with acquire ordering.

Unsafe to use in noinstr code; use [`raw_atomic_fetch_andnot_acquire()`](basics.md#c.raw_atomic_fetch_andnot_acquire "raw_atomic_fetch_andnot_acquire") there.

**Return**

The original value of **v**.

int atomic_fetch_andnot_release(int i, atomic_t \*v)
:   atomic bitwise AND NOT with release ordering

**Parameters**

`int i`
:   int value

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** & **~i**) with release ordering.

Unsafe to use in noinstr code; use [`raw_atomic_fetch_andnot_release()`](basics.md#c.raw_atomic_fetch_andnot_release "raw_atomic_fetch_andnot_release") there.

**Return**

The original value of **v**.

int atomic_fetch_andnot_relaxed(int i, atomic_t \*v)
:   atomic bitwise AND NOT with relaxed ordering

**Parameters**

`int i`
:   int value

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** & **~i**) with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic_fetch_andnot_relaxed()`](basics.md#c.raw_atomic_fetch_andnot_relaxed "raw_atomic_fetch_andnot_relaxed") there.

**Return**

The original value of **v**.

void atomic_or(int i, atomic_t \*v)
:   atomic bitwise OR with relaxed ordering

**Parameters**

`int i`
:   int value

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** | **i**) with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic_or()`](basics.md#c.raw_atomic_or "raw_atomic_or") there.

**Return**

Nothing.

int atomic_fetch_or(int i, atomic_t \*v)
:   atomic bitwise OR with full ordering

**Parameters**

`int i`
:   int value

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** | **i**) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic_fetch_or()`](basics.md#c.raw_atomic_fetch_or "raw_atomic_fetch_or") there.

**Return**

The original value of **v**.

int atomic_fetch_or_acquire(int i, atomic_t \*v)
:   atomic bitwise OR with acquire ordering

**Parameters**

`int i`
:   int value

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** | **i**) with acquire ordering.

Unsafe to use in noinstr code; use [`raw_atomic_fetch_or_acquire()`](basics.md#c.raw_atomic_fetch_or_acquire "raw_atomic_fetch_or_acquire") there.

**Return**

The original value of **v**.

int atomic_fetch_or_release(int i, atomic_t \*v)
:   atomic bitwise OR with release ordering

**Parameters**

`int i`
:   int value

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** | **i**) with release ordering.

Unsafe to use in noinstr code; use [`raw_atomic_fetch_or_release()`](basics.md#c.raw_atomic_fetch_or_release "raw_atomic_fetch_or_release") there.

**Return**

The original value of **v**.

int atomic_fetch_or_relaxed(int i, atomic_t \*v)
:   atomic bitwise OR with relaxed ordering

**Parameters**

`int i`
:   int value

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** | **i**) with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic_fetch_or_relaxed()`](basics.md#c.raw_atomic_fetch_or_relaxed "raw_atomic_fetch_or_relaxed") there.

**Return**

The original value of **v**.

void atomic_xor(int i, atomic_t \*v)
:   atomic bitwise XOR with relaxed ordering

**Parameters**

`int i`
:   int value

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** ^ **i**) with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic_xor()`](basics.md#c.raw_atomic_xor "raw_atomic_xor") there.

**Return**

Nothing.

int atomic_fetch_xor(int i, atomic_t \*v)
:   atomic bitwise XOR with full ordering

**Parameters**

`int i`
:   int value

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** ^ **i**) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic_fetch_xor()`](basics.md#c.raw_atomic_fetch_xor "raw_atomic_fetch_xor") there.

**Return**

The original value of **v**.

int atomic_fetch_xor_acquire(int i, atomic_t \*v)
:   atomic bitwise XOR with acquire ordering

**Parameters**

`int i`
:   int value

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** ^ **i**) with acquire ordering.

Unsafe to use in noinstr code; use [`raw_atomic_fetch_xor_acquire()`](basics.md#c.raw_atomic_fetch_xor_acquire "raw_atomic_fetch_xor_acquire") there.

**Return**

The original value of **v**.

int atomic_fetch_xor_release(int i, atomic_t \*v)
:   atomic bitwise XOR with release ordering

**Parameters**

`int i`
:   int value

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** ^ **i**) with release ordering.

Unsafe to use in noinstr code; use [`raw_atomic_fetch_xor_release()`](basics.md#c.raw_atomic_fetch_xor_release "raw_atomic_fetch_xor_release") there.

**Return**

The original value of **v**.

int atomic_fetch_xor_relaxed(int i, atomic_t \*v)
:   atomic bitwise XOR with relaxed ordering

**Parameters**

`int i`
:   int value

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** ^ **i**) with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic_fetch_xor_relaxed()`](basics.md#c.raw_atomic_fetch_xor_relaxed "raw_atomic_fetch_xor_relaxed") there.

**Return**

The original value of **v**.

int atomic_xchg(atomic_t \*v, int new)
:   atomic exchange with full ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

`int new`
:   int value to assign

**Description**

Atomically updates **v** to **new** with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic_xchg()`](basics.md#c.raw_atomic_xchg "raw_atomic_xchg") there.

**Return**

The original value of **v**.

int atomic_xchg_acquire(atomic_t \*v, int new)
:   atomic exchange with acquire ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

`int new`
:   int value to assign

**Description**

Atomically updates **v** to **new** with acquire ordering.

Unsafe to use in noinstr code; use [`raw_atomic_xchg_acquire()`](basics.md#c.raw_atomic_xchg_acquire "raw_atomic_xchg_acquire") there.

**Return**

The original value of **v**.

int atomic_xchg_release(atomic_t \*v, int new)
:   atomic exchange with release ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

`int new`
:   int value to assign

**Description**

Atomically updates **v** to **new** with release ordering.

Unsafe to use in noinstr code; use [`raw_atomic_xchg_release()`](basics.md#c.raw_atomic_xchg_release "raw_atomic_xchg_release") there.

**Return**

The original value of **v**.

int atomic_xchg_relaxed(atomic_t \*v, int new)
:   atomic exchange with relaxed ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

`int new`
:   int value to assign

**Description**

Atomically updates **v** to **new** with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic_xchg_relaxed()`](basics.md#c.raw_atomic_xchg_relaxed "raw_atomic_xchg_relaxed") there.

**Return**

The original value of **v**.

int atomic_cmpxchg(atomic_t \*v, int old, int new)
:   atomic compare and exchange with full ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

`int old`
:   int value to compare with

`int new`
:   int value to assign

**Description**

If (**v** == **old**), atomically updates **v** to **new** with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic_cmpxchg()`](basics.md#c.raw_atomic_cmpxchg "raw_atomic_cmpxchg") there.

**Return**

The original value of **v**.

int atomic_cmpxchg_acquire(atomic_t \*v, int old, int new)
:   atomic compare and exchange with acquire ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

`int old`
:   int value to compare with

`int new`
:   int value to assign

**Description**

If (**v** == **old**), atomically updates **v** to **new** with acquire ordering.

Unsafe to use in noinstr code; use [`raw_atomic_cmpxchg_acquire()`](basics.md#c.raw_atomic_cmpxchg_acquire "raw_atomic_cmpxchg_acquire") there.

**Return**

The original value of **v**.

int atomic_cmpxchg_release(atomic_t \*v, int old, int new)
:   atomic compare and exchange with release ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

`int old`
:   int value to compare with

`int new`
:   int value to assign

**Description**

If (**v** == **old**), atomically updates **v** to **new** with release ordering.

Unsafe to use in noinstr code; use [`raw_atomic_cmpxchg_release()`](basics.md#c.raw_atomic_cmpxchg_release "raw_atomic_cmpxchg_release") there.

**Return**

The original value of **v**.

int atomic_cmpxchg_relaxed(atomic_t \*v, int old, int new)
:   atomic compare and exchange with relaxed ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

`int old`
:   int value to compare with

`int new`
:   int value to assign

**Description**

If (**v** == **old**), atomically updates **v** to **new** with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic_cmpxchg_relaxed()`](basics.md#c.raw_atomic_cmpxchg_relaxed "raw_atomic_cmpxchg_relaxed") there.

**Return**

The original value of **v**.

bool atomic_try_cmpxchg(atomic_t \*v, int \*old, int new)
:   atomic compare and exchange with full ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

`int *old`
:   pointer to int value to compare with

`int new`
:   int value to assign

**Description**

If (**v** == **old**), atomically updates **v** to **new** with full ordering.
Otherwise, updates **old** to the current value of **v**.

Unsafe to use in noinstr code; use [`raw_atomic_try_cmpxchg()`](basics.md#c.raw_atomic_try_cmpxchg "raw_atomic_try_cmpxchg") there.

**Return**

**true** if the exchange occured, **false** otherwise.

bool atomic_try_cmpxchg_acquire(atomic_t \*v, int \*old, int new)
:   atomic compare and exchange with acquire ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

`int *old`
:   pointer to int value to compare with

`int new`
:   int value to assign

**Description**

If (**v** == **old**), atomically updates **v** to **new** with acquire ordering.
Otherwise, updates **old** to the current value of **v**.

Unsafe to use in noinstr code; use [`raw_atomic_try_cmpxchg_acquire()`](basics.md#c.raw_atomic_try_cmpxchg_acquire "raw_atomic_try_cmpxchg_acquire") there.

**Return**

**true** if the exchange occured, **false** otherwise.

bool atomic_try_cmpxchg_release(atomic_t \*v, int \*old, int new)
:   atomic compare and exchange with release ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

`int *old`
:   pointer to int value to compare with

`int new`
:   int value to assign

**Description**

If (**v** == **old**), atomically updates **v** to **new** with release ordering.
Otherwise, updates **old** to the current value of **v**.

Unsafe to use in noinstr code; use [`raw_atomic_try_cmpxchg_release()`](basics.md#c.raw_atomic_try_cmpxchg_release "raw_atomic_try_cmpxchg_release") there.

**Return**

**true** if the exchange occured, **false** otherwise.

bool atomic_try_cmpxchg_relaxed(atomic_t \*v, int \*old, int new)
:   atomic compare and exchange with relaxed ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

`int *old`
:   pointer to int value to compare with

`int new`
:   int value to assign

**Description**

If (**v** == **old**), atomically updates **v** to **new** with relaxed ordering.
Otherwise, updates **old** to the current value of **v**.

Unsafe to use in noinstr code; use [`raw_atomic_try_cmpxchg_relaxed()`](basics.md#c.raw_atomic_try_cmpxchg_relaxed "raw_atomic_try_cmpxchg_relaxed") there.

**Return**

**true** if the exchange occured, **false** otherwise.

bool atomic_sub_and_test(int i, atomic_t \*v)
:   atomic subtract and test if zero with full ordering

**Parameters**

`int i`
:   int value to add

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** - **i**) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic_sub_and_test()`](basics.md#c.raw_atomic_sub_and_test "raw_atomic_sub_and_test") there.

**Return**

**true** if the resulting value of **v** is zero, **false** otherwise.

bool atomic_dec_and_test(atomic_t \*v)
:   atomic decrement and test if zero with full ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** - 1) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic_dec_and_test()`](basics.md#c.raw_atomic_dec_and_test "raw_atomic_dec_and_test") there.

**Return**

**true** if the resulting value of **v** is zero, **false** otherwise.

bool atomic_inc_and_test(atomic_t \*v)
:   atomic increment and test if zero with full ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** + 1) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic_inc_and_test()`](basics.md#c.raw_atomic_inc_and_test "raw_atomic_inc_and_test") there.

**Return**

**true** if the resulting value of **v** is zero, **false** otherwise.

bool atomic_add_negative(int i, atomic_t \*v)
:   atomic add and test if negative with full ordering

**Parameters**

`int i`
:   int value to add

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** + **i**) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic_add_negative()`](basics.md#c.raw_atomic_add_negative "raw_atomic_add_negative") there.

**Return**

**true** if the resulting value of **v** is negative, **false** otherwise.

bool atomic_add_negative_acquire(int i, atomic_t \*v)
:   atomic add and test if negative with acquire ordering

**Parameters**

`int i`
:   int value to add

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** + **i**) with acquire ordering.

Unsafe to use in noinstr code; use [`raw_atomic_add_negative_acquire()`](basics.md#c.raw_atomic_add_negative_acquire "raw_atomic_add_negative_acquire") there.

**Return**

**true** if the resulting value of **v** is negative, **false** otherwise.

bool atomic_add_negative_release(int i, atomic_t \*v)
:   atomic add and test if negative with release ordering

**Parameters**

`int i`
:   int value to add

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** + **i**) with release ordering.

Unsafe to use in noinstr code; use [`raw_atomic_add_negative_release()`](basics.md#c.raw_atomic_add_negative_release "raw_atomic_add_negative_release") there.

**Return**

**true** if the resulting value of **v** is negative, **false** otherwise.

bool atomic_add_negative_relaxed(int i, atomic_t \*v)
:   atomic add and test if negative with relaxed ordering

**Parameters**

`int i`
:   int value to add

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** + **i**) with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic_add_negative_relaxed()`](basics.md#c.raw_atomic_add_negative_relaxed "raw_atomic_add_negative_relaxed") there.

**Return**

**true** if the resulting value of **v** is negative, **false** otherwise.

int atomic_fetch_add_unless(atomic_t \*v, int a, int u)
:   atomic add unless value with full ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

`int a`
:   int value to add

`int u`
:   int value to compare with

**Description**

If (**v** != **u**), atomically updates **v** to (**v** + **a**) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic_fetch_add_unless()`](basics.md#c.raw_atomic_fetch_add_unless "raw_atomic_fetch_add_unless") there.

**Return**

The original value of **v**.

bool atomic_add_unless(atomic_t \*v, int a, int u)
:   atomic add unless value with full ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

`int a`
:   int value to add

`int u`
:   int value to compare with

**Description**

If (**v** != **u**), atomically updates **v** to (**v** + **a**) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic_add_unless()`](basics.md#c.raw_atomic_add_unless "raw_atomic_add_unless") there.

**Return**

**true** if **v** was updated, **false** otherwise.

bool atomic_inc_not_zero(atomic_t \*v)
:   atomic increment unless zero with full ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

**Description**

If (**v** != 0), atomically updates **v** to (**v** + 1) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic_inc_not_zero()`](basics.md#c.raw_atomic_inc_not_zero "raw_atomic_inc_not_zero") there.

**Return**

**true** if **v** was updated, **false** otherwise.

bool atomic_inc_unless_negative(atomic_t \*v)
:   atomic increment unless negative with full ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

**Description**

If (**v** >= 0), atomically updates **v** to (**v** + 1) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic_inc_unless_negative()`](basics.md#c.raw_atomic_inc_unless_negative "raw_atomic_inc_unless_negative") there.

**Return**

**true** if **v** was updated, **false** otherwise.

bool atomic_dec_unless_positive(atomic_t \*v)
:   atomic decrement unless positive with full ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

**Description**

If (**v** <= 0), atomically updates **v** to (**v** - 1) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic_dec_unless_positive()`](basics.md#c.raw_atomic_dec_unless_positive "raw_atomic_dec_unless_positive") there.

**Return**

**true** if **v** was updated, **false** otherwise.

int atomic_dec_if_positive(atomic_t \*v)
:   atomic decrement if positive with full ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

**Description**

If (**v** > 0), atomically updates **v** to (**v** - 1) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic_dec_if_positive()`](basics.md#c.raw_atomic_dec_if_positive "raw_atomic_dec_if_positive") there.

**Return**

The old value of (**v** - 1), regardless of whether **v** was updated.

s64 atomic64_read(const atomic64_t \*v)
:   atomic load with relaxed ordering

**Parameters**

`const atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically loads the value of **v** with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_read()`](basics.md#c.raw_atomic64_read "raw_atomic64_read") there.

**Return**

The value loaded from **v**.

s64 atomic64_read_acquire(const atomic64_t \*v)
:   atomic load with acquire ordering

**Parameters**

`const atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically loads the value of **v** with acquire ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_read_acquire()`](basics.md#c.raw_atomic64_read_acquire "raw_atomic64_read_acquire") there.

**Return**

The value loaded from **v**.

void atomic64_set(atomic64_t \*v, s64 i)
:   atomic set with relaxed ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

`s64 i`
:   s64 value to assign

**Description**

Atomically sets **v** to **i** with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_set()`](basics.md#c.raw_atomic64_set "raw_atomic64_set") there.

**Return**

Nothing.

void atomic64_set_release(atomic64_t \*v, s64 i)
:   atomic set with release ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

`s64 i`
:   s64 value to assign

**Description**

Atomically sets **v** to **i** with release ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_set_release()`](basics.md#c.raw_atomic64_set_release "raw_atomic64_set_release") there.

**Return**

Nothing.

void atomic64_add(s64 i, atomic64_t \*v)
:   atomic add with relaxed ordering

**Parameters**

`s64 i`
:   s64 value to add

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** + **i**) with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_add()`](basics.md#c.raw_atomic64_add "raw_atomic64_add") there.

**Return**

Nothing.

s64 atomic64_add_return(s64 i, atomic64_t \*v)
:   atomic add with full ordering

**Parameters**

`s64 i`
:   s64 value to add

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** + **i**) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_add_return()`](basics.md#c.raw_atomic64_add_return "raw_atomic64_add_return") there.

**Return**

The updated value of **v**.

s64 atomic64_add_return_acquire(s64 i, atomic64_t \*v)
:   atomic add with acquire ordering

**Parameters**

`s64 i`
:   s64 value to add

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** + **i**) with acquire ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_add_return_acquire()`](basics.md#c.raw_atomic64_add_return_acquire "raw_atomic64_add_return_acquire") there.

**Return**

The updated value of **v**.

s64 atomic64_add_return_release(s64 i, atomic64_t \*v)
:   atomic add with release ordering

**Parameters**

`s64 i`
:   s64 value to add

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** + **i**) with release ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_add_return_release()`](basics.md#c.raw_atomic64_add_return_release "raw_atomic64_add_return_release") there.

**Return**

The updated value of **v**.

s64 atomic64_add_return_relaxed(s64 i, atomic64_t \*v)
:   atomic add with relaxed ordering

**Parameters**

`s64 i`
:   s64 value to add

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** + **i**) with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_add_return_relaxed()`](basics.md#c.raw_atomic64_add_return_relaxed "raw_atomic64_add_return_relaxed") there.

**Return**

The updated value of **v**.

s64 atomic64_fetch_add(s64 i, atomic64_t \*v)
:   atomic add with full ordering

**Parameters**

`s64 i`
:   s64 value to add

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** + **i**) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_fetch_add()`](basics.md#c.raw_atomic64_fetch_add "raw_atomic64_fetch_add") there.

**Return**

The original value of **v**.

s64 atomic64_fetch_add_acquire(s64 i, atomic64_t \*v)
:   atomic add with acquire ordering

**Parameters**

`s64 i`
:   s64 value to add

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** + **i**) with acquire ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_fetch_add_acquire()`](basics.md#c.raw_atomic64_fetch_add_acquire "raw_atomic64_fetch_add_acquire") there.

**Return**

The original value of **v**.

s64 atomic64_fetch_add_release(s64 i, atomic64_t \*v)
:   atomic add with release ordering

**Parameters**

`s64 i`
:   s64 value to add

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** + **i**) with release ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_fetch_add_release()`](basics.md#c.raw_atomic64_fetch_add_release "raw_atomic64_fetch_add_release") there.

**Return**

The original value of **v**.

s64 atomic64_fetch_add_relaxed(s64 i, atomic64_t \*v)
:   atomic add with relaxed ordering

**Parameters**

`s64 i`
:   s64 value to add

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** + **i**) with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_fetch_add_relaxed()`](basics.md#c.raw_atomic64_fetch_add_relaxed "raw_atomic64_fetch_add_relaxed") there.

**Return**

The original value of **v**.

void atomic64_sub(s64 i, atomic64_t \*v)
:   atomic subtract with relaxed ordering

**Parameters**

`s64 i`
:   s64 value to subtract

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** - **i**) with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_sub()`](basics.md#c.raw_atomic64_sub "raw_atomic64_sub") there.

**Return**

Nothing.

s64 atomic64_sub_return(s64 i, atomic64_t \*v)
:   atomic subtract with full ordering

**Parameters**

`s64 i`
:   s64 value to subtract

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** - **i**) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_sub_return()`](basics.md#c.raw_atomic64_sub_return "raw_atomic64_sub_return") there.

**Return**

The updated value of **v**.

s64 atomic64_sub_return_acquire(s64 i, atomic64_t \*v)
:   atomic subtract with acquire ordering

**Parameters**

`s64 i`
:   s64 value to subtract

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** - **i**) with acquire ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_sub_return_acquire()`](basics.md#c.raw_atomic64_sub_return_acquire "raw_atomic64_sub_return_acquire") there.

**Return**

The updated value of **v**.

s64 atomic64_sub_return_release(s64 i, atomic64_t \*v)
:   atomic subtract with release ordering

**Parameters**

`s64 i`
:   s64 value to subtract

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** - **i**) with release ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_sub_return_release()`](basics.md#c.raw_atomic64_sub_return_release "raw_atomic64_sub_return_release") there.

**Return**

The updated value of **v**.

s64 atomic64_sub_return_relaxed(s64 i, atomic64_t \*v)
:   atomic subtract with relaxed ordering

**Parameters**

`s64 i`
:   s64 value to subtract

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** - **i**) with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_sub_return_relaxed()`](basics.md#c.raw_atomic64_sub_return_relaxed "raw_atomic64_sub_return_relaxed") there.

**Return**

The updated value of **v**.

s64 atomic64_fetch_sub(s64 i, atomic64_t \*v)
:   atomic subtract with full ordering

**Parameters**

`s64 i`
:   s64 value to subtract

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** - **i**) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_fetch_sub()`](basics.md#c.raw_atomic64_fetch_sub "raw_atomic64_fetch_sub") there.

**Return**

The original value of **v**.

s64 atomic64_fetch_sub_acquire(s64 i, atomic64_t \*v)
:   atomic subtract with acquire ordering

**Parameters**

`s64 i`
:   s64 value to subtract

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** - **i**) with acquire ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_fetch_sub_acquire()`](basics.md#c.raw_atomic64_fetch_sub_acquire "raw_atomic64_fetch_sub_acquire") there.

**Return**

The original value of **v**.

s64 atomic64_fetch_sub_release(s64 i, atomic64_t \*v)
:   atomic subtract with release ordering

**Parameters**

`s64 i`
:   s64 value to subtract

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** - **i**) with release ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_fetch_sub_release()`](basics.md#c.raw_atomic64_fetch_sub_release "raw_atomic64_fetch_sub_release") there.

**Return**

The original value of **v**.

s64 atomic64_fetch_sub_relaxed(s64 i, atomic64_t \*v)
:   atomic subtract with relaxed ordering

**Parameters**

`s64 i`
:   s64 value to subtract

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** - **i**) with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_fetch_sub_relaxed()`](basics.md#c.raw_atomic64_fetch_sub_relaxed "raw_atomic64_fetch_sub_relaxed") there.

**Return**

The original value of **v**.

void atomic64_inc(atomic64_t \*v)
:   atomic increment with relaxed ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** + 1) with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_inc()`](basics.md#c.raw_atomic64_inc "raw_atomic64_inc") there.

**Return**

Nothing.

s64 atomic64_inc_return(atomic64_t \*v)
:   atomic increment with full ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** + 1) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_inc_return()`](basics.md#c.raw_atomic64_inc_return "raw_atomic64_inc_return") there.

**Return**

The updated value of **v**.

s64 atomic64_inc_return_acquire(atomic64_t \*v)
:   atomic increment with acquire ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** + 1) with acquire ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_inc_return_acquire()`](basics.md#c.raw_atomic64_inc_return_acquire "raw_atomic64_inc_return_acquire") there.

**Return**

The updated value of **v**.

s64 atomic64_inc_return_release(atomic64_t \*v)
:   atomic increment with release ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** + 1) with release ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_inc_return_release()`](basics.md#c.raw_atomic64_inc_return_release "raw_atomic64_inc_return_release") there.

**Return**

The updated value of **v**.

s64 atomic64_inc_return_relaxed(atomic64_t \*v)
:   atomic increment with relaxed ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** + 1) with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_inc_return_relaxed()`](basics.md#c.raw_atomic64_inc_return_relaxed "raw_atomic64_inc_return_relaxed") there.

**Return**

The updated value of **v**.

s64 atomic64_fetch_inc(atomic64_t \*v)
:   atomic increment with full ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** + 1) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_fetch_inc()`](basics.md#c.raw_atomic64_fetch_inc "raw_atomic64_fetch_inc") there.

**Return**

The original value of **v**.

s64 atomic64_fetch_inc_acquire(atomic64_t \*v)
:   atomic increment with acquire ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** + 1) with acquire ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_fetch_inc_acquire()`](basics.md#c.raw_atomic64_fetch_inc_acquire "raw_atomic64_fetch_inc_acquire") there.

**Return**

The original value of **v**.

s64 atomic64_fetch_inc_release(atomic64_t \*v)
:   atomic increment with release ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** + 1) with release ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_fetch_inc_release()`](basics.md#c.raw_atomic64_fetch_inc_release "raw_atomic64_fetch_inc_release") there.

**Return**

The original value of **v**.

s64 atomic64_fetch_inc_relaxed(atomic64_t \*v)
:   atomic increment with relaxed ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** + 1) with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_fetch_inc_relaxed()`](basics.md#c.raw_atomic64_fetch_inc_relaxed "raw_atomic64_fetch_inc_relaxed") there.

**Return**

The original value of **v**.

void atomic64_dec(atomic64_t \*v)
:   atomic decrement with relaxed ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** - 1) with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_dec()`](basics.md#c.raw_atomic64_dec "raw_atomic64_dec") there.

**Return**

Nothing.

s64 atomic64_dec_return(atomic64_t \*v)
:   atomic decrement with full ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** - 1) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_dec_return()`](basics.md#c.raw_atomic64_dec_return "raw_atomic64_dec_return") there.

**Return**

The updated value of **v**.

s64 atomic64_dec_return_acquire(atomic64_t \*v)
:   atomic decrement with acquire ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** - 1) with acquire ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_dec_return_acquire()`](basics.md#c.raw_atomic64_dec_return_acquire "raw_atomic64_dec_return_acquire") there.

**Return**

The updated value of **v**.

s64 atomic64_dec_return_release(atomic64_t \*v)
:   atomic decrement with release ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** - 1) with release ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_dec_return_release()`](basics.md#c.raw_atomic64_dec_return_release "raw_atomic64_dec_return_release") there.

**Return**

The updated value of **v**.

s64 atomic64_dec_return_relaxed(atomic64_t \*v)
:   atomic decrement with relaxed ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** - 1) with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_dec_return_relaxed()`](basics.md#c.raw_atomic64_dec_return_relaxed "raw_atomic64_dec_return_relaxed") there.

**Return**

The updated value of **v**.

s64 atomic64_fetch_dec(atomic64_t \*v)
:   atomic decrement with full ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** - 1) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_fetch_dec()`](basics.md#c.raw_atomic64_fetch_dec "raw_atomic64_fetch_dec") there.

**Return**

The original value of **v**.

s64 atomic64_fetch_dec_acquire(atomic64_t \*v)
:   atomic decrement with acquire ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** - 1) with acquire ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_fetch_dec_acquire()`](basics.md#c.raw_atomic64_fetch_dec_acquire "raw_atomic64_fetch_dec_acquire") there.

**Return**

The original value of **v**.

s64 atomic64_fetch_dec_release(atomic64_t \*v)
:   atomic decrement with release ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** - 1) with release ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_fetch_dec_release()`](basics.md#c.raw_atomic64_fetch_dec_release "raw_atomic64_fetch_dec_release") there.

**Return**

The original value of **v**.

s64 atomic64_fetch_dec_relaxed(atomic64_t \*v)
:   atomic decrement with relaxed ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** - 1) with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_fetch_dec_relaxed()`](basics.md#c.raw_atomic64_fetch_dec_relaxed "raw_atomic64_fetch_dec_relaxed") there.

**Return**

The original value of **v**.

void atomic64_and(s64 i, atomic64_t \*v)
:   atomic bitwise AND with relaxed ordering

**Parameters**

`s64 i`
:   s64 value

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** & **i**) with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_and()`](basics.md#c.raw_atomic64_and "raw_atomic64_and") there.

**Return**

Nothing.

s64 atomic64_fetch_and(s64 i, atomic64_t \*v)
:   atomic bitwise AND with full ordering

**Parameters**

`s64 i`
:   s64 value

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** & **i**) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_fetch_and()`](basics.md#c.raw_atomic64_fetch_and "raw_atomic64_fetch_and") there.

**Return**

The original value of **v**.

s64 atomic64_fetch_and_acquire(s64 i, atomic64_t \*v)
:   atomic bitwise AND with acquire ordering

**Parameters**

`s64 i`
:   s64 value

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** & **i**) with acquire ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_fetch_and_acquire()`](basics.md#c.raw_atomic64_fetch_and_acquire "raw_atomic64_fetch_and_acquire") there.

**Return**

The original value of **v**.

s64 atomic64_fetch_and_release(s64 i, atomic64_t \*v)
:   atomic bitwise AND with release ordering

**Parameters**

`s64 i`
:   s64 value

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** & **i**) with release ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_fetch_and_release()`](basics.md#c.raw_atomic64_fetch_and_release "raw_atomic64_fetch_and_release") there.

**Return**

The original value of **v**.

s64 atomic64_fetch_and_relaxed(s64 i, atomic64_t \*v)
:   atomic bitwise AND with relaxed ordering

**Parameters**

`s64 i`
:   s64 value

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** & **i**) with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_fetch_and_relaxed()`](basics.md#c.raw_atomic64_fetch_and_relaxed "raw_atomic64_fetch_and_relaxed") there.

**Return**

The original value of **v**.

void atomic64_andnot(s64 i, atomic64_t \*v)
:   atomic bitwise AND NOT with relaxed ordering

**Parameters**

`s64 i`
:   s64 value

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** & **~i**) with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_andnot()`](basics.md#c.raw_atomic64_andnot "raw_atomic64_andnot") there.

**Return**

Nothing.

s64 atomic64_fetch_andnot(s64 i, atomic64_t \*v)
:   atomic bitwise AND NOT with full ordering

**Parameters**

`s64 i`
:   s64 value

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** & **~i**) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_fetch_andnot()`](basics.md#c.raw_atomic64_fetch_andnot "raw_atomic64_fetch_andnot") there.

**Return**

The original value of **v**.

s64 atomic64_fetch_andnot_acquire(s64 i, atomic64_t \*v)
:   atomic bitwise AND NOT with acquire ordering

**Parameters**

`s64 i`
:   s64 value

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** & **~i**) with acquire ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_fetch_andnot_acquire()`](basics.md#c.raw_atomic64_fetch_andnot_acquire "raw_atomic64_fetch_andnot_acquire") there.

**Return**

The original value of **v**.

s64 atomic64_fetch_andnot_release(s64 i, atomic64_t \*v)
:   atomic bitwise AND NOT with release ordering

**Parameters**

`s64 i`
:   s64 value

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** & **~i**) with release ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_fetch_andnot_release()`](basics.md#c.raw_atomic64_fetch_andnot_release "raw_atomic64_fetch_andnot_release") there.

**Return**

The original value of **v**.

s64 atomic64_fetch_andnot_relaxed(s64 i, atomic64_t \*v)
:   atomic bitwise AND NOT with relaxed ordering

**Parameters**

`s64 i`
:   s64 value

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** & **~i**) with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_fetch_andnot_relaxed()`](basics.md#c.raw_atomic64_fetch_andnot_relaxed "raw_atomic64_fetch_andnot_relaxed") there.

**Return**

The original value of **v**.

void atomic64_or(s64 i, atomic64_t \*v)
:   atomic bitwise OR with relaxed ordering

**Parameters**

`s64 i`
:   s64 value

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** | **i**) with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_or()`](basics.md#c.raw_atomic64_or "raw_atomic64_or") there.

**Return**

Nothing.

s64 atomic64_fetch_or(s64 i, atomic64_t \*v)
:   atomic bitwise OR with full ordering

**Parameters**

`s64 i`
:   s64 value

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** | **i**) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_fetch_or()`](basics.md#c.raw_atomic64_fetch_or "raw_atomic64_fetch_or") there.

**Return**

The original value of **v**.

s64 atomic64_fetch_or_acquire(s64 i, atomic64_t \*v)
:   atomic bitwise OR with acquire ordering

**Parameters**

`s64 i`
:   s64 value

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** | **i**) with acquire ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_fetch_or_acquire()`](basics.md#c.raw_atomic64_fetch_or_acquire "raw_atomic64_fetch_or_acquire") there.

**Return**

The original value of **v**.

s64 atomic64_fetch_or_release(s64 i, atomic64_t \*v)
:   atomic bitwise OR with release ordering

**Parameters**

`s64 i`
:   s64 value

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** | **i**) with release ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_fetch_or_release()`](basics.md#c.raw_atomic64_fetch_or_release "raw_atomic64_fetch_or_release") there.

**Return**

The original value of **v**.

s64 atomic64_fetch_or_relaxed(s64 i, atomic64_t \*v)
:   atomic bitwise OR with relaxed ordering

**Parameters**

`s64 i`
:   s64 value

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** | **i**) with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_fetch_or_relaxed()`](basics.md#c.raw_atomic64_fetch_or_relaxed "raw_atomic64_fetch_or_relaxed") there.

**Return**

The original value of **v**.

void atomic64_xor(s64 i, atomic64_t \*v)
:   atomic bitwise XOR with relaxed ordering

**Parameters**

`s64 i`
:   s64 value

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** ^ **i**) with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_xor()`](basics.md#c.raw_atomic64_xor "raw_atomic64_xor") there.

**Return**

Nothing.

s64 atomic64_fetch_xor(s64 i, atomic64_t \*v)
:   atomic bitwise XOR with full ordering

**Parameters**

`s64 i`
:   s64 value

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** ^ **i**) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_fetch_xor()`](basics.md#c.raw_atomic64_fetch_xor "raw_atomic64_fetch_xor") there.

**Return**

The original value of **v**.

s64 atomic64_fetch_xor_acquire(s64 i, atomic64_t \*v)
:   atomic bitwise XOR with acquire ordering

**Parameters**

`s64 i`
:   s64 value

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** ^ **i**) with acquire ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_fetch_xor_acquire()`](basics.md#c.raw_atomic64_fetch_xor_acquire "raw_atomic64_fetch_xor_acquire") there.

**Return**

The original value of **v**.

s64 atomic64_fetch_xor_release(s64 i, atomic64_t \*v)
:   atomic bitwise XOR with release ordering

**Parameters**

`s64 i`
:   s64 value

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** ^ **i**) with release ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_fetch_xor_release()`](basics.md#c.raw_atomic64_fetch_xor_release "raw_atomic64_fetch_xor_release") there.

**Return**

The original value of **v**.

s64 atomic64_fetch_xor_relaxed(s64 i, atomic64_t \*v)
:   atomic bitwise XOR with relaxed ordering

**Parameters**

`s64 i`
:   s64 value

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** ^ **i**) with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_fetch_xor_relaxed()`](basics.md#c.raw_atomic64_fetch_xor_relaxed "raw_atomic64_fetch_xor_relaxed") there.

**Return**

The original value of **v**.

s64 atomic64_xchg(atomic64_t \*v, s64 new)
:   atomic exchange with full ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

`s64 new`
:   s64 value to assign

**Description**

Atomically updates **v** to **new** with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_xchg()`](basics.md#c.raw_atomic64_xchg "raw_atomic64_xchg") there.

**Return**

The original value of **v**.

s64 atomic64_xchg_acquire(atomic64_t \*v, s64 new)
:   atomic exchange with acquire ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

`s64 new`
:   s64 value to assign

**Description**

Atomically updates **v** to **new** with acquire ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_xchg_acquire()`](basics.md#c.raw_atomic64_xchg_acquire "raw_atomic64_xchg_acquire") there.

**Return**

The original value of **v**.

s64 atomic64_xchg_release(atomic64_t \*v, s64 new)
:   atomic exchange with release ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

`s64 new`
:   s64 value to assign

**Description**

Atomically updates **v** to **new** with release ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_xchg_release()`](basics.md#c.raw_atomic64_xchg_release "raw_atomic64_xchg_release") there.

**Return**

The original value of **v**.

s64 atomic64_xchg_relaxed(atomic64_t \*v, s64 new)
:   atomic exchange with relaxed ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

`s64 new`
:   s64 value to assign

**Description**

Atomically updates **v** to **new** with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_xchg_relaxed()`](basics.md#c.raw_atomic64_xchg_relaxed "raw_atomic64_xchg_relaxed") there.

**Return**

The original value of **v**.

s64 atomic64_cmpxchg(atomic64_t \*v, s64 old, s64 new)
:   atomic compare and exchange with full ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

`s64 old`
:   s64 value to compare with

`s64 new`
:   s64 value to assign

**Description**

If (**v** == **old**), atomically updates **v** to **new** with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_cmpxchg()`](basics.md#c.raw_atomic64_cmpxchg "raw_atomic64_cmpxchg") there.

**Return**

The original value of **v**.

s64 atomic64_cmpxchg_acquire(atomic64_t \*v, s64 old, s64 new)
:   atomic compare and exchange with acquire ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

`s64 old`
:   s64 value to compare with

`s64 new`
:   s64 value to assign

**Description**

If (**v** == **old**), atomically updates **v** to **new** with acquire ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_cmpxchg_acquire()`](basics.md#c.raw_atomic64_cmpxchg_acquire "raw_atomic64_cmpxchg_acquire") there.

**Return**

The original value of **v**.

s64 atomic64_cmpxchg_release(atomic64_t \*v, s64 old, s64 new)
:   atomic compare and exchange with release ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

`s64 old`
:   s64 value to compare with

`s64 new`
:   s64 value to assign

**Description**

If (**v** == **old**), atomically updates **v** to **new** with release ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_cmpxchg_release()`](basics.md#c.raw_atomic64_cmpxchg_release "raw_atomic64_cmpxchg_release") there.

**Return**

The original value of **v**.

s64 atomic64_cmpxchg_relaxed(atomic64_t \*v, s64 old, s64 new)
:   atomic compare and exchange with relaxed ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

`s64 old`
:   s64 value to compare with

`s64 new`
:   s64 value to assign

**Description**

If (**v** == **old**), atomically updates **v** to **new** with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_cmpxchg_relaxed()`](basics.md#c.raw_atomic64_cmpxchg_relaxed "raw_atomic64_cmpxchg_relaxed") there.

**Return**

The original value of **v**.

bool atomic64_try_cmpxchg(atomic64_t \*v, s64 \*old, s64 new)
:   atomic compare and exchange with full ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

`s64 *old`
:   pointer to s64 value to compare with

`s64 new`
:   s64 value to assign

**Description**

If (**v** == **old**), atomically updates **v** to **new** with full ordering.
Otherwise, updates **old** to the current value of **v**.

Unsafe to use in noinstr code; use [`raw_atomic64_try_cmpxchg()`](basics.md#c.raw_atomic64_try_cmpxchg "raw_atomic64_try_cmpxchg") there.

**Return**

**true** if the exchange occured, **false** otherwise.

bool atomic64_try_cmpxchg_acquire(atomic64_t \*v, s64 \*old, s64 new)
:   atomic compare and exchange with acquire ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

`s64 *old`
:   pointer to s64 value to compare with

`s64 new`
:   s64 value to assign

**Description**

If (**v** == **old**), atomically updates **v** to **new** with acquire ordering.
Otherwise, updates **old** to the current value of **v**.

Unsafe to use in noinstr code; use [`raw_atomic64_try_cmpxchg_acquire()`](basics.md#c.raw_atomic64_try_cmpxchg_acquire "raw_atomic64_try_cmpxchg_acquire") there.

**Return**

**true** if the exchange occured, **false** otherwise.

bool atomic64_try_cmpxchg_release(atomic64_t \*v, s64 \*old, s64 new)
:   atomic compare and exchange with release ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

`s64 *old`
:   pointer to s64 value to compare with

`s64 new`
:   s64 value to assign

**Description**

If (**v** == **old**), atomically updates **v** to **new** with release ordering.
Otherwise, updates **old** to the current value of **v**.

Unsafe to use in noinstr code; use [`raw_atomic64_try_cmpxchg_release()`](basics.md#c.raw_atomic64_try_cmpxchg_release "raw_atomic64_try_cmpxchg_release") there.

**Return**

**true** if the exchange occured, **false** otherwise.

bool atomic64_try_cmpxchg_relaxed(atomic64_t \*v, s64 \*old, s64 new)
:   atomic compare and exchange with relaxed ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

`s64 *old`
:   pointer to s64 value to compare with

`s64 new`
:   s64 value to assign

**Description**

If (**v** == **old**), atomically updates **v** to **new** with relaxed ordering.
Otherwise, updates **old** to the current value of **v**.

Unsafe to use in noinstr code; use [`raw_atomic64_try_cmpxchg_relaxed()`](basics.md#c.raw_atomic64_try_cmpxchg_relaxed "raw_atomic64_try_cmpxchg_relaxed") there.

**Return**

**true** if the exchange occured, **false** otherwise.

bool atomic64_sub_and_test(s64 i, atomic64_t \*v)
:   atomic subtract and test if zero with full ordering

**Parameters**

`s64 i`
:   s64 value to add

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** - **i**) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_sub_and_test()`](basics.md#c.raw_atomic64_sub_and_test "raw_atomic64_sub_and_test") there.

**Return**

**true** if the resulting value of **v** is zero, **false** otherwise.

bool atomic64_dec_and_test(atomic64_t \*v)
:   atomic decrement and test if zero with full ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** - 1) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_dec_and_test()`](basics.md#c.raw_atomic64_dec_and_test "raw_atomic64_dec_and_test") there.

**Return**

**true** if the resulting value of **v** is zero, **false** otherwise.

bool atomic64_inc_and_test(atomic64_t \*v)
:   atomic increment and test if zero with full ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** + 1) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_inc_and_test()`](basics.md#c.raw_atomic64_inc_and_test "raw_atomic64_inc_and_test") there.

**Return**

**true** if the resulting value of **v** is zero, **false** otherwise.

bool atomic64_add_negative(s64 i, atomic64_t \*v)
:   atomic add and test if negative with full ordering

**Parameters**

`s64 i`
:   s64 value to add

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** + **i**) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_add_negative()`](basics.md#c.raw_atomic64_add_negative "raw_atomic64_add_negative") there.

**Return**

**true** if the resulting value of **v** is negative, **false** otherwise.

bool atomic64_add_negative_acquire(s64 i, atomic64_t \*v)
:   atomic add and test if negative with acquire ordering

**Parameters**

`s64 i`
:   s64 value to add

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** + **i**) with acquire ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_add_negative_acquire()`](basics.md#c.raw_atomic64_add_negative_acquire "raw_atomic64_add_negative_acquire") there.

**Return**

**true** if the resulting value of **v** is negative, **false** otherwise.

bool atomic64_add_negative_release(s64 i, atomic64_t \*v)
:   atomic add and test if negative with release ordering

**Parameters**

`s64 i`
:   s64 value to add

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** + **i**) with release ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_add_negative_release()`](basics.md#c.raw_atomic64_add_negative_release "raw_atomic64_add_negative_release") there.

**Return**

**true** if the resulting value of **v** is negative, **false** otherwise.

bool atomic64_add_negative_relaxed(s64 i, atomic64_t \*v)
:   atomic add and test if negative with relaxed ordering

**Parameters**

`s64 i`
:   s64 value to add

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** + **i**) with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_add_negative_relaxed()`](basics.md#c.raw_atomic64_add_negative_relaxed "raw_atomic64_add_negative_relaxed") there.

**Return**

**true** if the resulting value of **v** is negative, **false** otherwise.

s64 atomic64_fetch_add_unless(atomic64_t \*v, s64 a, s64 u)
:   atomic add unless value with full ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

`s64 a`
:   s64 value to add

`s64 u`
:   s64 value to compare with

**Description**

If (**v** != **u**), atomically updates **v** to (**v** + **a**) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_fetch_add_unless()`](basics.md#c.raw_atomic64_fetch_add_unless "raw_atomic64_fetch_add_unless") there.

**Return**

The original value of **v**.

bool atomic64_add_unless(atomic64_t \*v, s64 a, s64 u)
:   atomic add unless value with full ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

`s64 a`
:   s64 value to add

`s64 u`
:   s64 value to compare with

**Description**

If (**v** != **u**), atomically updates **v** to (**v** + **a**) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_add_unless()`](basics.md#c.raw_atomic64_add_unless "raw_atomic64_add_unless") there.

**Return**

**true** if **v** was updated, **false** otherwise.

bool atomic64_inc_not_zero(atomic64_t \*v)
:   atomic increment unless zero with full ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

If (**v** != 0), atomically updates **v** to (**v** + 1) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_inc_not_zero()`](basics.md#c.raw_atomic64_inc_not_zero "raw_atomic64_inc_not_zero") there.

**Return**

**true** if **v** was updated, **false** otherwise.

bool atomic64_inc_unless_negative(atomic64_t \*v)
:   atomic increment unless negative with full ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

If (**v** >= 0), atomically updates **v** to (**v** + 1) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_inc_unless_negative()`](basics.md#c.raw_atomic64_inc_unless_negative "raw_atomic64_inc_unless_negative") there.

**Return**

**true** if **v** was updated, **false** otherwise.

bool atomic64_dec_unless_positive(atomic64_t \*v)
:   atomic decrement unless positive with full ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

If (**v** <= 0), atomically updates **v** to (**v** - 1) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_dec_unless_positive()`](basics.md#c.raw_atomic64_dec_unless_positive "raw_atomic64_dec_unless_positive") there.

**Return**

**true** if **v** was updated, **false** otherwise.

s64 atomic64_dec_if_positive(atomic64_t \*v)
:   atomic decrement if positive with full ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

If (**v** > 0), atomically updates **v** to (**v** - 1) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic64_dec_if_positive()`](basics.md#c.raw_atomic64_dec_if_positive "raw_atomic64_dec_if_positive") there.

**Return**

The old value of (**v** - 1), regardless of whether **v** was updated.

long atomic_long_read(const atomic_long_t \*v)
:   atomic load with relaxed ordering

**Parameters**

`const atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically loads the value of **v** with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_read()`](basics.md#c.raw_atomic_long_read "raw_atomic_long_read") there.

**Return**

The value loaded from **v**.

long atomic_long_read_acquire(const atomic_long_t \*v)
:   atomic load with acquire ordering

**Parameters**

`const atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically loads the value of **v** with acquire ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_read_acquire()`](basics.md#c.raw_atomic_long_read_acquire "raw_atomic_long_read_acquire") there.

**Return**

The value loaded from **v**.

void atomic_long_set(atomic_long_t \*v, long i)
:   atomic set with relaxed ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

`long i`
:   long value to assign

**Description**

Atomically sets **v** to **i** with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_set()`](basics.md#c.raw_atomic_long_set "raw_atomic_long_set") there.

**Return**

Nothing.

void atomic_long_set_release(atomic_long_t \*v, long i)
:   atomic set with release ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

`long i`
:   long value to assign

**Description**

Atomically sets **v** to **i** with release ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_set_release()`](basics.md#c.raw_atomic_long_set_release "raw_atomic_long_set_release") there.

**Return**

Nothing.

void atomic_long_add(long i, atomic_long_t \*v)
:   atomic add with relaxed ordering

**Parameters**

`long i`
:   long value to add

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** + **i**) with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_add()`](basics.md#c.raw_atomic_long_add "raw_atomic_long_add") there.

**Return**

Nothing.

long atomic_long_add_return(long i, atomic_long_t \*v)
:   atomic add with full ordering

**Parameters**

`long i`
:   long value to add

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** + **i**) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_add_return()`](basics.md#c.raw_atomic_long_add_return "raw_atomic_long_add_return") there.

**Return**

The updated value of **v**.

long atomic_long_add_return_acquire(long i, atomic_long_t \*v)
:   atomic add with acquire ordering

**Parameters**

`long i`
:   long value to add

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** + **i**) with acquire ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_add_return_acquire()`](basics.md#c.raw_atomic_long_add_return_acquire "raw_atomic_long_add_return_acquire") there.

**Return**

The updated value of **v**.

long atomic_long_add_return_release(long i, atomic_long_t \*v)
:   atomic add with release ordering

**Parameters**

`long i`
:   long value to add

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** + **i**) with release ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_add_return_release()`](basics.md#c.raw_atomic_long_add_return_release "raw_atomic_long_add_return_release") there.

**Return**

The updated value of **v**.

long atomic_long_add_return_relaxed(long i, atomic_long_t \*v)
:   atomic add with relaxed ordering

**Parameters**

`long i`
:   long value to add

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** + **i**) with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_add_return_relaxed()`](basics.md#c.raw_atomic_long_add_return_relaxed "raw_atomic_long_add_return_relaxed") there.

**Return**

The updated value of **v**.

long atomic_long_fetch_add(long i, atomic_long_t \*v)
:   atomic add with full ordering

**Parameters**

`long i`
:   long value to add

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** + **i**) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_fetch_add()`](basics.md#c.raw_atomic_long_fetch_add "raw_atomic_long_fetch_add") there.

**Return**

The original value of **v**.

long atomic_long_fetch_add_acquire(long i, atomic_long_t \*v)
:   atomic add with acquire ordering

**Parameters**

`long i`
:   long value to add

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** + **i**) with acquire ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_fetch_add_acquire()`](basics.md#c.raw_atomic_long_fetch_add_acquire "raw_atomic_long_fetch_add_acquire") there.

**Return**

The original value of **v**.

long atomic_long_fetch_add_release(long i, atomic_long_t \*v)
:   atomic add with release ordering

**Parameters**

`long i`
:   long value to add

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** + **i**) with release ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_fetch_add_release()`](basics.md#c.raw_atomic_long_fetch_add_release "raw_atomic_long_fetch_add_release") there.

**Return**

The original value of **v**.

long atomic_long_fetch_add_relaxed(long i, atomic_long_t \*v)
:   atomic add with relaxed ordering

**Parameters**

`long i`
:   long value to add

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** + **i**) with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_fetch_add_relaxed()`](basics.md#c.raw_atomic_long_fetch_add_relaxed "raw_atomic_long_fetch_add_relaxed") there.

**Return**

The original value of **v**.

void atomic_long_sub(long i, atomic_long_t \*v)
:   atomic subtract with relaxed ordering

**Parameters**

`long i`
:   long value to subtract

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** - **i**) with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_sub()`](basics.md#c.raw_atomic_long_sub "raw_atomic_long_sub") there.

**Return**

Nothing.

long atomic_long_sub_return(long i, atomic_long_t \*v)
:   atomic subtract with full ordering

**Parameters**

`long i`
:   long value to subtract

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** - **i**) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_sub_return()`](basics.md#c.raw_atomic_long_sub_return "raw_atomic_long_sub_return") there.

**Return**

The updated value of **v**.

long atomic_long_sub_return_acquire(long i, atomic_long_t \*v)
:   atomic subtract with acquire ordering

**Parameters**

`long i`
:   long value to subtract

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** - **i**) with acquire ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_sub_return_acquire()`](basics.md#c.raw_atomic_long_sub_return_acquire "raw_atomic_long_sub_return_acquire") there.

**Return**

The updated value of **v**.

long atomic_long_sub_return_release(long i, atomic_long_t \*v)
:   atomic subtract with release ordering

**Parameters**

`long i`
:   long value to subtract

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** - **i**) with release ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_sub_return_release()`](basics.md#c.raw_atomic_long_sub_return_release "raw_atomic_long_sub_return_release") there.

**Return**

The updated value of **v**.

long atomic_long_sub_return_relaxed(long i, atomic_long_t \*v)
:   atomic subtract with relaxed ordering

**Parameters**

`long i`
:   long value to subtract

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** - **i**) with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_sub_return_relaxed()`](basics.md#c.raw_atomic_long_sub_return_relaxed "raw_atomic_long_sub_return_relaxed") there.

**Return**

The updated value of **v**.

long atomic_long_fetch_sub(long i, atomic_long_t \*v)
:   atomic subtract with full ordering

**Parameters**

`long i`
:   long value to subtract

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** - **i**) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_fetch_sub()`](basics.md#c.raw_atomic_long_fetch_sub "raw_atomic_long_fetch_sub") there.

**Return**

The original value of **v**.

long atomic_long_fetch_sub_acquire(long i, atomic_long_t \*v)
:   atomic subtract with acquire ordering

**Parameters**

`long i`
:   long value to subtract

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** - **i**) with acquire ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_fetch_sub_acquire()`](basics.md#c.raw_atomic_long_fetch_sub_acquire "raw_atomic_long_fetch_sub_acquire") there.

**Return**

The original value of **v**.

long atomic_long_fetch_sub_release(long i, atomic_long_t \*v)
:   atomic subtract with release ordering

**Parameters**

`long i`
:   long value to subtract

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** - **i**) with release ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_fetch_sub_release()`](basics.md#c.raw_atomic_long_fetch_sub_release "raw_atomic_long_fetch_sub_release") there.

**Return**

The original value of **v**.

long atomic_long_fetch_sub_relaxed(long i, atomic_long_t \*v)
:   atomic subtract with relaxed ordering

**Parameters**

`long i`
:   long value to subtract

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** - **i**) with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_fetch_sub_relaxed()`](basics.md#c.raw_atomic_long_fetch_sub_relaxed "raw_atomic_long_fetch_sub_relaxed") there.

**Return**

The original value of **v**.

void atomic_long_inc(atomic_long_t \*v)
:   atomic increment with relaxed ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** + 1) with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_inc()`](basics.md#c.raw_atomic_long_inc "raw_atomic_long_inc") there.

**Return**

Nothing.

long atomic_long_inc_return(atomic_long_t \*v)
:   atomic increment with full ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** + 1) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_inc_return()`](basics.md#c.raw_atomic_long_inc_return "raw_atomic_long_inc_return") there.

**Return**

The updated value of **v**.

long atomic_long_inc_return_acquire(atomic_long_t \*v)
:   atomic increment with acquire ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** + 1) with acquire ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_inc_return_acquire()`](basics.md#c.raw_atomic_long_inc_return_acquire "raw_atomic_long_inc_return_acquire") there.

**Return**

The updated value of **v**.

long atomic_long_inc_return_release(atomic_long_t \*v)
:   atomic increment with release ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** + 1) with release ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_inc_return_release()`](basics.md#c.raw_atomic_long_inc_return_release "raw_atomic_long_inc_return_release") there.

**Return**

The updated value of **v**.

long atomic_long_inc_return_relaxed(atomic_long_t \*v)
:   atomic increment with relaxed ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** + 1) with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_inc_return_relaxed()`](basics.md#c.raw_atomic_long_inc_return_relaxed "raw_atomic_long_inc_return_relaxed") there.

**Return**

The updated value of **v**.

long atomic_long_fetch_inc(atomic_long_t \*v)
:   atomic increment with full ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** + 1) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_fetch_inc()`](basics.md#c.raw_atomic_long_fetch_inc "raw_atomic_long_fetch_inc") there.

**Return**

The original value of **v**.

long atomic_long_fetch_inc_acquire(atomic_long_t \*v)
:   atomic increment with acquire ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** + 1) with acquire ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_fetch_inc_acquire()`](basics.md#c.raw_atomic_long_fetch_inc_acquire "raw_atomic_long_fetch_inc_acquire") there.

**Return**

The original value of **v**.

long atomic_long_fetch_inc_release(atomic_long_t \*v)
:   atomic increment with release ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** + 1) with release ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_fetch_inc_release()`](basics.md#c.raw_atomic_long_fetch_inc_release "raw_atomic_long_fetch_inc_release") there.

**Return**

The original value of **v**.

long atomic_long_fetch_inc_relaxed(atomic_long_t \*v)
:   atomic increment with relaxed ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** + 1) with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_fetch_inc_relaxed()`](basics.md#c.raw_atomic_long_fetch_inc_relaxed "raw_atomic_long_fetch_inc_relaxed") there.

**Return**

The original value of **v**.

void atomic_long_dec(atomic_long_t \*v)
:   atomic decrement with relaxed ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** - 1) with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_dec()`](basics.md#c.raw_atomic_long_dec "raw_atomic_long_dec") there.

**Return**

Nothing.

long atomic_long_dec_return(atomic_long_t \*v)
:   atomic decrement with full ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** - 1) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_dec_return()`](basics.md#c.raw_atomic_long_dec_return "raw_atomic_long_dec_return") there.

**Return**

The updated value of **v**.

long atomic_long_dec_return_acquire(atomic_long_t \*v)
:   atomic decrement with acquire ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** - 1) with acquire ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_dec_return_acquire()`](basics.md#c.raw_atomic_long_dec_return_acquire "raw_atomic_long_dec_return_acquire") there.

**Return**

The updated value of **v**.

long atomic_long_dec_return_release(atomic_long_t \*v)
:   atomic decrement with release ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** - 1) with release ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_dec_return_release()`](basics.md#c.raw_atomic_long_dec_return_release "raw_atomic_long_dec_return_release") there.

**Return**

The updated value of **v**.

long atomic_long_dec_return_relaxed(atomic_long_t \*v)
:   atomic decrement with relaxed ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** - 1) with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_dec_return_relaxed()`](basics.md#c.raw_atomic_long_dec_return_relaxed "raw_atomic_long_dec_return_relaxed") there.

**Return**

The updated value of **v**.

long atomic_long_fetch_dec(atomic_long_t \*v)
:   atomic decrement with full ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** - 1) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_fetch_dec()`](basics.md#c.raw_atomic_long_fetch_dec "raw_atomic_long_fetch_dec") there.

**Return**

The original value of **v**.

long atomic_long_fetch_dec_acquire(atomic_long_t \*v)
:   atomic decrement with acquire ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** - 1) with acquire ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_fetch_dec_acquire()`](basics.md#c.raw_atomic_long_fetch_dec_acquire "raw_atomic_long_fetch_dec_acquire") there.

**Return**

The original value of **v**.

long atomic_long_fetch_dec_release(atomic_long_t \*v)
:   atomic decrement with release ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** - 1) with release ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_fetch_dec_release()`](basics.md#c.raw_atomic_long_fetch_dec_release "raw_atomic_long_fetch_dec_release") there.

**Return**

The original value of **v**.

long atomic_long_fetch_dec_relaxed(atomic_long_t \*v)
:   atomic decrement with relaxed ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** - 1) with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_fetch_dec_relaxed()`](basics.md#c.raw_atomic_long_fetch_dec_relaxed "raw_atomic_long_fetch_dec_relaxed") there.

**Return**

The original value of **v**.

void atomic_long_and(long i, atomic_long_t \*v)
:   atomic bitwise AND with relaxed ordering

**Parameters**

`long i`
:   long value

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** & **i**) with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_and()`](basics.md#c.raw_atomic_long_and "raw_atomic_long_and") there.

**Return**

Nothing.

long atomic_long_fetch_and(long i, atomic_long_t \*v)
:   atomic bitwise AND with full ordering

**Parameters**

`long i`
:   long value

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** & **i**) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_fetch_and()`](basics.md#c.raw_atomic_long_fetch_and "raw_atomic_long_fetch_and") there.

**Return**

The original value of **v**.

long atomic_long_fetch_and_acquire(long i, atomic_long_t \*v)
:   atomic bitwise AND with acquire ordering

**Parameters**

`long i`
:   long value

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** & **i**) with acquire ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_fetch_and_acquire()`](basics.md#c.raw_atomic_long_fetch_and_acquire "raw_atomic_long_fetch_and_acquire") there.

**Return**

The original value of **v**.

long atomic_long_fetch_and_release(long i, atomic_long_t \*v)
:   atomic bitwise AND with release ordering

**Parameters**

`long i`
:   long value

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** & **i**) with release ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_fetch_and_release()`](basics.md#c.raw_atomic_long_fetch_and_release "raw_atomic_long_fetch_and_release") there.

**Return**

The original value of **v**.

long atomic_long_fetch_and_relaxed(long i, atomic_long_t \*v)
:   atomic bitwise AND with relaxed ordering

**Parameters**

`long i`
:   long value

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** & **i**) with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_fetch_and_relaxed()`](basics.md#c.raw_atomic_long_fetch_and_relaxed "raw_atomic_long_fetch_and_relaxed") there.

**Return**

The original value of **v**.

void atomic_long_andnot(long i, atomic_long_t \*v)
:   atomic bitwise AND NOT with relaxed ordering

**Parameters**

`long i`
:   long value

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** & **~i**) with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_andnot()`](basics.md#c.raw_atomic_long_andnot "raw_atomic_long_andnot") there.

**Return**

Nothing.

long atomic_long_fetch_andnot(long i, atomic_long_t \*v)
:   atomic bitwise AND NOT with full ordering

**Parameters**

`long i`
:   long value

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** & **~i**) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_fetch_andnot()`](basics.md#c.raw_atomic_long_fetch_andnot "raw_atomic_long_fetch_andnot") there.

**Return**

The original value of **v**.

long atomic_long_fetch_andnot_acquire(long i, atomic_long_t \*v)
:   atomic bitwise AND NOT with acquire ordering

**Parameters**

`long i`
:   long value

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** & **~i**) with acquire ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_fetch_andnot_acquire()`](basics.md#c.raw_atomic_long_fetch_andnot_acquire "raw_atomic_long_fetch_andnot_acquire") there.

**Return**

The original value of **v**.

long atomic_long_fetch_andnot_release(long i, atomic_long_t \*v)
:   atomic bitwise AND NOT with release ordering

**Parameters**

`long i`
:   long value

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** & **~i**) with release ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_fetch_andnot_release()`](basics.md#c.raw_atomic_long_fetch_andnot_release "raw_atomic_long_fetch_andnot_release") there.

**Return**

The original value of **v**.

long atomic_long_fetch_andnot_relaxed(long i, atomic_long_t \*v)
:   atomic bitwise AND NOT with relaxed ordering

**Parameters**

`long i`
:   long value

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** & **~i**) with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_fetch_andnot_relaxed()`](basics.md#c.raw_atomic_long_fetch_andnot_relaxed "raw_atomic_long_fetch_andnot_relaxed") there.

**Return**

The original value of **v**.

void atomic_long_or(long i, atomic_long_t \*v)
:   atomic bitwise OR with relaxed ordering

**Parameters**

`long i`
:   long value

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** | **i**) with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_or()`](basics.md#c.raw_atomic_long_or "raw_atomic_long_or") there.

**Return**

Nothing.

long atomic_long_fetch_or(long i, atomic_long_t \*v)
:   atomic bitwise OR with full ordering

**Parameters**

`long i`
:   long value

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** | **i**) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_fetch_or()`](basics.md#c.raw_atomic_long_fetch_or "raw_atomic_long_fetch_or") there.

**Return**

The original value of **v**.

long atomic_long_fetch_or_acquire(long i, atomic_long_t \*v)
:   atomic bitwise OR with acquire ordering

**Parameters**

`long i`
:   long value

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** | **i**) with acquire ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_fetch_or_acquire()`](basics.md#c.raw_atomic_long_fetch_or_acquire "raw_atomic_long_fetch_or_acquire") there.

**Return**

The original value of **v**.

long atomic_long_fetch_or_release(long i, atomic_long_t \*v)
:   atomic bitwise OR with release ordering

**Parameters**

`long i`
:   long value

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** | **i**) with release ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_fetch_or_release()`](basics.md#c.raw_atomic_long_fetch_or_release "raw_atomic_long_fetch_or_release") there.

**Return**

The original value of **v**.

long atomic_long_fetch_or_relaxed(long i, atomic_long_t \*v)
:   atomic bitwise OR with relaxed ordering

**Parameters**

`long i`
:   long value

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** | **i**) with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_fetch_or_relaxed()`](basics.md#c.raw_atomic_long_fetch_or_relaxed "raw_atomic_long_fetch_or_relaxed") there.

**Return**

The original value of **v**.

void atomic_long_xor(long i, atomic_long_t \*v)
:   atomic bitwise XOR with relaxed ordering

**Parameters**

`long i`
:   long value

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** ^ **i**) with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_xor()`](basics.md#c.raw_atomic_long_xor "raw_atomic_long_xor") there.

**Return**

Nothing.

long atomic_long_fetch_xor(long i, atomic_long_t \*v)
:   atomic bitwise XOR with full ordering

**Parameters**

`long i`
:   long value

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** ^ **i**) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_fetch_xor()`](basics.md#c.raw_atomic_long_fetch_xor "raw_atomic_long_fetch_xor") there.

**Return**

The original value of **v**.

long atomic_long_fetch_xor_acquire(long i, atomic_long_t \*v)
:   atomic bitwise XOR with acquire ordering

**Parameters**

`long i`
:   long value

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** ^ **i**) with acquire ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_fetch_xor_acquire()`](basics.md#c.raw_atomic_long_fetch_xor_acquire "raw_atomic_long_fetch_xor_acquire") there.

**Return**

The original value of **v**.

long atomic_long_fetch_xor_release(long i, atomic_long_t \*v)
:   atomic bitwise XOR with release ordering

**Parameters**

`long i`
:   long value

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** ^ **i**) with release ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_fetch_xor_release()`](basics.md#c.raw_atomic_long_fetch_xor_release "raw_atomic_long_fetch_xor_release") there.

**Return**

The original value of **v**.

long atomic_long_fetch_xor_relaxed(long i, atomic_long_t \*v)
:   atomic bitwise XOR with relaxed ordering

**Parameters**

`long i`
:   long value

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** ^ **i**) with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_fetch_xor_relaxed()`](basics.md#c.raw_atomic_long_fetch_xor_relaxed "raw_atomic_long_fetch_xor_relaxed") there.

**Return**

The original value of **v**.

long atomic_long_xchg(atomic_long_t \*v, long new)
:   atomic exchange with full ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

`long new`
:   long value to assign

**Description**

Atomically updates **v** to **new** with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_xchg()`](basics.md#c.raw_atomic_long_xchg "raw_atomic_long_xchg") there.

**Return**

The original value of **v**.

long atomic_long_xchg_acquire(atomic_long_t \*v, long new)
:   atomic exchange with acquire ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

`long new`
:   long value to assign

**Description**

Atomically updates **v** to **new** with acquire ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_xchg_acquire()`](basics.md#c.raw_atomic_long_xchg_acquire "raw_atomic_long_xchg_acquire") there.

**Return**

The original value of **v**.

long atomic_long_xchg_release(atomic_long_t \*v, long new)
:   atomic exchange with release ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

`long new`
:   long value to assign

**Description**

Atomically updates **v** to **new** with release ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_xchg_release()`](basics.md#c.raw_atomic_long_xchg_release "raw_atomic_long_xchg_release") there.

**Return**

The original value of **v**.

long atomic_long_xchg_relaxed(atomic_long_t \*v, long new)
:   atomic exchange with relaxed ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

`long new`
:   long value to assign

**Description**

Atomically updates **v** to **new** with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_xchg_relaxed()`](basics.md#c.raw_atomic_long_xchg_relaxed "raw_atomic_long_xchg_relaxed") there.

**Return**

The original value of **v**.

long atomic_long_cmpxchg(atomic_long_t \*v, long old, long new)
:   atomic compare and exchange with full ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

`long old`
:   long value to compare with

`long new`
:   long value to assign

**Description**

If (**v** == **old**), atomically updates **v** to **new** with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_cmpxchg()`](basics.md#c.raw_atomic_long_cmpxchg "raw_atomic_long_cmpxchg") there.

**Return**

The original value of **v**.

long atomic_long_cmpxchg_acquire(atomic_long_t \*v, long old, long new)
:   atomic compare and exchange with acquire ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

`long old`
:   long value to compare with

`long new`
:   long value to assign

**Description**

If (**v** == **old**), atomically updates **v** to **new** with acquire ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_cmpxchg_acquire()`](basics.md#c.raw_atomic_long_cmpxchg_acquire "raw_atomic_long_cmpxchg_acquire") there.

**Return**

The original value of **v**.

long atomic_long_cmpxchg_release(atomic_long_t \*v, long old, long new)
:   atomic compare and exchange with release ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

`long old`
:   long value to compare with

`long new`
:   long value to assign

**Description**

If (**v** == **old**), atomically updates **v** to **new** with release ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_cmpxchg_release()`](basics.md#c.raw_atomic_long_cmpxchg_release "raw_atomic_long_cmpxchg_release") there.

**Return**

The original value of **v**.

long atomic_long_cmpxchg_relaxed(atomic_long_t \*v, long old, long new)
:   atomic compare and exchange with relaxed ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

`long old`
:   long value to compare with

`long new`
:   long value to assign

**Description**

If (**v** == **old**), atomically updates **v** to **new** with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_cmpxchg_relaxed()`](basics.md#c.raw_atomic_long_cmpxchg_relaxed "raw_atomic_long_cmpxchg_relaxed") there.

**Return**

The original value of **v**.

bool atomic_long_try_cmpxchg(atomic_long_t \*v, long \*old, long new)
:   atomic compare and exchange with full ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

`long *old`
:   pointer to long value to compare with

`long new`
:   long value to assign

**Description**

If (**v** == **old**), atomically updates **v** to **new** with full ordering.
Otherwise, updates **old** to the current value of **v**.

Unsafe to use in noinstr code; use [`raw_atomic_long_try_cmpxchg()`](basics.md#c.raw_atomic_long_try_cmpxchg "raw_atomic_long_try_cmpxchg") there.

**Return**

**true** if the exchange occured, **false** otherwise.

bool atomic_long_try_cmpxchg_acquire(atomic_long_t \*v, long \*old, long new)
:   atomic compare and exchange with acquire ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

`long *old`
:   pointer to long value to compare with

`long new`
:   long value to assign

**Description**

If (**v** == **old**), atomically updates **v** to **new** with acquire ordering.
Otherwise, updates **old** to the current value of **v**.

Unsafe to use in noinstr code; use [`raw_atomic_long_try_cmpxchg_acquire()`](basics.md#c.raw_atomic_long_try_cmpxchg_acquire "raw_atomic_long_try_cmpxchg_acquire") there.

**Return**

**true** if the exchange occured, **false** otherwise.

bool atomic_long_try_cmpxchg_release(atomic_long_t \*v, long \*old, long new)
:   atomic compare and exchange with release ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

`long *old`
:   pointer to long value to compare with

`long new`
:   long value to assign

**Description**

If (**v** == **old**), atomically updates **v** to **new** with release ordering.
Otherwise, updates **old** to the current value of **v**.

Unsafe to use in noinstr code; use [`raw_atomic_long_try_cmpxchg_release()`](basics.md#c.raw_atomic_long_try_cmpxchg_release "raw_atomic_long_try_cmpxchg_release") there.

**Return**

**true** if the exchange occured, **false** otherwise.

bool atomic_long_try_cmpxchg_relaxed(atomic_long_t \*v, long \*old, long new)
:   atomic compare and exchange with relaxed ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

`long *old`
:   pointer to long value to compare with

`long new`
:   long value to assign

**Description**

If (**v** == **old**), atomically updates **v** to **new** with relaxed ordering.
Otherwise, updates **old** to the current value of **v**.

Unsafe to use in noinstr code; use [`raw_atomic_long_try_cmpxchg_relaxed()`](basics.md#c.raw_atomic_long_try_cmpxchg_relaxed "raw_atomic_long_try_cmpxchg_relaxed") there.

**Return**

**true** if the exchange occured, **false** otherwise.

bool atomic_long_sub_and_test(long i, atomic_long_t \*v)
:   atomic subtract and test if zero with full ordering

**Parameters**

`long i`
:   long value to add

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** - **i**) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_sub_and_test()`](basics.md#c.raw_atomic_long_sub_and_test "raw_atomic_long_sub_and_test") there.

**Return**

**true** if the resulting value of **v** is zero, **false** otherwise.

bool atomic_long_dec_and_test(atomic_long_t \*v)
:   atomic decrement and test if zero with full ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** - 1) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_dec_and_test()`](basics.md#c.raw_atomic_long_dec_and_test "raw_atomic_long_dec_and_test") there.

**Return**

**true** if the resulting value of **v** is zero, **false** otherwise.

bool atomic_long_inc_and_test(atomic_long_t \*v)
:   atomic increment and test if zero with full ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** + 1) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_inc_and_test()`](basics.md#c.raw_atomic_long_inc_and_test "raw_atomic_long_inc_and_test") there.

**Return**

**true** if the resulting value of **v** is zero, **false** otherwise.

bool atomic_long_add_negative(long i, atomic_long_t \*v)
:   atomic add and test if negative with full ordering

**Parameters**

`long i`
:   long value to add

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** + **i**) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_add_negative()`](basics.md#c.raw_atomic_long_add_negative "raw_atomic_long_add_negative") there.

**Return**

**true** if the resulting value of **v** is negative, **false** otherwise.

bool atomic_long_add_negative_acquire(long i, atomic_long_t \*v)
:   atomic add and test if negative with acquire ordering

**Parameters**

`long i`
:   long value to add

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** + **i**) with acquire ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_add_negative_acquire()`](basics.md#c.raw_atomic_long_add_negative_acquire "raw_atomic_long_add_negative_acquire") there.

**Return**

**true** if the resulting value of **v** is negative, **false** otherwise.

bool atomic_long_add_negative_release(long i, atomic_long_t \*v)
:   atomic add and test if negative with release ordering

**Parameters**

`long i`
:   long value to add

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** + **i**) with release ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_add_negative_release()`](basics.md#c.raw_atomic_long_add_negative_release "raw_atomic_long_add_negative_release") there.

**Return**

**true** if the resulting value of **v** is negative, **false** otherwise.

bool atomic_long_add_negative_relaxed(long i, atomic_long_t \*v)
:   atomic add and test if negative with relaxed ordering

**Parameters**

`long i`
:   long value to add

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** + **i**) with relaxed ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_add_negative_relaxed()`](basics.md#c.raw_atomic_long_add_negative_relaxed "raw_atomic_long_add_negative_relaxed") there.

**Return**

**true** if the resulting value of **v** is negative, **false** otherwise.

long atomic_long_fetch_add_unless(atomic_long_t \*v, long a, long u)
:   atomic add unless value with full ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

`long a`
:   long value to add

`long u`
:   long value to compare with

**Description**

If (**v** != **u**), atomically updates **v** to (**v** + **a**) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_fetch_add_unless()`](basics.md#c.raw_atomic_long_fetch_add_unless "raw_atomic_long_fetch_add_unless") there.

**Return**

The original value of **v**.

bool atomic_long_add_unless(atomic_long_t \*v, long a, long u)
:   atomic add unless value with full ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

`long a`
:   long value to add

`long u`
:   long value to compare with

**Description**

If (**v** != **u**), atomically updates **v** to (**v** + **a**) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_add_unless()`](basics.md#c.raw_atomic_long_add_unless "raw_atomic_long_add_unless") there.

**Return**

**true** if **v** was updated, **false** otherwise.

bool atomic_long_inc_not_zero(atomic_long_t \*v)
:   atomic increment unless zero with full ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

If (**v** != 0), atomically updates **v** to (**v** + 1) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_inc_not_zero()`](basics.md#c.raw_atomic_long_inc_not_zero "raw_atomic_long_inc_not_zero") there.

**Return**

**true** if **v** was updated, **false** otherwise.

bool atomic_long_inc_unless_negative(atomic_long_t \*v)
:   atomic increment unless negative with full ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

If (**v** >= 0), atomically updates **v** to (**v** + 1) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_inc_unless_negative()`](basics.md#c.raw_atomic_long_inc_unless_negative "raw_atomic_long_inc_unless_negative") there.

**Return**

**true** if **v** was updated, **false** otherwise.

bool atomic_long_dec_unless_positive(atomic_long_t \*v)
:   atomic decrement unless positive with full ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

If (**v** <= 0), atomically updates **v** to (**v** - 1) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_dec_unless_positive()`](basics.md#c.raw_atomic_long_dec_unless_positive "raw_atomic_long_dec_unless_positive") there.

**Return**

**true** if **v** was updated, **false** otherwise.

long atomic_long_dec_if_positive(atomic_long_t \*v)
:   atomic decrement if positive with full ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

If (**v** > 0), atomically updates **v** to (**v** - 1) with full ordering.

Unsafe to use in noinstr code; use [`raw_atomic_long_dec_if_positive()`](basics.md#c.raw_atomic_long_dec_if_positive "raw_atomic_long_dec_if_positive") there.

**Return**

The old value of (**v** - 1), regardless of whether **v** was updated.

int raw_atomic_read(const atomic_t \*v)
:   atomic load with relaxed ordering

**Parameters**

`const atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically loads the value of **v** with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic_read()`](basics.md#c.atomic_read "atomic_read") elsewhere.

**Return**

The value loaded from **v**.

int raw_atomic_read_acquire(const atomic_t \*v)
:   atomic load with acquire ordering

**Parameters**

`const atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically loads the value of **v** with acquire ordering.

Safe to use in noinstr code; prefer [`atomic_read_acquire()`](basics.md#c.atomic_read_acquire "atomic_read_acquire") elsewhere.

**Return**

The value loaded from **v**.

void raw_atomic_set(atomic_t \*v, int i)
:   atomic set with relaxed ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

`int i`
:   int value to assign

**Description**

Atomically sets **v** to **i** with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic_set()`](basics.md#c.atomic_set "atomic_set") elsewhere.

**Return**

Nothing.

void raw_atomic_set_release(atomic_t \*v, int i)
:   atomic set with release ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

`int i`
:   int value to assign

**Description**

Atomically sets **v** to **i** with release ordering.

Safe to use in noinstr code; prefer [`atomic_set_release()`](basics.md#c.atomic_set_release "atomic_set_release") elsewhere.

**Return**

Nothing.

void raw_atomic_add(int i, atomic_t \*v)
:   atomic add with relaxed ordering

**Parameters**

`int i`
:   int value to add

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** + **i**) with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic_add()`](basics.md#c.atomic_add "atomic_add") elsewhere.

**Return**

Nothing.

int raw_atomic_add_return(int i, atomic_t \*v)
:   atomic add with full ordering

**Parameters**

`int i`
:   int value to add

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** + **i**) with full ordering.

Safe to use in noinstr code; prefer [`atomic_add_return()`](basics.md#c.atomic_add_return "atomic_add_return") elsewhere.

**Return**

The updated value of **v**.

int raw_atomic_add_return_acquire(int i, atomic_t \*v)
:   atomic add with acquire ordering

**Parameters**

`int i`
:   int value to add

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** + **i**) with acquire ordering.

Safe to use in noinstr code; prefer [`atomic_add_return_acquire()`](basics.md#c.atomic_add_return_acquire "atomic_add_return_acquire") elsewhere.

**Return**

The updated value of **v**.

int raw_atomic_add_return_release(int i, atomic_t \*v)
:   atomic add with release ordering

**Parameters**

`int i`
:   int value to add

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** + **i**) with release ordering.

Safe to use in noinstr code; prefer [`atomic_add_return_release()`](basics.md#c.atomic_add_return_release "atomic_add_return_release") elsewhere.

**Return**

The updated value of **v**.

int raw_atomic_add_return_relaxed(int i, atomic_t \*v)
:   atomic add with relaxed ordering

**Parameters**

`int i`
:   int value to add

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** + **i**) with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic_add_return_relaxed()`](basics.md#c.atomic_add_return_relaxed "atomic_add_return_relaxed") elsewhere.

**Return**

The updated value of **v**.

int raw_atomic_fetch_add(int i, atomic_t \*v)
:   atomic add with full ordering

**Parameters**

`int i`
:   int value to add

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** + **i**) with full ordering.

Safe to use in noinstr code; prefer [`atomic_fetch_add()`](basics.md#c.atomic_fetch_add "atomic_fetch_add") elsewhere.

**Return**

The original value of **v**.

int raw_atomic_fetch_add_acquire(int i, atomic_t \*v)
:   atomic add with acquire ordering

**Parameters**

`int i`
:   int value to add

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** + **i**) with acquire ordering.

Safe to use in noinstr code; prefer [`atomic_fetch_add_acquire()`](basics.md#c.atomic_fetch_add_acquire "atomic_fetch_add_acquire") elsewhere.

**Return**

The original value of **v**.

int raw_atomic_fetch_add_release(int i, atomic_t \*v)
:   atomic add with release ordering

**Parameters**

`int i`
:   int value to add

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** + **i**) with release ordering.

Safe to use in noinstr code; prefer [`atomic_fetch_add_release()`](basics.md#c.atomic_fetch_add_release "atomic_fetch_add_release") elsewhere.

**Return**

The original value of **v**.

int raw_atomic_fetch_add_relaxed(int i, atomic_t \*v)
:   atomic add with relaxed ordering

**Parameters**

`int i`
:   int value to add

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** + **i**) with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic_fetch_add_relaxed()`](basics.md#c.atomic_fetch_add_relaxed "atomic_fetch_add_relaxed") elsewhere.

**Return**

The original value of **v**.

void raw_atomic_sub(int i, atomic_t \*v)
:   atomic subtract with relaxed ordering

**Parameters**

`int i`
:   int value to subtract

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** - **i**) with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic_sub()`](basics.md#c.atomic_sub "atomic_sub") elsewhere.

**Return**

Nothing.

int raw_atomic_sub_return(int i, atomic_t \*v)
:   atomic subtract with full ordering

**Parameters**

`int i`
:   int value to subtract

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** - **i**) with full ordering.

Safe to use in noinstr code; prefer [`atomic_sub_return()`](basics.md#c.atomic_sub_return "atomic_sub_return") elsewhere.

**Return**

The updated value of **v**.

int raw_atomic_sub_return_acquire(int i, atomic_t \*v)
:   atomic subtract with acquire ordering

**Parameters**

`int i`
:   int value to subtract

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** - **i**) with acquire ordering.

Safe to use in noinstr code; prefer [`atomic_sub_return_acquire()`](basics.md#c.atomic_sub_return_acquire "atomic_sub_return_acquire") elsewhere.

**Return**

The updated value of **v**.

int raw_atomic_sub_return_release(int i, atomic_t \*v)
:   atomic subtract with release ordering

**Parameters**

`int i`
:   int value to subtract

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** - **i**) with release ordering.

Safe to use in noinstr code; prefer [`atomic_sub_return_release()`](basics.md#c.atomic_sub_return_release "atomic_sub_return_release") elsewhere.

**Return**

The updated value of **v**.

int raw_atomic_sub_return_relaxed(int i, atomic_t \*v)
:   atomic subtract with relaxed ordering

**Parameters**

`int i`
:   int value to subtract

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** - **i**) with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic_sub_return_relaxed()`](basics.md#c.atomic_sub_return_relaxed "atomic_sub_return_relaxed") elsewhere.

**Return**

The updated value of **v**.

int raw_atomic_fetch_sub(int i, atomic_t \*v)
:   atomic subtract with full ordering

**Parameters**

`int i`
:   int value to subtract

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** - **i**) with full ordering.

Safe to use in noinstr code; prefer [`atomic_fetch_sub()`](basics.md#c.atomic_fetch_sub "atomic_fetch_sub") elsewhere.

**Return**

The original value of **v**.

int raw_atomic_fetch_sub_acquire(int i, atomic_t \*v)
:   atomic subtract with acquire ordering

**Parameters**

`int i`
:   int value to subtract

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** - **i**) with acquire ordering.

Safe to use in noinstr code; prefer [`atomic_fetch_sub_acquire()`](basics.md#c.atomic_fetch_sub_acquire "atomic_fetch_sub_acquire") elsewhere.

**Return**

The original value of **v**.

int raw_atomic_fetch_sub_release(int i, atomic_t \*v)
:   atomic subtract with release ordering

**Parameters**

`int i`
:   int value to subtract

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** - **i**) with release ordering.

Safe to use in noinstr code; prefer [`atomic_fetch_sub_release()`](basics.md#c.atomic_fetch_sub_release "atomic_fetch_sub_release") elsewhere.

**Return**

The original value of **v**.

int raw_atomic_fetch_sub_relaxed(int i, atomic_t \*v)
:   atomic subtract with relaxed ordering

**Parameters**

`int i`
:   int value to subtract

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** - **i**) with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic_fetch_sub_relaxed()`](basics.md#c.atomic_fetch_sub_relaxed "atomic_fetch_sub_relaxed") elsewhere.

**Return**

The original value of **v**.

void raw_atomic_inc(atomic_t \*v)
:   atomic increment with relaxed ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** + 1) with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic_inc()`](basics.md#c.atomic_inc "atomic_inc") elsewhere.

**Return**

Nothing.

int raw_atomic_inc_return(atomic_t \*v)
:   atomic increment with full ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** + 1) with full ordering.

Safe to use in noinstr code; prefer [`atomic_inc_return()`](basics.md#c.atomic_inc_return "atomic_inc_return") elsewhere.

**Return**

The updated value of **v**.

int raw_atomic_inc_return_acquire(atomic_t \*v)
:   atomic increment with acquire ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** + 1) with acquire ordering.

Safe to use in noinstr code; prefer [`atomic_inc_return_acquire()`](basics.md#c.atomic_inc_return_acquire "atomic_inc_return_acquire") elsewhere.

**Return**

The updated value of **v**.

int raw_atomic_inc_return_release(atomic_t \*v)
:   atomic increment with release ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** + 1) with release ordering.

Safe to use in noinstr code; prefer [`atomic_inc_return_release()`](basics.md#c.atomic_inc_return_release "atomic_inc_return_release") elsewhere.

**Return**

The updated value of **v**.

int raw_atomic_inc_return_relaxed(atomic_t \*v)
:   atomic increment with relaxed ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** + 1) with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic_inc_return_relaxed()`](basics.md#c.atomic_inc_return_relaxed "atomic_inc_return_relaxed") elsewhere.

**Return**

The updated value of **v**.

int raw_atomic_fetch_inc(atomic_t \*v)
:   atomic increment with full ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** + 1) with full ordering.

Safe to use in noinstr code; prefer [`atomic_fetch_inc()`](basics.md#c.atomic_fetch_inc "atomic_fetch_inc") elsewhere.

**Return**

The original value of **v**.

int raw_atomic_fetch_inc_acquire(atomic_t \*v)
:   atomic increment with acquire ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** + 1) with acquire ordering.

Safe to use in noinstr code; prefer [`atomic_fetch_inc_acquire()`](basics.md#c.atomic_fetch_inc_acquire "atomic_fetch_inc_acquire") elsewhere.

**Return**

The original value of **v**.

int raw_atomic_fetch_inc_release(atomic_t \*v)
:   atomic increment with release ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** + 1) with release ordering.

Safe to use in noinstr code; prefer [`atomic_fetch_inc_release()`](basics.md#c.atomic_fetch_inc_release "atomic_fetch_inc_release") elsewhere.

**Return**

The original value of **v**.

int raw_atomic_fetch_inc_relaxed(atomic_t \*v)
:   atomic increment with relaxed ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** + 1) with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic_fetch_inc_relaxed()`](basics.md#c.atomic_fetch_inc_relaxed "atomic_fetch_inc_relaxed") elsewhere.

**Return**

The original value of **v**.

void raw_atomic_dec(atomic_t \*v)
:   atomic decrement with relaxed ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** - 1) with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic_dec()`](basics.md#c.atomic_dec "atomic_dec") elsewhere.

**Return**

Nothing.

int raw_atomic_dec_return(atomic_t \*v)
:   atomic decrement with full ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** - 1) with full ordering.

Safe to use in noinstr code; prefer [`atomic_dec_return()`](basics.md#c.atomic_dec_return "atomic_dec_return") elsewhere.

**Return**

The updated value of **v**.

int raw_atomic_dec_return_acquire(atomic_t \*v)
:   atomic decrement with acquire ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** - 1) with acquire ordering.

Safe to use in noinstr code; prefer [`atomic_dec_return_acquire()`](basics.md#c.atomic_dec_return_acquire "atomic_dec_return_acquire") elsewhere.

**Return**

The updated value of **v**.

int raw_atomic_dec_return_release(atomic_t \*v)
:   atomic decrement with release ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** - 1) with release ordering.

Safe to use in noinstr code; prefer [`atomic_dec_return_release()`](basics.md#c.atomic_dec_return_release "atomic_dec_return_release") elsewhere.

**Return**

The updated value of **v**.

int raw_atomic_dec_return_relaxed(atomic_t \*v)
:   atomic decrement with relaxed ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** - 1) with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic_dec_return_relaxed()`](basics.md#c.atomic_dec_return_relaxed "atomic_dec_return_relaxed") elsewhere.

**Return**

The updated value of **v**.

int raw_atomic_fetch_dec(atomic_t \*v)
:   atomic decrement with full ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** - 1) with full ordering.

Safe to use in noinstr code; prefer [`atomic_fetch_dec()`](basics.md#c.atomic_fetch_dec "atomic_fetch_dec") elsewhere.

**Return**

The original value of **v**.

int raw_atomic_fetch_dec_acquire(atomic_t \*v)
:   atomic decrement with acquire ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** - 1) with acquire ordering.

Safe to use in noinstr code; prefer [`atomic_fetch_dec_acquire()`](basics.md#c.atomic_fetch_dec_acquire "atomic_fetch_dec_acquire") elsewhere.

**Return**

The original value of **v**.

int raw_atomic_fetch_dec_release(atomic_t \*v)
:   atomic decrement with release ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** - 1) with release ordering.

Safe to use in noinstr code; prefer [`atomic_fetch_dec_release()`](basics.md#c.atomic_fetch_dec_release "atomic_fetch_dec_release") elsewhere.

**Return**

The original value of **v**.

int raw_atomic_fetch_dec_relaxed(atomic_t \*v)
:   atomic decrement with relaxed ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** - 1) with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic_fetch_dec_relaxed()`](basics.md#c.atomic_fetch_dec_relaxed "atomic_fetch_dec_relaxed") elsewhere.

**Return**

The original value of **v**.

void raw_atomic_and(int i, atomic_t \*v)
:   atomic bitwise AND with relaxed ordering

**Parameters**

`int i`
:   int value

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** & **i**) with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic_and()`](basics.md#c.atomic_and "atomic_and") elsewhere.

**Return**

Nothing.

int raw_atomic_fetch_and(int i, atomic_t \*v)
:   atomic bitwise AND with full ordering

**Parameters**

`int i`
:   int value

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** & **i**) with full ordering.

Safe to use in noinstr code; prefer [`atomic_fetch_and()`](basics.md#c.atomic_fetch_and "atomic_fetch_and") elsewhere.

**Return**

The original value of **v**.

int raw_atomic_fetch_and_acquire(int i, atomic_t \*v)
:   atomic bitwise AND with acquire ordering

**Parameters**

`int i`
:   int value

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** & **i**) with acquire ordering.

Safe to use in noinstr code; prefer [`atomic_fetch_and_acquire()`](basics.md#c.atomic_fetch_and_acquire "atomic_fetch_and_acquire") elsewhere.

**Return**

The original value of **v**.

int raw_atomic_fetch_and_release(int i, atomic_t \*v)
:   atomic bitwise AND with release ordering

**Parameters**

`int i`
:   int value

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** & **i**) with release ordering.

Safe to use in noinstr code; prefer [`atomic_fetch_and_release()`](basics.md#c.atomic_fetch_and_release "atomic_fetch_and_release") elsewhere.

**Return**

The original value of **v**.

int raw_atomic_fetch_and_relaxed(int i, atomic_t \*v)
:   atomic bitwise AND with relaxed ordering

**Parameters**

`int i`
:   int value

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** & **i**) with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic_fetch_and_relaxed()`](basics.md#c.atomic_fetch_and_relaxed "atomic_fetch_and_relaxed") elsewhere.

**Return**

The original value of **v**.

void raw_atomic_andnot(int i, atomic_t \*v)
:   atomic bitwise AND NOT with relaxed ordering

**Parameters**

`int i`
:   int value

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** & **~i**) with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic_andnot()`](basics.md#c.atomic_andnot "atomic_andnot") elsewhere.

**Return**

Nothing.

int raw_atomic_fetch_andnot(int i, atomic_t \*v)
:   atomic bitwise AND NOT with full ordering

**Parameters**

`int i`
:   int value

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** & **~i**) with full ordering.

Safe to use in noinstr code; prefer [`atomic_fetch_andnot()`](basics.md#c.atomic_fetch_andnot "atomic_fetch_andnot") elsewhere.

**Return**

The original value of **v**.

int raw_atomic_fetch_andnot_acquire(int i, atomic_t \*v)
:   atomic bitwise AND NOT with acquire ordering

**Parameters**

`int i`
:   int value

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** & **~i**) with acquire ordering.

Safe to use in noinstr code; prefer [`atomic_fetch_andnot_acquire()`](basics.md#c.atomic_fetch_andnot_acquire "atomic_fetch_andnot_acquire") elsewhere.

**Return**

The original value of **v**.

int raw_atomic_fetch_andnot_release(int i, atomic_t \*v)
:   atomic bitwise AND NOT with release ordering

**Parameters**

`int i`
:   int value

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** & **~i**) with release ordering.

Safe to use in noinstr code; prefer [`atomic_fetch_andnot_release()`](basics.md#c.atomic_fetch_andnot_release "atomic_fetch_andnot_release") elsewhere.

**Return**

The original value of **v**.

int raw_atomic_fetch_andnot_relaxed(int i, atomic_t \*v)
:   atomic bitwise AND NOT with relaxed ordering

**Parameters**

`int i`
:   int value

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** & **~i**) with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic_fetch_andnot_relaxed()`](basics.md#c.atomic_fetch_andnot_relaxed "atomic_fetch_andnot_relaxed") elsewhere.

**Return**

The original value of **v**.

void raw_atomic_or(int i, atomic_t \*v)
:   atomic bitwise OR with relaxed ordering

**Parameters**

`int i`
:   int value

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** | **i**) with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic_or()`](basics.md#c.atomic_or "atomic_or") elsewhere.

**Return**

Nothing.

int raw_atomic_fetch_or(int i, atomic_t \*v)
:   atomic bitwise OR with full ordering

**Parameters**

`int i`
:   int value

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** | **i**) with full ordering.

Safe to use in noinstr code; prefer [`atomic_fetch_or()`](basics.md#c.atomic_fetch_or "atomic_fetch_or") elsewhere.

**Return**

The original value of **v**.

int raw_atomic_fetch_or_acquire(int i, atomic_t \*v)
:   atomic bitwise OR with acquire ordering

**Parameters**

`int i`
:   int value

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** | **i**) with acquire ordering.

Safe to use in noinstr code; prefer [`atomic_fetch_or_acquire()`](basics.md#c.atomic_fetch_or_acquire "atomic_fetch_or_acquire") elsewhere.

**Return**

The original value of **v**.

int raw_atomic_fetch_or_release(int i, atomic_t \*v)
:   atomic bitwise OR with release ordering

**Parameters**

`int i`
:   int value

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** | **i**) with release ordering.

Safe to use in noinstr code; prefer [`atomic_fetch_or_release()`](basics.md#c.atomic_fetch_or_release "atomic_fetch_or_release") elsewhere.

**Return**

The original value of **v**.

int raw_atomic_fetch_or_relaxed(int i, atomic_t \*v)
:   atomic bitwise OR with relaxed ordering

**Parameters**

`int i`
:   int value

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** | **i**) with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic_fetch_or_relaxed()`](basics.md#c.atomic_fetch_or_relaxed "atomic_fetch_or_relaxed") elsewhere.

**Return**

The original value of **v**.

void raw_atomic_xor(int i, atomic_t \*v)
:   atomic bitwise XOR with relaxed ordering

**Parameters**

`int i`
:   int value

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** ^ **i**) with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic_xor()`](basics.md#c.atomic_xor "atomic_xor") elsewhere.

**Return**

Nothing.

int raw_atomic_fetch_xor(int i, atomic_t \*v)
:   atomic bitwise XOR with full ordering

**Parameters**

`int i`
:   int value

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** ^ **i**) with full ordering.

Safe to use in noinstr code; prefer [`atomic_fetch_xor()`](basics.md#c.atomic_fetch_xor "atomic_fetch_xor") elsewhere.

**Return**

The original value of **v**.

int raw_atomic_fetch_xor_acquire(int i, atomic_t \*v)
:   atomic bitwise XOR with acquire ordering

**Parameters**

`int i`
:   int value

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** ^ **i**) with acquire ordering.

Safe to use in noinstr code; prefer [`atomic_fetch_xor_acquire()`](basics.md#c.atomic_fetch_xor_acquire "atomic_fetch_xor_acquire") elsewhere.

**Return**

The original value of **v**.

int raw_atomic_fetch_xor_release(int i, atomic_t \*v)
:   atomic bitwise XOR with release ordering

**Parameters**

`int i`
:   int value

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** ^ **i**) with release ordering.

Safe to use in noinstr code; prefer [`atomic_fetch_xor_release()`](basics.md#c.atomic_fetch_xor_release "atomic_fetch_xor_release") elsewhere.

**Return**

The original value of **v**.

int raw_atomic_fetch_xor_relaxed(int i, atomic_t \*v)
:   atomic bitwise XOR with relaxed ordering

**Parameters**

`int i`
:   int value

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** ^ **i**) with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic_fetch_xor_relaxed()`](basics.md#c.atomic_fetch_xor_relaxed "atomic_fetch_xor_relaxed") elsewhere.

**Return**

The original value of **v**.

int raw_atomic_xchg(atomic_t \*v, int new)
:   atomic exchange with full ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

`int new`
:   int value to assign

**Description**

Atomically updates **v** to **new** with full ordering.

Safe to use in noinstr code; prefer [`atomic_xchg()`](basics.md#c.atomic_xchg "atomic_xchg") elsewhere.

**Return**

The original value of **v**.

int raw_atomic_xchg_acquire(atomic_t \*v, int new)
:   atomic exchange with acquire ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

`int new`
:   int value to assign

**Description**

Atomically updates **v** to **new** with acquire ordering.

Safe to use in noinstr code; prefer [`atomic_xchg_acquire()`](basics.md#c.atomic_xchg_acquire "atomic_xchg_acquire") elsewhere.

**Return**

The original value of **v**.

int raw_atomic_xchg_release(atomic_t \*v, int new)
:   atomic exchange with release ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

`int new`
:   int value to assign

**Description**

Atomically updates **v** to **new** with release ordering.

Safe to use in noinstr code; prefer [`atomic_xchg_release()`](basics.md#c.atomic_xchg_release "atomic_xchg_release") elsewhere.

**Return**

The original value of **v**.

int raw_atomic_xchg_relaxed(atomic_t \*v, int new)
:   atomic exchange with relaxed ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

`int new`
:   int value to assign

**Description**

Atomically updates **v** to **new** with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic_xchg_relaxed()`](basics.md#c.atomic_xchg_relaxed "atomic_xchg_relaxed") elsewhere.

**Return**

The original value of **v**.

int raw_atomic_cmpxchg(atomic_t \*v, int old, int new)
:   atomic compare and exchange with full ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

`int old`
:   int value to compare with

`int new`
:   int value to assign

**Description**

If (**v** == **old**), atomically updates **v** to **new** with full ordering.

Safe to use in noinstr code; prefer [`atomic_cmpxchg()`](basics.md#c.atomic_cmpxchg "atomic_cmpxchg") elsewhere.

**Return**

The original value of **v**.

int raw_atomic_cmpxchg_acquire(atomic_t \*v, int old, int new)
:   atomic compare and exchange with acquire ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

`int old`
:   int value to compare with

`int new`
:   int value to assign

**Description**

If (**v** == **old**), atomically updates **v** to **new** with acquire ordering.

Safe to use in noinstr code; prefer [`atomic_cmpxchg_acquire()`](basics.md#c.atomic_cmpxchg_acquire "atomic_cmpxchg_acquire") elsewhere.

**Return**

The original value of **v**.

int raw_atomic_cmpxchg_release(atomic_t \*v, int old, int new)
:   atomic compare and exchange with release ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

`int old`
:   int value to compare with

`int new`
:   int value to assign

**Description**

If (**v** == **old**), atomically updates **v** to **new** with release ordering.

Safe to use in noinstr code; prefer [`atomic_cmpxchg_release()`](basics.md#c.atomic_cmpxchg_release "atomic_cmpxchg_release") elsewhere.

**Return**

The original value of **v**.

int raw_atomic_cmpxchg_relaxed(atomic_t \*v, int old, int new)
:   atomic compare and exchange with relaxed ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

`int old`
:   int value to compare with

`int new`
:   int value to assign

**Description**

If (**v** == **old**), atomically updates **v** to **new** with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic_cmpxchg_relaxed()`](basics.md#c.atomic_cmpxchg_relaxed "atomic_cmpxchg_relaxed") elsewhere.

**Return**

The original value of **v**.

bool raw_atomic_try_cmpxchg(atomic_t \*v, int \*old, int new)
:   atomic compare and exchange with full ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

`int *old`
:   pointer to int value to compare with

`int new`
:   int value to assign

**Description**

If (**v** == **old**), atomically updates **v** to **new** with full ordering.
Otherwise, updates **old** to the current value of **v**.

Safe to use in noinstr code; prefer [`atomic_try_cmpxchg()`](basics.md#c.atomic_try_cmpxchg "atomic_try_cmpxchg") elsewhere.

**Return**

**true** if the exchange occured, **false** otherwise.

bool raw_atomic_try_cmpxchg_acquire(atomic_t \*v, int \*old, int new)
:   atomic compare and exchange with acquire ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

`int *old`
:   pointer to int value to compare with

`int new`
:   int value to assign

**Description**

If (**v** == **old**), atomically updates **v** to **new** with acquire ordering.
Otherwise, updates **old** to the current value of **v**.

Safe to use in noinstr code; prefer [`atomic_try_cmpxchg_acquire()`](basics.md#c.atomic_try_cmpxchg_acquire "atomic_try_cmpxchg_acquire") elsewhere.

**Return**

**true** if the exchange occured, **false** otherwise.

bool raw_atomic_try_cmpxchg_release(atomic_t \*v, int \*old, int new)
:   atomic compare and exchange with release ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

`int *old`
:   pointer to int value to compare with

`int new`
:   int value to assign

**Description**

If (**v** == **old**), atomically updates **v** to **new** with release ordering.
Otherwise, updates **old** to the current value of **v**.

Safe to use in noinstr code; prefer [`atomic_try_cmpxchg_release()`](basics.md#c.atomic_try_cmpxchg_release "atomic_try_cmpxchg_release") elsewhere.

**Return**

**true** if the exchange occured, **false** otherwise.

bool raw_atomic_try_cmpxchg_relaxed(atomic_t \*v, int \*old, int new)
:   atomic compare and exchange with relaxed ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

`int *old`
:   pointer to int value to compare with

`int new`
:   int value to assign

**Description**

If (**v** == **old**), atomically updates **v** to **new** with relaxed ordering.
Otherwise, updates **old** to the current value of **v**.

Safe to use in noinstr code; prefer [`atomic_try_cmpxchg_relaxed()`](basics.md#c.atomic_try_cmpxchg_relaxed "atomic_try_cmpxchg_relaxed") elsewhere.

**Return**

**true** if the exchange occured, **false** otherwise.

bool raw_atomic_sub_and_test(int i, atomic_t \*v)
:   atomic subtract and test if zero with full ordering

**Parameters**

`int i`
:   int value to add

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** - **i**) with full ordering.

Safe to use in noinstr code; prefer [`atomic_sub_and_test()`](basics.md#c.atomic_sub_and_test "atomic_sub_and_test") elsewhere.

**Return**

**true** if the resulting value of **v** is zero, **false** otherwise.

bool raw_atomic_dec_and_test(atomic_t \*v)
:   atomic decrement and test if zero with full ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** - 1) with full ordering.

Safe to use in noinstr code; prefer [`atomic_dec_and_test()`](basics.md#c.atomic_dec_and_test "atomic_dec_and_test") elsewhere.

**Return**

**true** if the resulting value of **v** is zero, **false** otherwise.

bool raw_atomic_inc_and_test(atomic_t \*v)
:   atomic increment and test if zero with full ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** + 1) with full ordering.

Safe to use in noinstr code; prefer [`atomic_inc_and_test()`](basics.md#c.atomic_inc_and_test "atomic_inc_and_test") elsewhere.

**Return**

**true** if the resulting value of **v** is zero, **false** otherwise.

bool raw_atomic_add_negative(int i, atomic_t \*v)
:   atomic add and test if negative with full ordering

**Parameters**

`int i`
:   int value to add

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** + **i**) with full ordering.

Safe to use in noinstr code; prefer [`atomic_add_negative()`](basics.md#c.atomic_add_negative "atomic_add_negative") elsewhere.

**Return**

**true** if the resulting value of **v** is negative, **false** otherwise.

bool raw_atomic_add_negative_acquire(int i, atomic_t \*v)
:   atomic add and test if negative with acquire ordering

**Parameters**

`int i`
:   int value to add

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** + **i**) with acquire ordering.

Safe to use in noinstr code; prefer [`atomic_add_negative_acquire()`](basics.md#c.atomic_add_negative_acquire "atomic_add_negative_acquire") elsewhere.

**Return**

**true** if the resulting value of **v** is negative, **false** otherwise.

bool raw_atomic_add_negative_release(int i, atomic_t \*v)
:   atomic add and test if negative with release ordering

**Parameters**

`int i`
:   int value to add

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** + **i**) with release ordering.

Safe to use in noinstr code; prefer [`atomic_add_negative_release()`](basics.md#c.atomic_add_negative_release "atomic_add_negative_release") elsewhere.

**Return**

**true** if the resulting value of **v** is negative, **false** otherwise.

bool raw_atomic_add_negative_relaxed(int i, atomic_t \*v)
:   atomic add and test if negative with relaxed ordering

**Parameters**

`int i`
:   int value to add

`atomic_t *v`
:   pointer to atomic_t

**Description**

Atomically updates **v** to (**v** + **i**) with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic_add_negative_relaxed()`](basics.md#c.atomic_add_negative_relaxed "atomic_add_negative_relaxed") elsewhere.

**Return**

**true** if the resulting value of **v** is negative, **false** otherwise.

int raw_atomic_fetch_add_unless(atomic_t \*v, int a, int u)
:   atomic add unless value with full ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

`int a`
:   int value to add

`int u`
:   int value to compare with

**Description**

If (**v** != **u**), atomically updates **v** to (**v** + **a**) with full ordering.

Safe to use in noinstr code; prefer [`atomic_fetch_add_unless()`](basics.md#c.atomic_fetch_add_unless "atomic_fetch_add_unless") elsewhere.

**Return**

The original value of **v**.

bool raw_atomic_add_unless(atomic_t \*v, int a, int u)
:   atomic add unless value with full ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

`int a`
:   int value to add

`int u`
:   int value to compare with

**Description**

If (**v** != **u**), atomically updates **v** to (**v** + **a**) with full ordering.

Safe to use in noinstr code; prefer [`atomic_add_unless()`](basics.md#c.atomic_add_unless "atomic_add_unless") elsewhere.

**Return**

**true** if **v** was updated, **false** otherwise.

bool raw_atomic_inc_not_zero(atomic_t \*v)
:   atomic increment unless zero with full ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

**Description**

If (**v** != 0), atomically updates **v** to (**v** + 1) with full ordering.

Safe to use in noinstr code; prefer [`atomic_inc_not_zero()`](basics.md#c.atomic_inc_not_zero "atomic_inc_not_zero") elsewhere.

**Return**

**true** if **v** was updated, **false** otherwise.

bool raw_atomic_inc_unless_negative(atomic_t \*v)
:   atomic increment unless negative with full ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

**Description**

If (**v** >= 0), atomically updates **v** to (**v** + 1) with full ordering.

Safe to use in noinstr code; prefer [`atomic_inc_unless_negative()`](basics.md#c.atomic_inc_unless_negative "atomic_inc_unless_negative") elsewhere.

**Return**

**true** if **v** was updated, **false** otherwise.

bool raw_atomic_dec_unless_positive(atomic_t \*v)
:   atomic decrement unless positive with full ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

**Description**

If (**v** <= 0), atomically updates **v** to (**v** - 1) with full ordering.

Safe to use in noinstr code; prefer [`atomic_dec_unless_positive()`](basics.md#c.atomic_dec_unless_positive "atomic_dec_unless_positive") elsewhere.

**Return**

**true** if **v** was updated, **false** otherwise.

int raw_atomic_dec_if_positive(atomic_t \*v)
:   atomic decrement if positive with full ordering

**Parameters**

`atomic_t *v`
:   pointer to atomic_t

**Description**

If (**v** > 0), atomically updates **v** to (**v** - 1) with full ordering.

Safe to use in noinstr code; prefer [`atomic_dec_if_positive()`](basics.md#c.atomic_dec_if_positive "atomic_dec_if_positive") elsewhere.

**Return**

The old value of (**v** - 1), regardless of whether **v** was updated.

s64 raw_atomic64_read(const atomic64_t \*v)
:   atomic load with relaxed ordering

**Parameters**

`const atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically loads the value of **v** with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic64_read()`](basics.md#c.atomic64_read "atomic64_read") elsewhere.

**Return**

The value loaded from **v**.

s64 raw_atomic64_read_acquire(const atomic64_t \*v)
:   atomic load with acquire ordering

**Parameters**

`const atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically loads the value of **v** with acquire ordering.

Safe to use in noinstr code; prefer [`atomic64_read_acquire()`](basics.md#c.atomic64_read_acquire "atomic64_read_acquire") elsewhere.

**Return**

The value loaded from **v**.

void raw_atomic64_set(atomic64_t \*v, s64 i)
:   atomic set with relaxed ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

`s64 i`
:   s64 value to assign

**Description**

Atomically sets **v** to **i** with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic64_set()`](basics.md#c.atomic64_set "atomic64_set") elsewhere.

**Return**

Nothing.

void raw_atomic64_set_release(atomic64_t \*v, s64 i)
:   atomic set with release ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

`s64 i`
:   s64 value to assign

**Description**

Atomically sets **v** to **i** with release ordering.

Safe to use in noinstr code; prefer [`atomic64_set_release()`](basics.md#c.atomic64_set_release "atomic64_set_release") elsewhere.

**Return**

Nothing.

void raw_atomic64_add(s64 i, atomic64_t \*v)
:   atomic add with relaxed ordering

**Parameters**

`s64 i`
:   s64 value to add

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** + **i**) with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic64_add()`](basics.md#c.atomic64_add "atomic64_add") elsewhere.

**Return**

Nothing.

s64 raw_atomic64_add_return(s64 i, atomic64_t \*v)
:   atomic add with full ordering

**Parameters**

`s64 i`
:   s64 value to add

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** + **i**) with full ordering.

Safe to use in noinstr code; prefer [`atomic64_add_return()`](basics.md#c.atomic64_add_return "atomic64_add_return") elsewhere.

**Return**

The updated value of **v**.

s64 raw_atomic64_add_return_acquire(s64 i, atomic64_t \*v)
:   atomic add with acquire ordering

**Parameters**

`s64 i`
:   s64 value to add

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** + **i**) with acquire ordering.

Safe to use in noinstr code; prefer [`atomic64_add_return_acquire()`](basics.md#c.atomic64_add_return_acquire "atomic64_add_return_acquire") elsewhere.

**Return**

The updated value of **v**.

s64 raw_atomic64_add_return_release(s64 i, atomic64_t \*v)
:   atomic add with release ordering

**Parameters**

`s64 i`
:   s64 value to add

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** + **i**) with release ordering.

Safe to use in noinstr code; prefer [`atomic64_add_return_release()`](basics.md#c.atomic64_add_return_release "atomic64_add_return_release") elsewhere.

**Return**

The updated value of **v**.

s64 raw_atomic64_add_return_relaxed(s64 i, atomic64_t \*v)
:   atomic add with relaxed ordering

**Parameters**

`s64 i`
:   s64 value to add

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** + **i**) with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic64_add_return_relaxed()`](basics.md#c.atomic64_add_return_relaxed "atomic64_add_return_relaxed") elsewhere.

**Return**

The updated value of **v**.

s64 raw_atomic64_fetch_add(s64 i, atomic64_t \*v)
:   atomic add with full ordering

**Parameters**

`s64 i`
:   s64 value to add

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** + **i**) with full ordering.

Safe to use in noinstr code; prefer [`atomic64_fetch_add()`](basics.md#c.atomic64_fetch_add "atomic64_fetch_add") elsewhere.

**Return**

The original value of **v**.

s64 raw_atomic64_fetch_add_acquire(s64 i, atomic64_t \*v)
:   atomic add with acquire ordering

**Parameters**

`s64 i`
:   s64 value to add

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** + **i**) with acquire ordering.

Safe to use in noinstr code; prefer [`atomic64_fetch_add_acquire()`](basics.md#c.atomic64_fetch_add_acquire "atomic64_fetch_add_acquire") elsewhere.

**Return**

The original value of **v**.

s64 raw_atomic64_fetch_add_release(s64 i, atomic64_t \*v)
:   atomic add with release ordering

**Parameters**

`s64 i`
:   s64 value to add

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** + **i**) with release ordering.

Safe to use in noinstr code; prefer [`atomic64_fetch_add_release()`](basics.md#c.atomic64_fetch_add_release "atomic64_fetch_add_release") elsewhere.

**Return**

The original value of **v**.

s64 raw_atomic64_fetch_add_relaxed(s64 i, atomic64_t \*v)
:   atomic add with relaxed ordering

**Parameters**

`s64 i`
:   s64 value to add

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** + **i**) with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic64_fetch_add_relaxed()`](basics.md#c.atomic64_fetch_add_relaxed "atomic64_fetch_add_relaxed") elsewhere.

**Return**

The original value of **v**.

void raw_atomic64_sub(s64 i, atomic64_t \*v)
:   atomic subtract with relaxed ordering

**Parameters**

`s64 i`
:   s64 value to subtract

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** - **i**) with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic64_sub()`](basics.md#c.atomic64_sub "atomic64_sub") elsewhere.

**Return**

Nothing.

s64 raw_atomic64_sub_return(s64 i, atomic64_t \*v)
:   atomic subtract with full ordering

**Parameters**

`s64 i`
:   s64 value to subtract

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** - **i**) with full ordering.

Safe to use in noinstr code; prefer [`atomic64_sub_return()`](basics.md#c.atomic64_sub_return "atomic64_sub_return") elsewhere.

**Return**

The updated value of **v**.

s64 raw_atomic64_sub_return_acquire(s64 i, atomic64_t \*v)
:   atomic subtract with acquire ordering

**Parameters**

`s64 i`
:   s64 value to subtract

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** - **i**) with acquire ordering.

Safe to use in noinstr code; prefer [`atomic64_sub_return_acquire()`](basics.md#c.atomic64_sub_return_acquire "atomic64_sub_return_acquire") elsewhere.

**Return**

The updated value of **v**.

s64 raw_atomic64_sub_return_release(s64 i, atomic64_t \*v)
:   atomic subtract with release ordering

**Parameters**

`s64 i`
:   s64 value to subtract

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** - **i**) with release ordering.

Safe to use in noinstr code; prefer [`atomic64_sub_return_release()`](basics.md#c.atomic64_sub_return_release "atomic64_sub_return_release") elsewhere.

**Return**

The updated value of **v**.

s64 raw_atomic64_sub_return_relaxed(s64 i, atomic64_t \*v)
:   atomic subtract with relaxed ordering

**Parameters**

`s64 i`
:   s64 value to subtract

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** - **i**) with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic64_sub_return_relaxed()`](basics.md#c.atomic64_sub_return_relaxed "atomic64_sub_return_relaxed") elsewhere.

**Return**

The updated value of **v**.

s64 raw_atomic64_fetch_sub(s64 i, atomic64_t \*v)
:   atomic subtract with full ordering

**Parameters**

`s64 i`
:   s64 value to subtract

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** - **i**) with full ordering.

Safe to use in noinstr code; prefer [`atomic64_fetch_sub()`](basics.md#c.atomic64_fetch_sub "atomic64_fetch_sub") elsewhere.

**Return**

The original value of **v**.

s64 raw_atomic64_fetch_sub_acquire(s64 i, atomic64_t \*v)
:   atomic subtract with acquire ordering

**Parameters**

`s64 i`
:   s64 value to subtract

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** - **i**) with acquire ordering.

Safe to use in noinstr code; prefer [`atomic64_fetch_sub_acquire()`](basics.md#c.atomic64_fetch_sub_acquire "atomic64_fetch_sub_acquire") elsewhere.

**Return**

The original value of **v**.

s64 raw_atomic64_fetch_sub_release(s64 i, atomic64_t \*v)
:   atomic subtract with release ordering

**Parameters**

`s64 i`
:   s64 value to subtract

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** - **i**) with release ordering.

Safe to use in noinstr code; prefer [`atomic64_fetch_sub_release()`](basics.md#c.atomic64_fetch_sub_release "atomic64_fetch_sub_release") elsewhere.

**Return**

The original value of **v**.

s64 raw_atomic64_fetch_sub_relaxed(s64 i, atomic64_t \*v)
:   atomic subtract with relaxed ordering

**Parameters**

`s64 i`
:   s64 value to subtract

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** - **i**) with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic64_fetch_sub_relaxed()`](basics.md#c.atomic64_fetch_sub_relaxed "atomic64_fetch_sub_relaxed") elsewhere.

**Return**

The original value of **v**.

void raw_atomic64_inc(atomic64_t \*v)
:   atomic increment with relaxed ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** + 1) with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic64_inc()`](basics.md#c.atomic64_inc "atomic64_inc") elsewhere.

**Return**

Nothing.

s64 raw_atomic64_inc_return(atomic64_t \*v)
:   atomic increment with full ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** + 1) with full ordering.

Safe to use in noinstr code; prefer [`atomic64_inc_return()`](basics.md#c.atomic64_inc_return "atomic64_inc_return") elsewhere.

**Return**

The updated value of **v**.

s64 raw_atomic64_inc_return_acquire(atomic64_t \*v)
:   atomic increment with acquire ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** + 1) with acquire ordering.

Safe to use in noinstr code; prefer [`atomic64_inc_return_acquire()`](basics.md#c.atomic64_inc_return_acquire "atomic64_inc_return_acquire") elsewhere.

**Return**

The updated value of **v**.

s64 raw_atomic64_inc_return_release(atomic64_t \*v)
:   atomic increment with release ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** + 1) with release ordering.

Safe to use in noinstr code; prefer [`atomic64_inc_return_release()`](basics.md#c.atomic64_inc_return_release "atomic64_inc_return_release") elsewhere.

**Return**

The updated value of **v**.

s64 raw_atomic64_inc_return_relaxed(atomic64_t \*v)
:   atomic increment with relaxed ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** + 1) with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic64_inc_return_relaxed()`](basics.md#c.atomic64_inc_return_relaxed "atomic64_inc_return_relaxed") elsewhere.

**Return**

The updated value of **v**.

s64 raw_atomic64_fetch_inc(atomic64_t \*v)
:   atomic increment with full ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** + 1) with full ordering.

Safe to use in noinstr code; prefer [`atomic64_fetch_inc()`](basics.md#c.atomic64_fetch_inc "atomic64_fetch_inc") elsewhere.

**Return**

The original value of **v**.

s64 raw_atomic64_fetch_inc_acquire(atomic64_t \*v)
:   atomic increment with acquire ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** + 1) with acquire ordering.

Safe to use in noinstr code; prefer [`atomic64_fetch_inc_acquire()`](basics.md#c.atomic64_fetch_inc_acquire "atomic64_fetch_inc_acquire") elsewhere.

**Return**

The original value of **v**.

s64 raw_atomic64_fetch_inc_release(atomic64_t \*v)
:   atomic increment with release ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** + 1) with release ordering.

Safe to use in noinstr code; prefer [`atomic64_fetch_inc_release()`](basics.md#c.atomic64_fetch_inc_release "atomic64_fetch_inc_release") elsewhere.

**Return**

The original value of **v**.

s64 raw_atomic64_fetch_inc_relaxed(atomic64_t \*v)
:   atomic increment with relaxed ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** + 1) with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic64_fetch_inc_relaxed()`](basics.md#c.atomic64_fetch_inc_relaxed "atomic64_fetch_inc_relaxed") elsewhere.

**Return**

The original value of **v**.

void raw_atomic64_dec(atomic64_t \*v)
:   atomic decrement with relaxed ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** - 1) with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic64_dec()`](basics.md#c.atomic64_dec "atomic64_dec") elsewhere.

**Return**

Nothing.

s64 raw_atomic64_dec_return(atomic64_t \*v)
:   atomic decrement with full ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** - 1) with full ordering.

Safe to use in noinstr code; prefer [`atomic64_dec_return()`](basics.md#c.atomic64_dec_return "atomic64_dec_return") elsewhere.

**Return**

The updated value of **v**.

s64 raw_atomic64_dec_return_acquire(atomic64_t \*v)
:   atomic decrement with acquire ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** - 1) with acquire ordering.

Safe to use in noinstr code; prefer [`atomic64_dec_return_acquire()`](basics.md#c.atomic64_dec_return_acquire "atomic64_dec_return_acquire") elsewhere.

**Return**

The updated value of **v**.

s64 raw_atomic64_dec_return_release(atomic64_t \*v)
:   atomic decrement with release ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** - 1) with release ordering.

Safe to use in noinstr code; prefer [`atomic64_dec_return_release()`](basics.md#c.atomic64_dec_return_release "atomic64_dec_return_release") elsewhere.

**Return**

The updated value of **v**.

s64 raw_atomic64_dec_return_relaxed(atomic64_t \*v)
:   atomic decrement with relaxed ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** - 1) with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic64_dec_return_relaxed()`](basics.md#c.atomic64_dec_return_relaxed "atomic64_dec_return_relaxed") elsewhere.

**Return**

The updated value of **v**.

s64 raw_atomic64_fetch_dec(atomic64_t \*v)
:   atomic decrement with full ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** - 1) with full ordering.

Safe to use in noinstr code; prefer [`atomic64_fetch_dec()`](basics.md#c.atomic64_fetch_dec "atomic64_fetch_dec") elsewhere.

**Return**

The original value of **v**.

s64 raw_atomic64_fetch_dec_acquire(atomic64_t \*v)
:   atomic decrement with acquire ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** - 1) with acquire ordering.

Safe to use in noinstr code; prefer [`atomic64_fetch_dec_acquire()`](basics.md#c.atomic64_fetch_dec_acquire "atomic64_fetch_dec_acquire") elsewhere.

**Return**

The original value of **v**.

s64 raw_atomic64_fetch_dec_release(atomic64_t \*v)
:   atomic decrement with release ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** - 1) with release ordering.

Safe to use in noinstr code; prefer [`atomic64_fetch_dec_release()`](basics.md#c.atomic64_fetch_dec_release "atomic64_fetch_dec_release") elsewhere.

**Return**

The original value of **v**.

s64 raw_atomic64_fetch_dec_relaxed(atomic64_t \*v)
:   atomic decrement with relaxed ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** - 1) with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic64_fetch_dec_relaxed()`](basics.md#c.atomic64_fetch_dec_relaxed "atomic64_fetch_dec_relaxed") elsewhere.

**Return**

The original value of **v**.

void raw_atomic64_and(s64 i, atomic64_t \*v)
:   atomic bitwise AND with relaxed ordering

**Parameters**

`s64 i`
:   s64 value

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** & **i**) with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic64_and()`](basics.md#c.atomic64_and "atomic64_and") elsewhere.

**Return**

Nothing.

s64 raw_atomic64_fetch_and(s64 i, atomic64_t \*v)
:   atomic bitwise AND with full ordering

**Parameters**

`s64 i`
:   s64 value

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** & **i**) with full ordering.

Safe to use in noinstr code; prefer [`atomic64_fetch_and()`](basics.md#c.atomic64_fetch_and "atomic64_fetch_and") elsewhere.

**Return**

The original value of **v**.

s64 raw_atomic64_fetch_and_acquire(s64 i, atomic64_t \*v)
:   atomic bitwise AND with acquire ordering

**Parameters**

`s64 i`
:   s64 value

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** & **i**) with acquire ordering.

Safe to use in noinstr code; prefer [`atomic64_fetch_and_acquire()`](basics.md#c.atomic64_fetch_and_acquire "atomic64_fetch_and_acquire") elsewhere.

**Return**

The original value of **v**.

s64 raw_atomic64_fetch_and_release(s64 i, atomic64_t \*v)
:   atomic bitwise AND with release ordering

**Parameters**

`s64 i`
:   s64 value

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** & **i**) with release ordering.

Safe to use in noinstr code; prefer [`atomic64_fetch_and_release()`](basics.md#c.atomic64_fetch_and_release "atomic64_fetch_and_release") elsewhere.

**Return**

The original value of **v**.

s64 raw_atomic64_fetch_and_relaxed(s64 i, atomic64_t \*v)
:   atomic bitwise AND with relaxed ordering

**Parameters**

`s64 i`
:   s64 value

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** & **i**) with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic64_fetch_and_relaxed()`](basics.md#c.atomic64_fetch_and_relaxed "atomic64_fetch_and_relaxed") elsewhere.

**Return**

The original value of **v**.

void raw_atomic64_andnot(s64 i, atomic64_t \*v)
:   atomic bitwise AND NOT with relaxed ordering

**Parameters**

`s64 i`
:   s64 value

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** & **~i**) with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic64_andnot()`](basics.md#c.atomic64_andnot "atomic64_andnot") elsewhere.

**Return**

Nothing.

s64 raw_atomic64_fetch_andnot(s64 i, atomic64_t \*v)
:   atomic bitwise AND NOT with full ordering

**Parameters**

`s64 i`
:   s64 value

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** & **~i**) with full ordering.

Safe to use in noinstr code; prefer [`atomic64_fetch_andnot()`](basics.md#c.atomic64_fetch_andnot "atomic64_fetch_andnot") elsewhere.

**Return**

The original value of **v**.

s64 raw_atomic64_fetch_andnot_acquire(s64 i, atomic64_t \*v)
:   atomic bitwise AND NOT with acquire ordering

**Parameters**

`s64 i`
:   s64 value

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** & **~i**) with acquire ordering.

Safe to use in noinstr code; prefer [`atomic64_fetch_andnot_acquire()`](basics.md#c.atomic64_fetch_andnot_acquire "atomic64_fetch_andnot_acquire") elsewhere.

**Return**

The original value of **v**.

s64 raw_atomic64_fetch_andnot_release(s64 i, atomic64_t \*v)
:   atomic bitwise AND NOT with release ordering

**Parameters**

`s64 i`
:   s64 value

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** & **~i**) with release ordering.

Safe to use in noinstr code; prefer [`atomic64_fetch_andnot_release()`](basics.md#c.atomic64_fetch_andnot_release "atomic64_fetch_andnot_release") elsewhere.

**Return**

The original value of **v**.

s64 raw_atomic64_fetch_andnot_relaxed(s64 i, atomic64_t \*v)
:   atomic bitwise AND NOT with relaxed ordering

**Parameters**

`s64 i`
:   s64 value

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** & **~i**) with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic64_fetch_andnot_relaxed()`](basics.md#c.atomic64_fetch_andnot_relaxed "atomic64_fetch_andnot_relaxed") elsewhere.

**Return**

The original value of **v**.

void raw_atomic64_or(s64 i, atomic64_t \*v)
:   atomic bitwise OR with relaxed ordering

**Parameters**

`s64 i`
:   s64 value

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** | **i**) with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic64_or()`](basics.md#c.atomic64_or "atomic64_or") elsewhere.

**Return**

Nothing.

s64 raw_atomic64_fetch_or(s64 i, atomic64_t \*v)
:   atomic bitwise OR with full ordering

**Parameters**

`s64 i`
:   s64 value

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** | **i**) with full ordering.

Safe to use in noinstr code; prefer [`atomic64_fetch_or()`](basics.md#c.atomic64_fetch_or "atomic64_fetch_or") elsewhere.

**Return**

The original value of **v**.

s64 raw_atomic64_fetch_or_acquire(s64 i, atomic64_t \*v)
:   atomic bitwise OR with acquire ordering

**Parameters**

`s64 i`
:   s64 value

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** | **i**) with acquire ordering.

Safe to use in noinstr code; prefer [`atomic64_fetch_or_acquire()`](basics.md#c.atomic64_fetch_or_acquire "atomic64_fetch_or_acquire") elsewhere.

**Return**

The original value of **v**.

s64 raw_atomic64_fetch_or_release(s64 i, atomic64_t \*v)
:   atomic bitwise OR with release ordering

**Parameters**

`s64 i`
:   s64 value

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** | **i**) with release ordering.

Safe to use in noinstr code; prefer [`atomic64_fetch_or_release()`](basics.md#c.atomic64_fetch_or_release "atomic64_fetch_or_release") elsewhere.

**Return**

The original value of **v**.

s64 raw_atomic64_fetch_or_relaxed(s64 i, atomic64_t \*v)
:   atomic bitwise OR with relaxed ordering

**Parameters**

`s64 i`
:   s64 value

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** | **i**) with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic64_fetch_or_relaxed()`](basics.md#c.atomic64_fetch_or_relaxed "atomic64_fetch_or_relaxed") elsewhere.

**Return**

The original value of **v**.

void raw_atomic64_xor(s64 i, atomic64_t \*v)
:   atomic bitwise XOR with relaxed ordering

**Parameters**

`s64 i`
:   s64 value

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** ^ **i**) with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic64_xor()`](basics.md#c.atomic64_xor "atomic64_xor") elsewhere.

**Return**

Nothing.

s64 raw_atomic64_fetch_xor(s64 i, atomic64_t \*v)
:   atomic bitwise XOR with full ordering

**Parameters**

`s64 i`
:   s64 value

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** ^ **i**) with full ordering.

Safe to use in noinstr code; prefer [`atomic64_fetch_xor()`](basics.md#c.atomic64_fetch_xor "atomic64_fetch_xor") elsewhere.

**Return**

The original value of **v**.

s64 raw_atomic64_fetch_xor_acquire(s64 i, atomic64_t \*v)
:   atomic bitwise XOR with acquire ordering

**Parameters**

`s64 i`
:   s64 value

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** ^ **i**) with acquire ordering.

Safe to use in noinstr code; prefer [`atomic64_fetch_xor_acquire()`](basics.md#c.atomic64_fetch_xor_acquire "atomic64_fetch_xor_acquire") elsewhere.

**Return**

The original value of **v**.

s64 raw_atomic64_fetch_xor_release(s64 i, atomic64_t \*v)
:   atomic bitwise XOR with release ordering

**Parameters**

`s64 i`
:   s64 value

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** ^ **i**) with release ordering.

Safe to use in noinstr code; prefer [`atomic64_fetch_xor_release()`](basics.md#c.atomic64_fetch_xor_release "atomic64_fetch_xor_release") elsewhere.

**Return**

The original value of **v**.

s64 raw_atomic64_fetch_xor_relaxed(s64 i, atomic64_t \*v)
:   atomic bitwise XOR with relaxed ordering

**Parameters**

`s64 i`
:   s64 value

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** ^ **i**) with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic64_fetch_xor_relaxed()`](basics.md#c.atomic64_fetch_xor_relaxed "atomic64_fetch_xor_relaxed") elsewhere.

**Return**

The original value of **v**.

s64 raw_atomic64_xchg(atomic64_t \*v, s64 new)
:   atomic exchange with full ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

`s64 new`
:   s64 value to assign

**Description**

Atomically updates **v** to **new** with full ordering.

Safe to use in noinstr code; prefer [`atomic64_xchg()`](basics.md#c.atomic64_xchg "atomic64_xchg") elsewhere.

**Return**

The original value of **v**.

s64 raw_atomic64_xchg_acquire(atomic64_t \*v, s64 new)
:   atomic exchange with acquire ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

`s64 new`
:   s64 value to assign

**Description**

Atomically updates **v** to **new** with acquire ordering.

Safe to use in noinstr code; prefer [`atomic64_xchg_acquire()`](basics.md#c.atomic64_xchg_acquire "atomic64_xchg_acquire") elsewhere.

**Return**

The original value of **v**.

s64 raw_atomic64_xchg_release(atomic64_t \*v, s64 new)
:   atomic exchange with release ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

`s64 new`
:   s64 value to assign

**Description**

Atomically updates **v** to **new** with release ordering.

Safe to use in noinstr code; prefer [`atomic64_xchg_release()`](basics.md#c.atomic64_xchg_release "atomic64_xchg_release") elsewhere.

**Return**

The original value of **v**.

s64 raw_atomic64_xchg_relaxed(atomic64_t \*v, s64 new)
:   atomic exchange with relaxed ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

`s64 new`
:   s64 value to assign

**Description**

Atomically updates **v** to **new** with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic64_xchg_relaxed()`](basics.md#c.atomic64_xchg_relaxed "atomic64_xchg_relaxed") elsewhere.

**Return**

The original value of **v**.

s64 raw_atomic64_cmpxchg(atomic64_t \*v, s64 old, s64 new)
:   atomic compare and exchange with full ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

`s64 old`
:   s64 value to compare with

`s64 new`
:   s64 value to assign

**Description**

If (**v** == **old**), atomically updates **v** to **new** with full ordering.

Safe to use in noinstr code; prefer [`atomic64_cmpxchg()`](basics.md#c.atomic64_cmpxchg "atomic64_cmpxchg") elsewhere.

**Return**

The original value of **v**.

s64 raw_atomic64_cmpxchg_acquire(atomic64_t \*v, s64 old, s64 new)
:   atomic compare and exchange with acquire ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

`s64 old`
:   s64 value to compare with

`s64 new`
:   s64 value to assign

**Description**

If (**v** == **old**), atomically updates **v** to **new** with acquire ordering.

Safe to use in noinstr code; prefer [`atomic64_cmpxchg_acquire()`](basics.md#c.atomic64_cmpxchg_acquire "atomic64_cmpxchg_acquire") elsewhere.

**Return**

The original value of **v**.

s64 raw_atomic64_cmpxchg_release(atomic64_t \*v, s64 old, s64 new)
:   atomic compare and exchange with release ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

`s64 old`
:   s64 value to compare with

`s64 new`
:   s64 value to assign

**Description**

If (**v** == **old**), atomically updates **v** to **new** with release ordering.

Safe to use in noinstr code; prefer [`atomic64_cmpxchg_release()`](basics.md#c.atomic64_cmpxchg_release "atomic64_cmpxchg_release") elsewhere.

**Return**

The original value of **v**.

s64 raw_atomic64_cmpxchg_relaxed(atomic64_t \*v, s64 old, s64 new)
:   atomic compare and exchange with relaxed ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

`s64 old`
:   s64 value to compare with

`s64 new`
:   s64 value to assign

**Description**

If (**v** == **old**), atomically updates **v** to **new** with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic64_cmpxchg_relaxed()`](basics.md#c.atomic64_cmpxchg_relaxed "atomic64_cmpxchg_relaxed") elsewhere.

**Return**

The original value of **v**.

bool raw_atomic64_try_cmpxchg(atomic64_t \*v, s64 \*old, s64 new)
:   atomic compare and exchange with full ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

`s64 *old`
:   pointer to s64 value to compare with

`s64 new`
:   s64 value to assign

**Description**

If (**v** == **old**), atomically updates **v** to **new** with full ordering.
Otherwise, updates **old** to the current value of **v**.

Safe to use in noinstr code; prefer [`atomic64_try_cmpxchg()`](basics.md#c.atomic64_try_cmpxchg "atomic64_try_cmpxchg") elsewhere.

**Return**

**true** if the exchange occured, **false** otherwise.

bool raw_atomic64_try_cmpxchg_acquire(atomic64_t \*v, s64 \*old, s64 new)
:   atomic compare and exchange with acquire ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

`s64 *old`
:   pointer to s64 value to compare with

`s64 new`
:   s64 value to assign

**Description**

If (**v** == **old**), atomically updates **v** to **new** with acquire ordering.
Otherwise, updates **old** to the current value of **v**.

Safe to use in noinstr code; prefer [`atomic64_try_cmpxchg_acquire()`](basics.md#c.atomic64_try_cmpxchg_acquire "atomic64_try_cmpxchg_acquire") elsewhere.

**Return**

**true** if the exchange occured, **false** otherwise.

bool raw_atomic64_try_cmpxchg_release(atomic64_t \*v, s64 \*old, s64 new)
:   atomic compare and exchange with release ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

`s64 *old`
:   pointer to s64 value to compare with

`s64 new`
:   s64 value to assign

**Description**

If (**v** == **old**), atomically updates **v** to **new** with release ordering.
Otherwise, updates **old** to the current value of **v**.

Safe to use in noinstr code; prefer [`atomic64_try_cmpxchg_release()`](basics.md#c.atomic64_try_cmpxchg_release "atomic64_try_cmpxchg_release") elsewhere.

**Return**

**true** if the exchange occured, **false** otherwise.

bool raw_atomic64_try_cmpxchg_relaxed(atomic64_t \*v, s64 \*old, s64 new)
:   atomic compare and exchange with relaxed ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

`s64 *old`
:   pointer to s64 value to compare with

`s64 new`
:   s64 value to assign

**Description**

If (**v** == **old**), atomically updates **v** to **new** with relaxed ordering.
Otherwise, updates **old** to the current value of **v**.

Safe to use in noinstr code; prefer [`atomic64_try_cmpxchg_relaxed()`](basics.md#c.atomic64_try_cmpxchg_relaxed "atomic64_try_cmpxchg_relaxed") elsewhere.

**Return**

**true** if the exchange occured, **false** otherwise.

bool raw_atomic64_sub_and_test(s64 i, atomic64_t \*v)
:   atomic subtract and test if zero with full ordering

**Parameters**

`s64 i`
:   s64 value to add

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** - **i**) with full ordering.

Safe to use in noinstr code; prefer [`atomic64_sub_and_test()`](basics.md#c.atomic64_sub_and_test "atomic64_sub_and_test") elsewhere.

**Return**

**true** if the resulting value of **v** is zero, **false** otherwise.

bool raw_atomic64_dec_and_test(atomic64_t \*v)
:   atomic decrement and test if zero with full ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** - 1) with full ordering.

Safe to use in noinstr code; prefer [`atomic64_dec_and_test()`](basics.md#c.atomic64_dec_and_test "atomic64_dec_and_test") elsewhere.

**Return**

**true** if the resulting value of **v** is zero, **false** otherwise.

bool raw_atomic64_inc_and_test(atomic64_t \*v)
:   atomic increment and test if zero with full ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** + 1) with full ordering.

Safe to use in noinstr code; prefer [`atomic64_inc_and_test()`](basics.md#c.atomic64_inc_and_test "atomic64_inc_and_test") elsewhere.

**Return**

**true** if the resulting value of **v** is zero, **false** otherwise.

bool raw_atomic64_add_negative(s64 i, atomic64_t \*v)
:   atomic add and test if negative with full ordering

**Parameters**

`s64 i`
:   s64 value to add

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** + **i**) with full ordering.

Safe to use in noinstr code; prefer [`atomic64_add_negative()`](basics.md#c.atomic64_add_negative "atomic64_add_negative") elsewhere.

**Return**

**true** if the resulting value of **v** is negative, **false** otherwise.

bool raw_atomic64_add_negative_acquire(s64 i, atomic64_t \*v)
:   atomic add and test if negative with acquire ordering

**Parameters**

`s64 i`
:   s64 value to add

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** + **i**) with acquire ordering.

Safe to use in noinstr code; prefer [`atomic64_add_negative_acquire()`](basics.md#c.atomic64_add_negative_acquire "atomic64_add_negative_acquire") elsewhere.

**Return**

**true** if the resulting value of **v** is negative, **false** otherwise.

bool raw_atomic64_add_negative_release(s64 i, atomic64_t \*v)
:   atomic add and test if negative with release ordering

**Parameters**

`s64 i`
:   s64 value to add

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** + **i**) with release ordering.

Safe to use in noinstr code; prefer [`atomic64_add_negative_release()`](basics.md#c.atomic64_add_negative_release "atomic64_add_negative_release") elsewhere.

**Return**

**true** if the resulting value of **v** is negative, **false** otherwise.

bool raw_atomic64_add_negative_relaxed(s64 i, atomic64_t \*v)
:   atomic add and test if negative with relaxed ordering

**Parameters**

`s64 i`
:   s64 value to add

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

Atomically updates **v** to (**v** + **i**) with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic64_add_negative_relaxed()`](basics.md#c.atomic64_add_negative_relaxed "atomic64_add_negative_relaxed") elsewhere.

**Return**

**true** if the resulting value of **v** is negative, **false** otherwise.

s64 raw_atomic64_fetch_add_unless(atomic64_t \*v, s64 a, s64 u)
:   atomic add unless value with full ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

`s64 a`
:   s64 value to add

`s64 u`
:   s64 value to compare with

**Description**

If (**v** != **u**), atomically updates **v** to (**v** + **a**) with full ordering.

Safe to use in noinstr code; prefer [`atomic64_fetch_add_unless()`](basics.md#c.atomic64_fetch_add_unless "atomic64_fetch_add_unless") elsewhere.

**Return**

The original value of **v**.

bool raw_atomic64_add_unless(atomic64_t \*v, s64 a, s64 u)
:   atomic add unless value with full ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

`s64 a`
:   s64 value to add

`s64 u`
:   s64 value to compare with

**Description**

If (**v** != **u**), atomically updates **v** to (**v** + **a**) with full ordering.

Safe to use in noinstr code; prefer [`atomic64_add_unless()`](basics.md#c.atomic64_add_unless "atomic64_add_unless") elsewhere.

**Return**

**true** if **v** was updated, **false** otherwise.

bool raw_atomic64_inc_not_zero(atomic64_t \*v)
:   atomic increment unless zero with full ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

If (**v** != 0), atomically updates **v** to (**v** + 1) with full ordering.

Safe to use in noinstr code; prefer [`atomic64_inc_not_zero()`](basics.md#c.atomic64_inc_not_zero "atomic64_inc_not_zero") elsewhere.

**Return**

**true** if **v** was updated, **false** otherwise.

bool raw_atomic64_inc_unless_negative(atomic64_t \*v)
:   atomic increment unless negative with full ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

If (**v** >= 0), atomically updates **v** to (**v** + 1) with full ordering.

Safe to use in noinstr code; prefer [`atomic64_inc_unless_negative()`](basics.md#c.atomic64_inc_unless_negative "atomic64_inc_unless_negative") elsewhere.

**Return**

**true** if **v** was updated, **false** otherwise.

bool raw_atomic64_dec_unless_positive(atomic64_t \*v)
:   atomic decrement unless positive with full ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

If (**v** <= 0), atomically updates **v** to (**v** - 1) with full ordering.

Safe to use in noinstr code; prefer [`atomic64_dec_unless_positive()`](basics.md#c.atomic64_dec_unless_positive "atomic64_dec_unless_positive") elsewhere.

**Return**

**true** if **v** was updated, **false** otherwise.

s64 raw_atomic64_dec_if_positive(atomic64_t \*v)
:   atomic decrement if positive with full ordering

**Parameters**

`atomic64_t *v`
:   pointer to atomic64_t

**Description**

If (**v** > 0), atomically updates **v** to (**v** - 1) with full ordering.

Safe to use in noinstr code; prefer [`atomic64_dec_if_positive()`](basics.md#c.atomic64_dec_if_positive "atomic64_dec_if_positive") elsewhere.

**Return**

The old value of (**v** - 1), regardless of whether **v** was updated.

long raw_atomic_long_read(const atomic_long_t \*v)
:   atomic load with relaxed ordering

**Parameters**

`const atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically loads the value of **v** with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic_long_read()`](basics.md#c.atomic_long_read "atomic_long_read") elsewhere.

**Return**

The value loaded from **v**.

long raw_atomic_long_read_acquire(const atomic_long_t \*v)
:   atomic load with acquire ordering

**Parameters**

`const atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically loads the value of **v** with acquire ordering.

Safe to use in noinstr code; prefer [`atomic_long_read_acquire()`](basics.md#c.atomic_long_read_acquire "atomic_long_read_acquire") elsewhere.

**Return**

The value loaded from **v**.

void raw_atomic_long_set(atomic_long_t \*v, long i)
:   atomic set with relaxed ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

`long i`
:   long value to assign

**Description**

Atomically sets **v** to **i** with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic_long_set()`](basics.md#c.atomic_long_set "atomic_long_set") elsewhere.

**Return**

Nothing.

void raw_atomic_long_set_release(atomic_long_t \*v, long i)
:   atomic set with release ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

`long i`
:   long value to assign

**Description**

Atomically sets **v** to **i** with release ordering.

Safe to use in noinstr code; prefer [`atomic_long_set_release()`](basics.md#c.atomic_long_set_release "atomic_long_set_release") elsewhere.

**Return**

Nothing.

void raw_atomic_long_add(long i, atomic_long_t \*v)
:   atomic add with relaxed ordering

**Parameters**

`long i`
:   long value to add

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** + **i**) with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic_long_add()`](basics.md#c.atomic_long_add "atomic_long_add") elsewhere.

**Return**

Nothing.

long raw_atomic_long_add_return(long i, atomic_long_t \*v)
:   atomic add with full ordering

**Parameters**

`long i`
:   long value to add

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** + **i**) with full ordering.

Safe to use in noinstr code; prefer [`atomic_long_add_return()`](basics.md#c.atomic_long_add_return "atomic_long_add_return") elsewhere.

**Return**

The updated value of **v**.

long raw_atomic_long_add_return_acquire(long i, atomic_long_t \*v)
:   atomic add with acquire ordering

**Parameters**

`long i`
:   long value to add

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** + **i**) with acquire ordering.

Safe to use in noinstr code; prefer [`atomic_long_add_return_acquire()`](basics.md#c.atomic_long_add_return_acquire "atomic_long_add_return_acquire") elsewhere.

**Return**

The updated value of **v**.

long raw_atomic_long_add_return_release(long i, atomic_long_t \*v)
:   atomic add with release ordering

**Parameters**

`long i`
:   long value to add

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** + **i**) with release ordering.

Safe to use in noinstr code; prefer [`atomic_long_add_return_release()`](basics.md#c.atomic_long_add_return_release "atomic_long_add_return_release") elsewhere.

**Return**

The updated value of **v**.

long raw_atomic_long_add_return_relaxed(long i, atomic_long_t \*v)
:   atomic add with relaxed ordering

**Parameters**

`long i`
:   long value to add

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** + **i**) with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic_long_add_return_relaxed()`](basics.md#c.atomic_long_add_return_relaxed "atomic_long_add_return_relaxed") elsewhere.

**Return**

The updated value of **v**.

long raw_atomic_long_fetch_add(long i, atomic_long_t \*v)
:   atomic add with full ordering

**Parameters**

`long i`
:   long value to add

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** + **i**) with full ordering.

Safe to use in noinstr code; prefer [`atomic_long_fetch_add()`](basics.md#c.atomic_long_fetch_add "atomic_long_fetch_add") elsewhere.

**Return**

The original value of **v**.

long raw_atomic_long_fetch_add_acquire(long i, atomic_long_t \*v)
:   atomic add with acquire ordering

**Parameters**

`long i`
:   long value to add

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** + **i**) with acquire ordering.

Safe to use in noinstr code; prefer [`atomic_long_fetch_add_acquire()`](basics.md#c.atomic_long_fetch_add_acquire "atomic_long_fetch_add_acquire") elsewhere.

**Return**

The original value of **v**.

long raw_atomic_long_fetch_add_release(long i, atomic_long_t \*v)
:   atomic add with release ordering

**Parameters**

`long i`
:   long value to add

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** + **i**) with release ordering.

Safe to use in noinstr code; prefer [`atomic_long_fetch_add_release()`](basics.md#c.atomic_long_fetch_add_release "atomic_long_fetch_add_release") elsewhere.

**Return**

The original value of **v**.

long raw_atomic_long_fetch_add_relaxed(long i, atomic_long_t \*v)
:   atomic add with relaxed ordering

**Parameters**

`long i`
:   long value to add

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** + **i**) with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic_long_fetch_add_relaxed()`](basics.md#c.atomic_long_fetch_add_relaxed "atomic_long_fetch_add_relaxed") elsewhere.

**Return**

The original value of **v**.

void raw_atomic_long_sub(long i, atomic_long_t \*v)
:   atomic subtract with relaxed ordering

**Parameters**

`long i`
:   long value to subtract

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** - **i**) with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic_long_sub()`](basics.md#c.atomic_long_sub "atomic_long_sub") elsewhere.

**Return**

Nothing.

long raw_atomic_long_sub_return(long i, atomic_long_t \*v)
:   atomic subtract with full ordering

**Parameters**

`long i`
:   long value to subtract

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** - **i**) with full ordering.

Safe to use in noinstr code; prefer [`atomic_long_sub_return()`](basics.md#c.atomic_long_sub_return "atomic_long_sub_return") elsewhere.

**Return**

The updated value of **v**.

long raw_atomic_long_sub_return_acquire(long i, atomic_long_t \*v)
:   atomic subtract with acquire ordering

**Parameters**

`long i`
:   long value to subtract

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** - **i**) with acquire ordering.

Safe to use in noinstr code; prefer [`atomic_long_sub_return_acquire()`](basics.md#c.atomic_long_sub_return_acquire "atomic_long_sub_return_acquire") elsewhere.

**Return**

The updated value of **v**.

long raw_atomic_long_sub_return_release(long i, atomic_long_t \*v)
:   atomic subtract with release ordering

**Parameters**

`long i`
:   long value to subtract

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** - **i**) with release ordering.

Safe to use in noinstr code; prefer [`atomic_long_sub_return_release()`](basics.md#c.atomic_long_sub_return_release "atomic_long_sub_return_release") elsewhere.

**Return**

The updated value of **v**.

long raw_atomic_long_sub_return_relaxed(long i, atomic_long_t \*v)
:   atomic subtract with relaxed ordering

**Parameters**

`long i`
:   long value to subtract

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** - **i**) with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic_long_sub_return_relaxed()`](basics.md#c.atomic_long_sub_return_relaxed "atomic_long_sub_return_relaxed") elsewhere.

**Return**

The updated value of **v**.

long raw_atomic_long_fetch_sub(long i, atomic_long_t \*v)
:   atomic subtract with full ordering

**Parameters**

`long i`
:   long value to subtract

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** - **i**) with full ordering.

Safe to use in noinstr code; prefer [`atomic_long_fetch_sub()`](basics.md#c.atomic_long_fetch_sub "atomic_long_fetch_sub") elsewhere.

**Return**

The original value of **v**.

long raw_atomic_long_fetch_sub_acquire(long i, atomic_long_t \*v)
:   atomic subtract with acquire ordering

**Parameters**

`long i`
:   long value to subtract

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** - **i**) with acquire ordering.

Safe to use in noinstr code; prefer [`atomic_long_fetch_sub_acquire()`](basics.md#c.atomic_long_fetch_sub_acquire "atomic_long_fetch_sub_acquire") elsewhere.

**Return**

The original value of **v**.

long raw_atomic_long_fetch_sub_release(long i, atomic_long_t \*v)
:   atomic subtract with release ordering

**Parameters**

`long i`
:   long value to subtract

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** - **i**) with release ordering.

Safe to use in noinstr code; prefer [`atomic_long_fetch_sub_release()`](basics.md#c.atomic_long_fetch_sub_release "atomic_long_fetch_sub_release") elsewhere.

**Return**

The original value of **v**.

long raw_atomic_long_fetch_sub_relaxed(long i, atomic_long_t \*v)
:   atomic subtract with relaxed ordering

**Parameters**

`long i`
:   long value to subtract

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** - **i**) with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic_long_fetch_sub_relaxed()`](basics.md#c.atomic_long_fetch_sub_relaxed "atomic_long_fetch_sub_relaxed") elsewhere.

**Return**

The original value of **v**.

void raw_atomic_long_inc(atomic_long_t \*v)
:   atomic increment with relaxed ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** + 1) with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic_long_inc()`](basics.md#c.atomic_long_inc "atomic_long_inc") elsewhere.

**Return**

Nothing.

long raw_atomic_long_inc_return(atomic_long_t \*v)
:   atomic increment with full ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** + 1) with full ordering.

Safe to use in noinstr code; prefer [`atomic_long_inc_return()`](basics.md#c.atomic_long_inc_return "atomic_long_inc_return") elsewhere.

**Return**

The updated value of **v**.

long raw_atomic_long_inc_return_acquire(atomic_long_t \*v)
:   atomic increment with acquire ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** + 1) with acquire ordering.

Safe to use in noinstr code; prefer [`atomic_long_inc_return_acquire()`](basics.md#c.atomic_long_inc_return_acquire "atomic_long_inc_return_acquire") elsewhere.

**Return**

The updated value of **v**.

long raw_atomic_long_inc_return_release(atomic_long_t \*v)
:   atomic increment with release ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** + 1) with release ordering.

Safe to use in noinstr code; prefer [`atomic_long_inc_return_release()`](basics.md#c.atomic_long_inc_return_release "atomic_long_inc_return_release") elsewhere.

**Return**

The updated value of **v**.

long raw_atomic_long_inc_return_relaxed(atomic_long_t \*v)
:   atomic increment with relaxed ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** + 1) with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic_long_inc_return_relaxed()`](basics.md#c.atomic_long_inc_return_relaxed "atomic_long_inc_return_relaxed") elsewhere.

**Return**

The updated value of **v**.

long raw_atomic_long_fetch_inc(atomic_long_t \*v)
:   atomic increment with full ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** + 1) with full ordering.

Safe to use in noinstr code; prefer [`atomic_long_fetch_inc()`](basics.md#c.atomic_long_fetch_inc "atomic_long_fetch_inc") elsewhere.

**Return**

The original value of **v**.

long raw_atomic_long_fetch_inc_acquire(atomic_long_t \*v)
:   atomic increment with acquire ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** + 1) with acquire ordering.

Safe to use in noinstr code; prefer [`atomic_long_fetch_inc_acquire()`](basics.md#c.atomic_long_fetch_inc_acquire "atomic_long_fetch_inc_acquire") elsewhere.

**Return**

The original value of **v**.

long raw_atomic_long_fetch_inc_release(atomic_long_t \*v)
:   atomic increment with release ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** + 1) with release ordering.

Safe to use in noinstr code; prefer [`atomic_long_fetch_inc_release()`](basics.md#c.atomic_long_fetch_inc_release "atomic_long_fetch_inc_release") elsewhere.

**Return**

The original value of **v**.

long raw_atomic_long_fetch_inc_relaxed(atomic_long_t \*v)
:   atomic increment with relaxed ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** + 1) with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic_long_fetch_inc_relaxed()`](basics.md#c.atomic_long_fetch_inc_relaxed "atomic_long_fetch_inc_relaxed") elsewhere.

**Return**

The original value of **v**.

void raw_atomic_long_dec(atomic_long_t \*v)
:   atomic decrement with relaxed ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** - 1) with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic_long_dec()`](basics.md#c.atomic_long_dec "atomic_long_dec") elsewhere.

**Return**

Nothing.

long raw_atomic_long_dec_return(atomic_long_t \*v)
:   atomic decrement with full ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** - 1) with full ordering.

Safe to use in noinstr code; prefer [`atomic_long_dec_return()`](basics.md#c.atomic_long_dec_return "atomic_long_dec_return") elsewhere.

**Return**

The updated value of **v**.

long raw_atomic_long_dec_return_acquire(atomic_long_t \*v)
:   atomic decrement with acquire ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** - 1) with acquire ordering.

Safe to use in noinstr code; prefer [`atomic_long_dec_return_acquire()`](basics.md#c.atomic_long_dec_return_acquire "atomic_long_dec_return_acquire") elsewhere.

**Return**

The updated value of **v**.

long raw_atomic_long_dec_return_release(atomic_long_t \*v)
:   atomic decrement with release ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** - 1) with release ordering.

Safe to use in noinstr code; prefer [`atomic_long_dec_return_release()`](basics.md#c.atomic_long_dec_return_release "atomic_long_dec_return_release") elsewhere.

**Return**

The updated value of **v**.

long raw_atomic_long_dec_return_relaxed(atomic_long_t \*v)
:   atomic decrement with relaxed ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** - 1) with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic_long_dec_return_relaxed()`](basics.md#c.atomic_long_dec_return_relaxed "atomic_long_dec_return_relaxed") elsewhere.

**Return**

The updated value of **v**.

long raw_atomic_long_fetch_dec(atomic_long_t \*v)
:   atomic decrement with full ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** - 1) with full ordering.

Safe to use in noinstr code; prefer [`atomic_long_fetch_dec()`](basics.md#c.atomic_long_fetch_dec "atomic_long_fetch_dec") elsewhere.

**Return**

The original value of **v**.

long raw_atomic_long_fetch_dec_acquire(atomic_long_t \*v)
:   atomic decrement with acquire ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** - 1) with acquire ordering.

Safe to use in noinstr code; prefer [`atomic_long_fetch_dec_acquire()`](basics.md#c.atomic_long_fetch_dec_acquire "atomic_long_fetch_dec_acquire") elsewhere.

**Return**

The original value of **v**.

long raw_atomic_long_fetch_dec_release(atomic_long_t \*v)
:   atomic decrement with release ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** - 1) with release ordering.

Safe to use in noinstr code; prefer [`atomic_long_fetch_dec_release()`](basics.md#c.atomic_long_fetch_dec_release "atomic_long_fetch_dec_release") elsewhere.

**Return**

The original value of **v**.

long raw_atomic_long_fetch_dec_relaxed(atomic_long_t \*v)
:   atomic decrement with relaxed ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** - 1) with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic_long_fetch_dec_relaxed()`](basics.md#c.atomic_long_fetch_dec_relaxed "atomic_long_fetch_dec_relaxed") elsewhere.

**Return**

The original value of **v**.

void raw_atomic_long_and(long i, atomic_long_t \*v)
:   atomic bitwise AND with relaxed ordering

**Parameters**

`long i`
:   long value

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** & **i**) with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic_long_and()`](basics.md#c.atomic_long_and "atomic_long_and") elsewhere.

**Return**

Nothing.

long raw_atomic_long_fetch_and(long i, atomic_long_t \*v)
:   atomic bitwise AND with full ordering

**Parameters**

`long i`
:   long value

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** & **i**) with full ordering.

Safe to use in noinstr code; prefer [`atomic_long_fetch_and()`](basics.md#c.atomic_long_fetch_and "atomic_long_fetch_and") elsewhere.

**Return**

The original value of **v**.

long raw_atomic_long_fetch_and_acquire(long i, atomic_long_t \*v)
:   atomic bitwise AND with acquire ordering

**Parameters**

`long i`
:   long value

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** & **i**) with acquire ordering.

Safe to use in noinstr code; prefer [`atomic_long_fetch_and_acquire()`](basics.md#c.atomic_long_fetch_and_acquire "atomic_long_fetch_and_acquire") elsewhere.

**Return**

The original value of **v**.

long raw_atomic_long_fetch_and_release(long i, atomic_long_t \*v)
:   atomic bitwise AND with release ordering

**Parameters**

`long i`
:   long value

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** & **i**) with release ordering.

Safe to use in noinstr code; prefer [`atomic_long_fetch_and_release()`](basics.md#c.atomic_long_fetch_and_release "atomic_long_fetch_and_release") elsewhere.

**Return**

The original value of **v**.

long raw_atomic_long_fetch_and_relaxed(long i, atomic_long_t \*v)
:   atomic bitwise AND with relaxed ordering

**Parameters**

`long i`
:   long value

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** & **i**) with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic_long_fetch_and_relaxed()`](basics.md#c.atomic_long_fetch_and_relaxed "atomic_long_fetch_and_relaxed") elsewhere.

**Return**

The original value of **v**.

void raw_atomic_long_andnot(long i, atomic_long_t \*v)
:   atomic bitwise AND NOT with relaxed ordering

**Parameters**

`long i`
:   long value

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** & **~i**) with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic_long_andnot()`](basics.md#c.atomic_long_andnot "atomic_long_andnot") elsewhere.

**Return**

Nothing.

long raw_atomic_long_fetch_andnot(long i, atomic_long_t \*v)
:   atomic bitwise AND NOT with full ordering

**Parameters**

`long i`
:   long value

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** & **~i**) with full ordering.

Safe to use in noinstr code; prefer [`atomic_long_fetch_andnot()`](basics.md#c.atomic_long_fetch_andnot "atomic_long_fetch_andnot") elsewhere.

**Return**

The original value of **v**.

long raw_atomic_long_fetch_andnot_acquire(long i, atomic_long_t \*v)
:   atomic bitwise AND NOT with acquire ordering

**Parameters**

`long i`
:   long value

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** & **~i**) with acquire ordering.

Safe to use in noinstr code; prefer [`atomic_long_fetch_andnot_acquire()`](basics.md#c.atomic_long_fetch_andnot_acquire "atomic_long_fetch_andnot_acquire") elsewhere.

**Return**

The original value of **v**.

long raw_atomic_long_fetch_andnot_release(long i, atomic_long_t \*v)
:   atomic bitwise AND NOT with release ordering

**Parameters**

`long i`
:   long value

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** & **~i**) with release ordering.

Safe to use in noinstr code; prefer [`atomic_long_fetch_andnot_release()`](basics.md#c.atomic_long_fetch_andnot_release "atomic_long_fetch_andnot_release") elsewhere.

**Return**

The original value of **v**.

long raw_atomic_long_fetch_andnot_relaxed(long i, atomic_long_t \*v)
:   atomic bitwise AND NOT with relaxed ordering

**Parameters**

`long i`
:   long value

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** & **~i**) with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic_long_fetch_andnot_relaxed()`](basics.md#c.atomic_long_fetch_andnot_relaxed "atomic_long_fetch_andnot_relaxed") elsewhere.

**Return**

The original value of **v**.

void raw_atomic_long_or(long i, atomic_long_t \*v)
:   atomic bitwise OR with relaxed ordering

**Parameters**

`long i`
:   long value

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** | **i**) with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic_long_or()`](basics.md#c.atomic_long_or "atomic_long_or") elsewhere.

**Return**

Nothing.

long raw_atomic_long_fetch_or(long i, atomic_long_t \*v)
:   atomic bitwise OR with full ordering

**Parameters**

`long i`
:   long value

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** | **i**) with full ordering.

Safe to use in noinstr code; prefer [`atomic_long_fetch_or()`](basics.md#c.atomic_long_fetch_or "atomic_long_fetch_or") elsewhere.

**Return**

The original value of **v**.

long raw_atomic_long_fetch_or_acquire(long i, atomic_long_t \*v)
:   atomic bitwise OR with acquire ordering

**Parameters**

`long i`
:   long value

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** | **i**) with acquire ordering.

Safe to use in noinstr code; prefer [`atomic_long_fetch_or_acquire()`](basics.md#c.atomic_long_fetch_or_acquire "atomic_long_fetch_or_acquire") elsewhere.

**Return**

The original value of **v**.

long raw_atomic_long_fetch_or_release(long i, atomic_long_t \*v)
:   atomic bitwise OR with release ordering

**Parameters**

`long i`
:   long value

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** | **i**) with release ordering.

Safe to use in noinstr code; prefer [`atomic_long_fetch_or_release()`](basics.md#c.atomic_long_fetch_or_release "atomic_long_fetch_or_release") elsewhere.

**Return**

The original value of **v**.

long raw_atomic_long_fetch_or_relaxed(long i, atomic_long_t \*v)
:   atomic bitwise OR with relaxed ordering

**Parameters**

`long i`
:   long value

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** | **i**) with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic_long_fetch_or_relaxed()`](basics.md#c.atomic_long_fetch_or_relaxed "atomic_long_fetch_or_relaxed") elsewhere.

**Return**

The original value of **v**.

void raw_atomic_long_xor(long i, atomic_long_t \*v)
:   atomic bitwise XOR with relaxed ordering

**Parameters**

`long i`
:   long value

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** ^ **i**) with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic_long_xor()`](basics.md#c.atomic_long_xor "atomic_long_xor") elsewhere.

**Return**

Nothing.

long raw_atomic_long_fetch_xor(long i, atomic_long_t \*v)
:   atomic bitwise XOR with full ordering

**Parameters**

`long i`
:   long value

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** ^ **i**) with full ordering.

Safe to use in noinstr code; prefer [`atomic_long_fetch_xor()`](basics.md#c.atomic_long_fetch_xor "atomic_long_fetch_xor") elsewhere.

**Return**

The original value of **v**.

long raw_atomic_long_fetch_xor_acquire(long i, atomic_long_t \*v)
:   atomic bitwise XOR with acquire ordering

**Parameters**

`long i`
:   long value

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** ^ **i**) with acquire ordering.

Safe to use in noinstr code; prefer [`atomic_long_fetch_xor_acquire()`](basics.md#c.atomic_long_fetch_xor_acquire "atomic_long_fetch_xor_acquire") elsewhere.

**Return**

The original value of **v**.

long raw_atomic_long_fetch_xor_release(long i, atomic_long_t \*v)
:   atomic bitwise XOR with release ordering

**Parameters**

`long i`
:   long value

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** ^ **i**) with release ordering.

Safe to use in noinstr code; prefer [`atomic_long_fetch_xor_release()`](basics.md#c.atomic_long_fetch_xor_release "atomic_long_fetch_xor_release") elsewhere.

**Return**

The original value of **v**.

long raw_atomic_long_fetch_xor_relaxed(long i, atomic_long_t \*v)
:   atomic bitwise XOR with relaxed ordering

**Parameters**

`long i`
:   long value

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** ^ **i**) with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic_long_fetch_xor_relaxed()`](basics.md#c.atomic_long_fetch_xor_relaxed "atomic_long_fetch_xor_relaxed") elsewhere.

**Return**

The original value of **v**.

long raw_atomic_long_xchg(atomic_long_t \*v, long new)
:   atomic exchange with full ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

`long new`
:   long value to assign

**Description**

Atomically updates **v** to **new** with full ordering.

Safe to use in noinstr code; prefer [`atomic_long_xchg()`](basics.md#c.atomic_long_xchg "atomic_long_xchg") elsewhere.

**Return**

The original value of **v**.

long raw_atomic_long_xchg_acquire(atomic_long_t \*v, long new)
:   atomic exchange with acquire ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

`long new`
:   long value to assign

**Description**

Atomically updates **v** to **new** with acquire ordering.

Safe to use in noinstr code; prefer [`atomic_long_xchg_acquire()`](basics.md#c.atomic_long_xchg_acquire "atomic_long_xchg_acquire") elsewhere.

**Return**

The original value of **v**.

long raw_atomic_long_xchg_release(atomic_long_t \*v, long new)
:   atomic exchange with release ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

`long new`
:   long value to assign

**Description**

Atomically updates **v** to **new** with release ordering.

Safe to use in noinstr code; prefer [`atomic_long_xchg_release()`](basics.md#c.atomic_long_xchg_release "atomic_long_xchg_release") elsewhere.

**Return**

The original value of **v**.

long raw_atomic_long_xchg_relaxed(atomic_long_t \*v, long new)
:   atomic exchange with relaxed ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

`long new`
:   long value to assign

**Description**

Atomically updates **v** to **new** with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic_long_xchg_relaxed()`](basics.md#c.atomic_long_xchg_relaxed "atomic_long_xchg_relaxed") elsewhere.

**Return**

The original value of **v**.

long raw_atomic_long_cmpxchg(atomic_long_t \*v, long old, long new)
:   atomic compare and exchange with full ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

`long old`
:   long value to compare with

`long new`
:   long value to assign

**Description**

If (**v** == **old**), atomically updates **v** to **new** with full ordering.

Safe to use in noinstr code; prefer [`atomic_long_cmpxchg()`](basics.md#c.atomic_long_cmpxchg "atomic_long_cmpxchg") elsewhere.

**Return**

The original value of **v**.

long raw_atomic_long_cmpxchg_acquire(atomic_long_t \*v, long old, long new)
:   atomic compare and exchange with acquire ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

`long old`
:   long value to compare with

`long new`
:   long value to assign

**Description**

If (**v** == **old**), atomically updates **v** to **new** with acquire ordering.

Safe to use in noinstr code; prefer [`atomic_long_cmpxchg_acquire()`](basics.md#c.atomic_long_cmpxchg_acquire "atomic_long_cmpxchg_acquire") elsewhere.

**Return**

The original value of **v**.

long raw_atomic_long_cmpxchg_release(atomic_long_t \*v, long old, long new)
:   atomic compare and exchange with release ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

`long old`
:   long value to compare with

`long new`
:   long value to assign

**Description**

If (**v** == **old**), atomically updates **v** to **new** with release ordering.

Safe to use in noinstr code; prefer [`atomic_long_cmpxchg_release()`](basics.md#c.atomic_long_cmpxchg_release "atomic_long_cmpxchg_release") elsewhere.

**Return**

The original value of **v**.

long raw_atomic_long_cmpxchg_relaxed(atomic_long_t \*v, long old, long new)
:   atomic compare and exchange with relaxed ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

`long old`
:   long value to compare with

`long new`
:   long value to assign

**Description**

If (**v** == **old**), atomically updates **v** to **new** with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic_long_cmpxchg_relaxed()`](basics.md#c.atomic_long_cmpxchg_relaxed "atomic_long_cmpxchg_relaxed") elsewhere.

**Return**

The original value of **v**.

bool raw_atomic_long_try_cmpxchg(atomic_long_t \*v, long \*old, long new)
:   atomic compare and exchange with full ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

`long *old`
:   pointer to long value to compare with

`long new`
:   long value to assign

**Description**

If (**v** == **old**), atomically updates **v** to **new** with full ordering.
Otherwise, updates **old** to the current value of **v**.

Safe to use in noinstr code; prefer [`atomic_long_try_cmpxchg()`](basics.md#c.atomic_long_try_cmpxchg "atomic_long_try_cmpxchg") elsewhere.

**Return**

**true** if the exchange occured, **false** otherwise.

bool raw_atomic_long_try_cmpxchg_acquire(atomic_long_t \*v, long \*old, long new)
:   atomic compare and exchange with acquire ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

`long *old`
:   pointer to long value to compare with

`long new`
:   long value to assign

**Description**

If (**v** == **old**), atomically updates **v** to **new** with acquire ordering.
Otherwise, updates **old** to the current value of **v**.

Safe to use in noinstr code; prefer [`atomic_long_try_cmpxchg_acquire()`](basics.md#c.atomic_long_try_cmpxchg_acquire "atomic_long_try_cmpxchg_acquire") elsewhere.

**Return**

**true** if the exchange occured, **false** otherwise.

bool raw_atomic_long_try_cmpxchg_release(atomic_long_t \*v, long \*old, long new)
:   atomic compare and exchange with release ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

`long *old`
:   pointer to long value to compare with

`long new`
:   long value to assign

**Description**

If (**v** == **old**), atomically updates **v** to **new** with release ordering.
Otherwise, updates **old** to the current value of **v**.

Safe to use in noinstr code; prefer [`atomic_long_try_cmpxchg_release()`](basics.md#c.atomic_long_try_cmpxchg_release "atomic_long_try_cmpxchg_release") elsewhere.

**Return**

**true** if the exchange occured, **false** otherwise.

bool raw_atomic_long_try_cmpxchg_relaxed(atomic_long_t \*v, long \*old, long new)
:   atomic compare and exchange with relaxed ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

`long *old`
:   pointer to long value to compare with

`long new`
:   long value to assign

**Description**

If (**v** == **old**), atomically updates **v** to **new** with relaxed ordering.
Otherwise, updates **old** to the current value of **v**.

Safe to use in noinstr code; prefer [`atomic_long_try_cmpxchg_relaxed()`](basics.md#c.atomic_long_try_cmpxchg_relaxed "atomic_long_try_cmpxchg_relaxed") elsewhere.

**Return**

**true** if the exchange occured, **false** otherwise.

bool raw_atomic_long_sub_and_test(long i, atomic_long_t \*v)
:   atomic subtract and test if zero with full ordering

**Parameters**

`long i`
:   long value to add

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** - **i**) with full ordering.

Safe to use in noinstr code; prefer [`atomic_long_sub_and_test()`](basics.md#c.atomic_long_sub_and_test "atomic_long_sub_and_test") elsewhere.

**Return**

**true** if the resulting value of **v** is zero, **false** otherwise.

bool raw_atomic_long_dec_and_test(atomic_long_t \*v)
:   atomic decrement and test if zero with full ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** - 1) with full ordering.

Safe to use in noinstr code; prefer [`atomic_long_dec_and_test()`](basics.md#c.atomic_long_dec_and_test "atomic_long_dec_and_test") elsewhere.

**Return**

**true** if the resulting value of **v** is zero, **false** otherwise.

bool raw_atomic_long_inc_and_test(atomic_long_t \*v)
:   atomic increment and test if zero with full ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** + 1) with full ordering.

Safe to use in noinstr code; prefer [`atomic_long_inc_and_test()`](basics.md#c.atomic_long_inc_and_test "atomic_long_inc_and_test") elsewhere.

**Return**

**true** if the resulting value of **v** is zero, **false** otherwise.

bool raw_atomic_long_add_negative(long i, atomic_long_t \*v)
:   atomic add and test if negative with full ordering

**Parameters**

`long i`
:   long value to add

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** + **i**) with full ordering.

Safe to use in noinstr code; prefer [`atomic_long_add_negative()`](basics.md#c.atomic_long_add_negative "atomic_long_add_negative") elsewhere.

**Return**

**true** if the resulting value of **v** is negative, **false** otherwise.

bool raw_atomic_long_add_negative_acquire(long i, atomic_long_t \*v)
:   atomic add and test if negative with acquire ordering

**Parameters**

`long i`
:   long value to add

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** + **i**) with acquire ordering.

Safe to use in noinstr code; prefer [`atomic_long_add_negative_acquire()`](basics.md#c.atomic_long_add_negative_acquire "atomic_long_add_negative_acquire") elsewhere.

**Return**

**true** if the resulting value of **v** is negative, **false** otherwise.

bool raw_atomic_long_add_negative_release(long i, atomic_long_t \*v)
:   atomic add and test if negative with release ordering

**Parameters**

`long i`
:   long value to add

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** + **i**) with release ordering.

Safe to use in noinstr code; prefer [`atomic_long_add_negative_release()`](basics.md#c.atomic_long_add_negative_release "atomic_long_add_negative_release") elsewhere.

**Return**

**true** if the resulting value of **v** is negative, **false** otherwise.

bool raw_atomic_long_add_negative_relaxed(long i, atomic_long_t \*v)
:   atomic add and test if negative with relaxed ordering

**Parameters**

`long i`
:   long value to add

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

Atomically updates **v** to (**v** + **i**) with relaxed ordering.

Safe to use in noinstr code; prefer [`atomic_long_add_negative_relaxed()`](basics.md#c.atomic_long_add_negative_relaxed "atomic_long_add_negative_relaxed") elsewhere.

**Return**

**true** if the resulting value of **v** is negative, **false** otherwise.

long raw_atomic_long_fetch_add_unless(atomic_long_t \*v, long a, long u)
:   atomic add unless value with full ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

`long a`
:   long value to add

`long u`
:   long value to compare with

**Description**

If (**v** != **u**), atomically updates **v** to (**v** + **a**) with full ordering.

Safe to use in noinstr code; prefer [`atomic_long_fetch_add_unless()`](basics.md#c.atomic_long_fetch_add_unless "atomic_long_fetch_add_unless") elsewhere.

**Return**

The original value of **v**.

bool raw_atomic_long_add_unless(atomic_long_t \*v, long a, long u)
:   atomic add unless value with full ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

`long a`
:   long value to add

`long u`
:   long value to compare with

**Description**

If (**v** != **u**), atomically updates **v** to (**v** + **a**) with full ordering.

Safe to use in noinstr code; prefer [`atomic_long_add_unless()`](basics.md#c.atomic_long_add_unless "atomic_long_add_unless") elsewhere.

**Return**

**true** if **v** was updated, **false** otherwise.

bool raw_atomic_long_inc_not_zero(atomic_long_t \*v)
:   atomic increment unless zero with full ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

If (**v** != 0), atomically updates **v** to (**v** + 1) with full ordering.

Safe to use in noinstr code; prefer [`atomic_long_inc_not_zero()`](basics.md#c.atomic_long_inc_not_zero "atomic_long_inc_not_zero") elsewhere.

**Return**

**true** if **v** was updated, **false** otherwise.

bool raw_atomic_long_inc_unless_negative(atomic_long_t \*v)
:   atomic increment unless negative with full ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

If (**v** >= 0), atomically updates **v** to (**v** + 1) with full ordering.

Safe to use in noinstr code; prefer [`atomic_long_inc_unless_negative()`](basics.md#c.atomic_long_inc_unless_negative "atomic_long_inc_unless_negative") elsewhere.

**Return**

**true** if **v** was updated, **false** otherwise.

bool raw_atomic_long_dec_unless_positive(atomic_long_t \*v)
:   atomic decrement unless positive with full ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

If (**v** <= 0), atomically updates **v** to (**v** - 1) with full ordering.

Safe to use in noinstr code; prefer [`atomic_long_dec_unless_positive()`](basics.md#c.atomic_long_dec_unless_positive "atomic_long_dec_unless_positive") elsewhere.

**Return**

**true** if **v** was updated, **false** otherwise.

long raw_atomic_long_dec_if_positive(atomic_long_t \*v)
:   atomic decrement if positive with full ordering

**Parameters**

`atomic_long_t *v`
:   pointer to atomic_long_t

**Description**

If (**v** > 0), atomically updates **v** to (**v** - 1) with full ordering.

Safe to use in noinstr code; prefer [`atomic_long_dec_if_positive()`](basics.md#c.atomic_long_dec_if_positive "atomic_long_dec_if_positive") elsewhere.

**Return**

The old value of (**v** - 1), regardless of whether **v** was updated.

## Kernel objects manipulation

char \*kobject_get_path(const struct kobject \*kobj, gfp_t gfp_mask)
:   Allocate memory and fill in the path for **kobj**.

**Parameters**

`const struct kobject *kobj`
:   kobject in question, with which to build the path

`gfp_t gfp_mask`
:   the allocation type used to allocate the path

**Return**

The newly allocated memory, caller must free with [`kfree()`](../core-api/mm-api.md#c.kfree "kfree").

int kobject_set_name(struct kobject \*kobj, const char \*fmt, ...)
:   Set the name of a kobject.

**Parameters**

`struct kobject *kobj`
:   struct kobject to set the name of

`const char *fmt`
:   format string used to build the name

`...`
:   variable arguments

**Description**

This sets the name of the kobject. If you have already added the
kobject to the system, you must call [`kobject_rename()`](basics.md#c.kobject_rename "kobject_rename") in order to
change the name of the kobject.

void kobject_init(struct kobject \*kobj, const struct kobj_type \*ktype)
:   Initialize a kobject structure.

**Parameters**

`struct kobject *kobj`
:   pointer to the kobject to initialize

`const struct kobj_type *ktype`
:   pointer to the ktype for this kobject.

**Description**

This function will properly initialize a kobject such that it can then
be passed to the [`kobject_add()`](basics.md#c.kobject_add "kobject_add") call.

After this function is called, the kobject MUST be cleaned up by a call
to [`kobject_put()`](basics.md#c.kobject_put "kobject_put"), not by a call to kfree directly to ensure that all of
the memory is cleaned up properly.

int kobject_add(struct kobject \*kobj, struct kobject \*parent, const char \*fmt, ...)
:   The main kobject add function.

**Parameters**

`struct kobject *kobj`
:   the kobject to add

`struct kobject *parent`
:   pointer to the parent of the kobject.

`const char *fmt`
:   format to name the kobject with.

`...`
:   variable arguments

**Description**

The kobject name is set and added to the kobject hierarchy in this
function.

If **parent** is set, then the parent of the **kobj** will be set to it.
If **parent** is NULL, then the parent of the **kobj** will be set to the
kobject associated with the kset assigned to this kobject. If no kset
is assigned to the kobject, then the kobject will be located in the
root of the sysfs tree.

Note, no "add" uevent will be created with this call, the caller should set
up all of the necessary sysfs files for the object and then call
kobject_uevent() with the UEVENT_ADD parameter to ensure that
userspace is properly notified of this kobject's creation.

**Return**

If this function returns an error, kobject_put() must be
:   called to properly clean up the memory associated with the
    object. Under no instance should the kobject that is passed
    to this function be directly freed with a call to [`kfree()`](../core-api/mm-api.md#c.kfree "kfree"),
    that can leak memory.

    If this function returns success, [`kobject_put()`](basics.md#c.kobject_put "kobject_put") must also be called
    in order to properly clean up the memory associated with the object.

    In short, once this function is called, [`kobject_put()`](basics.md#c.kobject_put "kobject_put") MUST be called
    when the use of the object is finished in order to properly free
    everything.

int kobject_init_and_add(struct kobject \*kobj, const struct kobj_type \*ktype, struct kobject \*parent, const char \*fmt, ...)
:   Initialize a kobject structure and add it to the kobject hierarchy.

**Parameters**

`struct kobject *kobj`
:   pointer to the kobject to initialize

`const struct kobj_type *ktype`
:   pointer to the ktype for this kobject.

`struct kobject *parent`
:   pointer to the parent of this kobject.

`const char *fmt`
:   the name of the kobject.

`...`
:   variable arguments

**Description**

This function combines the call to [`kobject_init()`](basics.md#c.kobject_init "kobject_init") and [`kobject_add()`](basics.md#c.kobject_add "kobject_add").

If this function returns an error, [`kobject_put()`](basics.md#c.kobject_put "kobject_put") must be called to
properly clean up the memory associated with the object. This is the
same type of error handling after a call to [`kobject_add()`](basics.md#c.kobject_add "kobject_add") and kobject
lifetime rules are the same here.

int kobject_rename(struct kobject \*kobj, const char \*new_name)
:   Change the name of an object.

**Parameters**

`struct kobject *kobj`
:   object in question.

`const char *new_name`
:   object's new name

**Description**

It is the responsibility of the caller to provide mutual
exclusion between two different calls of kobject_rename
on the same kobject and to ensure that new_name is valid and
won't conflict with other kobjects.

int kobject_move(struct kobject \*kobj, struct kobject \*new_parent)
:   Move object to another parent.

**Parameters**

`struct kobject *kobj`
:   object in question.

`struct kobject *new_parent`
:   object's new parent (can be NULL)

void kobject_del(struct kobject \*kobj)
:   Unlink kobject from hierarchy.

**Parameters**

`struct kobject *kobj`
:   object.

**Description**

This is the function that should be called to delete an object
successfully added via [`kobject_add()`](basics.md#c.kobject_add "kobject_add").

struct kobject \*kobject_get(struct kobject \*kobj)
:   Increment refcount for object.

**Parameters**

`struct kobject *kobj`
:   object.

void kobject_put(struct kobject \*kobj)
:   Decrement refcount for object.

**Parameters**

`struct kobject *kobj`
:   object.

**Description**

Decrement the refcount, and if 0, call kobject_cleanup().

struct kobject \*kobject_create_and_add(const char \*name, struct kobject \*parent)
:   Create a struct kobject dynamically and register it with sysfs.

**Parameters**

`const char *name`
:   the name for the kobject

`struct kobject *parent`
:   the parent kobject of this kobject, if any.

**Description**

This function creates a kobject structure dynamically and registers it
with sysfs. When you are finished with this structure, call
[`kobject_put()`](basics.md#c.kobject_put "kobject_put") and the structure will be dynamically freed when
it is no longer being used.

If the kobject was not able to be created, NULL will be returned.

int kset_register(struct kset \*k)
:   Initialize and add a kset.

**Parameters**

`struct kset *k`
:   kset.

**NOTE**

On error, the kset.kobj.name allocated by() kobj_set_name()
is freed, it can not be used any more.

void kset_unregister(struct kset \*k)
:   Remove a kset.

**Parameters**

`struct kset *k`
:   kset.

struct kobject \*kset_find_obj(struct [kset](basics.md#c.kset_find_obj "kset") \*kset, const char \*name)
:   Search for object in kset.

**Parameters**

`struct kset *kset`
:   kset we're looking in.

`const char *name`
:   object's name.

**Description**

Lock kset via **kset->subsys**, and iterate over **kset->list**,
looking for a matching kobject. If matching object is found
take a reference and return the object.

struct kset \*kset_create_and_add(const char \*name, const struct kset_uevent_ops \*uevent_ops, struct kobject \*parent_kobj)
:   Create a struct kset dynamically and add it to sysfs.

**Parameters**

`const char *name`
:   the name for the kset

`const struct kset_uevent_ops *uevent_ops`
:   a struct kset_uevent_ops for the kset

`struct kobject *parent_kobj`
:   the parent kobject of this kset, if any.

**Description**

This function creates a kset structure dynamically and registers it
with sysfs. When you are finished with this structure, call
[`kset_unregister()`](basics.md#c.kset_unregister "kset_unregister") and the structure will be dynamically freed when it
is no longer being used.

If the kset was not able to be created, NULL will be returned.

## Kernel utility functions

REPEAT_BYTE

`REPEAT_BYTE (x)`

> repeat the value **x** multiple times as an unsigned long value

**Parameters**

`x`
:   value to repeat

**NOTE**

**x** is not checked for > 0xff; larger values produce odd results.

upper_32_bits

`upper_32_bits (n)`

> return bits 32-63 of a number

**Parameters**

`n`
:   the number we're accessing

**Description**

A basic shift-right of a 64- or 32-bit quantity. Use this to suppress
the "right shift count >= width of type" warning when that quantity is
32-bits.

lower_32_bits

`lower_32_bits (n)`

> return bits 0-31 of a number

**Parameters**

`n`
:   the number we're accessing

upper_16_bits

`upper_16_bits (n)`

> return bits 16-31 of a number

**Parameters**

`n`
:   the number we're accessing

lower_16_bits

`lower_16_bits (n)`

> return bits 0-15 of a number

**Parameters**

`n`
:   the number we're accessing

might_sleep

`might_sleep ()`

> annotation for functions that can sleep

**Parameters**

**Description**

this macro will print a stack trace if it is executed in an atomic
context (spinlock, irq-handler, ...). Additional sections where blocking is
not allowed can be annotated with [`non_block_start()`](basics.md#c.non_block_start "non_block_start") and [`non_block_end()`](basics.md#c.non_block_end "non_block_end")
pairs.

This is a useful debugging help to be able to catch problems early and not
be bitten later when the calling function happens to sleep when it is not
supposed to.

cant_sleep

`cant_sleep ()`

> annotation for functions that cannot sleep

**Parameters**

**Description**

this macro will print a stack trace if it is executed with preemption enabled

cant_migrate

`cant_migrate ()`

> annotation for functions that cannot migrate

**Parameters**

**Description**

Will print a stack trace if executed in code which is migratable

non_block_start

`non_block_start ()`

> annotate the start of section where sleeping is prohibited

**Parameters**

**Description**

This is on behalf of the oom reaper, specifically when it is calling the mmu
notifiers. The problem is that if the notifier were to block on, for example,
[`mutex_lock()`](../kernel-hacking/locking.md#c.mutex_lock "mutex_lock") and if the process which holds that mutex were to perform a
sleeping memory allocation, the oom reaper is now blocked on completion of
that memory allocation. Other blocking calls like [`wait_event()`](basics.md#c.wait_event "wait_event") pose similar
issues.

non_block_end

`non_block_end ()`

> annotate the end of section where sleeping is prohibited

**Parameters**

**Description**

Closes a section opened by [`non_block_start()`](basics.md#c.non_block_start "non_block_start").

trace_printk

`trace_printk (fmt, ...)`

> printf formatting in the ftrace buffer

**Parameters**

`fmt`
:   the printf format for printing

`...`
:   variable arguments

**Note**

__trace_printk is an internal function for trace_printk() and
:   the **ip** is passed in via the [`trace_printk()`](basics.md#c.trace_printk "trace_printk") macro.

**Description**

This function allows a kernel developer to debug fast path sections
that printk is not appropriate for. By scattering in various
printk like tracing in the code, a developer can quickly see
where problems are occurring.

This is intended as a debugging tool for the developer only.
Please refrain from leaving trace_printks scattered around in
your code. (Extra memory is used for special buffers that are
allocated when [`trace_printk()`](basics.md#c.trace_printk "trace_printk") is used.)

A little optimization trick is done here. If there's only one
argument, there's no need to scan the string for printf formats.
The [`trace_puts()`](basics.md#c.trace_puts "trace_puts") will suffice. But how can we take advantage of
using [`trace_puts()`](basics.md#c.trace_puts "trace_puts") when [`trace_printk()`](basics.md#c.trace_printk "trace_printk") has only one argument?
By stringifying the args and checking the size we can tell
whether or not there are args. __stringify((__VA_ARGS__)) will
turn into "()0" with a size of 3 when there are no args, anything
else will be bigger. All we need to do is define a string to this,
and then take its size and compare to 3. If it's bigger, use
do_trace_printk() otherwise, optimize it to [`trace_puts()`](basics.md#c.trace_puts "trace_puts"). Then just
let gcc optimize the rest.

trace_puts

`trace_puts (str)`

> write a string into the ftrace buffer

**Parameters**

`str`
:   the string to record

**Note**

__trace_bputs is an internal function for trace_puts and
:   the **ip** is passed in via the trace_puts macro.

**Description**

This is similar to [`trace_printk()`](basics.md#c.trace_printk "trace_printk") but is made for those really fast
paths that a developer wants the least amount of "Heisenbug" effects,
where the processing of the print format is still too much.

This function allows a kernel developer to debug fast path sections
that printk is not appropriate for. By scattering in various
printk like tracing in the code, a developer can quickly see
where problems are occurring.

This is intended as a debugging tool for the developer only.
Please refrain from leaving trace_puts scattered around in
your code. (Extra memory is used for special buffers that are
allocated when [`trace_puts()`](basics.md#c.trace_puts "trace_puts") is used.)

**Return**

0 if nothing was written, positive # if string was.
:   (1 when __trace_bputs is used, strlen(str) when __trace_puts is used)

void console_list_lock(void)
:   Lock the console list

**Parameters**

`void`
:   no arguments

**Description**

For console list or console->flags updates

void console_list_unlock(void)
:   Unlock the console list

**Parameters**

`void`
:   no arguments

**Description**

Counterpart to [`console_list_lock()`](basics.md#c.console_list_lock "console_list_lock")

int console_srcu_read_lock(void)
:   Register a new reader for the SRCU-protected console list

**Parameters**

`void`
:   no arguments

**Description**

Use for_each_console_srcu() to iterate the console list

**Context**

Any context.

**Return**

A cookie to pass to [`console_srcu_read_unlock()`](basics.md#c.console_srcu_read_unlock "console_srcu_read_unlock").

void console_srcu_read_unlock(int cookie)
:   Unregister an old reader from the SRCU-protected console list

**Parameters**

`int cookie`
:   cookie returned from [`console_srcu_read_lock()`](basics.md#c.console_srcu_read_lock "console_srcu_read_lock")

**Description**

Counterpart to [`console_srcu_read_lock()`](basics.md#c.console_srcu_read_lock "console_srcu_read_lock")

void console_lock(void)
:   block the console subsystem from printing

**Parameters**

`void`
:   no arguments

**Description**

Acquires a lock which guarantees that no consoles will
be in or enter their write() callback.

Can sleep, returns nothing.

int console_trylock(void)
:   try to block the console subsystem from printing

**Parameters**

`void`
:   no arguments

**Description**

Try to acquire a lock which guarantees that no consoles will
be in or enter their write() callback.

returns 1 on success, and 0 on failure to acquire the lock.

void console_unlock(void)
:   unblock the console subsystem from printing

**Parameters**

`void`
:   no arguments

**Description**

Releases the console_lock which the caller holds to block printing of
the console subsystem.

While the console_lock was held, console output may have been buffered
by [`printk()`](../core-api/printk-basics.md#c.printk "printk"). If this is the case, [`console_unlock()`](basics.md#c.console_unlock "console_unlock"); emits
the output prior to releasing the lock.

[`console_unlock()`](basics.md#c.console_unlock "console_unlock"); may be called from any context.

void console_conditional_schedule(void)
:   yield the CPU if required

**Parameters**

`void`
:   no arguments

**Description**

If the console code is currently allowed to sleep, and
if this CPU should yield the CPU to another task, do
so here.

Must be called within [`console_lock()`](basics.md#c.console_lock "console_lock");.

void console_force_preferred_locked(struct console \*con)
:   force a registered console preferred

**Parameters**

`struct console *con`
:   The registered console to force preferred.

**Description**

Must be called under [`console_list_lock()`](basics.md#c.console_list_lock "console_list_lock").

bool printk_timed_ratelimit(unsigned long \*caller_jiffies, unsigned int interval_msecs)
:   caller-controlled printk ratelimiting

**Parameters**

`unsigned long *caller_jiffies`
:   pointer to caller's state

`unsigned int interval_msecs`
:   minimum interval between prints

**Description**

[`printk_timed_ratelimit()`](basics.md#c.printk_timed_ratelimit "printk_timed_ratelimit") returns true if more than **interval_msecs**
milliseconds have elapsed since the last time [`printk_timed_ratelimit()`](basics.md#c.printk_timed_ratelimit "printk_timed_ratelimit")
returned true.

int kmsg_dump_register(struct kmsg_dumper \*dumper)
:   register a kernel log dumper.

**Parameters**

`struct kmsg_dumper *dumper`
:   pointer to the kmsg_dumper structure

**Description**

Adds a kernel log dumper to the system. The dump callback in the
structure will be called when the kernel oopses or panics and must be
set. Returns zero on success and `-EINVAL` or `-EBUSY` otherwise.

int kmsg_dump_unregister(struct kmsg_dumper \*dumper)
:   unregister a kmsg dumper.

**Parameters**

`struct kmsg_dumper *dumper`
:   pointer to the kmsg_dumper structure

**Description**

Removes a dump device from the system. Returns zero on success and
`-EINVAL` otherwise.

bool kmsg_dump_get_line(struct kmsg_dump_iter \*iter, bool syslog, char \*line, size_t size, size_t \*len)
:   retrieve one kmsg log line

**Parameters**

`struct kmsg_dump_iter *iter`
:   kmsg dump iterator

`bool syslog`
:   include the "<4>" prefixes

`char *line`
:   buffer to copy the line to

`size_t size`
:   maximum size of the buffer

`size_t *len`
:   length of line placed into buffer

**Description**

Start at the beginning of the kmsg buffer, with the oldest kmsg
record, and copy one record into the provided buffer.

Consecutive calls will return the next available record moving
towards the end of the buffer with the youngest messages.

A return value of FALSE indicates that there are no more records to
read.

bool kmsg_dump_get_buffer(struct kmsg_dump_iter \*iter, bool syslog, char \*buf, size_t size, size_t \*len_out)
:   copy kmsg log lines

**Parameters**

`struct kmsg_dump_iter *iter`
:   kmsg dump iterator

`bool syslog`
:   include the "<4>" prefixes

`char *buf`
:   buffer to copy the line to

`size_t size`
:   maximum size of the buffer

`size_t *len_out`
:   length of line placed into buffer

**Description**

Start at the end of the kmsg buffer and fill the provided buffer
with as many of the *youngest* kmsg records that fit into it.
If the buffer is large enough, all available kmsg records will be
copied with a single call.

Consecutive calls will fill the buffer with the next block of
available older records, not including the earlier retrieved ones.

A return value of FALSE indicates that there are no more records to
read.

void kmsg_dump_rewind(struct kmsg_dump_iter \*iter)
:   reset the iterator

**Parameters**

`struct kmsg_dump_iter *iter`
:   kmsg dump iterator

**Description**

Reset the dumper's iterator so that [`kmsg_dump_get_line()`](basics.md#c.kmsg_dump_get_line "kmsg_dump_get_line") and
[`kmsg_dump_get_buffer()`](basics.md#c.kmsg_dump_get_buffer "kmsg_dump_get_buffer") can be called again and used multiple
times within the same dumper.dump() callback.

void __printk_cpu_sync_wait(void)
:   Busy wait until the printk cpu-reentrant spinning lock is not owned by any CPU.

**Parameters**

`void`
:   no arguments

**Context**

Any context.

int __printk_cpu_sync_try_get(void)
:   Try to acquire the printk cpu-reentrant spinning lock.

**Parameters**

`void`
:   no arguments

**Description**

If no processor has the lock, the calling processor takes the lock and
becomes the owner. If the calling processor is already the owner of the
lock, this function succeeds immediately.

**Context**

Any context. Expects interrupts to be disabled.

**Return**

1 on success, otherwise 0.

void __printk_cpu_sync_put(void)
:   Release the printk cpu-reentrant spinning lock.

**Parameters**

`void`
:   no arguments

**Description**

The calling processor must be the owner of the lock.

**Context**

Any context. Expects interrupts to be disabled.

void panic(const char \*fmt, ...)
:   halt the system

**Parameters**

`const char *fmt`
:   The text string to print

    Display a message, then perform cleanups.

    This function never returns.

`...`
:   variable arguments

void add_taint(unsigned flag, enum [lockdep_ok](basics.md#c.add_taint "lockdep_ok") lockdep_ok)
:   add a taint flag if not already set.

**Parameters**

`unsigned flag`
:   one of the TAINT_\* constants.

`enum lockdep_ok lockdep_ok`
:   whether lock debugging is still OK.

**Description**

If something bad has gone wrong, you'll want **lockdebug_ok** = false, but for
some notewortht-but-not-corrupting cases, it can be set to true.

## Device Resource Management

void \*__devres_alloc_node(dr_release_t release, size_t size, gfp_t gfp, int nid, const char \*name)
:   Allocate device resource data

**Parameters**

`dr_release_t release`
:   Release function devres will be associated with

`size_t size`
:   Allocation size

`gfp_t gfp`
:   Allocation flags

`int nid`
:   NUMA node

`const char *name`
:   Name of the resource

**Description**

Allocate devres of **size** bytes. The allocated area is zeroed, then
associated with **release**. The returned pointer can be passed to
other devres_\*() functions.

**Return**

Pointer to allocated devres on success, NULL on failure.

void devres_for_each_res(struct [device](infrastructure.md#c.device "device") \*dev, dr_release_t release, dr_match_t match, void \*match_data, void (\*fn)(struct [device](infrastructure.md#c.device "device")\*, void\*, void\*), void \*data)
:   Resource iterator

**Parameters**

`struct device *dev`
:   Device to iterate resource from

`dr_release_t release`
:   Look for resources associated with this release function

`dr_match_t match`
:   Match function (optional)

`void *match_data`
:   Data for the match function

`void (*fn)(struct device *, void *, void *)`
:   Function to be called for each matched resource.

`void *data`
:   Data for **fn**, the 3rd parameter of **fn**

**Description**

Call **fn** for each devres of **dev** which is associated with **release**
and for which **match** returns 1.

**Return**

> void

void devres_free(void \*res)
:   Free device resource data

**Parameters**

`void *res`
:   Pointer to devres data to free

**Description**

Free devres created with devres_alloc().

void devres_add(struct [device](infrastructure.md#c.device "device") \*dev, void \*res)
:   Register device resource

**Parameters**

`struct device *dev`
:   Device to add resource to

`void *res`
:   Resource to register

**Description**

Register devres **res** to **dev**. **res** should have been allocated
using devres_alloc(). On driver detach, the associated release
function will be invoked and devres will be freed automatically.

void \*devres_find(struct [device](infrastructure.md#c.device "device") \*dev, dr_release_t release, dr_match_t match, void \*match_data)
:   Find device resource

**Parameters**

`struct device *dev`
:   Device to lookup resource from

`dr_release_t release`
:   Look for resources associated with this release function

`dr_match_t match`
:   Match function (optional)

`void *match_data`
:   Data for the match function

**Description**

Find the latest devres of **dev** which is associated with **release**
and for which **match** returns 1. If **match** is NULL, it's considered
to match all.

**Return**

Pointer to found devres, NULL if not found.

void \*devres_get(struct [device](infrastructure.md#c.device "device") \*dev, void \*new_res, dr_match_t match, void \*match_data)
:   Find devres, if non-existent, add one atomically

**Parameters**

`struct device *dev`
:   Device to lookup or add devres for

`void *new_res`
:   Pointer to new initialized devres to add if not found

`dr_match_t match`
:   Match function (optional)

`void *match_data`
:   Data for the match function

**Description**

Find the latest devres of **dev** which has the same release function
as **new_res** and for which **match** return 1. If found, **new_res** is
freed; otherwise, **new_res** is added atomically.

**Return**

Pointer to found or added devres.

void \*devres_remove(struct [device](infrastructure.md#c.device "device") \*dev, dr_release_t release, dr_match_t match, void \*match_data)
:   Find a device resource and remove it

**Parameters**

`struct device *dev`
:   Device to find resource from

`dr_release_t release`
:   Look for resources associated with this release function

`dr_match_t match`
:   Match function (optional)

`void *match_data`
:   Data for the match function

**Description**

Find the latest devres of **dev** associated with **release** and for
which **match** returns 1. If **match** is NULL, it's considered to
match all. If found, the resource is removed atomically and
returned.

**Return**

Pointer to removed devres on success, NULL if not found.

int devres_destroy(struct [device](infrastructure.md#c.device "device") \*dev, dr_release_t release, dr_match_t match, void \*match_data)
:   Find a device resource and destroy it

**Parameters**

`struct device *dev`
:   Device to find resource from

`dr_release_t release`
:   Look for resources associated with this release function

`dr_match_t match`
:   Match function (optional)

`void *match_data`
:   Data for the match function

**Description**

Find the latest devres of **dev** associated with **release** and for
which **match** returns 1. If **match** is NULL, it's considered to
match all. If found, the resource is removed atomically and freed.

Note that the release function for the resource will not be called,
only the devres-allocated data will be freed. The caller becomes
responsible for freeing any other data.

**Return**

0 if devres is found and freed, -ENOENT if not found.

int devres_release(struct [device](infrastructure.md#c.device "device") \*dev, dr_release_t release, dr_match_t match, void \*match_data)
:   Find a device resource and destroy it, calling release

**Parameters**

`struct device *dev`
:   Device to find resource from

`dr_release_t release`
:   Look for resources associated with this release function

`dr_match_t match`
:   Match function (optional)

`void *match_data`
:   Data for the match function

**Description**

Find the latest devres of **dev** associated with **release** and for
which **match** returns 1. If **match** is NULL, it's considered to
match all. If found, the resource is removed atomically, the
release function called and the resource freed.

**Return**

0 if devres is found and freed, -ENOENT if not found.

void \*devres_open_group(struct [device](infrastructure.md#c.device "device") \*dev, void \*id, gfp_t gfp)
:   Open a new devres group

**Parameters**

`struct device *dev`
:   Device to open devres group for

`void *id`
:   Separator ID

`gfp_t gfp`
:   Allocation flags

**Description**

Open a new devres group for **dev** with **id**. For **id**, using a
pointer to an object which won't be used for another group is
recommended. If **id** is NULL, address-wise unique ID is created.

**Return**

ID of the new group, NULL on failure.

void devres_close_group(struct [device](infrastructure.md#c.device "device") \*dev, void \*id)
:   Close a devres group

**Parameters**

`struct device *dev`
:   Device to close devres group for

`void *id`
:   ID of target group, can be NULL

**Description**

Close the group identified by **id**. If **id** is NULL, the latest open
group is selected.

void devres_remove_group(struct [device](infrastructure.md#c.device "device") \*dev, void \*id)
:   Remove a devres group

**Parameters**

`struct device *dev`
:   Device to remove group for

`void *id`
:   ID of target group, can be NULL

**Description**

Remove the group identified by **id**. If **id** is NULL, the latest
open group is selected. Note that removing a group doesn't affect
any other resources.

int devres_release_group(struct [device](infrastructure.md#c.device "device") \*dev, void \*id)
:   Release resources in a devres group

**Parameters**

`struct device *dev`
:   Device to release group for

`void *id`
:   ID of target group, can be NULL

**Description**

Release all resources in the group identified by **id**. If **id** is
NULL, the latest open group is selected. The selected group and
groups properly nested inside the selected group are removed.

**Return**

The number of released non-group resources.

int __devm_add_action(struct [device](infrastructure.md#c.device "device") \*dev, void (\*action)(void\*), void \*data, const char \*name)
:   add a custom action to list of managed resources

**Parameters**

`struct device *dev`
:   Device that owns the action

`void (*action)(void *)`
:   Function that should be called

`void *data`
:   Pointer to data passed to **action** implementation

`const char *name`
:   Name of the resource (for debugging purposes)

**Description**

This adds a custom action to the list of managed resources so that
it gets executed as part of standard resource unwinding.

void devm_remove_action(struct [device](infrastructure.md#c.device "device") \*dev, void (\*action)(void\*), void \*data)
:   removes previously added custom action

**Parameters**

`struct device *dev`
:   Device that owns the action

`void (*action)(void *)`
:   Function implementing the action

`void *data`
:   Pointer to data passed to **action** implementation

**Description**

Removes instance of **action** previously added by devm_add_action().
Both action and data should match one of the existing entries.

void devm_release_action(struct [device](infrastructure.md#c.device "device") \*dev, void (\*action)(void\*), void \*data)
:   release previously added custom action

**Parameters**

`struct device *dev`
:   Device that owns the action

`void (*action)(void *)`
:   Function implementing the action

`void *data`
:   Pointer to data passed to **action** implementation

**Description**

Releases and removes instance of **action** previously added by
devm_add_action(). Both action and data should match one of the
existing entries.

void \*devm_kmalloc(struct [device](infrastructure.md#c.device "device") \*dev, size_t size, gfp_t gfp)
:   Resource-managed kmalloc

**Parameters**

`struct device *dev`
:   Device to allocate memory for

`size_t size`
:   Allocation size

`gfp_t gfp`
:   Allocation gfp flags

**Description**

Managed kmalloc. Memory allocated with this function is
automatically freed on driver detach. Like all other devres
resources, guaranteed alignment is unsigned long long.

**Return**

Pointer to allocated memory on success, NULL on failure.

void \*devm_krealloc(struct [device](infrastructure.md#c.device "device") \*dev, void \*ptr, size_t new_size, gfp_t gfp)
:   Resource-managed [`krealloc()`](../core-api/mm-api.md#c.krealloc "krealloc")

**Parameters**

`struct device *dev`
:   Device to re-allocate memory for

`void *ptr`
:   Pointer to the memory chunk to re-allocate

`size_t new_size`
:   New allocation size

`gfp_t gfp`
:   Allocation gfp flags

**Description**

Managed [`krealloc()`](../core-api/mm-api.md#c.krealloc "krealloc"). Resizes the memory chunk allocated with [`devm_kmalloc()`](basics.md#c.devm_kmalloc "devm_kmalloc").
Behaves similarly to regular [`krealloc()`](../core-api/mm-api.md#c.krealloc "krealloc"): if **ptr** is NULL or ZERO_SIZE_PTR,
it's the equivalent of [`devm_kmalloc()`](basics.md#c.devm_kmalloc "devm_kmalloc"). If new_size is zero, it frees the
previously allocated memory and returns ZERO_SIZE_PTR. This function doesn't
change the order in which the release callback for the re-alloc'ed devres
will be called (except when falling back to [`devm_kmalloc()`](basics.md#c.devm_kmalloc "devm_kmalloc") or when freeing
resources when new_size is zero). The contents of the memory are preserved
up to the lesser of new and old sizes.

char \*devm_kstrdup(struct [device](infrastructure.md#c.device "device") \*dev, const char \*s, gfp_t gfp)
:   Allocate resource managed space and copy an existing string into that.

**Parameters**

`struct device *dev`
:   Device to allocate memory for

`const char *s`
:   the string to duplicate

`gfp_t gfp`
:   the GFP mask used in the [`devm_kmalloc()`](basics.md#c.devm_kmalloc "devm_kmalloc") call when
    allocating memory

**Return**

Pointer to allocated string on success, NULL on failure.

const char \*devm_kstrdup_const(struct [device](infrastructure.md#c.device "device") \*dev, const char \*s, gfp_t gfp)
:   resource managed conditional string duplication

**Parameters**

`struct device *dev`
:   device for which to duplicate the string

`const char *s`
:   the string to duplicate

`gfp_t gfp`
:   the GFP mask used in the [`kmalloc()`](../core-api/mm-api.md#c.kmalloc "kmalloc") call when allocating memory

**Description**

Strings allocated by devm_kstrdup_const will be automatically freed when
the associated device is detached.

**Return**

Source string if it is in .rodata section otherwise it falls back to
devm_kstrdup.

char \*devm_kvasprintf(struct [device](infrastructure.md#c.device "device") \*dev, gfp_t gfp, const char \*fmt, va_list ap)
:   Allocate resource managed space and format a string into that.

**Parameters**

`struct device *dev`
:   Device to allocate memory for

`gfp_t gfp`
:   the GFP mask used in the [`devm_kmalloc()`](basics.md#c.devm_kmalloc "devm_kmalloc") call when
    allocating memory

`const char *fmt`
:   The printf()-style format string

`va_list ap`
:   Arguments for the format string

**Return**

Pointer to allocated string on success, NULL on failure.

char \*devm_kasprintf(struct [device](infrastructure.md#c.device "device") \*dev, gfp_t gfp, const char \*fmt, ...)
:   Allocate resource managed space and format a string into that.

**Parameters**

`struct device *dev`
:   Device to allocate memory for

`gfp_t gfp`
:   the GFP mask used in the [`devm_kmalloc()`](basics.md#c.devm_kmalloc "devm_kmalloc") call when
    allocating memory

`const char *fmt`
:   The printf()-style format string

`...`
:   Arguments for the format string

**Return**

Pointer to allocated string on success, NULL on failure.

void devm_kfree(struct [device](infrastructure.md#c.device "device") \*dev, const void \*p)
:   Resource-managed kfree

**Parameters**

`struct device *dev`
:   Device this memory belongs to

`const void *p`
:   Memory to free

**Description**

Free memory allocated with [`devm_kmalloc()`](basics.md#c.devm_kmalloc "devm_kmalloc").

void \*devm_kmemdup(struct [device](infrastructure.md#c.device "device") \*dev, const void \*src, size_t len, gfp_t gfp)
:   Resource-managed kmemdup

**Parameters**

`struct device *dev`
:   Device this memory belongs to

`const void *src`
:   Memory region to duplicate

`size_t len`
:   Memory region length

`gfp_t gfp`
:   GFP mask to use

**Description**

Duplicate region of a memory using resource managed kmalloc

unsigned long devm_get_free_pages(struct [device](infrastructure.md#c.device "device") \*dev, gfp_t gfp_mask, unsigned int order)
:   Resource-managed __get_free_pages

**Parameters**

`struct device *dev`
:   Device to allocate memory for

`gfp_t gfp_mask`
:   Allocation gfp flags

`unsigned int order`
:   Allocation size is (1 << order) pages

**Description**

Managed get_free_pages. Memory allocated with this function is
automatically freed on driver detach.

**Return**

Address of allocated memory on success, 0 on failure.

void devm_free_pages(struct [device](infrastructure.md#c.device "device") \*dev, unsigned long addr)
:   Resource-managed free_pages

**Parameters**

`struct device *dev`
:   Device this memory belongs to

`unsigned long addr`
:   Memory to free

**Description**

Free memory allocated with [`devm_get_free_pages()`](basics.md#c.devm_get_free_pages "devm_get_free_pages"). Unlike free_pages,
there is no need to supply the **order**.

void __percpu \*__devm_alloc_percpu(struct [device](infrastructure.md#c.device "device") \*dev, size_t size, size_t align)
:   Resource-managed alloc_percpu

**Parameters**

`struct device *dev`
:   Device to allocate per-cpu memory for

`size_t size`
:   Size of per-cpu memory to allocate

`size_t align`
:   Alignment of per-cpu memory to allocate

**Description**

Managed alloc_percpu. Per-cpu memory allocated with this function is
automatically freed on driver detach.

**Return**

Pointer to allocated memory on success, NULL on failure.

void devm_free_percpu(struct [device](infrastructure.md#c.device "device") \*dev, void __percpu \*pdata)
:   Resource-managed free_percpu

**Parameters**

`struct device *dev`
:   Device this memory belongs to

`void __percpu *pdata`
:   Per-cpu memory to free

**Description**

Free memory allocated with [`devm_alloc_percpu()`](infrastructure.md#c.devm_alloc_percpu "devm_alloc_percpu").
