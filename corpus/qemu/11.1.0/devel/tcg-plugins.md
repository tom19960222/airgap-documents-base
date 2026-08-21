---
collection: qemu
version: "11.1.0"
title: "QEMU TCG Plugins"
source_url: https://www.qemu.org/docs/master/devel/tcg-plugins.html
fetched_at: 2026-08-21T03:23:49+00:00
---
# QEMU TCG Plugins

## Writing plugins

### API versioning

This is a new feature for QEMU and it does allow people to develop
out-of-tree plugins that can be dynamically linked into a running QEMU
process. However the project reserves the right to change or break the
API should it need to do so. The best way to avoid this is to submit
your plugin upstream so they can be updated if/when the API changes.

All plugins need to declare a symbol which exports the plugin API
version they were built against. This can be done simply by:

```
QEMU_PLUGIN_EXPORT int qemu_plugin_version = QEMU_PLUGIN_VERSION;
```

The core code will refuse to load a plugin that doesn’t export a
`qemu_plugin_version` symbol or if plugin version is outside of QEMU’s
supported range of API versions.

Additionally the `qemu_info_t` structure which is passed to the
`qemu_plugin_install` method of a plugin will detail the minimum and
current API versions supported by QEMU. The API version will be
incremented if new APIs are added. The minimum API version will be
incremented if existing APIs are changed or removed.

### Lifetime of the query handle

Each callback provides an opaque anonymous information handle which
can usually be further queried to find out information about a
translation, instruction or operation. The handles themselves are only
valid during the lifetime of the callback so it is important that any
information that is needed is extracted during the callback and saved
by the plugin.

### Plugin life cycle

First the plugin is loaded and the public qemu_plugin_install function
is called. The plugin will then register callbacks for various plugin
events. Generally plugins will register a handler for the *atexit*
if they want to dump a summary of collected information once the
program/system has finished running.

When a registered event occurs the plugin callback is invoked. The
callbacks may provide additional information. In the case of a
translation event the plugin has an option to enumerate the
instructions in a block of instructions and optionally register
callbacks to some or all instructions when they are executed.

There is also a facility to add inline instructions doing various operations,
like adding or storing an immediate value. It is also possible to execute a
callback conditionally, with condition being evaluated inline. All those inline
operations are associated to a `scoreboard`, which is a thread-local storage
automatically expanded when new cores/threads are created and that can be
accessed/modified in a thread-safe way without any lock needed. Combining inline
operations and conditional callbacks offer a more efficient way to instrument
binaries, compared to classic callbacks.

Finally when QEMU exits all the registered *atexit* callbacks are
invoked.

### Exposure of QEMU internals

The plugin architecture actively avoids leaking implementation details
about how QEMU’s translation works to the plugins. While there are
conceptions such as translation time and translation blocks the
details are opaque to plugins. The plugin is able to query select
details of instructions and system configuration only through the
exported *qemu_plugin* functions.

However the following assumptions can be made:

#### Translation Blocks

All code will go through a translation phase although not all
translations will be necessarily be executed. You need to instrument
actual executions to track what is happening.

It is quite normal to see the same address translated multiple times.
If you want to track the code in system emulation you should examine
the underlying physical address (`qemu_plugin_insn_haddr`) to take
into account the effects of virtual memory although if the system does
paging this will change too.

Not all instructions in a block will always execute so if its
important to track individual instruction execution you need to
instrument them directly. However asynchronous interrupts will not
change control flow mid-block.

#### Instructions

Instruction instrumentation runs before the instruction executes. You
can be can be sure the instruction will be dispatched, but you can’t
be sure it will complete. Generally this will be because of a
synchronous exception (e.g. SIGILL) triggered by the instruction
attempting to execute. If you want to be sure you will need to
instrument the next instruction as well. See the `execlog.c` plugin
for examples of how to track this and finalise details after execution.

#### Memory Accesses

Memory callbacks are called after a successful load or store.
Unsuccessful operations (i.e. faults) will not be visible to memory
instrumentation although the execution side effects can be observed
(e.g. entering a exception handler).

#### System Idle and Resume States

The `qemu_plugin_register_vcpu_idle_cb` and
`qemu_plugin_register_vcpu_resume_cb` functions can be used to track
when CPUs go into and return from sleep states when waiting for
external I/O. Be aware though that these may occur less frequently
than in real HW due to the inefficiencies of emulation giving less
chance for the CPU to idle.

## Internals

### Locking

We have to ensure we cannot deadlock, particularly under MTTCG. For
this we acquire a lock when called from plugin code. We also keep the
list of callbacks under RCU so that we do not have to hold the lock
when calling the callbacks. This is also for performance, since some
callbacks (e.g. memory access callbacks) might be called very
frequently.

> - A consequence of this is that we keep our own list of CPUs, so that
>   we do not have to worry about locking order wrt cpu_list_lock.
> - Use a recursive lock, since we can get registration calls from
>   callbacks.

As a result registering/unregistering callbacks is “slow”, since it
takes a lock. But this is very infrequent; we want performance when
calling (or not calling) callbacks, not when registering them. Using
RCU is great for this.

We support the uninstallation of a plugin at any time (e.g. from
plugin callbacks). This allows plugins to remove themselves if they no
longer want to instrument the code. This operation is asynchronous
which means callbacks may still occur after the uninstall operation is
requested. The plugin isn’t completely uninstalled until the safe work
has executed while all vCPUs are quiescent.

# Plugin API

The following API is generated from the inline documentation in
`include/plugins/qemu-plugin.h`. Please ensure any updates to the API
include the full kernel-doc annotations.

type qemu_plugin_id_t
:   Unique plugin ID

struct qemu_info_t
:   system information for plugins

**Definition**:

```
struct qemu_info_t {
    const char *target_name;
    struct {
        int min;
        int cur;
    } version;
    bool system_emulation;
    union {
        struct {
            int smp_vcpus;
            int max_vcpus;
        } system;
    };
};
```

**Members**

`target_name`
:   string describing architecture

`version`
:   minimum and current plugin API level

`system_emulation`
:   is this a full system emulation?

`{unnamed_union}`
:   anonymous

`system`
:   information relevant to system emulation

**Description**

This structure provides for some limited information about the
system to allow the plugin to make decisions on how to proceed. For
example it might only be suitable for running on some guest
architectures or when under full system emulation.

