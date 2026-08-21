---
collection: kernel
version: "6.8"
title: "Message logging with printk"
source_url: https://www.kernel.org/doc/html/v6.8/core-api/printk-basics.html
fetched_at: 2026-08-21T03:29:53+00:00
---
English

- [Chinese (Simplified)](../translations/zh_CN/core-api/printk-basics.md)

# Message logging with printk

[`printk()`](printk-basics.md#c.printk "printk") is one of the most widely known functions in the Linux kernel. It's the
standard tool we have for printing messages and usually the most basic way of
tracing and debugging. If you're familiar with printf(3) you can tell [`printk()`](printk-basics.md#c.printk "printk")
is based on it, although it has some functional differences:

> - [`printk()`](printk-basics.md#c.printk "printk") messages can specify a log level.
> - the format string, while largely compatible with C99, doesn't follow the
>   exact same specification. It has some extensions and a few limitations
>   (no `%n` or floating point conversion specifiers). See [How to get
>   printk format specifiers right](printk-formats.md#printk-specifiers).

All [`printk()`](printk-basics.md#c.printk "printk") messages are printed to the kernel log buffer, which is a ring
buffer exported to userspace through /dev/kmsg. The usual way to read it is
using `dmesg`.

[`printk()`](printk-basics.md#c.printk "printk") is typically used like this:

```
printk(KERN_INFO "Message: %s\n", arg);
```

where `KERN_INFO` is the log level (note that it's concatenated to the format
string, the log level is not a separate argument). The available log levels are:

| Name | String | Alias function |
| --- | --- | --- |
| KERN_EMERG | "0" | [`pr_emerg()`](printk-basics.md#c.pr_emerg "pr_emerg") |
| KERN_ALERT | "1" | [`pr_alert()`](printk-basics.md#c.pr_alert "pr_alert") |
| KERN_CRIT | "2" | [`pr_crit()`](printk-basics.md#c.pr_crit "pr_crit") |
| KERN_ERR | "3" | [`pr_err()`](printk-basics.md#c.pr_err "pr_err") |
| KERN_WARNING | "4" | [`pr_warn()`](printk-basics.md#c.pr_warn "pr_warn") |
| KERN_NOTICE | "5" | [`pr_notice()`](printk-basics.md#c.pr_notice "pr_notice") |
| KERN_INFO | "6" | [`pr_info()`](printk-basics.md#c.pr_info "pr_info") |
| KERN_DEBUG | "7" | [`pr_debug()`](printk-basics.md#c.pr_debug "pr_debug") and [`pr_devel()`](printk-basics.md#c.pr_devel "pr_devel") if DEBUG is defined |
| KERN_DEFAULT | "" |  |
| KERN_CONT | "c" | [`pr_cont()`](printk-basics.md#c.pr_cont "pr_cont") |

The log level specifies the importance of a message. The kernel decides whether
to show the message immediately (printing it to the current console) depending
on its log level and the current *console_loglevel* (a kernel variable). If the
message priority is higher (lower log level value) than the *console_loglevel*
the message will be printed to the console.

If the log level is omitted, the message is printed with `KERN_DEFAULT`
level.

You can check the current *console_loglevel* with:

```
$ cat /proc/sys/kernel/printk
4        4        1        7
```

The result shows the *current*, *default*, *minimum* and *boot-time-default* log
levels.

To change the current console_loglevel simply write the desired level to
`/proc/sys/kernel/printk`. For example, to print all messages to the console:

```
# echo 8 > /proc/sys/kernel/printk
```

Another way, using `dmesg`:

```
# dmesg -n 5
```

sets the console_loglevel to print KERN_WARNING (4) or more severe messages to
console. See `dmesg(1)` for more information.

As an alternative to [`printk()`](printk-basics.md#c.printk "printk") you can use the `pr_*()` aliases for
logging. This family of macros embed the log level in the macro names. For
example:

```
pr_info("Info message no. %d\n", msg_num);
```

prints a `KERN_INFO` message.

Besides being more concise than the equivalent [`printk()`](printk-basics.md#c.printk "printk") calls, they can use a
common definition for the format string through the [`pr_fmt()`](printk-basics.md#c.pr_fmt "pr_fmt") macro. For
instance, defining this at the top of a source file (before any `#include`
directive):

```
#define pr_fmt(fmt) "%s:%s: " fmt, KBUILD_MODNAME, __func__
```

would prefix every pr_\*() message in that file with the module and function name
that originated the message.

For debugging purposes there are also two conditionally-compiled macros:
[`pr_debug()`](printk-basics.md#c.pr_debug "pr_debug") and [`pr_devel()`](printk-basics.md#c.pr_devel "pr_devel"), which are compiled-out unless `DEBUG` (or
also `CONFIG_DYNAMIC_DEBUG` in the case of [`pr_debug()`](printk-basics.md#c.pr_debug "pr_debug")) is defined.

## Function reference

pr_fmt

`pr_fmt (fmt)`

> used by the pr_\*() macros to generate the printk format string

**Parameters**

`fmt`
:   format string passed from a pr_\*() macro

**Description**

This macro can be used to generate a unified format string for pr_\*()
macros. A common use is to prefix all pr_\*() messages in a file with a common
string. For example, defining this at the top of a source file:

> #define pr_fmt(fmt) KBUILD_MODNAME ": " fmt

would prefix all pr_info, pr_emerg... messages in the file with the module
name.

printk

`printk (fmt, ...)`

> print a kernel message

**Parameters**

`fmt`
:   format string

`...`
:   variable arguments

**Description**

This is [`printk()`](printk-basics.md#c.printk "printk"). It can be called from any context. We want it to work.

If printk indexing is enabled, _printk() is called from printk_index_wrap.
Otherwise, printk is simply #defined to _printk.

We try to grab the console_lock. If we succeed, it's easy - we log the
output and call the console drivers. If we fail to get the semaphore, we
place the output into the log buffer and return. The current holder of
the console_sem will notice the new output in [`console_unlock()`](../driver-api/basics.md#c.console_unlock "console_unlock"); and will
send it to the consoles before releasing the lock.

One effect of this deferred printing is that code which calls [`printk()`](printk-basics.md#c.printk "printk") and
then changes console_loglevel may break. This is because console_loglevel
is inspected when the actual printing occurs.

See also:
printf(3)

See the [`vsnprintf()`](kernel-api.md#c.vsnprintf "vsnprintf") documentation for format string extensions over C99.

pr_emerg

`pr_emerg (fmt, ...)`

> Print an emergency-level message

**Parameters**

`fmt`
:   format string

`...`
:   arguments for the format string

**Description**

This macro expands to a printk with KERN_EMERG loglevel. It uses [`pr_fmt()`](printk-basics.md#c.pr_fmt "pr_fmt") to
generate the format string.

pr_alert

`pr_alert (fmt, ...)`

> Print an alert-level message

**Parameters**

`fmt`
:   format string

`...`
:   arguments for the format string

**Description**

This macro expands to a printk with KERN_ALERT loglevel. It uses [`pr_fmt()`](printk-basics.md#c.pr_fmt "pr_fmt") to
generate the format string.

pr_crit

`pr_crit (fmt, ...)`

> Print a critical-level message

**Parameters**

`fmt`
:   format string

`...`
:   arguments for the format string

**Description**

This macro expands to a printk with KERN_CRIT loglevel. It uses [`pr_fmt()`](printk-basics.md#c.pr_fmt "pr_fmt") to
generate the format string.

pr_err

`pr_err (fmt, ...)`

> Print an error-level message

**Parameters**

`fmt`
:   format string

`...`
:   arguments for the format string

**Description**

This macro expands to a printk with KERN_ERR loglevel. It uses [`pr_fmt()`](printk-basics.md#c.pr_fmt "pr_fmt") to
generate the format string.

pr_warn

`pr_warn (fmt, ...)`

> Print a warning-level message

**Parameters**

`fmt`
:   format string

`...`
:   arguments for the format string

**Description**

This macro expands to a printk with KERN_WARNING loglevel. It uses [`pr_fmt()`](printk-basics.md#c.pr_fmt "pr_fmt")
to generate the format string.

pr_notice

`pr_notice (fmt, ...)`

> Print a notice-level message

**Parameters**

`fmt`
:   format string

`...`
:   arguments for the format string

**Description**

This macro expands to a printk with KERN_NOTICE loglevel. It uses [`pr_fmt()`](printk-basics.md#c.pr_fmt "pr_fmt") to
generate the format string.

pr_info

`pr_info (fmt, ...)`

> Print an info-level message

**Parameters**

`fmt`
:   format string

`...`
:   arguments for the format string

**Description**

This macro expands to a printk with KERN_INFO loglevel. It uses [`pr_fmt()`](printk-basics.md#c.pr_fmt "pr_fmt") to
generate the format string.

pr_cont

`pr_cont (fmt, ...)`

> Continues a previous log message in the same line.

**Parameters**

`fmt`
:   format string

`...`
:   arguments for the format string

**Description**

This macro expands to a printk with KERN_CONT loglevel. It should only be
used when continuing a log message with no newline ('n') enclosed. Otherwise
it defaults back to KERN_DEFAULT loglevel.

pr_devel

`pr_devel (fmt, ...)`

> Print a debug-level message conditionally

**Parameters**

`fmt`
:   format string

`...`
:   arguments for the format string

**Description**

This macro expands to a printk with KERN_DEBUG loglevel if DEBUG is
defined. Otherwise it does nothing.

It uses [`pr_fmt()`](printk-basics.md#c.pr_fmt "pr_fmt") to generate the format string.

pr_debug

`pr_debug (fmt, ...)`

> Print a debug-level message conditionally

**Parameters**

`fmt`
:   format string

`...`
:   arguments for the format string

**Description**

This macro expands to dynamic_pr_debug() if CONFIG_DYNAMIC_DEBUG is
set. Otherwise, if DEBUG is defined, it's equivalent to a printk with
KERN_DEBUG loglevel. If DEBUG is not defined it does nothing.

It uses [`pr_fmt()`](printk-basics.md#c.pr_fmt "pr_fmt") to generate the format string (dynamic_pr_debug() uses
[`pr_fmt()`](printk-basics.md#c.pr_fmt "pr_fmt") internally).
