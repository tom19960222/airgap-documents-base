---
collection: python
version: "3.12.14"
title: "syslog — Unix syslog library routines"
source_url: https://docs.python.org/3.12/library/syslog.html
fetched_at: 2026-09-17T15:35:33+00:00
---
# `syslog` — Unix syslog library routines

---

This module provides an interface to the Unix `syslog` library routines.
Refer to the Unix manual pages for a detailed description of the `syslog`
facility.

[Availability](intro.md#availability): Unix, not Emscripten, not WASI.

This module wraps the system `syslog` family of routines. A pure Python
library that can speak to a syslog server is available in the
[`logging.handlers`](logging.handlers.md#module-logging.handlers "logging.handlers: Handlers for the logging module.") module as `SysLogHandler`.

The module defines the following functions:

syslog.syslog(*message*)

syslog.syslog(*priority*, *message*)
:   Send the string *message* to the system logger. A trailing newline is added
    if necessary. Each message is tagged with a priority composed of a
    *facility* and a *level*. The optional *priority* argument, which defaults
    to `LOG_INFO`, determines the message priority. If the facility is
    not encoded in *priority* using logical-or (`LOG_INFO | LOG_USER`), the
    value given in the [`openlog()`](syslog.md#syslog.openlog "syslog.openlog") call is used.

    If [`openlog()`](syslog.md#syslog.openlog "syslog.openlog") has not been called prior to the call to [`syslog()`](syslog.md#module-syslog "syslog: An interface to the Unix syslog library routines. (Unix)"),
    [`openlog()`](syslog.md#syslog.openlog "syslog.openlog") will be called with no arguments.

    Raises an [auditing event](sys.md#auditing) `syslog.syslog` with arguments `priority`, `message`.

    Changed in version 3.2: In previous versions, [`openlog()`](syslog.md#syslog.openlog "syslog.openlog") would not be called automatically if
    it wasn’t called prior to the call to [`syslog()`](syslog.md#module-syslog "syslog: An interface to the Unix syslog library routines. (Unix)"), deferring to the syslog
    implementation to call `openlog()`.

    Changed in version 3.12: This function is restricted in subinterpreters.
    (Only code that runs in multiple interpreters is affected and
    the restriction is not relevant for most users.)
    [`openlog()`](syslog.md#syslog.openlog "syslog.openlog") must be called in the main interpreter before [`syslog()`](syslog.md#module-syslog "syslog: An interface to the Unix syslog library routines. (Unix)") may be used
    in a subinterpreter. Otherwise it will raise [`RuntimeError`](exceptions.md#RuntimeError "RuntimeError").

syslog.openlog([*ident*[, *logoption*[, *facility*]]])
:   Logging options of subsequent [`syslog()`](syslog.md#module-syslog "syslog: An interface to the Unix syslog library routines. (Unix)") calls can be set by calling
    [`openlog()`](syslog.md#syslog.openlog "syslog.openlog"). [`syslog()`](syslog.md#module-syslog "syslog: An interface to the Unix syslog library routines. (Unix)") will call [`openlog()`](syslog.md#syslog.openlog "syslog.openlog") with no arguments
    if the log is not currently open.

    The optional *ident* keyword argument is a string which is prepended to every
    message, and defaults to `sys.argv[0]` with leading path components
    stripped. The optional *logoption* keyword argument (default is 0) is a bit
    field – see below for possible values to combine. The optional *facility*
    keyword argument (default is `LOG_USER`) sets the default facility for
    messages which do not have a facility explicitly encoded.

    Raises an [auditing event](sys.md#auditing) `syslog.openlog` with arguments `ident`, `logoption`, `facility`.

    Changed in version 3.2: In previous versions, keyword arguments were not allowed, and *ident* was
    required.

    Changed in version 3.12: This function is restricted in subinterpreters.
    (Only code that runs in multiple interpreters is affected and
    the restriction is not relevant for most users.)
    This may only be called in the main interpreter.
    It will raise [`RuntimeError`](exceptions.md#RuntimeError "RuntimeError") if called in a subinterpreter.

syslog.closelog()
:   Reset the syslog module values and call the system library `closelog()`.

    This causes the module to behave as it does when initially imported. For
    example, [`openlog()`](syslog.md#syslog.openlog "syslog.openlog") will be called on the first [`syslog()`](syslog.md#module-syslog "syslog: An interface to the Unix syslog library routines. (Unix)") call (if
    [`openlog()`](syslog.md#syslog.openlog "syslog.openlog") hasn’t already been called), and *ident* and other
    [`openlog()`](syslog.md#syslog.openlog "syslog.openlog") parameters are reset to defaults.

    Raises an [auditing event](sys.md#auditing) `syslog.closelog` with no arguments.

    Changed in version 3.12: This function is restricted in subinterpreters.
    (Only code that runs in multiple interpreters is affected and
    the restriction is not relevant for most users.)
    This may only be called in the main interpreter.
    It will raise [`RuntimeError`](exceptions.md#RuntimeError "RuntimeError") if called in a subinterpreter.

syslog.setlogmask(*maskpri*)
:   Set the priority mask to *maskpri* and return the previous mask value. Calls
    to [`syslog()`](syslog.md#module-syslog "syslog: An interface to the Unix syslog library routines. (Unix)") with a priority level not set in *maskpri* are ignored.
    The default is to log all priorities. The function `LOG_MASK(pri)`
    calculates the mask for the individual priority *pri*. The function
    `LOG_UPTO(pri)` calculates the mask for all priorities up to and including
    *pri*.

    Raises an [auditing event](sys.md#auditing) `syslog.setlogmask` with argument `maskpri`.

The module defines the following constants:

Priority levels (high to low):
:   `LOG_EMERG`, `LOG_ALERT`, `LOG_CRIT`, `LOG_ERR`,
    `LOG_WARNING`, `LOG_NOTICE`, `LOG_INFO`,
    `LOG_DEBUG`.

Facilities:
:   `LOG_KERN`, `LOG_USER`, `LOG_MAIL`, `LOG_DAEMON`,
    `LOG_AUTH`, `LOG_LPR`, `LOG_NEWS`, `LOG_UUCP`,
    `LOG_CRON`, `LOG_SYSLOG`, `LOG_LOCAL0` to
    `LOG_LOCAL7`, and, if defined in `<syslog.h>`,
    `LOG_AUTHPRIV`.

Log options:
:   `LOG_PID`, `LOG_CONS`, `LOG_NDELAY`, and, if defined
    in `<syslog.h>`, `LOG_ODELAY`, `LOG_NOWAIT`, and
    `LOG_PERROR`.

## Examples

### Simple example

A simple set of examples:

```python3
import syslog

syslog.syslog('Processing started')
if error:
    syslog.syslog(syslog.LOG_ERR, 'Processing started')
```

An example of setting some log options, these would include the process ID in
logged messages, and write the messages to the destination facility used for
mail logging:

```python3
syslog.openlog(logoption=syslog.LOG_PID, facility=syslog.LOG_MAIL)
syslog.syslog('E-mail processing initiated...')
```