int qemu_plugin_install([qemu_plugin_id_t](tcg-plugins.md#c.qemu_plugin_id_t "qemu_plugin_id_t") id, const [qemu_info_t](tcg-plugins.md#c.qemu_info_t "qemu_info_t") \*info, int argc, char \*\*argv)
:   Install a plugin

**Parameters**

`qemu_plugin_id_t id`
:   this plugin’s opaque ID

`const qemu_info_t *info`
:   a block describing some details about the guest

`int argc`
:   number of arguments

`char **argv`
:   array of arguments (**argc** elements)

**Description**

All plugins must export this symbol which is called when the plugin
is first loaded. Calling qemu_plugin_uninstall() from this function
is a bug.

**Note**

**info** is only live during the call. Copy any information we
want to keep. **argv** remains valid throughout the lifetime of the
loaded plugin.

**Return**

0 on successful loading, !0 for an error.

qemu_plugin_udata_cb_t
:   **Typedef**: callback with user data

**Syntax**

> `void qemu_plugin_udata_cb_t (void *userdata)`

**Parameters**

`void *userdata`
:   user data for callback

qemu_plugin_vcpu_udata_cb_t
:   **Typedef**: vcpu callback

**Syntax**

> `void qemu_plugin_vcpu_udata_cb_t (unsigned int vcpu_index, void *userdata)`

**Parameters**

`unsigned int vcpu_index`
:   the current vcpu context

`void *userdata`
:   user data for callback

enum qemu_plugin_discon_type
:   type of a (potential) PC discontinuity

**Constants**

`QEMU_PLUGIN_DISCON_INTERRUPT`
:   an interrupt, defined across all architectures
    as an asynchronous event, usually originating
    from outside the CPU

`QEMU_PLUGIN_DISCON_EXCEPTION`
:   an exception, defined across all architectures
    as a synchronous event in response to a
    specific instruction being executed

`QEMU_PLUGIN_DISCON_HOSTCALL`
:   a host call, functionally a special kind of
    exception that is not handled by code run by
    the vCPU but machinery outside the vCPU

`QEMU_PLUGIN_DISCON_ALL`
:   all types of disconinuity events currently covered

qemu_plugin_vcpu_discon_cb_t
:   **Typedef**: vcpu discontinuity callback

**Syntax**

> `void qemu_plugin_vcpu_discon_cb_t (unsigned int vcpu_index, enum qemu_plugin_discon_type type, uint64_t from_pc, uint64_t to_pc, void *userdata)`

**Parameters**

`unsigned int vcpu_index`
:   the current vcpu context

`enum qemu_plugin_discon_type type`
:   the type of discontinuity

`uint64_t from_pc`
:   the source of the discontinuity, e.g. the PC before the
    transition

`uint64_t to_pc`
:   the PC pointing to the next instruction to be executed

`void *userdata`
:   user data for callback

**Description**

The exact semantics of **from_pc** depends on the **type** of discontinuity. For
interrupts, **from_pc** will point to the next instruction which would have
been executed. For exceptions and host calls, **from_pc** will point to the
instruction that caused the exception or issued the host call. Note that
in the case of exceptions, the instruction may not be retired and thus not
observable via general instruction exec callbacks. The same may be the case
for some host calls such as hypervisor call “exceptions”.

void qemu_plugin_uninstall([qemu_plugin_id_t](tcg-plugins.md#c.qemu_plugin_id_t "qemu_plugin_id_t") id, [qemu_plugin_udata_cb_t](tcg-plugins.md#c.qemu_plugin_udata_cb_t "qemu_plugin_udata_cb_t") cb, void \*userdata)
:   Uninstall a plugin

**Parameters**

`qemu_plugin_id_t id`
:   this plugin’s opaque ID

`qemu_plugin_udata_cb_t cb`
:   callback to be called once the plugin has been removed

`void *userdata`
:   user data for callback

**Description**

Do NOT assume that the plugin has been uninstalled once this function
returns. Plugins are uninstalled asynchronously, and therefore the given
plugin receives callbacks until **cb** is called.

**Note**

Calling this function from qemu_plugin_install() is a bug.

void qemu_plugin_reset([qemu_plugin_id_t](tcg-plugins.md#c.qemu_plugin_id_t "qemu_plugin_id_t") id, [qemu_plugin_udata_cb_t](tcg-plugins.md#c.qemu_plugin_udata_cb_t "qemu_plugin_udata_cb_t") cb, void \*userdata)
:   Reset a plugin

**Parameters**

`qemu_plugin_id_t id`
:   this plugin’s opaque ID

`qemu_plugin_udata_cb_t cb`
:   callback to be called once the plugin has been reset

`void *userdata`
:   user data for callback

**Description**

Unregisters all callbacks for the plugin given by **id**.

Do NOT assume that the plugin has been reset once this function returns.
Plugins are reset asynchronously, and therefore the given plugin receives
callbacks until **cb** is called.

void qemu_plugin_register_vcpu_init_cb([qemu_plugin_id_t](tcg-plugins.md#c.qemu_plugin_id_t "qemu_plugin_id_t") id, [qemu_plugin_vcpu_udata_cb_t](tcg-plugins.md#c.qemu_plugin_vcpu_udata_cb_t "qemu_plugin_vcpu_udata_cb_t") cb, void \*userdata)
:   register a vCPU initialization callback

**Parameters**

`qemu_plugin_id_t id`
:   plugin ID

`qemu_plugin_vcpu_udata_cb_t cb`
:   callback function

`void *userdata`
:   user data for callback

**Description**

The **cb** function is called every time a vCPU is initialized.

See also: qemu_plugin_register_vcpu_exit_cb()

void qemu_plugin_register_vcpu_exit_cb([qemu_plugin_id_t](tcg-plugins.md#c.qemu_plugin_id_t "qemu_plugin_id_t") id, [qemu_plugin_vcpu_udata_cb_t](tcg-plugins.md#c.qemu_plugin_vcpu_udata_cb_t "qemu_plugin_vcpu_udata_cb_t") cb, void \*userdata)
:   register a vCPU exit callback

**Parameters**

`qemu_plugin_id_t id`
:   plugin ID

`qemu_plugin_vcpu_udata_cb_t cb`
:   callback function

`void *userdata`
:   user data for callback

**Description**

The **cb** function is called every time a vCPU exits.

See also: qemu_plugin_register_vcpu_init_cb()

void qemu_plugin_register_vcpu_idle_cb([qemu_plugin_id_t](tcg-plugins.md#c.qemu_plugin_id_t "qemu_plugin_id_t") id, [qemu_plugin_vcpu_udata_cb_t](tcg-plugins.md#c.qemu_plugin_vcpu_udata_cb_t "qemu_plugin_vcpu_udata_cb_t") cb, void \*userdata)
:   register a vCPU idle callback

**Parameters**

`qemu_plugin_id_t id`
:   plugin ID

`qemu_plugin_vcpu_udata_cb_t cb`
:   callback function

`void *userdata`
:   user data for callback

**Description**

The **cb** function is called every time a vCPU idles.

void qemu_plugin_register_vcpu_resume_cb([qemu_plugin_id_t](tcg-plugins.md#c.qemu_plugin_id_t "qemu_plugin_id_t") id, [qemu_plugin_vcpu_udata_cb_t](tcg-plugins.md#c.qemu_plugin_vcpu_udata_cb_t "qemu_plugin_vcpu_udata_cb_t") cb, void \*userdata)
:   register a vCPU resume callback

**Parameters**

`qemu_plugin_id_t id`
:   plugin ID

`qemu_plugin_vcpu_udata_cb_t cb`
:   callback function

`void *userdata`
:   user data for callback

**Description**

The **cb** function is called every time a vCPU resumes execution.

void qemu_plugin_register_vcpu_discon_cb([qemu_plugin_id_t](tcg-plugins.md#c.qemu_plugin_id_t "qemu_plugin_id_t") id, enum [qemu_plugin_discon_type](tcg-plugins.md#c.qemu_plugin_discon_type "qemu_plugin_discon_type") type, [qemu_plugin_vcpu_discon_cb_t](tcg-plugins.md#c.qemu_plugin_vcpu_discon_cb_t "qemu_plugin_vcpu_discon_cb_t") cb, void \*userdata)
:   register a discontinuity callback

**Parameters**

`qemu_plugin_id_t id`
:   plugin ID

`enum qemu_plugin_discon_type type`
:   types of discontinuities for which to call the callback

`qemu_plugin_vcpu_discon_cb_t cb`
:   callback function

`void *userdata`
:   user data for callback

**Description**

The **cb** function is called every time a vCPU receives a discontinuity event
of the specified type(s), after the vCPU was prepared to handle the event.
Preparation entails updating the PC, usually to some interrupt handler or
trap vector entry.

type qemu_plugin_u64
:   uint64_t member of an entry in a scoreboard

**Description**

This field allows to access a specific uint64_t member in one given entry,
located at a specified offset. Inline operations expect this as entry.

enum qemu_plugin_cb_flags
:   type of callback

**Constants**

`QEMU_PLUGIN_CB_NO_REGS`
:   callback does not access the CPU’s regs

`QEMU_PLUGIN_CB_R_REGS`
:   callback reads the CPU’s regs

`QEMU_PLUGIN_CB_RW_REGS`
:   callback reads and writes the CPU’s regs

`QEMU_PLUGIN_CB_RW_REGS_PC`
:   callback reads and writes the CPU’s
    regs and updates the PC

enum qemu_plugin_mem_rw
:   type of memory access

**Constants**

`QEMU_PLUGIN_MEM_R`
:   memory read access only

`QEMU_PLUGIN_MEM_W`
:   memory write access only

`QEMU_PLUGIN_MEM_RW`
:   memory read and write access

enum qemu_plugin_mem_value_type
:   size of memory value

**Constants**

`QEMU_PLUGIN_MEM_VALUE_U8`
:   unsigned 8-bit value

`QEMU_PLUGIN_MEM_VALUE_U16`
:   unsigned 16-bit value

`QEMU_PLUGIN_MEM_VALUE_U32`
:   unsigned 32-bit value

`QEMU_PLUGIN_MEM_VALUE_U64`
:   unsigned 64-bit value

`QEMU_PLUGIN_MEM_VALUE_U128`
:   unsigned 128-bit value

type qemu_plugin_mem_value
:   value accessed during a load/store

enum qemu_plugin_cond
:   condition to enable callback

**Constants**

`QEMU_PLUGIN_COND_NEVER`
:   false

`QEMU_PLUGIN_COND_ALWAYS`
:   true

`QEMU_PLUGIN_COND_EQ`
:   is equal?

`QEMU_PLUGIN_COND_NE`
:   is not equal?

`QEMU_PLUGIN_COND_LT`
:   is less than?

`QEMU_PLUGIN_COND_LE`
:   is less than or equal?

`QEMU_PLUGIN_COND_GT`
:   is greater than?

`QEMU_PLUGIN_COND_GE`
:   is greater than or equal?

qemu_plugin_vcpu_tb_trans_cb_t
:   **Typedef**: translation callback

**Syntax**

> `void qemu_plugin_vcpu_tb_trans_cb_t (struct qemu_plugin_tb *tb, void *userdata)`

**Parameters**

`struct qemu_plugin_tb *tb`
:   opaque handle used for querying and instrumenting a block.

`void *userdata`
:   any plugin data to pass to the **cb**

void qemu_plugin_register_vcpu_tb_trans_cb([qemu_plugin_id_t](tcg-plugins.md#c.qemu_plugin_id_t "qemu_plugin_id_t") id, [qemu_plugin_vcpu_tb_trans_cb_t](tcg-plugins.md#c.qemu_plugin_vcpu_tb_trans_cb_t "qemu_plugin_vcpu_tb_trans_cb_t") cb, void \*userdata)
:   register a translate cb

**Parameters**

`qemu_plugin_id_t id`
:   plugin ID

`qemu_plugin_vcpu_tb_trans_cb_t cb`
:   callback function

`void *userdata`
:   user data for callback

**Description**

The **cb** function is called every time a translation occurs. The **cb**
function is passed an opaque qemu_plugin_type which it can query
for additional information including the list of translated
instructions. At this point the plugin can register further
callbacks to be triggered when the block or individual instruction
executes.

void qemu_plugin_register_vcpu_tb_exec_cb(struct qemu_plugin_tb \*tb, [qemu_plugin_vcpu_udata_cb_t](tcg-plugins.md#c.qemu_plugin_vcpu_udata_cb_t "qemu_plugin_vcpu_udata_cb_t") cb, enum [qemu_plugin_cb_flags](tcg-plugins.md#c.qemu_plugin_cb_flags "qemu_plugin_cb_flags") flags, void \*userdata)
:   register execution callback

**Parameters**

`struct qemu_plugin_tb *tb`
:   the opaque qemu_plugin_tb handle for the translation

`qemu_plugin_vcpu_udata_cb_t cb`
:   callback function

`enum qemu_plugin_cb_flags flags`
:   does the plugin read or write the CPU’s registers?

`void *userdata`
:   user data for callback

**Description**

The **cb** function is called every time a translated unit executes.

void qemu_plugin_register_vcpu_tb_exec_cond_cb(struct qemu_plugin_tb \*tb, [qemu_plugin_vcpu_udata_cb_t](tcg-plugins.md#c.qemu_plugin_vcpu_udata_cb_t "qemu_plugin_vcpu_udata_cb_t") cb, enum [qemu_plugin_cb_flags](tcg-plugins.md#c.qemu_plugin_cb_flags "qemu_plugin_cb_flags") flags, enum [qemu_plugin_cond](tcg-plugins.md#c.qemu_plugin_cond "qemu_plugin_cond") cond, [qemu_plugin_u64](tcg-plugins.md#c.qemu_plugin_u64 "qemu_plugin_u64") entry, uint64_t imm, void \*userdata)
:   register conditional callback

**Parameters**

`struct qemu_plugin_tb *tb`
:   the opaque qemu_plugin_tb handle for the translation

`qemu_plugin_vcpu_udata_cb_t cb`
:   callback function

`enum qemu_plugin_cb_flags flags`
:   does the plugin read or write the CPU’s registers?

`enum qemu_plugin_cond cond`
:   condition to enable callback

`qemu_plugin_u64 entry`
:   first operand for condition

`uint64_t imm`
:   second operand for condition

`void *userdata`
:   user data for callback

**Description**

The **cb** function is called when a translated unit executes if
entry **cond** imm is true.
If condition is QEMU_PLUGIN_COND_ALWAYS, condition is never interpreted and
this function is equivalent to qemu_plugin_register_vcpu_tb_exec_cb.
If condition QEMU_PLUGIN_COND_NEVER, condition is never interpreted and
callback is never installed.

enum qemu_plugin_op
:   describes an inline op

**Constants**

`QEMU_PLUGIN_INLINE_ADD_U64`
:   add an immediate value uint64_t

`QEMU_PLUGIN_INLINE_STORE_U64`
:   store an immediate value uint64_t

void qemu_plugin_register_vcpu_tb_exec_inline_per_vcpu(struct qemu_plugin_tb \*tb, enum [qemu_plugin_op](tcg-plugins.md#c.qemu_plugin_op "qemu_plugin_op") op, [qemu_plugin_u64](tcg-plugins.md#c.qemu_plugin_u64 "qemu_plugin_u64") entry, uint64_t imm)
:   execution inline op

**Parameters**

`struct qemu_plugin_tb *tb`
:   the opaque qemu_plugin_tb handle for the translation

`enum qemu_plugin_op op`
:   the type of qemu_plugin_op (e.g. ADD_U64)

`qemu_plugin_u64 entry`
:   entry to run op

`uint64_t imm`
:   the op data (e.g. 1)

**Description**

Insert an inline op on a given scoreboard entry.

void qemu_plugin_register_vcpu_insn_exec_cb(struct qemu_plugin_insn \*insn, [qemu_plugin_vcpu_udata_cb_t](tcg-plugins.md#c.qemu_plugin_vcpu_udata_cb_t "qemu_plugin_vcpu_udata_cb_t") cb, enum [qemu_plugin_cb_flags](tcg-plugins.md#c.qemu_plugin_cb_flags "qemu_plugin_cb_flags") flags, void \*userdata)
:   register insn execution cb

**Parameters**

`struct qemu_plugin_insn *insn`
:   the opaque qemu_plugin_insn handle for an instruction

`qemu_plugin_vcpu_udata_cb_t cb`
:   callback function

`enum qemu_plugin_cb_flags flags`
:   does the plugin read or write the CPU’s registers?

`void *userdata`
:   user data for callback

**Description**

The **cb** function is called every time an instruction is executed

void qemu_plugin_register_vcpu_insn_exec_cond_cb(struct qemu_plugin_insn \*insn, [qemu_plugin_vcpu_udata_cb_t](tcg-plugins.md#c.qemu_plugin_vcpu_udata_cb_t "qemu_plugin_vcpu_udata_cb_t") cb, enum [qemu_plugin_cb_flags](tcg-plugins.md#c.qemu_plugin_cb_flags "qemu_plugin_cb_flags") flags, enum [qemu_plugin_cond](tcg-plugins.md#c.qemu_plugin_cond "qemu_plugin_cond") cond, [qemu_plugin_u64](tcg-plugins.md#c.qemu_plugin_u64 "qemu_plugin_u64") entry, uint64_t imm, void \*userdata)
:   conditional insn execution cb

**Parameters**

`struct qemu_plugin_insn *insn`
:   the opaque qemu_plugin_insn handle for an instruction

`qemu_plugin_vcpu_udata_cb_t cb`
:   callback function

`enum qemu_plugin_cb_flags flags`
:   does the plugin read or write the CPU’s registers?

`enum qemu_plugin_cond cond`
:   condition to enable callback

`qemu_plugin_u64 entry`
:   first operand for condition

`uint64_t imm`
:   second operand for condition

`void *userdata`
:   user data for callback

**Description**

The **cb** function is called when an instruction executes if
entry **cond** imm is true.
If condition is QEMU_PLUGIN_COND_ALWAYS, condition is never interpreted and
this function is equivalent to qemu_plugin_register_vcpu_insn_exec_cb.
If condition QEMU_PLUGIN_COND_NEVER, condition is never interpreted and
callback is never installed.

void qemu_plugin_register_vcpu_insn_exec_inline_per_vcpu(struct qemu_plugin_insn \*insn, enum [qemu_plugin_op](tcg-plugins.md#c.qemu_plugin_op "qemu_plugin_op") op, [qemu_plugin_u64](tcg-plugins.md#c.qemu_plugin_u64 "qemu_plugin_u64") entry, uint64_t imm)
:   insn exec inline op

**Parameters**

`struct qemu_plugin_insn *insn`
:   the opaque qemu_plugin_insn handle for an instruction

`enum qemu_plugin_op op`
:   the type of qemu_plugin_op (e.g. ADD_U64)

`qemu_plugin_u64 entry`
:   entry to run op

`uint64_t imm`
:   the op data (e.g. 1)

**Description**

Insert an inline op to every time an instruction executes.

size_t qemu_plugin_tb_n_insns(const struct qemu_plugin_tb \*tb)
:   query helper for number of insns in TB

**Parameters**

`const struct qemu_plugin_tb *tb`
:   opaque handle to TB passed to callback

**Return**

number of instructions in this block

uint64_t qemu_plugin_tb_vaddr(const struct qemu_plugin_tb \*tb)
:   query helper for vaddr of TB start

**Parameters**

`const struct qemu_plugin_tb *tb`
:   opaque handle to TB passed to callback

**Return**

virtual address of block start

struct qemu_plugin_insn \*qemu_plugin_tb_get_insn(const struct qemu_plugin_tb \*tb, size_t idx)
:   retrieve handle for instruction

**Parameters**

`const struct qemu_plugin_tb *tb`
:   opaque handle to TB passed to callback

`size_t idx`
:   instruction number, 0 indexed

**Description**

The returned handle can be used in follow up helper queries as well
as when instrumenting an instruction. It is only valid for the
lifetime of the callback.

**Return**

opaque handle to instruction

size_t qemu_plugin_insn_data(const struct qemu_plugin_insn \*insn, void \*dest, size_t len)
:   copy instruction data

**Parameters**

`const struct qemu_plugin_insn *insn`
:   opaque instruction handle from qemu_plugin_tb_get_insn()

`void *dest`
:   destination into which data is copied

`size_t len`
:   length of dest

**Description**

Returns the number of bytes copied, minimum of **len** and insn size.

size_t qemu_plugin_insn_size(const struct qemu_plugin_insn \*insn)
:   return size of instruction

**Parameters**

`const struct qemu_plugin_insn *insn`
:   opaque instruction handle from qemu_plugin_tb_get_insn()

**Return**

size of instruction in bytes

uint64_t qemu_plugin_insn_vaddr(const struct qemu_plugin_insn \*insn)
:   return vaddr of instruction

**Parameters**

`const struct qemu_plugin_insn *insn`
:   opaque instruction handle from qemu_plugin_tb_get_insn()

**Return**

virtual address of instruction

void \*qemu_plugin_insn_haddr(const struct qemu_plugin_insn \*insn)
:   return hardware addr of instruction

**Parameters**

`const struct qemu_plugin_insn *insn`
:   opaque instruction handle from qemu_plugin_tb_get_insn()

**Return**

hardware (physical) target address of instruction

type qemu_plugin_meminfo_t
:   opaque memory transaction handle

**Description**

This can be further queried using the qemu_plugin_mem_\* query
functions.

unsigned int qemu_plugin_mem_size_shift([qemu_plugin_meminfo_t](tcg-plugins.md#c.qemu_plugin_meminfo_t "qemu_plugin_meminfo_t") info)
:   get size of access

**Parameters**

`qemu_plugin_meminfo_t info`
:   opaque memory transaction handle

**Return**

size of access in ^2 (0=byte, 1=16bit, 2=32bit etc…)

bool qemu_plugin_mem_is_sign_extended([qemu_plugin_meminfo_t](tcg-plugins.md#c.qemu_plugin_meminfo_t "qemu_plugin_meminfo_t") info)
:   was the access sign extended

**Parameters**

`qemu_plugin_meminfo_t info`
:   opaque memory transaction handle

**Return**

true if it was, otherwise false

bool qemu_plugin_mem_is_big_endian([qemu_plugin_meminfo_t](tcg-plugins.md#c.qemu_plugin_meminfo_t "qemu_plugin_meminfo_t") info)
:   was the access big endian

**Parameters**

`qemu_plugin_meminfo_t info`
:   opaque memory transaction handle

**Return**

true if it was, otherwise false

bool qemu_plugin_mem_is_store([qemu_plugin_meminfo_t](tcg-plugins.md#c.qemu_plugin_meminfo_t "qemu_plugin_meminfo_t") info)
:   was the access a store

**Parameters**

`qemu_plugin_meminfo_t info`
:   opaque memory transaction handle

**Return**

true if it was, otherwise false

[qemu_plugin_mem_value](tcg-plugins.md#c.qemu_plugin_mem_value "qemu_plugin_mem_value") qemu_plugin_mem_get_value([qemu_plugin_meminfo_t](tcg-plugins.md#c.qemu_plugin_meminfo_t "qemu_plugin_meminfo_t") info)
:   return last value loaded/stored

**Parameters**

`qemu_plugin_meminfo_t info`
:   opaque memory transaction handle

**Return**

memory value in host-endian order (no further swap is necessary).

struct qemu_plugin_hwaddr \*qemu_plugin_get_hwaddr([qemu_plugin_meminfo_t](tcg-plugins.md#c.qemu_plugin_meminfo_t "qemu_plugin_meminfo_t") info, uint64_t vaddr)
:   return handle for memory operation

**Parameters**

`qemu_plugin_meminfo_t info`
:   opaque memory info structure

`uint64_t vaddr`
:   the virtual address of the memory operation

**Description**

For system emulation returns a qemu_plugin_hwaddr handle to query
details about the actual physical address backing the virtual
address. For linux-user guests it just returns NULL.

This handle is *only* valid for the duration of the callback. Any
information about the handle should be recovered before the
callback returns.

bool qemu_plugin_hwaddr_is_io(const struct qemu_plugin_hwaddr \*haddr)
:   query whether memory operation is IO

**Parameters**

`const struct qemu_plugin_hwaddr *haddr`
:   address handle from qemu_plugin_get_hwaddr()

**Description**

Returns true if the handle’s memory operation is to memory-mapped IO, or
false if it is to RAM

uint64_t qemu_plugin_hwaddr_phys_addr(const struct qemu_plugin_hwaddr \*haddr)
:   query physical address for memory operation

**Parameters**

`const struct qemu_plugin_hwaddr *haddr`
:   address handle from qemu_plugin_get_hwaddr()

**Description**

Returns the physical address associated with the memory operation

Note that the returned physical address may not be unique if you are dealing
with multiple address spaces.

qemu_plugin_vcpu_mem_cb_t
:   **Typedef**: memory callback function type

**Syntax**

> `void qemu_plugin_vcpu_mem_cb_t (unsigned int vcpu_index, qemu_plugin_meminfo_t info, uint64_t vaddr, void *userdata)`

**Parameters**

`unsigned int vcpu_index`
:   the executing vCPU

`qemu_plugin_meminfo_t info`
:   an opaque handle for further queries about the memory

`uint64_t vaddr`
:   the virtual address of the transaction

`void *userdata`
:   user data for callback

void qemu_plugin_register_vcpu_mem_cb(struct qemu_plugin_insn \*insn, [qemu_plugin_vcpu_mem_cb_t](tcg-plugins.md#c.qemu_plugin_vcpu_mem_cb_t "qemu_plugin_vcpu_mem_cb_t") cb, enum [qemu_plugin_cb_flags](tcg-plugins.md#c.qemu_plugin_cb_flags "qemu_plugin_cb_flags") flags, enum [qemu_plugin_mem_rw](tcg-plugins.md#c.qemu_plugin_mem_rw "qemu_plugin_mem_rw") rw, void \*userdata)
:   register memory access callback

**Parameters**

`struct qemu_plugin_insn *insn`
:   handle for instruction to instrument

`qemu_plugin_vcpu_mem_cb_t cb`
:   callback of type qemu_plugin_vcpu_mem_cb_t

`enum qemu_plugin_cb_flags flags`
:   (currently unused) callback flags

`enum qemu_plugin_mem_rw rw`
:   monitor reads, writes or both

`void *userdata`
:   user data for callback

**Description**

This registers a full callback for every memory access generated by
an instruction. If the instruction doesn’t access memory no
callback will be made.

The callback reports the vCPU the access took place on, the virtual
address of the access and a handle for further queries. The user
can attach some userdata to the callback for additional purposes.

Other execution threads will continue to execute during the
callback so the plugin is responsible for ensuring it doesn’t get
confused by making appropriate use of locking if required.

void qemu_plugin_register_vcpu_mem_inline_per_vcpu(struct qemu_plugin_insn \*insn, enum [qemu_plugin_mem_rw](tcg-plugins.md#c.qemu_plugin_mem_rw "qemu_plugin_mem_rw") rw, enum [qemu_plugin_op](tcg-plugins.md#c.qemu_plugin_op "qemu_plugin_op") op, [qemu_plugin_u64](tcg-plugins.md#c.qemu_plugin_u64 "qemu_plugin_u64") entry, uint64_t imm)
:   inline op for mem access

**Parameters**

`struct qemu_plugin_insn *insn`
:   handle for instruction to instrument

`enum qemu_plugin_mem_rw rw`
:   apply to reads, writes or both

`enum qemu_plugin_op op`
:   the op, of type qemu_plugin_op

`qemu_plugin_u64 entry`
:   entry to run op

`uint64_t imm`
:   immediate data for **op**

**Description**

This registers a inline op every memory access generated by the
instruction.

const void \*qemu_plugin_request_time_control(void)
:   request the ability to control time

**Parameters**

`void`
:   no arguments

**Description**

This grants the plugin the ability to control system time. Only one
plugin can control time so if multiple plugins request the ability
all but the first will fail.

Returns an opaque handle or NULL if fails

void qemu_plugin_update_ns(const void \*handle, int64_t time)
:   update system emulation time

**Parameters**

`const void *handle`
:   opaque handle returned by qemu_plugin_request_time_control()

`int64_t time`
:   time in nanoseconds

**Description**

This allows an appropriately authorised plugin (i.e. holding the
time control handle) to move system time forward to **time**. For
user-mode emulation the time is not changed by this as all reported
time comes from the host kernel.

Start time is 0.

qemu_plugin_vcpu_syscall_cb_t
:   **Typedef**: vCPU syscall callback function type

**Syntax**

> `void qemu_plugin_vcpu_syscall_cb_t (unsigned int vcpu_index, int64_t num, uint64_t a1, uint64_t a2, uint64_t a3, uint64_t a4, uint64_t a5, uint64_t a6, uint64_t a7, uint64_t a8, void *userdata)`

**Parameters**

`unsigned int vcpu_index`
:   the executing vCPU

`int64_t num`
:   the syscall number

`uint64_t a1`
:   the 1st syscall argument

`uint64_t a2`
:   the 2nd syscall argument

`uint64_t a3`
:   the 3rd syscall argument

`uint64_t a4`
:   the 4th syscall argument

`uint64_t a5`
:   the 5th syscall argument

`uint64_t a6`
:   the 6th syscall argument

`uint64_t a7`
:   the 7th syscall argument

`uint64_t a8`
:   the 8th syscall argument

`void *userdata`
:   user data for callback

qemu_plugin_vcpu_syscall_filter_cb_t
:   **Typedef**: vCPU syscall filter callback function type

**Syntax**

> `bool qemu_plugin_vcpu_syscall_filter_cb_t (unsigned int vcpu_index, int64_t num, uint64_t a1, uint64_t a2, uint64_t a3, uint64_t a4, uint64_t a5, uint64_t a6, uint64_t a7, uint64_t a8, int64_t *sysret, void *userdata)`

**Parameters**

`unsigned int vcpu_index`
:   the executing vCPU

`int64_t num`
:   the syscall number

`uint64_t a1`
:   the 1st syscall argument

`uint64_t a2`
:   the 2nd syscall argument

`uint64_t a3`
:   the 3rd syscall argument

`uint64_t a4`
:   the 4th syscall argument

`uint64_t a5`
:   the 5th syscall argument

`uint64_t a6`
:   the 6th syscall argument

`uint64_t a7`
:   the 7th syscall argument

`uint64_t a8`
:   the 8th syscall argument

`int64_t *sysret`
:   reference of the syscall return value, must set this if filtered

`void *userdata`
:   user data for callback

**Description**

Returns true if you want to filter this syscall (i.e. stop it being
handled further), otherwise returns false.

qemu_plugin_vcpu_syscall_ret_cb_t
:   **Typedef**: vCPU syscall return callback function type

**Syntax**

> `void qemu_plugin_vcpu_syscall_ret_cb_t (unsigned int vcpu_index, int64_t num, int64_t ret, void *userdata)`

**Parameters**

`unsigned int vcpu_index`
:   the executing vCPU

`int64_t num`
:   the syscall number

`int64_t ret`
:   the syscall return value

`void *userdata`
:   user data for callback

void qemu_plugin_register_vcpu_syscall_cb([qemu_plugin_id_t](tcg-plugins.md#c.qemu_plugin_id_t "qemu_plugin_id_t") id, [qemu_plugin_vcpu_syscall_cb_t](tcg-plugins.md#c.qemu_plugin_vcpu_syscall_cb_t "qemu_plugin_vcpu_syscall_cb_t") cb, void \*userdata)
:   register a syscall entry callback

**Parameters**

`qemu_plugin_id_t id`
:   plugin id

`qemu_plugin_vcpu_syscall_cb_t cb`
:   callback of type qemu_plugin_vcpu_syscall_cb_t

`void *userdata`
:   user data for callback

**Description**

This registers a callback for every syscall executed by the guest. The **cb**
function is executed before a syscall is handled by the host.

void qemu_plugin_register_vcpu_syscall_filter_cb([qemu_plugin_id_t](tcg-plugins.md#c.qemu_plugin_id_t "qemu_plugin_id_t") id, [qemu_plugin_vcpu_syscall_filter_cb_t](tcg-plugins.md#c.qemu_plugin_vcpu_syscall_filter_cb_t "qemu_plugin_vcpu_syscall_filter_cb_t") cb, void \*userdata)
:   register a syscall filter callback

**Parameters**

`qemu_plugin_id_t id`
:   plugin id

`qemu_plugin_vcpu_syscall_filter_cb_t cb`
:   callback of type qemu_plugin_vcpu_syscall_filter_cb_t

`void *userdata`
:   user data for callback

**Description**

This registers a callback for every syscall executed by the guest. The **cb**
function is executed before a syscall is handled by the host. If the
callback returns true, the syscall is filtered and will not be executed by
the host. The callback must then set the syscall return value via the
corresponding pointer passed to it.

void qemu_plugin_register_vcpu_syscall_ret_cb([qemu_plugin_id_t](tcg-plugins.md#c.qemu_plugin_id_t "qemu_plugin_id_t") id, [qemu_plugin_vcpu_syscall_ret_cb_t](tcg-plugins.md#c.qemu_plugin_vcpu_syscall_ret_cb_t "qemu_plugin_vcpu_syscall_ret_cb_t") cb, void \*userdata)
:   register a syscall entry callback

**Parameters**

`qemu_plugin_id_t id`
:   plugin id

`qemu_plugin_vcpu_syscall_ret_cb_t cb`
:   callback of type qemu_plugin_vcpu_syscall_ret_cb_t

`void *userdata`
:   user data for callback

**Description**

This registers a callback for every syscall executed by the guest. The **cb**
function is executed upon return from the host syscall before execution is
handed back to the guest.

char \*qemu_plugin_insn_disas(const struct qemu_plugin_insn \*insn)
:   return disassembly string for instruction

**Parameters**

`const struct qemu_plugin_insn *insn`
:   instruction reference

**Description**

Returns an allocated string containing the disassembly

const char \*qemu_plugin_insn_symbol(const struct qemu_plugin_insn \*insn)
:   best effort symbol lookup

**Parameters**

`const struct qemu_plugin_insn *insn`
:   instruction reference

**Description**

Return a static string referring to the symbol. This is dependent
on the binary QEMU is running having provided a symbol table.

void qemu_plugin_vcpu_for_each([qemu_plugin_id_t](tcg-plugins.md#c.qemu_plugin_id_t "qemu_plugin_id_t") id, [qemu_plugin_vcpu_udata_cb_t](tcg-plugins.md#c.qemu_plugin_vcpu_udata_cb_t "qemu_plugin_vcpu_udata_cb_t") cb, void \*userdata)
:   iterate over the existing vCPU

**Parameters**

`qemu_plugin_id_t id`
:   plugin ID

`qemu_plugin_vcpu_udata_cb_t cb`
:   callback function

`void *userdata`
:   user data for callback

**Description**

The **cb** function is called once for each existing vCPU.

See also: qemu_plugin_register_vcpu_init_cb()

void qemu_plugin_register_flush_cb([qemu_plugin_id_t](tcg-plugins.md#c.qemu_plugin_id_t "qemu_plugin_id_t") id, [qemu_plugin_udata_cb_t](tcg-plugins.md#c.qemu_plugin_udata_cb_t "qemu_plugin_udata_cb_t") cb, void \*userdata)
:   register code cache flush callback

**Parameters**

`qemu_plugin_id_t id`
:   plugin ID

`qemu_plugin_udata_cb_t cb`
:   callback

`void *userdata`
:   user data for callback

**Description**

The **cb** function is called every time the code cache is flushed.
The callback can be used to free resources associated with existing
translated blocks in a plugin. **cb** is guaranteed to run with all cpus being
stopped, thus no lock is required within it.

void qemu_plugin_register_atexit_cb([qemu_plugin_id_t](tcg-plugins.md#c.qemu_plugin_id_t "qemu_plugin_id_t") id, [qemu_plugin_udata_cb_t](tcg-plugins.md#c.qemu_plugin_udata_cb_t "qemu_plugin_udata_cb_t") cb, void \*userdata)
:   register exit callback

**Parameters**

`qemu_plugin_id_t id`
:   plugin ID

`qemu_plugin_udata_cb_t cb`
:   callback

`void *userdata`
:   user data for callback

**Description**

The **cb** function is called once execution has finished. Plugins
should be able to free all their resources at this point much like
after a reset/uninstall callback is called.

In user-mode it is possible a few un-instrumented instructions from
child threads may run before the host kernel reaps the threads.

void qemu_plugin_outs(const char \*string)
:   output string via QEMU’s logging system

**Parameters**

`const char *string`
:   a string

bool qemu_plugin_bool_parse(const char \*name, const char \*val, bool \*ret)
:   parses a boolean argument in the form of “<argname>=[on|yes|true|off|no|false]”

**Parameters**

`const char *name`
:   argument name, the part before the equals sign

`const char *val`
:   argument value, what’s after the equals sign

`bool *ret`
:   output return value

**Description**

returns true if the combination **name\*\*=\*\*val** parses correctly to a boolean
argument, and false otherwise

const char \*qemu_plugin_path_to_binary(void)
:   path to binary file being executed

**Parameters**

`void`
:   no arguments

**Description**

Return a string representing the path to the binary. For user-mode
this is the main executable. For system emulation we currently
return NULL. The user should g_free() the string once no longer
needed.

uint64_t qemu_plugin_start_code(void)
:   returns start of text segment

**Parameters**

`void`
:   no arguments

**Description**

Returns the nominal start address of the main text segment in
user-mode. Currently returns 0 for system emulation.

uint64_t qemu_plugin_end_code(void)
:   returns end of text segment

**Parameters**

`void`
:   no arguments

**Description**

Returns the nominal end address of the main text segment in
user-mode. Currently returns 0 for system emulation.

uint64_t qemu_plugin_entry_code(void)
:   returns start address for module

**Parameters**

`void`
:   no arguments

**Description**

Returns the nominal entry address of the main text segment in
user-mode. Currently returns 0 for system emulation.

type qemu_plugin_reg_descriptor
:   register descriptions

GArray \*qemu_plugin_get_registers(void)
:   return register list for current vCPU

**Parameters**

`void`
:   no arguments

**Description**

Returns a potentially empty GArray of qemu_plugin_reg_descriptor.
Caller frees the array (but not the const strings).

Should be used from a qemu_plugin_register_vcpu_init_cb() callback
after the vCPU is initialised, i.e. in the vCPU context.

bool qemu_plugin_read_register(struct qemu_plugin_register \*handle, GByteArray \*buf)
:   read register for current vCPU

**Parameters**

`struct qemu_plugin_register *handle`
:   a **qemu_plugin_reg_handle** handle

`GByteArray *buf`
:   A GByteArray for the data owned by the plugin

**Description**

This function is only available in a context that register read access is
explicitly requested via the QEMU_PLUGIN_CB_R_REGS flag, if called inside a
callback that can be registered with a qemu_plugin_cb_flags argument. This
function can also be used in any callback context that does not use a flags
argument, such as in a callback registered with
qemu_plugin_register_vcpu_init_cb(), except for callbacks registered with
qemu_plugin_register_atexit_cb() and qemu_plugin_register_flush_cb().

Returns true on success, false on failure. The content of **buf** is in target
byte order.

bool qemu_plugin_write_register(struct qemu_plugin_register \*handle, GByteArray \*buf)
:   write register for current vCPU

**Parameters**

`struct qemu_plugin_register *handle`
:   a **qemu_plugin_reg_handle** handle

`GByteArray *buf`
:   A GByteArray for the data owned by the plugin

**Description**

This function is only available in a context that register read access is
explicitly requested via the QEMU_PLUGIN_CB_RW_REGS flag, if called inside a
callback that can be registered with a qemu_plugin_cb_flags argument. This
function can also be used in any callback context that does not use a flags
argument, such as in a callback registered with
qemu_plugin_register_vcpu_init_cb(), except for callbacks registered with
qemu_plugin_register_atexit_cb() and qemu_plugin_register_flush_cb().

The size of **buf** must be at least the size of the requested register.
Attempting to write a register with **buf** smaller than the register size
will result in a crash or other undesired behavior.

Returns true on success, false on failure.

void qemu_plugin_set_pc(uint64_t vaddr)
:   set the program counter for the current vCPU

**Parameters**

`uint64_t vaddr`
:   the new virtual (guest) address for the program counter

**Description**

This function sets the program counter for the current vCPU to **vaddr** and
resumes execution at that address. This function does not return.

bool qemu_plugin_read_memory_vaddr(uint64_t addr, GByteArray \*data, size_t len)
:   read from memory using a virtual address

**Parameters**

`uint64_t addr`
:   A virtual address to read from

`GByteArray *data`
:   A byte array to store data into

`size_t len`
:   The number of bytes to read, starting from **addr**

**Description**

**len** bytes of data is read starting at **addr** and stored into **data**. If **data**
is not large enough to hold **len** bytes, it will be expanded to the necessary
size, reallocating if necessary. **len** must be greater than 0.

This function does not ensure writes are flushed prior to reading, so
callers should take care when calling this function in plugin callbacks to
avoid attempting to read data which may not yet be written and should use
the memory callback API instead.

Returns true on success and false on failure.

bool qemu_plugin_write_memory_vaddr(uint64_t addr, GByteArray \*data)
:   write to memory using a virtual address

**Parameters**

`uint64_t addr`
:   A virtual address to write to

`GByteArray *data`
:   A byte array containing the data to write

**Description**

The contents of **data** will be written to memory starting at the virtual
address **addr**.

This function does not guarantee consistency of writes, nor does it ensure
that pending writes are flushed either before or after the write takes place,
so callers should take care to only call this function in vCPU context (i.e.
in callbacks) and avoid depending on the existence of data written using this
function which may be overwritten afterward.

Returns true on success and false on failure.

enum qemu_plugin_hwaddr_operation_result
:   result of a memory operation

**Constants**

`QEMU_PLUGIN_HWADDR_OPERATION_OK`
:   hwaddr operation succeeded

`QEMU_PLUGIN_HWADDR_OPERATION_ERROR`
:   unexpected error occurred

`QEMU_PLUGIN_HWADDR_OPERATION_DEVICE_ERROR`
:   error in memory device

`QEMU_PLUGIN_HWADDR_OPERATION_ACCESS_DENIED`
:   permission error

`QEMU_PLUGIN_HWADDR_OPERATION_INVALID_ADDRESS`
:   address was invalid

`QEMU_PLUGIN_HWADDR_OPERATION_INVALID_ADDRESS_SPACE`
:   invalid address space

enum [qemu_plugin_hwaddr_operation_result](tcg-plugins.md#c.qemu_plugin_hwaddr_operation_result "qemu_plugin_hwaddr_operation_result") qemu_plugin_read_memory_hwaddr(uint64_t addr, GByteArray \*data, size_t len)
:   read from memory using a hardware address

**Parameters**

`uint64_t addr`
:   The physical address to read from

`GByteArray *data`
:   A byte array to store data into

`size_t len`
:   The number of bytes to read, starting from **addr**

**Description**

**len** bytes of data is read from the current memory space for the current
vCPU starting at **addr** and stored into **data**. If **data** is not large enough to
hold **len** bytes, it will be expanded to the necessary size, reallocating if
necessary. **len** must be greater than 0.

This function does not ensure writes are flushed prior to reading, so
callers should take care when calling this function in plugin callbacks to
avoid attempting to read data which may not yet be written and should use
the memory callback API instead.

This function is only valid for softmmu targets.

Returns a qemu_plugin_hwaddr_operation_result indicating the result of the
operation.

enum [qemu_plugin_hwaddr_operation_result](tcg-plugins.md#c.qemu_plugin_hwaddr_operation_result "qemu_plugin_hwaddr_operation_result") qemu_plugin_write_memory_hwaddr(uint64_t addr, GByteArray \*data)
:   write to memory using a hardware address

**Parameters**

`uint64_t addr`
:   A physical address to write to

`GByteArray *data`
:   A byte array containing the data to write

**Description**

The contents of **data** will be written to memory starting at the hardware
address **addr** in the current address space for the current vCPU.

This function does not guarantee consistency of writes, nor does it ensure
that pending writes are flushed either before or after the write takes place,
so callers should take care when calling this function in plugin callbacks to
avoid depending on the existence of data written using this function which
may be overwritten afterward. In addition, this function requires that the
pages containing the address are not locked. Practically, this means that you
should not write instruction memory in a current translation block inside a
callback registered with qemu_plugin_register_vcpu_tb_trans_cb.

You can, for example, write instruction memory in a current translation block
in a callback registered with qemu_plugin_register_vcpu_tb_exec_cb, although
be aware that the write will not be flushed until after the translation block
has finished executing. In general, this function should be used to write
data memory or to patch code at a known address, not in a current translation
block.

This function is only valid for softmmu targets.

Returns a qemu_plugin_hwaddr_operation_result indicating the result of the
operation.

bool qemu_plugin_translate_vaddr(uint64_t vaddr, uint64_t \*hwaddr)
:   translate virtual address for current vCPU

**Parameters**

`uint64_t vaddr`
:   virtual address to translate

`uint64_t *hwaddr`
:   pointer to store the physical address

**Description**

This function is only valid in vCPU context (i.e. in callbacks) and is only
valid for softmmu targets.

Returns true on success and false on failure.

struct qemu_plugin_scoreboard \*qemu_plugin_scoreboard_new(size_t element_size)
:   alloc a new scoreboard

**Parameters**

`size_t element_size`
:   size (in bytes) for one entry

**Description**

Returns a pointer to a new scoreboard. It must be freed using
qemu_plugin_scoreboard_free.

void qemu_plugin_scoreboard_free(struct qemu_plugin_scoreboard \*score)
:   free a scoreboard

**Parameters**

`struct qemu_plugin_scoreboard *score`
:   scoreboard to free

void \*qemu_plugin_scoreboard_find(struct qemu_plugin_scoreboard \*score, unsigned int vcpu_index)
:   get pointer to an entry of a scoreboard

**Parameters**

`struct qemu_plugin_scoreboard *score`
:   scoreboard to query

`unsigned int vcpu_index`
:   entry index

**Description**

Returns address of entry of a scoreboard matching a given vcpu_index. This
address can be modified later if scoreboard is resized.

void qemu_plugin_u64_add([qemu_plugin_u64](tcg-plugins.md#c.qemu_plugin_u64 "qemu_plugin_u64") entry, unsigned int vcpu_index, uint64_t added)
:   add a value to a qemu_plugin_u64 for a given vcpu

**Parameters**

`qemu_plugin_u64 entry`
:   entry to query

`unsigned int vcpu_index`
:   entry index

`uint64_t added`
:   value to add

uint64_t qemu_plugin_u64_get([qemu_plugin_u64](tcg-plugins.md#c.qemu_plugin_u64 "qemu_plugin_u64") entry, unsigned int vcpu_index)
:   get value of a qemu_plugin_u64 for a given vcpu

**Parameters**

`qemu_plugin_u64 entry`
:   entry to query

`unsigned int vcpu_index`
:   entry index

void qemu_plugin_u64_set([qemu_plugin_u64](tcg-plugins.md#c.qemu_plugin_u64 "qemu_plugin_u64") entry, unsigned int vcpu_index, uint64_t val)
:   set value of a qemu_plugin_u64 for a given vcpu

**Parameters**

`qemu_plugin_u64 entry`
:   entry to query

`unsigned int vcpu_index`
:   entry index

`uint64_t val`
:   new value

uint64_t qemu_plugin_u64_sum([qemu_plugin_u64](tcg-plugins.md#c.qemu_plugin_u64 "qemu_plugin_u64") entry)
:   return sum of all vcpu entries in a scoreboard

**Parameters**

`qemu_plugin_u64 entry`
:   entry to sum
